"""External disposable-fixture controls; never writes the maintained worktree."""
import importlib.util
import json
import os
import tempfile
from pathlib import Path

D = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("archive_guard", D / "archive_resumption_evidence_v1.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def reject(action, name, checks):
    try:
        action()
    except (ValueError, FileExistsError):
        checks.append(name)
        return
    raise AssertionError("unsafe control accepted: " + name)


checks = []
with tempfile.TemporaryDirectory(prefix="step7d-resumption-archive-control-", dir="/private/tmp") as temporary:
    root = Path(temporary)
    target = root / "new" / "evidence.txt"
    assert m.write_new(root, target, b"immutable\n") == "create_exclusive"
    checks.append("new evidence created exclusively with exact readback")
    inode = target.stat().st_ino
    assert m.write_new(root, target, b"immutable\n") == "retain_identical"
    assert target.stat().st_ino == inode
    checks.append("existing identical evidence retained without rewriting inode")
    reject(lambda: m.write_new(root, target, b"changed\n"), "differing target rejected without overwrite", checks)
    assert target.read_bytes() == b"immutable\n"
    link = root / "alias.txt"
    link.symlink_to(target)
    reject(lambda: m.write_new(root, link, b"immutable\n"), "symlink target rejected", checks)
    parent = root / "parent-alias"
    parent.symlink_to(target.parent, target_is_directory=True)
    reject(lambda: m.write_new(root, parent / "new.txt", b"x"), "symlink parent rejected", checks)
    hardlink = root / "hardlink.txt"
    os.link(target, hardlink)
    reject(lambda: m.regular(hardlink), "hardlinked file rejected", checks)
    hardlink.unlink()
    reject(lambda: m.safe_relative("../outside.txt"), "path traversal rejected", checks)
    reject(lambda: m.safe_relative("/absolute.txt"), "absolute target rejected", checks)
    reject(lambda: m.safe_relative("a//b"), "noncanonical relative target rejected", checks)

    run = root / "run"
    execution = run / "execution"
    workspace = run / "step7d"
    logs = run / "logs"
    for directory in (execution, workspace, logs):
        directory.mkdir(parents=True)
    source = execution / "source.json"
    source.write_bytes(b"{\"frozen\":true}\n")
    report = workspace / "reports/step7d_mapping_901_20261103"
    report.mkdir(parents=True)
    prior = report / "prior.json"
    prior.write_bytes(b"{\"old\":true}\n")
    protected = workspace / "protected.txt"
    protected.write_bytes(b"unchanged\n")
    manifest = {
        "schema": "step7d-immutable-resumption-archive-v1",
        "workspace": str(workspace),
        "archive_relative": "reports/step7d_mapping_901_20261103/resumption",
        "source_roots": {"execution": str(execution), "logs": str(logs)},
        "files": [{"source_root": "execution", "source_relative": "source.json", "archive_relative": "source.json", "sha256": m.digest(source.read_bytes()), "size": source.stat().st_size}],
        "existing_report_files": [{"relative": "prior.json", "sha256": m.digest(prior.read_bytes()), "size": prior.stat().st_size}],
        "protected_sha256": {"protected.txt": m.digest(protected.read_bytes())},
    }
    manifest_path = execution / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    manifest_sha = m.digest(manifest_path.read_bytes())
    assert len(m.validate_manifest(manifest_path, manifest_sha)[2]) == 2
    checks.append("complete positive manifest validates without creating archive")
    assert not (report / "resumption").exists()
    reject(lambda: m.validate_manifest(manifest_path, "0" * 64), "wrong reviewed manifest hash rejected", checks)
    source.write_bytes(b"changed")
    reject(lambda: m.validate_manifest(manifest_path, manifest_sha), "source drift rejected before archive write", checks)
    source.write_bytes(b"{\"frozen\":true}\n")
    prior.write_bytes(b"changed")
    reject(lambda: m.validate_manifest(manifest_path, manifest_sha), "old report drift rejected before archive write", checks)
    prior.write_bytes(b"{\"old\":true}\n")
    protected.write_bytes(b"changed")
    reject(lambda: m.validate_manifest(manifest_path, manifest_sha), "protected maintained endpoint drift rejected", checks)
    protected.write_bytes(b"unchanged\n")
    manifest["files"].append(dict(manifest["files"][0]))
    manifest_path.write_text(json.dumps(manifest))
    reject(lambda: m.validate_manifest(manifest_path, m.digest(manifest_path.read_bytes())), "duplicate target rejected", checks)

result = {
    "operator_sha256": m.digest((D / "archive_resumption_evidence_v1.py").read_bytes()),
    "controls_sha256": m.digest(Path(__file__).read_bytes()),
    "checks_passed": len(checks),
    "checks": checks,
    "fixture": "Disposable external temporary directory only",
    "maintained_writes": False,
    "git_mutations": False,
}
output = D / "archive-resumption-controls-v1.json"
with output.open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"checks_passed": len(checks), "result": str(output), "sha256": m.digest(output.read_bytes())}, indent=2))
