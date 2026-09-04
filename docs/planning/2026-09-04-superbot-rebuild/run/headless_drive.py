#!/usr/bin/env python3
"""Headless boot + in-process drive of ``superbot-next`` — the instrument
behind ``run/boot-observation.md`` (verdict gap 1).

WHAT IS REAL in this run
  * the composition root ``sb.app.main.run_app()`` executed END TO END —
    preflight, the K0 installs, boot-gate legs A and B, ``db.init`` with the
    migration chain on a real (throwaway, local) PostgreSQL 16, the health
    server, the live manifests, the dispatch index, the panel registry and
    engine, the discord.py ``commands.Bot`` with its app-command tree, the
    component feed, the test-guild effect ports, the poll supervisor, the
    subscribe rosters, the boot hooks and the boot canary;
  * every interaction goes through the real spine: discord.py ``Interaction``
    → the command tree / component feed → ``resolve()`` → the panel engine →
    the PRODUCTION ``DiscordPanelPresenter`` → discord.py's
    ``InteractionResponse`` / ``Webhook`` → the wire payload.

WHAT IS SYNTHETIC
  * the transport: ``connect_gateway`` is replaced by a stub (no token is
    read, no socket is opened), and every HTTP call discord.py would make is
    answered by an in-process fake that records the wire payload and mints
    message ids;
  * the guild: one guild (channels, roles, three members) injected into the
    client cache; the actor is that guild's owner unless stated otherwise;
  * the interactions: INTERACTION_CREATE payloads built by the walker from
    the recorded messages (a click carries the exact custom_id the presenter
    put on the wire).

WHAT IS NOT OBSERVED
  Anything Discord itself does: rate limits, permission errors, the remote
  command set, real rendering. A real-guild drive (R4) is still owed.

Population contract (08-verification.md § 1): EXPECTED is the panel-id set of
the COMMITTED ``manifest.snapshot.json``, read independently of the engine;
ACTUAL is the set of panel ids the presenter was asked to present. The run
reports both directions of the difference and never asserts a floor alone.

usage:
  <venv>/bin/python headless_drive.py --repo /home/user/superbot-next \
      --dsn postgresql://superbot@127.0.0.1:54329/superbot --out result.json
"""
from __future__ import annotations

import argparse
import asyncio
import collections
import datetime as dt
import itertools
import json
import logging
import os
import re
import signal
import sys
import time

# --------------------------------------------------------------------------
# synthetic world constants (all ids are outside any real snowflake range in use)
# --------------------------------------------------------------------------
TEST_APP_ID = 1298426054636994611      # the estate's recorded TEST app id (Galaxy Bot)
GUILD_ID = 900000000000000000
OWNER_ID = 900000000000000001
ADMIN_ID = 900000000000000002
MEMBER_ID = 900000000000000003
ROLE_EVERYONE = GUILD_ID
ROLE_ADMIN = 900000000000000010
ROLE_MEMBER = 900000000000000011
CH_GENERAL = 900000000000000100
CH_MODLOGS = 900000000000000101
CH_WELCOME = 900000000000000102
CH_BOTCMDS = 900000000000000103
CH_STAFF = 900000000000000104
HEALTH_PORT = 18080

_snowflake = itertools.count(910000000000000000)


def snowflake() -> int:
    return next(_snowflake)


def now_iso() -> str:
    return dt.datetime.now(tz=dt.timezone.utc).isoformat()


# --------------------------------------------------------------------------
# recorder — every wire payload the bot tried to send, and the minted messages
# --------------------------------------------------------------------------
class Recorder:
    def __init__(self) -> None:
        self.events: list[dict] = []          # every outbound call, in order
        self.messages: dict[int, dict] = {}   # message id -> current payload
        self.by_interaction: dict[int, list[dict]] = collections.defaultdict(list)
        self.http_calls: collections.Counter = collections.Counter()
        self.unhandled_http: list[str] = []

    def bot_user_payload(self) -> dict:
        return {"id": str(TEST_APP_ID), "username": "headless-test-bot",
                "discriminator": "0", "avatar": None, "bot": True,
                "global_name": "headless-test-bot"}

    def mint_message(self, *, channel_id: int, data: dict, flags: int = 0,
                     interaction_id: int | None = None) -> dict:
        mid = snowflake()
        payload = {
            "id": str(mid), "channel_id": str(channel_id),
            "guild_id": str(GUILD_ID),
            "author": self.bot_user_payload(),
            "content": data.get("content") or "",
            "timestamp": now_iso(), "edited_timestamp": None,
            "tts": bool(data.get("tts", False)), "mention_everyone": False,
            "mentions": [], "mention_roles": [], "attachments": [],
            "embeds": list(data.get("embeds") or []),
            "components": list(data.get("components") or []),
            "pinned": False, "type": 0,
            "flags": int(data.get("flags") or flags or 0),
        }
        if interaction_id is not None:
            payload["interaction_metadata"] = {
                "id": str(interaction_id), "type": 2,
                "user": {"id": str(OWNER_ID), "username": "owner",
                         "discriminator": "0", "avatar": None},
                "authorizing_integration_owners": {"0": str(GUILD_ID)},
            }
        self.messages[mid] = payload
        return payload

    def apply_edit(self, mid: int, data: dict) -> dict:
        payload = self.messages.get(mid)
        if payload is None:
            payload = self.mint_message(channel_id=CH_GENERAL, data=data)
            mid = int(payload["id"])
        for key in ("content", "embeds", "components", "flags"):
            if key in data and data[key] is not None:
                payload[key] = data[key]
        payload["edited_timestamp"] = now_iso()
        return payload

    def record(self, kind: str, **fields) -> None:
        fields["kind"] = kind
        fields["seq"] = len(self.events)
        self.events.append(fields)
        iid = fields.get("interaction_id")
        if iid is not None:
            self.by_interaction[int(iid)].append(fields)


REC = Recorder()


def _payload_from_params(params) -> dict:
    payload = getattr(params, "payload", None)
    if payload is None:
        multipart = getattr(params, "multipart", None) or []
        for part in multipart:
            if part.get("name") == "payload_json":
                payload = json.loads(part["value"])
                break
    return payload or {}


class FakeWebhookAdapter:
    """Answers discord.py's interaction/webhook adapter calls in-process."""

    async def create_interaction_response(self, interaction_id, token, *, session=None,
                                          proxy=None, proxy_auth=None, params=None):
        payload = _payload_from_params(params)
        rtype = int(payload.get("type", 0))
        data = payload.get("data") or {}
        resource = None
        message = None
        if rtype in (4, 7):
            channel_id = INTERACTIONS.channel_of(int(interaction_id))
            if rtype == 7:
                mid = INTERACTIONS.message_of(int(interaction_id))
                message = REC.apply_edit(mid, data) if mid else REC.mint_message(
                    channel_id=channel_id, data=data, interaction_id=int(interaction_id))
            else:
                message = REC.mint_message(channel_id=channel_id, data=data,
                                           interaction_id=int(interaction_id))
            resource = {"type": rtype, "message": message}
            INTERACTIONS.set_original(int(interaction_id), int(message["id"]))
        REC.record("interaction_response", interaction_id=int(interaction_id),
                   response_type=rtype, data=data,
                   message_id=int(message["id"]) if message else None)
        out = {"interaction": {"id": str(interaction_id), "type": 2,
                               "response_message_id": message["id"] if message else None,
                               "response_message_loading": rtype in (5,),
                               "response_message_ephemeral": bool(int(data.get("flags") or 0) & 64)}}
        if resource is not None:
            out["resource"] = resource
        return out

    async def get_original_interaction_response(self, application_id, token, *, session=None,
                                                proxy=None, proxy_auth=None):
        iid = INTERACTIONS.interaction_for_token(token)
        mid = INTERACTIONS.original_of(iid)
        if mid is None:
            # a deferred interaction with no visible message yet: mint an empty one
            payload = REC.mint_message(channel_id=INTERACTIONS.channel_of(iid), data={},
                                       interaction_id=iid)
            INTERACTIONS.set_original(iid, int(payload["id"]))
            return payload
        return REC.messages[mid]

    async def edit_original_interaction_response(self, application_id, token, *, session=None,
                                                 proxy=None, proxy_auth=None, payload=None,
                                                 multipart=None, files=None):
        iid = INTERACTIONS.interaction_for_token(token)
        data = payload if payload is not None else _payload_from_params(
            type("P", (), {"payload": None, "multipart": multipart})())
        mid = INTERACTIONS.original_of(iid)
        if mid is None:
            message = REC.mint_message(channel_id=INTERACTIONS.channel_of(iid), data=data,
                                       interaction_id=iid)
            INTERACTIONS.set_original(iid, int(message["id"]))
        else:
            message = REC.apply_edit(mid, data)
        REC.record("edit_original", interaction_id=iid, data=data,
                   message_id=int(message["id"]))
        return message

    async def delete_original_interaction_response(self, application_id, token, *, session=None,
                                                   proxy=None, proxy_auth=None):
        iid = INTERACTIONS.interaction_for_token(token)
        REC.record("delete_original", interaction_id=iid)
        return None

    async def execute_webhook(self, webhook_id, token, *, session=None, proxy=None,
                              proxy_auth=None, payload=None, multipart=None, files=None,
                              thread_id=None, wait=False, with_components=False):
        iid = INTERACTIONS.interaction_for_token(token)
        data = payload if payload is not None else _payload_from_params(
            type("P", (), {"payload": None, "multipart": multipart})())
        message = REC.mint_message(channel_id=INTERACTIONS.channel_of(iid), data=data,
                                   interaction_id=iid)
        REC.record("followup", interaction_id=iid, data=data,
                   message_id=int(message["id"]))
        return message

    async def get_webhook_message(self, webhook_id, token, message_id, *, session=None,
                                  proxy=None, proxy_auth=None, thread_id=None):
        return REC.messages[int(message_id)]

    async def edit_webhook_message(self, webhook_id, token, message_id, *, session=None,
                                   proxy=None, proxy_auth=None, payload=None, multipart=None,
                                   files=None, thread_id=None, with_components=False):
        iid = INTERACTIONS.interaction_for_token(token)
        data = payload if payload is not None else _payload_from_params(
            type("P", (), {"payload": None, "multipart": multipart})())
        message = REC.apply_edit(int(message_id), data)
        REC.record("edit_followup", interaction_id=iid, data=data,
                   message_id=int(message_id))
        return message

    async def delete_webhook_message(self, webhook_id, token, message_id, *, session=None,
                                     proxy=None, proxy_auth=None, thread_id=None):
        REC.record("delete_followup", message_id=int(message_id))
        return None


class InteractionLedger:
    """interaction id -> (token, channel, hosting message, original response)."""

    def __init__(self) -> None:
        self.tokens: dict[str, int] = {}
        self.channels: dict[int, int] = {}
        self.messages: dict[int, int | None] = {}
        self.originals: dict[int, int] = {}

    def open(self, *, channel_id: int, message_id: int | None) -> tuple[int, str]:
        iid = snowflake()
        token = f"headless-{iid}"
        self.tokens[token] = iid
        self.channels[iid] = channel_id
        self.messages[iid] = message_id
        return iid, token

    def interaction_for_token(self, token: str) -> int:
        return self.tokens.get(str(token), 0)

    def channel_of(self, iid: int) -> int:
        return self.channels.get(iid, CH_GENERAL)

    def message_of(self, iid: int) -> int | None:
        return self.messages.get(iid)

    def set_original(self, iid: int, mid: int) -> None:
        self.originals.setdefault(iid, mid)

    def original_of(self, iid: int) -> int | None:
        return self.originals.get(iid)


INTERACTIONS = InteractionLedger()


# --------------------------------------------------------------------------
# the fake REST transport under discord.py's HTTPClient.request
# --------------------------------------------------------------------------
def _ids_from_route(route) -> dict:
    """Recover the path parameters from the built URL against the template."""
    template = route.path
    url = route.url
    base_idx = url.find("/api/v")
    path = url[url.find("/", base_idx + 5):] if base_idx >= 0 else url
    pattern = re.sub(r"\{([a-z_]+)\}", r"(?P<\1>[^/]+)", template)
    m = re.fullmatch(pattern, path)
    return {k: v for k, v in (m.groupdict().items() if m else [])}


def install_fake_http(bot, guild_state):
    import discord

    http = bot.http

    class _Resp:
        def __init__(self, status, reason):
            self.status, self.reason = status, reason

    async def fake_request(route, *, files=None, form=None, **kwargs):
        method, path = route.method, route.path
        key = f"{method} {path}"
        REC.http_calls[key] += 1
        ids = _ids_from_route(route)
        payload = kwargs.get("json")
        if method == "POST" and path == "/channels/{channel_id}/messages":
            channel_id = int(ids.get("channel_id", CH_GENERAL))
            message = REC.mint_message(channel_id=channel_id, data=payload or {})
            REC.record("channel_send", channel_id=channel_id, data=payload or {},
                       message_id=int(message["id"]))
            return message
        if method == "PATCH" and path == "/channels/{channel_id}/messages/{message_id}":
            mid = int(ids["message_id"])
            message = REC.apply_edit(mid, payload or {})
            REC.record("message_edit", message_id=mid, data=payload or {})
            return message
        if method == "GET" and path == "/channels/{channel_id}/messages/{message_id}":
            mid = int(ids["message_id"])
            if mid in REC.messages:
                return REC.messages[mid]
            raise discord.NotFound(_Resp(404, "Not Found"), {"code": 10008, "message": "Unknown Message"})
        if method == "DELETE" and path.startswith("/channels/{channel_id}/messages"):
            REC.record("message_delete", ids=ids)
            return None
        if path.startswith("/channels/{channel_id}/messages/{message_id}/reactions"):
            REC.record("reaction", method=method, ids=ids)
            return None
        if method == "GET" and path == "/channels/{channel_id}":
            ch = guild_state["guild"].get_channel(int(ids["channel_id"]))
            if ch is None:
                raise discord.NotFound(_Resp(404, "Not Found"), {"code": 10003, "message": "Unknown Channel"})
            return channel_payload(ch.id, ch.name, position=ch.position)
        if method == "POST" and path == "/guilds/{guild_id}/channels":
            cid = snowflake()
            name = (payload or {}).get("name", "new-channel")
            data = channel_payload(cid, name, position=len(guild_state["guild"].channels),
                                   overwrites=(payload or {}).get("permission_overwrites") or [])
            guild = guild_state["guild"]
            channel = discord.TextChannel(state=bot._connection, guild=guild, data=data)
            guild._add_channel(channel)
            REC.record("channel_create", channel_id=cid, name=name, data=payload or {})
            return data
        if method == "PATCH" and path == "/channels/{channel_id}":
            REC.record("channel_edit", ids=ids, data=payload or {})
            ch = guild_state["guild"].get_channel(int(ids["channel_id"]))
            return channel_payload(ch.id, (payload or {}).get("name", ch.name), position=ch.position)
        if method == "PUT" and path == "/applications/{application_id}/guilds/{guild_id}/commands":
            out = []
            for cmd in payload or []:
                cmd = dict(cmd)
                cmd["id"] = str(snowflake())
                cmd["application_id"] = ids.get("application_id")
                cmd["guild_id"] = ids.get("guild_id")
                cmd["version"] = "1"
                out.append(cmd)
            REC.record("guild_command_sync", count=len(out), names=sorted(c["name"] for c in out))
            return out
        if method == "GET" and path == "/applications/{application_id}/commands":
            # the REMOTE global set cannot be observed headless — refuse loudly
            raise discord.HTTPException(_Resp(503, "headless: remote command set not observable"),
                                        {"message": "headless"})
        if method == "POST" and path == "/guilds/{guild_id}/roles":
            rid = snowflake()
            data = role_payload(rid, (payload or {}).get("name", "new-role"),
                                (payload or {}).get("permissions", "0"))
            guild = guild_state["guild"]
            guild._add_role(discord.Role(guild=guild, state=bot._connection, data=data))
            REC.record("role_create", role_id=rid, data=payload or {})
            return data
        if "/members/{user_id}/roles/{role_id}" in path:
            REC.record("member_role", method=method, ids=ids)
            return None
        if method == "POST" and path == "/channels/{channel_id}/invites":
            REC.record("invite_create", ids=ids, data=payload or {})
            return {"code": "headless0", "guild": {"id": str(GUILD_ID), "name": "Headless Test Guild"},
                    "channel": {"id": ids.get("channel_id"), "name": "general", "type": 0},
                    "inviter": REC.bot_user_payload(), "max_age": 0, "max_uses": 0,
                    "temporary": False, "created_at": now_iso(), "uses": 0}
        if method == "GET" and path == "/guilds/{guild_id}/members/{member_id}":
            uid = int(ids["member_id"])
            if uid in MEMBERS:
                REC.record("member_fetch", user_id=uid)
                return MEMBERS[uid]
            raise discord.NotFound(_Resp(404, "Not Found"), {"code": 10007, "message": "Unknown Member"})
        if method == "GET" and path == "/guilds/{guild_id}/channels":
            return [channel_payload(c.id, c.name, position=c.position)
                    for c in guild_state["guild"].text_channels]
        if method == "PUT" and path == "/channels/{channel_id}/permissions/{target}":
            REC.record("channel_permissions", ids=ids, data=payload or {})
            return None
        if method == "DELETE" and path == "/channels/{channel_id}":
            REC.record("channel_delete", ids=ids)
            ch = guild_state["guild"].get_channel(int(ids["channel_id"]))
            if ch is not None:
                guild_state["guild"]._remove_channel(ch)
            return channel_payload(int(ids["channel_id"]), getattr(ch, "name", "deleted"))
        REC.unhandled_http.append(key)
        REC.record("http_unhandled", method=method, path=path, ids=ids, data=payload)
        raise discord.HTTPException(_Resp(503, f"headless: no fake for {key}"), {"message": key})

    http.request = fake_request  # instance attribute shadows the method


# --------------------------------------------------------------------------
# synthetic guild payloads
# --------------------------------------------------------------------------
def role_payload(rid: int, name: str, permissions: str, position: int = 1) -> dict:
    return {"id": str(rid), "name": name, "permissions": str(permissions),
            "position": position, "color": 0, "hoist": False, "managed": False,
            "mentionable": False, "flags": 0}


def channel_payload(cid: int, name: str, *, position: int = 0, overwrites=None) -> dict:
    return {"id": str(cid), "type": 0, "name": name, "position": position,
            "guild_id": str(GUILD_ID), "permission_overwrites": overwrites or [],
            "nsfw": False, "parent_id": None, "topic": None,
            "rate_limit_per_user": 0, "last_message_id": None}


def user_payload(uid: int, name: str, *, bot: bool = False) -> dict:
    out = {"id": str(uid), "username": name, "discriminator": "0", "avatar": None,
           "global_name": name}
    if bot:
        out["bot"] = True
    return out


def member_payload(uid: int, name: str, roles: list[int], permissions: int,
                   *, bot: bool = False) -> dict:
    return {"user": user_payload(uid, name, bot=bot), "roles": [str(r) for r in roles],
            "joined_at": "2026-09-04T00:00:00+00:00", "deaf": False, "mute": False,
            "flags": 0, "permissions": str(permissions), "nick": None,
            "premium_since": None, "pending": False}


MEMBERS: dict[int, dict] = {}   # uid -> member payload (filled by guild_payload)


def guild_payload(all_perms: int, none_perms: int) -> dict:
    return {
        "id": str(GUILD_ID), "name": "Headless Test Guild", "owner_id": str(OWNER_ID),
        "member_count": 3, "verification_level": 0, "default_message_notifications": 0,
        "explicit_content_filter": 0, "afk_timeout": 300, "icon": None, "banner": None,
        "features": [], "system_channel_id": str(CH_GENERAL),
        "preferred_locale": "en-US", "nsfw_level": 0, "mfa_level": 0, "premium_tier": 0,
        "roles": [
            role_payload(ROLE_EVERYONE, "@everyone", str(none_perms), 0),
            role_payload(ROLE_MEMBER, "Member", str(none_perms), 1),
            role_payload(ROLE_ADMIN, "Admin", str(all_perms), 2),
        ],
        "channels": [
            channel_payload(CH_GENERAL, "general", position=0),
            channel_payload(CH_MODLOGS, "mod-logs", position=1),
            channel_payload(CH_WELCOME, "welcome", position=2),
            channel_payload(CH_BOTCMDS, "bot-commands", position=3),
            channel_payload(CH_STAFF, "staff", position=4),
        ],
        "members": [
            member_payload(OWNER_ID, "owner", [], all_perms),
            member_payload(ADMIN_ID, "admin", [ROLE_ADMIN], all_perms),
            member_payload(MEMBER_ID, "member", [ROLE_MEMBER], none_perms),
            # the bot itself is a member of every guild it is in (guild.me)
            member_payload(TEST_APP_ID, "headless-test-bot", [ROLE_ADMIN], all_perms, bot=True),
        ],
    }


def _index_members(payload: dict) -> None:
    for m in payload["members"]:
        MEMBERS[int(m["user"]["id"])] = m


# --------------------------------------------------------------------------
# interaction payloads
# --------------------------------------------------------------------------
class Actor:
    def __init__(self, uid: int, name: str, roles: list[int], permissions: int) -> None:
        self.uid, self.name, self.roles, self.permissions = uid, name, roles, permissions

    def member(self) -> dict:
        return member_payload(self.uid, self.name, self.roles, self.permissions)


def base_interaction(actor: Actor, *, channel_id: int, itype: int, data: dict,
                     message: dict | None = None) -> dict:
    iid, token = INTERACTIONS.open(channel_id=channel_id,
                                   message_id=int(message["id"]) if message else None)
    payload = {
        "id": str(iid), "application_id": str(TEST_APP_ID), "type": itype,
        "data": data, "guild_id": str(GUILD_ID),
        "channel": channel_payload(channel_id, "general"),
        "channel_id": str(channel_id),
        "member": actor.member(), "token": token, "version": 1,
        "app_permissions": str((1 << 41) - 1), "locale": "en-US", "guild_locale": "en-US",
        "entitlements": [], "authorizing_integration_owners": {"0": str(GUILD_ID)},
        "context": 0, "attachment_size_limit": 26214400,
    }
    if message is not None:
        payload["message"] = message
    return payload


def slash_payload(actor: Actor, name: str, *, channel_id: int = CH_GENERAL,
                  subcommands: list[str] | None = None) -> dict:
    data = {"id": str(snowflake()), "name": name, "type": 1, "options": []}
    if subcommands:
        node = data
        for i, sub in enumerate(subcommands):
            opt = {"name": sub, "type": 1 if i == len(subcommands) - 1 else 2, "options": []}
            node["options"] = [opt]
            node = opt
    return base_interaction(actor, channel_id=channel_id, itype=2, data=data)


def component_payload(actor: Actor, message: dict, custom_id: str, component_type: int,
                      values: list[str] | None = None) -> dict:
    data = {"custom_id": custom_id, "component_type": component_type}
    if values is not None:
        data["values"] = list(values)
    return base_interaction(actor, channel_id=int(message["channel_id"]), itype=3,
                            data=data, message=message)


def modal_payload(actor: Actor, message: dict | None, custom_id: str, fields: dict) -> dict:
    rows = [{"type": 1, "components": [{"type": 4, "custom_id": k, "value": v}]}
            for k, v in fields.items()]
    data = {"custom_id": custom_id, "components": rows}
    return base_interaction(actor, channel_id=int(message["channel_id"]) if message else CH_GENERAL,
                            itype=5, data=data, message=message)


def wire_components(message: dict) -> list[dict]:
    """Flatten the action rows of a recorded message into clickable controls."""
    out = []
    for row in message.get("components") or []:
        for comp in row.get("components") or []:
            ctype = int(comp.get("type", 0))
            if ctype == 2 and comp.get("url"):
                out.append({"type": ctype, "custom_id": None, "label": comp.get("label"),
                            "url": comp["url"], "disabled": bool(comp.get("disabled"))})
            elif ctype == 2:
                out.append({"type": ctype, "custom_id": comp.get("custom_id"),
                            "label": comp.get("label") or comp.get("emoji", {}).get("name"),
                            "disabled": bool(comp.get("disabled"))})
            elif ctype in (3, 5, 6, 7, 8):
                out.append({"type": ctype, "custom_id": comp.get("custom_id"),
                            "placeholder": comp.get("placeholder"),
                            "options": [(o.get("label"), o.get("value")) for o in comp.get("options") or []],
                            "disabled": bool(comp.get("disabled"))})
    return out


# --------------------------------------------------------------------------
# the drive
# --------------------------------------------------------------------------
class Drive:
    def __init__(self, bot, repo: str, dsn: str = "") -> None:
        self.bot = bot
        self.repo = repo
        self.dsn = dsn
        self.presented: list[dict] = []        # every presenter call, in order
        self.resolved: list[dict] = []         # every resolve() result, in order
        self.steps: list[dict] = []            # every driven interaction with its outcome
        self.lockouts: list[dict] = []         # command-access lock-outs met, and the reset
        self.expected_panels = self._expected_panels()

    async def reset_command_access(self) -> dict:
        """INTERVENTION (recorded): put the guild's command-access policy back to
        all_channels so the walk can continue past a lock-out the walker
        itself caused. Never part of the bot's behaviour."""
        import asyncpg

        conn = await asyncpg.connect(self.dsn)
        try:
            async with conn.transaction():
                before = [dict(r) for r in await conn.fetch(
                    "SELECT guild_id, mode, updated_by FROM guild_command_access_policy "
                    "WHERE guild_id=$1", GUILD_ID)]
                # scoped to the synthetic guild only — a reused test database
                # may hold other guilds' rows, which are not this walk's to touch
                await conn.execute(
                    "DELETE FROM guild_command_access_channel_roles WHERE guild_id=$1", GUILD_ID)
                await conn.execute(
                    "DELETE FROM guild_command_access_channels WHERE guild_id=$1", GUILD_ID)
                await conn.execute(
                    "UPDATE guild_command_access_policy SET mode='all_channels' WHERE guild_id=$1",
                    GUILD_ID)
        finally:
            await conn.close()
        # the reader caches per guild for 60 s (sb/domain/platform/command_access.py
        # _CACHE) — the UI write invalidates through forget_guild; so must we.
        from sb.domain.platform.command_access import forget_guild

        forget_guild(GUILD_ID)
        return {"before": before, "after": "all_channels", "cache": "forget_guild called"}

    def _expected_panels(self) -> set[str]:
        snap = json.load(open(os.path.join(self.repo, "manifest.snapshot.json")))
        ids = set()
        for sub, s in snap["subsystems"].items():
            p = s.get("panels") or {}
            it = p.items() if isinstance(p, dict) else [(x.get("panel_id"), x) for x in p]
            for pid, spec in it:
                ids.add(spec.get("panel_id", pid))
        return ids

    # -- instrumentation ----------------------------------------------------
    def install_probes(self) -> None:
        import importlib

        from sb.kernel.panels import engine as panel_engine

        resolve_mod = importlib.import_module("sb.kernel.interaction.resolve")

        real_presenter = panel_engine._presenter

        async def recording_presenter(rendered, req):
            entry = {
                "seq": len(self.presented), "panel_id": rendered.panel_id,
                "audience": rendered.audience, "anchor_policy": rendered.anchor_policy,
                "title": getattr(rendered.embed, "title", None) if rendered.embed else None,
                "nonnav_controls": sum(
                    1 for c in rendered.components
                    if not str(c.custom_id).startswith("nav:") and not c.disabled
                    and not getattr(c, "url", "")),
                "origin_none": req.origin is None,
                "components": [
                    {"kind": c.kind, "custom_id": c.custom_id, "label": c.label,
                     "disabled": c.disabled, "url": getattr(c, "url", ""),
                     "n_options": len(c.options or ()),
                     "native": getattr(c, "native_picker", "") or ("channel" if getattr(c, "channel_types", None) else "")}
                    for c in rendered.components],
                "edit": rendered.edit_message_ref is not None,
                "interaction_id": getattr(req.origin, "id", None),
                "surface": getattr(req.surface, "value", None),
            }
            self.presented.append(entry)
            ref = await real_presenter(rendered, req)
            # None = the production presenter found no send branch for this
            # request shape and dropped the render on the floor.
            entry["sent"] = ref is not None
            entry["message_ref"] = str(ref) if ref is not None else None
            return ref

        panel_engine.install_panel_presenter(recording_presenter)

        real_resolve = resolve_mod.resolve

        async def recording_resolve(req):
            result = await real_resolve(req)
            self.resolved.append({
                "seq": len(self.resolved), "target": req.target.key,
                "surface": getattr(req.surface, "value", None),
                "outcome": getattr(result, "outcome", None),
                "reason": getattr(getattr(result, "reason", None), "value", None),
                "error_class": getattr(getattr(result, "error_class", None), "value", None),
                "user_message": (str(result.user_message)[:300] if getattr(result, "user_message", None) else None),
                "interaction_id": getattr(req.origin, "id", None),
            })
            return result

        # every adapter imported resolve by name; patch each binding
        import sb.kernel.interaction.adapters.component as comp_mod
        import sb.kernel.interaction.adapters.modal as modal_mod
        import sb.kernel.interaction.adapters.slash as slash_mod
        for mod in (comp_mod, modal_mod, slash_mod):
            if hasattr(mod, "resolve"):
                mod.resolve = recording_resolve
        resolve_mod.resolve = recording_resolve

    # -- one interaction ----------------------------------------------------
    async def run_interaction(self, payload: dict, *, label: str) -> dict:
        import discord
        from sb.adapters.discord import component_feed

        state = self.bot._connection
        interaction = discord.Interaction(data=payload, state=state)
        iid = interaction.id
        n_presented, n_resolved, n_events = len(self.presented), len(self.resolved), len(REC.events)
        error = None
        t0 = time.perf_counter()
        try:
            if interaction.type is discord.InteractionType.application_command:
                await self.bot.tree._call(interaction)
            elif interaction.type is discord.InteractionType.component:
                await component_feed.handle_component_interaction(interaction)
            elif interaction.type is discord.InteractionType.modal_submit:
                if component_feed.is_confirm_modal_submit(interaction):
                    await component_feed.handle_confirm_modal_submit(interaction)
                else:
                    await component_feed.handle_panel_modal_submit(interaction)
        except Exception as exc:  # noqa: BLE001 — the drive records, never dies
            error = f"{type(exc).__name__}: {exc}"[:300]
        # let any scheduled follow-up tasks (the tree wrapper, listeners) settle
        for _ in range(20):
            pending = [t for t in asyncio.all_tasks()
                       if t is not asyncio.current_task() and not t.done()
                       and (t.get_name() or "").startswith(("CommandTree", "discord"))]
            if not pending:
                break
            await asyncio.sleep(0.01)
        step = {
            "seq": len(self.steps), "label": label, "interaction_id": iid,
            "type": int(interaction.type.value), "custom_id": payload["data"].get("custom_id"),
            "command": payload["data"].get("name"), "values": payload["data"].get("values"),
            "elapsed_ms": round((time.perf_counter() - t0) * 1000, 1),
            "presented": self.presented[n_presented:],
            "resolved": self.resolved[n_resolved:],
            "responses": [
                {k: v for k, v in e.items() if k in ("kind", "response_type", "message_id", "channel_id")}
                for e in REC.events[n_events:]],
            "messages": [REC.messages[e["message_id"]] for e in REC.events[n_events:]
                         if e.get("message_id") in REC.messages],
            "modals": [e.get("data") for e in REC.events[n_events:]
                       if e.get("response_type") == 9],
            "error": error,
        }
        # message id -> the panel the engine stored under that message key
        from sb.kernel.panels import engine as panel_engine

        step["message_panels"] = {}
        for m in step["messages"]:
            sess = panel_engine.session_for(str(m["id"]))
            if sess is not None:
                step["message_panels"][m["id"]] = sess.panel_id
        # the user-visible text of the first response (denials, pointers, refusals)
        texts = []
        for e in REC.events[n_events:]:
            d = e.get("data") or {}
            if d.get("content"):
                texts.append(str(d["content"])[:300])
            for emb in d.get("embeds") or []:
                if emb.get("title"):
                    texts.append("[embed] " + str(emb["title"])[:120])
        step["texts"] = texts
        self.steps.append(step)
        return step

    # -- walkers ------------------------------------------------------------
    async def walk_from(self, actor: Actor, roots: list[dict], *, budget: int,
                        label: str, max_depth: int = 8) -> dict:
        """BFS over rendered controls. Each (panel_id, control, value) is
        clicked once. Returns the observed graph."""
        seen_panels: dict[str, int] = {}          # panel -> depth first seen
        edges: list[tuple[str, str, str, str | None]] = []
        clicked: set[tuple[str, str, str | None]] = set()
        queue: collections.deque = collections.deque()
        modals: list[dict] = []
        dead_ends: list[str] = []
        n = 0

        def register(step: dict, depth: int, source_panel: str | None, via: str | None,
                     value: str | None) -> None:
            for p in step["presented"]:
                pid = p["panel_id"]
                if source_panel is not None:
                    edges.append((source_panel, via or "", pid, value))
                if pid not in seen_panels:
                    seen_panels[pid] = depth
            pids = [p["panel_id"] for p in step["presented"]]
            for msg in step["messages"]:
                pid = step["message_panels"].get(msg["id"]) or (pids[-1] if pids else None)
                if pid is None:
                    continue
                if depth < max_depth:
                    queue.append((msg, pid, depth + 1))
            for modal in step["modals"]:
                modals.append({"from": source_panel, "via": via, "step": step["seq"],
                               "custom_id": modal.get("custom_id"), "title": modal.get("title")})
                if depth < max_depth:
                    queue.append(({"__modal__": modal, "__host__": (step["messages"] or [None])[-1]},
                                  source_panel or "?", depth + 1))

        from sb.kernel.panels import engine as panel_engine

        def canon(cid: str) -> str:
            # session-lifecycle panels mint a fresh 32-hex id per render; the
            # walk must key a control by its DECLARED identity or it re-clicks
            # the same Cog Manager select forever (measured: 6,518 clicks).
            b = panel_engine.ephemeral_route(cid)
            return f"{b.panel_id}.{b.component_id}" if b is not None else cid

        async def drive_step(payload: dict, step_label: str) -> dict:
            step = await self.run_interaction(payload, label=step_label)
            if any(x["reason"] == "channel" for x in step["resolved"]) and self.dsn:
                # the walker's own earlier click changed the command-access
                # policy and the guild owner is now locked out of #general —
                # record it, reset the policy (an intervention), and replay
                # this one interaction so the walk measures reachability,
                # not the lock-out.
                cause = next((s for s in reversed(self.steps[:-1])
                              if any(x["target"].startswith("settings.command_access")
                                     and x["outcome"] == "success" for x in s["resolved"])), None)
                reset = await self.reset_command_access()
                self.lockouts.append({
                    "denied_step": step["seq"], "denied_label": step_label,
                    "denial_text": (step["texts"] or [""])[0][:200],
                    "cause_step": cause["seq"] if cause else None,
                    "cause_label": cause["label"] if cause else None,
                    "cause_texts": (cause["texts"] if cause else None),
                    "policy_reset": reset,
                })
                payload = json.loads(json.dumps(payload))
                iid, token = INTERACTIONS.open(channel_id=int(payload["channel_id"]),
                                               message_id=int(payload["message"]["id"]) if payload.get("message") else None)
                payload["id"], payload["token"] = str(iid), token
                step = await self.run_interaction(payload, label=step_label + " [replay after reset]")
            return step

        for root in roots:
            step = await drive_step(root["payload"], f"{label}:{root['label']}")
            n += 1
            register(step, 0, None, None, None)
        while queue and n < budget:
            msg, pid, depth = queue.popleft()
            if "__modal__" in msg:
                modal = msg["__modal__"]
                key = (pid, f"modal:{modal.get('custom_id')}", None)
                if key in clicked:
                    continue
                clicked.add(key)
                fields = {}
                for row in modal.get("components") or []:
                    for comp in row.get("components") or []:
                        flabel = str(comp.get("label") or "").lower()
                        numeric = any(w in flabel for w in ("day", "level", "number", "count", "hours", "minutes", "amount", "id"))
                        fields[comp.get("custom_id")] = "3" if numeric else "headless test value"
                payload = modal_payload(actor, msg["__host__"], modal.get("custom_id"), fields)
                step = await drive_step(payload, f"{label}:{pid}:modal:{modal.get('title')}")
                n += 1
                register(step, depth, pid, f"modal:{modal.get('title')}:{modal.get('custom_id')}", None)
                continue
            ctrls = [c for c in wire_components(msg) if c["custom_id"] and not c["disabled"]]
            if not ctrls:
                dead_ends.append(pid)
                continue
            for c in ctrls:
                if n >= budget:
                    break
                cid = c["custom_id"]
                if c["type"] == 2:
                    key = (pid, canon(cid), None)
                    if key in clicked:
                        continue
                    clicked.add(key)
                    payload = component_payload(actor, msg, cid, 2)
                    step = await drive_step(payload, f"{label}:{pid}:{c.get('label')}")
                    n += 1
                    register(step, depth, pid, f"button:{c.get('label')}:{cid}", None)
                elif c["type"] == 3:
                    options = c["options"] or []
                    for _lab, val in options:
                        if n >= budget:
                            break
                        key = (pid, canon(cid), val)
                        if key in clicked:
                            continue
                        clicked.add(key)
                        payload = component_payload(actor, msg, cid, 3, values=[val])
                        step = await drive_step(payload, f"{label}:{pid}:{_lab}")
                        n += 1
                        register(step, depth, pid, f"select:{_lab}:{cid}", val)
                else:
                    # native pickers: one representative value each
                    value = {5: str(MEMBER_ID), 6: str(ROLE_MEMBER), 8: str(CH_MODLOGS),
                             7: str(CH_MODLOGS)}.get(c["type"], "")
                    key = (pid, canon(cid), value)
                    if key in clicked:
                        continue
                    clicked.add(key)
                    payload = component_payload(actor, msg, cid, c["type"], values=[value])
                    step = await drive_step(payload, f"{label}:{pid}:picker")
                    n += 1
                    register(step, depth, pid, f"picker{c['type']}:{cid}", value)
        return {"label": label, "interactions": n, "panels": seen_panels,
                "edges": edges, "modals": modals, "dead_ends": sorted(set(dead_ends)),
                "budget_exhausted": n >= budget, "queue_left": len(queue),
                "lockouts": [l for l in self.lockouts if l["denied_label"].startswith(label + ":")]}


# --------------------------------------------------------------------------
# DB census
# --------------------------------------------------------------------------
async def table_counts(dsn: str) -> dict[str, int]:
    import asyncpg

    conn = await asyncpg.connect(dsn)
    try:
        rows = await conn.fetch(
            "SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename")
        out = {}
        for r in rows:
            out[r["tablename"]] = await conn.fetchval(f'SELECT count(*) FROM "{r["tablename"]}"')
        return out
    finally:
        await conn.close()


async def fetch_rows(dsn: str, sql: str) -> list[dict]:
    import asyncpg

    conn = await asyncpg.connect(dsn)
    try:
        return [dict(r) for r in await conn.fetch(sql)]
    except Exception as exc:  # noqa: BLE001
        return [{"error": str(exc)[:200]}]
    finally:
        await conn.close()


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def checkout_revision(repo: str) -> tuple[str, bool]:
    """(HEAD sha, dirty) of the checkout the drive is about to run — the pin
    the record carries is READ from the tree, never taken from a flag."""
    import subprocess

    head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()
    status = subprocess.run(["git", "-C", repo, "status", "--porcelain"],
                            capture_output=True, text=True, check=True).stdout
    return head, bool(status.strip())


async def main_async(args) -> int:
    head, dirty = checkout_revision(args.repo)
    if args.pin and head != args.pin:
        raise SystemExit(f"checkout HEAD {head} is not the expected pin {args.pin}; "
                         f"refusing to attribute evidence to the wrong source state")
    if dirty:
        raise SystemExit(f"checkout at {head} has uncommitted changes; the record "
                         f"could not be attributed to a revision")
    sys.path.insert(0, args.repo)
    os.chdir(args.repo)
    os.environ["DISCORD_BOT_TOKEN_PRODUCTION"] = "headless-placeholder-never-a-real-token"
    os.environ["DATABASE_URL"] = args.dsn
    os.environ["SB_DATA_PLANE"] = "test"
    os.environ["SB_TEST_DB_HOSTS"] = "127.0.0.1"
    os.environ["SB_APPCMD_SYNC_GUILD_ID"] = str(GUILD_ID)
    os.environ["HEALTH_HOST"] = "127.0.0.1"
    os.environ["HEALTH_PORT"] = str(HEALTH_PORT)
    os.environ.pop("SB_VERIFY_BOOT", None)
    if args.intents:
        os.environ["SB_INTENT_MSGCONTENT_OK"] = "true"
        os.environ["SB_INTENT_MEMBERS_OK"] = "true"

    boot_log: list[str] = []

    class _Capture(logging.Handler):
        def emit(self, record):
            try:
                boot_log.append(f"{record.levelname} {record.name}: {record.getMessage()}")
            except Exception:  # noqa: BLE001
                pass

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    logging.getLogger().addHandler(_Capture())

    import discord
    from discord.webhook import async_ as webhook_async

    from sb.adapters.discord import gateway as gw
    from sb.app import main as app_main
    from sb.domain.diagnostic.log_buffer import install as install_log_ring

    install_log_ring()
    webhook_async.async_context.set(FakeWebhookAdapter())

    all_perms = discord.Permissions.all().value
    none_perms = discord.Permissions.none().value
    guild_state: dict = {}
    boot_complete = asyncio.Event()
    holder: dict = {}

    real_build_bot = gw.build_bot

    def build_bot_and_fake(cfg):
        bot = real_build_bot(cfg)
        holder["bot"] = bot
        install_fake_http(bot, guild_state)
        return bot

    async def stub_connect_gateway(bot, token, *, ready_timeout_s=None):
        # NO token is used. Populate what a READY would have populated: the
        # client user, the application id and the one synthetic guild.
        state = bot._connection
        state.user = discord.ClientUser(state=state, data={
            "id": str(TEST_APP_ID), "username": "headless-test-bot", "discriminator": "0",
            "avatar": None, "bot": True, "verified": True, "mfa_enabled": False})
        state.application_id = TEST_APP_ID
        gp = guild_payload(all_perms, none_perms)
        _index_members(gp)
        guild = discord.Guild(data=gp, state=state)
        state._add_guild(guild)
        guild_state["guild"] = guild
        REC.record("gateway_stub", note="connect_gateway replaced; no socket, no token")
        # the stub "gateway task" ends when the composition root closes the
        # bot — the shape a real bot.start() task has, so the shutdown path
        # is the root's own, not a cancellation from outside.
        closed = asyncio.Event()
        real_close = bot.close

        async def close_and_signal():
            try:
                await real_close()
            finally:
                closed.set()

        bot.close = close_and_signal
        return asyncio.create_task(closed.wait(), name="sb-gateway-stub")

    gw.build_bot = build_bot_and_fake
    gw.connect_gateway = stub_connect_gateway

    boot_state = {"ok": False, "failed": False}

    class _BootWatch(logging.Handler):
        def emit(self, record):
            if record.name != "sb.app.main":
                return
            message = record.getMessage()
            if "boot complete" in message:
                boot_state["ok"] = True
                boot_complete.set()
            elif "FAILED_STARTUP" in message:
                boot_state["failed"] = True
                boot_complete.set()

    logging.getLogger("sb.app.main").addHandler(_BootWatch())

    counts_before = await table_counts(args.dsn)
    t_boot = time.perf_counter()
    app_task = asyncio.create_task(app_main.run_app(), name="sb-run-app")
    await asyncio.wait({app_task, asyncio.create_task(boot_complete.wait())},
                       timeout=180, return_when=asyncio.FIRST_COMPLETED)
    boot_s = round(time.perf_counter() - t_boot, 2)
    from sb.kernel import lifecycle

    booted = (boot_state["ok"] and not boot_state["failed"] and not app_task.done()
              and lifecycle.get_phase() is lifecycle.Phase.RUNNING)
    result: dict = {"pin": head, "started_at": now_iso(), "boot_seconds": boot_s,
                    "boot_log": boot_log[:], "boot_failed": not booted,
                    "boot_state": dict(boot_state), "wait_timed_out": not boot_complete.is_set()}
    if not booted:
        # a timeout, a FAILED_STARTUP, or a task that already unwound: nothing
        # below may run against it — record the state and stop.
        if not app_task.done():
            app_task.cancel()
            try:
                await app_task
            except (asyncio.CancelledError, Exception):  # noqa: BLE001
                pass
        result["exit"] = (app_task.result() if app_task.done() and not app_task.cancelled()
                          and app_task.exception() is None else repr(
                              app_task.exception() if app_task.done() and not app_task.cancelled()
                              else "cancelled"))
        result["lifecycle_phase_final"] = lifecycle.get_phase().value
        json.dump(result, open(args.out, "w"), indent=1, default=str)
        print(json.dumps({k: v for k, v in result.items() if k != "boot_log"}, indent=1, default=str))
        return 1

    bot = holder["bot"]
    result["lifecycle_phase_after_boot"] = lifecycle.get_phase().value
    # /ready as the health server sees it (no gateway => not ready by design)
    import urllib.request

    def _probe_ready():
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            with opener.open(f"http://127.0.0.1:{HEALTH_PORT}/ready", timeout=5) as r:
                return {"status": r.status, "body": r.read().decode()[:300]}
        except urllib.error.HTTPError as e:
            return {"status": e.code, "body": e.read().decode()[:300]}
        except Exception as exc:  # noqa: BLE001
            return {"error": str(exc)[:200]}

    # blocking I/O off the loop, or the health server can never answer
    result["ready_http"] = await asyncio.to_thread(_probe_ready)

    drive = Drive(bot, args.repo, args.dsn)
    drive.install_probes()
    tree_cmds = sorted(c.qualified_name for c in bot.tree.walk_commands())
    result["tree_commands"] = tree_cmds
    result["tree_command_count"] = len(tree_cmds)
    result["expected_panels"] = len(drive.expected_panels)

    owner = Actor(OWNER_ID, "owner", [], all_perms)
    member = Actor(MEMBER_ID, "member", [ROLE_MEMBER], none_perms)

    phases: dict = {}

    if args.restart_check:
        # SECOND BOOT over the SAME database: the "come back the next day"
        # scenario — the boot hook's resume sweep ran above (see boot_log);
        # re-open the console and the status card and read what they show.
        phases["restart"] = [
            await drive.run_interaction(slash_payload(owner, "setup-hub"), label="restart:/setup-hub"),
            await drive.run_interaction(slash_payload(owner, "setup-status"), label="restart:/setup-status"),
            await drive.run_interaction(slash_payload(owner, "setup"), label="restart:/setup"),
            await drive.run_interaction(slash_payload(owner, "help"), label="restart:/help"),
        ]
        result["db"] = {"after": await table_counts(args.dsn)}
        result["db"]["setup_session_rows"] = await fetch_rows(
            args.dsn, "SELECT * FROM setup_session ORDER BY 1 LIMIT 5")
        result["phases"] = phases
        result["presented"] = drive.presented
        result["resolved"] = drive.resolved
        result["steps"] = drive.steps
        result["http_calls"] = dict(REC.http_calls)
        result["resume_sweep_log"] = [l for l in boot_log if "resume" in l.lower() or "boot hook" in l.lower()]
        os.kill(os.getpid(), signal.SIGTERM)
        try:
            result["run_app_exit"] = await asyncio.wait_for(app_task, timeout=60)
        except Exception as exc:  # noqa: BLE001
            result["run_app_exit"] = f"shutdown error: {exc!r}"
        json.dump(result, open(args.out, "w"), indent=1, default=str)
        print(json.dumps({"restart_check": True, "run_app_exit": result["run_app_exit"],
                          "resume_sweep_log": result["resume_sweep_log"]}, indent=1, default=str))
        return 0 if result["run_app_exit"] == 0 else 2

    # PHASE 0 — first contact on a fresh guild: /help and /setup as the owner,
    # /help as a plain member. Nothing configured, empty tables.
    phases["p0_first_contact"] = [
        await drive.run_interaction(slash_payload(owner, "help"), label="owner:/help"),
        await drive.run_interaction(slash_payload(member, "help"), label="member:/help"),
        await drive.run_interaction(slash_payload(member, "setup-hub"), label="member:/setup-hub"),
    ]

    # PHASE 1 — the help tree from /help, walked to exhaustion.
    phases["p1_help_walk"] = await drive.walk_from(
        owner, [{"label": "/help", "payload": slash_payload(owner, "help")}],
        budget=args.budget, label="help")

    # PHASE 2 — the setup surfaces: the join launcher, /setup, /setup-hub (+depths),
    # /setup-advanced, /setup-status, /setup-describe — walked from each root.
    from sb.kernel.interaction.guild_events import GuildJoinEvent, dispatch_guild_join

    n_ev = len(REC.events)
    join_consumers = await dispatch_guild_join(GuildJoinEvent(
        guild_id=GUILD_ID, guild_name="Headless Test Guild", owner_id=OWNER_ID,
        system_channel_id=CH_GENERAL))
    join_events = REC.events[n_ev:]
    launcher_msgs = [REC.messages[e["message_id"]] for e in join_events if e.get("message_id") in REC.messages]
    phases["p2_join"] = {"consumers": join_consumers,
                         "events": [{k: v for k, v in e.items() if k != "data"} for e in join_events],
                         "launcher_messages": launcher_msgs,
                         "launcher_texts": [e.get("data", {}).get("content") for e in join_events if e.get("data")]}
    roots = [{"label": "/setup", "payload": slash_payload(owner, "setup")},
             {"label": "/setup-hub", "payload": slash_payload(owner, "setup-hub")},
             {"label": "/setup-advanced", "payload": slash_payload(owner, "setup-advanced")},
             {"label": "/setup-status", "payload": slash_payload(owner, "setup-status")},
             {"label": "/setup-describe", "payload": slash_payload(owner, "setup-describe")}]
    setup_walk = await drive.walk_from(owner, roots, budget=args.budget, label="setup")
    # the launcher card's buttons, clicked as the owner (a channel message,
    # not an interaction reply — so it is driven here rather than by the walk)
    launcher_walk = None
    if launcher_msgs:
        seen = {}
        for msg in launcher_msgs:
            for c in wire_components(msg):
                if not c["custom_id"] or c["disabled"]:
                    continue
                step = await drive.run_interaction(
                    component_payload(owner, msg, c["custom_id"], c["type"]),
                    label=f"launcher:{c.get('label')}")
                seen[c["custom_id"]] = {"label": c.get("label"),
                                        "presented": [p["panel_id"] for p in step["presented"]],
                                        "texts": step["texts"], "resolved": step["resolved"]}
        launcher_walk = seen
    phases["p2_setup_walk"] = setup_walk
    phases["p2_launcher_clicks"] = launcher_walk
    counts_after_setup = await table_counts(args.dsn)

    # PHASE 3 — every slash command in the tree as the owner, then every
    # rendered control, to a budget: the runtime reachability figure.
    if not args.skip_global:
        roots = []
        for name in tree_cmds:
            parts = name.split(" ")
            if len(parts) == 1:
                roots.append({"label": f"/{name}", "payload": slash_payload(owner, name)})
            else:
                roots.append({"label": f"/{name}", "payload": slash_payload(owner, parts[0], subcommands=parts[1:])})
        phases["p3_global_walk"] = await drive.walk_from(owner, roots, budget=args.global_budget,
                                                         label="global")
    counts_after = await table_counts(args.dsn)

    # settings + audit rows that the setup drive left behind
    result["db"] = {
        "before": counts_before, "after_setup": counts_after_setup, "after": counts_after,
        "delta_setup": {k: counts_after_setup.get(k, 0) - counts_before.get(k, 0)
                        for k in counts_after_setup if counts_after_setup.get(k, 0) != counts_before.get(k, 0)},
        "delta_total": {k: counts_after.get(k, 0) - counts_before.get(k, 0)
                        for k in counts_after if counts_after.get(k, 0) != counts_before.get(k, 0)},
    }
    result["db"]["setup_session_rows"] = await fetch_rows(
        args.dsn, "SELECT * FROM setup_session ORDER BY 1 LIMIT 5")
    result["db"]["audit_sample"] = await fetch_rows(
        args.dsn, "SELECT subsystem, mutation_type, target, scope, guild_id, actor_id, actor_type "
                  "FROM audit_log ORDER BY 1 LIMIT 40")
    result["db"]["outbox_by_status"] = await fetch_rows(
        args.dsn, "SELECT status, count(*) AS n FROM event_outbox GROUP BY status")

    # population contract: expected (committed snapshot) vs presented (engine)
    presented_ids = {p["panel_id"] for p in drive.presented}
    sent_ids = {p["panel_id"] for p in drive.presented if p.get("sent")}
    result["population"] = {
        "expected": len(drive.expected_panels),
        "presented": len(presented_ids),
        "sent": len(sent_ids),
        "rendered_but_never_sent": sorted(presented_ids - sent_ids),
        "presented_not_expected": sorted(presented_ids - drive.expected_panels),
        "expected_not_presented": sorted(drive.expected_panels - presented_ids),
    }
    result["phases"] = phases
    result["presented"] = drive.presented
    result["resolved"] = drive.resolved
    result["steps"] = drive.steps
    result["http_calls"] = dict(REC.http_calls)
    result["unhandled_http"] = sorted(set(REC.unhandled_http))
    result["events_total"] = len(REC.events)
    result["lockouts"] = drive.lockouts

    # shutdown through the composition root's own signal path
    os.kill(os.getpid(), signal.SIGTERM)
    try:
        exit_code = await asyncio.wait_for(app_task, timeout=60)
    except Exception as exc:  # noqa: BLE001
        exit_code = f"shutdown error: {exc!r}"
    result["run_app_exit"] = exit_code
    result["lifecycle_phase_final"] = lifecycle.get_phase().value
    result["shutdown_log"] = [l for l in boot_log if "lifecycle" in l.lower() or "drain" in l.lower()][-12:]
    json.dump(result, open(args.out, "w"), indent=1, default=str)
    summary = {k: result[k] for k in ("boot_seconds", "lifecycle_phase_after_boot", "ready_http",
                                     "tree_command_count", "population", "run_app_exit",
                                     "lifecycle_phase_final", "events_total", "unhandled_http")}
    summary["phase_sizes"] = {k: (v.get("interactions", len(v)) if isinstance(v, dict) else len(v))
                              for k, v in phases.items() if v is not None}
    print(json.dumps(summary, indent=1, default=str))
    # the shell sees the composition root's own verdict: a non-zero return, a
    # shutdown that timed out or raised, is an unclean run and says so.
    return 0 if exit_code == 0 else 2


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="/home/user/superbot-next")
    ap.add_argument("--dsn", default="postgresql://superbot@127.0.0.1:54329/superbot")
    ap.add_argument("--out", default="headless_drive_result.json")
    ap.add_argument("--pin", default=None,
                    help="the revision the checkout is EXPECTED to be at; the drive refuses "
                         "to run when HEAD differs. The recorded pin is always read from HEAD.")
    ap.add_argument("--budget", type=int, default=400)
    ap.add_argument("--global-budget", type=int, default=3000)
    ap.add_argument("--skip-global", action="store_true")
    ap.add_argument("--intents", action="store_true",
                    help="declare both privileged intents approved (arms the message feed)")
    ap.add_argument("--restart-check", action="store_true",
                    help="second boot over the SAME database: re-open the console and stop")
    args = ap.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    sys.exit(main())
