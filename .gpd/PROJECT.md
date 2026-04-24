# Project: Gnosis Indus Atlas

## What This Is

`Gnosis Indus Atlas` is the governed workstream for staging the Indus lane as a
truthful standalone anchor application and evidence repo. It exists to answer
whether the lane can be migrated out of the monorepo without losing the Phase 4
stability caveat, the Phase 5 non-decipherment posture, or the internal search
application boundary.

## Core Research Or Build Question

Can `gnosis-indus` be migrated into a truthful standalone anchor application and
evidence repo under the authority metric of truth-surface coherence and the
declared falsification battery?

## Scoping Contract Summary

### Contract Coverage

- `claim-anchor-application`: the repo preserves the corrected anchor
  application posture.
- `claim-truthful-boundaries`: the repo keeps non-decipherment, Phase 4 caveat,
  data-rights limits, and search boundary explicit.
- `claim-repo-starter`: the repo contains a usable standalone starter surface.
- `False progress to reject`: fake product boundaries, washed-out caveats,
  narrative cleanup, or code extraction without source admission.

### User Or Sponsor Guidance To Preserve

- `User-stated observables`: non-decipherment posture, visible Phase 4 caveat,
  script-search kept as an application surface
- `User-stated deliverables`: migration-ready workstream pack, repo-ready
  starter with customized docs and GPD pack
- `Must-have references or prior outputs`: corrected workstream set, Phase 4/5
  review pack, Paper 1 verdict files, repo-doc and GPD shared packs
- `Stop or rethink conditions`: if promotion requires dropping caveats or
  spinning search into a fake repo boundary
- `Execution doctrine`: autonomous end-to-end execution, blockers-only outward
  reporting, repo-local evidence artifacts mandatory

### Scope Boundaries

**In scope**

- repo-local authority bundle and docs
- minimal Python namespace and smoke path
- source, data, migration, and export boundaries

**Out of scope**

- decipherment or substrate closure
- standalone `gnosis-script-search` positioning
- cuneiform, glyph-engine, or morph-bench extraction beyond boundary notes

### Active Anchor Registry

| Anchor ID | Locator | Why It Matters | Carry Forward | Required Action |
| --------- | ------- | -------------- | ------------- | --------------- |
| `ref-prd` | `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` | sovereign brief | planning, execution, writing | read, obey, compare |
| `ref-agents` | `AGENTS.md` | execution boundary | planning, execution | read, obey |
| `ref-authority` | `AUTHORITY_SNAPSHOT.md` | compact carried-forward truth | execution, writing | read, compare |
| `ref-phase4` | `authority/review_pack/phase4_governing_verdict.md` | morphology caveat anchor | execution, writing | read, cite |
| `ref-phase5` | `authority/review_pack/phase5_governing_verdict.md` | falsification anchor | execution, writing | read, cite |
| `ref-paper1-v2` | `authority/papers/paper1_governing_verdict_v2.md` | current paper authority | execution, writing | read, cite |
| `ref-search-demo` | `authority/review_pack/search_demo_summary.md` | in-repo application surface anchor | execution, writing | read, cite |

### Carry-Forward Inputs

- copied review-pack verdict and PRD docs under `authority/`
- copied paper verdict docs under `authority/papers/`
- shared repo-doc and GPD starter packs, specialized locally

### Skeptical Review

- `Weakest anchor`: public image-rights and full standalone runtime are not yet
  closed
- `Unvalidated assumptions`: the first extraction slice is not yet chosen;
  package splits with sibling workstreams are not yet frozen
- `Competing explanation`: the repo could become a docs shell without a usable
  extracted runtime
- `Disconfirming observation`: any doc that requires cleaner language than the
  copied authority files allow
- `False progress to reject`: polishing docs while hiding unresolved source,
  rights, or runtime boundaries

### Open Contract Questions

- What public license and contact surface will eventually govern the repo?

_(Resolved in Phase 01 Plan 01: the first runtime slice under
`src/gnosis_indus/` is the search-without-decode application surface,
i.e. `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`.
See `SOURCE_BOUNDARY.md` and `MIGRATION_PLAN.md` for the justification and
execution order.)_

_(Resolved in Phase 02 Plan 01: derived integer-only cluster sequences
that reproduce authority-doc query records are safe to vendor as the
authority-anchored demo fixture
`artifacts/phase4/indus_catalogue_demo_fixture.json`. Image families
and the full 412/70/179 catalogue stay `BLOCKED_RIGHTS` /
`FETCH_EXTERNAL` per `DATA_POLICY.md`.)_

## Research Questions

### Answered

- [x] Should `gnosis-indus` be treated as an anchor application rather than the
      portfolio lead? Yes.
- [x] Which source family lands first as a runtime slice under
      `src/gnosis_indus/`? The search-without-decode application surface
      (`scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`).
      Phase 4 catalogue and Phase 5 falsification families are sequenced
      as the second and third waves.
- [x] Which assets stay fetch-only because of size or rights? Per
      `DATA_POLICY.md` first-slice classification: raw sign images are
      `BLOCKED_RIGHTS`; the full 412-sign / 70-cluster / 179-inscription
      catalogue and ICIT reference JSON are `FETCH_EXTERNAL`; derived
      cluster tables and the demo fixture are `PUBLIC_LATER`; latency
      and compression numbers are `PUBLIC_NOW`.
- [x] What is the minimal truthful smoke path beyond starter import?
      `pip install -e .[test] && pytest -q` (14 passed) — reproduces
      authority-doc query records from
      `authority/review_pack/search_demo_summary.md` against the bundled
      authority-anchored demo fixture; gates `sequence_search` latency
      at < 100 ms; independently confirmed on a clean RunPod pod from a
      fresh `git clone`.

### Active

_(All Active questions are answered. Remaining open question is
"What public license and contact surface will eventually govern the
repo?" under Open Contract Questions; it is owner-deferred.)_

### Out Of Scope

- Which language the Indus script encodes

## Research Context

### Physical Or Operational System

The Indus sign corpus and its derived morphology, falsification, paper, and
search surfaces.

### Theoretical Or Engineering Framework

Truth-preserving repo extraction: docs, authority copies, package boundaries,
and fetch policy are treated as engineering artifacts rather than administrative
afterthoughts.

### Key Parameters And Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| Truth-surface coherence | `C_truth` | pass/fail | Governing metric |
| Starter smoke path | `S_smoke` | pass/fail | Minimal package integrity |
| Phase 4 caveat visibility | `V_p4` | explicit in front-door docs | Must remain visible |

### Known Results

- Corrected workstream set ranks `gnosis-indus` as the evidence-bearing anchor.
- Phase 4 admits the catalogue conditionally and keeps a real stability caveat.
- Phase 5 supports linguistic structure without substrate closure.
- Search-without-decode is a useful application surface but not a sovereign repo.

### What Is New

This workstream translates those truths into a standalone repo candidate with a
local authority bundle, a repo PRD, and a staged package surface.

### Target Environment Or Venue

Standalone GitHub-style repo candidate and autonomous agent workspace.

### Computational Or Operational Environment

Python 3.11 starter package, markdown authority bundle, heavy assets held
outside the starter until admitted by policy.

## Notation And Conventions

See `.gpd/CONVENTIONS.md`.
See `.gpd/NOTATION_GLOSSARY.md`.

## Unit System

`n/a`

## Requirements

See `.gpd/REQUIREMENTS.md`.

## Key References

- `ref-prd`
- `ref-agents`
- `ref-authority`
- `ref-phase4`
- `ref-phase5`
- `ref-paper1-v2`
- `ref-search-demo`

## Constraints

- `Workspace locality`: workstream control surfaces stay in this repo root.
- `Authority doctrine`: failure on truth-surface coherence is failure.
- `Evidence discipline`: no promoted claim without a local source path or an
  explicit fetch surface.
- `Reporting discipline`: no interim reporting unless blocked.
- `Boundary doctrine`: search remains inside this repo; decipherment stays out.

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Keep `gnosis-indus` as an anchor application and evidence repo | corrected control plane ranks it third and caveated | ratified |
| Keep search-without-decode inside this repo | current evidence does not justify a separate sovereign repo | ratified |
| Preserve the Phase 4 caveat everywhere | packaging cannot outrun the authority docs | ratified |

Full log: `.gpd/DECISIONS.md`
