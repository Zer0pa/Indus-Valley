"""SearchEngine for the Phase 4 Track C search-without-decode demo fixture.

Anchored to the admitted authority document
`authority/review_pack/search_demo_summary.md`. The three query APIs
(`sign_lookup`, `sequence_search`, `subsequence_search`) reproduce the
ground-truth query records on the demo fixture, modulo the `... and N
more` truncation in the doc.

Caveats carried forward (must remain visible to all consumers):

- **k=70 conditional caveat.** The Indus sign catalogue is admitted with
  a stability caveat — see
  `authority/review_pack/phase4_governing_verdict.md`.
- **Non-decipherment posture.** Cluster IDs are morphological groupings
  only. They do NOT encode meaning. Phase 5
  (`authority/review_pack/phase5_governing_verdict.md`) leaves substrate
  identification indistinguishable.
- **Demo fixture vs full catalogue.** The bundled fixture is small and
  authority-anchored; the real full catalogue stays FETCH_EXTERNAL.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from .catalogue import Catalogue


@dataclass(frozen=True)
class SignLookupResult:
    """Result of `SearchEngine.sign_lookup`.

    Mirrors the fields the authority doc reports for query 1/2/3/4/5
    (sign_lookup) result blocks: cluster_id, cluster_size, members,
    dominant_set, dominant_graph.
    """

    sign_id: int
    cluster_id: int
    cluster_size: int
    members: tuple[int, ...]
    dominant_set: str
    dominant_graph: str


@dataclass(frozen=True)
class SequenceSearchResult:
    """Result of `SearchEngine.sequence_search` or `subsequence_search`.

    `matches` is a list of `(inscription_id, label, cluster_seq)` tuples
    in deterministic, sorted-by-inscription-id order. The authority doc
    lists matches in an arbitrary order; tests compare as sets where
    order does not matter, and as ordered lists only against the
    explicitly enumerated subset.
    """

    query: tuple[int, ...]
    matches: tuple[tuple[str, str | None, tuple[int, ...]], ...]

    @property
    def match_count(self) -> int:
        return len(self.matches)


def _contiguous_match(seq: Sequence[int], query: Sequence[int]) -> bool:
    """True iff `query` appears as a contiguous slice anywhere in `seq`."""
    n, m = len(seq), len(query)
    if m == 0 or m > n:
        return m == 0
    q = list(query)
    for i in range(n - m + 1):
        if list(seq[i : i + m]) == q:
            return True
    return False


def _order_preserving_subsequence_match(seq: Sequence[int], query: Sequence[int]) -> bool:
    """True iff `query` appears as an order-preserving (not necessarily contiguous) subsequence.

    Verified against the authority doc's query 9/10 results: query 9
    `[26, 57, 65]` matches M-117A whose cluster sequence is
    `[11, 15, 40, 26, 63, 57, 65, 57]` — `26` at index 3, `57` at index
    5, `65` at index 6 — non-contiguous (the `63` between is skipped).
    """
    if not query:
        return True
    it = iter(seq)
    return all(any(token == target for token in it) for target in query)


class SearchEngine:
    """In-memory search engine over an authority-anchored Catalogue.

    Wraps a `Catalogue` (see `catalogue.py`) and exposes the three query
    APIs the Phase 4 Track C authority doc enumerates:

    - `sign_lookup(sign_id)` — return the cluster context for a sign id.
    - `sequence_search(query)` — find inscriptions whose cluster sequence
      contains `query` as a contiguous slice. (Matches the authority
      doc's query 6/7/8 result shape.)
    - `subsequence_search(query)` — find inscriptions whose cluster
      sequence contains `query` as an order-preserving (non-contiguous)
      subsequence. (Matches the authority doc's query 9/10 result shape.)

    The Phase 4 catalogue is admitted CONDITIONALLY at k=70 with a
    stability caveat. The demo fixture is a small authority-anchored
    snapshot; the full catalogue stays FETCH_EXTERNAL per
    `DATA_POLICY.md`. Cluster IDs are morphological groupings only and
    do NOT encode meaning (non-decipherment posture).
    """

    def __init__(self, catalogue: Catalogue) -> None:
        self._catalogue = catalogue

    # ------------------------------------------------------------------ ctors

    @classmethod
    def from_catalogue(cls, path: str | Path) -> "SearchEngine":
        """Build a SearchEngine from a catalogue JSON file (fixture schema)."""
        return cls(Catalogue.from_json(path))

    # ----------------------------------------------------------------- access

    @property
    def catalogue(self) -> Catalogue:
        return self._catalogue

    # ------------------------------------------------------------------- API

    def sign_lookup(self, sign_id: int) -> SignLookupResult:
        """Look up the cluster context for `sign_id`.

        Raises `KeyError` if the sign is not in any cluster known to the
        catalogue. The fixture only knows clusters 2/26/38/65 (the four
        that the authority doc enumerates members for); a query for any
        other sign id will raise.
        """
        cid = self._catalogue.cluster_of(sign_id)
        if cid is None:
            raise KeyError(
                f"sign_id {sign_id} is not present in any known cluster of this "
                f"demo-fixture catalogue (only clusters {sorted(self._catalogue.clusters)} "
                f"are enumerated)."
            )
        cluster = self._catalogue.clusters[cid]
        return SignLookupResult(
            sign_id=sign_id,
            cluster_id=cluster.cluster_id,
            cluster_size=cluster.size,
            members=cluster.members,
            dominant_set=cluster.dominant_set,
            dominant_graph=cluster.dominant_graph,
        )

    def sequence_search(self, query: Iterable[int]) -> SequenceSearchResult:
        """Return inscriptions whose cluster sequence contains `query` as a contiguous slice.

        Matches the shape of the authority doc's query 6/7/8 records.
        """
        q = tuple(int(t) for t in query)
        matches: list[tuple[str, str | None, tuple[int, ...]]] = []
        for ins_id in sorted(self._catalogue.inscriptions):
            ins = self._catalogue.inscriptions[ins_id]
            if _contiguous_match(ins.cluster, q):
                matches.append((ins.inscription_id, ins.label, ins.cluster))
        return SequenceSearchResult(query=q, matches=tuple(matches))

    def subsequence_search(self, query: Iterable[int]) -> SequenceSearchResult:
        """Return inscriptions whose cluster sequence contains `query` as an order-preserving subsequence.

        Matches the shape of the authority doc's query 9/10 records.
        """
        q = tuple(int(t) for t in query)
        matches: list[tuple[str, str | None, tuple[int, ...]]] = []
        for ins_id in sorted(self._catalogue.inscriptions):
            ins = self._catalogue.inscriptions[ins_id]
            if _order_preserving_subsequence_match(ins.cluster, q):
                matches.append((ins.inscription_id, ins.label, ins.cluster))
        return SequenceSearchResult(query=q, matches=tuple(matches))
