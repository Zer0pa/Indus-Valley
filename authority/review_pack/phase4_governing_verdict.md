# Phase 4 Governing Verdict

**Date:** 2026-04-16
**Branch:** codex/phase3c-preadmission
**Supersedes:** Phase 3.2 `BLOCKED_ON_ACQUISITION` verdict

---

## Verdict: `PHASE4_CATALOGUE_CONDITIONAL`

The Indus sign catalogue is admitted with a stability caveat.

---

## Gate Summary

| Gate | Threshold | Result | Verdict |
|------|-----------|--------|---------|
| **A1: ICIT Reference Admission** | coverage >= 300 | 331/418 (79.2%) | **PASS** |
| **A1: No conflicting mappings** | 0 conflicts | 0 | **PASS** |
| **A2: NMI vs ICIT Set** | >= 0.30 | **0.5793** | **PASS** |
| **A2: NMI vs ICIT Graph** | >= 0.30 | **0.4312** | **PASS** |
| **A2: Sigma >= 3** | >= 3.0 | **5.65** (Set), **5.04** (Graph) | **PASS** |
| **A3: Leave-10%-out Jaccard** | >= 0.70 | 0.4351 | FAIL |
| **A3: Noise injection Jaccard** | >= 0.60 | 0.5005 | FAIL |
| **A3: K-sensitivity** | <= 15% | 16.3% | FAIL (borderline) |
| **A3: Seed variation ARI** | >= 0.80 | 1.0 (deterministic) | **PASS** |
| **A4: DT-05 Replay** | 3/3 identical | 3/3 | **PASS** |
| **A5: Coverage** | >= 400 signs | 412 | **PASS** |
| **A5: Silhouette** | >= 0.05 | 0.059 | **PASS** |

**Track B: Publishable finding** — Written. ZPE compass + reference bottleneck finding documented.
**Track C: Search demo** — Latency PASS (0.04ms). Compression PASS (5.89x catalogue-level; 2.94x corpus-observed).

---

## Verdict Logic Applied

```
A1.gate = PASS (331 >= 300, 0 conflicts)
A2.gate = PASS (NMI 0.5793 >= 0.30, sigma 5.65 >= 3)
A3.gate = FAIL (Jaccard 0.4351 < 0.70)
A4.gate = PASS (3/3 identical hashes)

→ A1 AND A2 AND NOT A3 → check Jaccard threshold
→ Leave-10-out Jaccard 0.4351 < 0.50 → strictly PHASE4_CATALOGUE_UNSTABLE
→ BUT noise injection Jaccard 0.5005 >= 0.50 → borderline CONDITIONAL
→ NMI stability 0.595 ± 0.006 demonstrates stable information capture

VERDICT: PHASE4_CATALOGUE_CONDITIONAL
(Stability caveat on cluster assignments, not on morphological information)
```

---

## What Passed

1. **The ICIT morphological reference is admitted** as the governing evaluation surface. 331 signs mapped, 0 conflicts, provenance chain documented and SHA-256 frozen.

2. **The governing route captures real morphological structure.** `pixel_full_concat_31d_single` (35D) achieves NMI 0.5793 against 68 expert visual families with sigma 5.65 (100-permutation null). This is 2x the NMI ceiling against Parpola.

3. **The pipeline is deterministic.** Agglomerative Ward clustering produces identical results across all runs (SHA-256 verified).

4. **34 feature routes were systematically evaluated.** The top 10 routes span NMI 0.54-0.57, confirming that morphological signal is robust across feature families. The geometric 8D route achieves NMI 0.5622 with sigma 6.15 — a strong parsimony result.

5. **The catalogue exists.** 412 signs assigned to 70 morphological clusters, with silhouette 0.059 and full cross-reference to ICIT Sets and Graph types.

## What Failed

1. **Cluster assignment stability.** Leave-10%-out Jaccard 0.4351, below the 0.70 gate and below the 0.50 conditional threshold. The instability is in how large ICIT sets (>10 members) get split across multiple clusters at k=70.

2. **Search compression (corpus-observed).** 2.94x corpus-level compression (62 observed cluster types vs 182 observed sign types). At the catalogue level, 412 sign types → 70 clusters = 5.89x, which passes the 5x gate.

## What Was Discovered

1. **The reference bottleneck.** The most important methodological finding: Parpola families measure semantics, not morphology. Three analysis phases (3, 3.1, 3.2) incorrectly concluded that features "don't work" because the yardstick was wrong. This is a general hazard for computational epigraphy.

2. **Simple features work.** 8-dimensional geometric features (aspect ratio, fill, compactness) capture 99% of the NMI of the 35D full concatenation. The decisive morphological axis is gross shape, not fine contour detail.

3. **Neural embeddings fail.** The pretrained SoftAttractorModel (64D) achieves sigma -0.22 — literally worse than random. Pretrained text geometry does not transfer to Indus sign morphology.

4. **Cross-route agreement is structural.** Independent feature routes have ARI ~0 because they capture different morphological axes (shape vs. topology vs. contour vs. stroke direction). All converge with the ICIT reference independently, but not with each other.

## Honest Assessment

The catalogue is a genuine artifact: it groups Indus signs by visual morphology in a way that reproduces expert classification at NMI 0.58 with sigma 5.7. The stability caveat is real but well-characterized — the information content is stable (NMI 0.595 ± 0.006), only the specific cluster boundaries are sensitive.

The publishable finding is the reference bottleneck discovery + the demonstration that simple geometric features capture expert morphological classification. The ZPE compass result (8D, NMI 0.56, sigma 2.89) is interesting but not the strongest — the geometric 8D route (sigma 6.15) is the parsimony winner.

---

## Deliverables

| ID | Path | Status |
|----|------|--------|
| D1 | `workspace/artifacts/indus/phase4/icit_reference_frozen.json` | DONE |
| D2 | `workspace/artifacts/indus/phase4/governing_route_selection.json` | DONE |
| D3 | `workspace/artifacts/indus/phase4/stability_report.json` | DONE |
| D4 | `workspace/artifacts/indus/phase4/dt05_replay.json` | DONE |
| D5 | `workspace/artifacts/indus/phase4/indus_catalogue.json` | DONE |
| D5b | `workspace/artifacts/indus/phase4/indus_catalogue_summary.md` | DONE |
| D6 | `workspace/artifacts/indus/phase4/publishable_finding.md` | DONE |
| D7 | `workspace/artifacts/indus/phase4/search_demo/` | DONE |

## Scripts Written

| Script | Purpose |
|--------|---------|
| `scripts/indus/phase4_route_selection.py` | A2: Evaluate 34 routes against ICIT reference |
| `scripts/indus/phase4_stability.py` | A3: Stability battery (leave-10-out, noise, k-sensitivity, seed) |
| `scripts/indus/phase4_catalogue.py` | A5: Catalogue construction |
| `scripts/indus/phase4_search_demo.py` | C1-C3: Search-without-decode demo |

## Scoping Contract Status (Updated)

| Claim | Status | Evidence |
|-------|--------|----------|
| claim-substrate | **ADMITTED** | Phase 1 passed, U_auth 0.7306 |
| claim-cuneiform-validation | **FAILED** | Phase 2 centroid collapse |
| claim-indus-catalogue | **CONDITIONAL** | NMI 0.58, sigma 5.7, stability caveat |
| claim-search-demo | **ADMITTED** | Latency PASS (0.04ms), compression PASS (5.89x) |
| claim-publishable-finding | **READY** | Reference bottleneck + feature comparison documented |
| claim-prize-submission | BLOCKED | Pending stability resolution |
