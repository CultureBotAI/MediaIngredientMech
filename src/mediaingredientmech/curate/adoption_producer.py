"""Bounded private captured execution for the #1303 operator.

Reuse the reviewed #1305 capture implementation, configured only in its fresh
private namespace. No public module is modified or reloaded. Script imports
compile captured bytes too, including the aggregator's dynamic exporter import.
"""

from __future__ import annotations

import importlib.abc
import importlib.util
import sys
import types
from pathlib import Path
from typing import Any

ENTRY = "mediaingredientmech.curate.stable_id_adoption"
LOADER = "src/mediaingredientmech/curate/adoption_producer.py"
BASE = "src/mediaingredientmech/export/source_producer.py"
MODULES = (
    ENTRY,
    "mediaingredientmech.mapping_scope",
    "mediaingredientmech.stable_ids",
    "mediaingredientmech.curie",
    "mediaingredientmech.curate.curation_event",
    "mediaingredientmech.curate.apply_receipt",
    "mediaingredientmech.curate.publication_guard",
    "mediaingredientmech.curate.adoption_filesystem",
    "mediaingredientmech.validation.write_validated",
    "mediaingredientmech.utils.yaml_handler",
)
SCRIPTS = (
    "scripts/record_review.py",
    "scripts/aggregate_records.py",
    "scripts/export_individual_records.py",
    "scripts/verify_roundtrip.py",
)
SCHEMAS = (
    "src/mediaingredientmech/schema/mediaingredientmech.yaml",
    "src/mediaingredientmech/schema/mech_shared.yaml",
    "src/mediaingredientmech/schema/history.yaml",
    "schema/record_review.yaml",
)


def load(root: Path, loader_bytes: bytes):
    # Compile the exact existing capture helper rather than importing a possibly
    # cached copy. Its own bytes join the captured closure before any API returns.
    helper_path = root / BASE
    raw = helper_path.read_bytes()
    helper: Any = types.ModuleType("_adoption_capture_base")
    helper.__file__ = str(helper_path)
    exec(compile(raw, str(helper_path), "exec"), helper.__dict__)
    helper.SOURCE = "src/" + ENTRY.replace(".", "/") + ".py"
    helper.LOADER = LOADER
    helper.MODULES = MODULES
    helper.AUXILIARY = (
        LOADER,
        BASE,
        "MAPPING_SEMANTICS.md",
        *SCRIPTS,
        *SCHEMAS,
        "uv.lock",
        "pyproject.toml",
        ".python-version",
    )

    CaptureBase: Any = helper.Capture

    class Capture(CaptureBase):
        def imported(self, name, globals=None, locals=None, fromlist=(), level=0):
            if name == "importlib.util" and level == 0:
                return types.SimpleNamespace(
                    util=types.SimpleNamespace(
                        spec_from_file_location=self.spec,
                        module_from_spec=importlib.util.module_from_spec,
                    )
                )
            return super().imported(name, globals, locals, fromlist, level)

        def spec(self, name, path):
            relative = str(Path(path).absolute().relative_to(self.root))
            helper.require(relative in self.files, "uncaptured script: " + relative)
            capture = self

            class ScriptLoader(importlib.abc.Loader):
                def create_module(self, spec):
                    return None

                def exec_module(self, module):
                    module.__file__ = str(capture.root / relative)
                    module.__dict__["__builtins__"] = {
                        **vars(__import__("builtins")),
                        "__import__": capture.imported,
                    }
                    exec(
                        compile(capture.files[relative][0], module.__file__, "exec"),
                        module.__dict__,
                    )

            return importlib.util.spec_from_loader(self.prefix + name, ScriptLoader())

        def script(self, path):
            spec = self.spec(path.replace("/", "_"), self.root / path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            return module

    capture = Capture(root, loader_bytes)
    helper.require(capture.files[BASE][0] == raw, "capture helper changed")
    implementation = capture.load(ENTRY)
    for name in MODULES:
        capture.load(name)
    capture.verify()
    return capture, implementation
