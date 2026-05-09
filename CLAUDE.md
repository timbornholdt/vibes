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

It's crucial that every new page to this repo is represented with a link on the index.html page.

Format:

```html
    <a class="item" href="patio.html">
      <div class="item-row">
        <span class="item-title">[name of project]</span>
        <span class="item-tag">[appropriate tag(s), make something up that feels right]</span>
      </div>
      <div class="item-desc">[pithy description of what this tool does, two sentence max.]</div>
      <div class="item-date">[current month/year, e.g. may 2026]</div>
    </a>
```

Insert this block at the top of the list.

## What this repo is *not*

- Not production code. No tests required.
- Not a place for anything I'd be embarrassed to have break.
- Not a portfolio piece in the traditional sense — these are experiments.

If a request would push beyond these constraints (needs a server, secrets, persistence beyond localStorage, multi-file structure), stop and ask before proceeding.