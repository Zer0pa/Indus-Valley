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
| `OWNER_DEFERRED` | final license, public contact, unpublished release metadata | wait for owner input |

## Specific caveats

- ICIT/Wells/Fuls, CISI, Mahadevan-derived, and related sign-image rights are
  not yet clean enough for an unrestricted public image release.
- The current repo may describe the catalogue and search surface using derived
  outputs without claiming unrestricted redistribution of all source images.
- Large language corpora used in Phase 5 should be fetched from their upstream
  homes, not mirrored casually into this repo.

## Safe starter contents

- markdown verdicts and authority docs
- contracts and manifests
- minimal package code

## Unsafe starter contents

- raw sign-image dumps
- mirrored large corpora without a rights check
- unpublished owner-held data or credentials
