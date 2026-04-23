# Source Boundary

## Repo identity

`gnosis-indus` owns the Indus anchor application and evidence surface.

## Included now

| Surface | Status | Why it belongs here |
| --- | --- | --- |
| Root docs and boundary docs | included | front-door truth for the repo |
| `authority/` copied verdict and review docs | included | self-contained evidence posture |
| `.gpd/` control plane | included | autonomous execution surface |
| `src/gnosis_indus/` starter namespace | included | repo-ready package root |
| `docs/family/INDUS_EXPORT_CONTRACT.md` | included | downstream contract and search boundary |

## Future extraction targets

### First extraction slice (Phase 02 target)

| Current source family | Future landing zone | Status |
| --- | --- | --- |
| `scripts/indus/phase4_search_demo.py` | `src/gnosis_indus/search_surface/` | **FIRST SLICE — Phase 02** |

**First-slice justification.** The search-without-decode demo is the lowest-risk
extraction path against the three admission criteria:

- **(a) Rights-gate risk — LOW.** The demo operates on already-derived
  cluster IDs and sign-ID integers (see
  `authority/review_pack/search_demo_summary.md`). It does not redistribute
  sign images, does not re-consume ICIT/Wells/Fuls imagery, and does not
  mirror any `BLOCKED_RIGHTS` or large language corpora. No new rights
  surface is opened.
- **(b) Monorepo-local helper dependency — LOW.** The query engine
  (`sign_lookup`, `sequence_search`, `subsequence_search`) needs only the
  catalogue JSON (`indus_catalogue.json`) plus a query list. It does not
  need the A2 route-selection battery, the A3 stability battery, or the
  feature-extraction stack. Those helpers stay in the monorepo until a
  later wave.
- **(c) Stronger-smoke-path story — HIGH.** The demo has a clean declared
  public API surface that a smoke test can instantiate and assert against:
  load the catalogue, run one `sequence_search`, assert that max latency
  stays below 100 ms and catalogue-level compression remains at 5.89x per
  the Phase 4 Track C gate thresholds. This is materially stronger than
  the current `python -c "import gnosis_indus"` starter smoke path and
  matches the PRD framing of search as the in-repo application surface.

Because the Phase 4 admission verdict treats `claim-search-demo` as
`ADMITTED` while keeping `claim-indus-catalogue` as `CONDITIONAL`, starting
with the search surface avoids pulling the k=70 stability caveat into
runtime before the caveat itself has been given a proper runtime home.

### Deferred second and third wave (still Phase 02 scope)

| Current source family | Future landing zone | Wave | Notes |
| --- | --- | --- | --- |
| `scripts/indus/phase4_*.py` (route-selection, stability, catalogue, summary) | `src/gnosis_indus/catalogue/` | second wave | must carry the Phase 4 `PHASE4_CATALOGUE_CONDITIONAL` k=70 stability caveat into runtime text; depends on the feature-extraction and stability batteries still living in the monorepo |
| `scripts/indus/phase5_*.py` (falsification summaries, comparators) | `src/gnosis_indus/falsification/` | third wave | must preserve `PHASE5_INDISTINGUISHABLE - LINGUISTIC_CONFIRMED`; depends on large language corpora that stay `FETCH_EXTERNAL` |
| selected `workspace/artifacts/indus/phase4/` (catalogue JSON, cluster summary) | `artifacts/phase4/` | co-landed with the first slice | needed so the Phase 02 smoke path has a real catalogue to query |
| selected `workspace/artifacts/indus/phase5/` | `artifacts/phase5/` | co-landed with the third wave | small derived artifacts only; source corpora stay fetch-only |

No `scripts/indus/phase4_*.py` or `scripts/indus/phase5_*.py` family is in a
grey zone any longer. Each is either the named first slice, an explicitly
named second/third wave, or out of scope below.

## Explicitly out of scope

- `scripts/cuneiform/` and cuneiform artifacts
- a separate `gnosis-script-search` repo boundary
- generic shared-kernel ownership that belongs to another workstream
- outreach and prize materials unless specifically admitted later

## Shared dependency note

This repo may depend on work that later moves into `gnosis-glyph-engine` or
`gnosis-morph-bench`, but it should express those as dependencies or copied
bridges, not by erasing ownership boundaries.
