"""Bounded captured-byte execution of the native CM verifier (#1431, KGM #1882).

Only the orchestration layer admits supported producer versions. This executor
retains parent-frozen file/ancestor identity across child startup, without
changing the qualified runtime's legitimate hardlink policy.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path

IDENTITY_FIELDS = (
    "st_dev",
    "st_ino",
    "st_mode",
    "st_nlink",
    "st_size",
    "st_mtime_ns",
    "st_ctime_ns",
)
ENVIRONMENT = {"PATH": "", "LANG": "C", "LC_ALL": "C", "TZ": "UTC"}
TIMEOUT_SECONDS = 300


def _require(condition, message):
    if not condition:
        raise ValueError("CM replay executor: " + message)


def _identity(value):
    return {name: getattr(value, name) for name in IDENTITY_FIELDS}


def _ancestors(path):
    result = []
    for parent in reversed(path.parents):
        value = parent.lstat()
        _require(stat.S_ISDIR(value.st_mode), "non-directory/symlink ancestor")
        result.append(
            {
                "path": str(parent),
                "st_dev": value.st_dev,
                "st_ino": value.st_ino,
                "st_mode": value.st_mode,
            }
        )
    return result


def freeze_file(path, *, source):
    """Capture bytes and physical identity; runtime hardlinks remain permitted."""
    path = Path(path).absolute()
    _require(str(path) == os.path.normpath(str(path)), "noncanonical file path")
    parents = _ancestors(path)
    before = path.lstat()
    _require(stat.S_ISREG(before.st_mode), "nonregular/symlink file")
    _require(not source or before.st_nlink == 1, "aliased source file")
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), "rb") as stream:
        opened = os.fstat(stream.fileno())
        _require(_identity(opened) == _identity(before), "file replaced before open")
        raw = stream.read()
        _require(
            _identity(os.fstat(stream.fileno())) == _identity(opened), "file changed while reading"
        )
    _require(_identity(path.lstat()) == _identity(before), "file replaced after read")
    _require(_ancestors(path) == parents, "ancestor replaced during capture")
    return {
        "path": str(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "identity": _identity(before),
        "ancestors": parents,
    }, raw


def check_frozen(value, *, source):
    current, raw = freeze_file(value["path"], source=source)
    _require(current == value, "frozen file or ancestor changed")
    return raw


# Deliberately standard-library-only. The child receives the parent's original
# identities, rather than trusting a new baseline after its interpreter starts.
BOOTSTRAP = r"""
import hashlib, json, os, stat, sys
FIELDS = ("st_dev", "st_ino", "st_mode", "st_nlink", "st_size", "st_mtime_ns", "st_ctime_ns")
def require(ok, message):
    if not ok:
        raise ValueError(message)
def unique(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, "duplicate payload key")
        value[key] = item
    return value
def keys(value, fields):
    require(isinstance(value, dict) and set(value) == set(fields), "invalid payload fields")
def identity(value):
    return {name: getattr(value, name) for name in FIELDS}
def check_path(path):
    require(isinstance(path, str) and os.path.isabs(path) and os.path.normpath(path) == path,
            "noncanonical path")
def parents(path):
    values = []
    parent = os.path.dirname(path)
    while True:
        values.append(parent)
        if parent == os.path.dirname(parent):
            return list(reversed(values))
        parent = os.path.dirname(parent)
def ancestors(value):
    require(isinstance(value["ancestors"], list), "invalid ancestors")
    require([item.get("path") for item in value["ancestors"]] == parents(value["path"]),
            "ancestor inventory differs")
    for item in value["ancestors"]:
        keys(item, ("path", "st_dev", "st_ino", "st_mode"))
        require(all(type(item[key]) is int for key in ("st_dev", "st_ino", "st_mode")),
                "invalid ancestor identity")
        current = os.lstat(item["path"])
        require(stat.S_ISDIR(current.st_mode) and all(getattr(current, key) == item[key]
                for key in ("st_dev", "st_ino", "st_mode")), "frozen ancestor changed")
def read(value, source):
    keys(value, ("path", "sha256", "identity", "ancestors"))
    check_path(value["path"])
    require(isinstance(value["sha256"], str) and len(value["sha256"]) == 64
            and all(c in "0123456789abcdef" for c in value["sha256"]), "invalid digest")
    keys(value["identity"], FIELDS)
    require(all(type(item) is int for item in value["identity"].values()), "invalid file identity")
    ancestors(value)
    before = os.lstat(value["path"])
    require(stat.S_ISREG(before.st_mode) and (not source or before.st_nlink == 1),
            "nonregular/aliased source")
    require(identity(before) == value["identity"], "frozen file changed")
    with os.fdopen(os.open(value["path"], os.O_RDONLY | os.O_NOFOLLOW), "rb") as stream:
        require(identity(os.fstat(stream.fileno())) == value["identity"], "file changed at open")
        raw = stream.read()
        require(identity(os.fstat(stream.fileno())) == value["identity"], "file changed at read")
    require(hashlib.sha256(raw).hexdigest() == value["sha256"], "file digest changed")
    require(identity(os.lstat(value["path"])) == value["identity"], "file changed after read")
    ancestors(value)
    return raw
try:
    require(len(sys.argv) == 2, "unexpected bootstrap arguments")
    plan = json.loads(sys.argv[1], object_pairs_hook=unique)
    keys(plan, ("schema_version", "script", "executable", "argv"))
    require(type(plan["schema_version"]) is int and plan["schema_version"] == 1, "unknown bootstrap")
    require(os.path.realpath(sys.executable) == plan["executable"]["path"], "interpreter differs")
    read(plan["executable"], False)
    raw = read(plan["script"], True)
    argv = plan["argv"]
    require(isinstance(argv, list) and len(argv) == 6 and all(isinstance(v, str) for v in argv),
            "invalid verifier argv")
    require(argv[0] == plan["script"]["path"] and argv[1] == "verify"
            and argv[2] == "--bundle-dir" and argv[4] == "--expected-manifest-sha256",
            "non-verifier invocation")
    check_path(argv[3])
    require(len(argv[5]) == 64 and all(c in "0123456789abcdef" for c in argv[5]), "invalid manifest pin")
    code = compile(raw, plan["script"]["path"], "exec")
except Exception as exc:
    print("MIM_CM_BOOTSTRAP_REFUSAL: " + str(exc), file=sys.stderr)
    raise SystemExit(125)
sys.argv = argv
exec(code, {"__name__": "__main__", "__file__": plan["script"]["path"], "__package__": None})
"""


def prepare_plan(script, bundle, manifest_pin, *, executable=None):
    script_snapshot, _ = freeze_file(script, source=True)
    # Resolving the existing qualified interpreter does not change that runtime.
    runtime = Path(executable or sys.executable).resolve(strict=True)
    runtime_snapshot, _ = freeze_file(runtime, source=False)
    return {
        "schema_version": 1,
        "script": script_snapshot,
        "executable": runtime_snapshot,
        "argv": [
            str(Path(script).absolute()),
            "verify",
            "--bundle-dir",
            str(Path(bundle).absolute()),
            "--expected-manifest-sha256",
            manifest_pin,
        ],
    }


def execute_plan(plan, *, cwd):
    """Run real captured code; caller has already admitted its supported version."""
    # These prechecks are intentionally repeated inside the child against the
    # same parent snapshot, so a late same-byte replacement never becomes truth.
    check_frozen(plan["script"], source=True)
    check_frozen(plan["executable"], source=False)
    command = [
        plan["executable"]["path"],
        "-I",
        "-S",
        "-B",
        "-c",
        BOOTSTRAP,
        json.dumps(plan, sort_keys=True, separators=(",", ":")),
    ]
    result = subprocess.run(
        command,
        cwd=cwd,
        env=ENVIRONMENT.copy(),
        text=True,
        encoding="utf-8",
        errors="strict",
        capture_output=True,
        check=True,
        timeout=TIMEOUT_SECONDS,
    )
    check_frozen(plan["script"], source=True)
    check_frozen(plan["executable"], source=False)
    return result


class VerifierProcess:
    """Private import facade for the one authentic historical subprocess call."""

    def __init__(self, plan, original_python, producer):
        self.plan = plan
        self.original_python = str(original_python)
        self.producer = Path(producer).absolute()

    def run(self, command, **kwargs):
        expected = [
            self.original_python,
            "scripts/ingredient_release_bundle.py",
            *self.plan["argv"][1:],
        ]
        _require(command == expected, "unexpected historical child argv")
        _require(
            set(kwargs) == {"cwd", "text", "capture_output", "check"},
            "unexpected historical child options",
        )
        _require(Path(kwargs["cwd"]).absolute() == self.producer, "unexpected child cwd")
        _require(
            all(kwargs[name] is True for name in ("text", "capture_output", "check")),
            "unexpected historical subprocess semantics",
        )
        return execute_plan(self.plan, cwd=self.producer)
