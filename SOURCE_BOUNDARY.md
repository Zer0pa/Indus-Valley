# Source Boundary

## Repo identity

`gnosis-indus` owns the Indus anchor application and evidence surface.

## Included now

| Surface | Status | Why it belongs here |
| --- | --- | --- |
| Root docs and boundary docs | included | front-door truth for the repo |
| `authority/` copied verdict and review docs | included | self-contained evidence posture |
| `.gpd/` control plane | included | autonomous execution surface |
| `src/gnosis_indus/` starter namespace | included | repo-ready package root |
| `docs/family/INDUS_EXPORT_CONTRACT.md` | included | downstream contract and search boundary |

## Future extraction targets

| Current source family | Future landing zone | Notes |
| --- | --- | --- |
| `scripts/indus/phase4_*.py` | `src/gnosis_indus/catalogue/` | keep conditional-catalogue caveat visible |
| `scripts/indus/phase5_*.py` | `src/gnosis_indus/falsification/` | no decipherment claims |
| `scripts/indus/phase4_search_demo.py` | `src/gnosis_indus/search_surface/` | remains in-repo application surface |
| selected `workspace/artifacts/indus/phase4/` | `artifacts/phase4/` | small derived artifacts first |
| selected `workspace/artifacts/indus/phase5/` | `artifacts/phase5/` | small derived artifacts first |

## Explicitly out of scope

- `scripts/cuneiform/` and cuneiform artifacts
- a separate `gnosis-script-search` repo boundary
- generic shared-kernel ownership that belongs to another workstream
- outreach and prize materials unless specifically admitted later

## Shared dependency note

This repo may depend on work that later moves into `gnosis-glyph-engine` or
`gnosis-morph-bench`, but it should express those as dependencies or copied
bridges, not by erasing ownership boundaries.
