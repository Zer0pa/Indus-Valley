# Private Provenance Appendix

**Visibility:** PRIVATE / INTERNAL only. This file must be removed or
excluded before any public release.

## Purpose

Front-door docs, authority-bundle copies, and GPD state in this repo
have been scrubbed of operational paths and endpoints to prevent
leakage under eventual public release. Symbolic labels (`<FOO>`) were
substituted for the concrete values. This appendix records the
mapping so that internal reviewers, agents, and operators can decode
the labels and so that scientific provenance is not destroyed — only
parameterized.

This scrub pattern follows §P2 of
`GNOSIS_REPO_CLOSEOUT_BRIEF_2026-04-24.md`: "Replace operational paths
with symbolic labels such as `<LOCAL_MONOREPO_ROOT>`, `<RUNPOD_HOST>`,
`<HF_ORG>`, and keep a private-only provenance appendix if needed. Do
not delete scientific provenance."

## Label mapping

| Symbolic label | Concrete value (private) | Appears in |
| --- | --- | --- |
| `<MONOREPO_ROOT>` | the monorepo filesystem root that held the original Phase 4 / Phase 5 scripts and paper sources | `authority/review_pack/prd_phase4_indus_catalogue.md`, `authority/review_pack/prd_phase5_falsification.md`, `authority/papers/paper1_governing_verdict.md`, `authority/papers/paper2_governing_verdict.md`, `.gpd/DECISIONS.md`, `.gpd/phases/02-.../02-CONTEXT.md`, `STATUS_REPORT_2026-04-24.md` |
| `<RUNPOD_POD>` | the RunPod pod identifier used for the Phase 02 independent-machine smoke and the Phase 03 re-verification | `DATA_POLICY.md`, `.gpd/phases/03-.../03-CONTEXT.md`, `STATUS_REPORT_2026-04-24.md`, `.gpd/state.json` |
| `<RUNPOD_HOST>` | the exposed-TCP IP for that pod (ephemeral; changes when pod is recycled) | `.gpd/state.json` (historic) |

The concrete values are held outside this repo in the operator's
runbook. Agents that need them should read the runbook, not paste
them back into tracked files.

## Why this is a private-only file

- The labels themselves are safe for eventual public release (they carry
  no operational information).
- The decoded values are not safe: they expose a specific user
  filesystem layout, a monorepo name/organization scheme that reveals
  internal structure, and a specific compute-surface identity.
- If this repo is ever promoted to public, this file must either be
  excluded from the public mirror or moved to a private sibling repo.

## Removal protocol before public release

1. `git rm PRIVATE_PROVENANCE_APPENDIX.md` on the release branch.
2. Add an entry in `.gitignore` on the public release branch so an
   accidental re-commit is caught.
3. Confirm no remaining `<MONOREPO_ROOT>`, `<RUNPOD_POD>`, or
   `<RUNPOD_HOST>` label references exist in user-facing front-door
   docs (they may legitimately remain in `authority/` verdict copies
   and in `PRD §1.3` language as provenance placeholders).
4. Re-run `pytest -q` and confirm nothing depends on decoded labels.

## Recorded because it is true

The scrub does not change any scientific claim in the repo. The
authority bundle's verdict text, the Phase 4 conditional k=70 caveat,
the Phase 5 non-decipherment posture, the query-reproduction results
on the demo fixture, and the migration/data boundaries all survive the
scrub unchanged. Only operational paths are parameterized.
