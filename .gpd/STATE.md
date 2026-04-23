# Research State

## Project Reference

See: `.gpd/PROJECT.md`

**Core research or build question:** Can `gnosis-indus` be migrated into a
truthful standalone anchor application and evidence repo without losing the
scientific caveats that justify the lane?
**Current focus:** Phase 01 is active. Freeze source truth, authority
boundaries, and data posture before extracting runtime code.

## Current Position

**Current Phase:** `01`
**Current Phase Name:** Source Truth And Authority Admission
**Total Phases:** `4`
**Current Plan:** `1`
**Total Plans In Phase:** `1`
**Status:** `READY`
**Status Detail:** the scaffold is complete; the next gate is to freeze source
and data boundaries before choosing the first extracted runtime slice.
**Last Activity:** `2026-04-23`
**Last Activity Description:** instantiated the workstream pack, copied the
authority bundle, and specialized the repo scaffold and GPD surfaces

**Execution Doctrine:** no interim reporting unless there is a real blocker
that cannot be removed locally or on admitted surfaces.

**Progress:** [###-------] `30%`

## Active Calculations

- none; Phase 01 is a source-truth and boundary-admission phase

## Intermediate Results

- repo-local authority bundle copied into `authority/`
- standalone starter package rooted at `src/gnosis_indus/`
- boundary docs and export contract written

## Open Questions

- Which runtime slice should be extracted first?
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
- first extraction slice is not yet chosen

### Pending Todos

- execute Phase 01 Plan 01
- choose the first clean extraction target
- strengthen the smoke path in Phase 02

### Blockers/Concerns

- None yet. Rights and ownership caveats are real constraints, but not current
  blockers for Phase 01.

## Session Continuity

**Last session:** `2026-04-23T00:00:00Z`
**Stopped at:** scaffold and control plane completed; Phase 01 ready to open
**Resume file:** `.gpd/phases/01-source-truth-and-authority-admission/01-01-PLAN.md`
