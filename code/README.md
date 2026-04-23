# Code README

## Scope

This file describes the repo's code-facing surface: the starter package root,
the intended extraction targets, the current smoke path, and the technical
boundaries that still block a fuller standalone runtime.

## Layout

| Path | Purpose |
| --- | --- |
| `src/gnosis_indus/` | starter namespace for future extracted runtime code |
| `authority/` | copied review and paper verdicts that govern promoted claims |
| `docs/family/INDUS_EXPORT_CONTRACT.md` | bundle and application-surface contract |
| `SMOKE_TESTS.md` | current starter integrity checks |

## Build Or Run

```bash
python -m pip install -e .
```

## Interface Surface

| Interface | Path | Input | Output | Stability |
| --- | --- | --- | --- | --- |
| Starter package import | `src/gnosis_indus/__init__.py` | Python import | versioned namespace | experimental |
| Export contract | `docs/family/INDUS_EXPORT_CONTRACT.md` | admitted authority and artifact bundles | downstream bundle rules | stable for the starter |
| Smoke path | `SMOKE_TESTS.md` | local staged repo | integrity verdict | stable for the starter |

## Artifact Outputs

| Artifact | Produced By | Path | Used By |
| --- | --- | --- | --- |
| Repo truth snapshot | docs authoring | `AUTHORITY_SNAPSHOT.md` | front door and audit path |
| Migration plan | staged extraction planning | `MIGRATION_PLAN.md` | future extraction work |
| Future catalogue bundle | later extracted runtime | `artifacts/phase4/` | search and evidence surfaces |

## Known Boundaries

- the first real extracted runtime slice is not present yet
- large corpora and sign-image assets remain outside the starter repo
