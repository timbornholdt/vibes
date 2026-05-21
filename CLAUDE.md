# Project conventions for timbornholdt/junk

This repo hosts low-stakes, vibe-coded HTML tools deployed to
https://junk.timbornholdt.com/ via auto-deploy.

## Where new tools go

- HTML tools live in `vibes/` and are accessible at `junk.timbornholdt.com/vibes/<filename>.html`.
- Use lowercase, hyphenated filenames (e.g. `image-cropper.html`, not `ImageCropper.html`).
- One file per tool. No subdirectories inside `vibes/` unless explicitly asked.

## Hard rules for tool files

- **Single self-contained HTML file.** Inline all CSS and JavaScript. No build step, no bundler, no separate `.css` or `.js` files.
- **No React, no JSX, no frameworks that require a build step.** Plain HTML, vanilla JS, and CSS only.
- **External libraries via CDN only**, pinned to a specific version (cdnjs or jsDelivr). Prefer no dependencies at all when reasonable.
- **No backend, no API keys baked in, no server calls that require secrets.** Everything runs in the browser. If a tool needs an API key, prompt the user to paste their own and store it in `localStorage`.
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
- Include a small footer linking back to the source on GitHub:
  `<a href="https://github.com/timbornholdt/junk/blob/main/vibes/<filename>.html">view source</a>`

## Commit messages

When committing a new tool or significant edit, include in the commit message:
- A one-line summary of what the tool does
- The original prompt (or a link to the chat transcript) that produced the change

This is the provenance trail — it's how I'll know later what was asked for and why.

## Update index page

It's crucial that every new page to this repo is represented with a link on the index.html page. When you make a meaningful update to an existing tool, also bump that tool's `last deployed` date to today.

Format:

```html
    <a class="item" href="patio.html">
      <div class="item-row">
        <span class="item-title">[name of project]</span>
        <span class="item-tag">[appropriate tag(s), make something up that feels right]</span>
      </div>
      <div class="item-desc">[pithy description of what this tool does, two sentence max.]</div>
      <div class="item-date">last deployed [today's date, e.g. last deployed may 10, 2026]</div>
    </a>
```

Insert this block at the top of the list when adding a new tool. Use lowercase month names with a numeric day and year (e.g. `last deployed may 10, 2026`). Older entries that pre-date this convention can keep their existing date strings — don't backfill them retroactively.

## Shipping

This repo auto-deploys to https://junk.timbornholdt.com/ when changes land on
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

If a request would push beyond these constraints (needs a server, secrets, persistence beyond localStorage, multi-file structure), stop and ask before proceeding.