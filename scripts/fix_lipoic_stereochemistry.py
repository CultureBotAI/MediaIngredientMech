#!/usr/bin/env python3
"""Merge generic lipoic/thioctic labels off unsupported R/S targets (#454)."""

from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import io
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

CURATOR = "fix_lipoic_stereochemistry"
ISSUE = "#454"
SOURCE_TOKEN = f"MIM:curator={CURATOR}"

SURVIVOR_TERM = "(DL)-alpha-Lipoic acid"
SURVIVOR_ID = "CHEBI:16494"
SURVIVOR_LABEL = "lipoic acid"
SURVIVOR_SUBJECT = "MIM:Dl-alpha-lipoic_Acid"

BAD_IDENTIFIERS = frozenset({"CHEBI:30314", "CHEBI:43796"})
DROP_SSSOM_SUBJECTS = frozenset({"MIM:Thioctic_Acid", "MIM:~391-lipoic_Acid"})
EXPECTED_DROPPED_SSSOM_ROWS = 2
EXPECTED_MOVED_MEMBERSHIP_ROWS = 47


@dataclass(frozen=True)
class DuplicateSpec:
    identifier: str
    preferred_term: str
    source_labels: tuple[str, ...]


DUPLICATES = (
    DuplicateSpec("CHEBI:30314", "Thioctic acid", ("Thioctic acid",)),
    DuplicateSpec(
        "CHEBI:43796",
        "α-lipoic acid",
        ("α-lipoic acid", "α--Lipoic acid", "D,L-6,8-Thioctic Acid"),
    ),
)


COMPONENT_RETARGETS = (
    "ATCC Wolfe's vitamin mix",
    "Wolfe's vitamin mix",
)


STEREOSPECIFIC_SOURCE_LABELS = frozenset({
    "(+)-alpha-Lipoic acid",
    "(R)-(+)-Lipoate",
    "(R)-(+)-lipoic acid",
    "(R)-1,2-Dithiolane-3-pentanoic acid",
    "(R)-1,2-dithiolane-3-valeric acid",
    "(R)-6,8-thioctic acid",
    "(S)-(-)-lipoic acid",
    "(S)-1,2-dithiolane-3-pentanoic acid",
    "(S)-alpha-lipoic acid",
    "5-[(3R)-1,2-dithiolan-3-yl]pentanoic acid",
    "5-[(3S)-1,2-dithiolan-3-yl]pentanoic acid",
    "L-1,2-dithiolane 3-valeric acid",
    "L-6,8-thioctic acid",
    "L-6-thioctic acid",
    "R-(+)-Lipoic acid",
    "R-LA",
    "RLA",
    "S-LA",
    "SLA",
    "Thioctic acid d-form",
    "thioctic acid l-form",
})
STEREOSPECIFIC_SOURCE_LABEL_KEYS = frozenset(
    text.casefold() for text in STEREOSPECIFIC_SOURCE_LABELS
)


def _read_collection(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _find_record(records: list[dict], identifier: str, preferred_term: str) -> dict:
    hits = [
        record
        for record in records
        if record.get("identifier") == identifier
        and record.get("preferred_term") == preferred_term
        and record.get("mapping_status") == "MAPPED"
    ]
    if len(hits) != 1:
        raise SystemExit(
            f"{preferred_term!r} on {identifier} matched {len(hits)} active record(s), "
            "expected exactly 1"
        )
    return hits[0]


def _append_source_synonyms(record: dict, specs: Iterable[DuplicateSpec]) -> int:
    synonyms = record.setdefault("synonyms", [])
    seen = {
        str(synonym.get("synonym_text") or "").strip().casefold()
        for synonym in synonyms
    }
    seen.add(str(record.get("preferred_term") or "").strip().casefold())

    added = 0
    for spec in specs:
        for text in spec.source_labels:
            key = text.casefold()
            if key in seen:
                continue
            synonyms.append(
                {
                    "synonym_text": text,
                    "synonym_type": "RAW_TEXT",
                    "source": f"MERGED_FROM_{spec.identifier}",
                }
            )
            seen.add(key)
            added += 1
    return added


def _merge_roles(survivor: dict, duplicates: Iterable[dict]) -> int:
    added = 0
    for field in FACET_ROLE_SLOTS:
        target = survivor.setdefault(field, [])
        present_roles = {
            item.get("role")
            for item in target
            if isinstance(item, dict) and item.get("role")
        }
        for duplicate in duplicates:
            for item in duplicate.get(field) or []:
                role = item.get("role") if isinstance(item, dict) else None
                if role and role in present_roles:
                    continue
                if item in target:
                    continue
                target.append(copy.deepcopy(item))
                if role:
                    present_roles.add(role)
                added += 1
    return added


def _merge_occurrence_statistics(survivor: dict, duplicates: Iterable[dict]) -> tuple[int, int]:
    target = survivor.setdefault("occurrence_statistics", {})
    total = 0
    media = 0
    by_source = {
        entry.get("source"): dict(entry)
        for entry in target.get("source_occurrences") or []
        if entry.get("source")
    }

    for duplicate in duplicates:
        stats = duplicate.get("occurrence_statistics") or {}
        total += stats.get("total_occurrences") or 0
        media += stats.get("media_count") or 0
        for entry in stats.get("source_occurrences") or []:
            source = entry.get("source")
            if not source:
                continue
            existing = by_source.get(source)
            if existing is None:
                by_source[source] = dict(entry)
            else:
                existing["count"] = (existing.get("count") or 0) + (entry.get("count") or 0)

    target["total_occurrences"] = (target.get("total_occurrences") or 0) + total
    target["media_count"] = (target.get("media_count") or 0) + media
    if by_source:
        target["source_occurrences"] = [by_source[source] for source in sorted(by_source)]
    return total, media


def _retarget_to_survivor(record: dict) -> None:
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
                    "The source label names generic or racemic lipoic/thioctic "
                    "acid. No source occurrence asserts an R- or S-only "
                    "enantiomer, so CHEBI:16494 is the supported ChEBI target."
                ),
            }
        ],
    }
    if record.get("kg_microbe_node_id") in BAD_IDENTIFIERS:
        record["kg_microbe_node_id"] = SURVIVOR_ID
    record["chemical_properties"] = {}


def _reject_stereospecific_synonyms(record: dict) -> int:
    rejected = 0
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict):
            continue
        text = str(synonym.get("synonym_text") or "").strip()
        if text.casefold() not in STEREOSPECIFIC_SOURCE_LABEL_KEYS:
            continue
        synonym["synonym_type"] = "REJECTED_LABEL"
        rejected += 1
    return rejected


def _tombstone(record: dict, old_identifier: str, stamp: str) -> int:
    _retarget_to_survivor(record)
    rejected_synonyms = _reject_stereospecific_synonyms(record)
    record["mapping_status"] = "REJECTED"
    record["representative"] = SURVIVOR_ID
    record["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}
    record.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_INTO",
            "changes": (
                f"Merged into {SURVIVOR_ID} {SURVIVOR_TERM!r}; the old "
                f"{old_identifier} target was an unsupported enantiomer-specific "
                "grounding. Occurrences were transferred to the generic lipoic "
                f"acid record and SSSOM rows were dropped ({ISSUE}), and "
                f"{rejected_synonyms} R/S-only target synonym(s) were retained as "
                f"REJECTED_LABEL provenance ({ISSUE}/#634)."
            ),
            "previous_status": "MAPPED",
            "new_status": "REJECTED",
            "llm_assisted": False,
        }
    )
    return rejected_synonyms


def _fix_components(records: list[dict], stamp: str) -> int:
    fixed = 0
    by_term = {record.get("preferred_term"): record for record in records}
    for term in COMPONENT_RETARGETS:
        record = by_term.get(term)
        if record is None:
            raise SystemExit(f"missing component record {term!r}")
        changed = 0
        for component in record.get("components") or []:
            if (
                component.get("component_name") == "Thioctic acid"
                and component.get("component_id") == "CHEBI:30314"
            ):
                component["component_id"] = SURVIVOR_ID
                changed += 1
        if changed != 1:
            raise SystemExit(
                f"expected one CHEBI:30314 Thioctic acid component in {term!r}; "
                f"found {changed}"
            )
        record.setdefault("curation_history", []).append(
            {
                "timestamp": stamp,
                "curator": CURATOR,
                "action": "CORRECTED",
                "changes": (
                    "Retargeted Thioctic acid component CHEBI:30314 -> "
                    "CHEBI:16494 after the source label moved from the "
                    f"R-enantiomer to generic lipoic acid ({ISSUE})."
                ),
                "llm_assisted": False,
            }
        )
        fixed += changed
    return fixed


def _append_source(source: str) -> str:
    pieces = [piece for piece in source.split("|") if piece]
    if SOURCE_TOKEN not in pieces:
        pieces.append(SOURCE_TOKEN)
    return "|".join(pieces)


def _sssom_other(record: dict) -> str:
    drop = {SURVIVOR_TERM.casefold(), SURVIVOR_LABEL.casefold(), ""}
    seen: set[str] = set()
    out: list[str] = []
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict) or not is_resolving_synonym(synonym):
            continue
        text = str(synonym.get("synonym_text") or "").strip()
        key = text.casefold()
        if key in drop or key in seen:
            continue
        seen.add(key)
        out.append(text)
    cas = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
    cas_token = f"CAS:{cas}" if cas else ""
    cas_key = cas_token.casefold()
    if cas_token and cas_key not in drop and cas_key not in seen:
        out.append(cas_token)
    return "|".join(out)


def rewrite_sssom(survivor: dict, stamp: str) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    fieldnames = body[0].rstrip("\n").split("\t")
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()

    rewrote = 0
    dropped = 0
    for row in csv.DictReader(body[1:], fieldnames=fieldnames, delimiter="\t"):
        if row["subject_id"] in DROP_SSSOM_SUBJECTS:
            dropped += 1
            continue
        if row["subject_id"] == SURVIVOR_SUBJECT:
            if row["object_id"] != SURVIVOR_ID:
                raise SystemExit(
                    f"{SURVIVOR_SUBJECT} points at {row['object_id']}, "
                    f"expected {SURVIVOR_ID}"
                )
            row["source"] = _append_source(row.get("source") or "")
            row["mapping_date"] = stamp[:10]
            row["comment"] = (
                "Merged generic/racemic lipoic aliases that had been grounded "
                f"to unsupported R/S targets ({ISSUE})."
            )
            row["other"] = _sssom_other(survivor)
            rewrote += 1
        writer.writerow(row)

    if rewrote != 1:
        raise SystemExit(f"rewrote {rewrote} survivor SSSOM row(s), expected 1")
    if dropped != EXPECTED_DROPPED_SSSOM_ROWS:
        raise SystemExit(
            f"dropped {dropped} duplicate SSSOM row(s), "
            f"expected {EXPECTED_DROPPED_SSSOM_ROWS}"
        )
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
        if identifier in BAD_IDENTIFIERS:
            identifier = SURVIVOR_ID
            moved += 1
        key = (identifier, recipe_id)
        edges[key] = edges.get(key, 0) + int(occurrences)

    if header is None:
        raise SystemExit("membership header not found")
    if moved != EXPECTED_MOVED_MEMBERSHIP_ROWS:
        raise SystemExit(
            f"moved {moved} lipoic membership row(s), "
            f"expected {EXPECTED_MOVED_MEMBERSHIP_ROWS}"
        )
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
    collection = _read_collection(MAPPED)
    records = collection.get("ingredients") or []
    survivor = _find_record(records, SURVIVOR_ID, SURVIVOR_TERM)
    duplicates = tuple(
        _find_record(records, spec.identifier, spec.preferred_term)
        for spec in DUPLICATES
    )

    added_synonyms = _append_source_synonyms(survivor, DUPLICATES)
    moved_total, moved_media = _merge_occurrence_statistics(survivor, duplicates)
    added_roles = _merge_roles(survivor, duplicates)
    fixed_components = _fix_components(records, stamp)

    survivor.setdefault("ontology_mapping", {}).setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                "The Thioctic acid, alpha-lipoic acid, and D,L-6,8-Thioctic "
                "Acid source labels name generic or racemic lipoic/thioctic "
                "acid rather than R- or S-only lipoic acid."
            ),
        }
    )
    survivor.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_FROM_MAPPED_RECORD",
            "changes": (
                "Absorbed generic/racemic Thioctic acid and alpha-lipoic acid "
                f"records from CHEBI:30314/CHEBI:43796; carried {added_synonyms} "
                "observed source label(s), kept R/S-only target synonyms as "
                "REJECTED_LABEL provenance on the tombstones, moved "
                f"{moved_total}/{moved_media} occurrences, and retargeted "
                f"{fixed_components} component reference(s) ({ISSUE}/#634)."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )

    rejected_synonyms = sum(
        _tombstone(duplicate, duplicate["identifier"], stamp)
        for duplicate in duplicates
    )

    collection["generation_date"] = stamp
    collection["total_count"] = len(records)
    collection["mapped_count"] = sum(
        1 for record in records if record.get("mapping_status") == "MAPPED"
    )

    sssom_text, rewrote, dropped = rewrite_sssom(survivor, stamp)
    membership_text, moved_edges = rewrite_membership()

    print(f"{'APPLIED' if args.apply else 'DRY RUN'}")
    print(f"  source labels carried: {added_synonyms}")
    print(f"  occurrence counts moved: {moved_total}/{moved_media}")
    print(f"  role facets added: {added_roles}")
    print(f"  component references fixed: {fixed_components}")
    print(f"  R/S labels rejected: {rejected_synonyms}")
    print(f"  SSSOM rows rewritten: {rewrote}")
    print(f"  SSSOM rows dropped: {dropped}")
    print(f"  membership rows moved: {moved_edges}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to write.")
        return 0

    save_yaml(
        collection,
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
