"""Exact executable qualification is separate from native endpoint approval (#1423)."""

import shutil
import subprocess

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import curation_successor_producer as loader
from mediaingredientmech.curate import stable_sssom_publication as publication
from tests.test_stable_id_adoption import ROOT, commit, initialize


@pytest.mark.parametrize(
    "revision,expected",
    [
        (
            "13f4f8494a46dbb3b1084652cbf5a030a60f6c03",
            "a5ac25dbdbbbb0fecb88a3d7fb3a0bc338175be98ac09d71ae8e52644c28cd1b",
        ),
        (
            "cf44010e54c4b51ade2c94d2528068039ac15985",
            "d64bb16c03c65566f466bec34fdc89d04d05357d8296c986aa40fe6e9a404798",
        ),
        (
            "f63930804fe143cd0bd4eba0374d9d2be2dd66ba",
            "ed8dcf4328c17fc8e78dab08f357fa53b60bd5c037ca85b3810dc6b3440973c9",
        ),
    ],
)
def test_retained_recorded_source_counterparts_remain_qualified(tmp_path, revision, expected):
    """Use real recorded source, not a claimed old digest on new implementation."""
    root = tmp_path / "historical-source"
    initialize(root)
    for name in successor._CAPTURE.files:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
    raw = subprocess.check_output(
        ["git", "--no-optional-locks", "show", revision + ":" + publication.SOURCE_HANDOFF_SOURCE],
        cwd=ROOT,
    )
    assert successor.native().sha(raw) == expected
    (root / publication.SOURCE_HANDOFF_SOURCE).write_bytes(raw)
    commit(root)
    capture, implementation = loader.load(root, (root / loader.LOADER).read_bytes())
    api = implementation.native()
    producer = capture.receipt(api.Inputs(root))
    assert producer["source_sha256"] == expected
    assert producer["files"] == {name: api.sha(raw) for name, (raw, _) in capture.files.items()}
    guard = object.__new__(publication._SourcePublicationGuard)
    guard.capture, guard.api, guard.producer = capture, api, producer
    guard._implementation()
    producer["runtime"] = {}
    with pytest.raises(ValueError, match="unsupported source handoff"):
        guard._implementation()


@pytest.mark.parametrize(
    "change", [None, "unknown-source", "claimed-old", "omitted-file", "runtime"]
)
def test_counterpart_requires_exact_source_and_complete_native_capture(tmp_path, change):
    root = tmp_path / "source"
    initialize(root)
    for name in successor._CAPTURE.files:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
    source = root / publication.SOURCE_HANDOFF_SOURCE
    if change == "unknown-source":
        source.write_bytes(source.read_bytes() + b"\n# Actual unqualified source revision\n")
    commit(root)
    capture, implementation = loader.load(root, (root / loader.LOADER).read_bytes())
    api = implementation.native()
    producer = capture.receipt(api.Inputs(root))
    assert producer["files"] == {name: api.sha(raw) for name, (raw, _) in capture.files.items()}
    assert producer["runtime"] == capture.runtime
    if change == "claimed-old":
        producer["source_sha256"] = (
            "6b34ede05a681531d07715ea68a847692b90c51f25a0884d6f8a577eecd13766"
        )
    elif change == "omitted-file":
        del producer["files"]["scripts/aggregate_records.py"]
    elif change == "runtime":
        producer["runtime"] = {}
    # Exercise the real closed implementation predicate with genuine captured
    # bytes/receipt. Endpoint/science/lease approval is exercised separately by
    # the full native correction→publication and tracked-handoff regressions.
    guard = object.__new__(publication._SourcePublicationGuard)
    guard.capture, guard.api, guard.producer = capture, api, producer
    if change is None:
        guard._implementation()
        assert producer["source_sha256"] == publication.SOURCE_HANDOFF_SOURCE_SHA
    else:
        with pytest.raises(ValueError, match="unsupported source handoff"):
            guard._implementation()
