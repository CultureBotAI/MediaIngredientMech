#!/usr/bin/env python3
"""Migrate legacy `media_roles` assignments onto the three role facets (MIM #128).

Step 4 of the facet migration: `IngredientRoleEnum` / `RoleAssignment` /
`media_roles` are retired, so every existing assignment must be rehomed onto
`nutritional_roles`, `physicochemical_roles`, or `cellular_metabolic_roles`.

Routing
-------
18 of the 20 legacy values share a name with a value on exactly one facet enum;
those route mechanically and losslessly (`DIRECT_ROUTING`). The two that do not:

* ``MINERAL`` — used by curators as a catch-all across trace metals, iron,
  sulfate, phosphate, and bulk cations. Routed per-record from the mapped
  ontology term's molecular formula (``mineral_targets``), so the result is
  deterministic and auditable rather than a single lossy guess. A handful of
  records tagged MINERAL are not minerals at all (the nitrilotriacetate
  chelators, the tartrate/acetate organic salts); those are named explicitly in
  ``SPECIAL_CASES``.
* ``SALT`` — all six occurrences are mis-assignments (DMSO, distilled water,
  ethanol, HCl, methanol, triethanolamine are not salts contributing ionic
  strength). Mapping them onto ``OSMOTIC_AGENT`` would launder bad data into the
  new schema, so they are dropped.

Dropped assignments are never silent: each one is recorded as a ``CORRECTED``
curation_history event on its record and written to the report TSV.

Usage
-----
    python scripts/migrate_media_roles_to_facets.py --dry-run
    python scripts/migrate_media_roles_to_facets.py --apply
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Optional

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.curate.curation_event import (  # noqa: E402
    now_iso,
    record_curation_event,
)
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

#: Single timestamp for the whole run, so every event this migration writes
#: shares one identifiable point in the audit trail.
CURATOR = "migrate_media_roles_to_facets"
RUN_TIMESTAMP = now_iso()

NUTRITIONAL = "nutritional_roles"
PHYSICOCHEMICAL = "physicochemical_roles"
CELLULAR = "cellular_metabolic_roles"

#: Legacy value -> (facet slot, facet enum value). Name-identical in all 18 cases.
DIRECT_ROUTING: dict[str, tuple[str, str]] = {
    "CARBON_SOURCE": (NUTRITIONAL, "CARBON_SOURCE"),
    "NITROGEN_SOURCE": (NUTRITIONAL, "NITROGEN_SOURCE"),
    "TRACE_ELEMENT": (NUTRITIONAL, "TRACE_ELEMENT"),
    "VITAMIN_SOURCE": (NUTRITIONAL, "VITAMIN_SOURCE"),
    "PROTEIN_SOURCE": (NUTRITIONAL, "PROTEIN_SOURCE"),
    "AMINO_ACID_SOURCE": (NUTRITIONAL, "AMINO_ACID_SOURCE"),
    "ENERGY_SOURCE": (NUTRITIONAL, "ENERGY_SOURCE"),
    "COFACTOR_PROVIDER": (NUTRITIONAL, "COFACTOR_PROVIDER"),
    "BUFFER": (PHYSICOCHEMICAL, "BUFFER"),
    "SOLIDIFYING_AGENT": (PHYSICOCHEMICAL, "SOLIDIFYING_AGENT"),
    "CHELATOR": (PHYSICOCHEMICAL, "CHELATOR"),
    "SURFACTANT": (PHYSICOCHEMICAL, "SURFACTANT"),
    "REDUCING_AGENT": (PHYSICOCHEMICAL, "REDUCING_AGENT"),
    "PH_INDICATOR": (PHYSICOCHEMICAL, "PH_INDICATOR"),
    "REDOX_INDICATOR": (PHYSICOCHEMICAL, "REDOX_INDICATOR"),
    "SELECTIVE_AGENT": (PHYSICOCHEMICAL, "SELECTIVE_AGENT"),
    "ELECTRON_DONOR": (CELLULAR, "ELECTRON_DONOR"),
    "ELECTRON_ACCEPTOR": (CELLULAR, "ELECTRON_ACCEPTOR"),
}

#: Micronutrient metals/halogens supplied in trace amounts. Presence of any of
#: these in the formula makes TRACE_ELEMENT the salient nutritional role.
TRACE_ELEMENTS = (
    "Co", "Cu", "Mn", "Zn", "Ni", "Mo", "W", "V", "Se", "B",
    "Al", "Ba", "Sr", "Sn", "Li", "Cr", "I", "F", "Br",
)

#: Bulk mineral cations -> the residual MINERAL_SOURCE bucket.
BULK_CATIONS = ("Mg", "Ca", "K", "Na")

#: Records tagged MINERAL that are not mineral nutrients. Keyed by preferred_term.
#: Value is a list of (facet slot, value) pairs, or None to drop the assignment.
SPECIAL_CASES: dict[str, Optional[list[tuple[str, str]]]] = {
    # Nitrilotriacetate family: metal chelators used to keep trace metals soluble.
    "NTA": [(PHYSICOCHEMICAL, "CHELATOR")],
    "Nitrilotriacetate": [(PHYSICOCHEMICAL, "CHELATOR")],
    "Nitrilotriacetic acid": [(PHYSICOCHEMICAL, "CHELATOR")],
    "0.5 M Nitrilotriacetic acid, disodium salt": [(PHYSICOCHEMICAL, "CHELATOR")],
    # Organic-acid salts: the organic anion is the nutritionally salient part.
    "Na-tartrate": [(NUTRITIONAL, "CARBON_SOURCE")],
    "Sodium tartrate": [(NUTRITIONAL, "CARBON_SOURCE")],
    "K-acetate": [(NUTRITIONAL, "CARBON_SOURCE")],
    "Magnesium acetate": [(NUTRITIONAL, "CARBON_SOURCE"), (NUTRITIONAL, "MINERAL_SOURCE")],
    # pH adjusters, not mineral nutrients. No facet value fits; drop for re-curation.
    "H2SO4": None,
    "KOH": None,
}

#: Every SALT assignment in the corpus is a mis-assignment; drop them all.
SALT_IS_MISASSIGNED = True

DROP_REASON_SALT = (
    "legacy media_roles SALT assignment dropped during the #128 facet migration: "
    "this ingredient is not a salt contributing ionic strength or osmotic balance, "
    "so the assignment was a mis-curation rather than a role to rehome. "
    "Re-curate onto PhysicochemicalRoleEnum.OSMOTIC_AGENT only if warranted."
)
DROP_REASON_MINERAL = (
    "legacy media_roles MINERAL assignment dropped during the #128 facet migration: "
    "this ingredient supplies no mineral nutrient (it is a solvent or a pH "
    "adjuster), so no NutritionalRoleEnum value applies. Flagged for curator re-review."
)

_ELEMENT_RE = re.compile(r"[A-Z][a-z]?")


def formula_elements(formula: str) -> set[str]:
    """Return the set of element symbols appearing in a molecular formula.

    ChEBI formulae for salts and hydrates use a dot-separated component form
    (e.g. ``Cl2Fe.4H2O``, ``2H4N.Ni.2O4S``); a plain symbol scan is sufficient
    because we only ever ask "is element X present?".
    """
    return set(_ELEMENT_RE.findall(formula or ""))


def mineral_targets(record: dict[str, Any]) -> Optional[list[tuple[str, str]]]:
    """Decide which facet role(s) a MINERAL assignment becomes for this record.

    Returns a list of (slot, value) pairs, or None if the assignment should be
    dropped. Priority reflects nutritional salience: a trace metal or iron
    dominates its counter-ion, so CuSO4 is a TRACE_ELEMENT source rather than a
    sulfur source. Sulfur and phosphate only count when paired with a bulk
    cation, where the anion really is the nutrient being supplied.
    """
    term = record.get("preferred_term")
    if term in SPECIAL_CASES:
        return SPECIAL_CASES[term]

    formula = ((record.get("chemical_properties") or {}).get("molecular_formula")) or ""
    elements = formula_elements(formula)
    label = ((record.get("ontology_mapping") or {}).get("ontology_label") or "").lower()

    targets: list[tuple[str, str]] = []
    has_trace = bool(elements & set(TRACE_ELEMENTS))
    has_iron = "Fe" in elements

    if has_trace:
        targets.append((NUTRITIONAL, "TRACE_ELEMENT"))
    if has_iron:
        targets.append((NUTRITIONAL, "IRON_SOURCE"))
    if "P" in elements:
        targets.append((NUTRITIONAL, "PHOSPHATE_SOURCE"))

    # Sulfur is a nutrient here only when it is not just a trace-metal or iron
    # counter-ion — i.e. elemental sulfur, or a sulfate paired with a bulk cation.
    if "S" in elements and not (has_trace or has_iron):
        targets.append((NUTRITIONAL, "SULFUR_SOURCE"))

    # Bulk cations fill the residual bucket, but only when nothing more specific
    # already described what the ingredient supplies.
    if not targets and (elements & set(BULK_CATIONS)):
        targets.append((NUTRITIONAL, "MINERAL_SOURCE"))

    # Formula-free records (e.g. elemental sulfur has no formula on the record)
    # fall back to the ontology label.
    if not targets:
        if "sulfur" in label or "sulphur" in label:
            targets.append((NUTRITIONAL, "SULFUR_SOURCE"))
        elif "iron" in label:
            targets.append((NUTRITIONAL, "IRON_SOURCE"))

    return targets or None


def convert_assignment(
    assignment: dict[str, Any], slot: str, value: str
) -> dict[str, Any]:
    """Rebuild a legacy RoleAssignment as a facet assignment.

    `confidence`, `evidence`, and `notes` carry over unchanged — the facet
    assignment classes declare the same attributes. Only `role` is rewritten.
    """
    converted: dict[str, Any] = {"role": value}
    if "confidence" in assignment:
        converted["confidence"] = assignment["confidence"]
    if assignment.get("evidence"):
        converted["evidence"] = assignment["evidence"]
    if assignment.get("notes"):
        converted["notes"] = assignment["notes"]
    return converted


def append_unique(record: dict[str, Any], slot: str, assignment: dict[str, Any]) -> bool:
    """Append `assignment` to `record[slot]` unless that role is already present."""
    existing = record.get(slot)
    if not isinstance(existing, list):
        existing = []
        record[slot] = existing
    if any(a.get("role") == assignment["role"] for a in existing if isinstance(a, dict)):
        return False
    existing.append(assignment)
    return True


def add_event(record: dict[str, Any], action: str, changes: str) -> None:
    """Append a CurationEvent via the shared helper.

    Routed through ``record_curation_event`` rather than appending a dict by
    hand: CurationEvent requires a `timestamp` (datetime), and hand-built events
    are how you end up writing a `date` the schema rejects.
    """
    record_curation_event(
        record,
        curator=CURATOR,
        action=action,
        changes=changes,
        timestamp=RUN_TIMESTAMP,
    )


def migrate_record(record: dict[str, Any], stats: Counter, dropped: list) -> bool:
    """Rehome one record's media_roles. Returns True if the record changed."""
    legacy = record.get("media_roles")
    if not legacy:
        # Still strip an empty/None slot so the retired field leaves no residue.
        if "media_roles" in record:
            del record["media_roles"]
            return True
        return False

    term = record.get("preferred_term") or record.get("identifier") or "?"
    moved: list[str] = []

    for assignment in legacy:
        if not isinstance(assignment, dict):
            continue
        role = assignment.get("role")

        if role in DIRECT_ROUTING:
            targets: Optional[list[tuple[str, str]]] = [DIRECT_ROUTING[role]]
        elif role == "MINERAL":
            targets = mineral_targets(record)
        elif role == "SALT":
            targets = None if SALT_IS_MISASSIGNED else [(PHYSICOCHEMICAL, "OSMOTIC_AGENT")]
        else:
            raise ValueError(f"Unroutable legacy role {role!r} on record {term!r}")

        if not targets:
            reason = DROP_REASON_SALT if role == "SALT" else DROP_REASON_MINERAL
            dropped.append((term, record.get("identifier"), role, reason))
            stats[f"DROPPED:{role}"] += 1
            add_event(record, "CORRECTED", f"Dropped media_roles role {role}: {reason}")
            continue

        for slot, value in targets:
            if append_unique(record, slot, convert_assignment(assignment, slot, value)):
                stats[f"{role} -> {slot}:{value}"] += 1
                moved.append(f"{role} -> {slot}.{value}")
            else:
                stats[f"DEDUPED:{role} -> {slot}:{value}"] += 1

    del record["media_roles"]
    if moved:
        add_event(
            record,
            "ANNOTATED",
            "Migrated legacy media_roles to role facets (#128): " + "; ".join(moved),
        )
    return True


def iter_record_files() -> list[Path]:
    return sorted(
        Path(p) for p in glob.glob(str(REPO_ROOT / "data/ingredients/**/*.yaml"), recursive=True)
    )


def dump_yaml(path: Path, data: Any) -> None:
    """Write via the shared helper so formatting matches every other writer.

    Hand-rolling ``yaml.dump`` here (particularly with a non-default ``width``)
    reflows lines the migration never touched and buries the real change in a
    reformatting diff.
    """
    save_yaml(data, path, backup=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Report without writing.")
    group.add_argument("--apply", action="store_true", help="Write the migration to disk.")
    parser.add_argument(
        "--report",
        default=str(REPO_ROOT / "reports/media_roles_facet_migration.tsv"),
        help="Where to write the per-assignment migration report.",
    )
    args = parser.parse_args()

    stats: Counter = Counter()
    dropped: list = []
    changed_files = 0

    for path in iter_record_files():
        record = yaml.safe_load(open(path))
        if not isinstance(record, dict):
            continue
        if migrate_record(record, stats, dropped):
            changed_files += 1
            if args.apply:
                dump_yaml(path, record)

    # The aggregate collection mirrors the per-record files; migrate it in place
    # so the two stay consistent without a full re-aggregation.
    collection_path = REPO_ROOT / "data/curated/mapped_ingredients.yaml"
    coll_stats: Counter = Counter()
    coll_dropped: list = []
    collection = yaml.safe_load(open(collection_path))
    coll_changed = 0
    for record in collection.get("ingredients", []):
        if isinstance(record, dict) and migrate_record(record, coll_stats, coll_dropped):
            coll_changed += 1
    if args.apply and coll_changed:
        dump_yaml(collection_path, collection)

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"=== media_roles -> facet migration [{mode}] ===\n")
    print(f"per-record files changed: {changed_files}")
    print(f"collection records changed: {coll_changed}\n")
    print("routing counts (per-record files):")
    for key, count in sorted(stats.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {count:5d}  {key}")

    if dropped:
        print(f"\ndropped assignments ({len(dropped)}):")
        for term, identifier, role, _ in dropped:
            print(f"  {role:8s} {term} ({identifier})")

    report_path = Path(args.report)
    if args.apply:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w") as fh:
            fh.write("preferred_term\tidentifier\tlegacy_role\tdisposition\treason\n")
            for term, identifier, role, reason in dropped:
                fh.write(f"{term}\t{identifier}\t{role}\tDROPPED\t{reason}\n")
        print(f"\nDropped-assignment report: {report_path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
