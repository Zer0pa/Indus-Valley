# Smoke Tests

## Current starter smoke path

The repo does not yet claim a full extracted runtime. The current smoke path is
therefore limited to starter integrity:

```bash
python -m compileall src
python -c "import gnosis_indus; print(gnosis_indus.__version__)"
test -f AUTHORITY_SNAPSHOT.md
test -f PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md
test -f docs/family/INDUS_EXPORT_CONTRACT.md
```

## What this establishes

- the starter package imports
- the authority and contract surfaces are present
- the staged repo can be handed to another agent without missing core docs

## What this does not establish

- Phase 4 or Phase 5 reruns
- clean-machine replay of the full evidence stack
- public-data rights clearance
