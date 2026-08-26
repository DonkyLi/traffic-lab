from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .config import Config
from .feishu import FeishuAdapter
from .github_cli import GitHubCLI
from .store import TaskStore


class Orchestrator:
    def __init__(self, config: Config):
        self.config = config
        Path(config.state_db).parent.mkdir(parents=True, exist_ok=True)
        self.store = TaskStore(config.state_db)
        self.github = GitHubCLI(config.repo)
        self.feishu = FeishuAdapter(config.feishu_webhook_url)

    def ingest_feishu_text(self, text: str, event_id: str) -> str:
        command = self.feishu.parse_command(text)
        if command.kind != "task" or not command.text:
            return command.kind
        task_id = "feishu-" + hashlib.sha256(event_id.encode()).hexdigest()[:16]
        self.store.create(task_id, command.text, "director")
        self.github.create_issue(
            title=f"[自动任务] {command.text[:70]}",
            body=f"来源：飞书事件 `{event_id}`\n\n{command.text}\n\n由 orchestrator 自动创建。",
            labels=["status:ready"],
        )
        self.feishu.notify(f"已创建自动任务：{command.text}\n任务 ID：{task_id}")
        return task_id

    def status_text(self) -> str:
        return json.dumps(
            {"repository": self.config.repo, "state_db": self.config.state_db},
            ensure_ascii=False,
        )
