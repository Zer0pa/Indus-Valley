# Phase 4 Demo Fixture

This directory ships an **authority-backed demo fixture**, not the real
Phase 4 catalogue.

## File: `indus_catalogue_demo_fixture.json`

A small JSON catalogue assembled strictly from data present in
`authority/review_pack/search_demo_summary.md`. It is sufficient to
reproduce the authority-doc query results that were enumerated in that
document, which is the subset the Phase 02 stronger smoke path asserts.

It is **not** the full catalogue. The real catalogue contains:

- 412 sign types
- 70 morphological clusters
- 179 inscriptions

The full catalogue is classified `FETCH_EXTERNAL` per
`DATA_POLICY.md`. It is not vendored here.

### Authority caveats carried forward

- **k=70 conditional admission.** The full catalogue is admitted with a
  stability caveat (Phase 4 Track A3 stability gates fail or come in
  borderline; see `authority/review_pack/phase4_governing_verdict.md`).
- **Non-decipherment posture.** Cluster IDs are morphological groupings
  only. They do not encode meaning. Phase 5
  (`authority/review_pack/phase5_governing_verdict.md`) leaves substrate
  identification indistinguishable.
- **Demo fixture vs full catalogue.** Every consumer of this fixture is
  responsible for surfacing this distinction and not promoting fixture
  results to full-catalogue results.

### Provenance trace

Each row in the fixture is traceable to a specific section of
`search_demo_summary.md`. Reading order in the doc maps to fixture rows
as follows:

| Fixture row | Source line(s) in `search_demo_summary.md` |
|-------------|---------------------------------------------|
| `clusters["2"]` | Query 1 result block (`Sign ID: 324`) — also used by query 4 (`Sign ID: 86`) |
| `clusters["26"]` | Query 5 result block (`Sign ID: 50`) |
| `clusters["38"]` | Query 3 result block (`Sign ID: 385`) |
| `clusters["65"]` | Query 2 result block (`Sign ID: 122`) |
| `inscriptions["M-1A"]` ... `inscriptions["M-9A"]` | Sample Encodings table (rows M-1A, M-3A, M-4A, M-5A, M-6A, M-7A, M-8A, M-9A). Note: M-2A is absent from the table; the fixture omits it accordingly. |
| `inscriptions["M-7A"]` `label` | Query 6 enumeration row for M-7A |
| `inscriptions_partial["M-14A"]` ... `["M-20A"]` | Query 6 enumeration rows |
| `inscriptions_partial["M-21A"]` ... `["M-44A"]` (the rows listed in query 7 enumeration) | Query 7 enumeration rows |
| `inscriptions_partial["M-50A"]` ... `["M-64A"]` | Query 8 enumeration rows |
| `inscriptions_partial["M-36A"]`, `["M-38A"]`, `["M-49A"]`, `["M-91A"]`, `["M-117A"]` | Query 9 enumeration rows |
| `inscriptions_partial["M-64A"]`, `["M-86A"]`, `["M-117A"]`, `["M-122A"]`, `["M-135A"]` | Query 10 enumeration rows |

### Truncation and `... and N more`

The authority doc renders each query's match list truncated with `... and N
more`. The fixture only encodes the inscriptions that are explicitly
enumerated. Tests that compare fixture match counts to authority match
counts therefore assert that the enumerated subset is contained in the
fixture's match set, **not** that the fixture's match count equals the
authority match count for queries 6/7/8/9 (where truncation hides
inscriptions). Query 10 is fully enumerated in the doc.

### Unmapped tokens

The authority doc renders some cluster positions as `-1` to mean "the
underlying sign is in the corpus but is not assigned a cluster". The
fixture preserves `-1` exactly as written. Consumers must not silently
drop or remap them.
