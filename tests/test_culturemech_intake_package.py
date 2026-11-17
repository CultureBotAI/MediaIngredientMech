"""A portable #1453 package must replay exact native decisions and refuse drift."""

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from mediaingredientmech.intake import culturemech as native
from tests.test_culturemech_binding_review_assembly import author_review
from tests.test_culturemech_binding_review_assembly import helper as assembler
from tests.test_culturemech_intake import handoff, prepared  # noqa: F401
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401

SPEC = importlib.util.spec_from_file_location(
    "intake_package", Path(__file__).parents[1] / "scripts/adhoc/package_culturemech_intake_1453.py"
)
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


@pytest.fixture
def package_args(handoff, monkeypatch):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    author = root / "author.json"
    native.write_json(author, author_review(source, pin))
    review_dir = root / "reports/binding-review"
    assembler.assemble(source, pin, [author], review_dir, root=root)
    review_path = "reports/binding-review/binding-review.json"
    reviewed = root / "reviewed"
    native.finalize(source, pin, review_path, reviewed, root=root)
    implementation = Path(__file__).parents[1]
    shutil.copytree(
        implementation / "src/mediaingredientmech",
        root / "src/mediaingredientmech",
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    (root / "scripts/adhoc").mkdir(parents=True)
    shutil.copyfile(
        implementation / "scripts/adhoc/package_culturemech_intake_1453.py",
        root / "scripts/adhoc/package_culturemech_intake_1453.py",
    )
    subprocess.run(["git", "init", "--quiet", str(root)], check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Synthetic",
            "-c",
            "user.email=synthetic@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Synthetic package fixture",
        ],
        cwd=root,
        check=True,
    )
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    monkeypatch.setattr(helper, "ROOT", root)
    return argparse.Namespace(
        intake=source,
        intake_sha256=pin,
        review=review_path,
        reviewed=reviewed,
        reviewed_sha256=native.fingerprint(reviewed / "reviewed-intake.json")["sha256"],
        consumer_commit=commit,
        supplement=[],
        output=root / "package",
    )


def test_portable_package_replays_native_outputs(package_args):
    receipt = helper.build(package_args)
    result = helper.verify(package_args.output, receipt["sha256"])
    assert result["status"] == "VERIFIED_REVIEWED_SOURCE_INTAKE"
    manifest = json.loads((package_args.output / "package.json").read_text())
    assert manifest["consumer_commit"] == package_args.consumer_commit
    assert (package_args.output / "native-verification.json").is_file()


def test_actual_packaged_cli_does_not_create_unmanifested_bytecode(package_args):
    receipt = helper.build(package_args)
    consumer = package_args.output / "consumer"
    env = dict(os.environ, PYTHONPATH=str(consumer / "src"))
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    result = subprocess.run(
        [
            sys.executable,
            "scripts/adhoc/package_culturemech_intake_1453.py",
            "verify",
            "--package",
            str(package_args.output),
            "--expected-package-sha256",
            receipt["sha256"],
        ],
        cwd=consumer,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["status"] == "VERIFIED_REVIEWED_SOURCE_INTAKE"
    assert not list(consumer.rglob("__pycache__"))


@pytest.mark.parametrize("mutation", ["changed", "omitted", "unexpected"])
def test_transfer_drift_refused_before_replay(package_args, mutation, monkeypatch):
    receipt = helper.build(package_args)
    target = package_args.output / "native-verification.json"
    if mutation == "changed":
        target.write_text("{}\n")
    elif mutation == "omitted":
        target.unlink()
    else:
        (package_args.output / "extra.txt").write_text("unreviewed")
    monkeypatch.setattr(helper, "replay", lambda *_: pytest.fail("Drift reached replay"))
    with pytest.raises(ValueError, match="membership/bytes"):
        helper.verify(package_args.output, receipt["sha256"])


def test_copy_cannot_replace_archive_input_or_follow_external_link(tmp_path):
    source, target = tmp_path / "source", tmp_path / "target"
    source.write_text("reviewed")
    target.write_text("different archive bytes")
    with pytest.raises(ValueError, match="collision"):
        helper.copy_exact(source, target)
    assert target.read_text() == "different archive bytes"
    link = tmp_path / "link"
    link.symlink_to(source)
    with pytest.raises(ValueError, match="symlink"):
        helper.copy_exact(link, tmp_path / "copy")


def test_authoritative_destination_refused_without_writes(package_args):
    package_args.output = helper.ROOT / "data/forbidden-package"
    with pytest.raises(ValueError, match="overlaps"):
        helper.build(package_args)
    assert not package_args.output.exists()
