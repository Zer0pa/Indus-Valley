# TODO

## Next extraction work

### Done in Phase 02

- defined the in-repo search application package under
  `src/gnosis_indus/search_surface/` (clean-room reimplementation
  anchored to `authority/review_pack/search_demo_summary.md`)
- built a stronger smoke path than the starter import check
  (`tests/test_search_surface.py`, `pip install -e .[test] && pytest -q`,
  14 passed; independently confirmed on a clean RunPod pod from a
  fresh clone)

### Still open

- extract the first clean Phase 4 runtime slice into `src/gnosis_indus/catalogue/`
- extract the first clean Phase 5 runtime slice into `src/gnosis_indus/falsification/`
- add fetch manifests for image and corpus families that cannot ship now

## Documentation follow-ups

- replace owner-deferred license and contact values
- add release notes and changelog once the repo starts moving independently
- expand `authority/` only with exact-source replacements or new admitted verdicts

## Boundary checks

- verify no doc reintroduces a separate `gnosis-script-search` repo story
- verify no doc drops the Phase 4 stability caveat
- verify no doc slips into decipherment language
