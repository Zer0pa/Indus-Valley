# Auditor Playbook

**Last reviewed:** 2026-04-28 against `main` after the public-refresh and
Ops-Gates adoption wave.

## Goal

Verify what this staged repo currently proves from repo-local evidence without
importing extra monorepo-only assumptions.

## Fast Path

1. Read the authority block in `README.md`.
2. Read `AUTHORITY_SNAPSHOT.md`.
3. Read `authority/review_pack/phase4_governing_verdict.md`.
4. Read `authority/review_pack/phase5_governing_verdict.md`.
5. Read `authority/papers/paper1_governing_verdict_v2.md`.
6. Run the replay path:

   ```bash
   pip install -e ".[test,numerics]"
   python tools/indus_ops_gate.py --pretty
   pytest -q
   ```

7. Read `PUBLIC_AUDIT_LIMITS.md` before making broader claims.

## Claim Replay Map

| Claim | Evidence Path | Publicly Verifiable? | Caveat |
| --- | --- | --- | --- |
| This repo keeps the Indus lane in an anchor-application posture | `AUTHORITY_SNAPSHOT.md`, `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` | Yes | repo is still staged, not promoted |
| Phase 4 morphology remains caveated rather than narratively cleaned up | `authority/review_pack/phase4_governing_verdict.md`, `authority/review_pack/indus_catalogue_summary.md` | Yes | later paper work improves the catalogue but does not erase the caveat |
| Search stays inside `gnosis-indus` as an application surface | `authority/review_pack/search_demo_summary.md`, `SOURCE_BOUNDARY.md`, `docs/family/INDUS_EXPORT_CONTRACT.md` | Yes | no standalone search repo claim |
| Search-without-decode runtime exists and reproduces the admitted demo fixture | `src/gnosis_indus/search_surface/`, `tests/test_search_surface.py`, `artifacts/phase4/indus_catalogue_demo_fixture.json` | Yes | fixture is small; full catalogue stays `FETCH_EXTERNAL` |
| Source-boundary and leakage checks are load-bearing in CI | `.github/workflows/ci.yml`, `tools/indus_ops_gate.py` | Yes | Ops-Gates consumer smoke is pinned to a private internal module SHA; Indus repo-truth profile remains repo-local until Ops-Gates grows a config/profile mode |
| Code/docs are licensed without widening data rights | `LICENSE`, `NOTICE`, `docs/LEGAL_BOUNDARIES.md`, `DATA_POLICY.md` | Yes | Apache-2.0 and CC-BY-4.0 do not license raw corpora, sign images, model weights, or private custody surfaces |

## Minimum Replay Steps

1. Confirm the authority files exist at the named paths.
2. Compare the README language against `AUTHORITY_SNAPSHOT.md`.
3. Compare the morphology language against the copied Phase 4 verdict.
4. Compare the language/substrate language against the copied Phase 5 verdict.
5. Run `python tools/indus_ops_gate.py --pretty`; a failure means the repo is
   not ready for website sync.
6. Run `pytest -q` and confirm `14 passed`.
7. Confirm `DATA_POLICY.md` and `HF_CUSTODY_REGISTER.md` agree that heavy or
   rights-gated assets stay off GitHub and that raw sign images remain
   `BLOCKED_RIGHTS`.
8. Record any unsupported claim as `UNKNOWN` or dispute it directly.

## If You Find A Problem

- Use the evidence dispute template for claim/evidence disagreements.
- Use the bug template for reproducible package or docs defects.
- Use `PUBLIC_AUDIT_LIMITS.md` when the disagreement depends on unavailable
  data rights or heavy upstream assets.
