import tempfile
import unittest
from pathlib import Path

from orchestrator.store import TaskStore


class StoreTests(unittest.TestCase):
    def test_task_lifecycle_and_retry_count(self):
        with tempfile.TemporaryDirectory() as directory:
            store = TaskStore(Path(directory) / "state.db")
            task = store.create("task-1", "做一个 L1 道路连接关卡", "director")
            self.assertEqual(task.status, "ready")
            claimed = store.claim_ready("director")
            self.assertEqual(claimed.id, "task-1")
            store.mark_running("task-1")
            store.mark_failed("task-1", "codex exited 1")
            failed = store.get("task-1")
            self.assertEqual(failed.status, "failed")
            self.assertEqual(failed.attempts, 1)

    def test_idempotent_create_returns_existing_task(self):
        with tempfile.TemporaryDirectory() as directory:
            store = TaskStore(Path(directory) / "state.db")
            first = store.create("same-event", "同一个任务", "director")
            second = store.create("same-event", "重复任务", "director")
            self.assertEqual(first.id, second.id)
            self.assertEqual(store.count(), 1)


if __name__ == "__main__":
    unittest.main()
