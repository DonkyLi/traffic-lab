from __future__ import annotations

import hashlib
import hmac
from dataclasses import dataclass


@dataclass(frozen=True)
class FeishuCommand:
    kind: str
    text: str = ""


def parse_feishu_text(text: str) -> FeishuCommand:
    cleaned = text.strip()
    if cleaned.startswith("/需求"):
        return FeishuCommand("task", cleaned[len("/需求") :].strip())
    if cleaned.startswith("/状态"):
        return FeishuCommand("status", cleaned[len("/状态") :].strip())
    if cleaned.startswith("/暂停"):
        return FeishuCommand("pause", cleaned[len("/暂停") :].strip())
    return FeishuCommand("unknown", cleaned)


def verify_feishu_signature(body: bytes, secret: str, signature: str) -> bool:
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
