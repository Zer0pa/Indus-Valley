"""Stronger smoke path for the gnosis-indus search_surface package.

Asserts the four acceptance tests declared in
`.gpd/phases/02-extraction-and-minimal-replay-surface/02-01-PLAN.md`:

- test-api-shape: SearchEngine exposes the documented API and return shapes.
- test-query-reproduction: queries 1, 2, 3, 6, 9, 10 from the authority
  doc reproduce on the demo fixture, modulo "... and N more" truncation.
- test-latency-gate: median sequence_search([65, 38]) latency over 5
  runs is < 100 ms on the fixture.
- test-caveat-visibility: package surface carries forward the three
  required caveats (k=70 conditional, non-decipherment, demo-fixture vs
  full-catalogue).
"""

from __future__ import annotations

import time
from pathlib import Path

import pytest

from gnosis_indus import search_surface
from gnosis_indus.search_surface import (
    Catalogue,
    SearchEngine,
    SequenceSearchResult,
    SignLookupResult,
    load_demo_fixture,
)


# ---------------------------------------------------------------------------
# fixtures


@pytest.fixture(scope="module")
def engine() -> SearchEngine:
    return load_demo_fixture()


# ---------------------------------------------------------------------------
# test-api-shape


def test_api_shape_engine_attributes(engine: SearchEngine) -> None:
    """SearchEngine exposes sign_lookup, sequence_search, subsequence_search."""
    assert hasattr(engine, "sign_lookup")
    assert hasattr(engine, "sequence_search")
    assert hasattr(engine, "subsequence_search")
    assert isinstance(engine.catalogue, Catalogue)


def test_api_shape_sign_lookup_returns_documented_fields(engine: SearchEngine) -> None:
    """sign_lookup return value carries the doc's fields."""
    result = engine.sign_lookup(324)
    assert isinstance(result, SignLookupResult)
    # The doc enumerates: cluster_id, cluster_size, members,
    # dominant_set, dominant_graph.
    assert isinstance(result.cluster_id, int)
    assert isinstance(result.cluster_size, int)
    assert isinstance(result.members, tuple)
    assert all(isinstance(m, int) for m in result.members)
    assert isinstance(result.dominant_set, str) and result.dominant_set
    assert isinstance(result.dominant_graph, str) and result.dominant_graph


def test_api_shape_sequence_search_returns_documented_fields(engine: SearchEngine) -> None:
    """sequence_search returns SequenceSearchResult with a list of (id, label, cluster_seq)."""
    result = engine.sequence_search([65, 38])
    assert isinstance(result, SequenceSearchResult)
    assert isinstance(result.matches, tuple)
    assert isinstance(result.match_count, int)
    for ins_id, label, cluster_seq in result.matches:
        assert isinstance(ins_id, str) and ins_id
        assert label is None or isinstance(label, str)
        assert isinstance(cluster_seq, tuple)
        assert all(isinstance(t, int) for t in cluster_seq)


def test_api_shape_subsequence_search_returns_same_shape(engine: SearchEngine) -> None:
    """subsequence_search returns the same SequenceSearchResult shape as sequence_search."""
    result = engine.subsequence_search([26, 57, 65])
    assert isinstance(result, SequenceSearchResult)
    assert isinstance(result.matches, tuple)
    for ins_id, label, cluster_seq in result.matches:
        assert isinstance(ins_id, str) and ins_id
        assert label is None or isinstance(label, str)
        assert isinstance(cluster_seq, tuple)


# ---------------------------------------------------------------------------
# test-query-reproduction


# Query 1: sign_lookup(324) -> cluster 2, size 20, set_04, human
def test_query1_sign_lookup_324(engine: SearchEngine) -> None:
    r = engine.sign_lookup(324)
    assert r.cluster_id == 2
    assert r.cluster_size == 20
    assert r.dominant_set == "set_04"
    assert r.dominant_graph == "human"
    assert r.members == (
        10, 18, 41, 56, 61, 76, 79, 81, 84, 86,
        92, 180, 186, 247, 279, 324, 390, 391, 406, 412,
    )


# Query 2: sign_lookup(122) -> cluster 65, size 3, set_01, stroke
def test_query2_sign_lookup_122(engine: SearchEngine) -> None:
    r = engine.sign_lookup(122)
    assert r.cluster_id == 65
    assert r.cluster_size == 3
    assert r.dominant_set == "set_01"
    assert r.dominant_graph == "stroke"
    assert r.members == (122, 219, 251)


# Query 3: sign_lookup(385) -> cluster 38, size 10, set_63, U-shape
def test_query3_sign_lookup_385(engine: SearchEngine) -> None:
    r = engine.sign_lookup(385)
    assert r.cluster_id == 38
    assert r.cluster_size == 10
    assert r.dominant_set == "set_63"
    assert r.dominant_graph == "U-shape"
    assert r.members == (65, 230, 253, 311, 337, 338, 359, 368, 385, 418)


# Query 6: sequence_search([65, 38]) -- doc reports 29 matches, but only
# enumerates 5 (M-7A, M-14A, M-15A, M-19A, M-20A). The fixture only knows
# the inscriptions explicitly enumerated in the doc, so the fixture's
# match count will be <= 29. We assert the enumerated 5 are a subset.
def test_query6_sequence_search_65_38_contains_enumerated(engine: SearchEngine) -> None:
    """Query 6 [65 38]: enumerated authority subset is a subset of fixture matches.

    The authority doc reports 29 matches with a "... and 24 more" truncation.
    We only assert containment of the explicitly enumerated subset because
    the fixture cannot see the truncated tail.
    """
    result = engine.sequence_search([65, 38])
    matched_ids = {ins_id for ins_id, _label, _seq in result.matches}
    enumerated = {"M-7A", "M-14A", "M-15A", "M-19A", "M-20A"}
    assert enumerated.issubset(matched_ids), (
        f"Authority-doc query 6 enumerated matches {enumerated - matched_ids} "
        f"are missing from fixture matches {sorted(matched_ids)}."
    )
    # The fixture's match count cannot exceed the authority doc's 29.
    assert result.match_count <= 29


# Query 9: subsequence_search([26, 57, 65]) -- doc reports 7 matches and
# enumerates 5. The fixture happens to contain exactly those 5.
def test_query9_subsequence_search_26_57_65(engine: SearchEngine) -> None:
    result = engine.subsequence_search([26, 57, 65])
    matched_ids = {ins_id for ins_id, _label, _seq in result.matches}
    enumerated = {"M-36A", "M-38A", "M-49A", "M-91A", "M-117A"}
    assert enumerated.issubset(matched_ids), (
        f"Authority-doc query 9 enumerated matches {enumerated - matched_ids} "
        f"are missing from fixture matches {sorted(matched_ids)}."
    )
    assert result.match_count <= 7


# Query 10: subsequence_search([11, 15, 40]) -- doc reports 5 matches
# and enumerates all 5 (no "... and N more" truncation). The fixture
# should reproduce the count exactly.
def test_query10_subsequence_search_11_15_40_full(engine: SearchEngine) -> None:
    """Query 10 [11 15 40] is fully enumerated (5/5) so the fixture must match exactly."""
    result = engine.subsequence_search([11, 15, 40])
    matched_ids = {ins_id for ins_id, _label, _seq in result.matches}
    expected = {"M-64A", "M-86A", "M-117A", "M-122A", "M-135A"}
    assert matched_ids == expected, (
        f"Query 10 fixture mismatch. Expected {expected}, got {sorted(matched_ids)}."
    )
    assert result.match_count == 5


def test_query9_specific_match_traces_non_contiguous(engine: SearchEngine) -> None:
    """Verify the order-preserving non-contiguous-subsequence semantics.

    M-117A cluster sequence is (11, 15, 40, 26, 63, 57, 65, 57). For
    query (26, 57, 65), 26 is at index 3, 57 at index 5, 65 at index 6;
    the 63 between is skipped. This anchors that subsequence_search is
    NOT a contiguous-slice match.
    """
    result = engine.subsequence_search([26, 57, 65])
    found = {ins_id: cluster for ins_id, _label, cluster in result.matches}
    assert "M-117A" in found
    assert found["M-117A"] == (11, 15, 40, 26, 63, 57, 65, 57)
    # And confirm sequence_search does NOT match the same query because
    # 26-57-65 is not a contiguous slice of M-117A's sequence.
    contig = engine.sequence_search([26, 57, 65])
    contig_ids = {ins_id for ins_id, _label, _seq in contig.matches}
    assert "M-117A" not in contig_ids


# ---------------------------------------------------------------------------
# test-latency-gate


def test_latency_gate_sequence_search_under_100ms(engine: SearchEngine) -> None:
    """Median sequence_search([65, 38]) latency over 5 runs is < 100 ms."""
    samples_ms: list[float] = []
    for _ in range(5):
        start = time.perf_counter()
        engine.sequence_search([65, 38])
        end = time.perf_counter()
        samples_ms.append((end - start) * 1000.0)
    samples_ms.sort()
    median_ms = samples_ms[len(samples_ms) // 2]
    assert median_ms < 100.0, (
        f"Phase 4 Track C latency gate violated: median {median_ms:.4f} ms "
        f"over samples {samples_ms} >= 100 ms."
    )


# ---------------------------------------------------------------------------
# test-caveat-visibility


def _gather_package_docstrings() -> str:
    """Collect docstrings from every public attribute on the search_surface package."""
    chunks: list[str] = []
    if search_surface.__doc__:
        chunks.append(search_surface.__doc__)
    for name in search_surface.__all__:
        obj = getattr(search_surface, name)
        if obj.__doc__:
            chunks.append(obj.__doc__)
    return "\n\n".join(chunks).lower()


def test_caveat_visibility_in_package_docstrings() -> None:
    """The package's user-facing docstrings name the three required caveats."""
    haystack = _gather_package_docstrings()
    # k=70 conditional caveat
    assert "k=70" in haystack, "k=70 conditional caveat missing from package docstrings."
    assert "conditional" in haystack, "'conditional' (caveat language) missing."
    # Non-decipherment posture
    assert "decipherment" in haystack, "non-decipherment posture missing."
    # Demo fixture vs full catalogue distinction
    assert (
        "demo fixture" in haystack or "demo-fixture" in haystack
    ), "demo fixture / full catalogue distinction missing."


def test_caveat_visibility_in_fixture_readme() -> None:
    """The artifacts/phase4/README.md carries the same three caveats."""
    here = Path(__file__).resolve()
    repo_root = next(
        p for p in (here, *here.parents) if (p / "src").is_dir() and (p / "artifacts").is_dir()
    )
    readme = (repo_root / "artifacts" / "phase4" / "README.md").read_text(encoding="utf-8").lower()
    assert "k=70" in readme
    assert "conditional" in readme
    assert "decipherment" in readme
    assert "demo fixture" in readme or "demo-fixture" in readme
