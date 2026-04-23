# Auditor Playbook

## Goal

Verify what this staged repo currently proves without importing extra
monorepo-only assumptions.

## Fast Path

1. Read the authority block in `README.md`.
2. Read `AUTHORITY_SNAPSHOT.md`.
3. Read `authority/review_pack/phase4_governing_verdict.md`.
4. Read `authority/review_pack/phase5_governing_verdict.md`.
5. Read `authority/papers/paper1_governing_verdict_v2.md`.
6. Read `PUBLIC_AUDIT_LIMITS.md` before making broader claims.

## Claim Replay Map

| Claim | Evidence Path | Publicly Verifiable? | Caveat |
| --- | --- | --- | --- |
| This repo keeps the Indus lane in an anchor-application posture | `AUTHORITY_SNAPSHOT.md`, `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` | Yes | repo is still staged, not promoted |
| Phase 4 morphology remains caveated rather than narratively cleaned up | `authority/review_pack/phase4_governing_verdict.md`, `authority/review_pack/indus_catalogue_summary.md` | Yes | later paper work improves the catalogue but does not erase the caveat |
| Search stays inside `gnosis-indus` as an application surface | `authority/review_pack/search_demo_summary.md`, `SOURCE_BOUNDARY.md`, `docs/family/INDUS_EXPORT_CONTRACT.md` | Yes | no standalone search repo claim |

## Minimum Replay Steps

1. Confirm the authority files exist at the named paths.
2. Compare the README language against `AUTHORITY_SNAPSHOT.md`.
3. Compare the morphology language against the copied Phase 4 verdict.
4. Compare the language/substrate language against the copied Phase 5 verdict.
5. Record any unsupported claim as `UNKNOWN` or dispute it directly.

## If You Find A Problem

- Use the evidence dispute template for claim/evidence disagreements.
- Use the bug template for reproducible package or docs defects.
- Use `PUBLIC_AUDIT_LIMITS.md` when the disagreement depends on unavailable
  data rights or heavy upstream assets.
