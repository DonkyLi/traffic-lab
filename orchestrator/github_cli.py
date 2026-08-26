from __future__ import annotations

import subprocess


def build_issue_command(repo: str, title: str, body: str, labels: list[str]) -> list[str]:
    command = ["gh", "issue", "create", "--repo", repo, "--title", title, "--body", body]
    for label in labels:
        command.extend(["--label", label])
    return command


class GitHubCLI:
    def __init__(self, repo: str):
        self.repo = repo

    def create_issue(self, title: str, body: str, labels: list[str] | None = None) -> str:
        command = build_issue_command(self.repo, title, body, labels or [])
        return subprocess.check_output(command, text=True).strip()

    def list_ready_issues(self) -> list[dict]:
        command = ["gh", "issue", "list", "--repo", self.repo, "--label", "status:ready", "--json", "number,title,body"]
        import json

        return json.loads(subprocess.check_output(command, text=True))
