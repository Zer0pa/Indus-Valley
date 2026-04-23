# Research State

## Project Reference

See: `.gpd/PROJECT.md`

**Core research or build question:** Can `gnosis-indus` be migrated into a
truthful standalone anchor application and evidence repo without losing the
scientific caveats that justify the lane?
**Current focus:** Phase 01 is complete. The first extraction slice is named
(search-without-decode). The repo is ready for Phase 02 to land real runtime
code under `src/gnosis_indus/search_surface/`.

## Current Position

**Current Phase:** `01`
**Current Phase Name:** Source Truth And Authority Admission
**Total Phases:** `4`
**Current Plan:** `1`
**Total Plans In Phase:** `1`
**Status:** `COMPLETE`
**Status Detail:** Phase 01 Plan 01 executed end-to-end. Source ledger
frozen, data posture tightened, first extraction slice chosen, stronger
Phase 02 smoke expectation declared. The orchestrator may advance to
Phase 02 after verification.
**Last Activity:** `2026-04-24`
**Last Activity Description:** executed Phase 01 Plan 01 — chose
search-without-decode as the first runtime extraction slice, tightened
data and legal boundaries, and wired the Phase 02 target smoke
expectation into `SMOKE_TESTS.md`.

**Execution Doctrine:** no interim reporting unless there is a real blocker
that cannot be removed locally or on admitted surfaces.

**Progress:** [######----] `60%`

## Active Calculations

- none; Phase 01 is a source-truth and boundary-admission phase

## Intermediate Results

- repo-local authority bundle copied into `authority/`
- standalone starter package rooted at `src/gnosis_indus/`
- boundary docs and export contract written
- first extraction slice chosen: search-without-decode application surface
  (`scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`)
- Phase 4 catalogue (`scripts/indus/phase4_*.py`) and Phase 5 falsification
  (`scripts/indus/phase5_*.py`) families sequenced as explicit second and
  third waves, not grey-zone
- DATA_POLICY first-slice classification table admits derived cluster
  tables and catalogue JSON as PUBLIC_LATER, latency/compression numbers
  as PUBLIC_NOW, ICIT reference JSON as FETCH_EXTERNAL, and raw sign
  images as BLOCKED_RIGHTS
- SMOKE_TESTS declares a Phase 02 target smoke that instantiates a
  SearchEngine and asserts Track C latency (< 100 ms) and compression
  (>= 5x) gates

## Open Questions

- Which derived artifacts are safe to vendor before a fetch manifest exists?
- What final release metadata will the owner supply?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Scaffold instantiation | current session | 1 | 0 |

## Accumulated Context

### Decisions

- [Phase 00]: keep `gnosis-indus` as an anchor application and evidence repo.
- [Phase 00]: keep search-without-decode inside this repo.
- [Phase 00]: preserve the Phase 4 stability caveat across front-door docs.

### Active Approximations

- The starter package proves import readiness, not full replay readiness.

**Convention Lock:**

- Natural units: `n/a`
- Coordinate system: `not applicable`

*Custom conventions:*
- Authority metric: truth-surface coherence
- Baseline comparator: copied authority docs plus corrected control-plane docs
- Workspace root: the directory that owns this `.gpd/` folder

### Propagated Uncertainties

- final license and public contact are owner-deferred
- first-slice runtime dependency list stays unfrozen until `scripts/indus/phase4_search_demo.py` is actually extracted in Phase 02 Plan 01 (expected minimum: `numpy` plus stdlib)

### Pending Todos

- advance orchestrator to Phase 02 after verification
- in Phase 02 Plan 01, extract `scripts/indus/phase4_search_demo.py` into
  `src/gnosis_indus/search_surface/` and co-land the derived
  `artifacts/phase4/indus_catalogue.json` needed by the smoke path
- implement the Phase 02 target smoke path declared in `SMOKE_TESTS.md`
- freeze the real runtime dependency list once the first slice lands
  (expected minimum: `numpy` plus stdlib)

### Blockers/Concerns

- None. Rights and ownership caveats are real constraints, but not current
  blockers for Phase 01. The first-slice choice explicitly avoids opening
  any new rights surface.

## Session Continuity

**Last session:** `2026-04-24T00:00:00Z`
**Stopped at:** Phase 01 Plan 01 complete; first extraction slice chosen
(search-without-decode); waiting for orchestrator to verify and advance
to Phase 02.
**Resume file:** `.gpd/ROADMAP.md` (Phase 02 row)
