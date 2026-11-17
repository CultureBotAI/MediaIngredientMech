#!/usr/bin/env python3
"""Package/replay an isolated reviewed intake, #1453, 2026-11-17.

Inputs: clean pinned consumer commit, frozen intake/review/output and supplements.
Output: new local self-contained directory with exact file manifest and native QC.
No network, installation, campaign mutation or canonical release publication.
Run with PYTHONPATH=src from the consumer checkout; verification also needs the
externally retained package.json SHA256. Native verify uses packaged owner bytes.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

# The actual extracted CLI must not alter its own pinned inventory (#1538).
sys.dont_write_bytecode = True
from mediaingredientmech.intake import culturemech as native  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def inventory(directory):
    result = {}
    for path in sorted(directory.rglob("*")):
        name = path.relative_to(directory).as_posix()
        if path.is_symlink():
            native.require(path.resolve().is_relative_to(directory.resolve()), "Escaping symlink")
            result[name] = {"symlink": os.readlink(path)}
        elif path.is_file():
            result[name] = native.fingerprint(path)
        else:
            native.require(path.is_dir(), "Nonregular package member")
    return result


def copy_exact(source, destination):
    """Never replace a tracked archive member with differing ignored evidence."""
    native.require(not source.is_symlink(), "Supplement must not be a symlink")
    if source.is_dir():
        native.require(not destination.is_symlink(), "Destination is a symlink")
        destination.mkdir(parents=True, exist_ok=True)
        for child in sorted(source.iterdir()):
            copy_exact(child, destination / child.name)
    else:
        expected = native.fingerprint(source)
        if destination.exists() or destination.is_symlink():
            native.require(native.fingerprint(destination) == expected, "Archive/copy collision")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        native.require(native.fingerprint(destination) == expected, "Copy differs from source")


def replay(package, value):
    consumer = package / "consumer"
    return native.verify_reviewed(
        native.relative(consumer, value["intake_path"]),
        value["intake_sha256"],
        value["review_path"],
        native.relative(consumer, value["reviewed_path"]),
        value["reviewed_sha256"],
        root=consumer,
    )


def verify(package, pin):
    value, expected = native.read_json(package / "package.json", pin)
    actual = inventory(package)
    native.require(actual.pop("package.json") == expected, "Package receipt changed")
    native.require(actual == value["files"], "Package file membership/bytes changed")
    result = replay(package, value)
    native.require(
        inventory(package) == {**value["files"], "package.json": expected}, "Package drift"
    )
    return result


def build(args):
    root, output = ROOT.resolve(), args.output.resolve()
    sources = [
        args.intake.resolve(),
        args.reviewed.resolve(),
        *[p.resolve() for p in args.supplement],
    ]
    review = native.relative(root, args.review)
    native.output_preflight(
        output, [*sources, review, root / "data", root / "mappings", root / "reports"]
    )
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    native.require(commit == args.consumer_commit, "Consumer HEAD differs from requested commit")
    subprocess.run(
        ["git", "diff", "--exit-code", commit, "--"],
        cwd=root,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    native.verify_reviewed(
        args.intake, args.intake_sha256, args.review, args.reviewed, args.reviewed_sha256, root=root
    )
    review_value, _ = native.read_json(review)
    sources += [review, *[native.relative(root, name) for name in review_value["inputs"]]]
    # Every source is repository-relative and its entire membership is pinned.
    snapshots = {}
    for source in sources:
        rel = source.relative_to(root).as_posix()
        snapshots[rel] = inventory(source) if source.is_dir() else native.fingerprint(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with native.staging(output) as stage:
        archive = stage / "consumer-source.tar.gz"
        subprocess.run(
            ["git", "archive", "--format=tar.gz", "--output", str(archive), commit],
            cwd=root,
            check=True,
        )
        consumer = stage / "consumer"
        consumer.mkdir()
        with tarfile.open(archive) as stream:
            stream.extractall(consumer, filter="data")
        for source in sources:
            copy_exact(source, consumer / source.relative_to(root))
        value = {
            "schema_version": 1,
            "status": "ISOLATED_REVIEWED_INTAKE_VERIFICATION_PACKAGE",
            "consumer_commit": commit,
            "intake_path": args.intake.resolve().relative_to(root).as_posix(),
            "intake_sha256": args.intake_sha256,
            "review_path": args.review,
            "reviewed_path": args.reviewed.resolve().relative_to(root).as_posix(),
            "reviewed_sha256": args.reviewed_sha256,
            "limitations": "Separate source intake only; no active campaign adoption, new global SSSOM publication, source correction or KGM installation. Native review provenance history is recorded in its immutable review files; this source archive has no Git object database.",
        }
        native.write_json(stage / "native-verification.json", replay(stage, value))
        for source in sources:
            observed = inventory(source) if source.is_dir() else native.fingerprint(source)
            native.require(
                observed == snapshots[source.relative_to(root).as_posix()],
                "Source drift during packaging",
            )
        native.require(
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            == commit,
            "Consumer HEAD drift",
        )
        subprocess.run(
            ["git", "diff", "--exit-code", commit, "--"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        value["files"] = inventory(stage)
        native.write_json(stage / "package.json", value)
    return native.fingerprint(output / "package.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    make = commands.add_parser("build")
    make.add_argument("--consumer-commit", required=True)
    make.add_argument("--intake", type=Path, required=True)
    make.add_argument("--intake-sha256", required=True)
    make.add_argument("--review", required=True)
    make.add_argument("--reviewed", type=Path, required=True)
    make.add_argument("--reviewed-sha256", required=True)
    make.add_argument("--supplement", type=Path, action="append", default=[])
    make.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("verify")
    check.add_argument("--package", type=Path, required=True)
    check.add_argument("--expected-package-sha256", required=True)
    args = parser.parse_args()
    result = (
        build(args)
        if args.command == "build"
        else verify(args.package, args.expected_package_sha256)
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
