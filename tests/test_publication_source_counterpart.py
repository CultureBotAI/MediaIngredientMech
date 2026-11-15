"""Exact executable qualification is separate from native endpoint approval (#1423)."""

import shutil

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import curation_successor_producer as loader
from mediaingredientmech.curate import stable_sssom_publication as publication
from tests.test_stable_id_adoption import ROOT, commit, initialize


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
