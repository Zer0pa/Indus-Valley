"""gnosis-indus search-without-decode application surface.

Clean-room reimplementation of the Phase 4 Track C search-without-decode
demo, anchored to the admitted authority document
`authority/review_pack/search_demo_summary.md`.

Caveats (must remain visible):

- **k=70 conditional caveat.** The Indus sign catalogue is admitted with
  a stability caveat — see
  `authority/review_pack/phase4_governing_verdict.md`.
- **Non-decipherment posture.** Cluster IDs are morphological groupings
  only. They do NOT encode meaning. Phase 5
  (`authority/review_pack/phase5_governing_verdict.md`) leaves substrate
  identification indistinguishable.
- **Demo fixture vs full catalogue.** The bundled demo fixture is small
  and authority-anchored; the real full catalogue (412 signs, 70
  clusters, 179 inscriptions) is FETCH_EXTERNAL per `DATA_POLICY.md`.
"""

from .catalogue import Catalogue, Cluster, Inscription
from .engine import SearchEngine, SequenceSearchResult, SignLookupResult
from ._fixture import demo_fixture_path, load_demo_fixture

__all__ = [
    "Catalogue",
    "Cluster",
    "Inscription",
    "SearchEngine",
    "SequenceSearchResult",
    "SignLookupResult",
    "demo_fixture_path",
    "load_demo_fixture",
]
