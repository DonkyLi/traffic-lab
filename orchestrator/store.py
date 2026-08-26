from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Task:
    id: str
    text: str
    role: str
    status: str
    attempts: int
    error: str | None = None


class TaskStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        self._init_db()

    def _connect(self):
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection

    def _init_db(self):
        with self._connect() as connection:
            connection.execute(
                """CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    text TEXT NOT NULL,
                    role TEXT NOT NULL,
                    status TEXT NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0,
                    error TEXT
                )"""
            )

    def create(self, task_id: str, text: str, role: str) -> Task:
        with self._connect() as connection:
            connection.execute(
                "INSERT OR IGNORE INTO tasks(id,text,role,status) VALUES(?,?,?,'ready')",
                (task_id, text, role),
            )
        return self.get(task_id)

    def get(self, task_id: str) -> Task:
        with self._connect() as connection:
            row = connection.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if row is None:
            raise KeyError(task_id)
        return Task(**dict(row))

    def claim_ready(self, role: str) -> Task | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM tasks WHERE role=? AND status='ready' ORDER BY rowid LIMIT 1",
                (role,),
            ).fetchone()
            if row is None:
                return None
            connection.execute("UPDATE tasks SET status='claimed' WHERE id=?", (row["id"],))
        return self.get(row["id"])

    def mark_running(self, task_id: str):
        self._set(task_id, "running")

    def mark_done(self, task_id: str):
        self._set(task_id, "done", None)

    def mark_failed(self, task_id: str, error: str):
        with self._connect() as connection:
            connection.execute(
                "UPDATE tasks SET status='failed', attempts=attempts+1, error=? WHERE id=?",
                (error, task_id),
            )

    def _set(self, task_id: str, status: str, error: str | None = None):
        with self._connect() as connection:
            connection.execute("UPDATE tasks SET status=?, error=? WHERE id=?", (status, error, task_id))

    def count(self) -> int:
        with self._connect() as connection:
            return connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
