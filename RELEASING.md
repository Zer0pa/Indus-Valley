# Releasing

## Release Principle

Release only when the staged repo's public truth matches the copied authority
surface and the current data-rights boundary. If a cleaner narrative would be
required to ship, the release is not ready.

## Release Types

| Release Type | Use When | Minimum Gate |
| --- | --- | --- |
| Snapshot | sharing a dated staged state for review | docs and authority surface are coherent |
| Tagged release | shipping a named public version | evidence, docs, smoke tests, and license surface agree |
| Breaking release | changing contracts or public semantics | explicit migration note plus downstream review |

## Required Checks

- `AUTHORITY_SNAPSHOT.md` is current.
- `AUDITOR_PLAYBOOK.md` still points to the right authority files.
- `PUBLIC_AUDIT_LIMITS.md` still matches the repo's actual evidence and rights posture.
- `docs/ARCHITECTURE.md` reflects the actual repo structure.
- `SMOKE_TESTS.md` passes.
- release notes do not reintroduce decipherment or standalone search claims.

## Live Sync Sequence

1. Freeze the intended acquisition surface.
2. Update authority, README, boundary docs, and architecture together.
3. Run the smoke path.
4. Publish only after rendered docs and local docs match.

## Current release metadata posture

- Versioning scheme: semantic versioning once runtime extraction starts
- Release notes location: `CHANGELOG.md` once created
- License identity: `OWNER_DEFERRED`
- Downstream compatibility promise: none beyond the documented starter contract
