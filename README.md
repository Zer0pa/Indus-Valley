# Gnosis Indus Atlas

> Staged anchor application and evidence repo for the Indus lane.
> Useful now, improving without overclaim.

## What This Repo Is

This repo is the standalone scaffold for the Indus-facing Gnosis workstream. It
packages the carried-forward evidence chain around the Indus morphological
catalogue, the Phase 5 falsification work, the paper verdict stack, and the
search-without-decode application surface. It is deliberately not a
decipherment repo, not the portfolio's lead thesis, and not a separate generic
search product.

Current scientific truth remains qualified: Phase 4 morphology is admitted with
a stability caveat, Phase 5 supports linguistic structure without closing on a
specific substrate, and later paper work strengthens the catalogue without
erasing the earlier caution.

## Current Authority

| Item | Current Truth |
| --- | --- |
| Product lane | Anchor application and evidence repo |
| Repo URL | `OWNER_DEFERRED_UNPUBLISHED` |
| Default branch | `main` |
| Acquisition surface | local staged scaffold pending later promotion |
| Current authority artifact | `AUTHORITY_SNAPSHOT.md` |
| Evidence status | `PARTIAL` |
| License | `OWNER_DEFERRED` |
| Primary contact | `OWNER_DEFERRED` |

## What We Prove Now

- This scaffold preserves the carried-forward authority surfaces and boundaries
  required to migrate `gnosis-indus` without monorepo tribal knowledge.
- The Indus lane is packaged here as an anchor application and evidence surface,
  not as a decipherment or substrate-closure claim.
- Search-without-decode remains documented here as an in-repo application
  surface rather than a separate sovereign repo.

## What We Do Not Claim

- We do not claim decipherment of the Indus script.
- We do not claim proven substrate identification.
- We do not claim unrestricted public redistribution rights for every
  image-bearing or corpus-bearing source used in the original monorepo.

## Replay

Reproduce the Phase 02 stronger smoke path on any clean Python 3.11 host:

    git clone https://github.com/Zer0pa/Indus-Valley.git gnosis-indus
    cd gnosis-indus
    python -m venv .venv && source .venv/bin/activate
    pip install -e ".[test]"
    pytest -q

Expected: `14 passed`. The pytest suite reproduces the
authority-doc query records from
`authority/review_pack/search_demo_summary.md` against the bundled
`artifacts/phase4/indus_catalogue_demo_fixture.json`. The fixture is
small and authority-anchored; the real full catalogue (412 signs, 70
clusters, 179 inscriptions) stays `FETCH_EXTERNAL` per
`DATA_POLICY.md`. The Phase 4 stability caveat (k=70 conditional)
remains visible in the package and fixture surfaces.

## Read Next

| Need | File |
| --- | --- |
| Current authority snapshot | `AUTHORITY_SNAPSHOT.md` |
| Sovereign repo brief | `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` |
| Fastest outsider audit path | `AUDITOR_PLAYBOOK.md` |
| Public-audit boundaries | `PUBLIC_AUDIT_LIMITS.md` |
| Architecture and truth map | `docs/ARCHITECTURE.md` |
| Migration backlog and blockers | `MIGRATION_PLAN.md` |
| Source and data boundaries | `SOURCE_BOUNDARY.md`, `DATA_POLICY.md` |

## Current Gaps

- Image-rights and provenance for any public image-bearing release remain
  unresolved; sign images stay `BLOCKED_RIGHTS` in `DATA_POLICY.md`.
- Final license text and public contact are owner-deferred
  (`OWNER_DEFERRED` in `LICENSE_PLACEHOLDER.md` and `docs/LEGAL_BOUNDARIES.md`).
- Phase 02 landed only the search-without-decode slice. The Phase 4
  catalogue and Phase 5 falsification slices are sequenced as later
  extraction waves (`MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`).
