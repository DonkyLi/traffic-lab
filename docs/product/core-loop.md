# Core loop

Traffic Lab is built around a short, repeatable engineering loop:

```text
read brief → design roads → run traffic → diagnose bottleneck → revise → rerun → compare
```

## Read the brief

The player receives a small map, vehicle demand between portals, constraints, a budget, and transparent target metrics.

## Design roads

The player works in a paused state. Roads can be drawn, connected, split, deleted, redirected, and configured with a small number of lane and intersection-control presets. Every change previews its cost and can be undone.

## Run traffic

The scenario runs with a fixed seed at 1×, 2×, or 4× speed. Pausing is immediate. In challenge mode, changing the network schedules a rerun from the same seed so comparisons remain fair and understandable.

## Diagnose the bottleneck

The player can switch between flow, speed/delay, queue, and demand-path overlays. Clicking a problem area must explain where the capacity is insufficient, whether signal waiting or downstream blocking is involved, and which demand is affected.

## Revise and compare

The player changes the network, reruns the same demand, and compares the new result with the previous design. Failure is a diagnostic state, not a long penalty or an irreversible loss.

## Core success signal

The loop works when a new player can build a runnable network quickly, identify at least one cause of congestion, make a change, and observe an understandable metric improvement within the same session.
