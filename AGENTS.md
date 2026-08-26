# Traffic Lab Agent Rules

## Product boundary

Traffic Lab is a desktop-first road-traffic planning game. The current milestone is a small, deterministic car-traffic loop:

`plan roads → run traffic → diagnose bottlenecks → revise → rerun`

Do not add buildings, population, economy, pedestrians, public transit, rail, aircraft, multiplayer, or complex 3D before the core loop is validated.

## Collaboration rules

- `main` is protected; work through a branch and pull request.
- Read the relevant files in `docs/` before changing behavior.
- Every task must state its scope, acceptance criteria, tests, and known risks.
- Do not modify another agent's owned area without an explicit interface change in the task.
- Prefer small, reversible changes. Do not delete tests to make a task pass.
- Product, scoring, and domain-model changes require human approval.

## Source of truth

- Product intent lives in `docs/product/`.
- Architecture decisions live in `docs/architecture/decisions/`.
- Code and tests are the implementation evidence.
- Generated caches and rendered artifacts are not authoritative.

## Quality bar

Changes are complete only when the relevant tests pass and the pull request records what changed, what was verified, and what remains intentionally out of scope.
