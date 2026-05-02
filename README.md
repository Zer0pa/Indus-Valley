# Gnosis Indus Atlas

> Anchor application and evidence repo for the Indus lane.
> Useful now, improving without overclaim.

---

**This is a live window into the Zer0pa lab.** None of the work in this repo is a final release. Zer0pa GitHub repos are open as a matter of course for visibility and community participation. Always-in-beta is the posture: useful now, improving continuously. Open gates and honest blockers are surfaced in plain text below — see `## What We Don't Claim` and `## Upcoming Workstreams`.

---

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See
`LICENSE` for the full text. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative
Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`. Canonical
terms: <https://creativecommons.org/licenses/by/4.0/>.

**Data and fixtures** are handled per dataset and artifact family. See
`DATA_POLICY.md` for this repository's data boundary. The code license does not
license raw corpora, image-bearing cultural-heritage assets, private HF
artifacts, model weights, endpoint logs, or operational transcripts.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are
trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights.
See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. The license files in
this repo define the intended open-source/open-documentation terms for released
Gnosis code and written materials; they do not publish rights-gated data.


## Traditional-Knowledge Acknowledgment

This repository works with material originating from the Indus Valley
Civilization, including the undeciphered Indus script. Zer0pa claims no
proprietary right over the Indus script, its imagery, or the archaeological
record.

Zer0pa's work is the computational analysis, lattice methods, and falsification
discipline applied to that material. This repository does not claim a definitive
decipherment of any Indus sign or sequence.

Good-faith inquiries from identified communities, governmental antiquity
authorities, or institutional bodies may be sent to architects@zer0pa.ai.

## What This Is

Gnosis applied-research repo for the Indus-script lane. It packages
the carried-forward evidence chain around the Indus morphological
catalogue (admitted at k=70 with a stability caveat), the Phase 5
falsification work (linguistic structure confirmed, substrate
identification not), the Paper 1 / Paper 2 verdict stack, and a
search-without-decode application surface implemented in this repo as
the first runtime slice. It is not a decipherment repo, not a generic
search product, and not the portfolio's lead thesis.

**Strongest current evidence surface:** Phase 4 admits a conditional
412-sign / 70-cluster catalogue over 179 inscriptions with NMI 0.5793
against ICIT Sets and sigma 5.65. Track C then demonstrates
search-without-decode over cluster sequences with 5.89x catalogue
compression and 0.0451 ms max query latency. Proof paths:
`authority/review_pack/phase4_governing_verdict.md`,
`authority/review_pack/indus_catalogue_summary.md`, and
`authority/review_pack/search_demo_summary.md`.

**Headline metric:** `pytest -q → 14 passed` (≈0.03 s local, ≈0.3 s
on RunPod from fresh clone). The clean-room search-without-decode
runtime (`src/gnosis_indus/search_surface/`) reproduces 6
authority-doc query records on the demo fixture
(`artifacts/phase4/indus_catalogue_demo_fixture.json`), with
`sequence_search` median latency well under the authority-doc 100 ms
gate (`authority/review_pack/search_demo_summary.md`). Per-phase
verifications: `.gpd/phases/0{1,2,3}-*/VERIFICATION.md` — all PASS,
10/10 confidence.

**Honest blocker:** Image-bearing sign rights remain `BLOCKED_RIGHTS`
per `DATA_POLICY.md`; the full k=70 catalogue (412 signs / 70 clusters
/ 179 inscriptions) stays `FETCH_EXTERNAL`. The bundled fixture is
small and authority-anchored to
`authority/review_pack/search_demo_summary.md`.

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
- We do not claim all rights gates are cleared. Image rights for
  sign-bearing releases remain open; this is an open lab, not a
  finished product.
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
├── NOTICE                              # Apache-2.0 code and CC-BY-4.0 docs posture
├── README.md                           # this file
├── CHANGELOG                           # release history
├── CITATION.cff                        # citation metadata
├── CODE_OF_CONDUCT.md                  # community conduct standards
├── PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md # sovereign brief
├── AGENTS.md                           # autonomous-agent rules
├── AUTHORITY_SNAPSHOT.md               # carried-forward truth
├── AUDITOR_PLAYBOOK.md                 # outsider-audit fast path (pre-Phase-02 vintage; refresh pending)
├── PUBLIC_AUDIT_LIMITS.md              # what audit can and cannot conclude
├── HF_CUSTODY_REGISTER.md             # off-repo storage truth
├── SOURCE_BOUNDARY.md                  # source families included / deferred / excluded
├── DATA_POLICY.md                      # data classes and rights posture
├── ROADMAP.md                          # milestone tracker
├── _internal/                          # scaffolding and internal orchestration docs
│   ├── MIGRATION_PLAN.md               # extraction roadmap and waves (internal)
│   ├── STATUS_REPORT_2026-04-24.md     # orchestrator execution narrative (internal)
│   ├── AUTONOMOUS_EXECUTION_POLICY.md
│   ├── GPD_BOOTSTRAP_GUIDE.md
│   ├── STARTUP_PROMPT.md
│   ├── UNIVERSAL_STARTUP_PROMPT.md
│   ├── WORKSTREAM_GPD_INIT_CHECKLIST.md
│   └── TEMPLATE_USAGE.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── LEGAL_BOUNDARIES.md
│   ├── FAQ.md
│   ├── SUPPORT.md
│   └── family/INDUS_EXPORT_CONTRACT.md
├── authority/                          # exact-source-only verdict copies
│   ├── review_pack/                    # Phase 4/5 governing verdicts and PRDs
│   └── papers/                         # Paper 1/2 governing verdicts
├── src/gnosis_indus/
│   └── search_surface/                 # Phase 02 first runtime slice (clean-room)
├── artifacts/phase4/
│   └── indus_catalogue_demo_fixture.json  # authority-anchored demo fixture
├── tests/
│   └── test_search_surface.py          # 14 tests reproducing authority queries
├── .gpd/                               # GPD control plane (PROJECT, STATE, ROADMAP, REQUIREMENTS, DECISIONS, CONVENTIONS, phase plans + verifications)
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
- **License text has landed** as Apache-2.0 for code and CC-BY-4.0 for docs.
  Public visibility remains separate and is blocked on rights, provenance, and
  release wording review.
- **Phase 02 landed only the search-without-decode slice.** The Phase
  4 catalogue and Phase 5 falsification slices are sequenced as later
  extraction waves (`MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`).
- **Full k=70 catalogue** (412 signs, 70 clusters, 179 inscriptions)
  is not vendored; the bundled demo fixture reproduces only what the
  authority doc enumerates.
- **`AUDITOR_PLAYBOOK.md` is pre-Phase-02 vintage.** Functionally
  superseded by the README Quick Start and the Phase 03 verification
  reports (`.gpd/phases/03-truth-preserving-packaging/VERIFICATION.md`),
  but the playbook itself awaits a maintenance refresh.

## Commercial Readiness

| Field | Value |
| --- | --- |
| **Evidence posture** | staged runtime scaffold; not a portfolio verdict |
| **Posture** | `rights_gated_data_classes_image_blocked_text_fetch_external` |

The runtime and test surface are functional and reproducible from a fresh clone.
Image-rights and full-catalogue redistribution gates remain open; those are
explicit, not hidden. The staged posture reflects a production-quality scaffold,
not clearance for all data releases.

## Upcoming Workstreams

### Active Engineering

- **AUDITOR_PLAYBOOK.md maintenance refresh** — currently self-flagged
  "pre-Phase-02 vintage"; should be updated to reference the Phase 02 / 03
  verification reports and the Quick Start replay path. (`AUDITOR_PLAYBOOK.md`)
- **Phase 4 catalogue extraction wave** — extract first clean runtime slice
  into `src/gnosis_indus/catalogue/` per `_internal/MIGRATION_PLAN.md` wave 2.
- **Phase 5 falsification extraction wave** — extract first clean runtime slice
  into `src/gnosis_indus/falsification/` per `_internal/MIGRATION_PLAN.md` wave 3.

### Operations / External Dependency

- **Image-rights and provenance review** for any image-bearing public release;
  sign images remain `BLOCKED_RIGHTS` in `DATA_POLICY.md` until a rights review
  is completed by the relevant authority.
- **Full k=70 catalogue redistribution rights review** — the 412-sign / 70-cluster
  / 179-inscription catalogue stays `FETCH_EXTERNAL` until cleared.

### Research-Deferred — Investigation Underway

_(none currently; Phase 5 posture — linguistic structure confirmed, substrate
identification not — is stable and not under active re-investigation.)_

### Zero-Base Scientific Thinking — GPD Research and Planning Pending

_(none currently.)_
