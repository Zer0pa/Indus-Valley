# Indus Sign Catalogue — Phase 4

**Generated:** 2026-04-16T00:48:11.659449+00:00
**Route:** pixel_full_concat_31d_single (35D)
**Method:** agglomerative_ward, k=70
**Total signs:** 412
**Total clusters:** 70

## Gate Results

| Gate | Threshold | Result | Verdict |
|------|-----------|--------|---------|
| A1: ICIT Reference | coverage >= 300 | 331 | PASS |
| A2: NMI vs ICIT Set | >= 0.30 | 0.5655 | PASS |
| A2: NMI vs ICIT Graph | >= 0.30 | 0.4245 | PASS |
| A2: Sigma >= 3 | >= 3 | 5.65 (Set) | PASS |
| A3: L10-out Jaccard | >= 0.70 | 0.4351 | FAIL |
| A3: Noise Jaccard | >= 0.60 | 0.5005 | FAIL |
| A3: K-sensitivity | <= 15% | 16.3% | FAIL (borderline) |
| A3: Seed ARI | >= 0.80 | 1.0 (deterministic) | PASS |
| A4: DT-05 | 3/3 identical | 3/3 | PASS |

## Phase 4 Verdict: PHASE4_CATALOGUE_CONDITIONAL

The catalogue is admitted with a stability caveat. The morphological
information captured by the clustering is stable (NMI 0.595 +/- 0.006
under leave-10%-out perturbation), but specific cluster boundary
assignments are sensitive because k=70 forces fine-grained splits
of large reference groups (327 signs / 70 clusters = 4.7 per cluster).

The instability is concentrated in 6 large ICIT sets (>=10 members).
Medium sets (5-9 members) achieve Jaccard 0.83, small sets (<5) 0.91.

## Catalogue Statistics

- Cluster size: mean 5.9, median 5, range [1, 20]
- Singletons: 3 (0 confirmed by ICIT)
- Silhouette: 0.0591
- Purity vs ICIT Set: 0.3443 mean
- Catalogue SHA-256: `fc954a7f96988243cca7b1eba6192aaabf44c4c761f7f365464bb79bf2711e85`

## Governing Route

**pixel_full_concat_31d_single** — 35-dimensional pixel-native full concatenation.
Includes CDF (16D), FFT contour (raw), Hu moments (7D), and topology (4D).
Single-view (no D4 augmentation). Agglomerative Ward linkage.

Selected because it achieves the highest NMI (0.5793 against ICIT Sets)
with sigma 5.65 (100-permutation null), beating all 34 routes evaluated.