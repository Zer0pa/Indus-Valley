# Data Policy

## Governing rule

Do not let evidence pressure become a pretext for vague rights language. If the
repo cannot safely ship an asset family yet, say so plainly and move it to a
fetch or derived-only surface.

## Classification

| Class | Asset family | Current handling |
| --- | --- | --- |
| `PUBLIC_NOW` | copied verdict markdown, PRD, docs, starter package files | ship in repo |
| `PUBLIC_LATER` | selected derived JSON metrics and paper source files | admit case by case |
| `FETCH_EXTERNAL` | open corpora, canonical sign images, ICIT reference sources | do not vendor now |
| `BLOCKED_RIGHTS` | image-bearing releases with unresolved provenance or redistribution terms | keep out of the public starter |
| `OWNER_HELD` | public contact and unpublished release metadata | wait for owner input |

## Specific caveats

- ICIT/Wells/Fuls, CISI, Mahadevan-derived, and related sign-image rights are
  not yet clean enough for an unrestricted public image release.
- The current repo may describe the catalogue and search surface using derived
  outputs without claiming unrestricted redistribution of all source images.
- Large language corpora used in Phase 5 should be fetched from their upstream
  homes, not mirrored casually into this repo.

### Classification of first-slice artifact families (search-without-decode)

The chosen Phase 02 first slice is the search-without-decode application
surface (`scripts/indus/phase4_search_demo.py` → `src/gnosis_indus/search_surface/`).
Its dependent artifact classes are admitted as follows:

| Artefact class | Example | Class | Handling |
| --- | --- | --- | --- |
| Derived cluster-ID tables and catalogue JSON required by the query engine | `indus_catalogue.json`, `indus_catalogue_summary.md` | `PUBLIC_LATER` | admit case by case into `artifacts/phase4/`; no image bits, integer IDs and cluster summaries only |
| Cluster-sequence encodings of inscriptions | `M-1A: [29 5 38 13 32]` style tables | `PUBLIC_LATER` | admit with the cluster-only encoding shown in the Phase 4 Track C demo; never accompanied by source sign imagery |
| Latency and compression benchmark outputs | query latency tables, 5.89x catalogue compression number | `PUBLIC_NOW` | safe to ship; they are already in the copied `authority/review_pack/search_demo_summary.md` |
| Raw sign images, ICIT/Wells/Fuls reference plates | any bitmap or vector trace of a sign | `BLOCKED_RIGHTS` | not admitted by the first slice; rights remain unresolved |
| ICIT reference JSON with image provenance chains | `icit_reference_frozen.json` | `FETCH_EXTERNAL` | referenced by locator only; pulled from its canonical upstream home when needed, not vendored |
| Phase 5 large language corpora | Sanskrit/Tamil/Prakrit reference corpora | `FETCH_EXTERNAL` | irrelevant to the first slice; remains fetch-only when the third wave lands |

The first slice therefore opens no new rights surface. It publishes only
derived integer IDs, cluster sequences, and latency/compression numbers
that the copied Phase 4 Track C authority document already describes.

## Safe starter contents

- markdown verdicts and authority docs
- contracts and manifests
- minimal package code

## Unsafe starter contents

- raw sign-image dumps
- mirrored large corpora without a rights check
- unpublished owner-held data or credentials

## Off-repo storage surfaces

Heavy or rights-gated assets never enter this GitHub repo. Approved private
landing zones for working artifacts are:

| Surface | Locator | Scope | Rights posture |
| --- | --- | --- | --- |
| HF dataset repo | `Architect-Prime/gnosis-indus-artifacts` (private) | derived Phase 4/5 artifacts, evaluation outputs, intermediate derived JSON, and durable source/workspace backups | private; no public redistribution until rights are cleared |
| HF model repo | `Architect-Prime/gnosis-indus-models` (private) | model checkpoints produced by runtime extractions | private; weights remain scoped to the lane |
| RunPod workspace | `/workspace/gnosis-indus-env/repo` on pod `<RUNPOD_POD>` | ephemeral compute staging for extraction and smoke paths | scratch; anything promoted back to this repo must pass `DATA_POLICY` classification |

`FETCH_EXTERNAL` families are fetched from their canonical upstream homes and
never mirrored into private HF storage unless a fetch manifest records the
provenance and rights decision. Per `HF_CUSTODY_REGISTER.md`, deleted
`Zer0pa/gnosis-indus-*` HF repos are historical only and are not active custody
surfaces for this lane.

`BLOCKED_RIGHTS` families never land on any of the above surfaces.
