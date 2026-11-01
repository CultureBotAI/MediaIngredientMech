"""Freeze an explicit completed-evidence selection, then publish exclusively.

No default publication. Draft selections/pending commands cannot be frozen.
Only publish writes the new tracked execution directory. Verify is read-only.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import gzip
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
REPORT = Path("reports/lithium_glycerophosphate_1005_20261101")
BASE = "838d0c2627552b0094545ebb580b5bb9b1a84d57"
SOURCE_MANIFEST_SHA = "ca89868b74535eb7d4296fbb3cb14cc6da8cb599dd78ab27ef95baff61f1eb24"


def require(value, reason):
    if not value:
        raise ValueError(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def regular(path):
    require(path.is_file() and not path.is_symlink() and path.resolve() == path.absolute(), "Non-original file path: " + str(path))
    return path.read_bytes()


def relative(name):
    path = Path(name)
    require(not path.is_absolute() and bool(path.parts) and ".." not in path.parts, "Unsafe relative path")
    return path


def source(name):
    path = RUN / relative(name)
    require(path.suffix not in {".db", ".sqlite", ".sqlite3"} and "/receipt-fixture/" not in str(path), "Excluded database/fixture corpus")
    require("unsupported-backlog" not in path.name and path.stat().st_size < 8_000_000, "Excluded oversized/generated backlog")
    if path.name in {"mim_nodes.tsv", "mim_edges.tsv", "ingredient_graph.json", "ingredient_umap.json"}:
        raise ValueError("Retain generated graph manifests, not whole graphs")
    return path


def freeze(selection, output):
    raw_selection = regular(selection)
    plan = json.loads(raw_selection)
    require(plan.get("state") == "final" and not plan.get("pending_final_inputs"), "Selection is draft or incomplete")
    require(plan["base"] == BASE and plan["worktree"] == "step4-mim", "Wrong execution scope")
    root = RUN / plan["worktree"]
    entries, commands = {}, []

    def add(name, destination, classification):
        path = source(name)
        target = str(relative(destination))
        require(target not in {"manifest.json", "README.md", "verify.py", "final-inputs.json"}, "Reserved package filename")
        data = regular(path)
        item = {"source_path": str(path), "destination": target, "classification": classification,
                "raw_sha256": sha(data), "raw_bytes": len(data)}
        if name in entries:
            require(entries[name]["raw_sha256"] == item["raw_sha256"], "Repeated source changed")
            return
        require(target not in {e["destination"] for e in entries.values()}, "Duplicate archive destination")
        entries[name] = item

    def command(item):
        name = item["receipt"]
        receipt = json.loads(regular(source(name)))
        require(receipt.get("finished_at") and type(receipt.get("exit_code")) is int, "Command is unfinished")
        require(receipt["exit_code"] == item["expected_exit"], "Unexpected command exit status")
        log = Path(receipt["log"])
        require(log.is_relative_to(RUN), "Command log is outside the run")
        log_name = str(log.relative_to(RUN))
        require(sha(regular(source(log_name))) == receipt["log_sha256"], "Command log hash differs")
        if receipt["exit_code"]:
            require(item.get("disposition"), "Failed command lacks an explicit disposition")
            replacement = json.loads(regular(source(item["successful_rerun"])))
            require(replacement.get("finished_at") and replacement.get("exit_code") == 0, "Failed attempt lacks a completed successful correction")
        commands.append({**item, "command_name": receipt["name"], "log_sha256": receipt["log_sha256"]})
        category = "failed_attempt" if receipt["exit_code"] else "completed_check"
        add(name, "commands/" + Path(name).name, category)
        add(log_name, "commands/" + Path(log_name).name, category)

    for item in plan["files"]:
        add(item["path"], item["destination"], item["classification"])
    for item in plan["commands"]:
        command(item)
    require(plan["execution_groups"], "Explicit completed native chain groups are required")
    stages = []
    for group in plan["execution_groups"]:
        directory = relative(group)
        complete = json.loads(regular(source(str(directory / "complete.json"))))
        require(complete.get("complete") is True and complete.get("scientific_approval_added") is False,
                "Native execution group is unfinished or approval-bearing")
        stages.append(complete["stage"])
        for name in ("start.json", "commands.jsonl", "verified-output.json", "complete.json"):
            add(str(directory / name), "native-chain/" + directory.name + "/" + name, "completed_native_chain")
        for line in regular(source(str(directory / "commands.jsonl"))).decode().splitlines():
            declared = json.loads(line)
            receipt_name = "logs/" + declared["name"] + ".json"
            receipt = json.loads(regular(source(receipt_name)))
            require(receipt["argv"] == declared["argv"], "Native command declaration/receipt mismatch")
            command({"receipt": receipt_name, "expected_exit": 0})
    require(sorted(stages) == ["build", "exports", "gates"], "Require exactly one completed build, exports and gates group")
    for item in plan["completion_receipts"]:
        value = json.loads(regular(source(item["path"])))
        require(value.get("state") == "complete" and value.get("applied") is True,
                "Publication receipt is not complete")
        require(value.get("transaction", {}).get("applied") is True, "Native transaction was not applied")
        add(item["path"], item["destination"], "actual_completed_publication")
        journal = Path(value["transaction"]["journal"])
        require(journal.is_relative_to(RUN), "Publication journal lies outside this run")
        add(str(journal.relative_to(RUN)), "transactions/" + Path(item["path"]).stem + "-journal.json", "native_transaction_journal")
    require(len({c["receipt"] for c in commands}) == len(commands), "Repeated command receipt selection")
    for item in commands:
        if item["expected_exit"]:
            require(item["successful_rerun"] in {c["receipt"] for c in commands}, "Successful correction must also be archived")

    source_manifest = root / REPORT / "sources/manifest.json"
    require(sha(regular(source_manifest)) == SOURCE_MANIFEST_SHA, "Frozen scientific source manifest changed")
    refs = {str(REPORT / "sources/manifest.json"): {"sha256": SOURCE_MANIFEST_SHA, "bytes": source_manifest.stat().st_size}}
    members = json.loads(source_manifest.read_bytes())["files"]
    require({p.name for p in source_manifest.parent.iterdir() if p.is_file()} == set(members) | {"manifest.json"}, "Source package membership changed")
    for name, item in members.items():
        path = root / REPORT / "sources" / relative(name)
        data = regular(path)
        require(sha(data) == item["sha256"] and len(data) == item["bytes"], "Frozen source bytes changed")
        refs[str(path.relative_to(root))] = {"sha256": sha(data), "bytes": len(data)}
    for name in plan["repository_references"]:
        data = regular(root / relative(name))
        refs[name] = {"sha256": sha(data), "bytes": len(data)}
    result = {"schema_version": 1, "kind": "explicit_final_execution_inputs", "created_at": datetime.now(timezone.utc).isoformat(),
              "base": BASE, "root": str(root), "destination": str(root / REPORT / "execution"),
              "packager_sha256": sha(regular(Path(__file__))), "selection_sha256": sha(raw_selection),
              "selection_path": str(selection), "sources": list(entries.values()), "commands": commands,
              "repository_references": refs, "scope_exclusions": plan["scope_exclusions"],
              "observed_limitations": plan["observed_limitations"], "scientific_approval_added": False, "supervisor_binding": None}
    for item in result["sources"]:
        require(sha(regular(Path(item["source_path"]))) == item["raw_sha256"], "Input changed while freezing")
    require(output.absolute().is_relative_to(HERE) and output.resolve() == output.absolute(), "Final input manifest must stay in the run-owned packaging directory")
    with output.open("x") as stream:
        json.dump(result, stream, indent=2); stream.write("\n")
    print(json.dumps({"frozen": str(output), "sha256": sha(output.read_bytes()), "sources": len(entries)}, indent=2))


def publish(inputs):
    frozen_bytes = regular(inputs)
    frozen = json.loads(frozen_bytes)
    require(frozen["kind"] == "explicit_final_execution_inputs" and frozen["base"] == BASE, "Wrong final manifest")
    require(sha(regular(Path(__file__))) == frozen["packager_sha256"], "Packager changed after freeze")
    require(sha(regular(Path(frozen["selection_path"]))) == frozen["selection_sha256"], "Final selection changed")
    root = Path(frozen["root"])
    destination = Path(frozen["destination"])
    require(root == RUN / "step4-mim" and destination == root / REPORT / "execution", "Publication destination differs")
    require(destination.parent.resolve() == destination.parent.absolute() and not destination.exists() and not destination.is_symlink(), "Execution output must be fresh and original")
    payloads, sources, by_digest = {}, [], {}
    for item in frozen["sources"]:
        raw = regular(Path(item["source_path"]))
        require(sha(raw) == item["raw_sha256"] and len(raw) == item["raw_bytes"], "Frozen execution input changed")
        if item["raw_sha256"] in by_digest:
            archived, encoding = by_digest[item["raw_sha256"]]
        else:
            encoding = "gzip" if len(raw) >= 100_000 else "identity"
            archived = str(relative(item["destination"])) + (".gz" if encoding == "gzip" else "")
            require(archived not in payloads, "Compressed archive name collision")
            payloads[archived] = gzip.compress(raw, mtime=0) if encoding == "gzip" else raw
            by_digest[item["raw_sha256"]] = (archived, encoding)
        sources.append({**item, "archive_path": archived, "encoding": encoding,
                        "archive_sha256": sha(payloads[archived]), "archive_bytes": len(payloads[archived])})
    payloads["final-inputs.json"] = frozen_bytes
    payloads["verify.py"] = regular(Path(__file__))
    payloads["README.md"] = (
        "# #1005 execution evidence\n\nThis package preserves explicitly selected completed transactions/checks, "
        "failed attempts with their dispositions, and independent probe checkpoints. Scientific source files "
        "remain in ../sources with their original manifest. Native diagnostic candidate and canonical promotion "
        "are different artifacts. Successful integrity checks do not grant scientific approval.\n\n"
        "Large payloads use deterministic gzip (mtime=0); raw/archive hashes and every original path are in manifest.json. "
        "Identical beforeimages and generation input snapshots share one archive. Rebuildable KGX, reviewed SSSOM "
        "and companion products are represented by manifests, not graph/backlog corpora.\n\n"
        "Verify: `python verify.py verify --package . --repository ../../.. --require-tracked` after publication. "
        "The tracked check is deliberately deferred until the final commit; it checks every referenced source member.\n\n"
        "Exclusions: " + "; ".join(frozen["scope_exclusions"]) + ".\n\nLimitations: "
        + "; ".join(frozen["observed_limitations"]) + ".\n"
    ).encode()
    for name, item in frozen["repository_references"].items():
        data = regular(root / relative(name))
        require(sha(data) == item["sha256"] and len(data) == item["bytes"], "Maintained reference changed")
    manifest = {"schema_version": 1, "base": BASE, "created_at": datetime.now(timezone.utc).isoformat(),
                "files": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in sorted(payloads.items())},
                "sources": sources, "commands": frozen["commands"], "repository_references": frozen["repository_references"],
                "scope_exclusions": frozen["scope_exclusions"], "observed_limitations": frozen["observed_limitations"],
                "scientific_approval_added": False, "supervisor_binding": None}
    # All inputs validated before exclusive output reservation; no existing path is overwritten.
    destination.mkdir(exist_ok=False)
    for name, data in payloads.items():
        path = destination / relative(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(data)
    for item in frozen["sources"]:
        require(sha(regular(Path(item["source_path"]))) == item["raw_sha256"], "Source changed during packaging; partial directory retained")
    for name, item in frozen["repository_references"].items():
        require(sha(regular(root / relative(name))) == item["sha256"], "Maintained reference changed during packaging; partial directory retained")
    with (destination / "manifest.json").open("x") as stream:
        json.dump(manifest, stream, indent=2); stream.write("\n")
    verify(destination, root, False)


def verify(package, repository, require_tracked):
    package = package.resolve()
    manifest = json.loads(regular(package / "manifest.json"))
    require(not any(p.is_symlink() for p in package.rglob("*")), "Package contains a file or directory alias")
    actual = {str(p.relative_to(package)) for p in package.rglob("*") if p.is_file()}
    require(actual == set(manifest["files"]) | {"manifest.json"}, "Execution archive membership differs")
    for name, item in manifest["files"].items():
        data = regular(package / relative(name))
        require(sha(data) == item["sha256"] and len(data) == item["bytes"], "Execution archive bytes differ")
    original_bytes = {}
    for item in manifest["sources"]:
        data = regular(package / relative(item["archive_path"]))
        require(sha(data) == item["archive_sha256"] and len(data) == item["archive_bytes"], "Original/archive binding differs")
        require(item["encoding"] in {"gzip", "identity"}, "Unknown compression")
        raw = gzip.decompress(data) if item["encoding"] == "gzip" else data
        require(sha(raw) == item["raw_sha256"] and len(raw) == item["raw_bytes"], "Decoded original bytes differ")
        require(item["source_path"] not in original_bytes, "Duplicate original identity")
        original_bytes[item["source_path"]] = raw
    for command in manifest["commands"]:
        matches = [raw for path, raw in original_bytes.items() if path.endswith("/" + command["receipt"])]
        require(len(matches) == 1, "Command receipt missing/ambiguous")
        receipt = json.loads(matches[0])
        require(receipt["exit_code"] == command["expected_exit"] and receipt["finished_at"], "Command status differs")
        require(sha(original_bytes[receipt["log"]]) == receipt["log_sha256"], "Archived command/log mismatch")
    if repository:
        repository = repository.resolve()
        for name, item in manifest["repository_references"].items():
            data = regular(repository / relative(name))
            require(sha(data) == item["sha256"] and len(data) == item["bytes"], "Referenced maintained evidence differs: " + name)
        if require_tracked:
            members = [str((package / p).relative_to(repository)) for p in actual]
            subprocess.run(["git", "ls-files", "--error-unmatch", "--", *manifest["repository_references"], *members], cwd=repository, check=True, stdout=subprocess.DEVNULL)
    require(not require_tracked or repository, "Tracked verification requires repository")
    print(json.dumps({"status": "PASS", "archive_members": len(actual), "original_identities": len(original_bytes),
                      "repository_references_checked": bool(repository), "tracked_checked": require_tracked,
                      "scientific_approval_added": False}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="mode", required=True)
    prepare = commands.add_parser("freeze")
    prepare.add_argument("--selection", type=Path, required=True)
    prepare.add_argument("--output", type=Path, required=True)
    publish_parser = commands.add_parser("publish")
    publish_parser.add_argument("--inputs", type=Path, required=True)
    check = commands.add_parser("verify")
    check.add_argument("--package", type=Path, required=True)
    check.add_argument("--repository", type=Path)
    check.add_argument("--require-tracked", action="store_true")
    args = parser.parse_args()
    if args.mode == "freeze":
        freeze(args.selection.absolute(), args.output.absolute())
    elif args.mode == "publish":
        publish(args.inputs.absolute())
    else:
        verify(args.package, args.repository, args.require_tracked)


if __name__ == "__main__":
    main()
