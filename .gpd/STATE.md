# Research State

## Project Reference

See: `.gpd/PROJECT.md`

**Core research or build question:** Can `gnosis-indus` be migrated into a
truthful standalone anchor application and evidence repo without losing the
scientific caveats that justify the lane?
**Current focus:** Phase 02 Plan 01 is complete. The first clean runtime
slice (`src/gnosis_indus/search_surface/`) is landed as a clean-room
reimplementation anchored to the admitted Phase 4 Track C authority doc,
and a stronger smoke path (pytest suite reproducing authority-doc
queries on a small authority-anchored demo fixture) runs green locally.
The repo is ready for Phase 03 (truth-preserving packaging).

## Current Position

**Current Phase:** `02`
**Current Phase Name:** Extraction And Minimal Replay Surface
**Total Phases:** `4`
**Current Plan:** `1`
**Total Plans In Phase:** `1`
**Status:** `COMPLETE`
**Status Detail:** Phase 02 Plan 01 executed end-to-end as a clean-room
reimplementation pivot (original `scripts/indus/phase4_search_demo.py`
was inaccessible from this machine; clean-room from the admitted
authority doc was the well-grounded alternative). Landed
`src/gnosis_indus/search_surface/` (Catalogue, SearchEngine,
load_demo_fixture), bundled
`artifacts/phase4/indus_catalogue_demo_fixture.json` strictly from
data enumerated in `authority/review_pack/search_demo_summary.md`,
and a 14-test pytest suite (`tests/test_search_surface.py`) that
reproduces queries 1, 2, 3, 6, 9, 10 on the fixture and gates
sequence_search latency at < 100 ms. The orchestrator may advance to
Phase 03 after verification.
**Last Activity:** `2026-04-24`
**Last Activity Description:** executed Phase 02 Plan 01 — built the
Phase 4 Track C demo fixture, the clean-room search_surface package,
and the pytest stronger smoke path; locally verified `pytest -q` =
14 passed in 0.06s on Python 3.11.

**Execution Doctrine:** no interim reporting unless there is a real blocker
that cannot be removed locally or on admitted surfaces.

**Progress:** [########--] `80%`

## Active Calculations

- none; Phase 02 lands a runtime slice but no new computation is owned
  by this workstream beyond reproducing authority-doc query results

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
- SMOKE_TESTS now declares a real Phase 02 stronger smoke path
  (`pip install -e .[test] && pytest -q`) that runs 14 tests in ~0.06s
- `src/gnosis_indus/search_surface/` landed as a clean-room
  reimplementation anchored to
  `authority/review_pack/search_demo_summary.md`: Catalogue (frozen
  dataclasses, JSON loader, preserves `-1` unmapped tokens), SearchEngine
  (`sign_lookup`, `sequence_search` contiguous, `subsequence_search`
  order-preserving non-contiguous), `load_demo_fixture` one-call helper
- `artifacts/phase4/indus_catalogue_demo_fixture.json` bundles 4
  clusters (2, 26, 38, 65), 8 fully-encoded inscriptions
  (M-1A/M-3A..M-9A; M-2A absent from doc table), and 19 partial
  inscriptions (cluster-seq only) with provenance README
- `tests/test_search_surface.py` reproduces queries 1, 2, 3, 6, 9, 10
  on the fixture (query 10 fully reproduces all 5 enumerated matches;
  queries 6/9 assert subset containment of the doc's enumerated subset
  given `... and N more` truncation)

## Open Questions

- Which derived artifacts are safe to vendor before a fetch manifest exists?
- What final release metadata will the owner supply?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| Scaffold instantiation | current session | 1 | 0 |
| Phase 02 Plan 01 execution | one session (2026-04-24) | 4 | 8 |

## Accumulated Context

### Decisions

- [Phase 00]: keep `gnosis-indus` as an anchor application and evidence repo.
- [Phase 00]: keep search-without-decode inside this repo.
- [Phase 00]: preserve the Phase 4 stability caveat across front-door docs.
- [Phase 02]: original `scripts/indus/phase4_search_demo.py` source not
  accessible from this machine (mdfind / pod search both empty); pivot
  to a clean-room reimplementation from the admitted Phase 4 Track C
  authority document. The clean-room is strictly more standalone than
  a copy that drags in monorepo helpers, and its outputs are anchored
  by reproducing authority-doc query records on a small
  authority-anchored demo fixture.

### Active Approximations

- The shipped fixture is a small authority-anchored demo, not the real
  full catalogue (412 signs, 70 clusters, 179 inscriptions). The full
  catalogue stays FETCH_EXTERNAL per `DATA_POLICY.md`.

**Convention Lock:**

- Natural units: `n/a`
- Coordinate system: `not applicable`

*Custom conventions:*
- Authority metric: truth-surface coherence
- Baseline comparator: copied authority docs plus corrected control-plane docs
- Workspace root: the directory that owns this `.gpd/` folder

### Propagated Uncertainties

- final license and public contact are owner-deferred
- runtime dependency list for the first slice is frozen at "stdlib only"
  for the search_surface package; numpy is exposed as an optional
  extra (`gnosis-indus[numerics]`) for later latency tuning but is not
  required by any current code path

### Pending Todos

- advance orchestrator to Phase 03 after verification of Phase 02
- Phase 03 Plan 01 (TBD): truth-preserving packaging — confirm front
  door, authority snapshot, and boundary docs still agree after the
  Phase 02 runtime slice landed; resolve or surface the unresolved
  fetch-manifest question for derived artifacts

### Blockers/Concerns

- None. The original-source inaccessibility (Phase 02 pivot reason) is
  resolved by the clean-room reimplementation from the admitted authority
  doc. Rights and ownership caveats remain real constraints but are not
  current blockers; the bundled fixture is rights-clean (derived cluster
  IDs and integer sign IDs only).

## Session Continuity

**Last session:** `2026-04-24T00:00:00Z`
**Stopped at:** Phase 02 Plan 01 complete; clean-room search_surface
slice landed; pytest-based stronger smoke path runs green
(14 passed in 0.06s on Python 3.11); waiting for orchestrator to
verify and advance to Phase 03.
**Resume file:** `.gpd/ROADMAP.md` (Phase 03 row)
