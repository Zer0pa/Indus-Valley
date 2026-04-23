# Phase 01 Verification — Source Truth And Authority Admission

- **Verdict:** `PASS_WITH_NOTES`
- **Verified on:** 2026-04-24
- **Verifier:** gpd-verifier (independent; Vercel-plugin bootstrap)
- **Commits verified:** `ac82c5b`, `cef9941`, `abb76eb` (origin/main..HEAD)
- **Governing surfaces:** `01-01-PLAN.md`, `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `MIGRATION_PLAN.md`, `SMOKE_TESTS.md`, `docs/LEGAL_BOUNDARIES.md`, `docs/family/INDUS_EXPORT_CONTRACT.md`, `.gpd/STATE.md`, `.gpd/state.json`, `.gpd/REQUIREMENTS.md`, `.gpd/ROADMAP.md`, `.gpd/DECISIONS.md`, `.gpd/PROJECT.md`
- **Ground truth for numerical claims:** `authority/review_pack/search_demo_summary.md`, `authority/review_pack/phase4_governing_verdict.md`

## Result

Phase 01 satisfies its contract. All three acceptance tests pass on evidence, all four falsification-battery items pass, authority/ and src/ are untouched, and the smoke path is not broken. One coherence defect remains: `.gpd/STATE.md` line 95 still carries the stale uncertainty "first extraction slice is not yet chosen" under `Propagated Uncertainties`, which contradicts the same file (lines 11–12, 46–47) and `state.json` (where that entry was correctly replaced). This is a stale-text issue inside one control-plane doc, not a contract failure.

Recommendation: orchestrator may advance state and push, but fix `.gpd/STATE.md` line 95 in the same push or at the top of Phase 02.

## Acceptance Tests

| Test ID | Subject | Result | Evidence |
| --- | --- | --- | --- |
| `test-source-ledger` | claim-source-admission | **PASS** | `SOURCE_BOUNDARY.md` now has three explicit buckets: **Included now** (5 families), **First extraction slice** (`phase4_search_demo.py`, flagged `FIRST SLICE — Phase 02`), **Deferred second/third wave** (Phase 4 `phase4_*.py`, Phase 5 `phase5_*.py`, `workspace/artifacts/indus/phase4`, `workspace/artifacts/indus/phase5`), and **Out of scope** (cuneiform, separate script-search repo, shared kernels, outreach). Line 62–64 states: "No `scripts/indus/phase4_*.py` or `scripts/indus/phase5_*.py` family is in a grey zone any longer." Verified by enumerating each `scripts/indus/` family named in the diff — each has an explicit class. |
| `test-data-posture` | claim-source-admission | **PASS** | `DATA_POLICY.md` already had the 5-class taxonomy (`PUBLIC_NOW`, `PUBLIC_LATER`, `FETCH_EXTERNAL`, `BLOCKED_RIGHTS`, `OWNER_DEFERRED`). The diff ADDS a first-slice classification table mapping derived cluster tables → `PUBLIC_LATER`, latency/compression numbers → `PUBLIC_NOW`, raw sign images → `BLOCKED_RIGHTS`, ICIT reference JSON → `FETCH_EXTERNAL`, Phase 5 corpora → `FETCH_EXTERNAL`. It also adds an off-repo storage surfaces table (private HF dataset/model repos, RunPod workspace) with explicit rights posture. `LEGAL_BOUNDARIES.md` adds a row reinforcing that derived HF artefacts stay private. Rights claim is **narrower**, not wider — raw images stay `BLOCKED_RIGHTS`, ICIT stays `FETCH_EXTERNAL`. |
| `test-first-extraction-target` | claim-source-admission | **PASS** | `MIGRATION_PLAN.md` "First extraction targets (in execution order)" names search-without-decode as #1 with full justification (rights risk, dependency footprint, smoke-path story). `SMOKE_TESTS.md` adds a "Phase 02 target smoke expectation" section with a concrete executable block asserting `sign_lookup`, `sequence_search`, `subsequence_search` and numeric gates (`max_latency_ms < 100.0`, `compression_ratio() >= 5.0`). Phase 02 can begin without reopening source-boundary ambiguity. |

## Falsification Battery (PRD §1.3 + §6.3)

| Item | Result | Evidence |
| --- | --- | --- |
| Phase 4 k=70 stability caveat preserved | **PASS** | `SOURCE_BOUNDARY.md:50` — "starting with the search surface avoids pulling the k=70 stability caveat into runtime before the caveat itself has been given a proper runtime home." `SOURCE_BOUNDARY.md:57` — second wave "must carry the Phase 4 `PHASE4_CATALOGUE_CONDITIONAL` k=70 stability caveat into runtime text." `MIGRATION_PLAN.md:39` — second wave "must carry the `PHASE4_CATALOGUE_CONDITIONAL` verdict and the k=70 stability caveat visibly into runtime docstrings." `INDUS_EXPORT_CONTRACT.md:19-20` (untouched by this diff) still requires every exported morphology surface to state whether it cites k=70 conditional vs k=100 paper surface vs both. No new language softens or erases the caveat. |
| No decipherment / substrate-identification language | **PASS** | No new phrase in the diff crosses the line. `docs/LEGAL_BOUNDARIES.md:23` unchanged: "no decipherment or broad product-rights claim is made here." `SOURCE_BOUNDARY.md:58` — third wave "must preserve `PHASE5_INDISTINGUISHABLE - LINGUISTIC_CONFIRMED`." `MIGRATION_PLAN.md:45-46` — same. `INDUS_EXPORT_CONTRACT.md:21-22` (untouched) — "linguistic structure does not equal decipherment or substrate closure." |
| Search positioned as in-repo application surface (not sovereign repo) | **PASS** | `INDUS_EXPORT_CONTRACT.md:14` (diff): "belongs inside `gnosis-indus`, not as a separate sovereign repo; first real bundle expected in Phase 02." `SOURCE_BOUNDARY.md:69` — "a separate `gnosis-script-search` repo boundary" listed under Explicitly out of scope. `state.json:73` — `forbidden_estimator_families` includes "standalone search spinout." No diff hunk reverses this. |
| No public image-rights inflation | **PASS** | `DATA_POLICY.md` diff keeps raw sign images as `BLOCKED_RIGHTS` (line 39) and ICIT reference JSON as `FETCH_EXTERNAL` (line 40). `LEGAL_BOUNDARIES.md` diff only adds a row stating HF artefacts are private with no public redistribution. `INDUS_EXPORT_CONTRACT.md` diff only appends a Phase 02 pointer — does not widen rights. Rule 4 of the contract ("Image-bearing exports require a rights review before public release.") is untouched. The new HF row is a narrowing: it documents that private surfaces stay private. |

## Cross-Document Coherence

| Check | Result | Evidence |
| --- | --- | --- |
| `SOURCE_BOUNDARY.md` first-slice choice matches `MIGRATION_PLAN.md` execution order | **PASS** | Both name `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/` as #1. Both sequence `phase4_*.py` → `catalogue/` as #2 and `phase5_*.py` → `falsification/` as #3. |
| `DATA_POLICY.md` first-slice artefact classes match the search-surface slice in `SOURCE_BOUNDARY.md` | **PASS** | `SOURCE_BOUNDARY.md:34` cites cluster IDs and sign-ID integers as inputs; `DATA_POLICY.md:36-37` classes exactly those (`indus_catalogue.json`, cluster sequences) as `PUBLIC_LATER`. Latency/compression numbers (`PUBLIC_NOW`) map to the Track C gates both docs reference. Neither introduces an artefact not in the other. |
| `SMOKE_TESTS.md` Phase 02 target smoke vs `INDUS_EXPORT_CONTRACT.md` `search_application_bundle` | **PASS** | `SMOKE_TESTS.md:42-44` asserts three methods (`sign_lookup`, `sequence_search`, `subsequence_search`). These are exactly the three query types tabulated in `authority/review_pack/search_demo_summary.md` (lines 43-141). `INDUS_EXPORT_CONTRACT.md:14` names the bundle as "search demo summary plus any future search interface docs" — the smoke-path API is the minimal interface that surface must expose. Consistent. |
| `.gpd/STATE.md` agrees with `.gpd/state.json` | **PASS_WITH_NOTES** | Matched on: status=COMPLETE, last_activity=2026-04-24, progress=60%, session stopped-at text, pending_todos, decisions (new Phase 01 entry appears in both). **DISAGREEMENT:** `STATE.md:95` still lists "first extraction slice is not yet chosen" under `Propagated Uncertainties`; `state.json:352` correctly replaced this entry with "Runtime dependency list is not frozen until the first slice lands in Phase 02." This is stale text in `STATE.md`; it directly contradicts `STATE.md:11-12` and `STATE.md:46-47` in the same file. Non-blocker for the contract (state.json is the machine-readable source of truth per GPD infra), but a real coherence defect. |
| `.gpd/REQUIREMENTS.md` `CALC-03` flip cites same target as `SOURCE_BOUNDARY.md` | **PASS** | `REQUIREMENTS.md:29-33` — CALC-03 now `[x]` and cites `scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/` with pointers to `SOURCE_BOUNDARY.md` and `MIGRATION_PLAN.md`. Identical target string. |
| `.gpd/ROADMAP.md` Phase 01 row shows right completion status | **PASS** | ROADMAP: Phase 01 now `[x]`, Plan 01-01 `[x] … (completed 2026-04-24)`, Progress table shows "1/1 Complete 2026-04-24". Plan 02-01 description updated to the concrete search-surface slice. Phase 02 total plans count corrected from `TBD` to `1`. |

## Authority-Doc Invariance

**PASS.** `git diff --stat origin/main..HEAD authority/ src/ pyproject.toml` returns empty. The three commits touch only docs and `.gpd/` control plane. AGENTS.md's exact-source-only rule for `authority/` is respected.

## Smoke-Path Executability

| Check | Result | Evidence |
| --- | --- | --- |
| `src/` unchanged in diff | **PASS** | `git diff --stat origin/main..HEAD src/` empty. |
| `pyproject.toml` unchanged | **PASS** | `git diff --stat origin/main..HEAD pyproject.toml` empty. |
| `python -m compileall src` still passes | **PASS** | Ran `python3 -m compileall src`: `Compiling 'src/gnosis_indus/__init__.py'...` with no errors. |
| "Current starter smoke path" block intact | **PASS** | `SMOKE_TESTS.md:3-14` is byte-identical to pre-diff version. Only the new "Phase 02 target smoke expectation" section (lines 28-55) was appended. |

## Numerical / Claim Sanity

| Claim | Repo location | Authority source | Match |
| --- | --- | --- | --- |
| Max query latency < 100 ms | `SMOKE_TESTS.md:45`, `SOURCE_BOUNDARY.md:45`, `DATA_POLICY.md:38` | `authority/review_pack/search_demo_summary.md:9` — "Max query latency \| 0.0451 ms \| < 100 ms \| Yes" | **PASS** — threshold cited verbatim; actual observed value 0.0451 ms is well under. |
| Catalogue-level symbol compression 5.89x | `SOURCE_BOUNDARY.md:45`, `DATA_POLICY.md:38` | `authority/review_pack/search_demo_summary.md:10,18,154` — "Symbol compression \| 5.89x \| >= 5x", "Symbol compression ratio (catalogue): 5.89x", "compress the Indus sign inventory by **5.9x**" | **PASS** — both the gate `>= 5x` and the observed `5.89x` are grounded. `SMOKE_TESTS.md:46` uses `>= 5.0` as the assertion threshold, consistent with the gate. |
| API names `sign_lookup`, `sequence_search`, `subsequence_search` | `SMOKE_TESTS.md:42-44`, `SOURCE_BOUNDARY.md:36` | `authority/review_pack/search_demo_summary.md` queries 1-10 (lines 43-141) — exactly these three function names | **PASS** — not invented; lifted from the Track C demo. |
| `claim-search-demo` = ADMITTED, `claim-indus-catalogue` = CONDITIONAL | `SOURCE_BOUNDARY.md:48-51` | `authority/review_pack/phase4_governing_verdict.md:120-121` — "claim-indus-catalogue \| **CONDITIONAL**", "claim-search-demo \| **ADMITTED**" | **PASS** — diff-added reasoning correctly cites both verdicts. |

## Confidence Assessment

**Confidence: 9/10.**

Rationale:
- All three acceptance tests verified on artefact evidence, not on summary claims.
- Falsification battery verified by direct textual comparison of the diff and the authority sources.
- Numerical gates (< 100 ms, 5.89x) verified against the actual `search_demo_summary.md` bytes.
- Authority/, src/, pyproject.toml untouched (empty `git diff --stat`).
- `python3 -m compileall src` passes.
- One coherence defect (`STATE.md:95` stale "first extraction slice is not yet chosen" uncertainty) is the only subtractive factor. It is a stale-text issue inside one control-plane doc; `state.json` is correct; the surrounding `STATE.md` prose is correct. Not a contract break, but a real disagreement that would fail a pedantic consistency-checker.

## Notes / Recommended Follow-ups

1. **`.gpd/STATE.md:95`** — remove or rewrite the stale `Propagated Uncertainties` bullet "first extraction slice is not yet chosen". Replace with the state.json text ("Runtime dependency list is not frozen until the first slice lands in Phase 02.") or simply delete. Low-cost, high-value for future coherence checks.
2. **VALD-04** remains `[ ]` in `REQUIREMENTS.md` — correctly, because it requires a stronger smoke path actually running, which is Phase 02 work. Not a Phase 01 gap.
