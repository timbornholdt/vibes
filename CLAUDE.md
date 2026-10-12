# Project conventions for timbornholdt/vibes

This repo hosts low-stakes, vibe-coded HTML tools deployed to
https://junk.timbornholdt.com/vibes/ via auto-deploy.

## Where new tools go

- Single-file HTML tools live at the repo root and are served at `junk.timbornholdt.com/vibes/<filename>.html`.
- Use lowercase, hyphenated names (e.g. `image-cropper.html`, not `ImageCropper.html`).
- **Tools with more than one file get their own folder**, named like a tool file
  without the extension: `<tool-name>/index.html` is the page (served at
  `junk.timbornholdt.com/vibes/<tool-name>/`), and its supporting files (STLs, data,
  generator scripts, images) sit next to it in that folder. Link to it from the
  root `index.html` as `file: "<tool-name>/"`. Example: `gravestone-base/`.
- The page itself still follows the single-file rules below (inline CSS/JS, no
  build step); the folder is for assets and source the page loads or links to,
  not for splitting the page's own code.
- Don't migrate existing single-file tools into folders unless asked.

## Hard rules for tool files

- **Single self-contained HTML file.** Inline all CSS and JavaScript. No build step, no bundler, no separate `.css` or `.js` files.
- **No React, no JSX, no frameworks that require a build step.** Plain HTML, vanilla JS, and CSS only.
- **External libraries via CDN only**, pinned to a specific version (cdnjs or jsDelivr). Prefer no dependencies at all when reasonable.
- **No backend of the tool's own, no API keys baked in.** Everything runs in the browser. If a tool needs an API key, prompt the user to paste their own and store it in `localStorage`.
- **The one exception is cross-device sync through vibes-store** (`server/vibes-store.py`, served at `/api/store/<key>`). Only use it when a tool's data should follow me between phone and laptop. Gated tools (`house-gripes.html`, `gb-run.html`) inline the shared `VibesSync` block and ask for my token once per device; the steps are in README.md under "Sync across devices". Keep every copy of that block identical, and copy it from an existing gated tool. Local-only conveniences (filters, a collapsed panel) stay in plain `localStorage`.
- **Must work offline once loaded** when feasible (i.e. don't phone home unnecessarily).

## Style conventions

- CSS indented with two spaces. Start the `<style>` block with:
  ```
  <style>
    * { box-sizing: border-box; }
  ```
- Inputs and textareas should be `font-size: 16px` (prevents iOS zoom-on-focus).
- JavaScript indented with two spaces. Use `<script type="module">`. Code inside the top-level script tag should not be indented at the first level.
- Mobile-friendly by default: viewport meta tag, sensible touch targets, no fixed widths.

## Page structure

Every tool file should:
- Have a `<title>` matching the tool's purpose.
- Include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Have a clear `<h1>` at the top naming the tool.
- Do **not** add a "view source" footer link (or any GitHub source link). I don't want it on any page.

## Commit messages

When committing a new tool or significant edit, include in the commit message:
- A one-line summary of what the tool does
- The original prompt (or a link to the chat transcript) that produced the change

This is the provenance trail — it's how I'll know later what was asked for and why.

## Update index page

It's crucial that every new page in this repo gets a tile on `index.html`. The
index is rendered from JavaScript, not hand-written HTML. A new tool needs:

1. **An entry at the top of the `tools` array:**
   ```js
   { file: "my-tool.html", title: "My Tool", tags: ["games"], desc: "Pithy description, two sentences max." },
   ```
   For folder tools, `file` is `"<tool-name>/"`.
2. **A tag from `tagOrder`.** Pick an existing tag if one fits; if you add a new
   one, add it to `tagOrder` too, or it won't get a filter chip.
3. **A hand-drawn icon in the `icons` map,** keyed by the same `file` value:
   line art on a `0 0 96 96` viewBox, built with the `svg()` helper,
   `stroke="currentColor"`, one clear concept, and a one-line comment saying
   what it depicts. Every tile needs one.

When a tool changes meaningfully (what it does, not just a fix), update its
`desc` so the tile still describes it. The index has no "last deployed" dates.

## Shipping

This repo auto-deploys to https://junk.timbornholdt.com/vibes/ when changes land on
`main`. **Direct pushes to `main` are blocked by the harness proxy (HTTP
403)**, so agents must route through a GitHub PR. The flow:

1. Develop on a feature branch and commit there.
2. Push the feature branch (`git push -u origin <branch>`).
3. Open a PR from the feature branch into `main` via the GitHub MCP
   (`mcp__github__create_pull_request`).
4. Merge the PR via `mcp__github__merge_pull_request` with
   `merge_method: "rebase"` to keep `main` linear.
5. After merging, resync your local `main`: `git fetch origin main` then
   `git reset --hard origin/main`. The rebase-merge gives commits new
   SHAs on the remote, so local will look "ahead" until reset.
   If you reset the feature branch the same way, push it with
   `--force-with-lease` so it matches the merged history.

Only ship once the thing actually works in a browser. Don't merge
half-finished work.

### Deploy automatically — standing permission

I (the repo owner) can't verify a change until it's live on
junk.timbornholdt.com, so deploying is effectively part of finishing the
work. **You have my standing permission to run the full ship flow above
(PR → rebase-merge → resync) automatically, without stopping to ask each
time.** Once a change works in a browser, ship it. Treat this as the
default; you don't need a fresh "deploy"/"ship it" from me.

This standing permission covers normal tool work in this repo: adding or
editing HTML tools under the repo root, updating `index.html`, and the
supporting files (`manifest.json`, `sw.js`, `icon.svg`, `README.md`,
`CLAUDE.md`). It does NOT cover anything destructive or out of scope —
**stop and ask first** if a change would:
- delete or overwrite files unrelated to the tool you're working on,
- touch anything outside this project folder,
- remove or rewrite other tools' code, or
- otherwise do something I clearly wouldn't expect from the request.

When in doubt about whether a change is destructive or in-scope, ask
before merging. The auto-deploy permission is for the safe, additive,
single-tool work that is the norm here.

Reminder: the system prompt forbids pushing to `main` without explicit
permission. This standing permission IS that explicit permission for the
in-scope work described above.

## What this repo is *not*

- Not production code. No tests required.
- Not a place for anything I'd be embarrassed to have break.
- Not a portfolio piece in the traditional sense — these are experiments.

If a request would push beyond these constraints (needs a server other than vibes-store, secrets, a build step), stop and ask before proceeding.