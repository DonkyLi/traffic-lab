from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    repo: str
    project_dir: str
    state_db: str
    feishu_verification_token: str = ""
    feishu_secret: str = ""
    feishu_webhook_url: str = ""
    allow_codex_execution: bool = False

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            repo=os.getenv("TRAFFIC_LAB_REPO", "DonkyLi/traffic-lab"),
            project_dir=os.getenv("TRAFFIC_LAB_PROJECT_DIR", "/Users/dongqi.li/game"),
            state_db=os.getenv("TRAFFIC_LAB_STATE_DB", ".orchestrator/state.db"),
            feishu_verification_token=os.getenv("FEISHU_VERIFICATION_TOKEN", ""),
            feishu_secret=os.getenv("FEISHU_SECRET", ""),
            feishu_webhook_url=os.getenv("FEISHU_WEBHOOK_URL", ""),
            allow_codex_execution=os.getenv("ORCHESTRATOR_ALLOW_CODEX", "0") == "1",
        )
