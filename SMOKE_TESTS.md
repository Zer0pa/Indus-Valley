# Smoke Tests

## Current starter smoke path

The repo does not yet claim a full extracted runtime. The current smoke path is
therefore limited to starter integrity:

```bash
python -m compileall src
python -c "import gnosis_indus; print(gnosis_indus.__version__)"
test -f AUTHORITY_SNAPSHOT.md
test -f PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md
test -f docs/family/INDUS_EXPORT_CONTRACT.md
```

## What this establishes

- the starter package imports
- the authority and contract surfaces are present
- the staged repo can be handed to another agent without missing core docs

## What this does not establish

- Phase 4 or Phase 5 reruns
- clean-machine replay of the full evidence stack
- public-data rights clearance

## Phase 02 target smoke expectation

Once the first extraction slice (search-without-decode, chosen in
`SOURCE_BOUNDARY.md` and sequenced in `MIGRATION_PLAN.md`) lands under
`src/gnosis_indus/search_surface/`, the smoke path must be materially
stronger than starter import. The expected shape:

```bash
python -m compileall src
python -c "
from gnosis_indus.search_surface import SearchEngine
engine = SearchEngine.from_catalogue('artifacts/phase4/indus_catalogue.json')
# declared public API surface must compile and be callable
assert hasattr(engine, 'sign_lookup')
assert hasattr(engine, 'sequence_search')
assert hasattr(engine, 'subsequence_search')
result = engine.sequence_search([65, 38])
assert result.max_latency_ms < 100.0, 'Phase 4 Track C latency gate'
assert engine.compression_ratio() >= 5.0, 'Phase 4 Track C compression gate'
print('search_surface smoke: PASS')
"
```

This expectation is aspirational until Phase 02 lands the slice, but it is
concrete enough that a failing test can be written against it the moment
the runtime module appears. The latency and compression thresholds are
inherited directly from the Phase 4 Track C gate in
`authority/review_pack/search_demo_summary.md`; they must not drift.
