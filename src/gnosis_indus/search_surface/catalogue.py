"""Catalogue loader for the Phase 4 Track C search-without-decode demo fixture.

This module is part of the gnosis-indus anchor application. It is anchored
to the admitted Phase 4 Track C authority document
(`authority/review_pack/search_demo_summary.md`).

Caveats carried forward (must remain visible to all consumers):

- **k=70 conditional caveat.** The Indus sign catalogue is admitted with a
  stability caveat — see `authority/review_pack/phase4_governing_verdict.md`.
- **Non-decipherment posture.** Cluster IDs are morphological groupings
  only. They do NOT encode meaning. Phase 5
  (`authority/review_pack/phase5_governing_verdict.md`) leaves substrate
  identification indistinguishable.
- **Demo fixture vs full catalogue.** The shipped fixture is a small
  authority-anchored demo. The real full catalogue (412 signs, 70
  clusters, 179 inscriptions) is FETCH_EXTERNAL per `DATA_POLICY.md`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Cluster:
    """A morphological cluster.

    Cluster IDs are morphological groupings only and do NOT encode
    meaning (non-decipherment posture; see
    `authority/review_pack/phase5_governing_verdict.md`).
    """

    cluster_id: int
    size: int
    members: tuple[int, ...]
    dominant_set: str
    dominant_graph: str


@dataclass(frozen=True)
class Inscription:
    """An inscription's raw and clustered token sequences.

    `raw` may be `None` for inscriptions the authority doc enumerates only
    by cluster sequence (e.g. inside query 6/7/8/9/10 result blocks).
    `cluster` may contain `-1` to mark unmapped tokens, exactly as the
    authority doc renders them. Consumers must not silently drop or
    remap them.
    """

    inscription_id: str
    cluster: tuple[int, ...]
    raw: tuple[int, ...] | None = None
    label: str | None = None


@dataclass(frozen=True)
class Catalogue:
    """An authority-anchored catalogue snapshot.

    The shipped demo fixture is built strictly from data enumerated in
    `authority/review_pack/search_demo_summary.md`. It is NOT the full
    k=70 catalogue (412 signs, 70 clusters, 179 inscriptions); the full
    catalogue is FETCH_EXTERNAL per `DATA_POLICY.md`. Phase 4 morphology
    is admitted CONDITIONALLY at k=70 with a stability caveat — see
    `authority/review_pack/phase4_governing_verdict.md`.
    """

    k: int
    n_signs_full: int
    n_clusters_full: int
    n_inscriptions_full: int
    clusters: Mapping[int, Cluster]
    inscriptions: Mapping[str, Inscription]
    sign_to_cluster: Mapping[int, int] = field(repr=False)
    source_authority: str = ""
    caveat: str = ""
    non_decipherment: str = ""

    @classmethod
    def from_json(cls, path: str | Path) -> "Catalogue":
        """Load a catalogue from a JSON file matching the demo-fixture schema.

        See `artifacts/phase4/indus_catalogue_demo_fixture.json` for the
        canonical schema. The loader is strict about cluster IDs (they
        must parse as int) and preserves `-1` cluster tokens exactly.
        """
        path = Path(path)
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: Mapping[str, object]) -> "Catalogue":
        """Build a Catalogue from a parsed JSON dict."""
        clusters_raw = data.get("clusters") or {}
        if not isinstance(clusters_raw, Mapping):
            raise ValueError("`clusters` must be a mapping of cluster_id -> record")

        clusters: dict[int, Cluster] = {}
        sign_to_cluster: dict[int, int] = {}
        for cid_str, record in clusters_raw.items():
            cid = int(cid_str)
            if not isinstance(record, Mapping):
                raise ValueError(f"Cluster {cid_str} record must be a mapping")
            members = tuple(int(m) for m in record.get("members", ()))
            cluster = Cluster(
                cluster_id=cid,
                size=int(record.get("size", len(members))),
                members=members,
                dominant_set=str(record.get("dominant_set", "")),
                dominant_graph=str(record.get("dominant_graph", "")),
            )
            clusters[cid] = cluster
            for sign_id in members:
                sign_to_cluster[sign_id] = cid

        inscriptions: dict[str, Inscription] = {}
        full_block = data.get("inscriptions") or {}
        if isinstance(full_block, Mapping):
            for ins_id, record in full_block.items():
                if ins_id.startswith("$"):
                    continue
                if not isinstance(record, Mapping):
                    raise ValueError(f"Inscription {ins_id} record must be a mapping")
                cluster_seq = tuple(int(t) for t in record.get("cluster", ()))
                raw_seq_raw = record.get("raw")
                raw_seq: tuple[int, ...] | None
                if raw_seq_raw is None:
                    raw_seq = None
                else:
                    raw_seq = tuple(int(t) for t in raw_seq_raw)
                label = record.get("label")
                inscriptions[ins_id] = Inscription(
                    inscription_id=ins_id,
                    cluster=cluster_seq,
                    raw=raw_seq,
                    label=str(label) if label is not None else None,
                )

        partial_block = data.get("inscriptions_partial") or {}
        if isinstance(partial_block, Mapping):
            for ins_id, record in partial_block.items():
                if ins_id.startswith("$"):
                    continue
                if not isinstance(record, Mapping):
                    raise ValueError(f"Partial inscription {ins_id} record must be a mapping")
                cluster_seq = tuple(int(t) for t in record.get("cluster", ()))
                label = record.get("label")
                if ins_id in inscriptions:
                    raise ValueError(
                        f"Inscription {ins_id} appears in both `inscriptions` and "
                        f"`inscriptions_partial`; the fixture must list it in only one."
                    )
                inscriptions[ins_id] = Inscription(
                    inscription_id=ins_id,
                    cluster=cluster_seq,
                    raw=None,
                    label=str(label) if label is not None else None,
                )

        return cls(
            k=int(data.get("k", 0)),
            n_signs_full=int(data.get("n_signs_full", 0)),
            n_clusters_full=int(data.get("n_clusters_full", 0)),
            n_inscriptions_full=int(data.get("n_inscriptions_full", 0)),
            clusters=clusters,
            inscriptions=inscriptions,
            sign_to_cluster=sign_to_cluster,
            source_authority=str(data.get("$source_authority", "")),
            caveat=str(data.get("$caveat", "")),
            non_decipherment=str(data.get("$non_decipherment", "")),
        )

    def cluster_of(self, sign_id: int) -> int | None:
        """Return the cluster ID containing `sign_id`, or None if unmapped."""
        return self.sign_to_cluster.get(sign_id)

    def inscription_ids(self) -> Sequence[str]:
        """Return the (sorted) list of inscription IDs in the catalogue."""
        return sorted(self.inscriptions)
