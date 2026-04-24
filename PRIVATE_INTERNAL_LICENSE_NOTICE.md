# Private Internal License Notice

**Visibility:** PRIVATE / INTERNAL only while this notice is in effect.

## Current legal status

No public license is granted unless and until a license file is added
by Zer0pa.

This repository (`Zer0pa/Indus-Valley`, GitHub visibility `INTERNAL`)
is held for internal and invited-reviewer use. No external
distribution, reproduction, mirroring, or publication of its contents
is authorized except as explicitly permitted in writing by Zer0pa.

## What this replaces

The repo root still contains `LICENSE_PLACEHOLDER.md`, which records
the upstream template's `OWNER_DEFERRED` posture. That placeholder
remains for migration-history continuity. **This notice is the
controlling statement on licensing until a real `LICENSE` file is
added.**

## What reviewers may do

Invited internal reviewers and collaborators with explicit access may:

- clone and inspect the repo
- run the local smoke path (`pip install -e .[test] && pytest -q`)
- open issues on the repo for review findings
- cite the repo internally within Zer0pa

## What reviewers may not do

- redistribute any portion of the repo outside the invited review set
- publish, mirror, or fork the repo to a public surface
- release derived artifacts, datasets, or weights based on the repo
  contents
- assume any OSS license applies by analogy to other Gnosis repos

## Specific carve-outs

- **`authority/` bundle copies.** The Phase 4 / Phase 5 review-pack
  verdicts and the Paper 1 / Paper 2 verdicts copied into `authority/`
  were produced by the Gnosis project and copied into this repo as
  scientific provenance. They carry whatever rights attach to the
  original verdict documents; see `DATA_POLICY.md` for the current
  classification table.
- **Indus image-bearing assets.** None are present in the starter.
  Raw sign images, ICIT/Wells/Fuls reference plates, and related
  image-bearing corpora are classified `BLOCKED_RIGHTS` in
  `DATA_POLICY.md` and are not admitted by the repo.
- **Demo fixture.** `artifacts/phase4/indus_catalogue_demo_fixture.json`
  contains only derived integer IDs, cluster sequences, and
  inscription labels extracted from the admitted Phase 4 Track C
  authority document. It is rights-clean for internal use but remains
  subject to this notice.

## Path to a public license

A public license decision requires Zer0pa legal review of:

1. code license (Apache-2.0 / MIT / source-available / proprietary)
2. documentation license (all-rights-reserved / CC-BY / CC-BY-NC)
3. dataset license for any admitted artifact families
4. model-weight license for any later weights produced from admitted
   corpora
5. third-party provenance obligations for image-bearing sources (ICIT,
   Wells-Fuls, CISI, Mahadevan-derived) and language corpora (DCS,
   OSCAR, IndicCorp)
6. contributor/IP representation for agent-authored code and copied
   authority material
7. brand/trademark posture for the Gnosis and Zer0pa names

See `GNOSIS_REPO_CLOSEOUT_BRIEF_2026-04-24.md` §Legal And Licensing
Brief for the portfolio-wide framing.

## Until then

- Visibility stays `INTERNAL`.
- No public release mechanism is wired.
- Reviewers auditing the repo should treat every file as "private,
  internal, all rights reserved by Zer0pa" unless an explicit narrower
  statement appears in the file.
