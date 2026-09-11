#!/usr/bin/env python3
"""Mint local identities for variable sulfate hydrates grounded to anhydrous terms.

MAPPING_SEMANTICS.md Section 3 says a hydrate record should use an exact
hydrate term when one exists, then its own CAS when one exists, then a local
registry identity with a parent row. The two variable hydrate labels here are
past the first two cases:

* `CHEBI:53471` is anhydrous chromium(III) sulfate and has CAS 10101-53-8.
* `CHEBI:53438` is anhydrous iron(3+) sulfate and has CAS 10028-22-5.

`Cr2(SO4)3 x n H2O` and `Fe2(SO4)3 x n H2O` name variable hydration states,
so exact-matching them to those anhydrous ChEBI terms publishes the wrong
identity and leaks anhydrous exact synonyms into SSSOM `other`. Mint a
`kgmicrobe.compound:` identity for each, keep the anhydrous ChEBI term only as
the nearest parent under MIM's current narrowMatch convention, and move the
CultureMech membership edges to the newly minted identifiers.

    python scripts/fix_variable_sulfate_hydrates.py
    python scripts/fix_variable_sulfate_hydrates.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.sssom_grading import (  # noqa: E402
    CONFIDENCE,
    JUSTIFICATION,
    PREDICATE,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

STAMP = "2026-09-11T00:00:00+00:00"
MAPPING_DATE = STAMP[:10]
CURATOR = "fix_variable_sulfate_hydrates"
ISSUE_SOURCE = "MIM:MIM curation (#321)"

VARIABLE_HYDRATES = {
    "Cr2(SO4)3 x n H2O": {
        "subject_id": "MIM:Cr2_So43_X_N_H2o",
        "old_identifier": "CHEBI:53471",
        "new_identifier": "kgmicrobe.compound:cr2_so43_x_n_h2o",
        "parent_label": "chromium(III) sulfate",
        "old_cas": "10101-53-8",
        "old_formula": "2Cr.3O4S",
    },
    "Fe2(SO4)3 x n H2O": {
        "subject_id": "MIM:Fe2_So43_X_N_H2o",
        "old_identifier": "CHEBI:53438",
        "new_identifier": "kgmicrobe.compound:fe2_so43_x_n_h2o",
        "parent_label": "iron(3+) sulfate",
        "old_cas": "10028-22-5",
        "old_formula": "2Fe.3O4S",
    },
}


def find(records: list[dict], label: str) -> dict:
    hits = [
        record
        for record in records
        if record.get("preferred_term") == label and record.get("mapping_status") == "MAPPED"
    ]
    if len(hits) != 1:
        raise SystemExit(f"expected one active mapped record named {label!r}; found {len(hits)}")
    return hits[0]


def _set(cells: list[str], column: dict[str, int], field: str, value: str) -> None:
    cells[column[field]] = value


def _sync_grade(cells: list[str], column: dict[str, int], quality: str) -> None:
    _set(cells, column, "predicate_id", PREDICATE[quality])
    _set(cells, column, "mapping_justification", JUSTIFICATION[quality])
    _set(cells, column, "confidence", CONFIDENCE[quality])


def append_mapping_source(source: str) -> str:
    tokens = [token for token in source.split("|") if token]
    if ISSUE_SOURCE not in tokens:
        tokens.append(ISSUE_SOURCE)
    return "|".join(tokens)


def _sssom_other(record: dict, *, object_label: str) -> str:
    drop = {
        str(record.get("preferred_term") or "").strip().casefold(),
        object_label.strip().casefold(),
        "",
    }
    out: list[str] = []
    seen: set[str] = set()
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict) or not is_resolving_synonym(synonym):
            continue
        token = str(synonym.get("synonym_text") or "").strip()
        key = token.casefold()
        if key in drop or key in seen:
            continue
        seen.add(key)
        out.append(token)
    return "|".join(out)


def prune_anhydrous_exact_synonyms(record: dict) -> int:
    kept = []
    removed = 0
    for synonym in record.get("synonyms") or []:
        if synonym.get("synonym_type") == "EXACT_SYNONYM" and synonym.get("source") == "kg_microbe":
            removed += 1
            continue
        kept.append(synonym)

    if kept:
        record["synonyms"] = kept
    else:
        record.pop("synonyms", None)
    return removed


def rewrite_records(records: list[dict]) -> tuple[dict[str, dict], dict[str, int]]:
    rewritten: dict[str, dict] = {}
    expected_membership_counts: dict[str, int] = {}

    for label, spec in VARIABLE_HYDRATES.items():
        record = find(records, label)
        old_identifier = spec["old_identifier"]
        new_identifier = spec["new_identifier"]
        if record.get("identifier") != old_identifier:
            raise SystemExit(f"{label} is on {record.get('identifier')}, not {old_identifier}")

        properties = record.get("chemical_properties") or {}
        if properties.get("cas_rn") != spec["old_cas"]:
            raise SystemExit(f"{label} CAS is {properties.get('cas_rn')}, not {spec['old_cas']}")
        if properties.get("molecular_formula") != spec["old_formula"]:
            raise SystemExit(
                f"{label} formula is {properties.get('molecular_formula')}, "
                f"not {spec['old_formula']}"
            )

        ontology_mapping = record.setdefault("ontology_mapping", {})
        if ontology_mapping.get("ontology_id") != old_identifier:
            raise SystemExit(
                f"{label} parent is {ontology_mapping.get('ontology_id')}, " f"not {old_identifier}"
            )
        old_quality = ontology_mapping.get("mapping_quality")

        removed_synonyms = prune_anhydrous_exact_synonyms(record)
        record["identifier"] = new_identifier
        if record.get("kg_microbe_node_id") == old_identifier:
            record.pop("kg_microbe_node_id")
        record["chemical_properties"] = {}

        ontology_mapping.update(
            {
                "ontology_id": old_identifier,
                "ontology_label": spec["parent_label"],
                "ontology_source": "CHEBI",
                "mapping_quality": "NARROW_MATCH",
            }
        )
        ontology_mapping.setdefault("evidence", []).append(
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": "MIM curation (#321)",
                "notes": (
                    f"Minted {new_identifier} for a variable hydrate identity with no "
                    f"exact ChEBI term or own CAS. {old_identifier} denotes anhydrous "
                    f"{spec['parent_label']} and remains only as the nearest parent "
                    "under MAPPING_SEMANTICS.md Section 3."
                ),
            }
        )
        record.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "MINTED_VARIABLE_HYDRATE_IDENTITY",
                "changes": (
                    f"identifier {old_identifier} -> {new_identifier}; "
                    f"mapping_quality {old_quality} -> NARROW_MATCH; cleared "
                    f"anhydrous chemical_properties ({spec['old_cas']}, "
                    f"{spec['old_formula']}); removed {removed_synonyms} anhydrous "
                    "kg_microbe exact synonym(s) (#321)."
                ),
                "llm_assisted": False,
            }
        )

        expected_membership_counts[old_identifier] = int(
            (record.get("occurrence_statistics") or {}).get("media_count") or 0
        )
        rewritten[label] = record

    return rewritten, expected_membership_counts


def rewrite_sssom(rewritten: dict[str, dict]) -> tuple[str, dict[str, int]]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    header = next(i for i, line in enumerate(lines) if line.startswith("subject_id\t"))
    fields = lines[header].rstrip("\n").split("\t")
    column = {field: index for index, field in enumerate(fields)}
    replacements = dict.fromkeys(VARIABLE_HYDRATES, 0)
    out: list[str] = []

    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if (
            len(cells) != len(fields)
            or line.startswith("#")
            or cells[column["subject_id"]] == "subject_id"
        ):
            out.append(line)
            continue

        label = cells[column["subject_label"]]
        spec = VARIABLE_HYDRATES.get(label)
        if not spec:
            out.append(line)
            continue

        if cells[column["subject_id"]] != spec["subject_id"]:
            raise SystemExit(
                f"{label} has subject {cells[column['subject_id']]}, " f"not {spec['subject_id']}"
            )
        if cells[column["object_id"]] != spec["old_identifier"]:
            raise SystemExit(
                f"{label} SSSOM object is {cells[column['object_id']]}, "
                f"not {spec['old_identifier']}"
            )
        if cells[column["predicate_id"]] != "skos:exactMatch":
            raise SystemExit(
                f"{label} SSSOM predicate is {cells[column['predicate_id']]}, "
                "not skos:exactMatch"
            )

        record = rewritten[label]
        parent = list(cells)
        _sync_grade(parent, column, "NARROW_MATCH")
        _set(parent, column, "object_label", spec["parent_label"])
        _set(parent, column, "object_source", object_source_for(spec["old_identifier"]))
        _set(parent, column, "source", append_mapping_source(parent[column["source"]]))
        _set(parent, column, "mapping_date", MAPPING_DATE)
        _set(parent, column, "confidence", CONFIDENCE["NARROW_MATCH"])
        _set(parent, column, "comment", "")
        _set(parent, column, "other", _sssom_other(record, object_label=spec["parent_label"]))
        _set(parent, column, "validation_method", "")

        registry = list(parent)
        _sync_grade(registry, column, "EXACT_MATCH")
        _set(registry, column, "mapping_justification", "semapv:ManualMappingCuration")
        _set(registry, column, "object_id", spec["new_identifier"])
        _set(registry, column, "object_label", label)
        _set(registry, column, "object_source", object_source_for(spec["new_identifier"]))
        _set(
            registry,
            column,
            "comment",
            (
                f"Registry/identity row preserving {spec['new_identifier']} "
                f"alongside parent {spec['old_identifier']}."
            ),
        )

        out.append("\t".join(parent) + "\n")
        out.append("\t".join(registry) + "\n")
        replacements[label] += 1

    missed = [label for label, count in replacements.items() if count != 1]
    if missed:
        raise SystemExit(
            "expected one exact SSSOM row for each variable hydrate; got "
            + ", ".join(f"{label}={replacements[label]}" for label in missed)
        )

    return "".join(out), replacements


def rewrite_membership(
    old_to_new: dict[str, str],
    expected_counts: dict[str, int],
) -> tuple[str, dict[str, int]]:
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments: list[str] = []
    table: list[list[str]] = []
    moved = dict.fromkeys(old_to_new, 0)

    for line in lines:
        if line.startswith("#"):
            comments.append(line if line.endswith("\n") else f"{line}\n")
            continue
        cells = line.rstrip("\n").split("\t")
        if cells[0] in old_to_new:
            old = cells[0]
            cells[0] = old_to_new[old]
            moved[old] += 1
        table.append(cells)

    header, rows = table[0], table[1:]
    rows.sort(key=lambda row: tuple(row[:2]))
    keys = [(row[0], row[1]) for row in rows]
    if len(keys) != len(set(keys)):
        raise SystemExit("membership rewrite would create duplicate edge keys")

    mismatched = [
        f"{old}: expected {expected_counts[old]}, moved {moved[old]}"
        for old in sorted(expected_counts)
        if moved[old] != expected_counts[old]
    ]
    if mismatched:
        raise SystemExit("membership count mismatch: " + "; ".join(mismatched))

    out = [*comments, "\t".join(header) + "\n"]
    out.extend("\t".join(row) + "\n" for row in rows)
    return "".join(out), moved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    doc = yaml.safe_load(COLLECTION.read_text(encoding="utf-8")) or {}
    records = doc.get("ingredients") or []
    active = {
        str(record.get("identifier") or "")
        for record in records
        if record.get("mapping_status") != "REJECTED"
    }
    for spec in VARIABLE_HYDRATES.values():
        if spec["new_identifier"] in active:
            raise SystemExit(f"{spec['new_identifier']} is already held by an active record")

    rewritten, expected_counts = rewrite_records(records)
    sssom_text, sssom_replacements = rewrite_sssom(rewritten)
    membership_text, moved_memberships = rewrite_membership(
        {spec["old_identifier"]: spec["new_identifier"] for spec in VARIABLE_HYDRATES.values()},
        expected_counts,
    )
    doc["generation_date"] = STAMP

    for label, spec in VARIABLE_HYDRATES.items():
        old_identifier = spec["old_identifier"]
        print(
            f"{label}: {old_identifier} -> {spec['new_identifier']} "
            f"(narrowMatch {old_identifier} {spec['parent_label']!r})"
        )
        print(f"  SSSOM rows replaced: {sssom_replacements[label]}")
        print(f"  membership rows moved: {moved_memberships[old_identifier]}")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(doc, COLLECTION, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    print("\nwrote curated collection, SSSOM, and membership")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
