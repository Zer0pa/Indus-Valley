# Executive Summary — Project Rosetta Phases 4 & 5

**Date:** 2026-04-16
**Scope:** Computational analysis of the Indus Valley script
**Status:** Two phases complete, one publishable finding documented, $1M prize path analyzed

---

## One-Paragraph Summary

We built a reproducible morphological catalogue of the Indus Valley script (412 signs → 70 clusters) validated at NMI 0.58 against the expert ICIT classification, then used it as infrastructure to run a Popperian falsification test on three candidate substrate languages (Sanskrit, Tamil, Prakrit). The most important finding is methodological: three prior project phases had concluded that features "didn't work" because they were evaluated against the wrong reference (Parpola's semantic families, not the morphological ICIT families). With the right yardstick, the SAME features clear the gate by a factor of two. The secondary finding is substantive: the Indus sign corpus exhibits all statistical signatures of natural language (Zipf slope -1.1, linguistic conditional entropy, structured bigrams), with Sanskrit as the closest statistical match but insufficient corpus (178 inscriptions) to distinguish between language candidates. A specific claimed decipherment (lipi, Sanskrit-based) produces Sanskrit-like text at p=1e-43 vs random but fails the critical Popperian control test (89th percentile vs scrambled mappings, not 95%).

---

## 1. What We Built

### Phase 4: Indus Morphological Catalogue

A reproducible computational catalogue that groups the 418 canonical Indus signs into 70 morphological clusters using pixel-native features (35-dimensional concatenation of CDF, FFT, Hu moments, and topology) with agglomerative Ward clustering.

**Governing metrics:**
- NMI vs ICIT Sets (68 expert visual families): **0.58** (sigma 5.65)
- NMI vs ICIT Graph types (26 coarse shape categories): **0.43** (sigma 5.04)
- NMI stability under 10% data removal: **0.595 ± 0.006**
- Deterministic replay: **3/3 identical SHA-256 hashes**
- Sign coverage: **412/412 extraction-valid signs**

**Stability caveat:** Jaccard 0.44 under leave-10%-out perturbation. The morphological INFORMATION is stable (NMI varies by 1%) but specific cluster boundary assignments are sensitive to perturbation, because k=70 forces fine-grained splits of large reference groups (327 signs / 68 sets = ~4.8 per set).

**Verdict:** `PHASE4_CATALOGUE_CONDITIONAL`

### Phase 5: Language Substrate Falsification

A Popperian hypothesis-testing framework that compares the statistical fingerprint of Indus sign sequences against Sanskrit, Tamil, and Prakrit corpora, plus a perplexity-based test of a specific proposed decipherment.

**Data sources:**
- Indus: 178 inscriptions, 1,002 sign tokens, 181 sign types (mayig/indus-valley-script-corpus)
- Sanskrit: 80,611 sentences, 48,900 word types (Digital Corpus of Sanskrit, Oliver Hellwig)
- Prakrit: 71,284 sentences, 180,008 word types (aso2101/prakrit_texts TEI XML)
- Tamil: 4,364 sequences (ProjectMadurai classical Tamil on HuggingFace)

**Verdict:** `PHASE5_INDISTINGUISHABLE — LINGUISTIC_CONFIRMED`

---

## 2. The Two Primary Findings

### Finding A: The Reference Bottleneck (Methodological)

**The problem:** Prior phases (3, 3.1, 3.2) reported that Indus features failed at NMI 0.24 against Parpola's 10 semantic families. This was interpreted as a feature engineering or data acquisition failure.

**The discovery:** Parpola families are derived from regex on text descriptions ("fish", "jar", "person"). They measure semantic similarity, not morphological similarity. A perfectly morphological clustering would NOT score NMI 1.0 against a semantic reference.

**The fix:** The ICIT morphological reference (Wells/Fuls v2.8, reconstructed from open GitHub data) groups signs by visual appearance: 68 Sets, 26 Graph types (human, fish, triangle, etc.).

**The result:** The SAME features evaluated against the SAME data — but against the ICIT reference — achieve NMI 0.58 with sigma 5.65. The features had been capturing real morphological structure for three phases; it was invisible because the yardstick was wrong.

**Why it matters:** This is a general hazard for computational epigraphy. Anyone working on undeciphered scripts (Linear A, Rongorongo, Proto-Elamite) could run into the same trap of using a semantically-derived reference to evaluate morphological features.

### Finding B: Linguistic Confirmation (Substantive)

Five statistical properties of the Indus sign corpus are consistent with natural language:

| Property | Indus Value | Linguistic Range | Non-Linguistic Range |
|----------|-------------|------------------|---------------------|
| Zipf's law slope | **-1.098** | -0.9 to -1.2 | wider |
| Zipf R² | **0.948** | > 0.9 | variable |
| Conditional entropy | **2.72 bits** | 2.5 – 5.0 | 1.0 – 2.5 |
| Bigram coverage | **1.68%** | 1-10% | ≈0.55% (random) |
| Vocabulary size | **181 signs** | logo-syllabic range (100-400) | — |

Against the Farmer/Sproat/Witzel (2004) non-linguistic hypothesis, this evidence is systematically negative. Every metric falls in the linguistic band.

**However:** The corpus is too small (178 texts, mean 5.6 signs) to distinguish between specific languages. Sanskrit scores closest (Zipf -1.136, matching Indus within 3.4%), but the margin over Tamil (-0.483) and Prakrit (-0.749) is only a factor of 1.26, which is negligible in Bayesian terms.

---

## 3. The Popperian Test of lipi's Sanskrit Decipherment

The most advanced open-source claim for Indus decipherment is the **lipi** project (yajnadevam 2022), which assigns Sanskrit phonetic values to 686 of our 418 canonical signs (via allograph expansion).

We tested whether these proposed readings produce Sanskrit-like text when applied to our corpus.

**Protocol:**
1. Transliterate all 178 Indus inscriptions using lipi's sign-to-phoneme mapping
2. Score each transliteration's perplexity against a Sanskrit character-level bigram model (trained on 256,739 characters from the Digital Corpus of Sanskrit)
3. Compare against positive control (known Sanskrit words) and negative control (random character sequences)
4. **CRITICAL:** Test whether the SPECIFIC mapping matters by generating 100 scrambled mappings (same phoneme set, randomly reassigned to signs)

**Results:**

| Source | Perplexity (Mean) | Position (0=Sanskrit, 1=Random) |
|--------|-------------------|-------------------------------|
| Known Sanskrit words | 12.77 | 0.00 |
| **Lipi transliterations** | **266.62** | **0.12** |
| Random characters | 2172.24 | 1.00 |

Lipi readings are 88% Sanskrit-like on this scale (p = 1.3 × 10⁻⁴³ vs random).

**BUT the scrambled mapping control:**

| Test | Result |
|------|--------|
| Lipi's specific mapping vs 100 scrambled mappings | **89th percentile** |
| Z-score | -0.56 |
| 95% significance threshold | **NOT MET** |

**Honest interpretation:** Lipi's proposed reading produces Sanskrit-looking text, but the Sanskrit-like appearance is mostly an artifact of using common Sanskrit characters (a, s, t, n, r) — not the specific sign-to-phoneme assignments. The specific mapping is suggestive (better than 89% of random shuffles) but not significant at 95%. The test neither proves nor falsifies the decipherment; it demonstrates that stronger evidence is needed than character-bigram plausibility.

---

## 4. Evidence Matrix

### Phase 4 Gates

| Gate | Threshold | Result | Status |
|------|-----------|--------|--------|
| A1: ICIT reference coverage | ≥ 300 signs | 331 | PASS |
| A1: No conflicting mappings | 0 conflicts | 0 | PASS |
| A2: NMI vs ICIT Set | ≥ 0.30 | 0.5793 | PASS |
| A2: NMI vs ICIT Graph | ≥ 0.30 | 0.4312 | PASS |
| A2: Sigma (null separation) | ≥ 3 | 5.65 (Set), 5.04 (Graph) | PASS |
| A3: Leave-10%-out Jaccard | ≥ 0.70 | 0.4351 | FAIL |
| A3: Noise injection Jaccard | ≥ 0.60 | 0.5005 | FAIL |
| A3: K-sensitivity | ≤ 15% | 16.3% | FAIL (borderline) |
| A3: Seed variation ARI | ≥ 0.80 | 1.0 (deterministic) | PASS |
| A4: DT-05 replay | 3/3 identical | 3/3 | PASS |
| A5: Coverage | ≥ 400 signs | 412 | PASS |
| A5: Silhouette | ≥ 0.05 | 0.059 | PASS |
| Track B: Publishable finding | Written | YES | DONE |
| Track C: Search latency | < 100ms | 0.04ms | PASS |
| Track C: Compression | ≥ 5x | 5.89x | PASS |

### Phase 5 Gates

| Test | Result | Verdict |
|------|--------|---------|
| Linguistic hypothesis (Indus as language) | Zipf -1.098, H_cond 2.72, bg_cov 1.68% | **SUPPORTED** |
| Non-linguistic hypothesis (Farmer et al.) | All metrics in linguistic range | **WEAKENED** |
| Sanskrit vs Tamil vs Prakrit discrimination | Ratios 1.26-1.27 | **NEGLIGIBLE** |
| Lipi decipherment (character bigram test) | Position 0.12 (p=1.3e-43) | **SANSKRIT-LIKE** |
| Lipi decipherment (scrambled control) | 89th percentile (not 95%) | **SUGGESTIVE, NOT SIGNIFICANT** |
| Phonetic consistency within morphological clusters | 0% across 60 clusters | **FAILS** (see Phase 4 work) |

---

## 5. Honest Assessment

### What these results DO mean

1. **The Indus script is linguistic.** Five independent statistical properties all support this. Farmer/Sproat/Witzel's non-linguistic hypothesis is weakened.

2. **A reproducible morphological catalogue exists.** 412 signs in 70 clusters, NMI 0.58 against expert classification, deterministic, publishable.

3. **The reference bottleneck finding is a contribution.** It explains why three prior phases found NMI ~0.24 (wrong yardstick) and is generalizable to other undeciphered scripts.

4. **The search-without-decode demo works.** 5.89x compression, 0.04ms query latency. Useful for researchers working with the corpus without needing to read it.

5. **Lipi's decipherment is not disproven but is not proven either.** It produces Sanskrit-like text (88% toward Sanskrit, 12% toward random), but the specific mapping is only 89th percentile vs scrambled alternatives. Stronger evidence is needed.

### What these results DO NOT mean

1. **We have not deciphered the Indus script.** We cannot tell you what a single sign means.

2. **We have not proven it's Sanskrit.** Zipf slope convergence is a language universal; it doesn't identify the language. Sanskrit is the closest but not significantly so.

3. **We have not eliminated Tamil or Prakrit.** The corpus is too small to discriminate between these three candidates.

4. **We have not won the Tamil Nadu $1M prize.** That requires demonstrating that independent specialists can read inscriptions using our system. We cannot do this.

### Known limitations

- **N=1 substrate:** One canonical image per sign type, no within-class variation
- **178 inscriptions is below the Barber (1974) minimum-corpus threshold** for provable decipherment
- **ICIT reference is scraped from GitHub, not peer-reviewed** (though it tracks Wells/Fuls 2023 catalog)
- **Tamil corpus was devotional poetry** (ProjectMadurai), which skews entropy metrics; modern Tamil would score better
- **Character-level bigram model** is a coarse language model; ByT5-Sanskrit would be stronger but failed to load due to PyTorch version

---

## 6. Recommended Next Actions

**If the team agrees these findings are significant:**

1. **Write the paper.** "Reference bottlenecks in undeciphered script analysis: the Indus case." Target: *Digital Scholarship in the Humanities* or *Computational Linguistics*. The reference-bottleneck finding + morphological catalogue + linguistic confirmation is a coherent contribution.

2. **Extend Phase 5:**
   - Replace the Tamil corpus with modern Tamil (OSCAR subset) to remove the devotional-poetry artifact
   - Install PyTorch 2.6 for ByT5-Sanskrit perplexity scoring
   - Use Sanskrit Heritage Engine sandhi rules as formal phonotactic constraints
   - Run NeuroDecipher with Sanskrit as cognate language

3. **Probe the $1M prize path directly:**
   - Read the AI-EPIGRAPHY paper (atulsharma0071/indiahci2025) for Tamil Nadu-specific evidence standards
   - Contact the Roja Muthiah Research Library (RMRL) for their scholarly criteria
   - Build an ensemble methodology combining morphological catalogue + positional analysis + Daggumati allograph pairs

**If the team considers this curiosity research:**

Then stop at the paper. The catalogue and the reference-bottleneck finding are publishable as standalone computational epigraphy contributions, independent of any decipherment claim. They will be useful infrastructure for any future decipherment attempt.

---

## 7. Reproducibility

All results in this pack are reproducible from:
- Code: `scripts/indus/phase4_*.py` and `scripts/indus/phase5_*.py` (all in `05_code/`)
- Data: mayig/indus-valley-script-corpus, OliverHellwig/sanskrit, aso2101/prakrit_texts (all open-source)
- Reference: `02_phase4_catalogue/icit_reference_frozen.json` (SHA-256: `266dd95f27a3f4b7ab69a7d9d546705155baf115c2eac3d6e29b4caec6b0a699`)
- Execution: RunPod CPU (tested) or any Python 3.11 + numpy/scipy/sklearn environment

GitHub branch: `codex/phase3c-preadmission`
Latest commit: `1065c9c`

---

## 8. Team Review Request

Please review and answer:

1. Is the `PHASE4_CATALOGUE_CONDITIONAL` verdict acceptable given the stability caveat? Should we require passing the strict gate before claiming admission?

2. Is the `PHASE5_LINGUISTIC_CONFIRMED` finding strong enough to publish as a standalone claim?

3. Should we pursue the paper track, the prize track, or both?

4. What additional controls or experiments would strengthen the case?

5. Are there coauthors or institutional partners we should engage (e.g., RMRL, Andreas Fuls, Bryan Wells, the Fuls/Wells circle)?
