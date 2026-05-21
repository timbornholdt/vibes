#!/usr/bin/env python3
"""
vibes-store: a tiny single-user JSON key-value API for junk.timbornholdt.com.

There is exactly one account (the repo owner). Every request must carry
  Authorization: Bearer <token>
where <token> matches the secret in the token file. There is no user table,
no login, no expiry — possession of the token is the whole auth model.

Routes (mounted at /api/ via nginx reverse proxy):
  GET  /api/store/<key>   -> 200 {"value": <json>, "updatedAt": <ms>} | 404
  PUT  /api/store/<key>   -> 200 {"ok": true, "updatedAt": <ms>}
                             body: {"value": <json>, "updatedAt": <ms?>}

Storage: one file per key at <data dir>/<key>.json, written atomically.

Config (environment variables):
  VIBES_STORE_TOKEN_FILE  path to a file containing the secret token (required)
  VIBES_STORE_DATA_DIR    directory for the JSON files       (default ./data)
  VIBES_STORE_HOST        bind address              (default 127.0.0.1)
  VIBES_STORE_PORT        bind port                 (default 8787)

Stdlib only — no pip installs. Python 3.7+.
"""

import hmac
import json
import os
import re
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
MAX_BODY = 5 * 1024 * 1024  # 5 MB ceiling per blob

HOST = os.environ.get("VIBES_STORE_HOST", "127.0.0.1")
PORT = int(os.environ.get("VIBES_STORE_PORT", "8787"))
DATA_DIR = os.environ.get("VIBES_STORE_DATA_DIR", "data")
TOKEN_FILE = os.environ.get("VIBES_STORE_TOKEN_FILE")


def load_token():
    if not TOKEN_FILE:
        sys.exit("VIBES_STORE_TOKEN_FILE is not set")
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            token = f.read().strip()
    except OSError as e:
        sys.exit(f"cannot read token file {TOKEN_FILE}: {e}")
    if not token:
        sys.exit(f"token file {TOKEN_FILE} is empty")
    return token


TOKEN = load_token()


def now_ms():
    import time
    return int(time.time() * 1000)


class Handler(BaseHTTPRequestHandler):
    server_version = "vibes-store/1"

    # Quieter logs: one line, to stderr.
    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _authed(self):
        header = self.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return False
        presented = header[len("Bearer "):].strip()
        return hmac.compare_digest(presented, TOKEN)

    def _key_from_path(self):
        # Expect exactly /api/store/<key>
        path = self.path.split("?", 1)[0]
        prefix = "/api/store/"
        if not path.startswith(prefix):
            return None
        key = path[len(prefix):]
        if not KEY_RE.match(key):
            return None
        return key

    def _file_for(self, key):
        return os.path.join(DATA_DIR, key + ".json")

    def do_GET(self):
        if not self._authed():
            return self._send(401, {"error": "unauthorized"})
        key = self._key_from_path()
        if key is None:
            return self._send(404, {"error": "not found"})
        path = self._file_for(key)
        if not os.path.exists(path):
            return self._send(404, {"error": "no value"})
        try:
            with open(path, "r", encoding="utf-8") as f:
                stored = json.load(f)
        except (OSError, ValueError):
            return self._send(500, {"error": "read failed"})
        return self._send(200, stored)

    def do_PUT(self):
        if not self._authed():
            return self._send(401, {"error": "unauthorized"})
        key = self._key_from_path()
        if key is None:
            return self._send(404, {"error": "not found"})

        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0 or length > MAX_BODY:
            return self._send(400, {"error": "bad body length"})
        raw = self.rfile.read(length)
        try:
            incoming = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return self._send(400, {"error": "invalid json"})
        if not isinstance(incoming, dict) or "value" not in incoming:
            return self._send(400, {"error": "missing value"})

        updated_at = incoming.get("updatedAt")
        if not isinstance(updated_at, (int, float)):
            updated_at = now_ms()
        record = {"value": incoming["value"], "updatedAt": int(updated_at)}

        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            fd, tmp = tempfile.mkstemp(dir=DATA_DIR, suffix=".tmp")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(record, f)
            os.replace(tmp, self._file_for(key))
        except OSError:
            return self._send(500, {"error": "write failed"})
        return self._send(200, {"ok": True, "updatedAt": record["updatedAt"]})


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    sys.stderr.write(f"vibes-store listening on {HOST}:{PORT}, data in {DATA_DIR}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    main()
