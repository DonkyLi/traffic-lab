from __future__ import annotations

from pathlib import Path

from .codex_cli import build_codex_command


def role_prompt(project_dir: str | Path, role: str) -> str:
    path = Path(project_dir) / "agents" / f"{role}.md"
    return path.read_text(encoding="utf-8")


def task_prompt(role: str, issue_body: str) -> str:
    return f"""你是角色 {role}。这是自动化执行任务，不要等待人工转发。\n\nGitHub Issue：\n{issue_body}\n\n完成后必须创建或更新 GitHub PR，并在报告中写明测试证据、风险和下一步。\n"""


def build_role_command(project_dir: str | Path, role: str, worktree: str, issue_body: str) -> list[str]:
    prompt = role_prompt(project_dir, role) + "\n\n" + task_prompt(role, issue_body)
    return build_codex_command(worktree, prompt)
