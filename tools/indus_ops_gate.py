#!/usr/bin/env python3
"""Indus operational gate for source-boundary and public-surface coherence.

This is the Indus lane profile for the Gnosis Ops-Gates adoption wave. It is
kept repo-local so CI can enforce the lane contract without needing a private
cross-repository token. The gate deliberately checks the surfaces Ops-Gates is
meant to make load-bearing for this lane:

- required repo/doc/runtime surfaces exist;
- private provenance and root TODO drift are gone;
- rights-gated image/corpus families are not vendored;
- concrete local paths, endpoints, and secret-shaped tokens do not leak;
- the current docs do not regress to pre-Phase-02 or owner-deferred-license
  framing.

Symbolic placeholders such as ``<MONOREPO_ROOT>`` and ``<RUNPOD_POD>`` are
allowed; concrete decoded paths are not.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "TRADEMARKS.md",
    "THIRD_PARTY_NOTICES.md",
    "DATA_POLICY.md",
    "SOURCE_BOUNDARY.md",
    "HF_CUSTODY_REGISTER.md",
    "AUTHORITY_SNAPSHOT.md",
    "AUDITOR_PLAYBOOK.md",
    "PUBLIC_AUDIT_LIMITS.md",
    "ROADMAP.md",
    "RELEASING.md",
    "GOVERNANCE.md",
    "docs/ARCHITECTURE.md",
    "docs/FAQ.md",
    "docs/LEGAL_BOUNDARIES.md",
    "docs/SUPPORT.md",
    "docs/family/INDUS_EXPORT_CONTRACT.md",
    "code/README.md",
    "pyproject.toml",
    ".github/workflows/ci.yml",
    ".gpd/STATE.md",
    ".gpd/ROADMAP.md",
    ".gpd/DECISIONS.md",
    "src/gnosis_indus/search_surface/__init__.py",
    "src/gnosis_indus/search_surface/catalogue.py",
    "src/gnosis_indus/search_surface/engine.py",
    "tests/test_search_surface.py",
    "artifacts/phase4/indus_catalogue_demo_fixture.json",
]

FORBIDDEN_ROOT_PATHS = [
    "PRIVATE_PROVENANCE_APPENDIX.md",
    "TODO.md",
]

FORBIDDEN_FILE_SUFFIXES = {
    ".tif",
    ".tiff",
    ".pt",
    ".pth",
    ".onnx",
    ".safetensors",
    ".parquet",
    ".feather",
    ".h5",
    ".hdf5",
    ".pkl",
    ".pickle",
}

LEAK_PATTERNS = [
    (re.compile(r"/Users/"), "concrete macOS user path"),
    (re.compile(r"(?<!<MONOREPO_ROOT>)/workspace/[A-Za-z0-9_.-]+"), "concrete workspace path"),
    (re.compile(r"\bssh\s+-i\s"), "ssh identity-file invocation"),
    (re.compile(r"\bid_(?:ed25519|rsa|ecdsa|dsa|xmss)(?:_sk)?\b"), "private-key filename"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access-key-id shape"),
    (re.compile(r"\bxox[abp]-[A-Za-z0-9-]+"), "Slack token shape"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "OpenAI-like API token shape"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "embedded private key"),
]

STALE_TEXT = {
    "AUTHORITY_SNAPSHOT.md": [
        "owner-deferred release metadata such as final license and contact",
    ],
    "AGENTS.md": [
        "`MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`, and `DATA_POLICY.md`",
        "is the future runtime package root",
    ],
    "PRD_GNOSIS_INDUS_ANCHOR_APPLICATION.md": [
        "controlling license posture until legal decides",
    ],
    "PUBLIC_AUDIT_LIMITS.md": [
        "`OWNER_DEFERRED`",
    ],
    "CONTRIBUTING.md": [
        "`OWNER_DEFERRED`",
    ],
    "RELEASING.md": [
        "License identity: `OWNER_DEFERRED`",
        "once runtime extraction starts",
    ],
    "docs/FAQ.md": [
        "The final public license",
        "the first clean extracted runtime slice are still unresolved",
    ],
    "docs/ARCHITECTURE.md": [
        "later extracted modules",
        "currently minimal",
        "the repo does not yet carry a real extracted runtime beyond the starter package",
    ],
    "code/README.md": [
        "starter namespace for future extracted runtime code",
        "the first real extracted runtime slice is not present yet",
        "Migration plan | staged extraction planning | `MIGRATION_PLAN.md`",
    ],
    ".gpd/STATE.md": [
        "owner-deferred license/contact",
        "final license and public contact",
        "replace `OWNER_DEFERRED` license text",
    ],
}

REQUIRED_TEXT = {
    "README.md": [
        "Apache License 2.0",
        "CC-BY-4.0",
        "BLOCKED_RIGHTS",
        "FETCH_EXTERNAL",
        "We do not claim decipherment",
    ],
    "DATA_POLICY.md": [
        "Architect-Prime/gnosis-indus-artifacts",
        "BLOCKED_RIGHTS",
        "FETCH_EXTERNAL",
        "<RUNPOD_WORKSPACE>",
    ],
    "AUDITOR_PLAYBOOK.md": [
        "Last reviewed:",
        "pytest -q",
        "Ops-Gates",
    ],
}

LEAK_SCAN_SKIP_DIRS = {
    "authority",  # exact-source authority copies intentionally retain symbolic provenance placeholders
    "_internal",  # historical orchestration material, not the public/front-door operating surface
}


def git_tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git ls-files failed")
    return [root / line for line in result.stdout.splitlines() if line.strip()]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_required_paths(root: Path, failures: list[str]) -> None:
    for relpath in REQUIRED_PATHS:
        if not (root / relpath).exists():
            failures.append(f"required path missing: {relpath}")
    for relpath in FORBIDDEN_ROOT_PATHS:
        if (root / relpath).exists():
            failures.append(f"drift path must not exist at root: {relpath}")


def check_rights_gated_files(root: Path, tracked: list[Path], failures: list[str]) -> None:
    for path in tracked:
        relpath = path.relative_to(root).as_posix()
        if path.suffix.lower() in FORBIDDEN_FILE_SUFFIXES:
            failures.append(f"rights/heavy artifact should not be tracked: {relpath}")
        if relpath.startswith("artifacts/") and relpath not in {
            "artifacts/phase4/README.md",
            "artifacts/phase4/indus_catalogue_demo_fixture.json",
        }:
            failures.append(f"unexpected tracked artifact outside admitted fixture: {relpath}")


def check_text_contracts(root: Path, failures: list[str]) -> None:
    for relpath, snippets in REQUIRED_TEXT.items():
        text = read_text(root / relpath)
        for snippet in snippets:
            if snippet not in text:
                failures.append(f"{relpath}: required text missing: {snippet!r}")
    for relpath, snippets in STALE_TEXT.items():
        text = read_text(root / relpath)
        for snippet in snippets:
            if snippet in text:
                failures.append(f"{relpath}: stale text remains: {snippet!r}")


def check_operational_leaks(root: Path, tracked: list[Path], failures: list[str]) -> None:
    for path in tracked:
        rel_parts = path.relative_to(root).parts
        if rel_parts and rel_parts[0] in LEAK_SCAN_SKIP_DIRS:
            continue
        if path.suffix.lower() not in {".md", ".py", ".toml", ".yml", ".yaml", ".json", ".cff", ""}:
            continue
        relpath = path.relative_to(root).as_posix()
        text = read_text(path)
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern, label in LEAK_PATTERNS:
                match = pattern.search(line)
                if match is not None:
                    failures.append(
                        f"{relpath}:{line_no}: {label}: {match.group(0)!r}"
                    )


def run_gate(root: Path) -> dict[str, object]:
    failures: list[str] = []
    tracked = git_tracked_files(root)
    check_required_paths(root, failures)
    check_rights_gated_files(root, tracked, failures)
    check_text_contracts(root, failures)
    check_operational_leaks(root, tracked, failures)
    return {
        "ok": not failures,
        "failures": failures,
        "tracked_files_checked": len(tracked),
        "gate": "indus-ops-gate",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root. Defaults to cwd.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON result.")
    args = parser.parse_args(argv)
    result = run_gate(Path(args.root).resolve())
    print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
