# Governance

## Scope

This document defines how `gnosis-indus` states truth, promotes claims, handles
disputes, and decides whether the staged repo is ready for release or promotion.

## Truth Hierarchy

1. `PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md` governs repo intent and boundaries.
2. Copied authority docs and later admitted artifacts govern promoted claims.
3. Public docs summarize current truth; they do not override authority docs.
4. Issues can challenge truth, but they do not redefine it by discussion alone.

## Status Vocabulary

| Token | Meaning |
| --- | --- |
| `VERIFIED` | Backed by current evidence in this repo |
| `PARTIAL` | Evidence exists, but the claim is bounded |
| `UNKNOWN` | No evidence surface exists yet |
| `UNVERIFIED` | Proposed, but not closed |
| `INFERRED` | Reasonable interpretation, not direct proof |
| `OWNER_DEFERRED` | Needs owner-supplied input before closure |

## Decision Rights

| Topic | Authority | Notes |
| --- | --- | --- |
| PRD amendments | repo maintainer | threshold changes must be explicit |
| Promoted public claims | repo maintainer | no proxy-only closure |
| Release approval | repo maintainer | must satisfy `RELEASING.md` |
| Legal statements | repo owner | must match final license text |

## Claim Discipline

- One canonical authority block lives in `README.md`.
- `AUTHORITY_SNAPSHOT.md` is the compact repo truth surface.
- Supporting docs deepen or bound the truth; they do not wash out caveats.
- Search must stay framed as an in-repo application surface.
- Phase 4 stability caveats remain visible across all front-door docs.

## Dispute Handling

1. Point to the exact statement under dispute.
2. Point to the conflicting evidence path.
3. Classify the issue as contradiction, ambiguity, missing artifact, or stale
   public surface.
4. Repair the evidence or downgrade the claim. Do not rewrite prose to hide the
   contradiction.
