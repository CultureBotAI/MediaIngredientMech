#!/usr/bin/env python3
"""Re-ground the unblocked exact-hydrate residuals from #321.

The repaired hydrate-grounding report (#461) left a small cohort whose preferred
terms name a hydrate while their published rows still point at an anhydrous
parent. The #321 ChEBI triage identified six that looked immediately fixable
because ChEBI now has a term whose label is exactly the parent label plus
"hydrate".

Two are no longer work for this script:

* `MgCl2x 6 H2O` has already merged into `MgCl2 x 6 H2O`.
* `Citric Acid*H2O` has a specific target, but its current `CHEBI:30769`
  identifier is shared with live anhydrous `Citric acid`, so the occurrence and
  membership rows cannot be moved without splitting duplicate evidence first.
* `Fe2(SO4)3 x n H2O` needs a variable-hydrate identity: ChEBI's
  "iron(3+) sulfate hydrate" term is the monohydrate by formula and exact
  synonym, while this label denotes variable hydration.

That leaves two promotions to exact ChEBI hydrate terms, plus one local
solution whose own identity stays `kgmicrobe.ingredient:` but whose parent
`closeMatch` moves from the anhydrous hydrochloride to the monohydrate.

    python scripts/fix_remaining_hydrate_regroundings.py
    python scripts/fix_remaining_hydrate_regroundings.py --apply
"""

from __future__ import annotations

import argparse
import re
import sqlite3
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
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"

STAMP = "2026-09-10T00:00:00+00:00"
CURATOR = "fix_remaining_hydrate_regroundings"
ISSUE = "#321"

PROMOTE = {
    "Esculin Monohydrate": {
        "old_identifier": "CHEBI:4853",
        "old_parent": "CHEBI:4853",
        "new_identifier": "CHEBI:73111",
        "new_label": "esculin hydrate",
    },
    "Betaine x H2O": {
        "old_identifier": "kgmicrobe.compound:betaine_x_h2o",
        "old_parent": "CHEBI:17750",
        "new_identifier": "CHEBI:91242",
        "new_label": "glycine betaine hydrate",
    },
}

LOCAL_PARENT = {
    "L-Cysteine x HCl x H2O solution": {
        "identifier": "kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution",
        "old_parent": "CHEBI:91247",
        "new_parent": "CHEBI:91248",
        "new_label": "L-cysteine hydrochloride hydrate",
    },
}

COMPONENT_RESCOPES = {
    "Esculin Ferric Citrate": {
        "component_name": "esculin",
        "component_id": "CHEBI:4853",
        "old_scope": "MIM_CATALOG",
        "new_scope": "EXTERNAL_TERM",
    },
}

MEMBERSHIP_REWRITES = {
    "kgmicrobe.compound:betaine_x_h2o": ("CHEBI:91242", "Betaine x H2O"),
}

FORMULA = "chemrof:generalized_empirical_formula"
INCHI = "chemrof:inchi_string"
SMILES = "chemrof:smiles_string"
CAS = re.compile(r"^cas:(\d{2,7}-\d{2}-\d)$")
HYDRATE_SYNONYM_SOURCE = "chebi_synonym_review"
MAX_OTHER_ENTRIES = 50


def find(records: list[dict], *, label: str) -> dict:
    hits = [
        rec for rec in records
        if rec.get("preferred_term") == label and rec.get("mapping_status") == "MAPPED"
    ]
    if len(hits) != 1:
        raise SystemExit(f"expected one active record named {label!r}; found {len(hits)}")
    return hits[0]


def chebi_props(conn: sqlite3.Connection, curie: str) -> dict[str, str]:
    rows = conn.execute(
        "SELECT predicate, value FROM statements WHERE subject=?",
        (curie,),
    ).fetchall()
    by_pred: dict[str, str] = {}
    cas_values: list[str] = []
    for predicate, value in rows:
        if predicate in {FORMULA, INCHI, SMILES}:
            by_pred[predicate] = value
        if predicate == "oio:hasDbXref":
            match = CAS.match(value)
            if match:
                cas_values.append(match.group(1))

    for predicate in (FORMULA, INCHI, SMILES):
        if predicate not in by_pred:
            raise SystemExit(f"{curie} has no {predicate} in {CHEBI_DB}")

    out = {
        "molecular_formula": by_pred[FORMULA],
        "inchi": by_pred[INCHI],
        "smiles": by_pred[SMILES],
    }
    if len(cas_values) > 1:
        raise SystemExit(f"{curie} has multiple CAS xrefs: {cas_values}")
    if cas_values:
        out["cas_rn"] = cas_values[0]
    return out


def chebi_exact_synonyms(conn: sqlite3.Connection, curie: str) -> list[str]:
    return sorted({
        str(row[0])
        for row in conn.execute(
            "SELECT value FROM statements "
            "WHERE subject=? AND predicate='oio:hasExactSynonym' "
            "AND value IS NOT NULL",
            (curie,),
        )
    })


def exact_hydrate_chemical_properties(
    current: dict,
    props: dict[str, str],
    curie: str,
) -> dict:
    updated = {
        **current,
        **props,
        "data_source": f"OAK/CHEBI exact hydrate term {curie}",
        "retrieval_date": STAMP,
    }
    if not props.get("cas_rn"):
        updated.pop("cas_rn", None)
    return updated


def hydrate_exact_synonyms(conn: sqlite3.Connection, new_id: str) -> list[dict]:
    return [
        {
            "synonym_text": text,
            "synonym_type": "EXACT_SYNONYM",
            "source": HYDRATE_SYNONYM_SOURCE,
        }
        for text in chebi_exact_synonyms(conn, new_id)
    ]


def replace_exact_synonyms(record: dict, replacements: list[dict]) -> int:
    replacements_by_text = {
        str(synonym["synonym_text"]).casefold(): synonym
        for synonym in replacements
    }
    replacement_texts = set(replacements_by_text)
    kept = []
    removed = 0
    for synonym in record.get("synonyms") or []:
        synonym_type = synonym.get("synonym_type")
        source = synonym.get("source")
        text = str(synonym.get("synonym_text") or "")
        if (
            synonym_type == "EXACT_SYNONYM"
            and source in {
                "kg_microbe",
                "merged_from_duplicate_mim_record",
                HYDRATE_SYNONYM_SOURCE,
            }
            and text.casefold() not in replacement_texts
        ):
            removed += 1
            continue
        kept.append(synonym)

    existing = {
        str(synonym.get("synonym_text") or "").casefold()
        for synonym in kept
    }
    for folded, synonym in replacements_by_text.items():
        if folded not in existing:
            kept.append(synonym)
            existing.add(folded)

    record["synonyms"] = kept
    return removed


def append_mapping_source(source: str, token: str = f"MIM:MIM curation ({ISSUE})") -> str:
    tokens = [part for part in source.split("|") if part]
    if token not in tokens:
        tokens.append(token)
    return "|".join(tokens)


def _set(fields: list[str], column: dict[str, int], name: str, value: str) -> None:
    fields[column[name]] = value


def _sync_grade(fields: list[str], column: dict[str, int], quality: str) -> None:
    _set(fields, column, "predicate_id", PREDICATE[quality])
    _set(fields, column, "mapping_justification", JUSTIFICATION[quality])
    _set(fields, column, "confidence", CONFIDENCE[quality])


def _sssom_other(record: dict, *, object_label: str, cas: str = "") -> str:
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
        if len(out) >= MAX_OTHER_ENTRIES:
            break

    cas_token = f"CAS:{cas}" if cas else ""
    cas_key = cas_token.casefold()
    if cas_token and cas_key not in drop and cas_key not in seen:
        out.append(cas_token)
    return "|".join(out)


def sssom_other_by_label(records: list[dict], cas_by_label: dict[str, str]) -> dict[str, str]:
    labels = set(PROMOTE) | set(LOCAL_PARENT)
    return {
        str(record["preferred_term"]): _sssom_other(
            record,
            object_label=str((record.get("ontology_mapping") or {}).get("ontology_label") or ""),
            cas=cas_by_label.get(str(record["preferred_term"]), ""),
        )
        for record in records
        if record.get("preferred_term") in labels
    }


def rewrite_sssom(other_by_label: dict[str, str]) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    header = next(i for i, line in enumerate(lines) if line.startswith("subject_id"))
    columns = lines[header].rstrip("\n").split("\t")
    column = {name: index for index, name in enumerate(columns)}
    updated = 0
    dropped = 0
    seen_promotions: set[str] = set()
    seen_local_parents: set[str] = set()
    seen_local_registry: set[str] = set()
    out: list[str] = []

    for line in lines:
        cells = line.rstrip("\n").split("\t")
        eol = "\n" if line.endswith("\n") else ""
        if len(cells) < len(columns) or cells[0].startswith("#") or cells[0] == "subject_id":
            out.append(line)
            continue

        label = cells[column["subject_label"]]
        object_id = cells[column["object_id"]]
        if label in PROMOTE:
            spec = PROMOTE[label]
            if object_id == spec["old_identifier"] and object_id != spec["old_parent"]:
                dropped += 1
                continue
            if object_id == spec["old_parent"]:
                _set(cells, column, "object_id", spec["new_identifier"])
                _set(cells, column, "object_label", spec["new_label"])
                _set(cells, column, "object_source", object_source_for(spec["new_identifier"]))
                _sync_grade(cells, column, "EXACT_MATCH")
                _set(
                    cells,
                    column,
                    "source",
                    append_mapping_source(cells[column["source"]]),
                )
                _set(cells, column, "comment", "")
                _set(cells, column, "mapping_date", STAMP[:10])
                _set(cells, column, "other", other_by_label[label])
                _set(cells, column, "validation_method", "")
                updated += 1
                seen_promotions.add(label)
        elif label in LOCAL_PARENT:
            spec = LOCAL_PARENT[label]
            if object_id == spec["old_parent"]:
                _set(cells, column, "object_id", spec["new_parent"])
                _set(cells, column, "object_label", spec["new_label"])
                _set(cells, column, "object_source", object_source_for(spec["new_parent"]))
                _sync_grade(cells, column, "CLOSE_MATCH")
                _set(
                    cells,
                    column,
                    "source",
                    append_mapping_source(cells[column["source"]]),
                )
                _set(cells, column, "mapping_date", STAMP[:10])
                _set(cells, column, "other", other_by_label[label])
                _set(cells, column, "validation_method", "")
                updated += 1
                seen_local_parents.add(label)
            elif object_id == spec["identifier"]:
                cells[column["comment"]] = (
                    f"Registry/identity row preserving {spec['identifier']} "
                    f"alongside parent {spec['new_parent']}."
                )
                _set(cells, column, "mapping_date", STAMP[:10])
                updated += 1
                seen_local_registry.add(label)
        out.append("\t".join(cells) + eol)

    missed = sorted(set(PROMOTE) - seen_promotions)
    if missed:
        raise SystemExit(f"failed to update promoted SSSOM row(s): {missed}")
    missed = sorted(set(LOCAL_PARENT) - seen_local_parents)
    if missed:
        raise SystemExit(f"failed to update local parent SSSOM row(s): {missed}")
    missed = sorted(set(LOCAL_PARENT) - seen_local_registry)
    if missed:
        raise SystemExit(f"failed to update local registry SSSOM row(s): {missed}")
    if dropped != 1:
        raise SystemExit(f"expected to drop one withdrawn registry row, dropped {dropped}")
    if out and not out[-1].endswith("\n"):
        out[-1] += "\n"
    return "".join(out), updated, dropped


def rewrite_membership(replacements: dict[str, str]) -> tuple[str, dict[str, int]]:
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments: list[str] = []
    table: list[list[str]] = []
    moved = dict.fromkeys(replacements, 0)

    for line in lines:
        if line.startswith("#"):
            comments.append(line if line.endswith("\n") else f"{line}\n")
            continue
        fields = line.rstrip("\n").split("\t")
        if fields[0] in replacements:
            old = fields[0]
            fields[0] = replacements[old]
            moved[old] += 1
        table.append(fields)

    header, rows = table[0], table[1:]
    rows.sort(key=lambda row: tuple(row[:2]))
    keys = [(row[0], row[1]) for row in rows]
    if len(keys) != len(set(keys)):
        raise SystemExit("membership rewrite would create duplicate edge keys")

    out = [*comments, "\t".join(header) + "\n"]
    out.extend("\t".join(row) + "\n" for row in rows)
    return "".join(out), moved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--chebi-db", type=Path, default=CHEBI_DB)
    args = ap.parse_args(argv)

    if not args.chebi_db.exists():
        raise SystemExit(f"ChEBI SQLite not found at {args.chebi_db}")

    conn = sqlite3.connect(f"file:{args.chebi_db}?mode=ro", uri=True)
    doc = yaml.safe_load(COLLECTION.read_text(encoding="utf-8")) or {}
    records = doc.get("ingredients") or []
    active = {
        str(rec.get("identifier") or "")
        for rec in records
        if rec.get("mapping_status") != "REJECTED"
    }
    actions: list[str] = []
    cas_by_label: dict[str, str] = {}

    for label, spec in PROMOTE.items():
        rec = find(records, label=label)
        old_identifier = spec["old_identifier"]
        if rec.get("identifier") != old_identifier:
            raise SystemExit(f"{label} is on {rec.get('identifier')}, not {old_identifier}")
        if spec["new_identifier"] in active:
            raise SystemExit(f"{spec['new_identifier']} is already held by an active record")

        props = chebi_props(conn, spec["new_identifier"])
        cas = props.get("cas_rn") or ""
        cas_by_label[label] = cas

        rec["identifier"] = spec["new_identifier"]
        if rec.get("kg_microbe_node_id") in {old_identifier, spec["old_parent"]}:
            rec["kg_microbe_node_id"] = spec["new_identifier"]
        om = rec.setdefault("ontology_mapping", {})
        old_parent = om.get("ontology_id")
        old_label = om.get("ontology_label")
        om.update({
            "ontology_id": spec["new_identifier"],
            "ontology_label": spec["new_label"],
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
        })
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"Promoted from {old_parent} ({old_label!r}) to the exact ChEBI "
                f"hydrate term {spec['new_identifier']} ({spec['new_label']!r}). "
                "The label names a hydrate and ChEBI has a term for that hydrate, "
                "so MAPPING_SEMANTICS.md Section 3 step 1 applies."
            ),
        })
        rec["chemical_properties"] = exact_hydrate_chemical_properties(
            rec.get("chemical_properties") or {},
            props,
            spec["new_identifier"],
        )
        synonym_replacements = hydrate_exact_synonyms(
            conn, spec["new_identifier"]
        )
        removed_synonyms = replace_exact_synonyms(rec, synonym_replacements)
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "PROMOTED_TO_SPECIFIC_HYDRATE",
            "changes": (
                f"identifier {old_identifier} -> {spec['new_identifier']}; "
                f"ontology_id {old_parent} -> {spec['new_identifier']}; "
                f"mapping_quality -> EXACT_MATCH. Structure fields were copied "
                f"from the exact ChEBI hydrate term, {removed_synonyms} stale "
                "anhydrous exact synonym(s) were replaced, and stale "
                f"kg_microbe_node_id values were aligned where present ({ISSUE})."
            ),
            "llm_assisted": False,
        })
        actions.append(f"PROMOTE {label}: {old_identifier} -> {spec['new_identifier']}")

    for label, spec in LOCAL_PARENT.items():
        rec = find(records, label=label)
        if rec.get("identifier") != spec["identifier"]:
            raise SystemExit(f"{label} is on {rec.get('identifier')}, not {spec['identifier']}")
        om = rec.setdefault("ontology_mapping", {})
        if om.get("ontology_id") != spec["old_parent"]:
            raise SystemExit(f"{label} parent is {om.get('ontology_id')}, not {spec['old_parent']}")
        om.update({
            "ontology_id": spec["new_parent"],
            "ontology_label": spec["new_label"],
            "ontology_source": "CHEBI",
            "mapping_quality": "CLOSE_MATCH",
        })
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"Repointed the local solution identity's parent from "
                f"{spec['old_parent']} to the hydrate-specific {spec['new_parent']} "
                f"({spec['new_label']!r}). The record still denotes a prepared "
                "solution, not the pure ChEBI compound, so it keeps its "
                "kgmicrobe.ingredient identifier and closeMatch grade."
            ),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "CORRECTED_PARENT",
            "changes": (
                f"ontology_id {spec['old_parent']} -> {spec['new_parent']} while "
                f"retaining local identifier {spec['identifier']} ({ISSUE})."
            ),
            "llm_assisted": False,
        })
        actions.append(f"PARENT  {label}: {spec['old_parent']} -> {spec['new_parent']}")

    for label, spec in COMPONENT_RESCOPES.items():
        rec = find(records, label=label)
        components = [
            component for component in rec.get("components") or []
            if component.get("component_name") == spec["component_name"]
            and component.get("component_id") == spec["component_id"]
        ]
        if len(components) != 1:
            raise SystemExit(
                f"expected one {label} component on {spec['component_id']}; "
                f"found {len(components)}"
            )
        component = components[0]
        if component.get("reference_scope") != spec["old_scope"]:
            raise SystemExit(
                f"{label} {spec['component_name']} scope is "
                f"{component.get('reference_scope')}, not {spec['old_scope']}"
            )
        component["reference_scope"] = spec["new_scope"]
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "RESCOPED_COMPONENT",
            "changes": (
                f"{spec['component_name']} component reference_scope "
                f"{spec['old_scope']} -> {spec['new_scope']}. "
                f"{spec['component_id']} names anhydrous esculin; after "
                f"Esculin Monohydrate moved to CHEBI:73111, no active MIM "
                f"record represents that component ({ISSUE})."
            ),
            "llm_assisted": False,
        })
        actions.append(
            f"COMPONENT {label}: {spec['component_id']} {spec['old_scope']} "
            f"-> {spec['new_scope']}"
        )

    sssom_text, sssom_updated, sssom_dropped = rewrite_sssom(
        sssom_other_by_label(records, cas_by_label)
    )
    membership_replacements = {
        old: new for old, (new, _label) in MEMBERSHIP_REWRITES.items()
    }
    membership_text, moved_edges = rewrite_membership(membership_replacements)
    for old, (_new, label) in MEMBERSHIP_REWRITES.items():
        stats = find(records, label=label).get("occurrence_statistics") or {}
        if moved_edges[old] != stats.get("media_count"):
            raise SystemExit(
                f"moved {moved_edges[old]} {label} membership edge(s), but "
                f"media_count is {stats.get('media_count')}"
            )

    print(f"{len(actions)} curation action(s)")
    for action in actions:
        print(f"  {action}")
    print(f"SSSOM: {sssom_updated} updated, {sssom_dropped} withdrawn registry row")
    moved_summary = ", ".join(
        f"{count} {old}->{membership_replacements[old]}"
        for old, count in sorted(moved_edges.items())
    )
    print(f"membership: {moved_summary}")

    if not args.apply:
        print("\nDRY RUN -- pass --apply to write")
        return 0

    save_yaml(doc, COLLECTION, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
