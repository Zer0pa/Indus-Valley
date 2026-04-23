# Phase 4 Track C — Search-Without-Decode Demo

Generated: 2026-04-16T00:52:37.984042+00:00

## Gate Verdict: **PASS**

| Criterion | Value | Threshold | Pass |
|-----------|-------|-----------|------|
| Max query latency | 0.0451 ms | < 100 ms | Yes |
| Symbol compression | 5.89x | >= 5x | Yes |

## C1: Corpus Encoding

- **Inscriptions encoded:** 179
- **Total tokens:** 1003
- **Catalogue sign types:** 412
- **Catalogue cluster types:** 70
- **Symbol compression ratio (catalogue):** 5.89x
- **Corpus sign types (observed):** 182
- **Corpus cluster types (observed):** 62
- **Corpus compression ratio:** 2.94x
- **Bits/token (raw):** 9
- **Bits/token (cluster):** 7
- **Bit-level compression:** 1.29x
- **Unmapped tokens:** 24
- **Coverage:** 97.6%

### Sample Encodings

| Artifact | Raw signs | Cluster seq |
|----------|-----------|-------------|
| M-1A | 121 202 385 73 108 | 29 5 38 13 32 |
| M-3A | 320 145 94 | 17 57 64 |
| M-4A | 205 186 147 316 56 122 237 268 268 147 | 4 2 15 40 2 65 44 39 39 15 |
| M-5A | 324 96 62 60 120 256 | 2 3 19 19 39 33 |
| M-6A | 378 384 201 65 | 57 6 68 38 |
| M-7A | 86 352 11 324 154 9 154 175 62 122 385 | 2 19 36 2 35 10 35 69 19 65 38 |
| M-8A | 316 11 270 | 40 36 12 |
| M-9A | 144 205 327 | 57 4 62 |

## C2: Query Engine Results

### Query 1: sign_lookup

- **Latency:** 0.0025 ms
- **Sign ID:** 324
- **Cluster ID:** 2
- **Cluster size:** 20
- **Members:** [10, 18, 41, 56, 61, 76, 79, 81, 84, 86, 92, 180, 186, 247, 279, 324, 390, 391, 406, 412]
- **Dominant set:** set_04
- **Dominant graph:** human

### Query 2: sign_lookup

- **Latency:** 0.0011 ms
- **Sign ID:** 122
- **Cluster ID:** 65
- **Cluster size:** 3
- **Members:** [122, 219, 251]
- **Dominant set:** set_01
- **Dominant graph:** stroke

### Query 3: sign_lookup

- **Latency:** 0.0011 ms
- **Sign ID:** 385
- **Cluster ID:** 38
- **Cluster size:** 10
- **Members:** [65, 230, 253, 311, 337, 338, 359, 368, 385, 418]
- **Dominant set:** set_63
- **Dominant graph:** U-shape

### Query 4: sign_lookup

- **Latency:** 0.0006 ms
- **Sign ID:** 86
- **Cluster ID:** 2
- **Cluster size:** 20
- **Members:** [10, 18, 41, 56, 61, 76, 79, 81, 84, 86, 92, 180, 186, 247, 279, 324, 390, 391, 406, 412]
- **Dominant set:** set_04
- **Dominant graph:** human

### Query 5: sign_lookup

- **Latency:** 0.0009 ms
- **Sign ID:** 50
- **Cluster ID:** 26
- **Cluster size:** 5
- **Members:** [17, 26, 50, 317, 351]
- **Dominant set:** set_04
- **Dominant graph:** human

### Query 6: sequence_search

- **Latency:** 0.0451 ms
- **Query cluster sequence:** [65 38]
- **Matches:** 29
  - **M-7A** (unicorn I seal): [2 19 36 2 35 10 35 69 19 65 38]
  - **M-14A** (unicorn II seal): [2 3 3 65 38]
  - **M-15A** (unicorn II seal): [15 2 59 65 38]
  - **M-19A** (unicorn II seal): [-1 65 38]
  - **M-20A** (unicorn II seal): [2 37 65 38 15 15 45 47]
  - ... and 24 more

### Query 7: sequence_search

- **Latency:** 0.0190 ms
- **Query cluster sequence:** [2 16]
- **Matches:** 14
  - **M-21A** (unicorn II seal): [7 29 2 16 33 57 65 38]
  - **M-28A** (unicorn II seal): [-1 56 2 16 20 -1 65 38]
  - **M-30A** (unicorn II seal): [2 16 28 3 19 19 63]
  - **M-36A** (unicorn III seal): [2 16 12 26 57 65 5 40 44]
  - **M-44A** (unicorn III seal): [2 16 15 40 63 65 35 68]
  - ... and 9 more

### Query 8: sequence_search

- **Latency:** 0.0135 ms
- **Query cluster sequence:** [15 40]
- **Matches:** 10
  - **M-4A** (unicorn I seal): [4 2 15 40 2 65 44 39 39 15]
  - **M-44A** (unicorn III seal): [2 16 15 40 63 65 35 68]
  - **M-50A** (unicorn III seal): [2 17 28 15 40 19 38 65 -1]
  - **M-54A** (unicorn III seal): [3 19 15 40 38 65 57]
  - **M-64A** (unicorn III seal): [11 15 40 39 26 13]
  - ... and 5 more

### Query 9: subsequence_search

- **Latency:** 0.0153 ms
- **Query cluster sequence:** [26 57 65]
- **Matches:** 7
  - **M-36A** (unicorn III seal): [2 16 12 26 57 65 5 40 44]
  - **M-38A** (unicorn III seal): [2 33 35 13 26 57 19 19 65 2 45 12 57]
  - **M-49A** (unicorn III seal): [-1 38 19 26 57 65 4 7 57 2]
  - **M-91A** (unicorn IV seal): [2 10 38 26 57 65 38 13 -1]
  - **M-117A** (unicorn IV seal): [11 15 40 26 63 57 65 57]
  - ... and 2 more

### Query 10: subsequence_search

- **Latency:** 0.0068 ms
- **Query cluster sequence:** [11 15 40]
- **Matches:** 5
  - **M-64A** (unicorn III seal): [11 15 40 39 26 13]
  - **M-86A** (unicorn IV seal): [11 15 40 2 65 57 37]
  - **M-117A** (unicorn IV seal): [11 15 40 26 63 57 65 57]
  - **M-122A** (unicorn IV seal): [11 15 40]
  - **M-135A** (unicorn IV seal): [11 15 40 57]

## C3: Interpretation

The search-without-decode demo confirms that 70 morphological clusters derived from pixel-native features compress the Indus sign inventory by **5.9x**, enabling pattern queries over the corpus without requiring decipherment. Cluster-level bigram and trigram searches identify structurally related inscriptions at sub-millisecond latency.
