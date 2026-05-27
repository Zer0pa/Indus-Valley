# Indus-Valley

> Product-page mirror for `/gnosis/Gnosis-Indus-Valley/`.
> Live public repo: [Zer0pa/Indus-Valley](https://github.com/Zer0pa/Indus-Valley).
> GitHub Markdown cannot reproduce the website typography, CSS, JavaScript, scroll behavior, or live bento layout; this README translates the product page into GitHub-safe Markdown evidence blocks.

## 0. Install / Developer Commands

The product page is the positioning authority. This section is the only retained developer-surface material from the previous root README.

```bash
**Headline metric:** `pytest -q → 14 passed` (≈0.03 s local, ≈0.3 s
reproduce the test surface via `pip install -e ".[test]" && pytest`.
└── workflows/ci.yml                   # boring CI: install + pytest
git clone https://github.com/Zer0pa/Indus-Valley.git gnosis-indus
pip install -e ".[test,numerics]"
pytest -q
Expected: `14 passed`. The pytest suite reproduces the authority-doc
```

## Product Page Mirror

**Product-page title:** Gnosis-Indus-Valley · Search Indus signs by shape · Zer0pa

**Product-page description:** Gnosis-Indus-Valley · non-decipherment search anchor · conditional 412-sign / 70-cluster catalogue · 0.0451 ms max query latency on a 100 ms authority gate · NMI 0.5793 vs ICIT Sets · Phase 5 substrate unresolved · PyPI gnosis-indus v0.1.0 · runtime demo fixture; no glyph reading is claimed

### Hero Translation

> 00 · GNOSIS-INDUS-VALLEY · NON-DECIPHERMENT SEARCHRESEARCH-READY · v0.1.0 Indus Script Search and Computational Exploration Gnosis Indus-Valley · PyPI gnosis-indus v0.1.0 · 412 signs · 70 clusters · github.com/Zer0pa/Indus-Valley The Indus script has gone unread for a century. Thousands of marks on seals, tablets, and tools — catalogued, contested, photographed — and no one knows what they say. What was missing was not more scholarship. It was a way to search the corpus by the shape of the marks, without claiming what they mean. gnosis-indus ships a clean-room 412-sign / 70-cluster catalogue and answers shape queries in 0.0451 ms. No glyph is read.

## Positioning

| Field | Value |
| --- | --- |
| Section | gnosis |
| Product route | /gnosis/Gnosis-Indus-Valley/ |
| Live public repository | https://github.com/Zer0pa/Indus-Valley |
| Repo identity used here | Indus-Valley |
| Website display identity | Indus-Valley |
| Verdict | STAGED |
| Posture | rights_gated_data_classes_image_blocked_text_fetch_external |
| Headline metric | pytest -q → 14 passed. Clean-room search-without-decode runtime reproduces 6 authority-doc query records on a small authority-anchored demo fixture; sequence_search median latency well under the 100ms gate. |
| Honest blocker | Image-bearing sign rights remain BLOCKED_RIGHTS per DATA_POLICY.md; the full k=70 catalogue (412 signs / 70 clusters / 179 inscriptions) stays FETCH_EXTERNAL. |
| Mechanics asset from product page |  |

## Key Metrics

| Metric | Value | Baseline |
| --- | --- | --- |
| Conditional catalogue | 412 signs / 70 clusters / 179 inscriptions | NMI 0.5793 against ICIT Sets; sigma 5.65 |
| Search compression | 5.89x catalogue compression | Track C search-without-decode |
| Query latency | 0.0451 ms max | 100 ms authority-doc gate |
| Pytest surface | 14 passed | clean Python 3.11 replay |

## Proof Anchors

| Path | State |
| --- | --- |
| Phase 4 conditional catalogue at k=70 with stability caveat | authority/review_pack/phase4_governing_verdict.md, authority/review_pack/indus_catalogue_summary.md |
| Phase 5 linguistic-structure-without-decipherment | authority/review_pack/phase5_governing_verdict.md |
| Paper 1 (DSH-ready) and Paper 2 (held until Paper 1 submission) verdicts | authority/papers/paper1_governing_verdict_v2.md, authority/papers/paper2_governing_verdict.md |
| Search-without-decode functional spec (API + latency/compression gates + 10 query ground-truth records) | authority/review_pack/search_demo_summary.md |
| Clean-room runtime reproducing the spec | src/gnosis_indus/search_surface/{__init__,catalogue,engine,_fixture}.py |
| Authority-anchored demo fixture | artifacts/phase4/indus_catalogue_demo_fixture.json (every row traced verbatim to a line in the authority doc; see artifacts/phase4/README.md) |

## What We Prove

- The lane is migrated out of the original monorepo as a standalone, truthful scaffold without losing the Phase 4 stability caveat or the Phase 5 non-decipherment posture.
- A clean-room search-without-decode runtime (`src/gnosis_indus/search_surface/`) anchored to `authority/review_pack/search_demo_summary.md` reproduces six authority-doc query records on a small authority-anchored demo fixture, with `sequence_search` median latency well under the authority-doc 100 ms gate.
- A clean-machine replay path exists: any Python 3.11 host can reproduce the test surface via `pip install -e ".[test]" && pytest`.
- Off-repo custody (private HF dataset + model repos) is provisioned for future heavy-artifact promotion under `DATA_POLICY.md` classification, with the register documented in `HF_CUSTODY_REGISTER.md`.

## What We Do Not Claim

- We do not claim decipherment of the Indus script.
- We do not claim proven substrate identification.
- We do not claim all rights gates are cleared. Image rights for sign-bearing releases remain open; this is an open lab, not a finished product.
- We do not claim unrestricted public redistribution rights for any image-bearing or rights-gated corpus referenced in the original monorepo work; sign images stay `BLOCKED_RIGHTS` in `DATA_POLICY.md`.
- We do not claim the bundled fixture is the real full catalogue. The full k=70 catalogue (412 signs, 70 clusters, 179 inscriptions) stays `FETCH_EXTERNAL` per `DATA_POLICY.md`.

## Blockers / Failures

> Image-bearing sign rights remain BLOCKED_RIGHTS per DATA_POLICY.md; the full k=70 catalogue (412 signs / 70 clusters / 179 inscriptions) stays FETCH_EXTERNAL.

## Verification Surface

| Code | Check | Verdict |
| --- | --- | --- |
| V_01 | `pytest -q` on Python 3.11: 14 passed | PASS |
| V_02 | `python -m compileall src` | PASS |
| V_03 | Per-phase verification reports all PASS | PASS |
| V_04 | Operational endpoint leak scan: 0 matches | PASS |
| V_05 | Image rights and full catalogue redistribution | PENDING |

## License

| Field | Value |
| --- | --- |
| License | Apache-2.0+CC-BY-4.0 |
| Authority source | README.md |

## Upcoming Workstreams

| Category | Summary |
| --- | --- |
| Active Engineering | Continue current authority-packet refinement on Gnosis-Indus-Valley; surface new receipts as they land. |
| Operations / External Dependency | Maintain CI gates and license-resolver synchronization with Zer0pa/ZPE-License-Commercial. |

## Related Repos

No related repos are declared on the product page frontmatter.

<details>
<summary>Full Visible Product-Page Bento Translation</summary>

This section preserves the product page cells as Markdown text blocks. It intentionally omits shared site navigation, footer chrome, CSS, and scripts.

### Bento Cell 1

> 00 · GNOSIS-INDUS-VALLEY · NON-DECIPHERMENT SEARCHRESEARCH-READY · v0.1.0 Indus Script Search and Computational Exploration Gnosis Indus-Valley · PyPI gnosis-indus v0.1.0 · 412 signs · 70 clusters · github.com/Zer0pa/Indus-Valley The Indus script has gone unread for a century. Thousands of marks on seals, tablets, and tools — catalogued, contested, photographed — and no one knows what they say. What was missing was not more scholarship. It was a way to search the corpus by the shape of the marks, without claiming what they mean. gnosis-indus ships a clean-room 412-sign / 70-cluster catalogue and answers shape queries in 0.0451 ms. No glyph is read.

### Bento Cell 2

> 01 · THE GAPA CENTURY WITHOUT SHAPE SEARCH The Indus script has gone undecoded for a century; its marks were never searchable by shape.

### Bento Cell 3

> 02 · MARKETSADJACENT FORECASTS Cultural heritage digitization'30 · $8.1B Research data management'30 · $6.7B Scholarly infrastructure'30 · $5.3B Digital humanities'30 · $3.2B AI for archaeology'30 · $1.4B source: heritage and research-infrastructure forecasts. Best-fit users: epigraphy labs, museum archives, and digital-humanities groups. No traction or TAM claim.

### Bento Cell 4

> 03 · VALUE $8.1B Heritage digitization is funded. Tools that index this script by shape, without claiming to read it, remain almost absent.

### Bento Cell 5

> 04 · INSIGHT The mark has a shape. The shape can be searched.

### Bento Cell 6

> 05.1 · CURRENT TECHCATALOGUED, NOT SEARCHABLE BY FORM Indus scholarship lives in sign catalogues, visual classifications, and concordances. They let scholars compare marks one at a time, but no tool let them query the whole corpus by the shape of a single sign.

### Bento Cell 7

> 05.2 · OUR TECHSEARCH BY SHAPE gnosis-indus is a clean-room runtime: no neural model, no learned embedding, no substrate hypothesis. It bundles a conditional 412-sign / 70-cluster catalogue and answers shape queries in 0.0451 ms. The full 179-inscription corpus stays fetch-external under data policy. No glyph is read; only the shape is found.

### Bento Cell 8

> 05.3 · BENCHMARKSSEARCH TARGET + NMI Query latency0.0451 ms target100 ms NMI0.5793vs ICIT sigma5.65 SearchPASS NMIPASS SubstrateOPEN Result: demo shape search 0.0451 ms vs 100 ms target · NMI 0.5793 vs ICIT Sets.

### Bento Cell 9

> 06 · MEASUREMENTSEARCH TARGET · NMI · STRUCTURE Shape search clears the latency target. Decipherment is not measured — deliberately.

### Bento Cell 10

> 06.1 · COMPARATIVE PERFORMANCE · DEMO FIXTURE Max query0.0451 ms target100 ms under~2,217× NMI0.5793 sigma 5.65 Demo shape search at 0.0451 ms against a 100 ms target — roughly 2,217× under. Catalogue NMI 0.5793 vs ICIT Sets at sigma 5.65. Phase 5 substrate question unresolved; no reading claimed.

### Bento Cell 11

> 07 · KEY METRICSMEASURED RESULTS

### Bento Cell 12

> 07.1 · MAX QUERY LATENCY 0.0451ms Demo shape search · vs 100 ms target

### Bento Cell 13

> 07.2 · CATALOGUE NMI 0.5793 vs ICIT Sets · sigma 5.65

### Bento Cell 14

> 07.3 · PHASE 5 VERDICT STRUCT Linguistic structure confirmed · substrate unresolved

### Bento Cell 15

> 07.4 · PYPI RELEASE 0.1.0 PyPI gnosis-indus · public, reproducible

### Bento Cell 16

> 07.5 · CATALOGUE SCOPE 412signs 70 clusters · 179 inscriptions; full corpus fetched separately

### Bento Cell 17

> 08 · DETERMINISMSEARCH THAT REPLAYS Same query. Same fixture. Same matches — across replay clones.

### Bento Cell 18

> 08.1 · WHAT REPLAYS EXACTLYDEMO SEARCH SURFACE The runtime is clean-room — no neural model, no learned embeddings, no substrate guess. The same shape query against the bundled fixture returns the same matches across replay clones, every time, anchored to the same source records. The catalogue is conditional on Phase 4 stability, and the Phase 5 source-structure question is unresolved. Determinism covers shape search, not interpretation. No glyph is read, and the runtime is built so it cannot quietly start to.

### Bento Cell 19

> 08.2 · HONEST BLOCKER Honest Blocker · No reading claimed. The Phase 5 source-structure question is unresolved: we do not know what language, if any, the script encodes. Sign images stay policy-limited under DATA_POLICY.md. The bundled fixture is small; the full 412 / 70 / 179 catalogue is fetched separately.

### Bento Cell 20

> 09 SEARCH THAT REFUSES TO READ.

### Bento Cell 21

> 09.1 · THE AMBITION The ambition is computational restraint. gnosis-indus gives Indus scholarship a search surface, a cluster map, and a comparison primitive — and stops there. The refusal to read is not a hedge. It is the product. A catalogue researchers and museums can trust because it never overreaches into translation.

### Bento Cell 22

> 09.2 · WHAT WORKS NOW Shape search runs in 0.0451 ms, NMI confirms cluster structure, and the catalogue stays free of reading.

### Bento Cell 23

> 09.3 · WHAT'S STILL OPEN Substrate question unresolved, image policy limited, catalogue conditional, and full corpus stays fetch-external for now.

### Bento Cell 24

> 09.4 · SCHOLARSHIP · NEAR-TERM (12–24 MO) Indus scholars can search by shape A paleographer who notices a familiar mark on a newly photographed seal can find every visually related sign across the corpus in milliseconds. The conversation moves from "have I seen this before" to "here are the seventeen places it appears."

### Bento Cell 25

> 09.5 · DEBATE · NEAR-TERM (12–24 MO) Decipherment debate gets cleaner footing Comparisons among signs and clusters can stay anchored to structure, not to translation guesses. Researchers arguing competing theories share the same shape-grounded reference instead of talking past each other about disputed readings.

### Bento Cell 26

> 09.6 · MUSEUMS · MID-TERM (24–48 MO) Museum catalogues gain a structural index Curators can attach sign-family and cluster labels to seal records alongside images. Visitors and remote researchers query holdings by mark shape, and discovery surfaces stop depending on a translation no museum is willing to assert.

### Bento Cell 27

> 09.7 · METHOD · MID-TERM (24–48 MO) Shape search becomes shared infrastructure The same primitive — search by form, refuse to read — generalises to other undeciphered scripts: Linear A, Proto-Elamite, Rongorongo. Shape-first analysis becomes a shared method, and labs stop rebuilding the same catalogue plumbing from scratch.

### Bento Cell 28

> 09.8 · DISCIPLINE · PARADIGM (48 MO+) Honest non-claim becomes a scientific asset In contested heritage, a maintained refusal to overclaim outlasts every dramatic weak claim. The Indus catalogue stands as the durable object: a corpus researchers, curators, and the public can trust precisely because it never said what the signs mean.

</details>

---

Source mapping: product route `/gnosis/Gnosis-Indus-Valley/` -> live public repo `Zer0pa/Indus-Valley`. README generated from product-page authority plus retained install/dev commands only.
