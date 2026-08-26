from __future__ import annotations

import subprocess
from pathlib import Path

from .codex_cli import build_codex_command
from .config import Config
from .store import Task, TaskStore
from .worker import build_role_command


class CodexRunner:
    def __init__(self, config: Config):
        self.config = config

    def run(self, role: str, issue_body: str, issue_number: str) -> subprocess.CompletedProcess[str]:
        branch = f"agent/{role}/{issue_number}-automation"
        worktree = Path(self.config.project_dir).parent / f"traffic-lab-{role}-{issue_number}"
        subprocess.run(
            ["git", "worktree", "add", "-B", branch, str(worktree), "main"],
            cwd=self.config.project_dir,
            check=True,
            capture_output=True,
            text=True,
        )
        command = build_role_command(self.config.project_dir, role, str(worktree), issue_body)
        return subprocess.run(command, cwd=self.config.project_dir, capture_output=True, text=True)


class TaskWorker:
    def __init__(self, config: Config, runner: CodexRunner | None = None):
        self.config = config
        self.store = TaskStore(config.state_db)
        self.runner = runner or CodexRunner(config)

    def process_one(self, role: str = "director") -> Task | None:
        task = self.store.claim_ready(role)
        if task is None:
            return None
        if not self.config.allow_codex_execution:
            self.store.mark_failed(task.id, "Codex execution disabled; set ORCHESTRATOR_ALLOW_CODEX=1")
            return self.store.get(task.id)
        self.store.mark_running(task.id)
        result = self.runner.run(role, task.text, task.id)
        if result.returncode == 0:
            self.store.mark_done(task.id)
        else:
            self.store.mark_failed(task.id, result.stderr[-2000:] or "codex exited non-zero")
        return self.store.get(task.id)
