# WP-B3 Referee Governing Verdict — Paper 1 v1

**Date:** 2026-04-16
**Work package:** WP-B3 (internal referee review)
**Reviewer:** internal sub-agent, simulating senior DSH referee
**Target:** *Digital Scholarship in the Humanities* (OUP)
**Supersedes:** WP-B2 author self-assessment (`governing_verdict.md`)

---

## Verdict: `MAJOR_REVISION_REQUIRED — NOT_READY_FOR_DSH_SUBMISSION`

The paper's intellectual core (dual-instance reference-bottleneck framing, ADMITTED k=100 catalogue, airtight H1 refutation, 10K lipi permutation, reproducibility substrate) is sound. The execution has five load-bearing flaws that a real DSH referee will find on first read. All are fixable without new experiments; all must be fixed before external submission.

---

## Priority-1 changes (must fix before v2 ships)

1. **§6.4 mis-stitched perplexity numbers.** Paragraph conflates Phase 5 perplexity scoring (266.62 per-inscription mean) with WP-A4 10K-permutation control (lipi_perplexity 33.52, 92.35th percentile). Two different tests, two different scoring grids, reported as one. Split into two sub-paragraphs, each with its own scoring grid disclosed.

2. **Barber 1974 citation is malformed.** Bibtex entry lists author "E. J. W. Barber" with journal = "Princeton University Press" (a publisher, not a journal) and a note-in-title parenthetical. The minimum-corpus-for-decipherment concept is typically attributed to Maurice Pope (1975) *The Story of Decipherment* or discussed in Robinson (2002) *Lost Languages*. Currently reads as a fabricated citation. Author to verify and replace with a correctly-cited source.

3. **Closed-vocabulary top-181 is an artifact too.** §6.2 correctly identifies matched-N bootstrap as a TTR artifact but fails to acknowledge that closed-vocab top-181 is a Zipf-tail-truncation artifact in its own right. A sophisticated referee will raise this. Add one paragraph framing the two controls as brackets, not as truth.

4. **Missing Piantadosi 2014 and Sproat 2014 citations.** Piantadosi 2014 is the standard Zipf-slope-regression methodology reference; Sproat 2014 is the peer-reviewed continuation of the Rao/FSW debate. Absence signals inadequate lit coverage to a script-studies referee.

5. **Ranking-flip metric drift in §6.3 and abstract.** Paper computes slope-magnitude distance (Prakrit closer than Sanskrit; Tamil closest) but the underlying WP-A3b verdict reports percentile-distance (Sanskrit closest). Disclose the metric and justify, or this looks like cherry-picking.

---

## Secondary issues (priority 2)

- NMI normalizer unstated; 100-permutation null is undersampled.
- Zipf-regression form not explicitly specified in Methods.
- "0th/100th/0th percentile" phrasing needs explicit rejection-level framing (Bonferroni-corrected p-value).
- Body is 4,700 words against DSH's 8,000–10,000 target — under-length, not concise. Execute v2 expansion plan.
- DaggumatiRevesz2023 bib entry has a note-to-self in the journal field.
- Search-demo data (§6.5, Fig 8) not in sha256_chain.json — breaks the reproducibility invariant.
- "Linguistic band" bands attributed to Rao 2009 / Yadav 2010 without specific table citations.

---

## Single most dangerous weakness a real reviewer will exploit

**The §6.4 perplexity-number mis-stitching.** Any DSH referee with statistical training will cross-check 266.62 against the WP-A4 null distribution (mean 168.80, p95 499.52) and find that 266.62 would land at roughly the ~65th percentile of that null — not the 92.35th reported. The arithmetic doesn't close because the two perplexity numbers come from different scoring grids, a fact the paper does not disclose. Left un-fixed, this reads as either (a) arithmetic error or (b) fudging; in either case the paper's credibility on the statistical-instance claim collapses. This is an afternoon's work to fix cleanly, but it is a dealbreaker if not fixed.

**Runner-up weakness:** the Barber 1974 citation. A script-studies referee who reaches for the bibliography will catch this in 30 seconds. Reads as fabrication.

---

## Readiness

- **Structural overhaul required?** NO. The section structure, the claim spine, and the evidence base are all sound.
- **Ready for v2 revision?** YES. Revision scope is well-defined: correct one citation, split one paragraph, add one paragraph, disclose one metric choice, add two missing references, expand body prose to ≈8,000 words.
- **Estimated v2 effort:** 1–2 working days of writing + one internal re-review pass.
- **Expected v2 disposition at DSH:** MINOR REVISION or ACCEPT with polish, provided priority-1 fixes land clean.

---

## Deliverable artifacts

- `paper1_referee_report_v1.md` — full six-pass referee report (this review's primary evidence artifact)
- `governing_verdict_referee.md` — this file
- Both are writeable referee-side artifacts; the paper v1 files are unmodified per operating law.
