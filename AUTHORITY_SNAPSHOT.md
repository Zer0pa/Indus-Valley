# Authority Snapshot

## Current repo posture

This staged repo is an anchor application and evidence surface for the Indus
lane. It is not the lead portfolio thesis, not a decipherment repo, and not a
standalone generic search product.

## Carried-forward truth

| Surface | Current truth | Evidence path |
| --- | --- | --- |
| Morphological catalogue | Phase 4 admitted the catalogue conditionally at k=70 with strong NMI and sigma but a real stability caveat; later k=100 paper work improves the catalogue while keeping the caveat visible | `authority/review_pack/phase4_governing_verdict.md`, `authority/review_pack/indus_catalogue_summary.md`, `authority/papers/paper1_governing_verdict_v2.md` |
| Language/substrate posture | Phase 5 supports linguistic structure but leaves Sanskrit, Tamil, and Prakrit indistinguishable at current evidence strength | `authority/review_pack/phase5_governing_verdict.md` |
| Search surface | Search-without-decode passes as a useful application surface inside this repo | `authority/review_pack/search_demo_summary.md` |
| Paper posture | Paper 1 v2 is judged submission-ready with two figure follow-ups; Paper 2 is held until Paper 1 is submitted | `authority/papers/paper1_governing_verdict_v2.md`, `authority/papers/paper2_governing_verdict.md` |

## What this repo does not claim

- decipherment of the Indus script
- proven substrate identification
- unrestricted public image-bearing release rights
- a separate sovereign `gnosis-script-search` product boundary

## Promotion blockers still visible

### Currently open

- image and reference licensing/provenance gaps
- full-catalogue redistribution review
- release wording review for any public visibility change

### Closed in Phase 02

- no extracted standalone runtime beyond the starter namespace —
  closed by `src/gnosis_indus/search_surface/` (clean-room
  reimplementation anchored to
  `authority/review_pack/search_demo_summary.md`; see
  `.gpd/phases/02-extraction-and-minimal-replay-surface/VERIFICATION.md`)
- no clean-machine replay path beyond the starter smoke test —
  closed by `pip install -e .[test] && pytest -q` (14 passed;
  independently confirmed on RunPod pod from fresh clone)

### Closed in the 2026-04-28 public-refresh wave

- code/docs license posture — closed by Apache-2.0 for code and CC-BY-4.0
  for documentation, reports, and written materials; this does not license
  raw corpora, image-bearing cultural-heritage assets, model weights, or
  private custody surfaces
- source-boundary operational gate — closed by `tools/indus_ops_gate.py`,
  wired into `.github/workflows/ci.yml`
