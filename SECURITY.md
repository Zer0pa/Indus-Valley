# Security

## Reporting

Report security issues through an owner-held private route until a public
security contact is published.

If you are unsure whether something is security-sensitive, default to private
reporting first.

## What To Include

- affected version, branch, or commit
- reproduction steps
- impact description
- any proof-of-concept material needed to verify the issue safely
- whether the issue is already public elsewhere

## Response Targets

| Step | Target |
| --- | --- |
| Initial acknowledgement | best effort while the repo remains staged |
| Triage decision | best effort while the repo remains staged |
| Fix or mitigation update | depends on issue severity and extraction state |

## Public Issues

Do not open public issues for vulnerabilities that could expose users,
operators, private assets, or unpatched attack paths. Use the bug template only
for non-sensitive defects.

## Repo Boundary

- Current code surface is a minimal starter, not the full extracted runtime.
- Data-rights and upstream-fetch constraints are real and may shape fixes.
