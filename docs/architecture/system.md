# Initial system boundary

```text
editor commands → design model → topology compiler → simulation backend → read-only snapshot → Godot UI/rendering
```

The simulation core must not depend on Godot scene nodes. The client must consume simulation snapshots rather than reimplementing traffic rules. The first traffic backend should be a deterministic mesoscopic flow model; a more detailed vehicle backend can be added later behind the same interface.
