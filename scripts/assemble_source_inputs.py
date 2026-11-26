#!/usr/bin/env python3
"""Prepare selected source-only inputs in a new directory (#1431).

Run with the reviewed interpreter's -I -B flags and a separately reviewed
selection SHA. This is not a scientific/native report, export or publication.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib
import json
import os
import platform
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

CODE = (
    "scripts/assemble_source_inputs.py",
    "src/mediaingredientmech/__init__.py",
    "src/mediaingredientmech/export/__init__.py",
    "src/mediaingredientmech/curate/__init__.py",
    "src/mediaingredientmech/curate/publication_guard.py",
    "src/mediaingredientmech/review_claims.py",
    "src/mediaingredientmech/export/culturemech_layout.py",
    "src/mediaingredientmech/export/source_conservation.py",
    "src/mediaingredientmech/export/source_assembly.py",
    "src/mediaingredientmech/export/source_input_selection.py",
)
NAMES = frozenset(
    {
        "cm-source-nodes.tsv",
        "cm-source-occurrences.tsv",
        "cm-raw-row-map.json",
        "cm-case-crosswalk.json",
        "source-nodes.tsv",
        "source-occurrences.tsv",
        "combined-position-map.json",
        "cm-reconciliation.tsv",
        "kg-provider-cases.json",
        "historical-obligations.json",
        "obligation-crosswalk.json",
        "projection-declaration.json",
        "curie-map.json",
        "input-selection.json",
        "manifest.json",
    }
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def document(raw: bytes) -> Any:
    return json.loads(raw, object_pairs_hook=unique)


def encoded(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode()


def relative(value: str) -> str:
    require(
        type(value) is str and bool(value) and "\\" not in value and "\x00" not in value,
        "invalid relative path",
    )
    path = PurePosixPath(value)
    require(
        not path.is_absolute() and ".." not in path.parts and str(path) == value and value != ".",
        "invalid relative path",
    )
    return value


def identity(info: os.stat_result) -> tuple[int, int, int, int]:
    return info.st_dev, info.st_ino, info.st_mode, info.st_nlink


def file_snapshot(info: os.stat_result) -> tuple[int, ...]:
    return (*identity(info), info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def read_bootstrap(path: Path) -> bytes:
    """Small pre-import read, re-captured through FrozenFile after imports."""
    require(not any(p.is_symlink() for p in (path, *path.parents)), "bootstrap path alias")
    parents = [(p, (p.stat().st_dev, p.stat().st_ino)) for p in path.parents]
    before = path.lstat()
    require(stat.S_ISREG(before.st_mode) and before.st_nlink == 1, "bootstrap file alias")
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, "rb") as handle:
        require(identity(os.fstat(handle.fileno())) == identity(before), "bootstrap file replaced")
        raw = handle.read()
        require(
            file_snapshot(os.fstat(handle.fileno())) == file_snapshot(before),
            "bootstrap file changed",
        )
    require(file_snapshot(path.lstat()) == file_snapshot(before), "bootstrap path changed")
    for parent, expected in parents:
        require(
            not parent.is_symlink() and (parent.stat().st_dev, parent.stat().st_ino) == expected,
            "bootstrap ancestor changed",
        )
    return raw


def bootstrap(
    root: Path, selection_path: Path, expected_sha: str
) -> tuple[dict[str, Any], dict[str, Any], Any]:
    require(
        sys.flags.isolated == 1 and sys.dont_write_bytecode,
        "use the reviewed interpreter with -I -B",
    )
    require(
        root.is_absolute()
        and root == root.resolve()
        and Path(__file__).absolute() == root / CODE[0],
        "isolated code root differs",
    )
    require(
        not any(
            name == "mediaingredientmech" or name.startswith("mediaingredientmech.")
            for name in sys.modules
        ),
        "preloaded MIM code refused",
    )
    selected_raw = read_bootstrap(selection_path)
    require(sha(selected_raw) == expected_sha, "reviewed selection hash differs")
    plan = document(selected_raw)
    require(
        type(plan) is dict
        and set(plan)
        == {
            "schema_version",
            "head",
            "implementation",
            "runtime",
            "scope",
            "declaration",
            "curie_map",
            "reviewed_crosswalk",
            "output_directory",
            "inputs",
        },
        "unknown selection shape",
    )
    require(
        type(plan["schema_version"]) is int and plan["schema_version"] == 1,
        "unknown selection version",
    )
    require(
        plan["runtime"]
        == {
            "executable": sys.executable,
            "version": platform.python_version(),
            "sha256": sha(Path(sys.executable).resolve().read_bytes()),
        },
        "selected runtime differs",
    )
    require(
        sys.version_info[:2] == (3, 13) and csv.field_size_limit() == 131072,
        "runtime/parser contract differs",
    )
    require(set(plan["implementation"]) == set(CODE), "implementation inventory differs")
    code = {}
    for name in CODE:
        path = root / name
        raw = read_bootstrap(path)
        require(sha(raw) == plan["implementation"][name], "implementation bytes differ: " + name)
        require(
            not path.with_suffix(".pyc").exists()
            and not list((path.parent / "__pycache__").glob(path.stem + ".*.pyc")),
            "selected bytecode cache refused",
        )
        code[name] = raw
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0", "GIT_NO_LAZY_FETCH": "1"}
    head = subprocess.run(
        ["git", "--no-optional-locks", "rev-parse", "HEAD"],
        cwd=root,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    ).stdout.strip()
    require(head == plan["head"], "selected code HEAD differs")
    for name, raw in code.items():
        committed = subprocess.run(
            ["git", "--no-optional-locks", "show", "HEAD:" + name],
            cwd=root,
            env=env,
            check=True,
            capture_output=True,
            timeout=30,
        ).stdout
        require(committed == raw, "implementation is not committed at selected HEAD: " + name)
    sys.path.insert(0, str(root / "src"))
    modules = {
        name: importlib.import_module("mediaingredientmech.export." + name)
        for name in ("source_assembly", "source_conservation", "source_input_selection")
    }
    guard = importlib.import_module("mediaingredientmech.curate.publication_guard")
    for name, module in tuple(sys.modules.items()):
        if name == "mediaingredientmech" or name.startswith("mediaingredientmech."):
            module_file = module.__file__
            if module_file is None:
                raise ValueError("MIM module has no source origin")
            origin = Path(module_file).absolute()
            require(
                origin.is_relative_to(root) and origin.relative_to(root).as_posix() in code,
                "foreign imported MIM module",
            )
    frozen = {name: guard.FrozenFile.capture(root / name) for name in CODE}
    for name, item in frozen.items():
        require(item.content == code[name], "code changed during import")
    frozen["@selection"] = guard.FrozenFile.capture(selection_path)
    require(frozen["@selection"].content == selected_raw, "selection changed during import")
    return plan, {"modules": modules, "frozen": frozen, "selection_raw": selected_raw}, guard


class UnsafeOutput(RuntimeError):
    """The originally owned directory/files cannot safely receive writes."""


class Output:
    """One exclusive source generation; fixed files, no arbitrary publication."""

    def __init__(self, path: Path, guard: Any):
        self.path, self.guard = path, guard
        self.directories: list[tuple[Any, str, int, tuple[int, int, int]]] = []
        self.files: dict[str, dict[str, Any]] = {}
        flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
        try:
            require(path.is_absolute() and ".." not in path.parts, "output path must be absolute")
            fd = os.open("/", flags)
            self.directories.append((None, "/", fd, identity(os.fstat(fd))[:3]))
            for name in path.parent.parts[1:]:
                parent = self.directories[-1][2]
                fd = os.open(name, flags, dir_fd=parent)
                self.directories.append((parent, name, fd, identity(os.fstat(fd))[:3]))
            self.lineage()
            parent = self.directories[-1][2]
            os.mkdir(path.name, 0o700, dir_fd=parent)
            created = os.stat(path.name, dir_fd=parent, follow_symlinks=False)
            self.fd = os.open(path.name, flags, dir_fd=parent)
            self.directories.append((parent, path.name, self.fd, identity(created)[:3]))
            self.verify()
            for name in sorted(NAMES):
                handle = os.fdopen(
                    os.open(
                        name,
                        os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                        0o600,
                        dir_fd=self.fd,
                    ),
                    "r+b",
                    buffering=0,
                )
                self.files[name] = {
                    "handle": handle,
                    "state": self.state(os.fstat(handle.fileno())),
                    "bytes": b"",
                }
            self.verify()
        except Exception:
            self.close()
            raise

    @staticmethod
    def state(info: os.stat_result) -> tuple[int, ...]:
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise UnsafeOutput("output is nonregular or hardlinked")
        return (*identity(info), info.st_size, info.st_mtime_ns, info.st_ctime_ns)

    def lineage(self) -> None:
        for parent, name, fd, original in self.directories:
            held = os.fstat(fd)
            entry = os.stat(name, dir_fd=parent, follow_symlinks=False)
            if (
                not stat.S_ISDIR(held.st_mode)
                or identity(held)[:3] != original
                or identity(entry)[:3] != original
            ):
                raise UnsafeOutput("output directory/ancestor replaced")

    def verify(self) -> None:
        self.lineage()
        if set(os.listdir(self.fd)) != set(self.files):
            raise UnsafeOutput("output membership changed")
        for name, item in self.files.items():
            handle = item["handle"]
            self.guard.check_reserved(handle, self.path / name)
            if self.state(os.fstat(handle.fileno())) != item["state"]:
                raise UnsafeOutput("output identity/metadata changed: " + name)
            if os.pread(handle.fileno(), len(item["bytes"]) + 1, 0) != item["bytes"]:
                raise UnsafeOutput("output bytes changed: " + name)
            if self.state(os.fstat(handle.fileno())) != item["state"]:
                raise UnsafeOutput("output changed during readback")
        self.lineage()

    def write(self, name: str, raw: bytes, *, manifest_replace: bool = False) -> None:
        require(name in NAMES and type(raw) is bytes, "unknown output member/type")
        self.verify()
        item = self.files[name]
        require(
            not item["bytes"] or (name == "manifest.json" and manifest_replace),
            "output already written",
        )
        fd = item["handle"].fileno()
        original = item["state"]
        if manifest_replace:
            require(name == "manifest.json", "only owned manifest may be invalidated")
            os.ftruncate(fd, 0)
        os.lseek(fd, 0, os.SEEK_SET)
        remaining = memoryview(raw)
        while remaining:
            written = os.write(fd, remaining)
            if written <= 0:
                raise UnsafeOutput("incomplete output write")
            remaining = remaining[written:]
        os.fsync(fd)
        after = self.state(os.fstat(fd))
        if after[:4] != original[:4] or after[4] != len(raw):
            raise UnsafeOutput("output identity/mode/link/size changed during write")
        item["bytes"], item["state"] = raw, after
        self.verify()

    def read(self, name: str) -> bytes:
        self.verify()
        item = self.files[name]
        return os.pread(item["handle"].fileno(), len(item["bytes"]) + 1, 0)

    def failure(self, error: Exception) -> None:
        print(f"Source-input assembly failed: {type(error).__name__}: {error}", file=sys.stderr)
        try:
            self.verify()
            self.write(
                "manifest.json",
                encoded(
                    {
                        "status": "FAILED_SOURCE_INPUT_PREPARATION",
                        "error": str(error),
                        "scientific_approval": False,
                        "native_conservation": False,
                        "publication_authorized": False,
                    }
                ),
                manifest_replace=True,
            )
        except Exception as unsafe:
            print(
                f"Unsafe output; no fallback writes or cleanup: {type(unsafe).__name__}: {unsafe}",
                file=sys.stderr,
            )

    def close(self) -> None:
        for item in self.files.values():
            item["handle"].close()
        for _, _, fd, _ in reversed(self.directories):
            os.close(fd)
        self.files, self.directories = {}, []


def execute(
    root: Path, plan: dict[str, Any], captured_code: dict[str, Any], guard: Any
) -> dict[str, Any]:
    """Capture selected originals and prepare one source-only generation."""
    modules = captured_code["modules"]
    selector, assembly, inverse = (
        modules[key] for key in ("source_input_selection", "source_assembly", "source_conservation")
    )
    output_name = relative(plan["output_directory"])
    output_path = root / output_name
    selector.validate_scope(plan["scope"])
    for role, name in selector.ARTIFACT_NAMES.items():
        require(
            plan["scope"]["artifacts"][role] == output_name + "/" + name,
            "artifact destination differs",
        )
    frozen = dict(captured_code["frozen"])
    inputs: dict[str, bytes] = {}
    require(type(plan["inputs"]) is dict, "selected inventory must be an object")
    for path, pin in plan["inputs"].items():
        relative(path)
        require(
            not (root / path).is_relative_to(output_path)
            and not output_path.is_relative_to(root / path),
            "input/output overlap",
        )
        require(type(pin) is dict and set(pin) == {"sha256", "bytes"}, "input pin shape differs")
        item = guard.FrozenFile.capture(root / path)
        require(
            sha(item.content) == pin["sha256"]
            and type(pin["bytes"]) is int
            and len(item.content) == pin["bytes"],
            "selected input bytes differ",
        )
        frozen["input:" + path], inputs[path] = item, item.content
    extra = set()

    def selected(name: str) -> bytes:
        ref = plan[name]
        require(
            type(ref) is dict and set(ref) == {"path", "sha256"}, "selected reference shape differs"
        )
        path = relative(ref["path"])
        require(path in inputs and sha(inputs[path]) == ref["sha256"], "selected reference differs")
        extra.add(path)
        return inputs[path]

    declaration, crosswalk, prefixes = (
        selected(name) for name in ("declaration", "reviewed_crosswalk", "curie_map")
    )
    require(len(extra) == 3, "selected control inputs overlap")
    data = selector.select_source_inputs(
        inputs,
        selected_scope=plan["scope"],
        declaration=declaration,
        declaration_path=output_name + "/projection-declaration.json",
        reviewed_crosswalk=crosswalk,
        curie_map=prefixes,
    )
    require(
        set(inputs) == set(data["consumed_inputs"]) | extra,
        "selected input inventory has missing/extra members",
    )
    args = {
        key: data[key]
        for key in (
            "cm",
            "kg",
            "family_paths",
            "curie_map",
            "historical_obligations",
            "reviewed_crosswalk",
        )
    }

    def recheck() -> None:
        for item in frozen.values():
            item.verify()
        require(csv.field_size_limit() == 131072, "reader budget changed")

    recheck()
    outputs = Output(output_path, guard)
    try:
        candidate = assembly.combine_sources(assembly.project_culturemech(args["cm"]), **args)
        products = {
            "cm-source-nodes.tsv": candidate["cm"]["nodes"],
            "cm-source-occurrences.tsv": candidate["cm"]["occurrences"],
            "cm-raw-row-map.json": encoded(candidate["cm"]["raw_row_map"]),
            "cm-case-crosswalk.json": encoded(candidate["cm"]["case_crosswalk"]),
            "source-nodes.tsv": candidate["nodes"],
            "source-occurrences.tsv": candidate["occurrences"],
            "combined-position-map.json": encoded(candidate["position_map"]),
            "cm-reconciliation.tsv": candidate["reconciliation"],
            "kg-provider-cases.json": encoded(candidate["kg_provider_cases"]),
            "historical-obligations.json": encoded(candidate["historical_obligations"]),
            "obligation-crosswalk.json": crosswalk,
            "projection-declaration.json": declaration,
            "curie-map.json": prefixes,
            "input-selection.json": captured_code["selection_raw"],
        }
        require(set(products) == NAMES - {"manifest.json"}, "product membership differs")
        for name, raw in products.items():
            outputs.write(name, raw)
        actual = {name: outputs.read(name) for name in products}
        reconstructed = {
            "cm": {
                "nodes": actual["cm-source-nodes.tsv"],
                "occurrences": actual["cm-source-occurrences.tsv"],
                "raw_row_map": document(actual["cm-raw-row-map.json"]),
                "case_crosswalk": document(actual["cm-case-crosswalk.json"]),
            },
            "nodes": actual["source-nodes.tsv"],
            "occurrences": actual["source-occurrences.tsv"],
            "position_map": document(actual["combined-position-map.json"]),
            "reconciliation": actual["cm-reconciliation.tsv"],
            "kg_provider_cases": document(actual["kg-provider-cases.json"]),
            "historical_obligations": document(actual["historical-obligations.json"]),
            "obligation_crosswalk": document(actual["obligation-crosswalk.json"]),
        }
        result = inverse.validate_source_conservation(reconstructed, **args)
        owner = document(inputs[plan["scope"]["authorities"]["kg_source_selection"]["path"]])
        require(
            result["kg_nodes"] == owner["row_counts"]["kg_source_ids"]
            and result["kg_occurrences"] == owner["row_counts"]["kg_occurrences"],
            "selected KG output counts differ",
        )
        require(
            result["kg_provider_occurrences"]
            == {k: v["occurrences"] for k, v in owner["provider_counts"].items()},
            "selected KG provider counts differ",
        )
        expected_lanes = owner["intended_accepted_cm_v3"]["expected_counts"]
        require(
            all(
                result["cm_lanes"].get(k, 0) == expected_lanes[k]
                for k in ("positive_inventory", "context_only", "held")
            ),
            "selected CM lane counts differ",
        )
        maxima = {"characters": 0, "utf8_bytes": 0}
        for name, raw in actual.items():
            if name.endswith(".tsv"):
                fields, rows = inverse._read_table(raw)
                for cell in [*fields, *(value for row in rows for value in row.values())]:
                    maxima["characters"] = max(maxima["characters"], len(cell))
                    maxima["utf8_bytes"] = max(maxima["utf8_bytes"], len(cell.encode("utf-8")))
        manifest = {
            "status": "SOURCE_INPUTS_ASSEMBLED_UNREVIEWED",
            "scientific_approval": False,
            "native_conservation": False,
            "publication_authorized": False,
            "selection_sha256": sha(captured_code["selection_raw"]),
            "head": plan["head"],
            "implementation": plan["implementation"],
            "runtime": plan["runtime"],
            "inputs": plan["inputs"],
            "files": {
                name: {"sha256": sha(raw), "bytes": len(raw)} for name, raw in actual.items()
            },
            "accounting": result,
            "cell_maxima": maxima,
            "historical_dispositions_not_current_approval": data[
                "historical_dispositions_not_current_approval"
            ],
            "limits": [
                "Raw original hashes are distinct from parsed/serialized conservation",
                "Not native conservation or current scientific approval",
                "Requires genuine successful terminal and final input/output lineage verification",
            ],
        }
        recheck()
        outputs.write("manifest.json", encoded(manifest))
        recheck()
        outputs.verify()
        return manifest
    except Exception as exc:
        outputs.failure(exc)
        raise
    finally:
        outputs.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--selection", required=True)
    parser.add_argument("--selection-sha256", required=True)
    options = parser.parse_args()
    try:
        path = options.root / relative(options.selection)
        plan, captured, guard = bootstrap(options.root, path, options.selection_sha256)
        result = execute(options.root, plan, captured, guard)
        print(json.dumps({"status": result["status"], "output": plan["output_directory"]}))
        return 0
    except Exception as exc:
        print(f"Source-input preparation refused: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
