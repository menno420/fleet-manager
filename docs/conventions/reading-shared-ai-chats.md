# Reading a shared AI chat transcript

> **Status:** `reference`
>
> Shared-chat URLs (`share.gemini.google/…`, `chatgpt.com/share/…`) hold real
> evidence and cannot be read by an ordinary fetcher. This is the method that
> works, the three container-specific fixes it needs, and what each fix costs if
> you skip it. Verified 2026-08-03; the tool is `tools/read_shared_chat.py`.

## Use it

```bash
python3 tools/read_shared_chat.py --setup            # once per container, needs root
python3 tools/read_shared_chat.py <url> -o out.txt
```

`--setup` installs `libnss3-tools` and imports the proxy CA bundle into the
browser's certificate store. It is idempotent — running it twice is harmless.

Measured on a Gemini share link: **70 426 characters of transcript**, the whole
conversation including every prompt and reply.

## Why an ordinary fetcher cannot do this

Three separate failures, each of which looks like a different problem:

| What you try | What happens |
|---|---|
| `WebFetch` on `share.gemini.google/…` | 301, and following it fails with `Parse Error: Header overflow` — the redirect target sends response headers larger than the fetcher's buffer |
| `curl` / plain HTTP | 200 and about 821 KB of HTML with **zero** conversation content — the page is an empty shell |
| a real browser | works |

The middle row is the trap. It succeeds, it returns a large body, and a size
check passes. The conversation simply is not in the HTML — it arrives after
JavaScript hydration. Anything downstream that greps the body finds nothing and
concludes the page is empty, when the page is fine and the reader is wrong.

## The three fixes, and what each one costs if skipped

### 1. Point Playwright at the browser that is already here

```python
browser = driver.chromium.launch(executable_path="/opt/pw-browsers/chromium", ...)
```

`pip install playwright` brings a driver that expects its own browser build in
its own cache. This container ships Chromium at `/opt/pw-browsers/chromium` and
sets `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`.

Skip this and Playwright reports the browser as missing. **Do not run
`playwright install`** — it is the obvious next step and it is wrong: it
downloads a second copy of a browser that is already on disk.

### 2. Import the proxy CA into the browser's own certificate store

```bash
apt-get install -y libnss3-tools
certutil -N -d sql:/root/.pki/nssdb --empty-password
# then, for each PEM block in /root/.ccr/ca-bundle.crt:
certutil -A -d sql:/root/.pki/nssdb -t "C,," -n ccr-ca-<n> -i cert.pem
```

Skip this and every navigation fails with `ERR_CERT_AUTHORITY_INVALID`.

This is the fix worth remembering, because the surrounding documentation
actively points the other way. The proxy README says trust is preconfigured, and
for `curl`, Python `requests`, Java and Node it is — each reads a bundle from a
path or an environment variable. **Chromium does not.** It reads an NSS database
at `/root/.pki/nssdb`, and on a fresh container that database **does not exist at
all**. Verified again this session: no `certutil`, no `/root/.pki/nssdb`, 151
certificates in the bundle and none of them reachable by the browser.

So "TLS is preconfigured" and "the browser cannot verify anything" are both true
at once. They are different trust stores.

Never resolve this with `--ignore-certificate-errors` or by disabling
verification. The certificate error is a missing-store problem with a clean fix,
and turning verification off would make every future page silently
unauthenticated.

### 3. Launch with `--no-proxy-server`

```python
args=["--no-proxy-server", "--no-sandbox"]
```

Skip this and navigation fails with `ERR_CONNECTION_RESET`.

Chromium picks up the ambient `HTTPS_PROXY`, and the agent proxy resets the
browser's connections. Going direct is what works. Note the ordering trap: fix 3
without fix 2 gives a certificate error, and fix 2 without fix 3 gives a
connection reset — so fixing either one alone looks like it made no difference,
and it is tempting to revert the fix that "did not help". Both are needed, and
only both together produce a page.

## Reading the page once it loads

```python
page.goto(url, wait_until="domcontentloaded", timeout=90_000)
time.sleep(8)
text = page.inner_text("body")
```

`domcontentloaded` rather than `networkidle`: these pages keep connections open,
so `networkidle` can wait out the timeout on a page that finished rendering
seconds ago. There is no event meaning "the transcript is on the page", so the
fixed wait is the honest mechanism. Eight seconds was enough for a
70 000-character Gemini transcript; raise `--wait` if a long one comes back
short.

`inner_text("body")` rather than parsing the DOM: the markup is generated and
will change, the text is what you want, and text survives redesigns.

## What you get

Gemini share pages render the entire conversation as text — every prompt, every
reply, in order — plus site chrome at the top and footer links at the bottom.
Two things worth knowing:

- The page displays a **canonical share URL that may differ from the one you
  opened**. Both resolve to the same conversation. Do not treat the mismatch as
  a wrong page.
- The header carries `Created with <model>` and `Published <date>`. That is a
  primary fact about which model produced the conversation, and it is more
  reliable than asking the model itself.

## Status per platform

**Gemini (`share.gemini.google/…`) — fully verified 2026-08-03.** Full
transcript extracted twice, once through the tool. Content spot-checked against
strings known to be in the conversation.

**ChatGPT (`chatgpt.com/share/…`) — transport and rendering verified; transcript
extraction not yet verified.** What was confirmed: the browser reaches
`chatgpt.com` over this path, TLS verifies against the imported store, the SPA
hydrates, and `inner_text("body")` returns route-specific rendered text — a
nonexistent share id rendered the logged-out app shell, and a GPT URL rendered
`This GPT is inaccessible or not found`. Every step of the mechanism is
therefore exercised. What was **not** confirmed is extraction from a live share
link, because no valid public one was available to test against. Shared
conversations are documented as viewable without an account, so the same command
should work:

```bash
python3 tools/read_shared_chat.py "https://chatgpt.com/share/<id>" -o out.txt
```

If it comes back with only the app shell and no conversation, raise `--wait`
before concluding anything — a short read is far more likely to be a hydration
race than a wall.

Worth trying first for ChatGPT: shared conversations are indexed by search
engines, which suggests the page may be server-rendered enough for a plain
fetcher. If `WebFetch` returns the conversation, use that and skip the browser
entirely.

## When to reach for this

Whenever a shared chat is the evidence — verifying what a model actually said,
reading a report someone was given, checking a claim about a conversation. A
summary of a chat is not the chat, and the transcript settles disagreements that
summaries create. Reading one is now a two-minute operation.
