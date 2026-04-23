# Contributing

## First Rule

Contribute only what `gnosis-indus` can honestly support. Do not import claims,
metrics, or release language from other Gnosis or ZPE repos.

## Before You Start

1. Read `README.md`.
2. Read `AUTHORITY_SNAPSHOT.md`.
3. Read `GOVERNANCE.md`.
4. Read `docs/ARCHITECTURE.md`.
5. Use an issue or documented task as the source of change intent.

## Contribution Rules

- Keep scope tight and local to this repo.
- If you change a public claim, update the supporting evidence path too.
- Keep the non-decipherment posture explicit.
- Keep the Phase 4 caveat visible where relevant.
- Keep search framed as an in-repo application surface.
- If a fact is not verified here, mark it `UNKNOWN`, `PARTIAL`, `UNVERIFIED`,
  `INFERRED`, or `OWNER_DEFERRED`.

## Pull Requests

Every PR should state:

- what changed
- why it changed
- what evidence supports it
- what docs were updated
- what remains unknown or deferred

## Boundaries

- Security-sensitive issues belong in `SECURITY.md`.
- Evidence disputes belong in the evidence dispute template.
- Questions that do not require a code change should use the question template.
