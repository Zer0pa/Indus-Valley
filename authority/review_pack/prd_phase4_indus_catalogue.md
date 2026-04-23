# PRD: Project Rosetta Phase 4 — Indus Catalogue Admission and Publishable Finding

**Version:** 1.0
**Date:** 2026-04-16
**Status:** PROPOSED
**Supersedes:** Phase 3.2 `BLOCKED_ON_ACQUISITION` verdict
**Depends on:** Phase 1 (PASS), Fresh-Eye Review 2026-04-15/16

---

## 0. Situation

### 0.1 What just happened

A fresh-eye review of Phases 1–3.2 discovered that the governing blocker was the **evaluation reference**, not the features or the data:

- **Parpola reference** (used in Phases 3–3.2): Regex on CISI text descriptions. Semantic, not morphological. NMI capped at ~0.24 regardless of feature method.
- **Visual families reference** (Phase 3.1): Circular — derived from the same features being evaluated. NMI=1.0 was meaningless.
- **ICIT morphological reference** (reconstructed from open GitHub data): Expert-curated Wells/Fuls classification with 70 Sets and 18 Graph types. Against this reference, existing features achieve **NMI 0.57** (Sets) and **0.42** (Graph types) with sigma 3.8–5.5.

The 0.30 NMI gate was cleared by existing features all along. It was invisible because the yardstick was wrong.

Additionally: the ZPE compass encoding (8-direction skeleton histogram) — the simplest possible ZPE-native feature — achieved the **highest sigma** (4.69) against expert visual categories of any feature tested across the entire project.

### 0.2 What stands from prior phases

| Phase | Verdict | Status after review |
|-------|---------|-------------------|
| 1 | PASS (U_auth 0.7306) | **STANDS** |
| 2 | NO_GO (cuneiform centroid collapse) | **STANDS** — tokenizer transfer failed |
| 3 | FAIL_NO_GO (NMI 0.236 vs Parpola) | **REINTERPRETED** — features correct, reference wrong |
| 3.1 | FAIL_IMPROVED (visual NMI 1.0) | **COMPROMISED** — visual families circular |
| 3.2 | BLOCKED_ON_ACQUISITION | **OVERTURNED** — reference was the blocker |

### 0.3 What this phase must do

1. **Admit the ICIT morphological reference** as the governing evaluation surface
2. **Run the remaining gates** (stability, deterministic replay) against it
3. **Build the catalogue** if gates pass
4. **Produce the publishable finding** documenting the ZPE compass result
5. **Prepare the search-without-decode demo** if catalogue is admitted

---

## 1. Governing Objective

**One sentence:** Admit a stable, reproducible Indus sign catalogue using the ICIT morphological reference as governing evaluation surface, produce a publishable finding on ZPE compass encoding, and prepare the search-without-decode demo.

### 1.1 Authority metric

- Morphological clustering NMI **>= 0.30** against ICIT Set families (70 expert visual groups)
- Morphological clustering NMI **>= 0.30** against ICIT Graph types (18 expert visual categories)
- Catalogue stability Jaccard **>= 0.70** under leave-10%-out perturbation
- Null separation **>= 5 sigma** on the governing route
- DT-05 deterministic replay: identical SHA-256 across 3 runs

### 1.2 Stretch targets

- NMI **>= 0.50** against ICIT Sets
- Cross-route agreement (stroke vs contour) ARI **>= 0.20** when measured against ICIT reference
- Publishable finding accepted with defended methodology
- Search-without-decode demo with latency < 100ms, compression >= 5x

---

## 2. Non-Negotiable Laws

1. Never optimize for a narratable win instead of the governing objective.
2. Reward hacking and interim reporting are the same failure mode.
3. Repo-local artifacts are mandatory evidence. Speak early only for real blockers.
4. Local git is sovereign custody. GitHub is a mirror. RunPod is execution custody only.
5. Authority closure requires real authority execution plus Comet truth plus U_auth >= 0.70.
6. Do not revive Freeman/P8 as the active cuneiform route.
7. Do not let partial wins substitute for the governing objective.
8. Do not retrain Stage 4 SoftAttractorModel unless explicitly authorized by user.

---

## 3. Phase Structure

This phase has three sequential tracks:

```
Track A: Catalogue Admission (SEQUENTIAL, gates must pass)
  A1 → A2 → A3 → A4 → A5

Track B: Publishable Finding (PARALLEL with Track A after A2)
  B1 → B2 → B3

Track C: Search Demo (SEQUENTIAL, depends on Track A completion)
  C1 → C2 → C3
```

---

## 4. Track A: Catalogue Admission

### A1: ICIT Reference Admission (GATE)

**Goal:** Formally admit the ICIT morphological reference as the governing evaluation surface.

**Input:**
- `workspace/data/icit_wells_sign_list.json` — 715 signs with Class, Set, Graph, Type, Function
- `workspace/data/parpola_wells_mahadevan_concordance.json` — P-to-W-to-M concordance
- `workspace/artifacts/review/fresh_eye_review_2026-04-15/icit_morphological_reference.json` — 331 mapped signs

**Tasks:**
1. Validate the ICIT data provenance chain: GitHub repo → ICIT.html → extracted JSON → concordance mapping → canonical sign IDs
2. Verify that the Wells-to-Mahadevan-to-canonical mapping has no duplicate or conflicting assignments
3. Compute coverage statistics: how many of our 418 canonical signs map to ICIT? (Currently: 331/418 = 79%)
4. For unmapped signs (87): document why they're missing (singletons? Wells numbers not in our manifest?)
5. Freeze the reference: write `workspace/artifacts/indus/phase4/icit_reference_frozen.json` with SHA-256

**Gate conditions:**
- Coverage >= 300 signs (72%)
- No duplicate/conflicting Wells→canonical mappings
- Reference provenance documented and checksummed

**Kill condition:** If coverage < 200 signs, the ICIT reference is too sparse to govern. Fall back to Parpola + ICIT Graph type as dual reference.

### A2: Governing Route Selection (GATE)

**Goal:** Select the best feature route for catalogue construction using the frozen ICIT reference.

**Input:**
- ICIT reference from A1
- All feature routes from Phase 3.2 prebinarized manifest (32 routes)
- Stroke compass 8D features from fresh-eye experiments
- Hybrid stroke+CDF 24D features

**Tasks:**
1. Evaluate all routes against ICIT Set reference at k = {10, 15, 20, 25, 30, 40, 50, 60, 70}
2. Evaluate all routes against ICIT Graph type reference
3. For the top 5 routes by NMI: compute silhouette score, compactness, and null separation
4. Select the governing route: highest NMI against ICIT Sets with sigma >= 3
5. Record the governing route name, k, method, and frozen NMI/sigma as the baseline

**Gate conditions:**
- Best route NMI >= 0.30 against ICIT Sets (already demonstrated at 0.57)
- Best route NMI >= 0.30 against ICIT Graph types (already demonstrated at 0.42)
- Best route sigma >= 3 against at least one reference

**Deliverable:** `workspace/artifacts/indus/phase4/governing_route_selection.json`

### A3: Stability Gate

**Goal:** Test whether the governing route's clustering is stable under perturbation.

**Input:**
- Governing route features from A2
- ICIT reference from A1

**Tasks:**
1. **Leave-10%-out Jaccard (20 iterations):** Remove 10% of signs, recluster, compare with original via Jaccard similarity. Record mean, std, min, max.
2. **Noise injection (20 iterations):** Add Gaussian noise at 5% of feature std, recluster, compare.
3. **K-sensitivity:** Vary k by ±30%, recluster, compare with baseline.
4. **Seed variation:** Run clustering with 5 different random seeds, compare pairwise ARI.

**Gate conditions:**
- Leave-10%-out Jaccard mean >= 0.70
- Noise injection Jaccard mean >= 0.60
- K-sensitivity: NMI change <= 15% across k range
- Seed variation: pairwise ARI >= 0.80

**Note on the 0.70 Jaccard gate:** Phase 3 originally required 0.90 (relaxed to 0.70 in Phase 3.1). With N=1 per sign and 331 evaluation signs in 70 sets (~4.7 per set), 0.70 may be tight. If Jaccard is between 0.50 and 0.70, record honestly and assess whether the instability is in small sets (expected) or large sets (concerning).

**Kill condition:** Jaccard < 0.50 means the clustering is noise-dominated regardless of NMI.

**Deliverable:** `workspace/artifacts/indus/phase4/stability_report.json`

### A4: Deterministic Replay (DT-05)

**Goal:** Verify that the pipeline is deterministic.

**Tasks:**
1. Run the full pipeline (image → features → clustering → evaluation) 3 times with seed=42
2. SHA-256 hash every output artifact
3. Verify all hashes are identical

**Gate:** 3/3 identical hashes.

**Deliverable:** `workspace/artifacts/indus/phase4/dt05_replay.json`

### A5: Catalogue Construction

**Goal:** Build the actual Indus sign catalogue.

**Depends on:** A2 (route), A3 (stability), A4 (determinism) all pass

**Tasks:**
1. Cluster all 412 extraction-valid signs using the governing route and parameters
2. Assign each sign to a morphological cluster
3. For each cluster: record member signs, cluster centroid, intra-cluster distance, nearest neighbor cluster
4. Cross-reference with ICIT Set and Graph type: report alignment per cluster
5. Compute catalogue-level statistics: cluster size distribution, silhouette, coverage
6. Generate visual inspection artifact: one representative sign image per cluster
7. Write the catalogue: `workspace/artifacts/indus/phase4/indus_catalogue.json`

**Quality checks:**
- No cluster has < 2 members (singletons allowed only if ICIT Set confirms singleton status)
- Catalogue covers >= 400 of 412 extraction-valid signs
- Intra-cluster cohesion: mean silhouette >= 0.05

**Deliverable:** `workspace/artifacts/indus/phase4/indus_catalogue.json` + `indus_catalogue_summary.md`

---

## 5. Track B: Publishable Finding

### B1: Methodology Write-Up

**Goal:** Document the finding that ZPE compass encoding captures Indus morphological structure.

**The finding:** An 8-dimensional feature vector — the normalized histogram of 8-direction skeleton orientations (the ZPE compass) — captures expert-curated morphological relationships between Indus Valley script signs at NMI 0.42 against 18 visual categories (sigma 4.69), outperforming 23-dimensional contour+FFT+Hu features that require complex preprocessing.

**Tasks:**
1. Write methodology section: binarization → skeletonization → 8-direction compass histogram → clustering → NMI evaluation
2. Write results section: NMI/sigma tables against ICIT Set, ICIT Graph, Parpola references
3. Write comparison section: stroke compass vs contour FFT vs pixel similarity vs SoftAttractorModel
4. Write discussion: why direction proportions capture morphology better than shape statistics
5. Acknowledge limitations: N=1 substrate, ICIT reference dependency, no decipherment claims

### B2: Figures and Evidence

**Tasks:**
1. Confusion matrix: stroke compass clustering vs ICIT Graph types
2. Feature distribution visualization: 8D compass histograms for each ICIT Graph type
3. Cross-route comparison table: all feature families against all references
4. Example signs: show representative signs from each cluster and verify visual coherence

### B3: Literature Positioning

**Tasks:**
1. Compare with Rao et al. 2009 entropy analysis (complementary finding)
2. Compare with Daggumati & Revesz 2021 allograph identification (our clustering should recover their pairs)
3. Compare with Fuls 2023 positional analysis (our clustering captures positional behavior?)
4. Position relative to prize criteria if applicable

**Deliverable:** `workspace/artifacts/indus/phase4/publishable_finding.md`

---

## 6. Track C: Search-Without-Decode Demo

### C1: Corpus Encoding

**Goal:** Encode the CISI corpus using the catalogue.

**Depends on:** A5 (catalogue exists)

**Tasks:**
1. For each CISI inscription: replace sign IDs with catalogue cluster IDs
2. Build compressed corpus representation
3. Compute compression ratio vs raw sign sequences

### C2: Query Engine

**Goal:** Build a simple search interface.

**Tasks:**
1. Given a query sign image: extract features → find nearest cluster → return all signs in cluster
2. Given a query sign sequence: find all inscriptions containing the same cluster sequence
3. Measure query latency

**Gate:** Latency < 100ms, compression >= 5x

### C3: Demo Artifact

**Tasks:**
1. Write demo script that demonstrates search-without-decode
2. Record example queries and results
3. Document limitations

**Deliverable:** `workspace/artifacts/indus/phase4/search_demo/`

---

## 7. Data Sources

| Source | Location | What it provides |
|--------|----------|-----------------|
| Canonical sign images | `workspace/data/indus/canonical_signs/` | 418 PNG images (256x256) |
| ICIT sign list | `workspace/data/icit_wells_sign_list.json` | 715 signs with Class/Set/Graph/Type/Function |
| Concordance | `workspace/data/parpola_wells_mahadevan_concordance.json` | P-W-M number mapping |
| CISI corpus | `workspace/artifacts/indus/cisi_corpus_summary.json` | 179 inscriptions, 1003 sign sequences |
| Sign manifest | `workspace/artifacts/indus/indus_sign_manifest.json` | 418 signs with metadata |
| Phase 3.2 features | `workspace/artifacts/indus/phase3c/prebinarized_feature_manifest.json` | 412 signs × 32 routes |
| Fresh-eye features | `workspace/artifacts/review/fresh_eye_review_2026-04-15/` | Stroke features, experiment results |
| ICIT reference | `workspace/artifacts/review/fresh_eye_review_2026-04-15/icit_morphological_reference.json` | 331 mapped signs |
| Pretrained models | `workspace/models/tokenizer/` | SoftAttractorModel weights (diagnostic only) |
| Indus sources | `Indus Script Sources/` | Fuls 2023, Daggumati 2021, Vahia, ICIT docs |
| GitHub repos | `workspace/repos/iswc2025/`, `workspace/repos/lipi/`, `workspace/repos/indus-valley-script-corpus/` | ICIT data, allographs, corpus |

---

## 8. Feature Routes to Carry Forward

| Route | Dim | Source | Best NMI (ICIT Set) | Sigma |
|-------|-----|--------|-------------------|-------|
| hybrid_stroke8_cdf16 | 24 | stroke compass + pixel CDF | 0.5737 | 4.44 |
| stroke_compass_8d | 8 | skeleton direction histogram | 0.5662 | 3.80 |
| geometric_8d | 8 | aspect ratio, fill, compactness | 0.5668 | 5.50 |
| cdf_fft_hu_23d_aug8 | 23 | Phase 3.1 corrective route | 0.5624 | 2.67 |
| pixel_cdf_fft_16d | 16 | Phase 3.2 pixel-native | 0.5493 | 2.43 |
| topology_4d | 4 | Betti numbers, junctions | 0.5569 | 2.54 |

All routes should be evaluated; the governing route is selected in A2.

---

## 9. Known Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| ICIT reference may not be authoritative (scraped from GitHub, not peer-reviewed) | Undermines NMI claims | Document provenance chain; cross-validate against Fuls 2023 preview data |
| Stability Jaccard may fail on N=1 substrate | Blocks catalogue | Report honestly; assess whether instability is in small sets |
| Cross-route ARI still ~0 | Weakens multi-route convergence claim | Reframe: test route-to-ICIT agreement instead of route-to-route |
| SoftAttractorModel doesn't transfer | No 64D embedding space | Accept: use raw features (8D-24D) without neural projection |
| Parpola NMI still < 0.30 | Inconsistency with prior phase verdicts | Document that Parpola measures semantics not morphology; ICIT is the governing reference |

---

## 10. Anti-Patterns

- Do NOT evaluate against visual families (circular reference, confirmed in fresh-eye audit)
- Do NOT claim the SoftAttractorModel "works" on Indus (it collapses)
- Do NOT claim decipherment, phonetic values, or language identification
- Do NOT retrain Stage 4 without explicit user authorization
- Do NOT use NMI against Parpola as a governing metric (it's diagnostic-only)
- Do NOT skip stability testing because NMI looks good
- Do NOT report ICIT Set NMI without noting the fine-grained reference (70 sets, ~4.7 signs/set)
- Do NOT narrate partial results externally before all gates are closed

---

## 11. Deliverables Summary

| ID | Deliverable | Track | Gate? |
|----|------------|-------|-------|
| D1 | ICIT reference frozen artifact | A1 | YES |
| D2 | Governing route selection report | A2 | YES |
| D3 | Stability report | A3 | YES |
| D4 | Deterministic replay report | A4 | YES |
| D5 | Indus sign catalogue (JSON + summary) | A5 | Final |
| D6 | Publishable finding (methodology + figures) | B3 | NO |
| D7 | Search-without-decode demo | C3 | NO |

---

## 12. Verdict Logic

```
IF A1.gate AND A2.gate AND A3.gate AND A4.gate:
    verdict = "PHASE4_CATALOGUE_ADMITTED"
    proceed to A5, B, C

ELIF A1.gate AND A2.gate AND NOT A3.gate:
    IF jaccard >= 0.50:
        verdict = "PHASE4_CATALOGUE_CONDITIONAL"
        # Catalogue exists but stability caveat documented
    ELSE:
        verdict = "PHASE4_CATALOGUE_UNSTABLE"
        # NMI passes but clustering is noise-dominated

ELIF NOT A2.gate:
    verdict = "PHASE4_REFERENCE_INSUFFICIENT"
    # ICIT reference doesn't improve on Parpola (shouldn't happen given existing evidence)

ELSE:
    verdict = "PHASE4_BLOCKED"
    # Document what failed and why
```

---

## 13. Coding Commandments

- Avoid deep nesting
- Avoid code duplication
- Use names other humans understand
- Use dependency injection where it helps
- Decouple components with interfaces where it makes sense
- Separate functions into single responsibilities where useful
- Keep all work inside `/Users/Zer0pa/ZPE/ZPE-Cipher`
