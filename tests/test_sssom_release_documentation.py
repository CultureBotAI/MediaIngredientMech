"""The documented count command follows regenerated manifests (#1110)."""

import json
import shlex
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "counts",
    [{"source": 5, "supported": 3, "withhold": 2}, {"source": 9, "supported": 4, "withhold": 5}],
)
def test_documented_counts_are_read_from_the_generated_manifest(tmp_path, counts):
    guide = Path(__file__).resolve().parents[1] / "docs/SSSOM_RELEASE.md"
    commands = [line for line in guide.read_text().splitlines() if line.startswith("python -c ")]
    assert len(commands) == 1
    args = shlex.split(commands[0])
    assert args[:2] == ["python", "-c"] and len(args) == 3
    manifest = tmp_path / "output/mim-reviewed-sssom/manifest.json"
    manifest.parent.mkdir(parents=True)
    expected = {"source_sha256": "a" * 64, "counts": counts}
    manifest.write_text(json.dumps(expected))
    output = subprocess.check_output([sys.executable, "-c", args[2]], cwd=tmp_path)
    assert json.loads(output) == expected
