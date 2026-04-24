# PRD: Project Rosetta Phase 5 — Language Substrate Falsification

**Version:** 1.0
**Date:** 2026-04-16
**Status:** EXECUTING
**Depends on:** Phase 4 (CONDITIONAL PASS), Fresh-Eye Review
**Execution surface:** RunPod (primary compute), Mac M1 (orchestration)

---

## 0. Situation

Phase 4 produced a morphological catalogue (412 signs, 70 clusters, NMI 0.58 against ICIT).
The catalogue is infrastructure — it tells us which signs look alike, not what they mean.
The $1M Tamil Nadu prize requires reading the language. The gap is: what language?

Three competing hypotheses exist:
- **H-Tamil**: Indus script encodes Proto-Dravidian (Tamil ancestor)
- **H-Sanskrit**: Indus script encodes early Indo-Aryan (Sanskrit ancestor)  
- **H-Prakrit**: Indus script encodes Middle Indo-Aryan (Prakrit)

A Popperian falsification framework tests each hypothesis against the corpus.
If one fails and another survives, we've narrowed the language question computationally.

## 1. Governing Objective

**One sentence:** Test whether the statistical fingerprint of the Indus sign corpus is more consistent with Sanskrit, Tamil, or Prakrit phonotactics, using pre-built language models and a Bayesian comparison framework, and produce falsification verdicts.

## 2. Non-Negotiable Laws

1. Never claim decipherment. This is hypothesis testing.
2. A null result (no hypothesis distinguished) is a valid and publishable outcome.
3. All code and artifacts stay in repo custody.
4. No interim reporting. Execute to completion.
5. RunPod is execution surface. Mac is orchestration. GitHub is mirror.

## 3. Tracks

### Track 1: Environment Setup (RunPod)
- SSH to RunPod, set up Python environment
- Clone/sync monorepo (see `PRIVATE_PROVENANCE_APPENDIX.md` for the source root)
- Download required models and datasets
- Verify disk space and compute capacity

### Track 2: Phonotactic Fingerprint Comparison (No decipherment needed)
**Method:** Bayesian model comparison adapted from chemvatho/isthmian-script
1. Extract from Indus corpus: positional entropy, segment-length distributions, bigram transitions, sign-role distributions
2. Extract same statistics from Sanskrit (DCS corpus, syllabified)
3. Extract same from Tamil (OSCAR/IndicCorp, syllabified via indic_nlp_library)
4. Extract same from Prakrit (aso2101/prakrit_texts)
5. Bayesian comparison: which language's phonotactic fingerprint best explains Indus patterns?
6. Control: test against known non-related languages (English, Sumerian) to calibrate

**Gate:** Bayes factor > 3 for any hypothesis = meaningful evidence. BF > 10 = strong.

### Track 3: Character-Level Perplexity Scoring
**Method:** Use byt5-sanskrit and build equivalent Tamil character model
1. Build character-level bigram/trigram models for Sanskrit (from DCS), Tamil (from OSCAR), Prakrit (from aso2101)
2. Take lipi's proposed Sanskrit sign values → transliterate all inscriptions
3. Take Parpola's proposed Dravidian sign values (from published work) → transliterate
4. Score each transliteration's perplexity against each language model
5. Compare: which language + which sign-value mapping produces lowest perplexity?

**Gate:** Perplexity ratio > 2x between best and worst hypothesis = meaningful discrimination.

### Track 4: Neural Decipherment Attempt (NeuroDecipher)
**Method:** Adapt j-luo93/NeuroDecipher for Indus
1. Prepare Indus sign sequences in .cog format
2. Run with Sanskrit as known language → does mapping converge?
3. Run with Tamil as known language → does mapping converge?
4. Compare convergence rates and mapping quality

**Gate:** Mapping convergence (loss decreasing) for one language but not others = evidence.

### Track 5: Morphological Cluster Validation
**Method:** Test our Phase 4 catalogue against language hypotheses
1. Under each proposed sign-value mapping, do morphologically similar signs (same cluster) have phonetically related values?
2. Compute phonetic consistency within clusters for each hypothesis
3. Already tested for lipi (0% consistency) — extend to other mappings

## 4. Data Acquisition Plan

| Resource | Size | Source | Priority |
|----------|------|--------|----------|
| Indus corpus (JSON) | ~1MB | mayig/indus-valley-script-corpus | P0 |
| hellosindh models + dataset | ~50MB | Hugging Face | P0 |
| DCS Sanskrit corpus | ~1.8GB | OliverHellwig/sanskrit | P0 |
| OSCAR Tamil (subset) | ~1GB | Hugging Face (sample) | P0 |
| isthmian-script framework | ~10MB | chemvatho/isthmian-script | P0 |
| NeuroDecipher | ~50MB | j-luo93/NeuroDecipher | P1 |
| Prakrit texts | ~5MB | aso2101/prakrit_texts | P1 |
| byt5-sanskrit model | ~1GB | Hugging Face | P1 |
| indic_nlp_library | pip | PyPI | P0 |
| open-tamil | pip | PyPI | P0 |
| Nacryos cognate pipeline | ~20MB | Hugging Face | P2 |

## 5. Execution Order

```
Track 1 (Setup) → parallel { Track 2, Track 3, Track 4, Track 5 }
```

Track 2 (phonotactic comparison) is the fastest and most likely to produce results.
Track 3 (perplexity) requires building Tamil character model first.
Track 4 (NeuroDecipher) is the most ambitious and may not converge.
Track 5 (cluster validation) extends Phase 4 work.

## 6. Deliverables

All artifacts to `workspace/artifacts/indus/phase5/`

| ID | Deliverable | Track |
|----|------------|-------|
| D1 | Phonotactic fingerprint comparison report | Track 2 |
| D2 | Bayesian model comparison results (Sanskrit vs Tamil vs Prakrit) | Track 2 |
| D3 | Character-level bigram models (all 3 languages) | Track 3 |
| D4 | Perplexity scoring results | Track 3 |
| D5 | NeuroDecipher convergence report | Track 4 |
| D6 | Morphological cluster phonetic consistency | Track 5 |
| D7 | Phase 5 governing verdict | All |

## 7. Verdict Logic

```
IF bayes_factor(H_Tamil vs H_Sanskrit) > 10:
    verdict = "STRONG_EVIDENCE_TAMIL" or "STRONG_EVIDENCE_SANSKRIT"
ELIF bayes_factor > 3:
    verdict = "MODERATE_EVIDENCE_[winner]"
ELIF all hypotheses score similarly:
    verdict = "INDISTINGUISHABLE — corpus too sparse or language not in hypothesis set"
ELIF all hypotheses fail:
    verdict = "NON_LINGUISTIC — supports Farmer/Sproat/Witzel thesis"
```

## 8. Anti-Patterns

- Do NOT claim any sign has a phonetic value based on this work
- Do NOT claim decipherment
- Do NOT optimize for one hypothesis winning — report honestly
- Do NOT skip Prakrit — it's the overlooked middle ground
- Do NOT run massive models that exhaust RunPod disk — sample corpora first
