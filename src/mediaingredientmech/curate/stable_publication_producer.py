"""Private captured execution for guarded stable SSSOM publication (#1335).

Configure the existing capture implementation in a private namespace. Adoption
keeps its own original capture closure, so verifying an adoption does not silently
substitute this larger publication producer for the producer that performed it.
"""

import types
from pathlib import Path
from typing import Any

ENTRY = "mediaingredientmech.curate.stable_sssom_publication"
LOADER = "src/mediaingredientmech/curate/stable_publication_producer.py"
ADOPTION_LOADER = "src/mediaingredientmech/curate/adoption_producer.py"


def load(root: Path, loader_bytes: bytes):
    path = root / ADOPTION_LOADER
    raw = path.read_bytes()
    helper: Any = types.ModuleType("_stable_publication_capture")
    helper.__file__ = str(path)
    exec(compile(raw, str(path), "exec"), helper.__dict__)
    helper.ENTRY, helper.LOADER = ENTRY, LOADER
    helper.MODULES = (
        ENTRY,
        "mediaingredientmech.curate.publication_guard",
        "mediaingredientmech.curate.adoption_filesystem",
        "mediaingredientmech.curate.apply_receipt",
        "mediaingredientmech.export.reviewed_sssom",
        "mediaingredientmech.stable_ids",
        "mediaingredientmech.review_claims",
        "mediaingredientmech.mapping_scope",
        "mediaingredientmech.curie",
        "mediaingredientmech.synonym_policy",
        "mediaingredientmech.sssom_metadata",
        "mediaingredientmech.identity_projection",
    )
    helper.SCRIPTS = (
        *helper.SCRIPTS,
        ADOPTION_LOADER,
        "scripts/validate_sssom_invariants.py",
        "src/mediaingredientmech/curate/stable_sssom_replay.py",
    )
    capture, implementation = helper.load(root, loader_bytes)
    if capture.files[ADOPTION_LOADER][0] != raw:
        raise ValueError("Publication capture helper changed")
    return capture, implementation
