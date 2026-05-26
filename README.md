```
                                                              
                  _/       _/                                 
 _/      _/               _/_/_/        _/_/         _/_/_/   
_/      _/      _/       _/    _/    _/_/_/_/     _/_/        
 _/  _/        _/       _/    _/    _/               _/_/     
  _/          _/       _/_/_/        _/_/_/     _/_/_/        
                                                              
                                                              
```

Personal project launchpad at `junk.timbornholdt.com/vibes`. A collection of one-off ideas, guides, and tools — accessible from iPhone home screen as a PWA.

## Adding a project

1. Drop your `.html` file in the repo root
2. Add an entry to the `tools` array in `index.html` (`file`, `title`, `cat`, `desc`)
3. Draw an SVG icon for it and add it to the `icons` map in `index.html` — see [Icons](#icons) (required)
4. Commit and push to `main` — deploys automatically

## Icons

Every page on the index gets a hand-made SVG icon representing what it does —
**no auto-generated page thumbnails.** Add it to the `icons` object in
`index.html`, keyed by filename. Conventions:

- `0 0 96 96` viewBox, simple line art.
- Use `stroke="currentColor"` (and `fill="currentColor"` for solid bits) so the
  card automatically tints the icon with its category color.
- Aim for one clear, recognizable concept per icon (e.g. a vinyl record, a skull,
  a game controller) rather than literal screenshots.

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
