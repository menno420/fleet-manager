# The owner's public Drive folder — reading it without the Drive API

> **Status:** `reference`
>
> Where the owner drops game recordings, cover art and reference images for a
> session to use, and the route that reads it with no configuration.

## The folder

**<https://drive.google.com/drive/folders/1xGaAvsg43oInwGZfPZHXzAvqkmdT7-90>**

Folder ID: `1xGaAvsg43oInwGZfPZHXzAvqkmdT7-90` · shared "anyone with the link".
Owner-maintained; he uploads gameplay captures and art here when a session
needs source material. As of 2026-08-05 it held ten Spider Swing screen
recordings and the cover art.

**Why it exists:** conversation image uploads arrive as inline vision only — no
file lands on disk — so an image the owner pastes into chat cannot be passed to
an image or video model. Dropping it in this folder makes it a real file.
Videos and documents *do* arrive as paths, so the folder matters most for
images.

## Reading it — measured 2026-08-05

The Drive API is **not** the route. `files.list` is blocked for API keys
(*"Requests to this API drive method … are blocked"*), and with a service
account it needs the Drive API enabled on the project, which it is not.

The route that works needs nothing enabled:

1. **List** — fetch the folder's public embed view and read filenames + IDs:

   ```
   https://drive.google.com/embeddedfolderview?id=<FOLDER_ID>#list
   ```

2. **Download** each file by ID:

   ```bash
   curl -sL --noproxy '*' -o out.mp4 \
     "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"
   ```

The `confirm=t` parameter matters — without it, large files return an
interstitial HTML page instead of bytes.

## Notes

- Files the owner exports from a phone may be **downscaled**: the cover art in
  the folder was 286×512, not the original resolution. Ask for the full-size
  original when quality matters (model conditioning, print, upscaling).
- Nothing here is private by accident, but treat the folder as public: it is
  link-shared, so anything placed in it is disclosed to anyone holding the URL.
