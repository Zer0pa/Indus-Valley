# Paper 2 (Reframed) — WP-C1 Governing Verdict

**Date:** 2026-04-16
**Branch:** claude/serene-feistel
**Work package:** WP-C1 (Paper 2 reframed outline)
**Phase context:** Post-Phase 6A; Phase 5 "Sanskrit closest" claim retired; H1 AIRTIGHT_REFUTED; H2 REJECTED at α=0.05.
**Authored by:** Opus paper-writer (sub-agent)

---

## Verdict: `WP_C1_CLEARED — PAPER2_OUTLINE_READY_HELD`

Paper 2 outline, figure plan, and target-venue analysis are ready. Paper 2 **should be held** until Paper 1 is submitted. Draft v1 is not authorized in this work package.

---

## Deliverables produced

| File | Status | Purpose |
|------|--------|---------|
| `outline.md` | Complete | 11-section outline, ~8,280 word target, honest framing compliant with all operating laws |
| `figure_plan.md` | Complete | 7 figures + 3 inline tables with source-data links |
| `target_journal_analysis.md` | Complete | PLoS ONE primary, *Computational Linguistics* secondary, JQL tertiary |
| `governing_verdict.md` | This file | Terse verdict + forward guidance |

All files under `<MONOREPO_ROOT>/workspace/papers/paper2/`.

---

## Working title

*Linguistic confirmation and substrate indistinguishability in the Indus corpus: Zipf convergence at natural scale is not a substrate signal.*

---

## Summary of contributions novel to Paper 2

- Dual-control falsification of "Sanskrit closest" (WP-A3 + WP-A3b).
- Prakrit-closer-than-Sanskrit ranking-flip observation.
- 10K-permutation lipi rejection at α=0.05 (92.35th pctile, Wilson 95% CI [91.81, 92.85]).
- Cleanly separated intrinsic linguistic signatures.
- Strengthened Barber 1974 threshold argument via bootstrap evidence.

None of the above duplicates Paper 1 (which develops the morphological reference-bottleneck at §§3–5 and reports only a 100-perm lipi test in §6.2).

---

## Recommended venue

**PLoS ONE** primary. Rationale: editorial criterion is technical soundness, not novelty — a direct match for a paper whose central contribution is honest null-result falsification. Fully open-access, broad interdisciplinary reviewer pool, faster review cycle, mandatory data-availability enforcement aligns with project operating laws.

*Computational Linguistics* (MIT) is strong secondary if PLoS ONE rejects.

---

## Timing recommendation — parallel vs held

**HELD until Paper 1 is submitted.**

Reasoning:
1. Paper 2 §1.3, §8.1, and references in §2 cite Paper 1 for the morphological instance of the reference-bottleneck pattern. The citation is load-bearing: Paper 2 presents the **statistical** instance; Paper 1 presents the **morphological** instance; the dual-bottleneck framing requires Paper 1 to exist as a submittable reference.
2. Paper 2 draft v1 should also benefit from whatever reviewer feedback Paper 1 attracts — particularly on the operating-law compliance and the FSW sub-argument treatment, which Paper 2 inherits from Paper 1's framing.
3. Parallel drafting risks scope-creep — Paper 2 is tempted to over-explain the morphological instance in §8.1 if Paper 1 is not yet cited-able.
4. Resource constraint: the paper-writer / orchestrator bandwidth is finite; Paper 1 is at §-outline-accepted stage and needs draft v1 (WP-B2) completion before the next round.

**Operational sequence:**
- Finish Paper 1 draft v1 (WP-B2) → Paper 1 internal review → Paper 1 submission to DSH → Paper 2 draft v1 begins with Paper 1 citable (preprint or accepted-MS hash).
- Estimated Paper 2 draft v1 start: T+2-3 months from now, assuming Paper 1 is submitted at T+1-2 months.

If pressed to parallel-draft, the minimum acceptable mitigation is:
- Paper 2 draft v1 cites Paper 1 as "in preparation (same authors)" with preprint hash.
- Paper 2 submission is held until Paper 1 is on arXiv at minimum.

**This work package does not authorize Paper 2 draft v1.** A subsequent work package (WP-C2) would do so, after Paper 1 submission.

---

## Operating-law compliance

- [x] No decipherment claim in outline — verified §11, §8.2, §1.3.
- [x] No substrate identification as proven — verified §4.3, §11.
- [x] Honest framing — outline is about indistinguishability AND ranking flip, not about identifying a substrate.
- [x] Evidence on disk mandatory — every claim anchored to a Phase 5 or Phase 6A artifact.
- [x] LaTeX/outline path: `<MONOREPO_ROOT>/workspace/papers/paper2/`.
- [x] No duplication of Paper 1 §§3–5 — Paper 2 cites Paper 1, does not rehash morphological bottleneck.
- [x] No interim reporting — WP-C1 is a single-deliverable work package; no mid-work status emitted.
- [x] No narrative wins — outline explicitly frames Paper 2 as retiring the project's own earlier headline claim.

---

## Risks flagged for WP-C2 (draft v1)

- **R1:** Paper 1 reviewer feedback could modify the morphological-instance narrative in ways that force Paper 2 §8.1 to be rewritten. Mitigation: hold Paper 2 until Paper 1 is stable.
- **R2:** Additional substrate candidates (Elamite, Proto-Dravidian) could be tested before Paper 2 submission, which would strengthen §7.2 but also risk scope expansion. Mitigation: scope freeze at WP-C2 start.
- **R3:** Closed-vocab V-sensitivity (V ∈ {150, 200, 250}) is not reported in Paper 2 outline. A reviewer could reasonably request it. Mitigation: optional pre-submission WP-A3c to report V-sensitivity as robustness check.
- **R4:** Tamil Wikipedia corpus choice (WP-A8) leaves residual "is −0.720 stable" uncertainty. A reviewer could request running-prose news-corpus replication. Mitigation: flagged as §10 L3 / §6.1 footnote; honest acknowledgment in limitations.
- **R5:** The 10K-permutation lipi test uses a character-bigram model only. A reviewer could request a neural LM replication. Mitigation: flagged as §10 L5.
- **R6:** FSW 2004 sub-arguments (i) and (iii) are explicitly not engaged. A reviewer could read this as weakness. Mitigation: transparent statement in §10 L7.

---

## Artifact SHA-256 manifest (this work package)

Manifest will be added to `workspace/papers/paper2/MANIFEST.sha256` at WP-C2 start. Current state: four markdown files produced, no binary artifacts.

---

## Sign-off

WP-C1 cleared. Paper 2 outline ready; held pending Paper 1 submission. No Paper 2 draft authorized until Paper 1 is on arXiv or accepted.

*End of verdict.*
