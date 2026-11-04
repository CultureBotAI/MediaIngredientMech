"""Copy only a hash-pinned immutable resumption evidence manifest.

Default verifies and prints a plan. Root alone invokes --apply. Existing report
files are never overwritten; identical target bytes are retained. No Git calls,
source edits, native producers, test runs, scientific approval or cleanup.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import os
import stat
from pathlib import Path


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError("resumption archive: " + message)


def regular(path):
    path = Path(path).absolute()
    info = path.lstat()
    require(path.resolve() == path and stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
            "aliased or nonregular file: " + str(path))
    return path.read_bytes()


def safe_relative(value):
    path = Path(value)
    require(not path.is_absolute() and path.parts and all(p not in {".", ".."} for p in path.parts),
            "unsafe relative path: " + value)
    require(str(path) == value and "\0" not in value, "noncanonical relative path: " + value)
    return path


def target_bytes(path, expected):
    path = Path(path).absolute()
    require(path.resolve() == path, "aliased destination: " + str(path))
    if os.path.lexists(path):
        require(regular(path) == expected, "existing evidence differs; never overwrite: " + str(path))
        return "retain_identical"
    return "create_exclusive"


def ensure_parent(root, destination):
    root = Path(root).absolute()
    require(root.resolve() == root and root.is_dir(), "unsafe repository root")
    parts = destination.relative_to(root).parts[:-1]
    current = root
    for part in parts:
        current /= part
        if not os.path.lexists(current):
            current.mkdir(mode=0o755)
        info = current.lstat()
        require(stat.S_ISDIR(info.st_mode) and current.resolve() == current,
                "aliased/non-directory parent: " + str(current))


def write_new(root, path, raw):
    status = target_bytes(path, raw)
    if status == "retain_identical":
        return status
    ensure_parent(root, path)
    require(path.resolve() == path and not os.path.lexists(path), "target appeared before exclusive create")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags, 0o644)
    with os.fdopen(descriptor, "wb") as output:
        output.write(raw)
        output.flush()
        os.fsync(output.fileno())
    require(regular(path) == raw, "created evidence readback mismatch")
    return status


def validate_manifest(path, expected_sha):
    raw = regular(path)
    require(digest(raw) == expected_sha, "manifest hash differs from reviewed hash")
    manifest = json.loads(raw)
    require(manifest["schema"] == "step7d-immutable-resumption-archive-v1", "wrong manifest schema")
    workspace = Path(manifest["workspace"]).absolute()
    report_relative = "reports/step7d_mapping_901_20261103"
    archive_relative = report_relative + "/resumption"
    require(manifest["archive_relative"] == archive_relative, "archive destination changed")
    require(workspace.resolve() == workspace and workspace.is_dir(), "unsafe workspace")
    roots = {name: Path(value).absolute() for name, value in manifest["source_roots"].items()}
    require(set(roots) == {"execution", "logs"}, "unexpected source root")
    require(roots["execution"].parent / "step7d" == workspace and roots["logs"] == roots["execution"].parent / "logs",
            "source roots differ from isolated Step7d context")
    files = []
    destinations = set()
    for entry in manifest["files"]:
        require(entry["source_root"] in roots, "unknown source root")
        source = roots[entry["source_root"]] / safe_relative(entry["source_relative"])
        relative = safe_relative(entry["archive_relative"])
        destination = workspace / archive_relative / relative
        require(str(relative) not in destinations, "duplicate archive destination")
        destinations.add(str(relative))
        content = regular(source)
        require(len(content) == entry["size"] and digest(content) == entry["sha256"],
                "frozen source changed: " + str(source))
        files.append((source, destination, content, target_bytes(destination, content)))
    # The manifest cannot include its own hash; archive exactly the verified bytes.
    manifest_target = workspace / archive_relative / "archive-manifest-v1.json"
    require("archive-manifest-v1.json" not in destinations, "manifest destination collision")
    files.append((Path(path).absolute(), manifest_target, raw, target_bytes(manifest_target, raw)))
    for entry in manifest["existing_report_files"]:
        relative = safe_relative(entry["relative"])
        content = regular(workspace / report_relative / relative)
        require(len(content) == entry["size"] and digest(content) == entry["sha256"],
                "old report evidence changed: " + str(relative))
    for relative, expected in manifest["protected_sha256"].items():
        require(digest(regular(workspace / safe_relative(relative))) == expected,
                "protected maintained endpoint changed: " + relative)
    return manifest, workspace, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    manifest, workspace, files = validate_manifest(args.manifest, args.manifest_sha256)
    operator = Path(__file__).absolute()
    require(any(source == operator and raw == regular(operator) for source, _, raw, _ in files),
            "executed operator is not pinned in manifest")
    state = {
        "state": "plan_only" if not args.apply else "running",
        "manifest_sha256": args.manifest_sha256,
        "operator_sha256": digest(regular(operator)),
        "files": len(files),
        "new_targets": sum(kind == "create_exclusive" for _, _, _, kind in files),
        "existing_identical_targets": sum(kind == "retain_identical" for _, _, _, kind in files),
        "old_report_files_verified": len(manifest["existing_report_files"]),
        "bytes_in_selected_evidence": sum(len(raw) for _, _, raw, _ in files),
        "git_mutations": False,
        "scientific_approval_added": False,
        "copied": [],
    }
    if not args.apply:
        print(json.dumps(state, indent=2))
        return
    execution = Path(manifest["source_roots"]["execution"])
    receipt_path = execution / "archive-resumption-apply-v1.json"
    trace_path = execution / "archive-resumption-apply-v1.jsonl"
    for target in (receipt_path, trace_path):
        require(target.resolve() == target and not os.path.lexists(target), "execution evidence already exists")
    # Reserve both external outputs before any maintained archive directory/write.
    with receipt_path.open("x") as receipt, trace_path.open("x") as trace:
        def save():
            receipt.seek(0)
            receipt.truncate()
            json.dump(state, receipt, indent=2)
            receipt.write("\n")
            receipt.flush()
        save()
        try:
            for source, destination, content, _ in files:
                require(regular(source) == content, "source changed during copy: " + str(source))
                action = write_new(workspace, destination, content)
                event = {"path": str(destination.relative_to(workspace)), "sha256": digest(content), "action": action}
                state["copied"].append(event)
                trace.write(json.dumps(event) + "\n")
                trace.flush()
                save()
            validate_manifest(args.manifest, args.manifest_sha256)
            require(all(regular(destination) == content for _, destination, content, _ in files), "final target mismatch")
            state.update(state="complete", finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
            save()
        except Exception as error:
            state.update(state="failed", error=str(error), stop="Preserve partial archive and receipts; no overwrite, deletion or automatic retry.")
            save()
            trace.write(json.dumps({"state": "failed", "error": str(error)}) + "\n")
            trace.flush()
            raise
    print(json.dumps({"state": "complete", "receipt": str(receipt_path), "receipt_sha256": digest(regular(receipt_path))}, indent=2))


if __name__ == "__main__":
    main()
