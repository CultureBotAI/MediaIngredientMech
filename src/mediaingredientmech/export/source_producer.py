"""Captured-byte execution and standalone producer provenance (#1305, #1195).

This loader is itself compiled from captured bytes by source_bindings. Public
MIM modules already present in sys.modules are never reused or reloaded.
"""

from __future__ import annotations

import builtins
import hashlib
import importlib.metadata
import os
import platform
import stat
import subprocess
import sys
import types
import uuid
from pathlib import Path

SOURCE = "src/mediaingredientmech/export/source_bindings.py"
LOADER = "src/mediaingredientmech/export/source_producer.py"
MODULES = (
    "mediaingredientmech.export.source_bindings",
    "mediaingredientmech.export.reviewed_sssom",
    "mediaingredientmech.native_acquisition",
    "mediaingredientmech.stable_ids",
    "mediaingredientmech.review_claims",
    "mediaingredientmech.mapping_scope",
    "mediaingredientmech.curie",
    "mediaingredientmech.synonym_policy",
    "mediaingredientmech.sssom_metadata",
    "mediaingredientmech.identity_projection",
)
AUXILIARY = (
    LOADER,
    "scripts/record_review.py",
    "schema/record_review.yaml",
    "uv.lock",
    "pyproject.toml",
    ".python-version",
)
RUNTIME_PACKAGES = ("sssom", "curies", "linkml", "linkml-runtime", "jsonschema", "pandas", "PyYAML")


def require(condition, message):
    if not condition:
        raise ValueError("Source producer provenance: " + message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def capture_file(path):
    path = Path(path).absolute()
    require(not any(p.is_symlink() for p in (path, *path.parents)), "symlink input")
    before = path.stat()
    require(stat.S_ISREG(before.st_mode) and before.st_nlink == 1, "nonregular/aliased producer")
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), "rb") as stream:
        opened = os.fstat(stream.fileno())
        require(
            (opened.st_dev, opened.st_ino) == (before.st_dev, before.st_ino),
            "producer changed while opening",
        )
        raw = stream.read()
        after = os.fstat(stream.fileno())
    require(
        (opened.st_size, opened.st_mtime_ns, opened.st_ctime_ns)
        == (after.st_size, after.st_mtime_ns, after.st_ctime_ns),
        "producer changed while reading",
    )
    require(
        (path.stat().st_dev, path.stat().st_ino) == (before.st_dev, before.st_ino),
        "producer substituted while reading",
    )
    return raw, (before.st_dev, before.st_ino)


def git(root, *args):
    result = subprocess.run(
        ["git", "--no-optional-locks", *args], cwd=root, capture_output=True, timeout=30
    )
    require(result.returncode == 0, "Git provenance command failed: " + " ".join(args))
    return result.stdout


def git_scope(root, contents):
    """Describe exact protected bytes relative to HEAD, including ignored inputs."""
    head = git(root, "rev-parse", "HEAD").decode().strip()
    entries = {}
    for entry in git(root, "ls-tree", "-rz", "--full-tree", head).split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        path = name.decode()
        if path in contents:
            mode, kind, oid = metadata.decode().split()
            require(kind == "blob" and mode in {"100644", "100755"}, "nonregular Git input")
            entries[path] = oid
    changes = {}
    for name, raw in contents.items():
        oid = entries.get(name)
        algorithm = hashlib.sha256 if oid and len(oid) == 64 else hashlib.sha1
        current_oid = algorithm(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if oid != current_oid:
            changes[name] = {"head_blob": oid, "sha256": sha(raw)}
    require(
        git(root, "rev-parse", "HEAD").decode().strip() == head, "Git HEAD moved during capture"
    )
    return {
        "git_revision": head,
        "state": "working_tree" if changes else "git_commit",
        "changed_inputs": changes,
    }


def runtime():
    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "packages": {name: importlib.metadata.version(name) for name in RUNTIME_PACKAGES},
    }


class Capture:
    def __init__(self, root, loader_bytes):
        self.root = Path(root).absolute()
        self.sources = {name: "src/" + name.replace(".", "/") + ".py" for name in MODULES}
        self.files = {
            path: capture_file(self.root / path) for path in (*self.sources.values(), *AUXILIARY)
        }
        require(self.files[LOADER][0] == loader_bytes, "loader changed before captured execution")
        self.git = git_scope(self.root, {path: raw for path, (raw, _) in self.files.items()})
        self.runtime = runtime()
        require(
            self.files[".python-version"][0].decode().strip()
            == ".".join(platform.python_version_tuple()[:2]),
            "runtime differs from maintained Python minor",
        )
        self.prefix = "_mim_source_capture_" + uuid.uuid4().hex + "."
        self.modules = {}
        self.packages = {}

    def verify(self):
        for path, (raw, identity) in self.files.items():
            current, current_identity = capture_file(self.root / path)
            require(
                current == raw and current_identity == identity,
                "executed producer/dependency changed: " + path,
            )
        require(
            git_scope(self.root, {path: raw for path, (raw, _) in self.files.items()}) == self.git,
            "executing producer Git context changed",
        )
        require(runtime() == self.runtime, "runtime dependencies changed")

    def imported(self, name, globals=None, locals=None, fromlist=(), level=0):
        if level == 0 and (
            name == "mediaingredientmech" or name.startswith("mediaingredientmech.")
        ):
            if name in self.sources:
                require(bool(fromlist), "unscoped native import")
                return self.load(name)
            require(bool(fromlist), "uncaptured native import")
            package = self.packages.setdefault(name, types.ModuleType(self.prefix + name))
            for item in fromlist:
                child = name + "." + item
                require(child in self.sources, "uncaptured native dependency: " + child)
                setattr(package, item, self.load(child))
            return package
        return builtins.__import__(name, globals, locals, fromlist, level)

    def load(self, name):
        if name in self.modules:
            return self.modules[name]
        path = self.sources[name]
        raw = self.files[path][0]
        module = types.ModuleType(self.prefix + name)
        module.__file__ = str(self.root / path)
        module.__package__ = name.rpartition(".")[0]
        module.__dict__.update(
            __builtins__={**vars(builtins), "__import__": self.imported},
            _SOURCE_BINDINGS_CAPTURED=True,
            _PRODUCER_CAPTURE=self,
        )
        self.modules[name] = module
        sys.modules[module.__name__] = module
        try:
            exec(compile(raw, module.__file__, "exec"), module.__dict__)
        except BaseException:
            self.modules.pop(name, None)
            sys.modules.pop(module.__name__, None)
            raise
        return module

    def bind(self, inputs):
        self.verify()
        for path, (raw, _) in self.files.items():
            require(
                inputs.read(path) == raw, "executing and selected producer bytes differ: " + path
            )

    def start_context(self, root):
        self.verify()
        return git(root, "rev-parse", "HEAD").decode().strip()

    def check_context(self, root, head):
        self.verify()
        require(
            git(root, "rev-parse", "HEAD").decode().strip() == head,
            "selected root Git HEAD changed",
        )

    def receipt(self, inputs):
        self.bind(inputs)
        selected = git_scope(inputs.root, inputs.bytes)
        return {
            "schema_version": 1,
            "status": "GENERATION_CONTEXT_ATTESTATION",
            "source_sha256": sha(self.files[SOURCE][0]),
            "files": {path: sha(raw) for path, (raw, _) in self.files.items()},
            "selected_context": selected,
            "runtime": self.runtime,
            "generation_origin": {
                "root": str(self.root),
                "executable": sys.executable,
                "module_paths": {
                    name: str(self.root / path) for name, path in self.sources.items()
                },
                "git_context": self.git,
            },
        }

    def validate_receipt(self, receipt, inputs):
        """Verify content/current endpoint; retain honest original origin attestation.

        A later validator can run equal compiled bytes at another owned location.
        Original absolute paths are descriptive metadata, never paths to execute
        or read, and never proof of scientific approval or author identity.
        """
        current = self.receipt(inputs)
        require(
            isinstance(receipt, dict) and set(receipt) == set(current), "invalid producer receipt"
        )
        for key in set(current) - {"generation_origin"}:
            require(receipt[key] == current[key], "producer receipt no longer matches: " + key)
        origin = receipt["generation_origin"]
        require(
            isinstance(origin, dict)
            and set(origin) == {"root", "executable", "module_paths", "git_context"},
            "invalid original generation origin",
        )
        require(
            isinstance(origin["root"], str)
            and Path(origin["root"]).is_absolute()
            and isinstance(origin["executable"], str)
            and Path(origin["executable"]).is_absolute(),
            "invalid origin paths",
        )
        require(
            origin["module_paths"]
            == {name: str(Path(origin["root"]) / path) for name, path in self.sources.items()},
            "invalid original module origins",
        )
        context = origin["git_context"]
        require(
            isinstance(context, dict)
            and set(context) == {"git_revision", "state", "changed_inputs"}
            and isinstance(context["git_revision"], str)
            and len(context["git_revision"]) in {40, 64}
            and set(context["git_revision"]) <= set("0123456789abcdef")
            and context["state"] in {"git_commit", "working_tree"}
            and isinstance(context["changed_inputs"], dict),
            "invalid original Git context",
        )
        require(
            context["state"] == ("working_tree" if context["changed_inputs"] else "git_commit"),
            "false clean generation state",
        )
        for name, change in context["changed_inputs"].items():
            require(
                name in self.files
                and isinstance(change, dict)
                and set(change) == {"head_blob", "sha256"}
                and change["sha256"] == sha(self.files[name][0]),
                "invalid original changed-producer pin",
            )
        return receipt


def captured_native_modules(root, loader_bytes):
    capture = Capture(root, loader_bytes)
    implementation = capture.load("mediaingredientmech.export.source_bindings")
    for name in MODULES:
        capture.load(name)
    capture.verify()
    return capture, implementation
