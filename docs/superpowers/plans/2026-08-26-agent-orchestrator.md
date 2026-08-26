# Agent Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automate Feishu → GitHub Issue → Codex role execution → GitHub result updates without manual message forwarding.

**Architecture:** A small Python standard-library service receives signed Feishu events, creates and tracks GitHub Issues through the authenticated `gh` CLI, invokes isolated Codex CLI runs for role agents, persists task state in SQLite, and posts concise status updates back to Feishu. GitHub remains the code and review source of truth.

**Tech Stack:** Python 3.11+, `sqlite3`, `http.server`, `urllib`, GitHub CLI, Codex CLI, Git worktrees.

---

## Scope

- Implement a tested task/state protocol and SQLite store.
- Implement GitHub CLI and Codex CLI adapters with injectable runners.
- Implement Feishu event verification, command parsing, and notification adapter.
- Implement a local HTTP service and a one-shot worker loop.
- Keep live credentials out of the repository.
- Do not claim live Feishu delivery until credentials and a reachable webhook are configured.
