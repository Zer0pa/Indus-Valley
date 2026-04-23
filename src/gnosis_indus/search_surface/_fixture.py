"""One-call helper to load the bundled Phase 4 Track C demo fixture.

The fixture lives at `artifacts/phase4/indus_catalogue_demo_fixture.json`,
relative to the repository root. It is a small, authority-anchored
catalogue snapshot built strictly from data enumerated in
`authority/review_pack/search_demo_summary.md` — NOT the real full
catalogue (which stays FETCH_EXTERNAL per `DATA_POLICY.md`).
"""

from __future__ import annotations

from pathlib import Path

from .engine import SearchEngine

# Demo-fixture path relative to the repository root. We walk up from this
# module to find the repo root (the directory that contains both `src/`
# and `artifacts/`).
_FIXTURE_RELPATH = Path("artifacts") / "phase4" / "indus_catalogue_demo_fixture.json"


def _find_repo_root(start: Path) -> Path:
    """Walk up from `start` to find the directory holding both `src/` and `artifacts/`."""
    for parent in (start, *start.parents):
        if (parent / "src").is_dir() and (parent / "artifacts").is_dir():
            return parent
    raise FileNotFoundError(
        f"Could not locate gnosis-indus repo root from {start!s}; "
        f"expected a parent directory containing both `src/` and `artifacts/`."
    )


def demo_fixture_path() -> Path:
    """Return the absolute path to the bundled demo-fixture JSON."""
    here = Path(__file__).resolve()
    root = _find_repo_root(here)
    return root / _FIXTURE_RELPATH


def load_demo_fixture() -> SearchEngine:
    """Load the bundled Phase 4 Track C demo fixture into a SearchEngine.

    The fixture is a small authority-anchored catalogue snapshot. The
    real full catalogue (412 signs, 70 clusters, 179 inscriptions) is
    NOT bundled and is FETCH_EXTERNAL per `DATA_POLICY.md`. Phase 4
    morphology is admitted CONDITIONALLY at k=70 with a stability
    caveat — see `authority/review_pack/phase4_governing_verdict.md`.
    """
    return SearchEngine.from_catalogue(demo_fixture_path())
