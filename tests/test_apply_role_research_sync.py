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


def _batch_with_one_applicable_role(tmp_path: Path) -> tuple[Path, Path]:
    """A record with an empty facet plus a batch that fills it, so main() writes."""
    import json

    import yaml

    rec_dir = tmp_path / "data" / "ingredients" / "mapped"
    rec_dir.mkdir(parents=True)
    rec = rec_dir / "Thing.yaml"
    rec.write_text(yaml.safe_dump({
        "identifier": "CHEBI:1", "preferred_term": "Thing", "mapping_status": "MAPPED",
    }))
    batch = tmp_path / "batch.json"
    batch.write_text(json.dumps({"proposals": [{
        "ingredient_identifier": "CHEBI:1",
        "ingredient_path": str(rec.relative_to(tmp_path)),
        "source_run": "research/ingredients/roles/x-edison-literature.md",
        "role_assignments": {"nutritional_roles": [{"role": "CARBON_SOURCE", "confidence": 0.9}]},
    }]}))
    return batch, rec


def test_real_run_syncs_by_default(tmp_path, monkeypatch):
    """Drives the REAL parser through main(), not a mirrored one: a test that
    rebuilt the flag itself would still pass if --no-sync were renamed or
    defaulted to True."""
    mod = _load()
    batch, _ = _batch_with_one_applicable_role(tmp_path)
    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(mod, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    calls: list[int] = []
    monkeypatch.setattr(mod, "sync_curated", lambda: calls.append(1) or 0)

    assert mod.main([str(batch)]) == 0
    assert calls == [1]


def test_no_sync_flag_suppresses_the_write_back(tmp_path, monkeypatch, capsys):
    mod = _load()
    batch, _ = _batch_with_one_applicable_role(tmp_path)
    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(mod, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    calls: list[int] = []
    monkeypatch.setattr(mod, "sync_curated", lambda: calls.append(1) or 0)

    assert mod.main([str(batch), "--no-sync"]) == 0
    assert calls == []
    # And it must say so loudly — a silent desync is the whole bug.
    assert "out of sync" in capsys.readouterr().out


def test_sync_failure_propagates_out_of_main(tmp_path, monkeypatch):
    """A failed write-back must not report success: the tree is left inconsistent."""
    mod = _load()
    batch, _ = _batch_with_one_applicable_role(tmp_path)
    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(mod, "INGREDIENTS_DIR", tmp_path / "data" / "ingredients")
    monkeypatch.setattr(mod, "sync_curated", lambda: 7)

    assert mod.main([str(batch)]) == 7
