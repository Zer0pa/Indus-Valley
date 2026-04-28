# Code README

## Scope

This file describes the repo's code-facing surface: the first
search-without-decode runtime slice, the intended extraction targets, the
current smoke path, and the technical boundaries that still block a fuller
standalone runtime.

## Layout

| Path | Purpose |
| --- | --- |
| `src/gnosis_indus/search_surface/` | current clean-room search-without-decode runtime slice |
| `authority/` | copied review and paper verdicts that govern promoted claims |
| `artifacts/phase4/indus_catalogue_demo_fixture.json` | small authority-anchored demo fixture |
| `tests/test_search_surface.py` | 14-test replay suite for the current runtime slice |
| `docs/family/INDUS_EXPORT_CONTRACT.md` | bundle and application-surface contract |
| `SMOKE_TESTS.md` | current starter integrity checks |

## Build Or Run

```bash
python -m pip install -e ".[test,numerics]"
pytest -q
```

## Interface Surface

| Interface | Path | Input | Output | Stability |
| --- | --- | --- | --- | --- |
| Search runtime | `src/gnosis_indus/search_surface/` | demo fixture JSON | `sign_lookup`, `sequence_search`, `subsequence_search` | staged and CI replayed |
| Export contract | `docs/family/INDUS_EXPORT_CONTRACT.md` | admitted authority and artifact bundles | downstream bundle rules | stable for the starter |
| Smoke path | `SMOKE_TESTS.md`, `tests/test_search_surface.py` | local staged repo | 14-test replay verdict | stable for the first slice |

## Artifact Outputs

| Artifact | Produced By | Path | Used By |
| --- | --- | --- | --- |
| Repo truth snapshot | docs authoring | `AUTHORITY_SNAPSHOT.md` | front door and audit path |
| Migration plan | staged extraction planning | `_internal/MIGRATION_PLAN.md` | future extraction work |
| Demo fixture | Phase 02 packaging | `artifacts/phase4/indus_catalogue_demo_fixture.json` | search runtime and pytest |
| Future catalogue bundle | later extracted runtime | `artifacts/phase4/` | search and evidence surfaces |

## Known Boundaries

- only the first search-without-decode slice is present
- Phase 4 catalogue and Phase 5 falsification runtime slices remain later waves
- large corpora and sign-image assets remain outside the starter repo
