import unittest

from orchestrator.github_cli import build_issue_command
from orchestrator.codex_cli import build_codex_command


class CommandTests(unittest.TestCase):
    def test_github_issue_command_contains_repository_and_labels(self):
        command = build_issue_command(
            "DonkyLi/traffic-lab", "做一个 L1 关卡", "需求正文", ["status:ready"]
        )
        self.assertEqual(command[:3], ["gh", "issue", "create"])
        self.assertIn("--repo", command)
        self.assertIn("DonkyLi/traffic-lab", command)
        self.assertIn("status:ready", command)

    def test_codex_command_is_non_interactive_and_pinned_to_worktree(self):
        command = build_codex_command("/tmp/worktree", "执行 Issue #1")
        self.assertEqual(command[:2], ["codex", "exec"])
        self.assertIn("--cd", command)
        self.assertIn("/tmp/worktree", command)
        self.assertIn("--json", command)


if __name__ == "__main__":
    unittest.main()
