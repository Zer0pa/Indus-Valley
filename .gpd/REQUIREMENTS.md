# Requirements: Gnosis Indus Atlas

**Defined:** 2026-04-23
**Core Research Or Build Question:** Can `gnosis-indus` be migrated into a
truthful standalone anchor application and evidence repo without losing the
scientific caveats that justify the lane?

## Primary Requirements

### Data And Anchors

- [x] **DATA-01**: Admit the copied authority bundle and source ledger inside
      this repo.
- [x] **DATA-02**: Freeze the corrected workstream posture and supersession of
      the standalone search story.
- [x] **DATA-03**: Freeze the data-rights and fetch posture for the starter.

### Derivations And Contracts

- [x] **DERV-01**: Define the standalone repo surface and sovereign PRD.
- [x] **DERV-02**: Define the export and boundary contract for search,
      morphology, and falsification surfaces.
- [x] **DERV-03**: Define the migration and smoke-test contract for the starter.

### Calculations And Analysis

- [x] **CALC-01**: Build a coherent front-door and authority surface.
- [x] **CALC-02**: Land a minimal package root and starter smoke path.
- [x] **CALC-03**: Choose the first clean extraction target for real runtime
      migration. _(Phase 01 Plan 01: search-without-decode application
      surface, `scripts/indus/phase4_search_demo.py` →
      `src/gnosis_indus/search_surface/`; see `SOURCE_BOUNDARY.md` and
      `MIGRATION_PLAN.md`.)_

### Simulation And Implementation

- [x] **SIMU-01**: Implement the minimal standalone scaffold and package root.
- [x] **SIMU-02**: Emit the required docs, plans, and machine-readable state.

### Validations

- [x] **VALD-01**: Verify that no doc promotes decipherment or substrate
      closure.
- [x] **VALD-02**: Verify that the Phase 4 caveat and search boundary remain
      explicit.
- [x] **VALD-03**: Verify source, data, and fetch boundaries.
- [x] **VALD-04**: Verify the first real extraction path on a stronger smoke or
      replay path than the starter import. _(Phase 02 Plan 01: closed by
      `tests/test_search_surface.py` (14 tests, 0.06s) reproducing
      authority-doc queries against
      `artifacts/phase4/indus_catalogue_demo_fixture.json`; smoke command
      `pip install -e .[test] && pytest -q` is now wired into
      `SMOKE_TESTS.md`.)_

### Writing And Packaging

- [x] **WRIT-01**: Produce the repo-local handoff and authority surface.
- [x] **WRIT-02**: Produce mirrored package-side handoff docs under
      `06_handover/`.

## Follow-Up Requirements

### Extended Investigation

- **EXTD-01**: Extract the first clean Phase 4 or Phase 5 runtime slice.
- **EXTD-02**: Add a rights-aware fetch manifest for omitted data families.

## Out Of Scope

| Topic | Reason |
| ----- | ------ |
| decipherment claims | violates carried-forward evidence posture |
| standalone `gnosis-script-search` repo promotion | corrected set demotes that story |
| unrestricted public image dump | rights and provenance gap remains real |

## Accuracy And Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| `DATA-01` / `VALD-03` | authority docs and boundary docs are local and coherent | repo-local audit |
| `CALC-01` / `VALD-01` / `VALD-02` | no contradictory front-door claims survive | truth-surface coherence audit |
| `CALC-02` | starter package imports and compile check pass | `SMOKE_TESTS.md` |
| `CALC-03` / `VALD-04` | first real extraction target is explicit and replayable | phase plan plus stronger smoke path |

## Contract Coverage

| Requirement | Decisive Output Or Deliverable | Anchor Or Benchmark | Prior Inputs Or Baselines | False Progress To Reject |
| ----------- | ------------------------------ | ------------------- | ------------------------- | ------------------------ |
| `DATA-01` / `DERV-01` | `AUTHORITY_SNAPSHOT.md` | `ref-prd`, `ref-authority` | copied verdicts | summary prose without local authority copies |
| `DATA-02` / `VALD-01` | `SOURCE_BOUNDARY.md` | `ref-phase4`, `ref-phase5` | corrected control plane | standalone search or decipherment drift |
| `DATA-03` / `VALD-03` | `DATA_POLICY.md` | `ref-authority` | rights and provenance caveats | silent public data inflation |
| `CALC-02` / `SIMU-01` | `pyproject.toml`, `src/gnosis_indus/`, `SMOKE_TESTS.md` | starter smoke path | repo scaffold | docs-only staging without any importable root |
| `WRIT-01` / `WRIT-02` | handoff docs in repo and package | `ref-prd` | migration contract | handover without mirrored package docs |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| `DATA-01`, `DERV-01`, `SIMU-01`, `SIMU-02` | Phase 00: Workstream Bootstrap | Complete |
| `DATA-02`, `DATA-03`, `DERV-02`, `VALD-01`, `VALD-02`, `VALD-03`, `WRIT-01`, `WRIT-02` | Phase 01: Source Truth And Authority Admission | Complete |
| `CALC-02`, `CALC-03`, `DERV-03`, `VALD-04` | Phase 02: Extraction And Minimal Replay Surface | Complete |
| packaging coherence pass | Phase 03: Truth-Preserving Packaging | Pending |
