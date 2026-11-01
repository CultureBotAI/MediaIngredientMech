"""Clean workflow producers must satisfy committed review prerequisites."""

import json
import shlex
import subprocess
from pathlib import Path

import pytest
import yaml

from tests.test_record_review_contract import reviews as reviews
from tests.test_record_review_contract import sample as sample

ROOT = Path(__file__).resolve().parents[1]


def workflow_commands(workflow, job, module):
    steps = yaml.safe_load((ROOT / workflow).read_text())["jobs"][job]["steps"]
    result = []
    for step in steps:
        # Workflow shell continuation lines belong to the same native command.
        script = step.get("run", "").replace("\\\n", "")
        for line in script.splitlines():
            if "-m " + module + " " in line:
                result.append(shlex.split(line))
    return result


def test_committed_semantic_review_uses_workflow_full_graph():
    workflow = ".github/workflows/qc-supported-kgx.yaml"
    producers = workflow_commands(workflow, "supported-graph", "mediaingredientmech.export.kgx")
    assert len(producers) == 1
    producer = producers[0]
    bundle = producer[producer.index("--output") + 1]
    consumers = workflow_commands(
        workflow, "supported-graph", "mediaingredientmech.export.supported_kgx"
    )
    assert consumers
    for command in consumers:
        report_path = command[command.index("--report") + 1]
        report = json.loads((ROOT / report_path).read_text())
        assert report["bundle"] == bundle, "Committed review binds a graph absent from clean CI"
        assert bundle + "/manifest.json" in report["inputs"]


def test_reviewed_sssom_checkout_retains_native_review_history():
    workflow = yaml.safe_load((ROOT / ".github/workflows/qc-reviewed-sssom.yaml").read_text())
    checkouts = [
        step
        for step in workflow["jobs"]["reviewed-sssom"]["steps"]
        if step.get("uses", "").startswith("actions/checkout@")
    ]
    assert len(checkouts) == 1
    assert str(checkouts[0].get("with", {}).get("fetch-depth")) == "0"


def test_native_review_refuses_shallow_missing_base_then_accepts_fetched_base(
    reviews, sample, tmp_path
):
    repository, record = sample

    def git(root, *args):
        return subprocess.check_output(["git", "-C", str(root), *args]).decode().strip()

    path = reviews.save_review(repository, record)
    relative = str(path.relative_to(repository))
    durable_base = record["source"]["git_revision"]
    git(repository, "add", ".")
    git(repository, "commit", "-qm", "Preserve synthetic native review above its durable base")
    head = git(repository, "rev-parse", "HEAD")
    clone = tmp_path / "depth-one"
    subprocess.run(
        ["git", "clone", "--quiet", "--depth", "1", repository.as_uri(), str(clone)],
        check=True,
        capture_output=True,
    )
    assert git(clone, "rev-parse", "--is-shallow-repository") == "true"
    missing = subprocess.run(
        ["git", "-C", str(clone), "cat-file", "-e", durable_base + "^{commit}"],
        capture_output=True,
    )
    assert missing.returncode != 0
    assert reviews.source_provenance(clone, record)["status"] == "unverified"
    with pytest.raises(reviews.ReviewError, match="source provenance unverified"):
        reviews.read_review(clone, relative)
    before = {
        name: (clone / name).read_bytes()
        for name in ("record.yaml", relative, str(Path(relative).with_name("review.md")))
    }
    git(clone, "fetch", "--quiet", "--depth", "1", repository.as_uri(), durable_base)
    assert git(clone, "rev-parse", "HEAD") == head
    assert reviews.source_provenance(clone, record)["status"] == "working_tree_attestation"
    assert reviews.read_review(clone, relative) == record
    assert all((clone / name).read_bytes() == data for name, data in before.items())
