"""The reviewed 57-record #369 migration is finite and idempotent."""

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

from mediaingredientmech.validation.component_partonomy import (
    load_curated_records,
    validate_component_partonomy,
)

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "_migrate_component_partonomy", ROOT / "scripts" / "migrate_component_partonomy.py"
)
assert SPEC and SPEC.loader
MIGRATION = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MIGRATION
SPEC.loader.exec_module(MIGRATION)


def test_migration_is_idempotent_and_has_reviewed_final_inventory():
    records = load_curated_records(ROOT / "data" / "curated")
    first = deepcopy(records)
    assert MIGRATION.migrate(first) == (54, 3)
    assert validate_component_partonomy(first) == []

    second = deepcopy(first)
    assert MIGRATION.migrate(second) == (54, 3)
    assert second == first

    parents = [record for record in second if record.get("components")]
    scopes = [
        component["reference_scope"] for record in parents for component in record["components"]
    ]
    assert len(parents) == 54
    assert sum(len(record["components"]) for record in parents) == 143
    # 3 components moved EXTERNAL_TERM -> MIM_CATALOG when `clarified rumen fluid`
    # (MICRO:0000520) gained a MIM record. A component's scope is a fact about the
    # catalog, not about the migration, so grounding a referenced term legitimately
    # shifts the split. The total (143) is unchanged, which is what this guards.
    assert scopes.count("MIM_CATALOG") == 134
    assert scopes.count("EXTERNAL_TERM") == 7
    assert scopes.count("UNMAPPED") == 2

    by_label = {record["preferred_term"]: record for record in second}
    for label in MIGRATION.REMOVE_NON_PARTONOMY:
        assert "components" not in by_label[label]
        assert any(
            event.get("action") == "REMOVED_NON_PARTONOMIC_COMPONENTS"
            for event in by_label[label].get("curation_history") or []
        )
