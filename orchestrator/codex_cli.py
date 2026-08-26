from __future__ import annotations


def build_codex_command(worktree: str, prompt: str) -> list[str]:
    return ["codex", "exec", "--json", "--cd", worktree, prompt]
