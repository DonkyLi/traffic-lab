# BOOT-001 vertical-slice scenario contract

This document fixes the smallest end-to-end scenario used to validate the
`plan roads → run traffic → diagnose bottlenecks → revise → rerun` loop. It is
scenario content and an observability contract; it does not introduce a new
score, medal rule, or runtime data type.

## Scenario identity and map

- Scenario ID: `boot-001-two-portal-crossing`.
- Coordinate space: a 12 × 8 orthogonal tile map, with `(0, 0)` at the
  north-west corner. Roads are drawn on tile edges and may be edited while
  paused.
- Buildable area: the full rectangle. No buildings, population, or decorative
  blockers are part of this slice.
- The map has **exactly two portals**:
  - `portal-west` (`entry`): west edge at `(0, 4)`.
  - `portal-east` (`exit`): east edge at `(11, 4)`.
- There are no implicit portals, turn-around exits, or alternate demand
  endpoints. A valid run must connect the two named portals through the
  player-designed road network.

The initial blank map is intentional: the player must make the network
decision. A reference solution may be used by tests or demonstrations, but is
not part of the player's starting design.

## Fixed demand and determinism

The scenario contains one and only one demand row:

| Field | Value |
| --- | --- |
| Demand ID | `demand-west-east-01` |
| Origin | `portal-west` |
| Destination | `portal-east` |
| Vehicles | 60 cars total |
| Release window | simulation seconds 0–59, one vehicle per second |
| Seed | `424242` |

Every run of an unchanged design uses the same seed and release schedule.
Changing the road design starts a new comparison run with the same seed; it
does not silently change demand, add vehicles, or reroll endpoints. The
simulation may be viewed at 1×, 2×, or 4× speed, but speed only affects
presentation time.

## Transparent indicators

The run summary and the on-map overlays expose these raw, reproducible values
for the single demand (not a hidden composite score):

- **Throughput**: number of the 60 released vehicles that reach
  `portal-east` by simulation second 120; also show the completion fraction.
- **Latency**: per-vehicle origin-to-destination travel time in simulation
  seconds; show mean and p95 for completed vehicles, plus the count of
  incomplete vehicles.
- **Queue**: queued vehicles at each controlled movement; show current and
  maximum queue length, and the map-wide maximum over the run.
- **Backlog**: released vehicles not yet completed at second 120. This is
  displayed alongside throughput so a player can distinguish low demand from
  a blocked route.

The overlays are labelled `flow`, `delay`, `queue`, and `demand path` to match
the core-loop terminology. Clicking a queue hotspot identifies the affected
demand (`demand-west-east-01`) and whether waiting is attributable to signal
service or downstream blocking when that explanation is available.

## Validation targets (not scoring rules)

For a smoke-test/reference run, the transparent indicators should make it
possible to observe the following targets:

- throughput: 60/60 completed;
- mean latency: ≤ 30 s;
- p95 latency: ≤ 45 s;
- maximum queue: ≤ 12 vehicles;
- backlog: 0 at second 120.

These targets are acceptance evidence for the vertical slice only. They must
not be turned into player score, medals, or failure penalties without a
separate product decision and architecture note. A deliberately poor road
layout is expected to miss one or more targets and remain a useful diagnostic
state.

## Contract boundaries

This contract uses the existing `Portal`, `Demand`, `Scenario`, and read-only
snapshot concepts in [data-contract.md](../architecture/data-contract.md) and
the editor → topology → simulation → snapshot boundary in
[system.md](../architecture/system.md). It does not require changes to those
schemas. Any implementation that needs additional fields, new scoring, or a
third portal must stop and request a decision record.
