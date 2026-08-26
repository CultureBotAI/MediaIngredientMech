#!/usr/bin/env python3
"""Run claw's evidence validator against the active MIM checkout.

The shared validator predates Git worktree use. It derives both the MIM input
checkout and its report directory from the location of the claw script. Calling
it directly can therefore validate one checkout while the caller is reviewing
another, and writes into the claw checkout as a side effect.

This adapter makes the boundary explicit. It finds the shared validator using,
in order:

1. ``CLAW_ROOT`` (the culturebotai-claw repository root);
2. ``CLAW_SRC`` (the repository's ``src`` directory; legacy override);
3. a ``culturebotai-claw`` sibling of the primary MIM checkout; or
4. a sibling of the active checkout (normal, non-worktree layout).

It then binds all MIM input and output globals to the checkout containing this
file before invoking the shared validator. Reports consequently land under the
active checkout's ``workspace/reports`` directory.
"""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from collections.abc import Mapping
from pathlib import Path
from types import ModuleType

MIM_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_RELATIVE_PATH = Path("scripts/validate_evidence_references.py")


class SharedValidatorNotFound(RuntimeError):
    """Raised when no usable culturebotai-claw validator can be located."""


def _primary_checkout(mim_root: Path) -> Path | None:
    """Return the primary checkout root for a repository or linked worktree."""

    result = subprocess.run(
        [
            "git",
            "-C",
            str(mim_root),
            "rev-parse",
            "--path-format=absolute",
            "--git-common-dir",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    common_dir = Path(result.stdout.strip()).resolve()
    return common_dir.parent


def _override_root(env: Mapping[str, str]) -> tuple[str, Path] | None:
    """Resolve the explicit override without silently ignoring a bad value."""

    if env.get("CLAW_ROOT"):
        return "CLAW_ROOT", Path(env["CLAW_ROOT"]).expanduser().resolve()
    if env.get("CLAW_SRC"):
        source = Path(env["CLAW_SRC"]).expanduser().resolve()
        return "CLAW_SRC", source.parent if source.name == "src" else source
    return None


def resolve_validator(
    mim_root: Path = MIM_ROOT,
    env: Mapping[str, str] | None = None,
) -> Path:
    """Locate the shared validator, with worktree-aware defaults."""

    environment = os.environ if env is None else env
    override = _override_root(environment)
    if override:
        variable, root = override
        candidate = root / VALIDATOR_RELATIVE_PATH
        if candidate.is_file():
            return candidate
        raise SharedValidatorNotFound(
            f"{variable} points to {root}, but {candidate} does not exist. "
            "Set CLAW_ROOT to the culturebotai-claw checkout root (or CLAW_SRC "
            "to its src/ directory)."
        )

    roots: list[Path] = []
    primary = _primary_checkout(mim_root)
    if primary is not None:
        roots.append(primary.parent / "culturebotai-claw")
    roots.append(mim_root.resolve().parent / "culturebotai-claw")

    checked: list[Path] = []
    for root in roots:
        candidate = root / VALIDATOR_RELATIVE_PATH
        if candidate in checked:
            continue
        checked.append(candidate)
        if candidate.is_file():
            return candidate

    locations = ", ".join(str(path) for path in checked) or "no inferred locations"
    raise SharedValidatorNotFound(
        "culturebotai-claw evidence validator not found. Checked: "
        f"{locations}. Set CLAW_ROOT to the culturebotai-claw checkout root "
        "(or CLAW_SRC to its src/ directory)."
    )


def load_validator(path: Path) -> ModuleType:
    """Load the shared script without adding its checkout to ``sys.path``."""

    spec = importlib.util.spec_from_file_location("_mim_shared_evidence_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load shared evidence validator: {path}")
    module = importlib.util.module_from_spec(spec)
    # Dataclasses and similar import-time helpers expect the module to be
    # discoverable while its code executes.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def bind_active_checkout(module: ModuleType, mim_root: Path = MIM_ROOT) -> None:
    """Point the shared validator's input and output globals at ``mim_root``."""

    root = mim_root.resolve()
    report_dir = root / "workspace" / "reports"
    bindings = {
        "REPO_ROOT": root,
        "MIM_ROOT": root,
        "CACHE_DIR": root / "references_cache",
        "INGREDIENTS": root / "data" / "ingredients",
        "OUT_DIR": report_dir,
        "OUT_TSV": report_dir / "evidence_reference_validation.tsv",
        "OUT_MD": report_dir / "evidence_reference_validation.md",
    }
    missing = [name for name in bindings if not hasattr(module, name)]
    if missing:
        raise RuntimeError(
            "shared evidence validator contract changed; missing globals: "
            + ", ".join(missing)
        )
    for name, value in bindings.items():
        setattr(module, name, value)


def run(mim_root: Path = MIM_ROOT, env: Mapping[str, str] | None = None) -> int:
    validator_path = resolve_validator(mim_root, env)
    module = load_validator(validator_path)
    bind_active_checkout(module, mim_root)
    main = getattr(module, "main", None)
    if not callable(main):
        raise RuntimeError(f"shared evidence validator has no callable main(): {validator_path}")
    return int(main())


def main() -> int:
    try:
        return run()
    except SharedValidatorNotFound as exc:
        print(f"qc-evidence: {exc}", file=sys.stderr)
        return 2
    except (ImportError, OSError, RuntimeError) as exc:
        print(f"qc-evidence: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
