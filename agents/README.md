# Codex agent prompts

These prompts are the role definitions for the first four Traffic Lab agents. Copy the relevant prompt into a Codex sub-agent when starting a task. They are intentionally repository-owned so the team shares the same instructions.

## GitHub connection

- Repository: `DonkyLi/traffic-lab`
- Remote: `git@github.com:DonkyLi/traffic-lab.git`
- Default branch: `main`
- Web: `https://github.com/DonkyLi/traffic-lab`
- Issue and PR templates live in `.github/`.

Agents must use the existing local GitHub authentication. Do not place GitHub tokens, SSH private keys, Feishu secrets, or other credentials in prompts, source files, Issues, or PRs. Before GitHub operations, verify the local session with `gh auth status` or the configured SSH identity.

## Branch policy

Use one branch per task and never work directly on `main`:

```text
agent/director/<issue-number>-<short-name>
agent/traffic/<issue-number>-<short-name>
agent/client/<issue-number>-<short-name>
agent/qa/<issue-number>-<short-name>
```

Open a PR against `main`. A task is not complete until the PR contains its verification evidence and the required checks pass.

## Task hand-off

Every agent report must include:

1. What changed.
2. Files changed.
3. Tests or checks run and their results.
4. Known risks and intentionally deferred work.
5. The GitHub Issue and PR numbers.
