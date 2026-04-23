# Architecture

## Purpose

Explain where technical truth lives in this staged repo. This file is a truth
map, not a marketing deck.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
| --- | --- | --- |
| Public docs | front door, authority snapshot, boundaries, release posture | `README.md`, `AUTHORITY_SNAPSHOT.md`, root boundary docs |
| Code or runtime | starter package root and later extracted modules | `src/gnosis_indus/` |
| Evidence artifacts | copied review-pack and paper verdicts | `authority/` |
| Downstream contracts | export semantics and bundle boundaries | `docs/family/INDUS_EXPORT_CONTRACT.md` |
| Owner-held or external context | image sets, corpora, final release metadata | `DATA_POLICY.md` |

## Component Map

| Component | Responsibility | Inputs | Outputs | Notes |
| --- | --- | --- | --- | --- |
| Authority bundle | preserve carried-forward verdict surfaces | copied markdown docs | reviewable repo-local evidence | not to be paraphrased in place |
| Starter package root | future landing zone for extracted runtime | later source extraction from `scripts/indus/` | installable namespace | currently minimal |
| Boundary docs | freeze migration, source, and data posture | PRD plus authority docs | auditable repo posture | sovereign for staged extraction |
| Search application surface | future in-repo query layer | admitted catalogue bundle | in-repo search tooling | not a separate repo boundary |

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

- the repo does not yet carry a real extracted runtime beyond the starter package
- large data and image assets are intentionally not vendored into this scaffold
