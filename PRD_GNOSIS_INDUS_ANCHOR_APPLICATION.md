# Gnosis Indus Atlas - ZER0PA Innovation PRD
Sector: Gnosis
Sector Folder: workstreams/gnosis-indus
Document Class: SECTOR_SPECIFIC_PRD
Version: 1.0.0
Created: 2026-04-23
Last Modified: 2026-04-23
Status: RATIFIED
PRD Class: IMMUTABLE_CHARTER + MUTABLE_EXPERIMENT_PROGRAM
Source Corpus:
- _control/verification/CORRECTED_WORKSTREAM_SET.md
- _control/research/WORKSTREAM_VALUE_RANKING.md
- _control/research/RESEARCH_CONTRADICTIONS_AND_GAPS.md
- 01_prd_and_authority/source_copies/review_pack/*
- 01_prd_and_authority/source_copies/papers/*
Authority Metric: Truth-surface coherence across the staged repo surface. Every
promoted claim must trace to a local authority copy or explicit fetch surface,
while preserving the non-decipherment posture, the Phase 4 stability caveat,
and the in-repo script-search boundary.
Comparator State: FROZEN

## 1. Mission and Structural Thesis

### 1.1 One-Sentence Mission

Stage `gnosis-indus` as a standalone anchor application and evidence repo for
the Indus lane without overstating the scientific claim set or inventing a
false product boundary.

### 1.2 Structural Thesis

This lane is valuable because it is where the Gnosis methods meet a real
artifact chain: morphology, falsification, papers, and a search application
surface all converge on one corpus. The repo should therefore optimize for
evidence integrity and reproducible boundaries, not for a flagship narrative.

### 1.3 Falsification Condition

Abort promotion or widen nothing if any of the following become necessary:

- hiding the Phase 4 stability caveat
- claiming decipherment or substrate identification
- splitting search into a fake sovereign repo boundary
- inventing clean public image rights that the evidence surface does not hold

### 1.4 Agent-Readable Brief

`gnosis-indus` is the anchor application/evidence repo for the Indus lane. Its
job is to preserve the carried-forward evidence chain: the conditional Phase 4
catalogue, the Phase 5 falsification results, the search-without-decode
application surface, and the paper verdict stack. It must remain explicitly
non-decipherment. Search stays inside this repo as an application surface.
Phase 4 caveats stay visible even where later k=100 paper work improves the
catalogue. Public image/data rights remain bounded by provenance and fetch
policy.

### 1.5 Superordinate Goal

Produce a truthful standalone repo candidate that can be audited without
monorepo tribal knowledge and without narrative inflation.

## 2. Scope and Boundaries

### 2.1 In-Scope Artifacts

| Artifact | Type | Lane | Target Path |
| --- | --- | --- | --- |
| Sovereign repo PRD | document | `gnosis-indus` | `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` |
| Authority snapshot | document | `gnosis-indus` | `AUTHORITY_SNAPSHOT.md` |
| Boundary docs | documents | `gnosis-indus` | `MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `TODO.md` |
| Repo doc surface | documents | `gnosis-indus` | root docs plus `docs/` |
| Minimal package root | code scaffold | `gnosis-indus` | `src/gnosis_indus/` |
| Export contract | document | `gnosis-indus` | `docs/family/INDUS_EXPORT_CONTRACT.md` |

### 2.2 Out-of-Scope

- any decipherment claim
- a standalone `gnosis-script-search` repo story
- cuneiform flagship or control-lane promotion
- glyph-engine or morph-bench extraction beyond interface notes
- unrestricted image-bearing public release before rights are cleared

### 2.3 Source Corpus and Coverage Matrix

| Source ID | Path | Type | Required For | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-01 | `source_copies/review_pack/phase4_governing_verdict.md` | verdict | README, authority, data policy | EXTRACTED | k=70 conditional catalogue anchor |
| SRC-02 | `source_copies/review_pack/phase5_governing_verdict.md` | verdict | README, authority, PRD | EXTRACTED | non-decipherment falsification anchor |
| SRC-03 | `source_copies/papers/paper1_governing_verdict_v2.md` | verdict | authority, roadmap | EXTRACTED | DSH-ready paper posture |
| SRC-04 | `source_copies/review_pack/search_demo_summary.md` | application evidence | README, export contract | EXTRACTED | search stays in-repo |
| SRC-05 | `_control/verification/CORRECTED_WORKSTREAM_SET.md` | control plane | boundary docs | EXTRACTED | corrected workstream class and search demotion |
| SRC-06 | `_control/research/RESEARCH_CONTRADICTIONS_AND_GAPS.md` | control plane | data policy, public limits | EXTRACTED | licensing and stability gaps |

### 2.4 Lane Boundaries

| Lane ID | Name | Owner Surface | Folder Boundary | Integration Rule |
| --- | --- | --- | --- | --- |
| L1 | Gnosis Indus Atlas | this repo | `gnosis-indus/` | sovereign |
| L2 | Gnosis Morph Bench | external dependency | separate workstream | cite only, do not absorb |
| L3 | Gnosis Glyph Engine | external dependency | separate workstream | cite only, do not absorb |
| L4 | Search application surface | internal application layer | inside `gnosis-indus` | do not spin out |

### 2.5 Anti-Scope-Creep Rule

This lane may reference shared methods and control materials, but it must not
fake independence by absorbing other workstreams or fake leverage by splitting
its own search surface into a sovereign repo.

## 3. Carried-Forward Scientific Truth

| Surface | Current truth | Repo posture |
| --- | --- | --- |
| Phase 4 morphology | `PHASE4_CATALOGUE_CONDITIONAL` at k=70; later k=100 paper work improves NMI and Jaccard but does not erase the stability caveat | promote with caveat |
| Phase 5 falsification | `PHASE5_INDISTINGUISHABLE - LINGUISTIC_CONFIRMED` | promote with non-decipherment boundary |
| Search demo | sub-millisecond search and 5.89x catalogue compression | keep as in-repo application surface |
| Paper 1 | v2 judged submission-ready with figure follow-ups | retain as evidence-bearing paper surface |
| Paper 2 | outline ready, held until Paper 1 submission | retain as deferred surface |

## 4. Architecture and Component Decisions

### 4.1 System Architecture

```text
authority copies + PRD + docs
        |
        v
  gnosis-indus staged repo
        |
        +-- src/gnosis_indus/          minimal package root
        +-- authority/                 copied verdict and review docs
        +-- docs/family/               export contract and downstream boundaries
        +-- boundary docs              migration, source, data, todo
```

### 4.2 Component Selection

| Component | Choice | Rationale |
| --- | --- | --- |
| Authority bundle | copied markdown verdicts | self-contained migration surface |
| Package root | minimal Python namespace | repo-ready starter without fake runtime claims |
| Search surface | kept inside repo | corrected control plane demotes standalone search repo story |
| Data posture | fetch-and-boundary first | licensing and provenance gap remains real |

### 4.3 Delivery Form Factor and Adoption Surface

| Form Factor | Primary User | Integration Mode | Evidence Needed |
| --- | --- | --- | --- |
| Evidence repo | reviewers, collaborators, future agents | clone and audit | local authority bundle and boundary docs |
| Application surface | Indus researchers using search-without-decode | in-repo search bundle | preserved search contract and smoke path |

## 5. Phase Plan and Execution Gates

### 5.1 Phase Sequence

| Phase | Name | Objective | Exit Gate |
| --- | --- | --- | --- |
| P0 | Bootstrap | initialize repo and GPD surfaces | standalone scaffold exists |
| P1 | Source Truth And Authority Admission | freeze authority docs, source ledger, and data policy | no contradictory front-door claims |
| P2 | Extraction And Minimal Replay Surface | extract the first clean package and smoke path | minimal replay/import path works |
| P3 | Truth-Preserving Packaging | align docs, export contract, and handover | staged repo is promotion-ready or honestly blocked |

### 5.2 Gate Execution Rules

- The authority metric is packaging truth, not rhetorical polish.
- If an extracted surface would require weakening a carried-forward caveat, the
  extraction route fails.
- Heavy data or unclear rights move to fetch surfaces, not into silent blob
  vendoring.

## 6. Acceptance Criteria and Falsification

### 6.1 Authority Metric

| Metric | Threshold | Measurement Method |
| --- | --- | --- |
| Truth-surface coherence | PASS | audit README, PRD, authority snapshot, migration docs, and data policy for contradiction-free carried-forward truth |

### 6.2 Secondary Metrics

| Metric | Threshold | Notes |
| --- | --- | --- |
| Authority bundle completeness | key review and paper verdicts copied locally | required |
| Package readiness | `pip install -e .` and import smoke path succeed | required for the starter |
| Boundary visibility | Phase 4 caveat, non-decipherment, search demotion each appear in front-door docs | required |

### 6.3 Falsification Battery

- no decipherment language in promoted docs
- no standalone script-search positioning
- no public image release language that outruns rights
- no removal of k=70 conditional caveat when citing later k=100 work

## 7. Artifact Contract

The staged repo is incomplete until it contains:

- `README.md`
- `AGENTS.md`
- `AUTHORITY_SNAPSHOT.md`
- `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md`
- `MIGRATION_PLAN.md`
- `SOURCE_BOUNDARY.md`
- `DATA_POLICY.md`
- `TODO.md`
- `docs/family/INDUS_EXPORT_CONTRACT.md`
- `.gpd/` control-plane surfaces
- `PRIVATE_INTERNAL_LICENSE_NOTICE.md` (controlling license statement until legal decides)
- `HF_CUSTODY_REGISTER.md` (off-repo custody truth)
- `PRIVATE_PROVENANCE_APPENDIX.md` (private-only symbolic-label decode; must be removed before public release)

## 8. Current Promotion Blockers

### 8.1 Currently open

- data-rights and provenance gap for image-bearing release
- owner-deferred license and public contact details

### 8.2 Closed in Phase 02

- no extracted standalone runtime beyond the starter namespace —
  closed by `src/gnosis_indus/search_surface/` (clean-room
  reimplementation anchored to
  `authority/review_pack/search_demo_summary.md`; see
  `.gpd/phases/02-extraction-and-minimal-replay-surface/VERIFICATION.md`)
- no clean-machine replay path yet — closed by
  `pip install -e .[test] && pytest -q` (14 passed; independently
  confirmed on RunPod pod from fresh clone)
