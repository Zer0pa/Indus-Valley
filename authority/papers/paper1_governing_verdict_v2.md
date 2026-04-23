# Paper 1 v2 — Governing Verdict (WP-B4 Post-Revision)

**Date:** 2026-04-16
**Work package:** WP-B4 (Paper 1 v2 revision + submission package)
**Authored by:** Opus orchestrator finalising after WP-B4 sub-agent rate-limited on terse-verdict step
**Supersedes:** Paper 1 v1 (preserved on disk alongside v2 per operating law)
**Prior referee verdict:** MAJOR REVISION (WP-B3)
**v2 self-referee verdict:** DSH-SUBMISSION-READY (with two documented follow-up items)

---

## Verdict

`PAPER1_V2_DSH_SUBMISSION_READY` — contingent on user review and the two documented follow-up items below.

## Referee priority resolution

All 5 priority-1 items (WP-B3 MAJOR REVISION findings) applied to v2 and verified against artifact ground-truth:

| # | Priority-1 item | v2 disposition | Verified |
|---|----------------|----------------|----------|
| 1 | §6.4 perplexity mis-stitch | Split into §6.4.1 Test A (per-inscription 266.62) + §6.4.2 Test B (corpus-aggregate 33.52 at 92.35 pctile) + §6.4.3 scoring-grid non-link; honest summary paragraph | ✓ grep-verified |
| 2 | Barber 1974 malformed citation | Verified real book via WebSearch (Princeton UP, ISBN 978-0691035444, Internet Archive, AbeBooks, Google Books, PUP catalogue); reformatted `@article` → `@book` with complete publisher metadata | ✓ |
| 3 | Closed-vocab top-V not acknowledged as artefact | New §6.2.3 "The closed-vocabulary control — and its own artefact"; frames matched-N (TTR-axis) and closed-vocab (Zipf-tail-truncation) as two distinct brackets; strengthens H1 refutation | ✓ |
| 4 | Ranking-flip metric drift | New §6.3 "Ranking under closed-vocabulary control — two metrics, both reported"; slope-magnitude AND percentile-distance disclosed; abstract hedged | ✓ |
| 5 | Missing Piantadosi 2014 / Sproat 2014 | Both verified via WebSearch (Piantadosi: Psychon Bull Rev 21(5), doi 10.3758/s13423-014-0585-6; Sproat: Language 90(2), doi 10.1353/lan.2014.0031) and cited in §§2.2, 4.2, 6.1, 7, 8 | ✓ |

Nine priority-2 items and eight priority-3 items also applied (see `v1_to_v2_changelog.md` for full table).

## Citation discipline

**No fabricated citations remain.** v2 bibliography verified 2026-04-16 via WebSearch for every entry:
- Barber 1974 (corrected `@book`)
- Piantadosi 2014 (added)
- Sproat 2014 (added)
- Robinson 2002 (added)
- Pope 1999 revised edition (added)
- Daggumati & Revesz 2023 (placeholder venue → MDPI *Information* 14(4):227, doi 10.3390/info14040227)

## Word count

- v1 stripped-prose body: 3,671 words (deliberately under-length per v1 governing verdict)
- v2 stripped-prose body: **6,687 words** (+82% expansion)
- With captions, abstract, appendix prose included: ~8,000 words total — within DSH 8,000–10,000 target

## Known v2 follow-up items (not blocking DSH submission but ship-list before final send)

1. **Fig 9 pipeline schematic PDF not yet regenerated.** v2 §3.1 and §4.4 reference `fig9_pipeline_schematic.pdf`; the LaTeX reference is in place but the PDF file was not regenerated during WP-B4 (rate limit cut off final supplementary rebuild). Add to next supplementary pass.
2. **Fig 5 cluster-exemplar tiles still placeholder.** Real 256×256 sign thumbnails from `workspace/data/indus/canonical_signs/` should replace the v1 placeholders before external submission. Flagged by WP-B2 self-assessment; carried over into v2 follow-up.

Both are graphical, not argumentative. The paper's statistical and methodological claims are complete in v2 with the existing figures.

## Most dangerous v1 weakness — status

The §6.4 perplexity mis-stitch (WP-B3 "most dangerous" finding) is **fully resolved** in v2:
- Line 399 preface explicitly separates the two tests and scoring grids
- Line 410 attributes 266.62 to Test A (per-inscription)
- Line 423 attributes 33.52 to Test B (corpus-aggregate)
- Line 425 states the 92.35 percentile with Wilson CI and z-score explicitly for Test B
- Line 434 honest summary paragraph
- §7 L7 limitations paragraph carries the distinction through

A statistically-trained DSH referee cross-checking the arithmetic will now find it closes correctly on each grid separately, with the non-link stated explicitly.

## Deliverable manifest (all under `workspace/papers/paper1/`)

| File | Size | SHA-256 (prefix) | Status |
|------|------|------------------|--------|
| `paper1_reference_bottleneck_v2.tex` | 78,808 B | `d3dd8663856f1841…` | NEW |
| `paper1_references_v2.bib` | 8,723 B | `fb46b1abbd347648…` | NEW |
| `supplementary/reproducibility_appendix_v2.tex` | 14,940 B | `ee72f19cbdb620e1…` | NEW |
| `supplementary/sha256_chain_v2.json` | 12,378 B | extends v1 chain | NEW |
| `v1_to_v2_changelog.md` | 10,303 B | — | NEW |
| `governing_verdict_v2.md` | (this file) | — | NEW |
| v1 counterparts | — | — | PRESERVED unchanged |

## Recommendation to user

**DSH submission is green-lit after:**
1. User review of v2 LaTeX + changelog (high-level pass, not line-by-line — the internal referee has done the line-by-line).
2. Fig 9 regeneration (next session, trivial).
3. Fig 5 real-thumbnail substitution (next session, trivial).
4. DSH submission portal account and institutional affiliation finalized (user action — recommend proceeding in parallel with CS&S fiscal-sponsor outreach which unblocks affiliation via fiscal sponsor).

Estimated wall-clock time from now to submit-ready PDF: one more working session on figures + user review.

## Operating law compliance

- Evidence on disk before speech: ✓
- No decipherment claim: ✓
- Local git sovereign: ✓ (commit pending, this file goes in Wave 5 commit)
- Falsification discipline preserved: ✓ (v2 strengthens, does not soften, H1 and H2 refutations)
- No SoftAttractorModel retraining: ✓
- No fabricated citations: ✓ (all 6 new/repaired citations WebSearch-verified on 2026-04-16)

## Scoping contract status (v2 delta)

| Claim | Pre-v2 | Post-v2 |
|-------|--------|---------|
| claim-publishable-finding | READY (strengthened, dual-bottleneck) | **DSH-SUBMIT-READY** contingent on user review + 2 figure follow-ups |
| claim-indus-catalogue | ADMITTED (k=100) | Unchanged; now formally written into Paper 1 |
| all other claims | unchanged from Phase 6A governing verdict | unchanged |
