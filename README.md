# Gnosis Indus Atlas

> Anchor application and evidence repo for the Indus lane. Website-sync posture: staged/WIP, useful now, with rights and provenance gates visible.

## What This Is

`gnosis-indus` is the Gnosis applied-research repo for the Indus-script lane. It packages the carried-forward evidence chain around the Indus morphological catalogue, the Phase 5 falsification posture, the Paper 1 / Paper 2 verdict stack, and a search-without-decode application surface. It is **not** a decipherment repo, not a generic search product, and not the portfolio's lead thesis.

Headline metric: `pytest -q` passes with **14 tests**. The clean-room search-without-decode runtime reproduces **6 authority-doc query records** on the demo fixture, with `sequence_search` median latency under the authority-doc **100 ms** gate.

Honest blocker: image-bearing sign rights remain `BLOCKED_RIGHTS`; the full k=70 catalogue (**412 signs / 70 clusters / 179 inscriptions**) stays `FETCH_EXTERNAL`. The bundled fixture is small and authority-anchored, not the full catalogue.

| Field | Value |
|-------|-------|
| Architecture | INDUS_SEARCH_STREAM |
| Encoding | INDUS_SEARCH_WITHOUT_DECODE_V1 |

## Key Metrics

| Metric | Value | Baseline |
|---|---:|---|
| PYTEST_PASS | 14 passed | pytest |
| AUTHORITY_QUERY_RECORDS | 6 | demo fixture |
| SEQUENCE_SEARCH_GATE | <100 ms | authority |
| FULL_CATALOGUE_SCOPE | 412 signs / 70 clusters / 179 inscriptions | fetch-only |

> Source: `tests/test_search_surface.py`, `authority/review_pack/search_demo_summary.md`, `artifacts/phase4/indus_catalogue_demo_fixture.json`, and `DATA_POLICY.md`.

## What We Prove

- The lane is migrated as a standalone, truthful scaffold without losing the Phase 4 stability caveat or Phase 5 non-decipherment posture.
- A clean-room search-without-decode runtime anchored to `authority/review_pack/search_demo_summary.md` reproduces six authority-doc query records.
- A clean-machine replay path exists via `pip install -e ".[test,numerics]" && pytest`.
- Off-repo custody is provisioned for future heavy-artifact promotion under `DATA_POLICY.md` classification.

## What We Don't Claim

- We do not claim decipherment of the Indus script.
- We do not claim proven substrate identification.
- We do not claim all rights gates are cleared.
- We do not claim unrestricted public redistribution rights for image-bearing or rights-gated corpora.
- We do not claim the bundled fixture is the real full catalogue.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | STAGED |
| Commit SHA | 490b720a77ef |
| Source | authority/review_pack/search_demo_summary.md |

The runtime and test surface are functional and reproducible from a fresh clone. Image-rights and full-catalogue redistribution gates remain open; those gates are explicit, not hidden.

## Tests and Verification

| Code | Check | Verdict |
|---|---|---|
| V_01 | `pytest -q` | PASS |
| V_02 | authority-query fixture replay | PASS |
| V_03 | Indus ops gate source-boundary/leakage checks | PASS |
| V_04 | Phase 02/03 GPD verification reports | PASS |

## Proof Anchors

| Path | State |
|---|---|
| `AUTHORITY_SNAPSHOT.md` | VERIFIED |
| `authority/review_pack/search_demo_summary.md` | VERIFIED |
| `authority/review_pack/phase4_governing_verdict.md` | VERIFIED |
| `authority/review_pack/phase5_governing_verdict.md` | VERIFIED |
| `artifacts/phase4/indus_catalogue_demo_fixture.json` | VERIFIED |
| `.gpd/phases/02-extraction-and-minimal-replay-surface/VERIFICATION.md` | VERIFIED |
| `tools/indus_ops_gate.py` | VERIFIED |
| `HF_CUSTODY_REGISTER.md` | VERIFIED |
| `DATA_POLICY.md` | VERIFIED |

## Repo Shape

| Field | Value |
|---|---|
| Package | `gnosis-indus` |
| Source | `src/gnosis_indus/search_surface/` |
| Tests | `tests/test_search_surface.py` |
| Authority | `authority/` |
| Demo fixture | `artifacts/phase4/indus_catalogue_demo_fixture.json` |
| Gate tooling | `tools/indus_ops_gate.py` |
| Legal/Data | `LICENSE`, `NOTICE`, `DATA_POLICY.md`, `docs/LEGAL_BOUNDARIES.md` |

## Quick Start

```bash
git clone https://github.com/Zer0pa/Indus-Valley.git gnosis-indus
cd gnosis-indus
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[test,numerics]"
pytest -q
```

Expected: `14 passed`. The pytest suite reproduces authority-doc query records against the bundled demo fixture. The real full catalogue stays `FETCH_EXTERNAL` per `DATA_POLICY.md`.

## Upcoming Workstreams

> This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **Phase 4 catalogue extraction wave** — Active Engineering. Extract the first clean runtime slice into `src/gnosis_indus/catalogue/` per `_internal/MIGRATION_PLAN.md`.
- **Phase 5 falsification extraction wave** — Active Engineering. Extract the first clean runtime slice into `src/gnosis_indus/falsification/` per `_internal/MIGRATION_PLAN.md`.
- **Image-rights and provenance review** — Operations / External Dependency. Sign images remain `BLOCKED_RIGHTS` until rights review completes.
- **Full k=70 catalogue redistribution review** — Operations / External Dependency. The 412-sign / 70-cluster / 179-inscription catalogue stays `FETCH_EXTERNAL` until cleared.

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See `LICENSE`. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`.

**Data, fixtures, corpora, image-bearing cultural-heritage assets, private HF artifacts, model weights, endpoint logs, and operational transcripts** are not licensed by the code or documentation licenses. Their boundary is governed by `DATA_POLICY.md`, artifact-specific notices, and any future owner admission record.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights. See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. These license files define the open code/docs posture; they do not publish rights-gated data.


## Traditional-Knowledge Acknowledgment

This repository works with material originating from the Indus Valley Civilization, including the undeciphered Indus script. Zer0pa claims no proprietary right over the Indus script, its imagery, or the archaeological record.

Zer0pa's work is the computational analysis, lattice methods, and falsification discipline applied to that material. This repository does not claim a definitive decipherment of any Indus sign or sequence.

Good-faith inquiries from identified communities, governmental antiquity authorities, or institutional bodies may be sent to architects@zer0pa.ai.
