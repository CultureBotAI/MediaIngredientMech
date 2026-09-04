#!/usr/bin/env python3
"""Type the existing MicrobeDecoder component decompositions for issue #369.

The migration is deliberately finite and reviewable: every current component
parent is classified below.  It adds explicit local/external/unmapped reference
scope plus record-level method/evidence, and removes three legacy lists that were
not has-part assertions at all.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.validation.component_partonomy import (  # noqa: E402
    validate_component_partonomy,
)
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    write_validated_ingredient,
)

INGREDIENTS_DIR = REPO_ROOT / "data" / "ingredients"
CURATED_DECOMPOSITIONS = (
    REPO_ROOT / "mappings" / "microbedecoder_residual_research_decomposition.tsv"
)
STAMP = "2026-08-24T00:00:00+00:00"
CURATOR = "migrate_component_partonomy"

LABEL_ENUMERATION = frozenset(
    {
        "1-butanol+CO2",
        "1-propanol+CO2",
        "2-butanol+CO2",
        "2-propanol+CO2",
        "Casitone + Yeast Extract + Rumen Fluid",
        "Corn Steep Liquor + Glucose + Fumarate",
        "Cyclopentanol+CO2",
        "Esculin Ferric Citrate",
        "Formate+3-methyl Mercaptopropionate",
        "Formate+dimethylsulfide",
        "Formate+methanol",
        "Formate+tetramethylammonium",
        "Formate+trimethylamine",
        "Gallate + Formate",
        "Glucose + Acetate",
        "Glucose + Cellobiose + Starch + Trypticase + Yeast Extract",
        "Glucose + Formate",
        "Glucose + Lactate",
        "Glucose + Maltose + Cellobiose + Starch + Glycerol",
        "Glucose + Xylose",
        "Glucose + Yeast Extract",
        "Glucose Peptone-yeast Extract",
        "H2 + CO2",
        "H2+3-methyl Mercaptopropionate",
        "H2+dimethylsulfide",
        "H2+methanol",
        "H2+tetramethylammonium",
        "H2+trimethylamine",
        "Peptone + Beef Extract + Yeast Extract",
        "Peptone + Yeast Extract",
        "Peptone-yeast Extract-glucose",
        "Sucrose + Yeast Extract",
        "Trypticase-glucose-yeast Extract",
        "Tryptone/yeast/beef (tyb)",
        "Yeast + Meat Extract + H2",
        "Yeast Extract + Gluconate",
        "Yeast Extract + Glucose",
        "Yeast Extract + Peptone",
        "Yeast Extract + Sulfur",
    }
)

ABBREVIATION_EXPANSION = frozenset(
    {
        "CMC + PY + Horse Serum",
        "GYPS",
        "PY-cellobiose",
        "PY-fructose",
        "PY-glucose-rumen Fluid",
        "PY-maltose",
        "PY-pectin",
        "PYEG",
        "PYG",
        "PYG + Rumen Fluid",
        "PYG-0.02% Tween 80",
        "PYGS",
        "TYGVS + Glucose",
    }
)

PARTIAL_MEDIUM_COMPOSITION = frozenset(
    {
        "Fastidious Anaerobe Broth With Meat Granules",
        "Modified Cooked Meat Medium",
    }
)

MIGRATED_COMPONENT_PARENTS = LABEL_ENUMERATION | ABBREVIATION_EXPANSION | PARTIAL_MEDIUM_COMPOSITION

REMOVE_NON_PARTONOMY = {
    "BHI": (
        "BHI to MICRO:0000193 brain heart infusion is a whole-medium identity/alias "
        "claim, not a has-part edge. The component was removed; identity cleanup must "
        "be handled separately."
    ),
    "Fermented Rumen Extract": (
        "Clarified rumen fluid is a related source material/interpretation, not an "
        "asserted physical constituent of fermented rumen extract."
    ),
    "Mono- And Disaccharides": (
        "Monosaccharide and disaccharide are category members named by a coordinated "
        "class label, not physical constituents of a mixture."
    ),
}


def _normalise(value: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(value or "").casefold())


def _curated_rows() -> dict[str, dict[str, str]]:
    with CURATED_DECOMPOSITIONS.open(encoding="utf-8", newline="") as handle:
        return {
            _normalise(row["source_label"]): row for row in csv.DictReader(handle, delimiter="\t")
        }


def _insert_after(record: dict[str, Any], anchor: str, key: str, value: Any) -> None:
    """Set ``key`` immediately after ``anchor`` without disturbing other key order."""

    items: list[tuple[str, Any]] = []
    inserted = False
    for old_key, old_value in record.items():
        if old_key == key:
            continue
        items.append((old_key, old_value))
        if old_key == anchor:
            items.append((key, value))
            inserted = True
    if not inserted:
        items.append((key, value))
    record.clear()
    record.update(items)


def _typed_component(component: dict[str, Any], active_ids: set[str]) -> dict[str, Any]:
    component_id = str(component.get("component_id") or "").strip()
    if not component_id:
        scope = "UNMAPPED"
    elif component_id in active_ids:
        scope = "MIM_CATALOG"
    else:
        scope = "EXTERNAL_TERM"

    typed: dict[str, Any] = {}
    for key, value in component.items():
        if key == "reference_scope":
            continue
        typed[key] = value
        if key == "component_id":
            typed["reference_scope"] = scope
    if "reference_scope" not in typed:
        _insert_after(typed, "component_name", "reference_scope", scope)
    return typed


def _evidence(label: str, method: str, curated: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    row = curated.get(_normalise(label))
    if method == "LABEL_ENUMERATION":
        evidence = [
            {
                "evidence_type": "SOURCE_LABEL",
                "source": "microbedecoder",
                "source_record": label,
                "notes": "The source label explicitly names every retained top-level part.",
            }
        ]
        if row:
            evidence.append(
                {
                    "evidence_type": "CURATED_DATASET",
                    "source": "mappings/microbedecoder_residual_research_decomposition.tsv",
                    "source_record": row["source_label"],
                    "notes": (
                        f"Reviewed row: strategy={row['strategy']}, "
                        f"confidence={row['confidence']}; {row['note']}"
                    ),
                }
            )
        return evidence

    if row:
        return [
            {
                "evidence_type": "CURATED_DATASET",
                "source": "mappings/microbedecoder_residual_research_decomposition.tsv",
                "source_record": row["source_label"],
                "notes": (
                    f"Reviewed row: strategy={row['strategy']}, "
                    f"confidence={row['confidence']}; {row['note']}"
                ),
            }
        ]
    return [
        {
            "evidence_type": "MANUAL_CURATION",
            "source": "scripts/decompose_py_media_and_ground_categories.py",
            "source_record": label,
            "notes": "The checked-in curation script records this expansion explicitly.",
        }
    ]


def _classification(label: str) -> tuple[str, str] | None:
    if label in LABEL_ENUMERATION:
        return "LABEL_ENUMERATION", "COMPLETE"
    if label in ABBREVIATION_EXPANSION:
        return "ABBREVIATION_EXPANSION", "UNKNOWN"
    if label in PARTIAL_MEDIUM_COMPOSITION:
        return "CURATED_INTERPRETATION", "PARTIAL"
    return None


def _history(record: dict[str, Any], action: str, changes: str) -> None:
    history = record.setdefault("curation_history", [])
    for event in history:
        if event.get("action") == action and event.get("curator") == CURATOR:
            event["changes"] = changes
            return
    history.append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": action,
            "changes": changes,
            "llm_assisted": False,
        }
    )


def migrate(records: list[dict[str, Any]]) -> tuple[int, int]:
    """Mutate ``records`` and return (typed, removed) record counts."""

    expected = MIGRATED_COMPONENT_PARENTS | set(REMOVE_NON_PARTONOMY)
    migration_records = [
        record for record in records if str(record.get("preferred_term") or "") in expected
    ]
    before_parent_count = sum(bool(record.get("components")) for record in migration_records)
    before_component_count = sum(
        len(record.get("components") or []) for record in migration_records
    )
    if (before_parent_count, before_component_count) not in {(57, 147), (54, 143)}:
        raise ValueError(
            "component inventory is neither the reviewed pre-migration 57/147 nor "
            f"the migrated 54/143 state: {before_parent_count}/{before_component_count}"
        )

    active_ids = {
        str(record["identifier"])
        for record in records
        if record.get("identifier") and record.get("mapping_status") != "REJECTED"
    }
    curated = _curated_rows()
    seen: set[str] = set()
    typed_count = removed_count = 0

    for record in records:
        label = str(record.get("preferred_term") or "")
        components = record.get("components") or []
        if label in REMOVE_NON_PARTONOMY:
            already_migrated = any(
                event.get("action") == "REMOVED_NON_PARTONOMIC_COMPONENTS"
                and event.get("curator") == CURATOR
                for event in record.get("curation_history") or []
            )
            if components or already_migrated:
                seen.add(label)
                record.pop("components", None)
                record.pop("component_assertion", None)
                ontology_mapping = record.get("ontology_mapping") or {}
                ontology_mapping["evidence"] = [
                    {
                        "evidence_type": "MANUAL_CURATION",
                        "source": "MIM curation (#369)",
                        "notes": (
                            "Registry identity retained while the whole-record grounding "
                            f"is reviewed separately. Corrected prior active evidence: "
                            f"{REMOVE_NON_PARTONOMY[label]}"
                        ),
                    }
                ]
                _history(
                    record,
                    "REMOVED_NON_PARTONOMIC_COMPONENTS",
                    f"#369: {REMOVE_NON_PARTONOMY[label]} Replaced the active mapping "
                    "evidence that described the false component claim; registry identity "
                    "and ingredient type were not changed.",
                )
                removed_count += 1
            continue

        if not components:
            continue

        classification = _classification(label)
        if classification is None:
            continue
        seen.add(label)
        method, completeness = classification
        typed_components = [_typed_component(component, active_ids) for component in components]
        record["components"] = typed_components
        assertion = {
            "method": method,
            "completeness": completeness,
            "evidence": _evidence(label, method, curated),
            "notes": (
                "This is an ingredient/mixture has-part assertion, not an identity "
                "mapping, variant hierarchy, or complete culturing recipe."
            ),
        }
        _insert_after(record, "components", "component_assertion", assertion)
        scopes = {component["reference_scope"] for component in typed_components}
        _history(
            record,
            "TYPED_COMPONENT_PARTONOMY",
            f"#369: added method/evidence/completeness and explicit reference scope "
            f"to {len(typed_components)} existing component(s) ({', '.join(sorted(scopes))}); "
            "constituent names, identifiers, and concentrations were not changed.",
        )
        typed_count += 1

    missing = expected - seen
    unexpected = seen - expected
    if missing or unexpected:
        raise ValueError(
            f"component-parent inventory drift: missing={sorted(missing)!r}, "
            f"unexpected={sorted(unexpected)!r}"
        )

    after_parents = [
        record
        for record in records
        if record.get("preferred_term") in MIGRATED_COMPONENT_PARENTS and record.get("components")
    ]
    after_component_count = sum(len(record["components"]) for record in after_parents)
    scope_counts: dict[str, int] = {}
    for record in after_parents:
        for component in record["components"]:
            scope = str(component.get("reference_scope"))
            scope_counts[scope] = scope_counts.get(scope, 0) + 1
    # 3 components moved EXTERNAL_TERM -> MIM_CATALOG when `clarified rumen fluid`
    # (MICRO:0000520) gained a MIM record: a component's scope is a fact about the
    # catalog, not about the migration, so grounding a referenced term legitimately
    # shifts this inventory. The total is unchanged, which is what the guard is for.
    expected_scopes = {"MIM_CATALOG": 134, "EXTERNAL_TERM": 7, "UNMAPPED": 2}
    if len(after_parents) != 54 or after_component_count != 143 or scope_counts != expected_scopes:
        raise ValueError(
            "post-migration inventory drift: "
            f"parents={len(after_parents)}, components={after_component_count}, "
            f"scopes={scope_counts!r}"
        )
    return typed_count, removed_count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    paths = sorted(INGREDIENTS_DIR.rglob("*.yaml"))
    records = [yaml.safe_load(path.read_text(encoding="utf-8")) or {} for path in paths]
    typed, removed = migrate(records)
    violations = validate_component_partonomy(records)
    if violations:
        for violation in violations:
            print(violation, file=sys.stderr)
        print(f"error: migrated corpus has {len(violations)} violation(s)", file=sys.stderr)
        return 2

    if args.apply:
        for path, record in zip(paths, records, strict=True):
            if record.get("component_assertion") or any(
                event.get("curator") == CURATOR for event in record.get("curation_history") or []
            ):
                write_validated_ingredient(record, path)
    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"{mode}: {typed} typed decompositions, {removed} non-partonomies removed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
