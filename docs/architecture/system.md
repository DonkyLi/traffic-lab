# Initial system boundary

```text
editor commands → design model → topology compiler → simulation backend → read-only snapshot → Godot UI/rendering
```

The simulation core must not depend on Godot scene nodes. The client must consume simulation snapshots rather than reimplementing traffic rules. The first traffic backend should be a deterministic mesoscopic flow model; a more detailed vehicle backend can be added later behind the same interface.

## Shared context rule

The documents in `docs/product/` define player-facing intent. The documents in `docs/architecture/` define technical boundaries. If implementation and documentation disagree, stop and create a decision record before proceeding.
