# Phase 02 Context

## Goal

Extract the first clean runtime slice into `src/gnosis_indus/search_surface/`
and land a smoke path stronger than the starter import check.

## Authority carry-forward

- `ref-phase4`: `authority/review_pack/phase4_governing_verdict.md` — k=70
  conditional catalogue with stability caveat (must remain visible).
- `ref-phase4-track-c`: `authority/review_pack/search_demo_summary.md` —
  complete functional specification for the search-without-decode demo,
  including API names, latency gate (<100 ms), symbol compression (5.89x),
  sample encodings for 8 inscriptions, cluster memberships for 4 clusters,
  and 10 query-result ground-truth records.
- `ref-phase5`: `authority/review_pack/phase5_governing_verdict.md` — keep
  non-decipherment posture explicit.

## Execution pivot

Phase 01 chose `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`
as the first extraction target. Between the Phase 01 verification push and
the start of Phase 02, the orchestrator searched the local machine and the
RunPod workspace for the source script and its catalogue JSON:

- `mdfind "phase4_search_demo.py"` on the local machine — only returned doc
  mentions, no source code.
- `find /workspace` on the pod — only the canonical ZPE Tokenizer dossier
  and an unrelated public Indus corpus (`indus-valley-script-corpus`, a
  Rust project) were present.
- Handover record (`../HANDOVER_NEXT_GNOSIS_ORCHESTRATOR_2026-04-23.md`)
  names the original source repo as `<MONOREPO_ROOT>` (see
  `PRIVATE_PROVENANCE_APPENDIX.md` for the mapping), which does not exist
  on this machine.

The source is therefore not accessible from this environment. Per
`AUTONOMOUS_EXECUTION_POLICY.md` §What Counts As A Blocker, a missing
required source is a genuine blocker. Per the user's executive mandate
(documented in the resume session), blockers are turned into tasks when a
well-grounded alternative exists.

A **clean-room reimplementation from the admitted authority documents** is
that well-grounded alternative, and it is architecturally preferable:

1. The `gnosis-indus` repo is classified `ANCHOR_APPLICATION` (PRD §1.1,
   §3). Its job is to preserve the evidence chain and expose a truthful
   application surface — not to mirror the original monorepo helpers.
2. `AGENTS.md` "What success looks like" says "the repo becomes more
   standalone without becoming less truthful." A clean-room from
   authority docs is strictly more standalone than a copy that drags in
   monorepo helpers.
3. `search_demo_summary.md` contains enough specification to build a
   reference implementation whose outputs match the admitted authority
   numbers — i.e. the implementation is *anchored* to authority, not
   invented.

Decision recorded in `.gpd/DECISIONS.md` and the Phase 02 plan.

## Non-negotiables (carried from Phase 01)

- Phase 4 k=70 stability caveat stays visible in docs and code comments.
- No decipherment / substrate-identification language.
- Search remains an in-repo application surface, not a sovereign repo.
- No image-bearing assets; only derived integer IDs and cluster sequences.
- Real full catalogue (412 signs, 70 clusters, 179 inscriptions) is NOT
  vendored. The first slice ships a small **authority-backed demo fixture**
  assembled strictly from data present in `search_demo_summary.md`.
