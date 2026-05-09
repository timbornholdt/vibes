# vibes

Personal project launchpad at `junk.timbornholdt.com/vibes`. A collection of one-off ideas, guides, and tools — accessible from iPhone home screen as a PWA.

## Structure

```
/                   ← index (PWA shell, lists all projects)
/lofi-guide.html
/music-syllabus.html
/patio.html
/ps2-curriculum.html
/manifest.json      ← PWA manifest
/sw.js              ← service worker (cache-first)
/icon.svg           ← punk profile silhouette icon
/private/           ← gitignored (local-only projects)
```

## Adding a project

1. Drop your `.html` file (or folder) in the repo root
2. Add an `<a class="item">` block to `index.html` following the existing pattern
3. Commit and push to `main` — deploys automatically

## Deploy

GitHub Actions → rsync over SSH on every push to `main`.

**Required GitHub Secrets:**
| Secret | Value |
|---|---|
| `VPS_HOST` | server hostname or IP |
| `VPS_USER` | SSH user |
| `VPS_PATH` | absolute path on server (e.g. `/var/www/junk.timbornholdt.com/vibes`) |
| `SSH_PRIVATE_KEY` | contents of deploy private key |

**One-time VPS setup:**
```bash
ssh-keygen -t ed25519 -f ~/.ssh/vibes_deploy -C "vibes-deploy"
# copy vibes_deploy.pub to VPS ~/.ssh/authorized_keys
# add vibes_deploy (private) as GitHub Secret SSH_PRIVATE_KEY
```

## PWA / iPhone install

Open `junk.timbornholdt.com/vibes` in Safari → Share → Add to Home Screen.
Launches full-screen, works offline for the index shell.

## Design

Terminal/zine aesthetic. WWWY 2023 palette: `#FFE600` yellow, `#FF2D78` pink, `#39FF14` green, `#0A0A0A` black. Monospace only.
