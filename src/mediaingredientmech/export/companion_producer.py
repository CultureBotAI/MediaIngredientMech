"""Bounded captured-byte execution for retained companion obligations (#1222).

Reuse the maintained source capture in a private namespace. Relative native
imports and packaged profile/schema reads also use captured bytes; no public
MIM module or resource cache can enter the opt-in execution path.
"""

from __future__ import annotations

import importlib.util
import os
import stat
import types
from pathlib import Path
from typing import Any

LOADER = "src/mediaingredientmech/export/companion_producer.py"
BASE = "src/mediaingredientmech/export/source_producer.py"
ENTRY = "mediaingredientmech.export.ingredient_bundle"
MODULES = (
    ENTRY,
    "mediaingredientmech.ingredient_bundle_contract",
    "mediaingredientmech.retained_companion",
    "mediaingredientmech.identity_projection_bundle",
    "mediaingredientmech.identity_projection_inventory",
    "mediaingredientmech.identity_projection",
    "mediaingredientmech.export.reviewed_sssom",
    "mediaingredientmech.native_acquisition",
    "mediaingredientmech.mapping_scope",
    "mediaingredientmech.review_claims",
    "mediaingredientmech.stable_ids",
    "mediaingredientmech.sssom_metadata",
    "mediaingredientmech.synonym_policy",
    "mediaingredientmech.curie",
)
RESOURCES = (
    "src/mediaingredientmech/profiles/ingredient_scope_v1.yaml",
    "src/mediaingredientmech/profiles/ingredient_bundle_v1.schema.json",
)
AUXILIARY = (LOADER, BASE, *RESOURCES, "uv.lock", "pyproject.toml", ".python-version")
PATHS = tuple("src/" + name.replace(".", "/") + ".py" for name in MODULES) + AUXILIARY


def _directories(path):
    result = []
    for parent in path.parents:
        info = parent.lstat()
        if not stat.S_ISDIR(info.st_mode):
            raise ValueError("Companion bootstrap: non-directory or aliased ancestor")
        result.append((parent, info.st_dev, info.st_ino))
    return result


def _bootstrap_bytes(path):
    """#1399 refuse disallowed helper origins before any helper code executes."""
    parents = _directories(path)
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
        raise ValueError("Companion bootstrap: nonregular or aliased helper")
    identity = (before.st_dev, before.st_ino)
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), "rb") as stream:
        opened = os.fstat(stream.fileno())
        if (opened.st_dev, opened.st_ino) != identity:
            raise ValueError("Companion bootstrap: helper changed while opening")
        raw = stream.read()
        after = os.fstat(stream.fileno())
    current = path.lstat()

    def snapshot(info):
        return (
            info.st_dev,
            info.st_ino,
            info.st_mode,
            info.st_nlink,
            info.st_size,
            info.st_mtime_ns,
            info.st_ctime_ns,
        )

    if not (
        snapshot(before) == snapshot(opened) == snapshot(after) == snapshot(current)
        and len(raw) == before.st_size
        and _directories(path) == parents
    ):
        raise ValueError("Companion bootstrap: helper or ancestor changed while reading")
    return raw, identity, parents


def load(root: Path, loader_bytes: bytes):
    root = Path(root).absolute()
    path = root / BASE
    raw, bootstrap_identity, bootstrap_parents = _bootstrap_bytes(path)
    helper: Any = types.ModuleType("_retained_companion_capture_base")
    helper.__file__ = str(path)
    exec(compile(raw, str(path), "exec"), helper.__dict__)
    helper.SOURCE = "src/" + ENTRY.replace(".", "/") + ".py"
    helper.LOADER = LOADER
    helper.MODULES = MODULES
    helper.AUXILIARY = AUXILIARY
    CaptureBase: Any = helper.Capture

    class Resource:
        def __init__(self, capture, relative="src/mediaingredientmech"):
            self.capture = capture
            self.relative = relative

        def joinpath(self, *names):
            return Resource(self.capture, "/".join((self.relative, *names)))

        def read_bytes(self):
            helper.require(self.relative in RESOURCES, "uncaptured companion resource")
            return self.capture.files[self.relative][0]

        def read_text(self, encoding="utf-8"):
            return self.read_bytes().decode(encoding)

    class Capture(CaptureBase):
        def imported(self, name, globals=None, locals=None, fromlist=(), level=0):
            if level:
                package = (globals or {}).get("__package__", "")
                if package == "mediaingredientmech" or package.startswith("mediaingredientmech."):
                    name = importlib.util.resolve_name("." * level + name, package)
                    level = 0
            if level == 0 and name == "importlib.resources":

                def files(package):
                    helper.require(package == "mediaingredientmech", "uncaptured resource package")
                    return Resource(self)

                return types.SimpleNamespace(files=files)
            return super().imported(name, globals, locals, fromlist, level)

        def load(self, name):
            module = super().load(name)
            module.__dict__["_RETAINED_CAPTURE"] = self
            return module

        def bind_review(self, review, sources):
            self.verify()
            for name, (content, _) in self.files.items():
                helper.require(
                    sources.get(name) == content
                    and review["inputs"].get(name) == helper.sha(content),
                    "retained executing/selected dependency differs: " + name,
                )

        def implementation(self):
            self.verify()
            return {
                "files": {name: helper.sha(raw) for name, (raw, _) in sorted(self.files.items())},
                "runtime": self.runtime,
            }

    capture = Capture(root, loader_bytes)
    helper.require(
        capture.files[BASE] == (raw, bootstrap_identity)
        and _directories(path) == bootstrap_parents,
        "capture helper or ancestor changed",
    )
    for name in MODULES:
        capture.load(name)
    capture.verify()
    return capture
