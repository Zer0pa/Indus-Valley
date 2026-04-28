# Hugging Face Custody Register — Indus-Valley

**As of:** 2026-04-28 (repo-docs coherence review after Wave 6)
**Token identity verified:** `Architect-Prime` (org membership `Zer0pa`)
**Scope:** off-machine durable storage for the entire Indus lane workspace
(`<LOCAL_INDUS_WORKSPACE>` in full,
including the migration-package context outside `05_repo_scaffold/`)
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

**Current GitHub note:** GitHub `main` advanced to `1f1529ce40a9` in the
2026-04-28 public-refresh wave. The AP HF mirror below is still the durable
backup register for the last verified HF sync; use GitHub as the preferred
recovery source unless a later HF resync updates this register.

## Canonical AP register (live)

### `Architect-Prime/gnosis-indus-artifacts`

| Field | Value |
| --- | --- |
| **Repo type** | `dataset` |
| **Visibility** | private (must remain so per brief §1.3 + §8) |
| **Tier** | canonical heavy/full off-machine store |
| **Revision SHA (main)** | `3a39d1aa20ef…` (post-Wave-5 refresh; re-verify via the command below for full SHA) |
| **File count** | 96 |
| **Composition** | Layer A (pre-existing 2026-04-26 portfolio safety pass): `backups/2026-04-27/indus_workspace_artifacts_2026-04-27.tar.zst` (5,604,377 B) + `backups/2026-04-27/LANE_CHECKSUMS.sha256` (719 B). Layer B (Wave-5, 2026-04-27): `Indus-Valley-source-d6a8bb10fef8.tar.gz` (114 KB git-archive of post-Wave-5 GitHub HEAD) + uncompressed `repo/` mirror of the same HEAD (90 files: full `authority/`, `artifacts/phase4/`, `src/gnosis_indus/`, `tests/`, `.gpd/`, `docs/`, root front-door, `.github/`). Layer C: `README.md` + `MANIFEST.txt`. **Layer D (Wave-6, 2026-04-27): `migration-package/` — durable backup of the lane workspace's migration-package context outside the GitHub repo.** Contains `migration-package/indus-migration-package.tar.gz` (47 KB, 24 files, 172 KB uncompressed; SHA-256 `37a699c71a312dbf42d87687a74ae9df4895e66bc85c1776df5e265ca0454b79`), `migration-package/MIGRATION_PACK_SHA256.txt` (per-file SHA-256 manifest), and `migration-package/uncompressed/` (browsable mirror). The migration-package covers `00_brief/`, `01_prd_and_authority/` (including the source-corpus `paper{1,2}_governing_verdict*.md` and pre-scrub `prd_phase{4,5}*.md` retained for provenance), `02_source_inventory/`, `03_data_policy/`, `04_evidence_manifest/`, `06_handover/`, and the workspace `README.md`. |
| **Holds** | full source + state + workspace artifact backup; everything required to reproduce the lane without local-Mac access. |
| **Rights class** | derived integer IDs and cluster sequences only; no image bytes admitted; `BLOCKED_RIGHTS` material excluded. |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **GitHub HEAD at last verified HF sync** | pre-public-refresh source mirror; verify exact archive name and SHA against the AP repo `MANIFEST.txt` before HF-only recovery |

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

First inspect `Architect-Prime/gnosis-indus-artifacts::MANIFEST.txt` and choose
the newest `Indus-Valley-source-*.tar.gz` listed there. The example below shows
the pre-public-refresh source mirror shape and must be updated after the next HF
resync.

```bash
pip install huggingface_hub
python3 -c "
from huggingface_hub import hf_hub_download
p = hf_hub_download(
    repo_id='Architect-Prime/gnosis-indus-artifacts',
    repo_type='dataset',
    filename='<INDUS_SOURCE_ARCHIVE_FROM_MANIFEST>',
)
print(p)"
tar xzf <INDUS_SOURCE_ARCHIVE_FROM_MANIFEST>
cd <EXTRACTED_INDUS_SOURCE_DIR>
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

## Off-machine durability check (mission test — Wave 6)

Every artifact of value for this lane must exist on at least two
off-machine surfaces. Wave-6 status (after the migration-package
durability pass and post-mirror bucket verification):

| Asset | GitHub | Architect-Prime HF |
|---|---|---|
| Front-door docs (NOTICE, README, AUTHORITY_SNAPSHOT, PRD, MIGRATION_PLAN, SOURCE_BOUNDARY, DATA_POLICY, etc.) | yes | yes (`repo/`) |
| Authority bundle (Phase 4/5 verdicts; Paper 1/2 verdicts) | yes | yes (`repo/authority/`) |
| Phase 4 demo fixture (`indus_catalogue_demo_fixture.json`) | yes | yes (`repo/artifacts/phase4/`) |
| Phase 02 runtime (`src/gnosis_indus/search_surface/`) | yes | yes (`repo/src/`) |
| pytest suite (`tests/test_search_surface.py`, 14 passed) | yes | yes (`repo/tests/`) |
| `.gpd/` control plane + every VERIFICATION report | yes | yes (`repo/.gpd/`) |
| `.github/workflows/ci.yml` | yes | yes (`repo/.github/`) |
| **Lane workspace migration-package context (folders 00, 01, 02, 03, 04, 06 + workspace README — 24 files, 172 KB uncompressed)** | **no — never tracked by GitHub** | **yes (`migration-package/`, Wave 6)** |
| **Source-corpus authority docs with pre-scrub paths (provenance audit trail)** | no — superseded by scrubbed copies | **yes (`migration-package/uncompressed/01_prd_and_authority/source_copies/`)** |
| Workspace artifact backup (`indus_workspace_artifacts_2026-04-27.tar.zst`) | no — too heavy for code repo | yes (`backups/2026-04-27/`) |
| Stage-4 structural adapter (`indus_structural_adapter_stage4.pt`) | no — model weight, not code | yes (`AP/gnosis-indus-models::checkpoints/`) |
| LANE_CHECKSUMS.sha256 | no | yes (`backups/2026-04-27/`) |

**Result: every Indus-lane asset of value, including the previously-
local-only migration-package context, is durable off-machine.**

### Migration-package byte-exact verification (Wave 6)

Round-trip SHA-256 verification performed in this session:

| Check | Local SHA-256 | AP-roundtrip SHA-256 | Status |
|---|---|---|---|
| Tarball `migration-package/indus-migration-package.tar.gz` | `37a699c71a312dbf42d87687a74ae9df4895e66bc85c1776df5e265ca0454b79` | `37a699c71a312dbf42d87687a74ae9df4895e66bc85c1776df5e265ca0454b79` | ✓ BYTE-EXACT |
| Sample file `01_prd_and_authority/PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` | `e87bb03f55b884a8c5aed2b4115d90d2fa73000d2c7f08ac760299e52a079d73` | `e87bb03f55b884a8c5aed2b4115d90d2fa73000d2c7f08ac760299e52a079d73` | ✓ MATCH |

Per-file SHA-256 manifest for all 24 migration-package files lives at
`Architect-Prime/gnosis-indus-artifacts::migration-package/MIGRATION_PACK_SHA256.txt`.

### Bucket scope check (Wave 6)

Per the orchestrator's 2026-04-27 post-mirror verification universal
brief, every lane must check whether it owns any HF buckets (xet-
backed scratch storage) and verify the orchestrator's bucket-mirror
operation.

Verified via direct HF API enumeration of both namespaces:

- `Zer0pa/*` buckets: 8 (ZPE-Geo, Zer0paShip, ZPE-Ink, ZPE-Cipher,
  DM3, ZPE-XR, ZPE-Video, ZPE-FT). Total 62.83 GB / 100 GB free-tier.
- `Architect-Prime/*` buckets: 8 mirrors (`zeropa-org-*-scratch`),
  byte-exact match against Zer0pa originals (every file count and
  every byte total matches; 62.83 GB total).
- **Indus / Gnosis buckets in either namespace: zero.** This lane
  does not own any scratch buckets, so STEP 2 of the post-mirror
  brief is N/A for Indus-Valley.

### Local-Mac deletion decisions (Wave 6)

Per the post-mirror brief STEP 3, local deletion is authorised only
after byte-exact AP verification AND only for content that is not on
the brief's NEVER-DELETE list (code tracked by git, .gitignore,
.git/, package config, LICENSE, README, governance/operating files).

| Local content | AP-verified | NEVER-DELETE class | Action taken |
|---|---|---|---|
| `05_repo_scaffold/` tracked files | yes (full mirror under `repo/`) | git-tracked → never delete | retained locally |
| `05_repo_scaffold/.git/` | n/a | repo working tree config → never delete | retained |
| `05_repo_scaffold/.pytest_cache/`, `*egg-info/`, `__pycache__/` | n/a | regenerated build debris | left alone (gitignored; tiny; not worth touching) |
| `00_brief/`, `01_prd_and_authority/`, `02_source_inventory/`, `03_data_policy/`, `04_evidence_manifest/`, `06_handover/` migration-package files (24 files, 172 KB) | yes (Wave-6 round-trip ✓) | governance/operating files (PRD source corpus, AUTHORITY_INDEX, EVIDENCE_MANIFEST, source inventory, data-policy summary, handover notes) → **never delete** | retained locally |
| Workspace `README.md` | yes | README → **never delete** | retained |

**Indus-lane deletion summary: zero files deleted from local Mac.
Every local file falls into the NEVER-DELETE class (tracked code,
README, or governance/operating content). The mission requirement
("if Mac dies, lane is recoverable") is satisfied by full
off-machine durability without needing local cleanup. Free-tier
storage savings on Zer0pa-org are zero for this lane (no Indus
content was on Zer0pa-org after Wave-5).**

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
