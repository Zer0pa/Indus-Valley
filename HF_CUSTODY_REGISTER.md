# Hugging Face Custody Register — Indus-Valley

**As of:** 2026-04-26 (Wave 4 — HF storage two-tier routing)
**Token identity verified:** `Architect-Prime` (org membership `Zer0pa`)
**Scope:** off-repo storage surfaces associated with `Zer0pa/Indus-Valley`

## Routing rule (governing)

Per `GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26.md` §1.2, Gnosis
storage uses two tiers:

- **`Zer0pa/*`** — lightweight discovery surface: README cards,
  manifests, indices, small JSON / Markdown summaries, schema files,
  small curated bundles useful for review;
- **`Architect-Prime/*`** — canonical heavy private store: any single
  file > 1 MB, total payload > 100 MB, model weights of any size, or
  many-file directories where aggregate weight matters.

For Indus-Valley, that maps to:

- `Zer0pa/gnosis-indus-artifacts` (dataset, private) — exists, card-only
- `Architect-Prime/gnosis-indus-artifacts` (dataset, private) — **not
  provisioned** (no heavy content exists; per brief §3 notes, AP repos
  are created only when the lane has heavy content worth storing)
- `Zer0pa/gnosis-indus-models` (model, private) — exists, card-only
- `Architect-Prime/gnosis-indus-models` (model, private) — **not
  provisioned** (no Indus weights exist)

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
| **Tier** | lightweight discovery surface (org tier) |
| **Private** | `true` |
| **Revision SHA (main)** | `686a0ae9b1ea0a54ae7f339a2bfdeff11ebee554` |
| **File count** | 2 |
| **Files** | `.gitattributes` (HF auto-init), `README.md` (Wave-4 two-tier-routing Gnosis card) |
| **Last modified (UTC)** | 2026-04-26 (Wave-4 card upload) |
| **Created for** | `Zer0pa/Indus-Valley` lightweight discovery surface (see `DATA_POLICY.md` Off-repo storage surfaces) |
| **Holds** | manifests, indices, small JSON / MD summaries, review-facing materials. Heavy items route to AP per Routing Rule above. |
| **Rights class** | holds `PUBLIC_LATER` and `FETCH_EXTERNAL` derived artifacts only; never raw sign images, never `BLOCKED_RIGHTS` assets |
| **Content at register time** | README card only; no scientific artifacts promoted yet |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **Heavy-tier sibling** | `Architect-Prime/gnosis-indus-artifacts` — not provisioned (no heavy content) |

| Field | Value |
| --- | --- |
| **Repo ID** | `Zer0pa/gnosis-indus-models` |
| **Repo type** | `model` |
| **Tier** | lightweight discovery surface (org tier) — see Operator note below |
| **Private** | `true` |
| **Revision SHA (main)** | `0230f0dbc77d0087bbbe2e41a7cae7242e7e0ba5` |
| **File count** | 2 |
| **Files** | `.gitattributes` (HF auto-init), `README.md` (Wave-4 two-tier-routing Gnosis card) |
| **Last modified (UTC)** | 2026-04-26 (Wave-4 card upload) |
| **Created for** | model-card / scorecard / pointer surface for any future Indus weights. **Weights themselves never live here** — they route to `Architect-Prime/gnosis-indus-models` per the brief's two-tier rule (model weights = heavy tier). |
| **Rights class** | private only; model-weight distribution is pending Zer0pa legal clearance per `NOTICE.md` |
| **Content at register time** | README card only; no weights exist anywhere |
| **Consuming GitHub repo** | `Zer0pa/Indus-Valley` |
| **Heavy-tier sibling** | `Architect-Prime/gnosis-indus-models` — not provisioned (no Indus weights exist) |
| **Operator note** | The brief's §3 routing table lists one HF row per Gnosis lane for `*-artifacts` only; a separate `*-models` repo is not explicitly blessed by the new matrix. This repo is retained pending orchestrator review of whether to keep, deprecate, or fold into `*-artifacts`. No churn taken in this pass per brief §6 step 6 ("stop before overreach"). |

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
`.gitattributes` plus the Gnosis-family README card and no
scientific-artifact files. Once real artifacts land, this register
must be regenerated with SHA-256 checksums per file.

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

Expected output (post-Wave-4 card refresh):

```
dataset:Zer0pa/gnosis-indus-artifacts private=True sha=686a0ae9b1ea files=2
model:Zer0pa/gnosis-indus-models private=True sha=0230f0dbc77d files=2
```

## Architect-Prime namespace state (Wave 4)

The earlier Lane Execution Brief
(`HF_LANE_EXECUTION_BRIEF_2026-04-26.md`) treated `Architect-Prime` as
a cleanup target for Gnosis. The newer HF Storage Execution Brief
(`GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26.md`) supersedes that
posture and designates `Architect-Prime/*` as the canonical heavy
private store for Gnosis.

Verified on 2026-04-26 via the production `Architect-Prime` token:

- `Architect-Prime` namespace contains 19 repos at audit time, all
  ZPE-prefixed (`zpe-video-artifacts`, `zpe-neuro-artifacts`,
  `zpe-prosody-artifacts`, etc.) plus restart packets. No Gnosis-
  prefixed content of any kind exists under `Architect-Prime`.
- No `Architect-Prime/gnosis-indus-artifacts` exists.
- No `Architect-Prime/gnosis-indus-models` exists.

Per the new brief's §3 notes ("create AP repos only if the lane
actually has heavy content worth storing"), no AP repos were created
for Indus in this pass. Heavy-content threshold check (§4):

- Largest tracked file in the consuming GitHub repo is
  `tests/test_search_surface.py` (~10 KB).
- `artifacts/phase4/` total size is 8 KB.
- No model weights exist anywhere for this lane.
- Aggregate Indus footprint is well below 100 MB and contains no
  individual file above 1 MB.

Conclusion: Indus has no heavy content to route to AP. The two AP
repos remain unprovisioned.

## What this register does **not** claim

- It does not claim either repo currently carries any Indus-specific
  content. Both still hold only `.gitattributes` plus a README card.
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
