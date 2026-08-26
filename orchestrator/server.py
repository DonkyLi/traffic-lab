from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from .config import Config
from .feishu import parse_event
from .service import Orchestrator
from .runner import TaskWorker


class Handler(BaseHTTPRequestHandler):
    orchestrator: Orchestrator
    config: Config

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body.decode("utf-8"))
            event = parse_event(payload, self.config.feishu_verification_token)
            if event.kind == "challenge":
                self._json(200, {"challenge": event.text})
                return
            task_id = self.orchestrator.ingest_feishu_text(event.text, event.event_id or "missing-event-id")
            self._json(200, {"ok": True, "task_id": task_id})
        except (ValueError, json.JSONDecodeError) as exc:
            self._json(400, {"ok": False, "error": str(exc)})

    def _json(self, status: int, payload: dict):
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, *_args):
        return


def serve(config: Config, host: str = "127.0.0.1", port: int = 8787):
    Handler.config = config
    Handler.orchestrator = Orchestrator(config)
    if config.allow_codex_execution:
        worker = TaskWorker(config)
        threading.Thread(target=worker.run_forever, name="codex-worker", daemon=True).start()
    HTTPServer((host, port), Handler).serve_forever()
