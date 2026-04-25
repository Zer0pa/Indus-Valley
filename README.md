# Gnosis Indus Atlas

> **Notice:** This is a private internal repository. See `NOTICE.md`.

> Anchor application and evidence repo for the Indus lane.
> Useful now, improving without overclaim.

## What This Is

Private Gnosis applied-research repo for the Indus-script lane. It
packages the carried-forward evidence chain around the Indus
morphological catalogue (admitted at k=70 with a stability caveat),
the Phase 5 falsification work (linguistic structure confirmed,
substrate identification not), the Paper 1 / Paper 2 verdict stack,
and a search-without-decode application surface implemented in this
repo as the first runtime slice. It is not a decipherment repo, not a
generic search product, and not the portfolio's lead thesis.

## What We Prove

- The lane is migrated out of the original monorepo as a standalone,
  truthful scaffold without losing the Phase 4 stability caveat or the
  Phase 5 non-decipherment posture.
- A clean-room search-without-decode runtime
  (`src/gnosis_indus/search_surface/`) anchored to
  `authority/review_pack/search_demo_summary.md` reproduces six
  authority-doc query records on a small authority-anchored demo
  fixture, with `sequence_search` median latency well under the
  authority-doc 100 ms gate.
- A clean-machine replay path exists: any Python 3.11 host can
  reproduce the test surface via `pip install -e ".[test]" && pytest`.
- Off-repo custody (private HF dataset + model repos) is provisioned
  for future heavy-artifact promotion under `DATA_POLICY.md`
  classification, with the register documented in
  `HF_CUSTODY_REGISTER.md`.

## What We Don't Claim

- We do not claim decipherment of the Indus script.
- We do not claim proven substrate identification.
- We do not claim public-release readiness; visibility stays
  `INTERNAL` until Zer0pa legal decides the license matrix.
- We do not claim unrestricted public redistribution rights for any
  image-bearing or rights-gated corpus referenced in the original
  monorepo work; sign images stay `BLOCKED_RIGHTS` in
  `DATA_POLICY.md`.
- We do not claim the bundled fixture is the real full catalogue. The
  full k=70 catalogue (412 signs, 70 clusters, 179 inscriptions) stays
  `FETCH_EXTERNAL` per `DATA_POLICY.md`.

## Tests and Verification

| Surface | Status |
| --- | --- |
| `pytest -q` (Python 3.11) | `14 passed` (≈0.03 s local, ≈0.3 s on RunPod from fresh clone) |
| `python -m compileall src` | passes |
| Per-phase verification reports | `.gpd/phases/0{1,2,3}-*/VERIFICATION.md` (all PASS, latest 10/10 confidence) |
| GitHub Actions CI | wired in `.github/workflows/ci.yml` (boring CI: install + pytest, no external fetches) |
| Operational endpoint leak scan | 0 matches across all tracked surfaces |
| Falsification battery (PRD §1.3) | all four conditions hold (k=70 caveat preserved; no decipherment language; search not reframed as sovereign repo; no image-rights inflation) |

## Proof Anchors

| Claim | Evidence |
| --- | --- |
| Phase 4 conditional catalogue at k=70 with stability caveat | `authority/review_pack/phase4_governing_verdict.md`, `authority/review_pack/indus_catalogue_summary.md` |
| Phase 5 linguistic-structure-without-decipherment | `authority/review_pack/phase5_governing_verdict.md` |
| Paper 1 (DSH-ready) and Paper 2 (held until Paper 1 submission) verdicts | `authority/papers/paper1_governing_verdict_v2.md`, `authority/papers/paper2_governing_verdict.md` |
| Search-without-decode functional spec (API + latency/compression gates + 10 query ground-truth records) | `authority/review_pack/search_demo_summary.md` |
| Clean-room runtime reproducing the spec | `src/gnosis_indus/search_surface/{__init__,catalogue,engine,_fixture}.py` |
| Authority-anchored demo fixture | `artifacts/phase4/indus_catalogue_demo_fixture.json` (every row traced verbatim to a line in the authority doc; see `artifacts/phase4/README.md`) |
| Phase 02 verification (10/10) | `.gpd/phases/02-extraction-and-minimal-replay-surface/VERIFICATION.md` |
| Phase 03 verification (10/10, PRD complete) | `.gpd/phases/03-truth-preserving-packaging/VERIFICATION.md` |
| Decision log (six rows, each with rollback trigger) | `.gpd/DECISIONS.md` |
| Off-repo custody register | `HF_CUSTODY_REGISTER.md` |

## Repo Shape

```
.
├── NOTICE.md                              # root legal posture (this pass)
├── README.md                              # this file
├── PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md # sovereign brief
├── AGENTS.md                              # autonomous-agent rules
├── AUTHORITY_SNAPSHOT.md                  # carried-forward truth
├── AUDITOR_PLAYBOOK.md                    # outsider-audit fast path (pre-Phase-02 framing — see STATUS_REPORT)
├── PUBLIC_AUDIT_LIMITS.md                 # what audit can and cannot conclude
├── STATUS_REPORT_2026-04-24.md            # orchestrator execution narrative
├── HF_CUSTODY_REGISTER.md                 # off-repo storage truth
├── PRIVATE_INTERNAL_LICENSE_NOTICE.md     # interim license-posture detail (transitional)
├── PRIVATE_PROVENANCE_APPENDIX.md         # private-only symbolic-label decode (remove before public)
├── MIGRATION_PLAN.md                      # extraction roadmap and waves
├── SOURCE_BOUNDARY.md                     # source families included / deferred / excluded
├── DATA_POLICY.md                         # data classes and rights posture
├── docs/
│   ├── ARCHITECTURE.md
│   ├── LEGAL_BOUNDARIES.md
│   ├── FAQ.md
│   ├── SUPPORT.md
│   └── family/INDUS_EXPORT_CONTRACT.md
├── authority/                             # exact-source-only verdict copies
│   ├── review_pack/                       # Phase 4/5 governing verdicts and PRDs
│   └── papers/                            # Paper 1/2 governing verdicts
├── src/gnosis_indus/
│   └── search_surface/                    # Phase 02 first runtime slice (clean-room)
├── artifacts/phase4/
│   └── indus_catalogue_demo_fixture.json  # authority-anchored demo fixture
├── tests/
│   └── test_search_surface.py             # 14 tests reproducing authority queries
├── .gpd/                                  # GPD control plane (PROJECT, STATE, ROADMAP, REQUIREMENTS, DECISIONS, CONVENTIONS, phase plans + verifications)
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/ci.yml                   # boring CI: install + pytest
```

## Quick Start

Reproduce the Phase 02 stronger smoke path on any clean Python 3.11
host:

```bash
git clone https://github.com/Zer0pa/Indus-Valley.git gnosis-indus
cd gnosis-indus
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e ".[test,numerics]"
pytest -q
```

Expected: `14 passed`. The pytest suite reproduces the authority-doc
query records from `authority/review_pack/search_demo_summary.md`
against the bundled `artifacts/phase4/indus_catalogue_demo_fixture.json`.
The fixture is small and authority-anchored; the real full catalogue
stays `FETCH_EXTERNAL` per `DATA_POLICY.md`. The Phase 4 stability
caveat (k=70 conditional) remains visible in the package and fixture
surfaces.

## Current Gaps

- **Image-rights and provenance** for any public image-bearing release
  remain unresolved; sign images stay `BLOCKED_RIGHTS` in
  `DATA_POLICY.md`.
- **License text and public contact** are owner-deferred. `NOTICE.md`
  is the controlling legal posture until Zer0pa legal decides the
  matrix; `PRIVATE_INTERNAL_LICENSE_NOTICE.md` carries the longer
  interim detail.
- **Phase 02 landed only the search-without-decode slice.** The Phase
  4 catalogue and Phase 5 falsification slices are sequenced as later
  extraction waves (`MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`).
- **Full k=70 catalogue** (412 signs, 70 clusters, 179 inscriptions)
  is not vendored; the bundled demo fixture reproduces only what the
  authority doc enumerates.
- **`AUDITOR_PLAYBOOK.md` is pre-Phase-02 vintage.** Functionally
  superseded by the README Quick Start and `STATUS_REPORT_2026-04-24.md`,
  but the playbook itself awaits a maintenance refresh.
