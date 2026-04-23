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

## First extraction targets

1. Phase 4 catalogue route, stability, and summary surfaces
2. Phase 5 falsification summaries and bundle contracts
3. Search-without-decode application surface, still inside this repo

## Deferred or externalized targets

- image-bearing corpora and large upstream corpora
- shared kernels that belong in `gnosis-glyph-engine` or `gnosis-morph-bench`
- any separate script-search repo story

## Known blockers

- image and provenance rights are not yet public-release clean
- the current source tree still depends on monorepo-local helpers
- no final package dependency list has been frozen
- public license and contact fields remain owner-supplied
