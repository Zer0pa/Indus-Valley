# Roadmap

## Overview

This repo moves in four bounded steps: freeze the authority and source
boundaries, extract the first honest runtime slice, preserve the key evidence
surface locally, and only then decide whether the repo is ready for public
promotion.

## Milestones

| Milestone | Status | Purpose |
| --- | --- | --- |
| M0 - staged scaffold | done | repo root, authority bundle, and control plane exist |
| M1 - source truth admission | next | freeze source ledger, exclusions, and data policy |
| M2 - minimal extraction | planned | land the first clean package slice under `src/gnosis_indus/` |
| M3 - replay surface | planned | add a stronger smoke or replay path for admitted surfaces |
| M4 - promotion readiness | blocked | requires rights, license, and coherence closure |

## Near-term priorities

- admit the first Phase 4 and Phase 5 source families cleanly
- define fetch surfaces for corpora and sign images
- keep search surface in-repo while extraction proceeds

## Explicitly not on this roadmap

- a decipherment launch narrative
- a separate `gnosis-script-search` repo promotion
- casual public dumping of image-bearing corpora
