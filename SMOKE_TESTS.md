# Smoke Tests

## Current smoke path

The repo has a first extracted runtime slice under
`src/gnosis_indus/search_surface/`. The current smoke path verifies both basic
package integrity and the Phase 02 search-without-decode replay surface:

```bash
python -m compileall src
pip install -e ".[test,numerics]"
python tools/indus_ops_gate.py --pretty
pytest -q
```

## What this establishes

- the package imports
- the Indus source-boundary and leakage gate passes
- the search runtime reproduces the authority-anchored demo fixture
- the authority and contract surfaces are present
- the staged repo can be handed to another agent without missing core docs

## What this does not establish

- Phase 4 or Phase 5 reruns
- clean-machine replay of the full evidence stack
- public-data rights clearance

## Phase 02 stronger smoke path (now real)

Phase 02 Plan 01 has landed the first clean runtime slice
(`src/gnosis_indus/search_surface/`) and the bundled authority-anchored
demo fixture at `artifacts/phase4/indus_catalogue_demo_fixture.json`.
The stronger smoke path is therefore concrete and runs locally:

```bash
python -m compileall src
pip install -e .[test]
pytest -q
```

`pytest -q` runs the suite under `tests/test_search_surface.py`, which
asserts the four acceptance tests declared in
`.gpd/phases/02-extraction-and-minimal-replay-surface/02-01-PLAN.md`:

- **test-api-shape** — `SearchEngine` exposes `sign_lookup`,
  `sequence_search`, and `subsequence_search` and returns the
  documented field set.
- **test-query-reproduction** — queries 1, 2, 3, 6, 9, 10 from
  `authority/review_pack/search_demo_summary.md` reproduce on the demo
  fixture, modulo the doc's `... and N more` truncation. Query 10 is
  the only one that is fully enumerated in the doc; for it the fixture
  match count must equal 5 exactly. Queries 6 and 9 assert subset
  containment of the explicitly enumerated matches.
- **test-latency-gate** — median `sequence_search([65, 38])` latency
  over 5 runs must stay under 100 ms (the Phase 4 Track C gate).
- **test-caveat-visibility** — package docstrings and the fixture
  README carry forward (a) the k=70 conditional caveat, (b) the
  non-decipherment posture, (c) the demo-fixture vs full-catalogue
  distinction.

The latency gate (< 100 ms) is inherited directly from
`authority/review_pack/search_demo_summary.md` and must not drift. The
authority-doc compression-ratio gate (>= 5x) cannot be asserted on the
demo fixture (which only carries the inscriptions the doc enumerates,
not the full 179-inscription corpus). It remains a property of the full
catalogue (FETCH_EXTERNAL per `DATA_POLICY.md`) and is verified there,
not on the bundled fixture; this distinction is a deliberate carry-over
of the demo-fixture vs full-catalogue boundary.

A standalone script smoke is also available without pytest:

```bash
python -c "
from gnosis_indus.search_surface import load_demo_fixture
e = load_demo_fixture()
r = e.sign_lookup(324)
assert r.cluster_id == 2 and r.cluster_size == 20
assert e.sequence_search([65, 38]).match_count >= 5
assert e.subsequence_search([11, 15, 40]).match_count == 5
print('search_surface smoke: PASS')
"
```
