# Automated agent orchestrator

This repository contains a local automation service under `orchestrator/`.

## What it automates

```text
Feishu event → GitHub Issue → persistent task → Codex CLI role run → branch/PR evidence → Feishu notification
```

The service uses the existing local `gh` and `codex` authentication. It never stores credentials in the repository.

## Safe local smoke test

```bash
cd /Users/dongqi.li/game
PYTHONPATH=. python3 -m orchestrator status
PYTHONPATH=. python3 -m orchestrator ingest '/需求 做一个 L1 道路连接关卡' --event-id local-test-1
```

## Start the webhook receiver

```bash
export TRAFFIC_LAB_PROJECT_DIR=/Users/dongqi.li/game
export FEISHU_VERIFICATION_TOKEN='value-from-feishu'
export FEISHU_WEBHOOK_URL='https://open.feishu.cn/open-apis/bot/v2/hook/…'
PYTHONPATH=. python3 -m orchestrator serve
```

Expose port `8787` through an HTTPS tunnel or a deployed service, then use that HTTPS URL plus `/feishu/events` in the Feishu developer console. A local-only `127.0.0.1` URL is not reachable by Feishu.

## Start the worker

The worker is intentionally disabled by default. After verifying the webhook and GitHub behavior, set:

```bash
export ORCHESTRATOR_ALLOW_CODEX=1
PYTHONPATH=. python3 -m orchestrator worker --role director
```

Run the worker under a process supervisor or scheduler for continuous processing. The next automation iteration should add a long-running polling loop, GitHub webhook handling, subtask extraction from director output, retry backoff, and explicit human approval gates before merging or publishing.

## Important boundary

The current Codex desktop project list is not itself a message bus. The orchestrator is the component that turns those role prompts into non-interactive `codex exec` runs. Feishu credentials and a reachable HTTPS endpoint are required for live Feishu activation.
