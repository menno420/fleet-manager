# 2026-11-20 — price-comparison homepage layout study, live on GitHub Pages

> **Status:** `in-progress` — branch `ccr-2d6463d1-utxgjc`, born red; flips to
> `complete` once the Pages deploy is verified live.

- **📊 Model:** opus-5.5 · medium · feature build
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01QRypXXoUVR1Q4guQm72ZrF](https://claude.ai/code/session_01QRypXXoUVR1Q4guQm72ZrF) · "Skroutz.gr website recreation"

**Ask (owner, live):** recreate https://www.skroutz.gr/ as a test, as close as
possible, improved where possible, live immediately via GitHub Actions; visual
and mechanical fidelity, not full function.

## What was built — `sites/skroutz-study/`

Static HTML/CSS/JS, no build step, hash-routed: home (hero carousel, promo
tiles, USP strip, category tiles, scroll-snap product rows, brands), mega menu,
search with autosuggest + keyboard nav, category/search listing with price /
subcategory / Plus / deal filters and sorting, product page with per-shop price
comparison and a 30-day price chart, cart drawer with quantities, favourites,
recently viewed (localStorage), mobile drawer nav, dark mode. Deployed by
`.github/workflows/pages-skroutz-study.yml` (push to `main` or this branch).

## Decisions and honest limits

- **Placeholder brand `kalathi`, not the real name/logo** — a public pixel-close
  copy of a real company's branding is a phishing lookalike; layout, palette and
  mechanics are matched instead, with a "not affiliated" footer note. No login
  or payment fields collect anything.
- **Source not fetched live** — `MEASURED` 2026-11-20: skroutz.gr serves a
  Cloudflare human-verification challenge to headless/curl clients (not
  bypassed, deliberately); web.archive.org and archive.ph tunnels dropped from
  this container. The layout is reconstructed from prior knowledge of the
  site, so fidelity is `REASONED`, not measured against a screenshot.
- Pages enabled (`build_type: workflow`) and `github-pages` environment branch
  policy set to `main` + this branch via the REST API, direct-PAT path.
- Gate: `python3 bootstrap.py check --strict` exit 0. Playwright run: no page
  or console errors; mobile 390 px scrollWidth 390 (no horizontal scroll).

## 💡 Session idea

**A "clone this site" ask should record the reference surface before the build
starts.** Here the target sat behind a bot challenge and both archives dropped,
so fidelity rests on recall. A small `tools/` helper that tries live → Wayback
→ archive.ph and stores the first screenshot it gets under the site folder would
turn the next such ask from `REASONED` into `MEASURED` without anyone thinking
of it.

## ⟲ Previous-session review

The previous card (`2026-09-04-spider-bot-pr-review`) is unrelated to this
work. Nothing in it bears on this ask, and this session did not re-verify its
claims.
