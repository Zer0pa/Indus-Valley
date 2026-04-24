# Research State

## Project Reference

See: `.gpd/PROJECT.md`

**Core research or build question:** Can `gnosis-indus` be migrated into a
truthful standalone anchor application and evidence repo without losing the
scientific caveats that justify the lane?
**Current focus:** Phase 03 Plan 01 is complete. The PRD is now closed
end-to-end: front door (`README.md`), authority snapshot
(`AUTHORITY_SNAPSHOT.md`), PRD §8, TODO, and init checklist all
agree with the post-Phase-02 reality. Two of four PRD §8 promotion
blockers are closed (extracted runtime, clean-machine replay) and
two remain owner-bound and visible (image rights, owner-deferred
license/contact). The staged scaffold is promotion-ready up to its
admitted limits.

## Current Position

**Current Phase:** `03`
**Current Phase Name:** Truth-Preserving Packaging
**Total Phases:** `4`
**Current Plan:** `1`
**Total Plans In Phase:** `1`
**Status:** `COMPLETE`
**Status Detail:** Phase 03 Plan 01 closed the truth-surface coherence
audit. README "Current Gaps" + new "Replay" section reflect the
landed search_surface slice and the real `pip install -e .[test]
&& pytest -q` (14 passed) command. `AUTHORITY_SNAPSHOT.md`
"Promotion blockers still visible" and PRD §8 split into
"Currently open" (2 items: image rights, owner-deferred license/
contact) and "Closed in Phase 02" (2 items: extracted standalone
runtime → `src/gnosis_indus/search_surface/`; clean-machine replay
→ pytest suite confirmed on RunPod from fresh clone). TODO and
WORKSTREAM_GPD_INIT_CHECKLIST.md updated. No PRD §1.3 falsification
condition triggered. All ten PRD §7 artifact contract files exist
and are non-empty.
**Last Activity:** `2026-04-24`
**Last Activity Description:** executed Phase 03 Plan 01 — front
door, authority snapshot, PRD §8, TODO, and init checklist brought
into agreement with the post-Phase-02 reality; pytest re-run = 14
passed; `python -m compileall src` clean.

**Execution Doctrine:** no interim reporting unless there is a real blocker
that cannot be removed locally or on admitted surfaces.

**Progress:** [##########] `100%`

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

- What final release metadata will the owner supply? (license text and
  public contact remain `OWNER_DEFERRED`.)

_(Resolved: "Which derived artifacts are safe to vendor before a fetch
manifest exists?" — answered by Phase 02. The bundled
`artifacts/phase4/indus_catalogue_demo_fixture.json` is rights-clean
(integer sign IDs and derived cluster sequences only, anchored to
`authority/review_pack/search_demo_summary.md`). Image families and
the full 412-sign / 70-cluster / 179-inscription catalogue stay
`BLOCKED_RIGHTS` / `FETCH_EXTERNAL` per `DATA_POLICY.md`.)_

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

This PRD is complete. The following are recorded for continuity, but
they are explicitly out of scope for this PRD; they belong to later
extraction waves outside the current contract:

- extract the first clean Phase 4 runtime slice into
  `src/gnosis_indus/catalogue/` (next wave; `MIGRATION_PLAN.md`,
  `SOURCE_BOUNDARY.md`)
- extract the first clean Phase 5 runtime slice into
  `src/gnosis_indus/falsification/` (next wave; `MIGRATION_PLAN.md`)
- add fetch manifests for the image and full-catalogue families that
  cannot ship now (`DATA_POLICY.md`, owner-bound for image rights)
- replace `OWNER_DEFERRED` license text and public contact (owner-bound)

### Blockers/Concerns

- None. The original-source inaccessibility (Phase 02 pivot reason) is
  resolved by the clean-room reimplementation from the admitted authority
  doc. Rights and ownership caveats remain real constraints but are not
  current blockers; the bundled fixture is rights-clean (derived cluster
  IDs and integer sign IDs only).

## Session Continuity

**Last session:** `2026-04-24T00:00:00Z`
**Stopped at:** PRD complete; staged scaffold is promotion-ready up
to its admitted limits (two PRD §8 blockers closed by Phase 02; two
remain owner-bound and visible in `AUTHORITY_SNAPSHOT.md` and PRD §8).
**Resume file:** `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md`
