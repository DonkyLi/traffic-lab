# Non-goals for the first milestone

These items are intentionally excluded until the road-planning loop has been validated with playtests.

## Simulation and content

- Buildings, zoning, population, jobs, taxes, land value, maintenance, or city finances.
- Pedestrians, bicycles, buses, trains, aircraft, ships, or multimodal transfers.
- Realistic collision physics, parking, garages, accidents, weather, day/night, or emergency events.
- Complex interchanges, elevation, tunnels, bridges, procedural infinite maps, or a full 3D city.

## Product and platform

- Multiplayer, live collaboration, cloud saves, modding, workshop integration, or user scripting.
- Mobile and touch-first input; desktop keyboard and mouse are the first target.
- Story campaign, decorative asset catalogue, achievements, monetization, or live-service systems.

## Technical shortcuts we will not take

- Do not make the UI reimplement traffic rules.
- Do not use disconnected roads or rejected demand as a scoring exploit.
- Do not replace tests with manual claims of correctness.
- Do not add a new subsystem unless it creates a meaningful player decision and an observable, testable result.

These non-goals can be revisited through an explicit product decision recorded in `docs/architecture/decisions/`.
