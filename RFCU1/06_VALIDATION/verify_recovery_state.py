#!/usr/bin/env python3
"""Validate the RFCU1 recovery branch without external dependencies."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "01_ARCHITECTURE" / "v3.0_source_gated"
STATE = ROOT / "00_CANONICAL_STATE"
RUNS = ROOT / "04_RUNS"
AUDITS = ROOT / "07_AUDITS"

EXPECTED_ARCHITECTURE_HASHES = {
    "README.md": "1cf3f146160b4e8e1b137887f667253987bc4f623d07e30337ee2bd64f6300d8",
    "RFC_CANONICAL_PROOF_LOCK_v3.0_SOURCE_GATED.md": "a8e73b5f1c7209301d575c5450ea95e0d124c741b7bc6426bc83614dc8bb4060",
    "RFC_DEEP_SOAK_AND_SOURCE_AUDIT_v3.0.md": "b8acdfce1aaaefb8efb4c4b7351f75f1bb7c2671b08ef5cd86970cc488f82f43",
    "RFC_NEW_INTEGRATED_PROOF_MASTER_ARCHITECTURE_v3.0_SOURCE_GATED.md": "74c88b62f919d0464f674a176da030294237039831fc0d2949a8d3ab19241f66",
    "RFC_v3.0_ARCHITECTURE_MANIFEST.json": "69751e5350b6e9c50369fe50c6744d49210ef99739b7770025916e814426887b",
}

REQUIRED_CONTROL_FILES = [
    STATE / "CURRENT_STATE.md",
    STATE / "NEXT_AUTHORIZED_RUN.md",
    STATE / "WORK_ITERATION_RECOVERY_INVENTORY.md",
    RUNS / "MODULE_A_RUN_001_007_LINEAGE.md",
    RUNS / "RUN_007_MODULE_A_EXPORT_AND_TEC" / "RUN_007_CLOSEOUT.md",
    AUDITS / "RECOVERY_COMPLETENESS_MATRIX.md",
    ROOT / "99_QUARANTINE" / "RFCU2_EXCLUSION.md",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def check_dag(modules: dict[str, Any], failures: list[str]) -> None:
    expected = [chr(code) for code in range(ord("A"), ord("Q") + 1)]
    if sorted(modules) != expected:
        fail("manifest must contain exactly modules A through Q", failures)
        return

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            fail(f"dependency cycle detected at module {node}", failures)
            return
        if node in visited:
            return
        visiting.add(node)
        deps = modules[node].get("depends_on", [])
        for dep in deps:
            if dep not in modules:
                fail(f"module {node} names missing dependency {dep}", failures)
                continue
            if dep >= node:
                fail(f"module {node} depends on non-earlier module {dep}", failures)
            visit(dep)
        visiting.remove(node)
        visited.add(node)

    for name in expected:
        visit(name)


def main() -> int:
    failures: list[str] = []

    for path in REQUIRED_CONTROL_FILES:
        if not path.is_file():
            fail(f"missing required control file: {path.relative_to(ROOT)}", failures)

    manifest_path = ARCH / "RFC_v3.0_ARCHITECTURE_MANIFEST.json"
    if not manifest_path.is_file():
        fail("missing v3.0 architecture manifest", failures)
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"architecture manifest is not valid JSON: {exc}", failures)
        else:
            if manifest.get("primitive_triad") != ["CIF", "QV", "RFL"]:
                fail("primitive triad is not ordered CIF, QV, RFL", failures)
            if manifest.get("first_action") != "QV(CIF) -> RFL":
                fail("First Action is not QV(CIF) -> RFL", failures)
            if manifest.get("rfc_u2_is_parent") is not False:
                fail("RFCU2 is not explicitly excluded as a parent", failures)
            if manifest.get("scientific_runs_authorized") is not False:
                fail("source-gated v3.0 manifest improperly authorizes execution", failures)
            modules = manifest.get("modules")
            if not isinstance(modules, dict):
                fail("manifest modules field is missing or invalid", failures)
            else:
                check_dag(modules, failures)

    for name, expected_hash in EXPECTED_ARCHITECTURE_HASHES.items():
        path = ARCH / name
        if not path.is_file():
            fail(f"missing separately readable architecture member: {name}", failures)
            continue
        actual = sha256(path)
        if actual != expected_hash:
            fail(f"hash mismatch for {name}: {actual} != {expected_hash}", failures)

    state_text = (STATE / "CURRENT_STATE.md").read_text(encoding="utf-8") if (STATE / "CURRENT_STATE.md").is_file() else ""
    next_text = (STATE / "NEXT_AUTHORIZED_RUN.md").read_text(encoding="utf-8") if (STATE / "NEXT_AUTHORIZED_RUN.md").is_file() else ""
    registry_text = (RUNS / "README.md").read_text(encoding="utf-8") if (RUNS / "README.md").is_file() else ""

    if "RUN 001" not in registry_text or "RUN 013" not in registry_text:
        fail("run registry does not explicitly span RUN 001 through RUN 013", failures)
    if "RUN 014" not in next_text or "not" not in next_text.lower():
        fail("RUN 014 is not explicitly blocked in next-action control", failures)
    if "QUARANTINED_NOT_A_PARENT" not in state_text:
        fail("current state does not explicitly quarantine RFCU2", failures)

    if failures:
        print(f"RECOVERY_GATE=FAIL ({len(failures)} failures)")
        return 1

    print("RECOVERY_GATE=CLEAN_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
