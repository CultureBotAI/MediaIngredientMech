#!/usr/bin/env python3
"""Repair element ingredient records that over-claimed ChEBI atom terms (#631)."""

from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.sssom_grading import CONFIDENCE, JUSTIFICATION  # noqa: E402
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

CURATOR = "fix_element_atom_overclaims"
ISSUE = "#631"
STAMP_SOURCE = f"MIM:curator={CURATOR}"

CALCIUM_2_ID = "CHEBI:29108"
MAGNESIUM_2_ID = "CHEBI:18420"
IRON_0_ID = "CHEBI:82664"
COPPER_ID = "kgmicrobe.compound:copper"
MOLYBDENUM_ID = "kgmicrobe.compound:molybdenum"

ATOM_TO_SURVIVOR = {
    "CHEBI:22984": CALCIUM_2_ID,
    "CHEBI:25107": MAGNESIUM_2_ID,
    "CHEBI:18248": IRON_0_ID,
    "CHEBI:28694": COPPER_ID,
    "CHEBI:28685": MOLYBDENUM_ID,
}

DROP_SUBJECTS = {
    "MIM:Calcium",
    "MIM:Magnesium",
    "MIM:Iron_Powder",
}

DROP_SSSOM_ROWS = 3

IRON_ATOM_SYNONYMS = {
    "26fe",
    "eisen",
    "fer",
    "ferrum",
    "hierro",
    "iron atom",
}


@dataclass(frozen=True)
class CationMerge:
    source_identifier: str
    source_term: str
    target_identifier: str
    target_term: str
    target_label: str
    transferred_occurrences: int
    source_note: str


@dataclass(frozen=True)
class LocalFallback:
    old_identifier: str
    preferred_term: str
    identifier: str
    note: str


CATION_MERGES = (
    CationMerge(
        source_identifier="CHEBI:22984",
        source_term="Calcium",
        target_identifier=CALCIUM_2_ID,
        target_term="Calcium(2+)",
        target_label="calcium(2+)",
        transferred_occurrences=2,
        source_note=(
            "CultureMech's source rows explicitly carry KEGG:ca2, so the "
            "source label denotes dissolved Ca2+ rather than a neutral "
            "calcium atom."
        ),
    ),
    CationMerge(
        source_identifier="CHEBI:25107",
        source_term="Magnesium",
        target_identifier=MAGNESIUM_2_ID,
        target_term="Magnesium(2+)",
        target_label="magnesium(2+)",
        transferred_occurrences=3,
        source_note=(
            "CultureMech's source rows explicitly carry KEGG:mg2, so the "
            "source label denotes dissolved Mg2+ rather than a neutral "
            "magnesium atom."
        ),
    ),
)

LOCAL_FALLBACKS = (
    LocalFallback(
        old_identifier="CHEBI:28694",
        preferred_term="Copper",
        identifier=COPPER_ID,
        note=(
            "The source rows are TAP trace-element entries, and CultureMech "
            "only recorded KEGG:cu with no charge or counter-ion. Keep a local "
            "identity until a precise copper species is evidenced."
        ),
    ),
    LocalFallback(
        old_identifier="CHEBI:28685",
        preferred_term="Molybdenum",
        identifier=MOLYBDENUM_ID,
        note=(
            "The source rows are TAP trace-element entries with no charge or "
            "counter-ion. Keep a local identity until a precise molybdenum "
            "species is evidenced."
        ),
    ),
)


def _read_collection(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _find_record(
    records: list[dict],
    identifier: str,
    preferred_term: str,
    mapping_status: str | None = "MAPPED",
) -> dict:
    hits = [
        record
        for record in records
        if record.get("identifier") == identifier
        and record.get("preferred_term") == preferred_term
        and (mapping_status is None or record.get("mapping_status") == mapping_status)
    ]
    if len(hits) != 1:
        raise SystemExit(
            f"{preferred_term!r} on {identifier} matched {len(hits)} record(s), "
            "expected exactly 1"
        )
    return hits[0]


def _mapping(
    ontology_id: str,
    ontology_label: str,
    ontology_source: str,
    mapping_quality: str,
    notes: str,
) -> dict:
    return {
        "ontology_id": ontology_id,
        "ontology_label": ontology_label,
        "ontology_source": ontology_source,
        "mapping_quality": mapping_quality,
        "evidence": [
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": f"MIM curation ({ISSUE})",
                "notes": notes,
            }
        ],
    }


def _dedupe_append(
    synonyms: list[dict],
    synonym: dict,
    seen: set[str],
) -> bool:
    text = str(synonym.get("synonym_text") or "").strip()
    if not text:
        return False
    key = text.casefold()
    if key in seen:
        return False
    synonyms.append(synonym)
    seen.add(key)
    return True


def _add_synonym(record: dict, text: str, source: str) -> bool:
    synonyms = record.setdefault("synonyms", [])
    seen = {str(synonym.get("synonym_text") or "").strip().casefold() for synonym in synonyms}
    return _dedupe_append(
        synonyms,
        {
            "synonym_text": text,
            "synonym_type": "RAW_TEXT",
            "source": source,
        },
        seen,
    )


def _append_source(source: str) -> str:
    pieces = [piece for piece in source.split("|") if piece]
    if STAMP_SOURCE not in pieces:
        pieces.append(STAMP_SOURCE)
    return "|".join(pieces)


def _zero_occurrences(record: dict) -> None:
    record["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}


def _tombstone(
    record: dict,
    old_identifier: str,
    target_identifier: str,
    target_mapping: dict,
    stamp: str,
    changes: str,
) -> None:
    record["identifier"] = target_identifier
    record["ontology_mapping"] = copy.deepcopy(target_mapping)
    record["mapping_status"] = "REJECTED"
    record["representative"] = target_identifier
    if record.get("kg_microbe_node_id") == old_identifier:
        record["kg_microbe_node_id"] = target_identifier
    _zero_occurrences(record)
    record.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_INTO",
            "changes": changes,
            "previous_status": "MAPPED",
            "new_status": "REJECTED",
            "llm_assisted": False,
        }
    )


def _merge_cation_source(records: list[dict], spec: CationMerge, stamp: str) -> bool:
    source = _find_record(records, spec.source_identifier, spec.source_term)
    target = _find_record(records, spec.target_identifier, spec.target_term)
    if source.get("occurrence_statistics") != {
        "total_occurrences": spec.transferred_occurrences,
        "media_count": spec.transferred_occurrences,
    }:
        raise SystemExit(
            f"{spec.source_term} occurrence statistics drifted: "
            f"{source.get('occurrence_statistics')}"
        )

    target["occurrence_statistics"]["total_occurrences"] = spec.transferred_occurrences
    target["occurrence_statistics"]["media_count"] = spec.transferred_occurrences
    added = _add_synonym(
        target,
        spec.source_term,
        "culturemech:output/ingredient_occurrences.tsv",
    )
    target.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_FROM_MAPPED_RECORD",
            "changes": (
                f"Absorbed {spec.source_term!r} from {spec.source_identifier}; "
                f"moved {spec.transferred_occurrences} CultureMech occurrence(s) "
                f"from the ChEBI atom term to {spec.target_identifier}. "
                f"{spec.source_note} ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    _tombstone(
        source,
        spec.source_identifier,
        spec.target_identifier,
        _mapping(
            spec.target_identifier,
            spec.target_label,
            "CHEBI",
            "EXACT_MATCH",
            spec.source_note,
        ),
        stamp,
        (
            f"Merged into {spec.target_identifier} {spec.target_term!r}; "
            f"transferred {spec.transferred_occurrences} CultureMech occurrence(s) "
            "and dropped the atom-grounded SSSOM row. "
            f"{spec.source_note} ({ISSUE})."
        ),
    )
    return added


def _retarget_local_fallback(record: dict, spec: LocalFallback, stamp: str) -> None:
    record["identifier"] = spec.identifier
    if record.get("kg_microbe_node_id") == spec.old_identifier:
        record["kg_microbe_node_id"] = spec.identifier
    record["ontology_mapping"] = _mapping(
        spec.identifier,
        spec.preferred_term,
        "kgmicrobe.compound",
        "FALLBACK_REGISTRY",
        f"{spec.note} ({ISSUE})",
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "CORRECTED",
            "changes": (
                f"identifier {spec.old_identifier} -> {spec.identifier}; "
                "removed exact ChEBI atom grounding. "
                f"{spec.note} ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )


def _merge_iron(records: list[dict], stamp: str) -> tuple[int, int]:
    iron = _find_record(records, "CHEBI:18248", "Iron")
    powder = _find_record(records, IRON_0_ID, "Iron powder")

    rejected = 0
    for synonym in iron.get("synonyms") or []:
        text = str(synonym.get("synonym_text") or "").strip()
        if text.casefold() in IRON_ATOM_SYNONYMS:
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected += 1

    synonyms = iron.setdefault("synonyms", [])
    seen = {str(synonym.get("synonym_text") or "").strip().casefold() for synonym in synonyms}
    carried = _dedupe_append(
        synonyms,
        {
            "synonym_text": "Iron powder",
            "synonym_type": "RAW_TEXT",
            "source": f"MERGED_FROM_{IRON_0_ID}",
        },
        seen,
    )
    for synonym in powder.get("synonyms") or []:
        if is_resolving_synonym(synonym):
            carried += _dedupe_append(
                synonyms,
                {
                    "synonym_text": str(synonym.get("synonym_text") or ""),
                    "synonym_type": "RAW_TEXT",
                    "source": f"MERGED_FROM_{IRON_0_ID}",
                },
                seen,
            )

    iron["identifier"] = IRON_0_ID
    iron["ontology_mapping"] = _mapping(
        IRON_0_ID,
        "iron(0)",
        "CHEBI",
        "EXACT_MATCH",
        (
            "CultureMech supplies Iron as a weighable grams-per-liter element, "
            "and MIM already curated Iron powder and Iron metal source labels "
            "to ChEBI iron(0), not to the ChEBI iron atom."
        ),
    )
    iron["occurrence_statistics"] = {"total_occurrences": 7, "media_count": 7}
    iron["chemical_properties"] = copy.deepcopy(powder.get("chemical_properties") or {})
    if powder.get("nutritional_roles"):
        iron["nutritional_roles"] = copy.deepcopy(powder["nutritional_roles"])
    iron.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_FROM_MAPPED_RECORD",
            "changes": (
                f"identifier CHEBI:18248 -> {IRON_0_ID}; retargeted from ChEBI "
                "iron atom to iron(0), absorbed the Iron powder record, moved "
                "2 atom memberships onto the 5 existing iron(0) memberships, "
                f"carried {carried} iron(0) label(s), and retained {rejected} "
                f"atom-only synonym(s) as REJECTED_LABEL ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )

    _tombstone(
        powder,
        IRON_0_ID,
        IRON_0_ID,
        iron["ontology_mapping"],
        stamp,
        (
            f"Merged into {IRON_0_ID} 'Iron'; occurrences transferred to the "
            "generic iron(0) record and the duplicate SSSOM row dropped "
            f"({ISSUE})."
        ),
    )
    return carried, rejected


def _sssom_other(record: dict, object_label: str) -> str:
    drop = {
        str(record.get("preferred_term") or "").strip().casefold(),
        object_label.casefold(),
        "",
    }
    out: list[str] = []
    seen: set[str] = set()
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict) or not is_resolving_synonym(synonym):
            continue
        text = str(synonym.get("synonym_text") or "").strip()
        key = text.casefold()
        if key in drop or key in seen:
            continue
        out.append(text)
        seen.add(key)
    return "|".join(out)


def _update_sssom_row(
    row: dict[str, str],
    record: dict,
    stamp: str,
    comment: str,
) -> None:
    mapping = record["ontology_mapping"]
    quality = mapping["mapping_quality"]
    object_id = mapping["ontology_id"]
    object_label = mapping["ontology_label"]

    row["object_id"] = object_id
    row["object_label"] = object_label
    row["object_source"] = object_source_for(object_id)
    row["predicate_id"] = "skos:exactMatch"
    row["mapping_justification"] = JUSTIFICATION[quality]
    row["source"] = _append_source(row.get("source") or "")
    row["mapping_date"] = stamp[:10]
    row["confidence"] = CONFIDENCE[quality]
    row["comment"] = comment
    row["other"] = _sssom_other(record, object_label)
    row["validation_method"] = ""


def rewrite_sssom(records_by_term: dict[str, dict], stamp: str) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    updates = {
        "MIM:Calcium~282~29": (
            "CHEBI:29108",
            records_by_term["Calcium(2+)"],
            "Merged the CultureMech calcium source label after removing "
            f"exact ChEBI atom grounding ({ISSUE}).",
        ),
        "MIM:Magnesium~282~29": (
            "CHEBI:18420",
            records_by_term["Magnesium(2+)"],
            "Merged the CultureMech magnesium source label after removing "
            f"exact ChEBI atom grounding ({ISSUE}).",
        ),
        "MIM:Iron": (
            "CHEBI:18248",
            records_by_term["Iron"],
            "Corrected from iron atom to weighable iron(0) and merged Iron " f"powder ({ISSUE}).",
        ),
        "MIM:Copper": (
            "CHEBI:28694",
            records_by_term["Copper"],
            "Removed exact ChEBI atom grounding; kept a local copper identity "
            f"pending an evidenced charge state or salt ({ISSUE}).",
        ),
        "MIM:Molybdenum": (
            "CHEBI:28685",
            records_by_term["Molybdenum"],
            "Removed exact ChEBI atom grounding; kept a local molybdenum "
            f"identity pending an evidenced charge state or salt ({ISSUE}).",
        ),
    }

    dropped = 0
    rewrote = 0
    seen_updates: set[str] = set()

    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    out.write(f"{header}\n")
    for line in body[1:]:
        reader = csv.DictReader(io.StringIO(f"{header}\n{line}"), delimiter="\t")
        row = next(reader)
        subject = row.get("subject_id") or ""
        if subject in DROP_SUBJECTS:
            dropped += 1
            continue
        update = updates.get(subject)
        if update is not None:
            expected_object_id, record, comment = update
            if row.get("object_id") != expected_object_id:
                raise SystemExit(
                    f"{subject} points at {row.get('object_id')}, " f"expected {expected_object_id}"
                )
            _update_sssom_row(row, record, stamp, comment)
            writer.writerow(row)
            seen_updates.add(subject)
            rewrote += 1
            continue
        out.write(line)
        if not line.endswith("\n"):
            out.write("\n")

    if dropped != DROP_SSSOM_ROWS:
        raise SystemExit(
            f"dropped {dropped} atom/duplicate SSSOM row(s), " f"expected {DROP_SSSOM_ROWS}"
        )
    missed = sorted(set(updates) - seen_updates)
    if missed:
        raise SystemExit(f"did not rewrite expected SSSOM subjects: {missed}")
    return "".join(preamble) + out.getvalue(), rewrote, dropped


def rewrite_membership() -> tuple[str, int]:
    comments: list[str] = []
    header: list[str] | None = None
    edges: dict[tuple[str, str], int] = {}
    moved = 0

    for line in MEMBERSHIP.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            comments.append(line)
            continue
        fields = line.split("\t")
        if fields == ["mim_identifier", "recipe_id", "occurrences"]:
            header = fields
            continue
        if len(fields) != 3:
            raise SystemExit(f"malformed membership row: {line!r}")
        identifier, recipe_id, occurrences = fields
        replacement = ATOM_TO_SURVIVOR.get(identifier)
        if replacement:
            identifier = replacement
            moved += 1
        key = (identifier, recipe_id)
        edges[key] = edges.get(key, 0) + int(occurrences)

    if header is None:
        raise SystemExit("membership header not found")
    if comments:
        comments[0] = re.sub(r"\bedges=\d+\b", f"edges={len(edges)}", comments[0])
        comments[0] = re.sub(
            r"\bmim_records=\d+\b",
            f"mim_records={len({identifier for identifier, _ in edges})}",
            comments[0],
        )

    out = [*(f"{comment}\n" for comment in comments), "\t".join(header) + "\n"]
    for (identifier, recipe_id), occurrences in sorted(edges.items()):
        out.append(f"{identifier}\t{recipe_id}\t{occurrences}\n")
    return "".join(out), moved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--membership-only",
        action="store_true",
        help="Only rewrite the existing CultureMech membership artifact.",
    )
    args = parser.parse_args(argv)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    if args.membership_only:
        membership_text, membership_moved = rewrite_membership()
        print(f"{'APPLIED' if args.apply else 'DRY RUN'}")
        print(f"  membership rows moved: {membership_moved}")
        if not args.apply:
            print("\nDry run only. Re-run with --apply to write.")
            return 0
        MEMBERSHIP.write_text(membership_text, encoding="utf-8")
        return 0

    mapped = _read_collection(MAPPED)
    records = mapped.get("ingredients", [])

    cation_labels = sum(_merge_cation_source(records, spec, stamp) for spec in CATION_MERGES)
    for spec in LOCAL_FALLBACKS:
        _retarget_local_fallback(
            _find_record(records, spec.old_identifier, spec.preferred_term),
            spec,
            stamp,
        )
    iron_labels, iron_rejections = _merge_iron(records, stamp)

    records_by_term = {str(record.get("preferred_term")): record for record in records}
    sssom_text, sssom_rewrote, sssom_dropped = rewrite_sssom(records_by_term, stamp)
    membership_text, membership_moved = rewrite_membership()

    mapped["generation_date"] = stamp
    mapped["total_count"] = len(records)
    mapped["mapped_count"] = sum(
        1 for record in records if record.get("mapping_status") == "MAPPED"
    )

    print(f"{'APPLIED' if args.apply else 'DRY RUN'}")
    print(f"  cation source labels carried: {cation_labels}")
    print(f"  iron source labels carried: {iron_labels}")
    print(f"  iron atom labels rejected: {iron_rejections}")
    print(f"  SSSOM rows rewritten: {sssom_rewrote}")
    print(f"  SSSOM rows dropped: {sssom_dropped}")
    print(f"  membership rows moved: {membership_moved}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to write.")
        return 0

    save_yaml(
        mapped,
        MAPPED,
        backup=False,
        validate=True,
        target_class="IngredientCollection",
    )
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
