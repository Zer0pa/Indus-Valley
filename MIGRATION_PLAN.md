# Migration Plan

## Goal

Turn this staged scaffold into a standalone `gnosis-indus` repo without losing
the carried-forward evidence truths that justify the split.

## Current stage

`Stage 0 - scaffold instantiated`

The doc surface, PRD, GPD pack, authority copies, and boundary files exist.
Runtime extraction and replay remain future work.

## Planned stages

| Stage | Objective | Exit gate |
| --- | --- | --- |
| 0 | Scaffold and authority bundle | repo starter exists with truthful docs |
| 1 | Source admission and boundary freeze | source ledger, exclusions, and data policy are stable |
| 2 | Minimal code extraction | first clean `src/gnosis_indus` runtime slice imports and passes smoke tests |
| 3 | Evidence bundle extraction | selective Phase 4/5 artifacts land with rights-aware handling |
| 4 | Replay and release gate | clean-machine smoke path and release coherence pass succeed |

## First extraction targets (in execution order)

1. **Search-without-decode application surface** —
   `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`.
   Lowest rights-gate risk (derived cluster IDs only, no images), smallest
   dependency footprint (consumes catalogue JSON plus a query list), and the
   cleanest stronger-smoke-path story (instantiable query engine with
   latency and compression gates inherited from the Phase 4 Track C demo).
   Must co-land with a small derived `artifacts/phase4/indus_catalogue.json`
   so the smoke path has something to query. Preserves the PRD framing of
   search as an in-repo application surface and does not touch the
   `PHASE4_CATALOGUE_CONDITIONAL` stability caveat.
2. **Phase 4 catalogue route, stability, and summary surfaces** —
   `scripts/indus/phase4_*.py` → `src/gnosis_indus/catalogue/`. Second wave.
   Must carry the `PHASE4_CATALOGUE_CONDITIONAL` verdict and the k=70
   stability caveat visibly into runtime docstrings and any runtime-facing
   summary. Depends on feature-extraction and stability batteries that
   currently live in the monorepo.
3. **Phase 5 falsification summaries and bundle contracts** —
   `scripts/indus/phase5_*.py` → `src/gnosis_indus/falsification/`. Third
   wave. Must preserve
   `PHASE5_INDISTINGUISHABLE - LINGUISTIC_CONFIRMED`. Large language
   corpora stay `FETCH_EXTERNAL`.

## Deferred or externalized targets

- image-bearing corpora and large upstream corpora
- shared kernels that belong in `gnosis-glyph-engine` or `gnosis-morph-bench`
- any separate script-search repo story

## Known blockers

- image and provenance rights are not yet public-release clean
- the current source tree still depends on monorepo-local helpers; the
  first-slice dependency footprint is expected to drag in (at minimum)
  `numpy`, `json` (stdlib), `pathlib` (stdlib), and `time` (stdlib), with
  `scipy`, `scikit-learn`, and `hdbscan` only entering once the second and
  third waves land. No package dependency list is frozen until the real
  extraction lands in Phase 02.
- public license and contact fields remain owner-supplied
