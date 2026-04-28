# Roadmap

## Overview

This repo moves in four bounded steps: freeze the authority and source
boundaries, extract the first honest runtime slice, preserve the key evidence
surface locally, and only then decide whether the repo is ready for public
promotion.

## Milestones

| Milestone | Status | Purpose |
| --- | --- | --- |
| M0 - staged scaffold | **done** | repo root, authority bundle, and control plane exist |
| M1 - source truth admission | **done** (Phase 01 PASS, 9/10) | froze source ledger, exclusions, and data policy |
| M2 - minimal extraction | **done** (Phase 02 PASS, 10/10) | landed clean-room search_surface slice under `src/gnosis_indus/`; 14 pytest passes |
| M3 - replay surface | **done** (Phase 03 PASS, 10/10) | truth-surface coherence audit; clean-machine replay confirmed on RunPod |
| M4 - promotion readiness | **blocked** | requires image-rights clearance, full catalogue redistribution review, and release-wording review |

## Near-term priorities

- extract Phase 4 catalogue runtime slice into `src/gnosis_indus/catalogue/` (see GitHub Issue #1)
- extract Phase 5 falsification runtime slice into `src/gnosis_indus/falsification/` (see GitHub Issue #2)
- add fetch manifests for image and corpus families that cannot ship now (see GitHub Issue #3)
- refresh AUDITOR_PLAYBOOK.md to reflect post-Phase-02 state

## Explicitly not on this roadmap

- a decipherment launch narrative
- a separate `gnosis-script-search` repo promotion
- casual public dumping of image-bearing corpora
