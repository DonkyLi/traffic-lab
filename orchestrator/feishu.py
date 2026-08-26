from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass

from .protocol import FeishuCommand, parse_feishu_text


@dataclass(frozen=True)
class FeishuEvent:
    kind: str
    text: str = ""
    event_id: str = ""


def parse_event(payload: dict, verification_token: str) -> FeishuEvent:
    if payload.get("challenge") is not None:
        if verification_token and payload.get("token") != verification_token:
            raise ValueError("invalid Feishu verification token")
        return FeishuEvent("challenge", str(payload["challenge"]))
    event = payload.get("event", {})
    message = event.get("message", {})
    content = message.get("content", "")
    try:
        text = json.loads(content).get("text", "")
    except (json.JSONDecodeError, TypeError):
        text = content
    return FeishuEvent("message", text, payload.get("header", {}).get("event_id", ""))


class FeishuAdapter:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def parse_command(self, text: str) -> FeishuCommand:
        return parse_feishu_text(text)

    def notify(self, text: str) -> None:
        if not self.webhook_url:
            return
        payload = json.dumps({"msg_type": "text", "content": {"text": text}}).encode()
        request = urllib.request.Request(
            self.webhook_url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=15):
            pass
