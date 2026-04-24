---
phase: 02-extraction-and-minimal-replay-surface
verified: 2026-04-24T00:00:00Z
status: passed
verdict: PASS
score: 4/4 acceptance tests verified
consistency_score: 14/14 contract / coherence / falsification checks
independently_confirmed: 14/14
confidence: HIGH (10/10)
re_verification: null
gaps: []
comparison_verdicts:
  - subject_kind: acceptance_test
    subject_id: test-api-shape
    reference_id: ref-phase4-track-c
    comparison_kind: spec_reproduction
    verdict: pass
    metric: api_surface
    threshold: "exposes sign_lookup, sequence_search, subsequence_search with documented field set"
  - subject_kind: acceptance_test
    subject_id: test-query-reproduction
    reference_id: ref-phase4-track-c
    comparison_kind: ground_truth_reproduction
    verdict: pass
    metric: enumerated_match_set
    threshold: "queries 1, 2, 3 exact; query 6 enumerated subset contained; query 9 enumerated subset contained (5 of 7 with '... and 2 more' honest); query 10 exact 5/5"
  - subject_kind: acceptance_test
    subject_id: test-latency-gate
    reference_id: ref-phase4-track-c
    comparison_kind: benchmark
    verdict: pass
    metric: median_latency_ms
    threshold: "< 100 ms"
  - subject_kind: acceptance_test
    subject_id: test-caveat-visibility
    reference_id: ref-phase4
    comparison_kind: audit
    verdict: pass
    metric: caveat_presence
    threshold: "k=70 conditional, non-decipherment, demo-fixture vs full-catalogue all present"
suggested_contract_checks: []
expert_verification: []
---

# Phase 02 Verification — Extraction And Minimal Replay Surface

**Phase goal (from ROADMAP.md):** extract the first clean runtime slice and strengthen the smoke path.

**Verdict:** PASS

**Confidence:** 10/10. Every acceptance test was traced from PLAN contract → test code → implementation → authority document, and the runtime was independently re-executed by this verifier (sys.path injection on macOS) reproducing every enumerated query exactly. The orchestrator additionally re-ran the full pytest suite on a clean RunPod machine after `git pull` and `uv pip install -e .[test]` (14 passed in 0.29s). Authority anchoring was audited verbatim row-by-row across 4 clusters, 8 sample-encoding inscriptions, and 19 partial inscriptions with zero discrepancies.

---

## 1. Acceptance Test Coverage (PLAN contract)

| Acceptance Test | Test in `tests/test_search_surface.py` | Implementation | Verdict |
|---|---|---|---|
| `test-api-shape` | 4 tests (lines 46-89): `test_api_shape_engine_attributes`, `test_api_shape_sign_lookup_returns_documented_fields`, `test_api_shape_sequence_search_returns_documented_fields`, `test_api_shape_subsequence_search_returns_same_shape` | `engine.py` `SearchEngine.sign_lookup/sequence_search/subsequence_search` + dataclasses `SignLookupResult`, `SequenceSearchResult` | **PASS** — `SignLookupResult` carries the doc's 5 fields (cluster_id, cluster_size, members, dominant_set, dominant_graph). `SequenceSearchResult` carries `query`, `matches` tuple of `(id, label, cluster_seq)` 3-tuples, plus `match_count` property. The 3-tuple shape is a strict superset of the plan's "match counts and cluster-sequence lists" — extra `label` field is justified by query 6/7/8/9/10 enumerations that include parenthetical labels (`unicorn II seal` etc.). |
| `test-query-reproduction` | 6 tests (lines 97-194): queries 1, 2, 3, 6, 9, 10 plus a dedicated non-contiguous-trace test | `engine.py` `_contiguous_match` (line 67) and `_order_preserving_subsequence_match` (line 79) | **PASS** — Verifier independently re-ran all 6 queries: q1 cluster=2/size=20/set_04/human; q2 cluster=65/size=3; q3 cluster=38/size=10; q6 enumerated `{M-7A, M-14A, M-15A, M-19A, M-20A}` ⊂ fixture matches (8 total ≤ doc 29); q9 enumerated `{M-36A, M-38A, M-49A, M-91A, M-117A}` ⊂ fixture matches (5 total ≤ doc 7); q10 exactly `{M-64A, M-86A, M-117A, M-122A, M-135A}` count=5. |
| `test-latency-gate` | 1 test (lines 201-214): `test_latency_gate_sequence_search_under_100ms` | `engine.py` `sequence_search` linear scan O(N·Q) | **PASS** — Verifier measured median 0.0656 ms over 5 runs locally (gate is < 100 ms). 1500x margin. The condition matches the authority doc's max query latency 0.0451 ms in the same ballpark. |
| `test-caveat-visibility` | 2 tests (lines 233-257): `test_caveat_visibility_in_package_docstrings`, `test_caveat_visibility_in_fixture_readme` | `__init__.py`, `catalogue.py`, `engine.py`, `_fixture.py` docstrings + `artifacts/phase4/README.md` | **PASS** — All three caveats grep-confirmed in both surfaces; assertions explicitly check `"k=70"`, `"conditional"`, `"decipherment"`, and `"demo fixture"` substrings. |

All four acceptance tests have a real test that exercises the claim, not a weaker proxy. Pass conditions match contract.

---

## 2. Authority Anchoring Audit (zero-fabrication)

**Method:** Loaded `artifacts/phase4/indus_catalogue_demo_fixture.json` and compared every row to `authority/review_pack/search_demo_summary.md` programmatically.

### Cluster memberships (4/4 PASS verbatim)

| Cluster | Authority Doc Source | Size | Members | Set | Graph | Verdict |
|---|---|---|---|---|---|---|
| 2 | Query 1 (sign 324) and Query 4 (sign 86) | 20 | `[10,18,41,56,61,76,79,81,84,86,92,180,186,247,279,324,390,391,406,412]` | `set_04` | `human` | PASS |
| 26 | Query 5 (sign 50) | 5 | `[17,26,50,317,351]` | `set_04` | `human` | PASS |
| 38 | Query 3 (sign 385) | 10 | `[65,230,253,311,337,338,359,368,385,418]` | `set_63` | `U-shape` | PASS |
| 65 | Query 2 (sign 122) | 3 | `[122,219,251]` | `set_01` | `stroke` | PASS |

### Sample Encodings (8/8 PASS verbatim)

| Inscription | Doc raw | Doc cluster | Fixture raw | Fixture cluster | Verdict |
|---|---|---|---|---|---|
| M-1A | `121 202 385 73 108` | `29 5 38 13 32` | match | match | PASS |
| M-3A | `320 145 94` | `17 57 64` | match | match | PASS |
| M-4A | `205 186 147 316 56 122 237 268 268 147` | `4 2 15 40 2 65 44 39 39 15` | match | match | PASS |
| M-5A | `324 96 62 60 120 256` | `2 3 19 19 39 33` | match | match | PASS |
| **M-6A** | `378 384 201 65` (4 tokens) | `57 6 68 38` (4 clusters) | `[378, 384, 201, 65]` | `[57, 6, 68, 38]` | **PASS** — executor correctly trimmed to 4 tokens. The orchestrator's draft schema concern (5th token `154`/`38`) is not present in the landed fixture. |
| M-7A | `86 352 11 324 154 9 154 175 62 122 385` | `2 19 36 2 35 10 35 69 19 65 38` | match | match | PASS |
| M-8A | `316 11 270` | `40 36 12` | match | match | PASS |
| M-9A | `144 205 327` | `57 4 62` | match | match | PASS |

M-2A is correctly absent (the doc table skips it, fixture skips it).

### Partial Inscriptions (19/19 PASS verbatim)

All 19 partial inscriptions (M-14A, M-15A, M-19A, M-20A, M-21A, M-28A, M-30A, M-36A, M-38A, M-44A, M-49A, M-50A, M-54A, M-64A, M-86A, M-91A, M-117A, M-122A, M-135A) match their authority-doc query enumeration lines verbatim, including `-1` unmapped tokens preserved literally.

### Over-coverage check

```
inscriptions not in authority sample table: set()   <-- empty, no fabrications
partials not in authority queries: set()            <-- empty, no fabrications
```

**Audit result:** every fixture row is traceable to a specific line in `search_demo_summary.md`. Zero fabrication.

---

## 3. Falsification Battery (PRD §1.3 + §6.3)

| Falsification target | Result | Evidence |
|---|---|---|
| Phase 4 k=70 stability caveat **visible** | PASS | `__init__.py:9-11`, `catalogue.py:9-10` `engine.py:11-13`, `_fixture.py:46-47`, fixture JSON `$caveat`, README §"Authority caveats carried forward". Contains `"k=70"` and `"conditional"`/`"CONDITIONALLY"`. |
| Decipherment / substrate-identification language **absent** | PASS | All occurrences of "decipherment" are negations: "do NOT encode meaning", "non-decipherment posture", "We do not claim decipherment". No promotion. |
| Search positioned as **in-repo application surface, not sovereign repo** | PASS | All occurrences of "sovereign repo" in repo are negations ("not a sovereign repo"). Decision rows in `DECISIONS.md` reaffirm. |
| **No image-bearing or rights-gated assets** in fixture | PASS | `file artifacts/phase4/*` returns only `JSON data` and `Unicode text, UTF-8 text`. Fixture body contains only integer IDs and cluster sequences. |
| **No fabricated cluster memberships or inscription sequences** | PASS | See §2 — every row verbatim; no extras. |

---

## 4. Cross-Document Coherence

| Check | Result | Evidence |
|---|---|---|
| `SMOKE_TESTS.md` contains `pip install -e .[test] && pytest -q` | PASS | Lines 35-39 show the new code block. The "aspirational Phase 02 target" block is replaced with "Phase 02 stronger smoke path (now real)" wording at line 28. |
| `pyproject.toml` declares `[project.optional-dependencies] test = ["pytest>=8"]` | PASS | Line 18. Also declares `numerics = ["numpy>=1.24"]` at line 17 (plan called it `[numerics]` — exact match). |
| `pyproject.toml` only added keys (no breaking changes) | PASS | Diff shows pure additions: comment, `[project.optional-dependencies]` block, `[tool.pytest.ini_options]` block. `dependencies = []` retained. |
| `.gpd/STATE.md` agrees with `.gpd/state.json` on Phase 02 status | PASS | Both: phase=02, plan=1, status=COMPLETE, progress=80%, last_activity=2026-04-24. |
| `.gpd/REQUIREMENTS.md`: `VALD-04` flipped `[x]` | PASS | Line 47-53: `[x] VALD-04` with note referencing `tests/test_search_surface.py`. |
| `.gpd/REQUIREMENTS.md`: traceability shows Phase 02 → Complete | PASS | Line 101: `CALC-02, CALC-03, DERV-03, VALD-04 \| Phase 02 ... \| Complete`. |
| `.gpd/DECISIONS.md`: Phase 02 pivot row with rollback trigger | PASS | Line 11: Phase 02 row with rollback trigger "a future evidence run produces query results that the clean-room engine cannot reproduce on the demo fixture". |
| `.gpd/ROADMAP.md`: Phase 02 → 1/1 Complete | PASS | Line 98: `02. Extraction And Minimal Replay Surface \| 1/1 \| Complete \| 2026-04-24`. Phase 02 checkbox flipped on line 20. |

---

## 5. Authority-Doc Invariance

`git diff 7f6c7d9..HEAD authority/` → empty. Authority bundle untouched in Phase 02.

---

## 6. Boundary: No Monorepo Helpers

`grep -nE "^(import|from)" src/gnosis_indus/search_surface/*.py`:

```
catalogue.py: from __future__, json, dataclasses, pathlib, typing
engine.py:    from __future__, dataclasses, pathlib, typing, .catalogue
__init__.py:  .catalogue, .engine, ._fixture
_fixture.py:  from __future__, pathlib, .engine
```

**Verdict: PASS** — Pure stdlib + intra-package imports. No monorepo paths, no `zpe_*`, no `cipher_*`, no `phase4_*` external imports. The optional `numpy>=1.24` extra is declared but not imported by any current code path.

---

## 7. Subsequence vs Sequence Semantics (Computational Oracle)

**Engine code:**

- `_contiguous_match` (engine.py:67-76) — sliding window equality, true contiguous-slice match.
- `_order_preserving_subsequence_match` (engine.py:79-90) — single-pass `iter()` over `seq`, advancing through query targets in order. This is the canonical streaming-subsequence algorithm and IS order-preserving non-contiguous.

**Decisive test (M-117A `[11, 15, 40, 26, 63, 57, 65, 57]` vs query `[26, 57, 65]`):**

```
M-117A subsequence match for [26,57,65]: True   <-- 26@idx3, then 57@idx5 (skipping 63), then 65@idx6
M-117A contiguous match for [26,57,65]: False   <-- 63 between 26 and 57 breaks contiguity
M-91A  subsequence match for [26,57,65]: True
M-91A  contiguous match for [26,57,65]: True    <-- M-91A has 26-57-65 contiguous at idx 3-5
M-7A   contiguous match for [65,38]:    True    <-- query 6 sanity
```

**Verdict: PASS.** `subsequence_search` is genuinely order-preserving non-contiguous; M-117A's match for `[26, 57, 65]` is not a coincidental contiguous match because the contiguous algorithm correctly rejects M-117A. The dedicated test `test_query9_specific_match_traces_non_contiguous` (lines 178-194) explicitly asserts BOTH that subsequence_search matches M-117A AND that sequence_search rejects it — pinning the semantic distinction in test code.

---

## 8. Computational Oracle (Live Re-execution)

```
q1 cluster=2 size=20 set=set_04 graph=human
q2 cluster=65 size=3
q3 cluster=38 size=10
q6 count=8 ids=['M-14A', 'M-15A', 'M-19A', 'M-20A', 'M-21A', 'M-28A', 'M-7A', 'M-91A']
q9 count=5 ids=['M-117A', 'M-36A', 'M-38A', 'M-49A', 'M-91A']
q10 count=5 ids=['M-117A', 'M-122A', 'M-135A', 'M-64A', 'M-86A']
latency median=0.0656ms gate=<100ms PASS=True
```

q6 fixture count is 8: doc enumerates 5 (M-7A/M-14A/M-15A/M-19A/M-20A) + fixture also matches M-21A, M-28A, M-91A whose cluster sequences contain `[65, 38]` contiguously (M-21A: `... 65 38`; M-28A: `... 65 38`; M-91A: `... 65 38 ...`). 8 ≤ 29 (doc total). Honest fixture-truncation containment.

q10 = 5 = 5 (doc enumerates all 5; no truncation; exact match required and met).

---

## 9. Discrepancies Found

**None.**

---

## 10. Confidence Assessment

10/10. Reasoning:

1. **Authority anchoring is verbatim.** 4 + 8 + 19 = 31 fixture rows, all programmatically cross-checked against the authority doc with zero discrepancies. The M-6A trim concern (orchestrator brief) is correctly resolved — fixture has the 4-token sequence the doc actually shows.
2. **Subsequence semantics are decisively non-contiguous**, proved by the M-117A computational oracle in §7 — `_order_preserving_subsequence_match` matches and `_contiguous_match` rejects the same `(seq, query)` pair, eliminating the "lucky contiguous accident" hypothesis.
3. **Pure stdlib boundary** is intact — no monorepo helpers smuggled in. The pivot's central premise (clean-room more standalone than copy) is honored.
4. **All four acceptance tests are real**: each has a test that exercises the precise claim, with pass conditions matching the contract; orchestrator independently confirmed `pytest -q` = 14 passed on a clean RunPod machine.
5. **All forbidden language is negated**, never promoted. All required caveats (k=70 conditional, non-decipherment, demo-fixture vs full-catalogue) appear in package docstrings AND the fixture README.
6. **Cross-document coherence** is complete: STATE/state.json/ROADMAP/REQUIREMENTS/DECISIONS/SMOKE_TESTS all agree on Phase 02 → COMPLETE with consistent narrative; authority/ untouched; pyproject only got additive changes.
7. **Latency gate** has 1500x margin (0.07 ms vs 100 ms) — robust.
8. **Truncation honesty**: q6 (29 → fixture 8) and q9 (7 → fixture 5) tests assert subset containment, not equality, with explicit comments about `... and N more`. q10 (5/5 fully enumerated) is asserted as exact.

**Phase 02 is ready to merge into the roadmap as COMPLETE. Orchestrator may advance to Phase 03.**
