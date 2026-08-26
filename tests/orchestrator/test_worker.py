import tempfile
import unittest
from pathlib import Path

from orchestrator.worker import role_prompt, task_prompt


class WorkerTests(unittest.TestCase):
    def test_role_prompt_reads_repository_role_definition(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "agents").mkdir()
            (root / "agents" / "traffic.md").write_text("TRAFFIC ROLE", encoding="utf-8")
            self.assertEqual(role_prompt(root, "traffic"), "TRAFFIC ROLE")

    def test_task_prompt_contains_issue_and_unattended_constraints(self):
        prompt = task_prompt("traffic", "ISSUE-7 body")
        self.assertIn("ISSUE-7 body", prompt)
        self.assertIn("不要等待人工转发", prompt)
        self.assertIn("GitHub PR", prompt)


if __name__ == "__main__":
    unittest.main()
