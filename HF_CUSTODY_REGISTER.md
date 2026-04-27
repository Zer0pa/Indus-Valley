# Hugging Face Custody Register — Indus-Valley

**As of:** 2026-04-27 (Wave 5 — operational-safety consolidation)
**Token identity verified:** `Architect-Prime` (org membership `Zer0pa`)
**Scope:** off-machine durable storage for `Zer0pa/Indus-Valley`
**Working assumption:** the local Mac is unstable and may become
unrecoverable at any moment. Every artifact of value for this lane
must live on at least two off-machine surfaces (GitHub + AP HF) so
the lane is reproducible without local access.

## Routing rule (governing)

Per `GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26.md` §1.2 plus the
2026-04-27 operational-safety direction:

- **`Zer0pa/*`** — **not used for this lane.** Per direct owner
  instruction, no Zer0pa-org HF storage is consumed for Indus-Valley.
- **`Architect-Prime/*`** — canonical durable store. Holds the full
  source mirror of `Zer0pa/Indus-Valley`, the authority bundle, the
  Phase 4 demo fixture, the `.gpd/` control plane, the Phase 02
  runtime, the test surface, the front-door doc set, plus the
  pre-existing 2026-04-26 portfolio-pass workspace artifacts.

`Zer0pa/Indus-Valley` (GitHub) remains the canonical authoring and CI
surface. `Architect-Prime/gnosis-indus-*` is the canonical durable
backup.

## Canonical AP register (live)

### `Architect-Prime/gnosis-indus-artifacts`

| Field | Value |
| --- | --- |
| **Repo type** | `dataset` |
| **Visibility** | private (must remain so per brief §1.3 + §8) |
| **Tier** | canonical heavy/full off-machine store |
| **Revision SHA (main)** | `3a39d1aa20ef…` (post-Wave-5 refresh; re-verify via the command below for full SHA) |
| **File count** | 96 |
| **Composition** | Layer A (pre-existing 2026-04-26 portfolio safety pass): `backups/2026-04-27/indus_workspace_artifacts_2026-04-27.tar.zst` (5,604,377 B) + `backups/2026-04-27/LANE_CHECKSUMS.sha256` (719 B). Layer B (Wave-5, 2026-04-27): `Indus-Valley-source-023a14e91155.tar.gz` (113 KB git-archive of GitHub HEAD) + uncompressed `repo/` mirror of the same HEAD (90 files: full `authority/`, `artifacts/phase4/`, `src/gnosis_indus/`, `tests/`, `.gpd/`, `docs/`, root front-door, `.github/`). Layer C: `README.md` + `MANIFEST.txt`. |
| **Holds** | full source + state + workspace artifact backup; everything required to reproduce the lane without local-Mac access. |
| **Rights class** | derived integer IDs and cluster sequences only; no image bytes admitted; `BLOCKED_RIGHTS` material excluded. |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **GitHub HEAD at last sync** | `023a14e91155637d8246262e79a00bab299975cc` |

### `Architect-Prime/gnosis-indus-models`

| Field | Value |
| --- | --- |
| **Repo type** | `model` |
| **Visibility** | private (must remain so per brief §1.3 + §8) |
| **Tier** | canonical heavy weight store |
| **Revision SHA (main)** | `6983a7eea43e…` (post-Wave-5 refresh; re-verify via the command below for full SHA) |
| **File count** | 3 |
| **Files** | `.gitattributes` (HF auto-init), `README.md` (Wave-5 truthful card), `checkpoints/indus_structural_adapter_stage4.pt` (44,077 B; pre-existing 2026-04-26 portfolio-pass upload). |
| **Pre-existing checkpoint** | `indus_structural_adapter_stage4.pt` Stage-4 structural adapter; SHA-256 `6fa357d9f26812ed5e1a61d736773981aa6d74b6706fa72aab204799f1dda5cc` per `Architect-Prime/gnosis-indus-artifacts::backups/2026-04-27/LANE_CHECKSUMS.sha256`. |
| **Rights class** | private only; weight distribution requires Zer0pa legal clearance per `NOTICE.md` and the Gnosis Portfolio Licensing Intake. |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |

## Decommissioned repos (Wave 5)

| Repo | Type | Status | Reason |
| --- | --- | --- | --- |
| `Zer0pa/gnosis-indus-artifacts` | dataset | **deleted** (404 confirmed) | direct owner instruction (no Zer0pa-org HF storage for this lane); content was a 2-file card-only stub with no scientific artifacts to migrate. |
| `Zer0pa/gnosis-indus-models` | model | **deleted** (404 confirmed) | as above. |
| `Architect-Prime/zeropa-org-gnosis-indus-artifacts` | dataset | **deleted** | byte-identical mirror of the now-deleted `Zer0pa/gnosis-indus-artifacts`; held no unique content beyond the canonical AP repo. |
| `Architect-Prime/zeropa-org-gnosis-indus-models` | model | **deleted** | byte-identical mirror of the now-deleted `Zer0pa/gnosis-indus-models`; held no unique content beyond the canonical AP repo. |

Card text from the now-deleted Zer0pa repos and their mirrors is
recoverable from this repo's git history at the prior commit
`023a14e91155` (the README.md served as the published card before
Wave-5 consolidation).

## Pre-existing portfolio safety-pass content (acknowledged)

A portfolio-level safety pass on **2026-04-26 23:44–23:50 UTC** (prior
to this Wave-5 lane work) produced the following artifacts, all of
which are preserved untouched by Wave 5:

- `Architect-Prime/gnosis-indus-artifacts::backups/2026-04-27/indus_workspace_artifacts_2026-04-27.tar.zst` (5.6 MB compressed Indus workspace)
- `Architect-Prime/gnosis-indus-artifacts::backups/2026-04-27/LANE_CHECKSUMS.sha256` (719 B SHA-256 manifest covering this and sibling lane backups)
- `Architect-Prime/gnosis-indus-models::checkpoints/indus_structural_adapter_stage4.pt` (44 KB Stage-4 structural adapter)

Wave 5 added the source mirror, MANIFEST, and refreshed READMEs but
did not modify these pre-existing items.

## Recovery procedure

**From GitHub (preferred):**

```bash
git clone https://github.com/Zer0pa/Indus-Valley.git
cd Indus-Valley
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e '.[test,numerics]'
pytest -q       # expected: 14 passed
```

**From Architect-Prime HF (Mac dies + GitHub disrupted):**

```bash
pip install huggingface_hub
python3 -c "
from huggingface_hub import hf_hub_download
p = hf_hub_download(
    repo_id='Architect-Prime/gnosis-indus-artifacts',
    repo_type='dataset',
    filename='Indus-Valley-source-023a14e91155.tar.gz',
)
print(p)"
tar xzf Indus-Valley-source-023a14e91155.tar.gz
cd Indus-Valley-023a14e91155
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e '.[test,numerics]'
pytest -q       # expected: 14 passed
```

**Pre-existing workspace backup recovery:**

```bash
python3 -c "
from huggingface_hub import hf_hub_download
print(hf_hub_download(
    repo_id='Architect-Prime/gnosis-indus-artifacts',
    repo_type='dataset',
    filename='backups/2026-04-27/indus_workspace_artifacts_2026-04-27.tar.zst',
))"
zstd -d indus_workspace_artifacts_2026-04-27.tar.zst -o indus_workspace_artifacts_2026-04-27.tar
# Verify SHA-256 against backups/2026-04-27/LANE_CHECKSUMS.sha256
```

**Stage-4 structural adapter recovery:**

```bash
python3 -c "
from huggingface_hub import hf_hub_download
print(hf_hub_download(
    repo_id='Architect-Prime/gnosis-indus-models',
    filename='checkpoints/indus_structural_adapter_stage4.pt',
))"
```

## Verification command

```bash
python3 -c "
from huggingface_hub import HfApi; a = HfApi()
for rt, rid in [
    ('dataset', 'Architect-Prime/gnosis-indus-artifacts'),
    ('model',   'Architect-Prime/gnosis-indus-models'),
]:
    info = (a.dataset_info if rt == 'dataset' else a.model_info)(rid)
    print(f'{rt}:{rid} private={info.private} sha={info.sha[:12]} files={len(info.siblings)}')
# Confirm decommissioned repos are gone:
for rt, rid in [
    ('dataset', 'Zer0pa/gnosis-indus-artifacts'),
    ('model',   'Zer0pa/gnosis-indus-models'),
    ('dataset', 'Architect-Prime/zeropa-org-gnosis-indus-artifacts'),
    ('model',   'Architect-Prime/zeropa-org-gnosis-indus-models'),
]:
    try:
        (a.dataset_info if rt == 'dataset' else a.model_info)(rid)
        print(f'  STILL EXISTS {rt}:{rid}')
    except Exception:
        print(f'  CONFIRMED DELETED {rt}:{rid}')
"
```

Expected (Wave 5):

```
dataset:Architect-Prime/gnosis-indus-artifacts private=True sha=<post-Wave-5> files=96
model:Architect-Prime/gnosis-indus-models     private=True sha=<post-Wave-5> files=3
  CONFIRMED DELETED dataset:Zer0pa/gnosis-indus-artifacts
  CONFIRMED DELETED model:Zer0pa/gnosis-indus-models
  CONFIRMED DELETED dataset:Architect-Prime/zeropa-org-gnosis-indus-artifacts
  CONFIRMED DELETED model:Architect-Prime/zeropa-org-gnosis-indus-models
```

## Off-machine durability check (mission test)

Every artifact of value for this lane must exist on at least two
off-machine surfaces. Wave-5 status:

| Asset | GitHub | Architect-Prime HF |
|---|---|---|
| Front-door docs (NOTICE, README, AUTHORITY_SNAPSHOT, PRD, MIGRATION_PLAN, SOURCE_BOUNDARY, DATA_POLICY, etc.) | yes (`Zer0pa/Indus-Valley@023a14e91155`) | yes (under `repo/` in AP/gnosis-indus-artifacts) |
| Authority bundle (Phase 4/5 verdicts; Paper 1/2 verdicts) | yes | yes (`repo/authority/`) |
| Phase 4 demo fixture (`indus_catalogue_demo_fixture.json`) | yes | yes (`repo/artifacts/phase4/`) |
| Phase 02 runtime (`src/gnosis_indus/search_surface/`) | yes | yes (`repo/src/`) |
| pytest suite (`tests/test_search_surface.py`, 14 passed) | yes | yes (`repo/tests/`) |
| `.gpd/` control plane + every VERIFICATION report | yes | yes (`repo/.gpd/`) |
| `.github/workflows/ci.yml` | yes | yes (`repo/.github/`) |
| Workspace artifact backup (`indus_workspace_artifacts_2026-04-27.tar.zst`) | no — too heavy for code repo | yes (`backups/2026-04-27/`) |
| Stage-4 structural adapter (`indus_structural_adapter_stage4.pt`) | no — model weight, not code | yes (`AP/gnosis-indus-models::checkpoints/`) |
| LANE_CHECKSUMS.sha256 | no | yes (`backups/2026-04-27/`) |

**Result: every Indus-lane asset of value is present on at least one
off-machine surface; everything except the workspace tarball, model
weight, and checksums file is on both GitHub and AP HF. The
heavy/binary items are on AP HF only because they don't belong in a
code repo, but they have SHA-256 commitments and are recoverable
deterministically.**

## What this register does **not** claim

- It does not claim the workspace tarball or the Stage-4 checkpoint
  were authored by this lane agent. They predate Wave 5 and are
  acknowledged as portfolio-safety-pass output (see "Pre-existing
  portfolio safety-pass content" above).
- It does not close the rights question for any future uploaded
  artifact. Every future promotion still requires a classification
  decision per `DATA_POLICY.md`.
- It does not bypass `NOTICE.md`. The legal posture for everything
  catalogued here is set by the consuming GitHub repo's `NOTICE.md`
  and the Gnosis Portfolio Licensing Intake.

## Update protocol

This register must be regenerated whenever:

- a file is added, removed, or replaced in either AP repo;
- either AP repo's visibility changes (it must not);
- the consuming GitHub repo advances HEAD beyond
  `023a14e91155637d8246262e79a00bab299975cc` and that advancement is
  synced to AP via the procedure in
  `Architect-Prime/gnosis-indus-artifacts::README.md` "Sync protocol";
- any new HF repo is created for this lane (it should not be unless
  the orchestrator says otherwise);
- the org membership or token identity changes.
