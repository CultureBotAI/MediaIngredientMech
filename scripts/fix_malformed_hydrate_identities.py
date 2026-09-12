#!/usr/bin/env python3
"""Localize malformed hydrate labels instead of asserting known compounds (#344).

MediaDive still carries eleven source labels with hydration counts that do not
correspond to a verified hydrate. Nine had already been split onto local
``kgmicrobe.compound`` identifiers, while the two sulfate labels still shared
the exact anhydrous CHEBI identifier with the valid anhydrous records.

Keep every source label addressable, but remove the fabricated chemistry:

* every malformed label owns a local identity with a closeMatch to the
  anhydrous CHEBI parent;
* chemical_properties are blank until the upstream row is clarified;
* exact anhydrous and different-hydrate aliases are kept only as
  REJECTED_LABEL provenance; and
* the CaSO4/K2SO4 memberships move only for recipes whose source label names
  the malformed heptahydrate row.

Dry-run by default; pass ``--apply`` to write.
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

from mediaingredientmech.curation.hydrate_guard import (  # noqa: E402
    HYDRATE_NOTATION,
    implausible_water_counts,
    water_multiplicity,
)
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

STAMP = "2026-09-12T00:00:00+00:00"
MAPPING_DATE = STAMP[:10]
CURATOR = "fix_malformed_hydrate_identities"
ISSUE_SOURCE = "MIM:MIM curation (#344)"
MAX_OTHER_ENTRIES = 50

ONE_WATER_NOTATION = re.compile(r"[xX×·•・⋅∙.]\s*H2\s*O(?![0-9])")
VARIABLE_WATER_NOTATION = re.compile(r"[xX×·•・⋅∙.]\s*n\s*H2\s*O(?![0-9])")


@dataclass(frozen=True)
class MalformedHydrate:
    label: str
    subject_id: str
    old_identifier: str
    new_identifier: str
    parent_id: str
    parent_label: str
    mediadive_compound_id: str


MALFORMED_HYDRATES: tuple[MalformedHydrate, ...] = (
    MalformedHydrate(
        label="CaCl2 x 7 H2O",
        subject_id="MIM:Cacl2_X_7_H2o",
        old_identifier="kgmicrobe.compound:cacl2_x_7_h2o",
        new_identifier="kgmicrobe.compound:cacl2_x_7_h2o",
        parent_id="CHEBI:3312",
        parent_label="calcium dichloride",
        mediadive_compound_id="mediadive.compound:479",
    ),
    MalformedHydrate(
        label="CaSO4 x 7 H2O",
        subject_id="MIM:Caso4_X_7_H2o",
        old_identifier="CHEBI:31346",
        new_identifier="kgmicrobe.compound:caso4_x_7_h2o",
        parent_id="CHEBI:31346",
        parent_label="calcium sulfate",
        mediadive_compound_id="mediadive.compound:2000",
    ),
    MalformedHydrate(
        label="CuCl2 x 6 H2O",
        subject_id="MIM:Cucl2_X_6_H2o",
        old_identifier="kgmicrobe.compound:cucl2_x_6_h2o",
        new_identifier="kgmicrobe.compound:cucl2_x_6_h2o",
        parent_id="CHEBI:49553",
        parent_label="copper(II) chloride",
        mediadive_compound_id="mediadive.compound:1056",
    ),
    MalformedHydrate(
        label="FeCl2 x 6 H2O",
        subject_id="MIM:Fecl2_X_6_H2o",
        old_identifier="kgmicrobe.compound:fecl2_x_6_h2o",
        new_identifier="kgmicrobe.compound:fecl2_x_6_h2o",
        parent_id="CHEBI:30812",
        parent_label="iron dichloride",
        mediadive_compound_id="mediadive.compound:555",
    ),
    MalformedHydrate(
        label="FeCl2 x 7 H2O",
        subject_id="MIM:Fecl2_X_7_H2o",
        old_identifier="kgmicrobe.compound:fecl2_x_7_h2o",
        new_identifier="kgmicrobe.compound:fecl2_x_7_h2o",
        parent_id="CHEBI:30812",
        parent_label="iron dichloride",
        mediadive_compound_id="mediadive.compound:840",
    ),
    MalformedHydrate(
        label="FeCl3 x 4 H2O",
        subject_id="MIM:Fecl3_X_4_H2o",
        old_identifier="kgmicrobe.compound:fecl3_x_4_h2o",
        new_identifier="kgmicrobe.compound:fecl3_x_4_h2o",
        parent_id="CHEBI:30808",
        parent_label="iron trichloride",
        mediadive_compound_id="mediadive.compound:922",
    ),
    MalformedHydrate(
        label="K2SO4 x 7 H2O",
        subject_id="MIM:K2so4_X_7_H2o",
        old_identifier="CHEBI:32036",
        new_identifier="kgmicrobe.compound:k2so4_x_7_h2o",
        parent_id="CHEBI:32036",
        parent_label="potassium sulfate",
        mediadive_compound_id="mediadive.compound:1920",
    ),
    MalformedHydrate(
        label="MgCl2 x 7 H2O",
        subject_id="MIM:Mgcl2_X_7_H2o",
        old_identifier="kgmicrobe.compound:mgcl2_x_7_h2o",
        new_identifier="kgmicrobe.compound:mgcl2_x_7_h2o",
        parent_id="CHEBI:6636",
        parent_label="magnesium dichloride",
        mediadive_compound_id="mediadive.compound:632",
    ),
    MalformedHydrate(
        label="Na2HPO4 x 3 H2O",
        subject_id="MIM:Na2hpo4_X_3_H2o",
        old_identifier="kgmicrobe.compound:na2hpo4_x_3_h2o",
        new_identifier="kgmicrobe.compound:na2hpo4_x_3_h2o",
        parent_id="CHEBI:34683",
        parent_label="disodium hydrogenphosphate",
        mediadive_compound_id="mediadive.compound:525",
    ),
    MalformedHydrate(
        label="Na2HPO4 x 6 H2O",
        subject_id="MIM:Na2hpo4_X_6_H2o",
        old_identifier="kgmicrobe.compound:na2hpo4_x_6_h2o",
        new_identifier="kgmicrobe.compound:na2hpo4_x_6_h2o",
        parent_id="CHEBI:34683",
        parent_label="disodium hydrogenphosphate",
        mediadive_compound_id="mediadive.compound:1580",
    ),
    MalformedHydrate(
        label="NiCl2 x 5 H2O",
        subject_id="MIM:Nicl2_X_5_H2o",
        old_identifier="kgmicrobe.compound:nicl2_x_5_h2o",
        new_identifier="kgmicrobe.compound:nicl2_x_5_h2o",
        parent_id="CHEBI:34887",
        parent_label="nickel dichloride",
        mediadive_compound_id="mediadive.compound:2037",
    ),
)

SPECS_BY_LABEL = {spec.label: spec for spec in MALFORMED_HYDRATES}
SPECS_BY_SUBJECT = {spec.subject_id: spec for spec in MALFORMED_HYDRATES}
SULFATE_MEMBERSHIP_MOVES = {
    ("CHEBI:31346", "CultureMech:002288"): "kgmicrobe.compound:caso4_x_7_h2o",
    ("CHEBI:31346", "CultureMech:010491"): "kgmicrobe.compound:caso4_x_7_h2o",
    ("CHEBI:31346", "CultureMech:014112"): "kgmicrobe.compound:caso4_x_7_h2o",
    ("CHEBI:31346", "CultureMech:014113"): "kgmicrobe.compound:caso4_x_7_h2o",
    ("CHEBI:32036", "CultureMech:003225"): "kgmicrobe.compound:k2so4_x_7_h2o",
    ("CHEBI:32036", "CultureMech:010337"): "kgmicrobe.compound:k2so4_x_7_h2o",
    ("CHEBI:32036", "CultureMech:010338"): "kgmicrobe.compound:k2so4_x_7_h2o",
    ("CHEBI:32036", "CultureMech:013797"): "kgmicrobe.compound:k2so4_x_7_h2o",
}


def append_mapping_source(source: str) -> str:
    tokens = [token for token in source.split("|") if token]
    if ISSUE_SOURCE not in tokens:
        tokens.append(ISSUE_SOURCE)
    return "|".join(tokens)


def find(records: list[dict], spec: MalformedHydrate) -> dict:
    hits = [
        record
        for record in records
        if record.get("preferred_term") == spec.label and record.get("mapping_status") == "MAPPED"
    ]
    if len(hits) != 1:
        raise SystemExit(f"expected one mapped record named {spec.label!r}; found {len(hits)}")
    return hits[0]


def _water_count(text: object) -> str | None:
    text = str(text or "")
    if implausible_water_counts(text):
        return "INVALID"
    count = water_multiplicity(text)
    if count:
        return count
    if HYDRATE_NOTATION.search(text) and not VARIABLE_WATER_NOTATION.search(text):
        if ONE_WATER_NOTATION.search(text):
            return "1"
    return None


def _same_malformed_surface(owner: str, text: object) -> bool:
    text_count = _water_count(text)
    return text_count is not None and text_count == _water_count(owner)


def _owner_by_token(records: list[dict]) -> dict[str, str]:
    owner_by_token: dict[str, str] = {}
    for spec in MALFORMED_HYDRATES:
        record = find(records, spec)
        owner_by_token[spec.label.strip().casefold()] = spec.label
        for synonym in record.get("synonyms") or []:
            if not is_resolving_synonym(synonym):
                continue
            if synonym.get("synonym_type") == "EXACT_SYNONYM":
                continue
            text = str(synonym.get("synonym_text") or "").strip()
            if _same_malformed_surface(spec.label, text):
                owner_by_token[text.casefold()] = spec.label
    return owner_by_token


def _reject_synonym(synonym: dict) -> bool:
    if synonym.get("synonym_type") == "REJECTED_LABEL":
        return False
    synonym["synonym_type"] = "REJECTED_LABEL"
    return True


def reject_owner_false_synonyms(record: dict, spec: MalformedHydrate) -> list[str]:
    rejected: list[str] = []
    owner_count = _water_count(spec.label)
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict):
            continue
        text = str(synonym.get("synonym_text") or "").strip()
        text_count = _water_count(text)
        is_false = (
            synonym.get("synonym_type") == "EXACT_SYNONYM"
            or text_count == "INVALID"
            or (text_count is not None and text_count != owner_count)
        )
        if is_false and _reject_synonym(synonym):
            rejected.append(text)
    return rejected


def reject_cross_owner_synonyms(
    records: list[dict],
    owner_by_token: dict[str, str],
) -> dict[str, set[str]]:
    rejected_by_label: dict[str, set[str]] = defaultdict(set)
    for record in records:
        if record.get("mapping_status") == "REJECTED":
            continue
        preferred_term = str(record.get("preferred_term") or "")
        for synonym in record.get("synonyms") or []:
            if not isinstance(synonym, dict) or not is_resolving_synonym(synonym):
                continue
            text = str(synonym.get("synonym_text") or "").strip()
            owner = owner_by_token.get(text.casefold())
            if owner is None or owner == preferred_term:
                continue
            if _reject_synonym(synonym):
                rejected_by_label[preferred_term].add(text)

    for preferred_term, labels in sorted(rejected_by_label.items()):
        rendered = ", ".join(repr(label) for label in sorted(labels, key=str.casefold))
        record = next(
            record for record in records if record.get("preferred_term") == preferred_term
        )
        record.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "REJECTED_MALFORMED_HYDRATE_ALIASES",
                "changes": (
                    "Marked malformed hydrate alias(es) as REJECTED_LABEL so they "
                    f"remain on their own #344 local identities only: {rendered}."
                ),
                "previous_status": "MAPPED",
                "new_status": "MAPPED",
                "llm_assisted": False,
            }
        )
    return rejected_by_label


def rewrite_records(
    records: list[dict],
) -> tuple[dict[str, dict], dict[str, str], dict[str, set[str]]]:
    owner_by_token = _owner_by_token(records)
    rewritten: dict[str, dict] = {}
    active = [record for record in records if record.get("mapping_status") != "REJECTED"]

    for spec in MALFORMED_HYDRATES:
        record = find(records, spec)
        conflicts = [
            other.get("preferred_term")
            for other in active
            if other is not record and other.get("identifier") == spec.new_identifier
        ]
        if conflicts:
            raise SystemExit(
                f"{spec.new_identifier} is already held by active record(s): {conflicts}"
            )
        if record.get("identifier") != spec.old_identifier:
            raise SystemExit(
                f"{spec.label} is on {record.get('identifier')}, " f"not {spec.old_identifier}"
            )

        ontology_mapping = record.setdefault("ontology_mapping", {})
        if ontology_mapping.get("ontology_id") != spec.parent_id:
            raise SystemExit(
                f"{spec.label} parent is {ontology_mapping.get('ontology_id')}, "
                f"not {spec.parent_id}"
            )

        old_quality = ontology_mapping.get("mapping_quality")
        old_chemistry = dict(record.get("chemical_properties") or {})
        rejected_synonyms = reject_owner_false_synonyms(record, spec)
        record["identifier"] = spec.new_identifier
        if record.get("kg_microbe_node_id") in {
            spec.old_identifier,
            spec.new_identifier,
            spec.parent_id,
        }:
            record.pop("kg_microbe_node_id")
        record["chemical_properties"] = {}

        ontology_mapping.update(
            {
                "ontology_id": spec.parent_id,
                "ontology_label": spec.parent_label,
                "ontology_source": "CHEBI",
                "mapping_quality": "CLOSE_MATCH",
            }
        )
        ontology_mapping.setdefault("evidence", []).append(
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": "MIM curation (#344)",
                "notes": (
                    f"{spec.mediadive_compound_id} still carries the source label "
                    f"{spec.label!r}, but no exact ontology term or CAS has been "
                    f"verified for that stated hydration count. {spec.parent_id} "
                    f"({spec.parent_label}) is retained only as the closest "
                    "anhydrous parent while the source label keeps its local "
                    "kgmicrobe.compound identity."
                ),
            }
        )
        record.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "LOCALIZED_MALFORMED_HYDRATE_IDENTITY",
                "changes": (
                    f"identifier {spec.old_identifier} -> {spec.new_identifier}; "
                    f"mapping_quality {old_quality} -> CLOSE_MATCH. Cleared "
                    f"unverified chemical_properties {old_chemistry!r} and "
                    f"marked {len(rejected_synonyms)} anhydrous or wrong-hydrate "
                    f"synonym(s) as REJECTED_LABEL for {spec.mediadive_compound_id} "
                    "(#344)."
                ),
                "previous_status": "MAPPED",
                "new_status": "MAPPED",
                "llm_assisted": False,
            }
        )
        rewritten[spec.label] = record

    rejected_by_label = reject_cross_owner_synonyms(records, owner_by_token)
    return rewritten, owner_by_token, rejected_by_label


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
        if len(out) >= MAX_OTHER_ENTRIES:
            break
    return "|".join(out)


def _sync_parent_row(
    row: dict[str, str],
    spec: MalformedHydrate,
    record: dict,
) -> dict[str, str]:
    out = dict(row)
    out["object_id"] = spec.parent_id
    out["object_label"] = spec.parent_label
    out["object_source"] = object_source_for(spec.parent_id)
    out["predicate_id"] = PREDICATE["CLOSE_MATCH"]
    out["mapping_justification"] = JUSTIFICATION["CLOSE_MATCH"]
    out["source"] = append_mapping_source(row.get("source", ""))
    out["mapping_date"] = MAPPING_DATE
    out["confidence"] = CONFIDENCE["CLOSE_MATCH"]
    out["comment"] = (
        f"Local kgmicrobe.compound identity retained because {spec.label} is an "
        f"unresolved malformed MediaDive hydrate label; {spec.parent_id} is the "
        "anhydrous parent."
    )
    out["other"] = _sssom_other(record, object_label=spec.parent_label)
    out["validation_method"] = ""
    return out


def _registry_row(
    row: dict[str, str],
    spec: MalformedHydrate,
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
    out["other"] = _sssom_other(record, object_label=spec.parent_label)
    out["validation_method"] = ""
    return out


def _scrub_other(row: dict[str, str], owner_by_token: dict[str, str]) -> bool:
    old = row.get("other") or ""
    subject_label = row.get("subject_label") or ""
    kept = [
        token
        for token in old.split("|")
        if owner_by_token.get(token.strip().casefold(), subject_label) == subject_label
    ]
    row["other"] = "|".join(kept)
    return row["other"] != old


def rewrite_sssom(
    records: list[dict],
    rewritten: dict[str, dict],
    owner_by_token: dict[str, str],
) -> tuple[str, int, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    rows = list(csv.DictReader(body, delimiter="\t"))
    has_registry = {
        row["subject_id"]
        for row in rows
        for spec in MALFORMED_HYDRATES
        if row["subject_id"] == spec.subject_id and row["object_id"] == spec.new_identifier
    }

    parent_rows: dict[str, int] = defaultdict(int)
    registry_rows: dict[str, int] = defaultdict(int)
    touched = 0
    scrubbed = 0
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    out.write(f"{header}\n")

    for row in rows:
        spec = SPECS_BY_SUBJECT.get(row["subject_id"])
        if spec is None:
            if _scrub_other(row, owner_by_token):
                writer.writerow(row)
                scrubbed += 1
            else:
                writer.writerow(row)
            continue

        record = rewritten[spec.label]
        if row["object_id"] == spec.parent_id:
            parent = _sync_parent_row(row, spec, record)
            writer.writerow(parent)
            parent_rows[spec.subject_id] += 1
            touched += 1
            if spec.subject_id not in has_registry:
                writer.writerow(_registry_row(parent, spec, record))
                registry_rows[spec.subject_id] += 1
                touched += 1
            continue
        if row["object_id"] == spec.new_identifier:
            writer.writerow(_registry_row(row, spec, record))
            registry_rows[spec.subject_id] += 1
            touched += 1
            continue
        raise SystemExit(f"{spec.subject_id} has unexpected SSSOM object {row['object_id']}")

    bad_parent = {
        spec.subject_id: parent_rows[spec.subject_id]
        for spec in MALFORMED_HYDRATES
        if parent_rows[spec.subject_id] != 1
    }
    bad_registry = {
        spec.subject_id: registry_rows[spec.subject_id]
        for spec in MALFORMED_HYDRATES
        if registry_rows[spec.subject_id] != 1
    }
    if bad_parent or bad_registry:
        raise SystemExit(
            f"malformed row rewrite missed rows: parents={bad_parent}, "
            f"registries={bad_registry}"
        )

    return "".join(preamble) + out.getvalue(), touched, scrubbed, len(has_registry)


def rewrite_membership() -> tuple[str, dict[str, int]]:
    move_counts = dict.fromkeys(set(SULFATE_MEMBERSHIP_MOVES.values()), 0)
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments: list[str] = []
    rows: list[list[str]] = []

    for line in lines:
        if line.startswith("#"):
            comments.append(line if line.endswith("\n") else f"{line}\n")
            continue
        cells = line.rstrip("\n").split("\t")
        replacement = SULFATE_MEMBERSHIP_MOVES.get((cells[0], cells[1]))
        if replacement is not None:
            cells[0] = replacement
            move_counts[replacement] += int(cells[2])
        rows.append(cells)

    moved = sum(move_counts.values())
    if moved != len(SULFATE_MEMBERSHIP_MOVES):
        raise SystemExit(
            f"moved {moved} sulfate membership rows, " f"expected {len(SULFATE_MEMBERSHIP_MOVES)}"
        )

    header, data = rows[0], rows[1:]
    data.sort(key=lambda cells: tuple(cells[:2]))
    keys = [(cells[0], cells[1]) for cells in data]
    if len(keys) != len(set(keys)):
        raise SystemExit("membership rewrite would create duplicate edge keys")

    out = [*comments, "\t".join(header) + "\n"]
    out.extend("\t".join(row) + "\n" for row in data)
    return "".join(out), move_counts


def sync_affected_occurrence_stats(
    records: list[dict],
    membership_text: str,
) -> int:
    affected = {
        "CHEBI:31346",
        "CHEBI:32036",
        "kgmicrobe.compound:caso4_x_7_h2o",
        "kgmicrobe.compound:k2so4_x_7_h2o",
    }
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
                "action": "REFRESHED_MALFORMED_SULFATE_OCCURRENCES",
                "changes": (
                    f"occurrence_statistics {old[0]}/{old[1]} -> "
                    f"{new[0]}/{new[1]} after moving CaSO4/K2SO4 x 7 H2O "
                    "memberships off the anhydrous parent identifiers (#344)."
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
        if spec is None:
            continue
        row["identifier"] = spec.new_identifier
        row["cas_rn_current"] = ""
        row["grounding_verdict"] = "CORRECT"
        row["recommended_target_curie"] = spec.new_identifier
        row["action"] = "LOCAL_IDENTITY_RETAINED"
        row["sssom_predicate_published"] = "skos:closeMatch|skos:exactMatch"
        if spec.new_identifier.endswith(("caso4_x_7_h2o", "k2so4_x_7_h2o")):
            row["source_rows_in_culturemech"] = "4"
        row["notes"] = (
            f"MIM keeps {spec.label} as a local unresolved source identity for "
            f"{spec.mediadive_compound_id}. {spec.parent_id} "
            f"({spec.parent_label}) is published only as a skos:closeMatch "
            "anhydrous parent; no exact formula, CAS, InChI, or SMILES is "
            "published until the malformed MediaDive hydration count is "
            "corrected upstream."
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    doc = yaml.safe_load(COLLECTION.read_text(encoding="utf-8")) or {}
    records = doc.get("ingredients") or []

    rewritten, owner_by_token, rejected_by_label = rewrite_records(records)
    membership_text, moved = rewrite_membership()
    stats_changed = sync_affected_occurrence_stats(records, membership_text)
    sssom_text, sssom_touched, sssom_scrubbed, existing_registries = rewrite_sssom(
        records,
        rewritten,
        owner_by_token,
    )
    hydrate_review_text, hydrate_review_changed = rewrite_hydrate_review()
    doc["generation_date"] = STAMP

    print(f"rewrote {len(rewritten)} malformed hydrate record(s)")
    print(f"rejected aliases on {len(rejected_by_label)} neighboring record(s)")
    print(f"moved sulfate memberships: {dict(sorted(moved.items()))}")
    print(f"refreshed {stats_changed} occurrence_statistics block(s)")
    print(
        f"rewrote {sssom_touched} malformed SSSOM row(s), preserving "
        f"{existing_registries} existing registry row(s)"
    )
    print(f"scrubbed malformed aliases from {sssom_scrubbed} other SSSOM row(s)")
    print(f"updated {hydrate_review_changed} hydrate_review row(s)")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(doc, COLLECTION, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    HYDRATE_REVIEW.write_text(hydrate_review_text, encoding="utf-8")
    print("\nwrote curated collection, SSSOM, membership, and hydrate_review")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
