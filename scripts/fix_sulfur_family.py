#!/usr/bin/env python3
"""Consolidate sulfur spelling/form records onto elemental sulfur (#368)."""

from __future__ import annotations

import argparse
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

from mediaingredientmech.sssom_grading import (  # noqa: E402
    CONFIDENCE,
    JUSTIFICATION,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

CURATOR = "fix_sulfur_family"
ISSUE = "#368"
STAMP_SOURCE = f"MIM:curator={CURATOR}"

SURVIVOR_TERM = "Sulfur"
SURVIVOR_OLD_ID = "CHEBI:26833"
SURVIVOR_ID = "CHEBI:33403"
SURVIVOR_LABEL = "elemental sulfur"

OLD_IDENTIFIERS = {
    "CHEBI:26833",
    "CHEBI:17909",
    "kgmicrobe.compound:sulfur_powder",
}
DROP_SUBJECTS = {"MIM:Sulphur", "MIM:Sulfur_Powder"}
DROP_SSSOM_ROWS = 3

REJECTED_SYNONYMS = {
    "16s",
    "polysulfur",
    "sulfur atom",
    "sulfur, homopolymer",
}

EXTRA_SOURCE_LABELS = (
    "Sulfur, powder",
    "Sulfur, powdered",
)


@dataclass(frozen=True)
class DuplicateSpec:
    identifier: str
    preferred_term: str


DUPLICATES = (
    DuplicateSpec("CHEBI:17909", "Sulphur"),
    DuplicateSpec("kgmicrobe.compound:sulfur_powder", "Sulfur (powder)"),
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
            f"{preferred_term!r} on {identifier} matched {len(hits)} record(s), expected exactly 1"
        )
    return hits[0]


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


def _append_source(source: str) -> str:
    pieces = [piece for piece in source.split("|") if piece]
    if STAMP_SOURCE not in pieces:
        pieces.append(STAMP_SOURCE)
    return "|".join(pieces)


def _merge_synonyms(target: dict, duplicates: tuple[dict, ...]) -> tuple[int, int]:
    synonyms = target.setdefault("synonyms", [])
    seen = {str(synonym.get("synonym_text") or "").strip().casefold() for synonym in synonyms}
    carried = 0
    rejected = 0

    for synonym in synonyms:
        text = str(synonym.get("synonym_text") or "").strip()
        if text.casefold() in REJECTED_SYNONYMS:
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected += 1

    for duplicate in duplicates:
        source = f"MERGED_FROM_{duplicate['identifier']}"
        carried += _dedupe_append(
            synonyms,
            {
                "synonym_text": duplicate["preferred_term"],
                "synonym_type": "RAW_TEXT",
                "source": source,
            },
            seen,
        )
        for synonym in duplicate.get("synonyms") or []:
            text = str(synonym.get("synonym_text") or "").strip()
            if text.casefold() in REJECTED_SYNONYMS:
                rejected += _dedupe_append(
                    synonyms,
                    {
                        "synonym_text": text,
                        "synonym_type": "REJECTED_LABEL",
                        "source": str(synonym.get("source") or source),
                    },
                    seen,
                )
            elif is_resolving_synonym(synonym):
                carried += _dedupe_append(
                    synonyms,
                    {
                        "synonym_text": text,
                        "synonym_type": "RAW_TEXT",
                        "source": source,
                    },
                    seen,
                )

    for text in EXTRA_SOURCE_LABELS:
        carried += _dedupe_append(
            synonyms,
            {
                "synonym_text": text,
                "synonym_type": "RAW_TEXT",
                "source": "mappings/culturemech_residual_triage.tsv",
            },
            seen,
        )

    return carried, rejected


def _reject_wrong_synonyms(record: dict) -> int:
    rejected = 0
    for synonym in record.get("synonyms") or []:
        text = str(synonym.get("synonym_text") or "").strip()
        if text.casefold() in REJECTED_SYNONYMS:
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected += 1
    return rejected


def _retarget_record(record: dict) -> None:
    record["identifier"] = SURVIVOR_ID
    record["ontology_mapping"] = {
        "ontology_id": SURVIVOR_ID,
        "ontology_label": SURVIVOR_LABEL,
        "ontology_source": "CHEBI",
        "mapping_quality": "EXACT_MATCH",
        "evidence": [
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": f"MIM curation ({ISSUE})",
                "notes": (
                    "A culture-media ingredient named sulfur, sulphur, or "
                    "sulfur powder denotes weighable elemental sulfur, not "
                    "ChEBI's sulfur atom or polysulfur terms."
                ),
            }
        ],
    }
    if record.get("kg_microbe_node_id") in OLD_IDENTIFIERS:
        record["kg_microbe_node_id"] = SURVIVOR_ID
    if record.get("chemical_properties"):
        record["chemical_properties"] = {}


def _zero_occurrences(record: dict) -> None:
    record["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}


def _merge_records(records: list[dict], stamp: str) -> tuple[int, int]:
    target = _find_record(records, SURVIVOR_OLD_ID, SURVIVOR_TERM)
    duplicates = tuple(
        _find_record(records, spec.identifier, spec.preferred_term) for spec in DUPLICATES
    )

    _retarget_record(target)
    carried, rejected = _merge_synonyms(target, duplicates)

    target["occurrence_statistics"] = {
        "total_occurrences": 477,
        "media_count": 477,
    }
    target.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "CORRECTED",
            "changes": (
                "identifier CHEBI:26833 -> CHEBI:33403 (elemental sulfur); "
                "absorbed duplicate Sulphur and Sulfur (powder) records; "
                f"merged CultureMech membership from 3 identifiers into {SURVIVOR_ID}; "
                f"added {carried} resolving source label(s) and retained "
                f"{rejected} atom/polysulfur-only label(s) as REJECTED_LABEL "
                f"({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )

    for duplicate in duplicates:
        old_id = duplicate["identifier"]
        _retarget_record(duplicate)
        _reject_wrong_synonyms(duplicate)
        duplicate["mapping_status"] = "REJECTED"
        duplicate["representative"] = SURVIVOR_ID
        _zero_occurrences(duplicate)
        duplicate.setdefault("curation_history", []).append(
            {
                "timestamp": stamp,
                "curator": CURATOR,
                "action": "MERGED_INTO",
                "changes": (
                    f"Merged into {SURVIVOR_ID} {SURVIVOR_TERM!r}; "
                    "occurrences transferred to the surviving elemental "
                    "sulfur record and SSSOM rows dropped. The old record "
                    f"{old_id} split a spelling or supplied powder form from "
                    f"the same weighable sulfur substance ({ISSUE})."
                ),
                "previous_status": "MAPPED",
                "new_status": "REJECTED",
                "llm_assisted": False,
            }
        )

    return carried, rejected


def _fix_yeast_extract_component(records: list[dict], stamp: str) -> bool:
    record = _find_record(
        records,
        "kgmicrobe.ingredient:yeast_extract_sulfur",
        "Yeast Extract + Sulfur",
    )
    for component in record.get("components") or []:
        if (
            component.get("component_name") == "sulfur"
            and component.get("component_id") == "CHEBI:26833"
        ):
            component["component_id"] = SURVIVOR_ID
            record.setdefault("curation_history", []).append(
                {
                    "timestamp": stamp,
                    "curator": CURATOR,
                    "action": "CORRECTED",
                    "changes": (
                        "Retargeted sulfur component CHEBI:26833 -> CHEBI:33403 "
                        "after the standalone Sulfur record moved from the atom "
                        f"term to elemental sulfur ({ISSUE})."
                    ),
                    "llm_assisted": False,
                }
            )
            return True
    return False


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


def rewrite_sssom(record: dict, stamp: str) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    dropped = 0
    rewrote = 0
    other = _sssom_other(record, SURVIVOR_LABEL)

    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    out.write(f"{header}\n")
    for line in body[1:]:
        reader = csv.DictReader(io.StringIO(f"{header}\n{line}"), delimiter="\t")
        row = next(reader)
        if row.get("subject_id") in DROP_SUBJECTS:
            dropped += 1
            continue
        if row.get("subject_id") == "MIM:Sulfur":
            if row.get("object_id") != SURVIVOR_OLD_ID:
                raise SystemExit(
                    f"MIM:Sulfur points at {row.get('object_id')}, expected {SURVIVOR_OLD_ID}"
                )
            row["object_id"] = SURVIVOR_ID
            row["object_label"] = SURVIVOR_LABEL
            row["object_source"] = object_source_for(SURVIVOR_ID)
            row["predicate_id"] = "skos:exactMatch"
            row["mapping_justification"] = JUSTIFICATION["EXACT_MATCH"]
            row["source"] = _append_source(row.get("source") or "")
            row["mapping_date"] = stamp[:10]
            row["confidence"] = CONFIDENCE["EXACT_MATCH"]
            row["comment"] = (
                "Corrected from sulfur atom to weighable elemental sulfur "
                f"and merged spelling/form duplicates ({ISSUE})."
            )
            row["other"] = other
            row["validation_method"] = ""
            writer.writerow(row)
            rewrote += 1
            continue
        out.write(line)
        if not line.endswith("\n"):
            out.write("\n")

    if dropped != DROP_SSSOM_ROWS:
        raise SystemExit(f"dropped {dropped} duplicate SSSOM row(s), expected {DROP_SSSOM_ROWS}")
    if rewrote != 1:
        raise SystemExit(f"rewrote {rewrote} Sulfur SSSOM rows, expected 1")
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
        if identifier in OLD_IDENTIFIERS:
            identifier = SURVIVOR_ID
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
    args = parser.parse_args(argv)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    mapped = _read_collection(MAPPED)
    records = mapped.get("ingredients", [])

    carried, rejected = _merge_records(records, stamp)
    component_fixed = _fix_yeast_extract_component(records, stamp)
    sulfur = _find_record(records, SURVIVOR_ID, SURVIVOR_TERM)
    sssom_text, sssom_rewrote, sssom_dropped = rewrite_sssom(sulfur, stamp)
    membership_text, membership_moved = rewrite_membership()

    mapped["generation_date"] = stamp
    mapped["total_count"] = len(records)
    mapped["mapped_count"] = sum(
        1 for record in records if record.get("mapping_status") == "MAPPED"
    )

    print(f"{'APPLIED' if args.apply else 'DRY RUN'}")
    print(f"  carried sulfur synonyms: {carried}")
    print(f"  rejected atom/polysulfur synonyms: {rejected}")
    print(f"  component fixed: {component_fixed}")
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
