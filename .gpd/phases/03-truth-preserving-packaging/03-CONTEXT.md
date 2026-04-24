# Phase 03 Context

## Goal

Package only what survives the admitted gates. Bring all front-door docs
and authority surfaces into agreement with the Phase 02 reality (clean-room
search_surface landed; pytest stronger smoke runs green on Mac and on
RunPod from a fresh clone). Surface remaining promotion blockers honestly.

## What Changed Since The Front-Door Was Last Coherent

| Surface | Before Phase 02 | After Phase 02 |
| --- | --- | --- |
| First extracted runtime slice | not landed | `src/gnosis_indus/search_surface/` landed (clean-room from authority doc) |
| Stronger smoke path | aspirational only | real: `pip install -e .[test] && pytest -q` (14 passed) |
| Clean-machine replay | not demonstrated | demonstrated on RunPod pod `7k3riasglemecu` from a fresh `git pull` |
| Demo fixture | not present | `artifacts/phase4/indus_catalogue_demo_fixture.json` (rights-clean, authority-anchored) |
| Off-repo storage surfaces | undeclared | `Zer0pa/gnosis-indus-artifacts` (HF dataset) and `Zer0pa/gnosis-indus-models` (HF model) provisioned private |

## PRD §8 Promotion Blockers — Current Truth

| Blocker (per PRD §8) | Current truth |
| --- | --- |
| data-rights and provenance gap for image-bearing release | **STILL OPEN** — outside this lane's authority |
| no extracted standalone runtime beyond the starter namespace | **CLOSED** — `src/gnosis_indus/search_surface/` landed in Phase 02 |
| no clean-machine replay path yet | **CLOSED** — pod replay from fresh clone confirmed |
| owner-deferred license and public contact details | **STILL OPEN** — requires owner input |

Two of four PRD §8 blockers are now closed. Two remain owner-bound.

## Phase 03 Scope

- Bring `README.md`, `AUTHORITY_SNAPSHOT.md`, and the PRD §8 block into
  agreement with the new truth surface.
- Update `TODO.md` to reflect what the runtime landing actually changed.
- Run a final coherence audit against the four falsification conditions
  (PRD §1.3) and the artifact contract (PRD §7).
- Bump GPD progress to 100% and mark Phase 03 complete.
- Do not invent new claims. Do not hide the two remaining promotion
  blockers (image rights, owner-deferred license/contact).

## Out Of Scope For Phase 03

- adding more runtime slices (would be Phase 02 second/third wave)
- resolving image-rights or licensing — outside this lane
- writing release notes or a CHANGELOG — premature without owner inputs
- pushing to any public surface beyond the existing private repo
