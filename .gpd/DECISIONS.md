# Decisions

Append-only decision log.

| Date | Phase | Decision | Rationale | Rollback Trigger | Status |
| ---- | ----- | -------- | --------- | ---------------- | ------ |
| `2026-04-23` | `00` | Keep `gnosis-indus` as an anchor application and evidence repo | corrected workstream set ranks it as the evidence-bearing anchor, not the lead thesis | new control-plane evidence demotes the lane further | `RATIFIED` |
| `2026-04-23` | `00` | Keep search-without-decode inside this repo | current evidence supports an application surface, not a sovereign repo | a later evidence program proves a clean independent moat | `RATIFIED` |
| `2026-04-23` | `00` | Preserve the Phase 4 stability caveat in all front-door docs | packaging cannot outrun the authority docs | a stronger authority source explicitly closes the caveat | `RATIFIED` |
| `2026-04-24` | `01` | First extraction slice chosen: `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/` | lowest rights-gate risk (derived cluster IDs only, no images), smallest helper-dependency footprint (catalogue JSON plus query list), cleanest stronger-smoke-path story (instantiable query engine with Track C latency and compression gates); Phase 4 catalogue and Phase 5 falsification families sequenced as explicit second and third waves | Phase 02 extraction uncovers a dependency on a rights-gated asset family that makes the slice unshippable | `RATIFIED` |
