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
- `tools/indus_ops_gate.py --pretty` passes.
- GitHub Actions installs the pinned private `gnosis-ops-gates` package and
  runs the Ops-Gates consumer smoke before the Indus repo-local gate.
- Repository secret `OPS_GATES_READ_TOKEN` exists for read access to the
  private `Gnosis-Ops-Gates` dependency.
- release notes do not reintroduce decipherment or standalone search claims.

## Live Sync Sequence

1. Freeze the intended acquisition surface.
2. Update authority, README, boundary docs, and architecture together.
3. Run the smoke path.
4. Publish only after rendered docs and local docs match.

## Current release metadata posture

- Versioning scheme: semantic versioning after the staged `0.0.0` surface is
  promoted beyond the first search runtime slice
- Release notes location: `CHANGELOG`
- License identity: Apache-2.0 for code; CC-BY-4.0 for documentation, reports,
  and written materials
- Downstream compatibility promise: none beyond the documented starter contract
