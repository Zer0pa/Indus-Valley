# Hugging Face Custody Register — Indus-Valley

**As of:** 2026-04-24
**Token identity verified:** `Architect-Prime` (org membership `Zer0pa`)
**Scope:** off-repo storage surfaces associated with `Zer0pa/Indus-Valley`

This register answers the closeout-brief requirement
(`GNOSIS_REPO_CLOSEOUT_BRIEF_2026-04-24.md` §Hugging Face State And
Housekeeping): produce a register of repo ID, repo type,
private/public status, revision SHA, files, rights class, and
consuming GitHub repo.

The central closeout brief reported that some Zer0pa HF repos (including
the two named below) were not visible to the review token. This register
documents that from the `Architect-Prime` token (org `Zer0pa`) those
repos **are** visible, private, and in a known state. The discrepancy
is a token-visibility issue on the review side, not an HF existence
issue. The production token must be used for all downstream custody
operations.

## Register

| Field | Value |
| --- | --- |
| **Repo ID** | `Zer0pa/gnosis-indus-artifacts` |
| **Repo type** | `dataset` |
| **Private** | `true` |
| **Revision SHA (main)** | `19fc4a7eff1e7ed2229e560d781cfd0a4b0dd41f` |
| **File count** | 1 |
| **Files** | `.gitattributes` (HF auto-init) |
| **Last modified (UTC)** | 2026-04-23 23:20:22 |
| **Created for** | `Zer0pa/Indus-Valley` derived artefact custody (see `DATA_POLICY.md` Off-repo storage surfaces) |
| **Rights class** | holds `PUBLIC_LATER` and `FETCH_EXTERNAL` derived artefacts only; never raw sign images, never `BLOCKED_RIGHTS` assets |
| **Content at register time** | none promoted yet; HF auto-init only |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **Landing-zone-for** | derived cluster JSON (e.g. full k=70 catalogue if rights clear), evaluation outputs, intermediate Phase 4 / Phase 5 JSON artefacts |

| Field | Value |
| --- | --- |
| **Repo ID** | `Zer0pa/gnosis-indus-models` |
| **Repo type** | `model` |
| **Private** | `true` |
| **Revision SHA (main)** | `84531841b6aa346fe789c9b9d6d75072cc8a97c0` |
| **File count** | 1 |
| **Files** | `.gitattributes` (HF auto-init) |
| **Last modified (UTC)** | 2026-04-23 23:20:23 |
| **Created for** | `Zer0pa/Indus-Valley` model-weight custody (see `DATA_POLICY.md`) |
| **Rights class** | private only; model-weight distribution is pending legal clearance per `PRIVATE_INTERNAL_LICENSE_NOTICE.md` §"Path to a public license" |
| **Content at register time** | none promoted yet; HF auto-init only |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **Landing-zone-for** | model checkpoints produced from extracted runtime work (Phase 02 search_surface has no model weights — first candidate weights would come from Phase 4 catalogue runtime or Phase 5 falsification runtime, neither yet extracted) |

## Spelling convention

This repo uses the American spelling `artifact` in filesystem paths
(`artifacts/phase4/`), HF repo names
(`Zer0pa/gnosis-indus-artifacts`), and docs. Other lanes in the Gnosis
portfolio use the British spelling `artefact` (e.g.
`Zer0pa/cuneiform-control-artefacts`, `Zer0pa/glyph-engine-artefacts`).
That inconsistency is known; this lane stays on `artifact` because
that is the spelling already on HF and in all tracked files. The
closeout brief flagged cross-lane alignment as a separate follow-up
and it is not in scope for this lane.

## Checksums

Not provided at register time: both repos contain only HF auto-init
`.gitattributes` and no substantive files. Once real artefacts land,
this register must be regenerated with SHA-256 checksums per file.

## Verification command

Re-verify with:

```bash
python3 -c "
from huggingface_hub import HfApi; a = HfApi()
for rt, rid in [('dataset', 'Zer0pa/gnosis-indus-artifacts'),
                ('model', 'Zer0pa/gnosis-indus-models')]:
    info = (a.dataset_info if rt == 'dataset' else a.model_info)(rid)
    print(f'{rt}:{rid} private={info.private} sha={info.sha[:12]} files={len(info.siblings)}')
"
```

Expected output:

```
dataset:Zer0pa/gnosis-indus-artifacts private=True sha=19fc4a7eff1e files=1
model:Zer0pa/gnosis-indus-models private=True sha=84531841b6aa files=1
```

## What this register does **not** claim

- It does not claim either repo currently carries any Indus-specific
  content. Both are empty landing zones (HF auto-init only).
- It does not claim HF is the durable off-Mac custody for this repo's
  scientific outputs yet. GitHub (`Zer0pa/Indus-Valley`) is the current
  durable custody surface. HF becomes the artefact surface only when
  admitted artefacts are promoted per `DATA_POLICY.md` classification
  and pushed with a corresponding register refresh.
- It does not close the rights question for any future uploaded
  artefact. Every promotion still requires a classification decision
  per `DATA_POLICY.md`.

## Update protocol

This register must be regenerated whenever:

- a file is added or removed from either HF repo;
- either repo's visibility changes;
- a new HF repo is created for this lane;
- the org membership or token identity changes.
