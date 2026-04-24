# Roadmap: Gnosis Indus Atlas

## Overview

`Gnosis Indus Atlas` runs on a staged extraction backbone. Phase 00 bootstraps
the repo-local control plane. Phase 01 freezes source truth, authority
boundaries, and data posture. Phase 02 lands the first clean runtime slice and
stronger smoke path. Phase 03 packages only what survives those gates.

Execution doctrine for every phase: repo-local evidence artifacts are
mandatory, but user-facing interim reporting is not. Work stays in the fix loop
until the active gate is closed or honestly blocked.

## Phases

- [x] **Phase 00: Workstream Bootstrap** - Initialize the repo-local GPD
      surfaces and starter package.
- [x] **Phase 01: Source Truth And Authority Admission** - Freeze authority,
      source, and data boundaries before runtime extraction.
- [x] **Phase 02: Extraction And Minimal Replay Surface** - Land the first
      clean runtime slice and a stronger smoke path.
- [x] **Phase 03: Truth-Preserving Packaging** - Package only the surfaces that
      stay honest under the admitted evidence.

## Phase Details

### Phase 00: Workstream Bootstrap

**Goal:** turn the copied starter pack into a truthful `gnosis-indus` control
plane and repo starter.
**Depends on:** nothing
**Requirements:** `DATA-01`, `DERV-01`, `SIMU-01`, `SIMU-02`
**Success Criteria**:

1. Repo docs, authority snapshot, starter package, and `.gpd/` surfaces exist.
2. No inherited placeholder claims survive.
3. The next phase is named and planned.

Plans:

- [x] **00-01**: Bootstrap the repo-local GPD surface

### Phase 01: Source Truth And Authority Admission

**Goal:** freeze the corrected workstream posture, source ledger, search
boundary, and data-rights posture before runtime extraction.
**Depends on:** Phase 00
**Requirements:** `DATA-02`, `DATA-03`, `DERV-02`, `VALD-01`, `VALD-02`,
`VALD-03`, `WRIT-01`, `WRIT-02`
**Success Criteria**:

1. The first extraction targets are explicit.
2. Search remains an in-repo application surface.
3. Data-rights and fetch boundaries are explicit.
4. The repo and package-side handoff surfaces agree.

Plans:

- [x] **01-01**: Freeze source truth and authority boundaries (completed 2026-04-24)

### Phase 02: Extraction And Minimal Replay Surface

**Goal:** extract the first clean runtime slice and strengthen the smoke path.
**Depends on:** Phase 01
**Requirements:** `CALC-02`, `CALC-03`, `DERV-03`, `VALD-04`
**Success Criteria**:

1. A real runtime slice lands under `src/gnosis_indus/`.
2. A stronger smoke or replay path exists.
3. Boundaries and caveats still match the authority docs.

Plans:

- [x] **02-01**: Extract the first clean runtime slice — search-without-decode application surface (clean-room reimplementation under `src/gnosis_indus/search_surface/`, anchored to `authority/review_pack/search_demo_summary.md`) plus the Phase 02 stronger smoke path now wired into `SMOKE_TESTS.md` and `tests/test_search_surface.py` (completed 2026-04-24).

### Phase 03: Truth-Preserving Packaging

**Goal:** package only the surfaces that stay honest under the admitted
evidence and runtime state.
**Depends on:** Phase 02
**Requirements:** packaging coherence pass
**Success Criteria**:

1. The front door, authority snapshot, and boundary docs agree.
2. Promotion blockers are either closed or still visible.
3. No release language outruns data, code, or authority truth.

Plans:

- [x] **03-01**: Truth-preserving packaging — front door, authority
      snapshot, PRD §8, and TODO brought into agreement with Phase 02
      reality (completed 2026-04-24)

## Progress

| Phase | Plans Complete | Status | Completed |
| ----- | -------------- | ------ | --------- |
| 00. Workstream Bootstrap | 1/1 | Complete | 2026-04-23 |
| 01. Source Truth And Authority Admission | 1/1 | Complete | 2026-04-24 |
| 02. Extraction And Minimal Replay Surface | 1/1 | Complete | 2026-04-24 |
| 03. Truth-Preserving Packaging | 1/1 | Complete | 2026-04-24 |
