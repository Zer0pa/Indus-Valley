# Architecture

## Purpose

Explain where technical truth lives in this staged repo. This file is a truth
map, not a marketing deck.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
| --- | --- | --- |
| Public docs | front door, authority snapshot, boundaries, release posture | `README.md`, `AUTHORITY_SNAPSHOT.md`, root boundary docs |
| Code or runtime | first search-without-decode runtime slice and later extraction targets | `src/gnosis_indus/`, `tests/` |
| Evidence artifacts | copied review-pack and paper verdicts | `authority/` |
| Downstream contracts | export semantics and bundle boundaries | `docs/family/INDUS_EXPORT_CONTRACT.md` |
| Owner-held or external context | image sets, corpora, final release metadata | `DATA_POLICY.md` |

## Component Map

| Component | Responsibility | Inputs | Outputs | Notes |
| --- | --- | --- | --- | --- |
| Authority bundle | preserve carried-forward verdict surfaces | copied markdown docs | reviewable repo-local evidence | not to be paraphrased in place |
| Search runtime slice | clean-room implementation of the admitted search-without-decode surface | authority search demo summary + demo fixture | installable `gnosis_indus.search_surface` API | current CI replay path |
| Boundary docs | freeze migration, source, and data posture | PRD plus authority docs | auditable repo posture | sovereign for staged extraction |
| Later extraction targets | Phase 4 catalogue and Phase 5 falsification runtime families | `_internal/MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md` | future `catalogue/` and `falsification/` modules | rights and fetch boundaries stay visible |

## Authority Artifacts

| Artifact | Path | Why It Matters | Public? |
| --- | --- | --- | --- |
| Repo truth snapshot | `../AUTHORITY_SNAPSHOT.md` | compact current authority block | Yes |
| Phase 4 verdict | `../authority/review_pack/phase4_governing_verdict.md` | morphology caveat anchor | Yes |
| Phase 5 verdict | `../authority/review_pack/phase5_governing_verdict.md` | non-decipherment substrate anchor | Yes |
| Search demo summary | `../authority/review_pack/search_demo_summary.md` | internal application-surface evidence | Yes |
| Paper 1 v2 verdict | `../authority/papers/paper1_governing_verdict_v2.md` | current paper posture | Yes |

## Truth Surface Boundaries

- `README.md` is the front door.
- `AUTHORITY_SNAPSHOT.md` is the compact truth surface.
- `AUDITOR_PLAYBOOK.md` is the shortest outsider replay path.
- `code/README.md` owns package and interface details.
- `DATA_POLICY.md` and `docs/LEGAL_BOUNDARIES.md` bound rights and release language.

## Known Gaps

- the repo carries only the first search-without-decode runtime slice
- the Phase 4 catalogue and Phase 5 falsification runtime families remain later extraction waves
- large data and image assets are intentionally not vendored into this scaffold
