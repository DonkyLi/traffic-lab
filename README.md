# Traffic Lab

Traffic Lab is a road-traffic planning game about designing a network, running a fixed traffic demand, finding bottlenecks, and improving the design.

> 把路画出来，让车流给答案。

The first milestone is intentionally small: desktop-first, car traffic only, deterministic scenarios, explainable congestion, and a fast plan → run → diagnose → rerun loop.

## Repository status

This repository is at the project bootstrap stage. The initial product and agent architecture are being documented before implementation begins.

## Planned top-level areas

```text
docs/       Product and architecture decisions
game/       Domain, simulation, client, and scenario code
tests/      Headless, integration, replay, and performance tests
reports/    Playtest and benchmark reports
```

## Collaboration

See [AGENTS.md](AGENTS.md) for the shared rules used by Codex agents. All code changes go through GitHub branches and pull requests.

Role prompts and GitHub hand-off rules are in [`agents/`](agents/README.md).
