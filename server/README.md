# vibes-store

A tiny single-user JSON key-value API that backs the *gated* tools on
junk.timbornholdt.com (currently `house-gripes` and `tattoo-care`), so their
data syncs across your phone and laptop.

There is exactly one account: you. Auth is a single secret bearer token —
no users, no login, no expiry. Anyone with the token can read and write;
nobody without it can do either. Served over HTTPS behind nginx, that's the
whole security model. Right amount for a gripe list; don't store anything
you'd actually mind leaking.

Stdlib Python 3.7+, no pip installs. Runs on `127.0.0.1:8787`; nginx proxies
`/api/` to it.

## Files

- `vibes-store.py` — the server.
- `vibes-store.service` — systemd unit (assumes `/opt/vibes-store`, user `vibes`).

This `server/` directory is **excluded from the rsync deploy**
(`.github/workflows/deploy.yml`), so it never lands in the public web root.
You copy it onto the box by hand, once.

## Play-by-play install (run on the VPS as a sudo user)

```bash
# 1. Create a dedicated, login-less service user and the app dir.
sudo useradd --system --no-create-home --shell /usr/sbin/nologin vibes
sudo mkdir -p /opt/vibes-store/data

# 2. Copy the two files from this repo onto the box, into /opt/vibes-store/.
#    (scp from your laptop, or paste them in with an editor.)
#      /opt/vibes-store/vibes-store.py
#      /opt/vibes-store/vibes-store.service

# 3. Generate the secret token. Keep a copy — you'll paste it into the
#    browser the first time you open each gated tool.
openssl rand -hex 24 | sudo tee /opt/vibes-store/token
sudo chmod 600 /opt/vibes-store/token

# 4. Lock down ownership.
sudo chown -R vibes:vibes /opt/vibes-store

# 5. Install + start the service.
sudo cp /opt/vibes-store/vibes-store.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now vibes-store

# 6. Confirm it's up (expect: 401 with no token, 404 with the token).
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8787/api/store/house-gripes-v1
curl -s -o /dev/null -w '%{http_code}\n' \
  -H "Authorization: Bearer $(sudo cat /opt/vibes-store/token)" \
  http://127.0.0.1:8787/api/store/house-gripes-v1
```

## nginx

Add this inside the `server { ... }` block that serves junk.timbornholdt.com
(same block as the static site, so `/api/` is same-origin — no CORS):

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8787;
    proxy_set_header Host $host;
}
```

Then:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Verify from the public side (should be 401 — no token):

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://junk.timbornholdt.com/api/store/house-gripes-v1
```

## Using it

Open `house-gripes` or `tattoo-care`, paste the token once per device. The
token is remembered in `localStorage`; data syncs on load and on every change.
Once loaded, the tools keep working offline (PWA) from the local cache and
re-sync when you're back online. Conflicts are last-write-wins.

> **Note:** the value keys (`house-gripes-v1`, `tattoo-care-v1`) must match the
> `KEY` constant in each tool's HTML. If you rename one, rename both.

## Ops

```bash
sudo systemctl status vibes-store      # health
sudo journalctl -u vibes-store -f      # logs
sudo systemctl restart vibes-store     # restart

# Rotate the token (then re-enter it on each device):
openssl rand -hex 24 | sudo tee /opt/vibes-store/token >/dev/null
sudo chown vibes:vibes /opt/vibes-store/token && sudo chmod 600 /opt/vibes-store/token
sudo systemctl restart vibes-store
```

Data lives in `/opt/vibes-store/data/<key>.json` — back that up if you care
about it.
