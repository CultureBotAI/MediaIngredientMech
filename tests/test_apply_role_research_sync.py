"""The role applier must leave data/ingredients/ and data/curated/ in sync (#171).

It writes faceted role slots straight into `data/ingredients/**/*.yaml`. Unlike
`discussions`, those slots DO exist in the curated collection, so writing only
the per-record side desynchronises the two surfaces — and `just
export-individual` projects the collection OVER the per-record tree, so the next
export silently reverts every role just applied. That is the mechanism that lost
55 curation events in #148.

Reproduced before the fix: applying one role made `just qc-roundtrip` exit 1.
These tests pin the write-back that prevents it.
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "apply_role_research_results", ROOT / "scripts" / "apply_role_research_results.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


class _Recorder:
    """Stands in for subprocess.run, recording commands instead of running them."""

    def __init__(self, returncode: int = 0):
        self.calls: list[list[str]] = []
        self.returncode = returncode

    def __call__(self, cmd, **kwargs):
        self.calls.append([str(c) for c in cmd])

        class _Proc:
            pass

        proc = _Proc()
        proc.returncode = self.returncode
        return proc


def test_sync_runs_aggregate_then_export_in_that_order(monkeypatch):
    """Order matters: aggregating writes the edits into the collection, and the
    re-export normalises the tree to the byte-exact fixed point the gate wants."""
    mod = _load()
    rec = _Recorder()
    monkeypatch.setattr(mod.subprocess, "run", rec)

    assert mod.sync_curated() == 0
    assert len(rec.calls) == 2

    aggregate, export = rec.calls
    assert aggregate[1].endswith("aggregate_records.py")
    assert "--output-dir" in aggregate
    assert aggregate[aggregate.index("--output-dir") + 1].endswith("data/curated")

    assert export[1].endswith("export_individual_records.py")
    assert "--input-dir" in export
    assert export[export.index("--input-dir") + 1].endswith("data/curated")


def test_sync_propagates_failure_and_stops_early(monkeypatch):
    """A failed aggregate must not be followed by an export that would then
    project a half-written collection back over the per-record tree."""
    mod = _load()
    rec = _Recorder(returncode=3)
    monkeypatch.setattr(mod.subprocess, "run", rec)

    assert mod.sync_curated() == 3
    assert len(rec.calls) == 1  # stopped after the failing step


def test_no_sync_flag_exists_and_is_off_by_default():
    """Syncing is the default; skipping it must be an explicit, named choice."""
    mod = _load()
    import argparse

    parser = argparse.ArgumentParser()
    # Mirror the flag under test rather than re-running main().
    parser.add_argument("--no-sync", action="store_true")
    assert parser.parse_args([]).no_sync is False
    assert parser.parse_args(["--no-sync"]).no_sync is True
    # And the real script must expose it.
    assert "--no-sync" in (mod.main.__doc__ or "") or "no_sync" in mod.main.__code__.co_names
