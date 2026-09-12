#!/usr/bin/env python3
"""Clear exact anhydrous identities from reviewed hydrate records (#652).

Four sulfate records name specific, chemically plausible hydrate states for
which no exact external ontology term is verified. They must keep local
``kgmicrobe.compound`` identifiers and publish their anhydrous CHEBI parents
only as ``skos:narrowMatch``.

The Citric Acid•H2O row is the opposite case: CHEBI has a supported monohydrate
term and MIM already has a live ``CHEBI:31404`` record for it, so the duplicate
record becomes a tombstone that resolves to the existing monohydrate.

Dry-run by default; pass ``--apply`` to write the collection, SSSOM,
CultureMech membership, hydrate review, and duplicate-identifier baseline.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.sssom_grading import (  # noqa: E402
    CONFIDENCE,
    JUSTIFICATION,
    JUSTIFICATION_MANUAL,
    PREDICATE,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
HYDRATE_REVIEW = ROOT / "mappings" / "hydrate_review.tsv"
DUPLICATE_BASELINE = ROOT / "mappings" / "duplicate_identifier_baseline.tsv"
DEFAULT_OCCURRENCES = ROOT.parent / "CultureMech" / "output" / "ingredient_occurrences.tsv"

STAMP = "2026-09-12T00:00:00+00:00"
MAPPING_DATE = STAMP[:10]
CURATOR = "fix_hydrate_local_identities"
ISSUE = "#652"
ISSUE_SOURCE = "MIM:MIM curation (#652)"
MAX_OTHER_ENTRIES = 50


def source_label_key(value: str) -> str:
    """Match CultureMech occurrence source labels without broad lexical guesses."""
    value = re.sub(r"\s*-\s*", "-", value.strip().casefold())
    value = re.sub(r"-+", "-", value)
    return re.sub(r"\s+", " ", value)


@dataclass(frozen=True)
class SulfateHydrate:
    label: str
    subject_id: str
    old_identifier: str
    new_identifier: str
    parent_id: str
    parent_label: str
    formula: str
    source_labels: tuple[str, ...]
    false_synonyms: frozenset[str] = frozenset()


SULFATE_HYDRATES: tuple[SulfateHydrate, ...] = (
    SulfateHydrate(
        label="FeSO4 x 5 H2O",
        subject_id="MIM:Feso4_X_5_H2o",
        old_identifier="CHEBI:75832",
        new_identifier="kgmicrobe.compound:feso4_x_5_h2o",
        parent_id="CHEBI:75832",
        parent_label="iron(2+) sulfate (anhydrous)",
        formula="Fe.O4S.5H2O",
        source_labels=("FeSO4 x 5 H2O",),
        false_synonyms=frozenset({"FeSO .7H O"}),
    ),
    SulfateHydrate(
        label="FeSO4 x 6 H2O",
        subject_id="MIM:Feso4_X_6_H2o",
        old_identifier="CHEBI:75832",
        new_identifier="kgmicrobe.compound:feso4_x_6_h2o",
        parent_id="CHEBI:75832",
        parent_label="iron(2+) sulfate (anhydrous)",
        formula="Fe.O4S.6H2O",
        source_labels=(
            "FeSO4 x 6 H2O",
            "FeSO4 x 6H2O",
            "FeSO4·6H2O",
            "FeSO4・6H2O",
        ),
        false_synonyms=frozenset({"FeSO .7H O"}),
    ),
    SulfateHydrate(
        label="MgSO4 x 6 H2O",
        subject_id="MIM:Mgso4_X_6_H2o",
        old_identifier="CHEBI:32599",
        new_identifier="kgmicrobe.compound:mgso4_x_6_h2o",
        parent_id="CHEBI:32599",
        parent_label="magnesium sulfate",
        formula="Mg.O4S.6H2O",
        source_labels=("MgSO4 x 6 H2O", "MgSO4 x 6H2O", "MgSO4·6H2O"),
        false_synonyms=frozenset({"Mg2SO4", "MgSO .7H O"}),
    ),
    SulfateHydrate(
        label="MnSO4 x 7 H2O",
        subject_id="MIM:Mnso4_X_7_H2o",
        old_identifier="CHEBI:86360",
        new_identifier="kgmicrobe.compound:mnso4_x_7_h2o",
        parent_id="CHEBI:86360",
        parent_label="manganese(II) sulfate",
        formula="Mn.O4S.7H2O",
        source_labels=(
            "MnSO4 . 7H2O",
            "MnSO4 x 7 H2O",
            "MnSO4 x 7H2O",
            "MnSO4.7H2O",
            "MnSO4·7H2O",
        ),
    ),
)

SPECS_BY_SUBJECT = {spec.subject_id: spec for spec in SULFATE_HYDRATES}
SPECS_BY_LABEL = {spec.label: spec for spec in SULFATE_HYDRATES}
SOURCE_LABEL_TO_TARGET = {
    source_label_key(source_label): spec.new_identifier
    for spec in SULFATE_HYDRATES
    for source_label in spec.source_labels
}
SOURCE_LABEL_TO_TARGET.update(
    {
        source_label_key("Citric Acid•H2O"): "CHEBI:31404",
        source_label_key("Citric Acid•H2O(Fisher A 104)"): "CHEBI:31404",
    }
)


def append_mapping_source(source: str) -> str:
    tokens = [token for token in source.split("|") if token]
    if ISSUE_SOURCE not in tokens:
        tokens.append(ISSUE_SOURCE)
    return "|".join(tokens)


def find_active(records: list[dict], label: str) -> dict:
    hits = [
        record
        for record in records
        if record.get("preferred_term") == label and record.get("mapping_status") == "MAPPED"
    ]
    if len(hits) != 1:
        raise SystemExit(f"expected one active record named {label!r}; found {len(hits)}")
    return hits[0]


def find_one(records: list[dict], label: str) -> dict:
    hits = [record for record in records if record.get("preferred_term") == label]
    if len(hits) != 1:
        raise SystemExit(f"expected one record named {label!r}; found {len(hits)}")
    return hits[0]


def reject_synonym(synonym: dict) -> bool:
    if synonym.get("synonym_type") == "REJECTED_LABEL":
        return False
    synonym["synonym_type"] = "REJECTED_LABEL"
    return True


def reject_false_synonyms(record: dict, spec: SulfateHydrate) -> list[str]:
    rejected: list[str] = []
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict):
            continue
        text = str(synonym.get("synonym_text") or "")
        if (
            synonym.get("synonym_type") == "EXACT_SYNONYM" or text in spec.false_synonyms
        ) and reject_synonym(synonym):
            rejected.append(text)
    return rejected


def ensure_synonym(record: dict, text: str, source: str) -> bool:
    key = text.strip().casefold()
    synonyms = record.setdefault("synonyms", [])
    for synonym in synonyms:
        if not isinstance(synonym, dict):
            continue
        if str(synonym.get("synonym_text") or "").strip().casefold() != key:
            continue
        if synonym.get("synonym_type") == "REJECTED_LABEL":
            synonym["synonym_type"] = "RAW_TEXT"
            synonym["source"] = source
            return True
        return False
    synonyms.append(
        {
            "synonym_text": text,
            "synonym_type": "RAW_TEXT",
            "source": source,
        }
    )
    return True


def ensure_hydrate_form(record: dict, text: str) -> bool:
    if source_label_key(text) == source_label_key(record.get("preferred_term") or ""):
        return False

    synonyms = record.setdefault("synonyms", [])
    for synonym in synonyms:
        if not isinstance(synonym, dict):
            continue
        if source_label_key(synonym.get("synonym_text") or "") != source_label_key(text):
            continue
        if synonym.get("synonym_type") == "HYDRATE_FORM":
            return False
        synonym["synonym_type"] = "HYDRATE_FORM"
        synonym["source"] = "MIM curation (#652)"
        return True

    synonyms.append(
        {
            "synonym_text": text,
            "synonym_type": "HYDRATE_FORM",
            "source": "MIM curation (#652)",
        }
    )
    return True


def rewrite_sulfate_records(records: list[dict]) -> dict[str, dict]:
    active = [record for record in records if record.get("mapping_status") != "REJECTED"]
    rewritten: dict[str, dict] = {}

    for spec in SULFATE_HYDRATES:
        record = find_active(records, spec.label)
        conflicts = [
            other.get("preferred_term")
            for other in active
            if other is not record and other.get("identifier") == spec.new_identifier
        ]
        if conflicts:
            raise SystemExit(
                f"{spec.new_identifier} is already held by active record(s): {conflicts}"
            )
        was_already_local = record.get("identifier") == spec.new_identifier
        if record.get("identifier") not in {spec.old_identifier, spec.new_identifier}:
            raise SystemExit(
                f"{spec.label} is on {record.get('identifier')}, not "
                f"{spec.old_identifier} or {spec.new_identifier}"
            )

        ontology_mapping = record.setdefault("ontology_mapping", {})
        if ontology_mapping.get("ontology_id") != spec.parent_id:
            raise SystemExit(
                f"{spec.label} parent is {ontology_mapping.get('ontology_id')}, "
                f"not {spec.parent_id}"
            )
        formula = (record.get("chemical_properties") or {}).get("molecular_formula")
        if formula != spec.formula:
            raise SystemExit(f"{spec.label} formula is {formula!r}, not {spec.formula!r}")

        old_quality = ontology_mapping.get("mapping_quality")
        old_chemistry = dict(record.get("chemical_properties") or {})
        rejected = reject_false_synonyms(record, spec)
        ensured = [
            source_label
            for source_label in spec.source_labels
            if ensure_hydrate_form(record, source_label)
        ]
        record["identifier"] = spec.new_identifier
        for event in record.get("curation_history") or []:
            if (
                event.get("timestamp") == STAMP
                and event.get("curator") == CURATOR
                and event.get("action") == "LOCALIZED_HYDRATE_IDENTITY"
            ):
                event["changes"] = str(event.get("changes") or "").replace(
                    " -> CLOSE_MATCH", " -> NARROW_MATCH"
                )
        if record.get("kg_microbe_node_id") in {
            spec.old_identifier,
            spec.new_identifier,
            spec.parent_id,
        }:
            record.pop("kg_microbe_node_id")
        record["chemical_properties"] = {
            "molecular_formula": spec.formula,
            "data_source": "MIM curation (#652)",
        }
        ontology_mapping.update(
            {
                "ontology_id": spec.parent_id,
                "ontology_label": spec.parent_label,
                "ontology_source": "CHEBI",
                "mapping_quality": "NARROW_MATCH",
            }
        )
        evidence = {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": "MIM curation (#652)",
            "notes": (
                f"{spec.label} names a formula-supported hydrate, but no exact "
                f"external ontology term is verified. {spec.parent_id} "
                f"({spec.parent_label}) is retained only as the asymmetric "
                "anhydrous parent while the supplied hydrate keeps a local "
                "kgmicrobe.compound identity."
            ),
        }
        evidence_list = ontology_mapping.setdefault("evidence", [])
        for old_evidence in evidence_list:
            if old_evidence.get("source") == "MIM curation (#652)":
                old_evidence.update(evidence)
                break
        else:
            evidence_list.append(evidence)

        if was_already_local:
            if ensured:
                record.setdefault("curation_history", []).append(
                    {
                        "timestamp": STAMP,
                        "curator": CURATOR,
                        "action": "ADDED_HYDRATE_FORM_SYNONYMS",
                        "changes": (
                            f"Added {', '.join(ensured)} as reviewed HYDRATE_FORM "
                            f"source label(s) for the local hydrate identity (#663)."
                        ),
                        "previous_status": "MAPPED",
                        "new_status": "MAPPED",
                        "llm_assisted": False,
                    }
                )
        else:
            record.setdefault("curation_history", []).append(
                {
                    "timestamp": STAMP,
                    "curator": CURATOR,
                    "action": "LOCALIZED_HYDRATE_IDENTITY",
                    "changes": (
                        f"identifier {spec.old_identifier} -> {spec.new_identifier}; "
                        f"mapping_quality {old_quality} -> NARROW_MATCH. Preserved "
                        f"the curated formula {spec.formula}, cleared parent-derived "
                        f"chemical_properties {old_chemistry!r}, and marked "
                        f"{len(rejected)} parent-derived synonym(s) as "
                        f"REJECTED_LABEL. Added {len(ensured)} reviewed source "
                        f"label(s) as HYDRATE_FORM synonyms ({ISSUE})."
                    ),
                    "previous_status": "MAPPED",
                    "new_status": "MAPPED",
                    "llm_assisted": False,
                }
            )
        rewritten[spec.label] = record

    return rewritten


def merge_citric_bullet_record(records: list[dict]) -> dict[str, dict]:
    source = find_one(records, "Citric Acid•H2O")
    destination = find_active(records, "Citric acid x H2O")
    source_was_active = source.get("mapping_status") != "REJECTED"
    expected_source_ids = {"CHEBI:30769"} if source_was_active else {"CHEBI:31404"}
    if source.get("identifier") not in expected_source_ids:
        raise SystemExit(
            "Citric Acid•H2O is on an unexpected identifier for its "
            f"{source.get('mapping_status')} state; found {source.get('identifier')}"
        )
    if destination.get("identifier") != "CHEBI:31404":
        raise SystemExit(
            "Citric acid x H2O no longer owns CHEBI:31404; "
            f"found {destination.get('identifier')}"
        )

    added = []
    for label in ("Citric Acid•H2O", "Citric Acid•H2O(Fisher A 104)"):
        if ensure_synonym(
            destination,
            label,
            "MERGED_FROM_CHEBI:30769 (#652)",
        ):
            added.append(label)

    rejected = []
    for synonym in source.get("synonyms") or []:
        if not isinstance(synonym, dict):
            continue
        if str(synonym.get("synonym_text") or "") in {
            "2-hydroxypropane-1,2,3-tricarboxylic acid",
            "(trisodium salt)",
        } and reject_synonym(synonym):
            rejected.append(str(synonym.get("synonym_text") or ""))

    source["identifier"] = "CHEBI:31404"
    source["mapping_status"] = "REJECTED"
    source["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}
    source.pop("chemical_properties", None)
    source["ontology_mapping"] = {
        "ontology_id": "CHEBI:31404",
        "ontology_label": "Citric acid monohydrate",
        "ontology_source": "CHEBI",
        "mapping_quality": "EXACT_MATCH",
        "evidence": [
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": "MIM curation (#652)",
                "notes": (
                    "Citric Acid•H2O is a duplicate source label for the existing "
                    "CHEBI:31404 Citric acid x H2O monohydrate record."
                ),
            }
        ],
    }
    if source_was_active:
        source.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "MERGED_INTO",
                "changes": (
                    "Merged duplicate Citric Acid•H2O into the existing CHEBI:31404 "
                    "Citric acid x H2O monohydrate record; tombstoned this record, "
                    f"zeroed occurrences, and rejected {len(rejected)} anhydrous or "
                    f"non-resolving synonym(s) instead of carrying them forward ({ISSUE})."
                ),
                "previous_status": "MAPPED",
                "new_status": "REJECTED",
                "llm_assisted": False,
            }
        )

    if source_was_active or added:
        destination.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "MERGED_FROM",
                "changes": (
                    "Absorbed duplicate CHEBI:30769 Citric Acid•H2O; "
                    f"added {len(added)} monohydrate source label(s) as RAW_TEXT "
                    "synonym(s) and left anhydrous or bare-parenthetical labels on "
                    f"the rejected tombstone ({ISSUE})."
                ),
                "previous_status": "MAPPED",
                "new_status": "MAPPED",
                "llm_assisted": False,
            }
        )
    return {"source": source, "destination": destination}


def owner_by_token() -> dict[str, str]:
    owners = {
        source_label_key(label): spec.label
        for spec in SULFATE_HYDRATES
        for label in spec.source_labels
    }
    owners[source_label_key("Citric Acid•H2O")] = "Citric acid x H2O"
    owners[source_label_key("Citric Acid•H2O(Fisher A 104)")] = "Citric acid x H2O"
    return owners


def sssom_other(record: dict, *, object_label: str) -> str:
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
    return "|".join(out)


def append_record_cas(other: str, record: dict) -> str:
    cas = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
    if not cas:
        return other

    token = f"CAS:{cas}"
    parts = [part for part in other.split("|") if part]
    if any(part.casefold() == token.casefold() for part in parts):
        return other
    return "|".join([*parts, token])


def sync_parent_row(
    row: dict[str, str],
    spec: SulfateHydrate,
    record: dict,
) -> dict[str, str]:
    out = dict(row)
    out["object_id"] = spec.parent_id
    out["object_label"] = spec.parent_label
    out["object_source"] = object_source_for(spec.parent_id)
    out["predicate_id"] = PREDICATE["NARROW_MATCH"]
    out["mapping_justification"] = JUSTIFICATION["NARROW_MATCH"]
    out["source"] = append_mapping_source(row.get("source", ""))
    out["mapping_date"] = MAPPING_DATE
    out["confidence"] = CONFIDENCE["CLOSE_MATCH"]
    out["comment"] = (
        f"Local kgmicrobe.compound identity retained because {spec.label} "
        "names a distinct hydrate with no verified external exact term; "
        f"{spec.parent_id} is the anhydrous parent."
    )
    out["other"] = sssom_other(record, object_label=spec.parent_label)
    out["validation_method"] = ""
    return out


def registry_row(
    row: dict[str, str],
    spec: SulfateHydrate,
    record: dict,
) -> dict[str, str]:
    out = dict(row)
    out["object_id"] = spec.new_identifier
    out["object_label"] = spec.label
    out["object_source"] = object_source_for(spec.new_identifier)
    out["predicate_id"] = PREDICATE["EXACT_MATCH"]
    out["mapping_justification"] = JUSTIFICATION_MANUAL
    out["source"] = append_mapping_source(row.get("source", ""))
    out["mapping_date"] = MAPPING_DATE
    out["confidence"] = CONFIDENCE["EXACT_MATCH"]
    out["comment"] = (
        f"Registry/identity row preserving {spec.new_identifier} alongside "
        f"anhydrous parent {spec.parent_id}."
    )
    out["other"] = sssom_other(record, object_label=spec.parent_label)
    out["validation_method"] = ""
    return out


def scrub_other(row: dict[str, str], owners: dict[str, str]) -> bool:
    old = row.get("other") or ""
    subject_label = row.get("subject_label") or ""
    kept = [
        token
        for token in old.split("|")
        if owners.get(source_label_key(token), subject_label) == subject_label
    ]
    row["other"] = "|".join(kept)
    return row["other"] != old


def rewrite_sssom(
    records: list[dict],
    rewritten: dict[str, dict],
    citric: dict[str, dict],
) -> tuple[str, int, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    header = body[0].rstrip("\n")
    rows = list(csv.DictReader(body, delimiter="\t"))
    has_registry = {
        row["subject_id"]
        for row in rows
        for spec in SULFATE_HYDRATES
        if row["subject_id"] == spec.subject_id and row["object_id"] == spec.new_identifier
    }

    owners = owner_by_token()
    parent_rows: dict[str, int] = defaultdict(int)
    registry_rows: dict[str, int] = defaultdict(int)
    touched = 0
    scrubbed = 0
    dropped_citric = 0
    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=header.split("\t"),
        delimiter="\t",
        lineterminator="\n",
    )
    out.write(f"{header}\n")

    for row in rows:
        if row["subject_id"] == "MIM:Citric_Acidh2o":
            dropped_citric += 1
            touched += 1
            continue
        if row["subject_id"] == "MIM:Citric_Acid_X_H2o":
            row["source"] = append_mapping_source(row.get("source", ""))
            row["mapping_date"] = MAPPING_DATE
            row["other"] = append_record_cas(
                sssom_other(
                    citric["destination"],
                    object_label="Citric acid monohydrate",
                ),
                citric["destination"],
            )
            writer.writerow(row)
            touched += 1
            continue

        spec = SPECS_BY_SUBJECT.get(row["subject_id"])
        if spec is None:
            if scrub_other(row, owners):
                scrubbed += 1
            writer.writerow(row)
            continue

        record = rewritten[spec.label]
        if row["object_id"] == spec.parent_id:
            parent = sync_parent_row(row, spec, record)
            writer.writerow(parent)
            parent_rows[spec.subject_id] += 1
            touched += 1
            if spec.subject_id not in has_registry:
                writer.writerow(registry_row(parent, spec, record))
                registry_rows[spec.subject_id] += 1
                touched += 1
            continue
        if row["object_id"] == spec.new_identifier:
            writer.writerow(registry_row(row, spec, record))
            registry_rows[spec.subject_id] += 1
            touched += 1
            continue
        raise SystemExit(f"{spec.subject_id} has unexpected SSSOM object {row['object_id']}")

    bad_parent = {
        spec.subject_id: parent_rows[spec.subject_id]
        for spec in SULFATE_HYDRATES
        if parent_rows[spec.subject_id] != 1
    }
    bad_registry = {
        spec.subject_id: registry_rows[spec.subject_id]
        for spec in SULFATE_HYDRATES
        if registry_rows[spec.subject_id] != 1
    }
    if bad_parent or bad_registry or dropped_citric > 1:
        raise SystemExit(
            "SSSOM rewrite missed rows: "
            f"parents={bad_parent}, registries={bad_registry}, "
            f"dropped_citric={dropped_citric}"
        )

    return "".join(preamble) + out.getvalue(), touched, scrubbed, len(has_registry)


def collect_membership_moves(
    occurrences: Path,
) -> tuple[dict[tuple[str, str], dict[str, int]], dict[str, int]]:
    moves: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: defaultdict(int))
    counts: dict[str, int] = defaultdict(int)
    with occurrences.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for field in ("preferred_term", "recipe_id", "resolved_identifier"):
            if field not in (reader.fieldnames or []):
                raise SystemExit(f"{occurrences} has no {field!r} column")
        for row in reader:
            target = SOURCE_LABEL_TO_TARGET.get(source_label_key(row.get("preferred_term") or ""))
            if target is None:
                continue
            source = str(row.get("resolved_identifier") or "").strip()
            recipe = str(row.get("recipe_id") or "").strip()
            if not source or not recipe or source == target:
                continue
            moves[(source, recipe)][target] += 1
            counts[target] += 1
    return moves, counts


def update_membership_header(comments: list[str], rows: dict[tuple[str, str], int]) -> list[str]:
    if not comments:
        return comments
    first = comments[0]
    first = re.sub(r"edges=\d+", f"edges={len(rows)}", first)
    first = re.sub(
        r"mim_records=\d+",
        f"mim_records={len({identifier for identifier, _ in rows})}",
        first,
    )
    first = re.sub(
        r"recipes=\d+",
        f"recipes={len({recipe for _, recipe in rows})}",
        first,
    )
    return [first, *comments[1:]]


def rewrite_membership(
    moves: dict[tuple[str, str], dict[str, int]],
) -> tuple[str, dict[str, int], int, int]:
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments: list[str] = []
    table: list[list[str]] = []
    for line in lines:
        if line.startswith("#"):
            comments.append(line if line.endswith("\n") else f"{line}\n")
        else:
            table.append(line.rstrip("\n").split("\t"))

    header, data = table[0], table[1:]
    rows = {
        (cells[0], cells[1]): int(cells[2])
        for cells in data
        if len(cells) == 3 and cells[0] and cells[1]
    }
    moved: dict[str, int] = defaultdict(int)
    partial_splits = 0
    skipped = 0
    for source_key, targets in moves.items():
        available = rows.get(source_key, 0)
        move_count = sum(targets.values())
        if not available:
            skipped += move_count
            continue
        if available < move_count:
            raise SystemExit(
                f"{source_key} has {available} membership occurrence(s), "
                f"cannot move {move_count}"
            )
        if available > move_count:
            rows[source_key] = available - move_count
            partial_splits += 1
        else:
            rows.pop(source_key)
        _, recipe = source_key
        for target, count in targets.items():
            rows[(target, recipe)] = rows.get((target, recipe), 0) + count
            moved[target] += count

    comments = update_membership_header(comments, rows)
    out = [*comments, "\t".join(header) + "\n"]
    out.extend(
        f"{identifier}\t{recipe}\t{count}\n" for (identifier, recipe), count in sorted(rows.items())
    )
    return "".join(out), dict(sorted(moved.items())), partial_splits, skipped


def sync_affected_occurrence_stats(
    records: list[dict],
    membership_text: str,
) -> int:
    affected = {
        "CHEBI:30769",
        "CHEBI:31404",
        "CHEBI:32599",
        "CHEBI:75832",
        "CHEBI:86360",
    } | {spec.new_identifier for spec in SULFATE_HYDRATES}
    by_identifier: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    lines = [line for line in membership_text.splitlines() if not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        if row["mim_identifier"] not in affected:
            continue
        by_identifier[row["mim_identifier"]][0] += 1
        by_identifier[row["mim_identifier"]][1] += int(row["occurrences"])

    changed = 0
    for record in records:
        identifier = str(record.get("identifier") or "")
        if identifier not in affected or record.get("mapping_status") == "REJECTED":
            continue
        stats = record.get("occurrence_statistics") or {}
        old = (stats.get("media_count") or 0, stats.get("total_occurrences") or 0)
        new = tuple(by_identifier.get(identifier, [0, 0]))
        if old == new:
            continue
        record["occurrence_statistics"] = {
            **stats,
            "media_count": new[0],
            "total_occurrences": new[1],
        }
        record.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "REFRESHED_HYDRATE_OCCURRENCES",
                "changes": (
                    f"occurrence_statistics {old[0]}/{old[1]} -> "
                    f"{new[0]}/{new[1]} after moving reviewed hydrate source "
                    "labels off their anhydrous parent identifiers and onto "
                    f"their exact hydrate identities ({ISSUE})."
                ),
                "previous_status": "MAPPED",
                "new_status": "MAPPED",
                "llm_assisted": False,
            }
        )
        changed += 1
    return changed


def rewrite_hydrate_review() -> tuple[str, int]:
    rows = list(
        csv.DictReader(
            HYDRATE_REVIEW.read_text(encoding="utf-8").splitlines(),
            delimiter="\t",
        )
    )
    changed = 0
    for row in rows:
        spec = SPECS_BY_LABEL.get(row.get("preferred_term") or "")
        if spec is not None:
            row["identifier"] = spec.new_identifier
            row["cas_rn_current"] = ""
            row["cas_correct_or_UNKNOWN"] = "UNKNOWN"
            row["grounding_verdict"] = "CORRECT"
            row["recommended_target_curie"] = spec.new_identifier
            row["action"] = "LOCAL_IDENTITY_RETAINED"
            row["sssom_predicate_published"] = "skos:narrowMatch|skos:exactMatch"
            row["notes"] = (
                f"MIM keeps {spec.label} as a local hydrate identity because "
                "no exact external ontology term has been verified. "
                f"{spec.parent_id} ({spec.parent_label}) is published only as "
                "a skos:narrowMatch anhydrous parent; the curated formula is "
                f"{spec.formula}, with no parent CAS, InChI, or SMILES."
            )
            changed += 1
            continue
        if row.get("preferred_term") == "Citric Acid•H2O":
            row["identifier"] = "CHEBI:31404"
            row["ontology_label"] = "Citric acid monohydrate"
            row["cas_rn_current"] = "5949-29-1"
            row["cas_correct_or_UNKNOWN"] = "5949-29-1"
            row["grounding_verdict"] = "CORRECT"
            row["recommended_target_curie"] = "CHEBI:31404"
            row["action"] = "MERGED_INTO_EXISTING"
            row["sssom_predicate_published"] = "skos:exactMatch"
            row["notes"] = (
                "Citric Acid•H2O was merged into MIM's existing exact "
                "CHEBI:31404 Citric acid x H2O record and retained there as "
                "a source label synonym."
            )
            changed += 1

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=rows[0].keys(),
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue(), changed


def rewrite_duplicate_baseline() -> tuple[str, int]:
    rows = list(
        csv.DictReader(
            DUPLICATE_BASELINE.read_text(encoding="utf-8").splitlines(),
            delimiter="\t",
        )
    )
    resolved = {
        "CHEBI:30769",
        "CHEBI:32599",
        "CHEBI:75832",
        "CHEBI:86360",
    }
    kept = [row for row in rows if row["identifier"] not in resolved]
    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=rows[0].keys(),
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(kept)
    return out.getvalue(), len(rows) - len(kept)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--occurrences", type=Path, default=DEFAULT_OCCURRENCES)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    doc = yaml.safe_load(COLLECTION.read_text(encoding="utf-8")) or {}
    records = doc.get("ingredients") or []

    rewritten = rewrite_sulfate_records(records)
    citric = merge_citric_bullet_record(records)
    moves, source_counts = collect_membership_moves(args.occurrences)
    membership_text, moved, partial_splits, skipped = rewrite_membership(moves)
    stats_changed = sync_affected_occurrence_stats(records, membership_text)
    sssom_text, sssom_touched, sssom_scrubbed, existing_registries = rewrite_sssom(
        records,
        rewritten,
        citric,
    )
    hydrate_review_text, hydrate_review_changed = rewrite_hydrate_review()
    duplicate_baseline_text, duplicate_baseline_removed = rewrite_duplicate_baseline()
    doc["generation_date"] = STAMP

    print(f"localized {len(rewritten)} sulfate hydrate record(s)")
    print("merged Citric Acid•H2O into Citric acid x H2O")
    print(f"source rows by target: {dict(sorted(source_counts.items()))}")
    print(f"moved memberships: {moved}")
    print(f"skipped {skipped} newer source row(s) absent from the membership artifact")
    print(f"split {partial_splits} parent edge(s) with mixed old/new counts")
    print(f"refreshed {stats_changed} occurrence_statistics block(s)")
    print(
        f"rewrote {sssom_touched} SSSOM row(s), preserving "
        f"{existing_registries} existing registry row(s)"
    )
    print(f"scrubbed reviewed hydrate aliases from {sssom_scrubbed} SSSOM row(s)")
    print(f"updated {hydrate_review_changed} hydrate_review row(s)")
    print(f"removed {duplicate_baseline_removed} duplicate baseline row(s)")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(doc, COLLECTION, backup=False, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    HYDRATE_REVIEW.write_text(hydrate_review_text, encoding="utf-8")
    DUPLICATE_BASELINE.write_text(duplicate_baseline_text, encoding="utf-8")
    print("\nwrote curated collection, SSSOM, membership, hydrate_review, and baseline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
