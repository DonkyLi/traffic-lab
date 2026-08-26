# Initial data contract

This is a bootstrap contract, not an implementation commitment. Changes require an architecture decision and a migration note.

## Authoritative design data

- `RoadAsset`: stable ID, centerline geometry, direction, lane count, speed limit, and cost.
- `JunctionAsset`: stable ID, control type, signal phases, and allowed movements.
- `Portal`: stable ID and entry/exit role.
- `Demand`: origin, destination, vehicle count or rate, time window, and seed.
- `Scenario`: design data, constraints, objectives, medal rules, and seed.

## Derived runtime data

- `TopologySnapshot`: lanes, movements, conflicts, and indices compiled from design data.
- `SimulationSnapshot`: read-only metrics and render state for a simulation tick.

Derived data is disposable. Saves must preserve the design model, schema version, seed, and command history or equivalent editable state.
