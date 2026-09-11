#!/usr/bin/env python3
"""Move salt and ion-pair records off cation/anion primary identifiers (#315).

The affected records name a full salt or ion pair but still use the bare ion as
their primary identifier:

* ``1-ethyl-3-methylimidazolium lysine`` -> EMIM cation
* ``Na-crotonate`` -> crotonate anion
* ``Na2 alpha-ketoglutarate`` -> 2-oxoglutarate dianion
* ``Tetramethyl ammonium`` -> tetramethylammonium cation

No exact local ChEBI term denotes these complete substances. Per
MAPPING_SEMANTICS.md Section 3, each record takes a distinct
``kgmicrobe.compound`` identifier and retains only its nearest whole-substance
ChEBI parent as a ``NARROW_MATCH``.

Dry-run by default; pass ``--apply`` to write.
"""

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

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

CURATOR = "fix_salt_ion_identity_overclaims"
ISSUE = "#315"
MAX_OTHER_ENTRIES = 50


@dataclass(frozen=True)
class Regrounding:
    subject_id: str
    preferred_term: str
    old_identifier: str
    new_identifier: str
    parent_id: str
    parent_label: str
    rationale: str
    stale_chemistry: str
    wrong_synonyms: frozenset[str] = frozenset()
    wrong_synonym_sources: frozenset[str] = frozenset()


@dataclass(frozen=True)
class RejectedSynonym:
    subject_id: str
    preferred_term: str
    synonym_text: str
    source: str


REGROUNDINGS = (
    Regrounding(
        subject_id="MIM:1-ethyl-3-methylimidazolium_Lysine",
        preferred_term="1-ethyl-3-methylimidazolium lysine",
        old_identifier="CHEBI:61326",
        new_identifier="kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine",
        parent_id="CHEBI:63895",
        parent_label="ionic liquid",
        rationale=(
            "The label names a complete EMIM/lysinate ion pair, while CHEBI:61326 "
            "denotes only the 1-ethyl-3-methylimidazolium cation; CHEBI:63895 "
            "is the nearest verified ChEBI whole-substance parent."
        ),
        stale_chemistry="the EMIM cation only",
        wrong_synonym_sources=frozenset({"chebi_synonym_review"}),
    ),
    Regrounding(
        subject_id="MIM:Na-crotonate",
        preferred_term="Na-crotonate",
        old_identifier="CHEBI:35899",
        new_identifier="kgmicrobe.compound:na-crotonate",
        parent_id="CHEBI:41131",
        parent_label="crotonic acid",
        rationale=(
            "The label names sodium crotonate, not the crotonate anion in "
            "CHEBI:35899; CHEBI:41131 is the ChEBI acid parent."
        ),
        stale_chemistry="the crotonate anion only",
        wrong_synonym_sources=frozenset({"kg_microbe"}),
    ),
    Regrounding(
        subject_id="MIM:Na2_Alpha-ketoglutarate",
        preferred_term="Na2 alpha-ketoglutarate",
        old_identifier="CHEBI:16810",
        new_identifier="kgmicrobe.compound:na2_alpha-ketoglutarate",
        parent_id="CHEBI:30915",
        parent_label="2-oxoglutaric acid",
        rationale=(
            "The label names a disodium salt, not the 2-oxoglutarate dianion "
            "in CHEBI:16810; CHEBI:30915 is the ChEBI acid parent."
        ),
        stale_chemistry="the 2-oxoglutarate dianion only",
        wrong_synonyms=frozenset(
            {
                "2-oxoglutarate",
                "2-oxopentanedioate",
                "alpha-ketoglutarate",
                "\u03b1-ketoglutarate",
            }
        ),
    ),
    Regrounding(
        subject_id="MIM:Tetramethyl_Ammonium",
        preferred_term="Tetramethyl ammonium",
        old_identifier="CHEBI:46020",
        new_identifier="kgmicrobe.compound:tetramethyl_ammonium",
        parent_id="CHEBI:35273",
        parent_label="quaternary ammonium salt",
        rationale=(
            "The culture-media surface form names tetramethyl ammonium as a "
            "supplied ingredient; CHEBI:46020 denotes only the cation, which "
            "cannot be supplied as a standalone neutral compound. CHEBI:35273 "
            "is the nearest verified whole-substance salt parent."
        ),
        stale_chemistry="the tetramethylammonium cation only",
        wrong_synonym_sources=frozenset({"kg_microbe"}),
    ),
)

ADJACENT_REJECTIONS = (
    RejectedSynonym(
        subject_id="MIM:1-ethyl-3-methylimidazolium_Acetate",
        preferred_term="1-ethyl-3-methylimidazolium acetate",
        synonym_text="1-ethyl-3-methyl-1H-imidazol-3-ium",
        source="chebi_synonym_review",
    ),
    RejectedSynonym(
        subject_id="MIM:1-ethyl-3-methylimidazolium_Acetate",
        preferred_term="1-ethyl-3-methylimidazolium acetate",
        synonym_text="1-ethyl-3-methylimidazolium lysine",
        source="mappings/ingredient_mappings.sssom.tsv",
    ),
    RejectedSynonym(
        subject_id="MIM:Tetramethyl_Ammonium_Chloride",
        preferred_term="Tetramethyl ammonium chloride",
        synonym_text="N,N,N-trimethylmethanaminium",
        source="chebi_synonym_review",
    ),
)

SSSOM_OTHER_REJECTIONS = {
    subject_id: frozenset(
        rejection.synonym_text.casefold()
        for rejection in ADJACENT_REJECTIONS
        if rejection.subject_id == subject_id
    )
    for subject_id in {rejection.subject_id for rejection in ADJACENT_REJECTIONS}
}

SODIUM_CROTONATE_MERGE = {
    "identifier": "UNMAPPED_0524",
    "preferred_term": "Sodium crotonate",
    "target": "Na-crotonate",
}

# The checked-in edge list was built from CultureMech data before source labels
# were retained, so the salt/anion split needs exact label-aware deltas here.
# Future supported rebuilds route these labels in culturemech_occurrences.py.
SODIUM_CROTONATE_MEMBERSHIP_ADDITIONS = (
    ("kgmicrobe.compound:na-crotonate", "CultureMech:002451", "1"),
    ("kgmicrobe.compound:na-crotonate", "CultureMech:014344", "1"),
)

NON_SALT_SOURCE_MEMBERSHIP_REMOVALS = (
    ("kgmicrobe.compound:na2_alpha-ketoglutarate", "CultureMech:002279"),
    ("kgmicrobe.compound:na2_alpha-ketoglutarate", "CultureMech:007698"),
    ("kgmicrobe.compound:na2_alpha-ketoglutarate", "CultureMech:014091"),
)

OCCURRENCE_STAT_REPAIRS = {
    "kgmicrobe.compound:na-crotonate": (9, 9),
    "kgmicrobe.compound:na2_alpha-ketoglutarate": (4, 4),
}

SOURCE_ID_RE = re.compile(r"source_id=([A-Za-z0-9_.:-]+)")


def _read_collection(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _append_source(source: str, curator: str) -> str:
    pieces = [piece for piece in source.split("|") if piece]
    tag = f"MIM:curator={curator}"
    if tag not in pieces:
        pieces.append(tag)
    return "|".join(pieces)


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
            f"{preferred_term!r} on {identifier} matched {len(hits)} mapped "
            "record(s), expected exactly 1"
        )
    return hits[0]


def _supersede_evidence(ontology_mapping: dict) -> None:
    for evidence in ontology_mapping.get("evidence") or []:
        note = str(evidence.get("notes") or "")
        if not note.startswith("SUPERSEDED"):
            evidence["notes"] = (
                f"SUPERSEDED ({ISSUE}): describes the bare ion identity, not the "
                f"complete salt or ion pair. Original note follows. {note}"
            )


def _reject_wrong_synonyms(record: dict, spec: Regrounding) -> int:
    rejected = 0
    wrong_text = {text.casefold() for text in spec.wrong_synonyms}
    for synonym in record.get("synonyms") or []:
        text = str(synonym.get("synonym_text") or "")
        source = str(synonym.get("source") or "")
        text_key = text.casefold()
        is_wrong = text_key in wrong_text or source in spec.wrong_synonym_sources
        if is_wrong:
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected += 1
    return rejected


def _find_by_preferred(records: list[dict], preferred_term: str) -> dict:
    hits = [
        record for record in records if record.get("preferred_term") == preferred_term
    ]
    if len(hits) != 1:
        raise SystemExit(f"{preferred_term!r} matched {len(hits)} record(s), expected 1")
    return hits[0]


def _reject_adjacent_wrong_synonyms(mapped: dict, stamp: str) -> int:
    rejected = 0
    records = mapped.get("ingredients", [])
    touched: dict[str, list[str]] = {}
    for rejection in ADJACENT_REJECTIONS:
        record = _find_by_preferred(records, rejection.preferred_term)
        synonyms = record.setdefault("synonyms", [])
        for synonym in synonyms:
            if (
                str(synonym.get("synonym_text") or "").casefold()
                == rejection.synonym_text.casefold()
            ):
                if synonym.get("synonym_type") != "REJECTED_LABEL":
                    synonym["synonym_type"] = "REJECTED_LABEL"
                    rejected += 1
                    touched.setdefault(rejection.preferred_term, []).append(
                        rejection.synonym_text
                    )
                break
        else:
            synonyms.append(
                {
                    "synonym_text": rejection.synonym_text,
                    "synonym_type": "REJECTED_LABEL",
                    "source": rejection.source,
                }
            )
            rejected += 1
            touched.setdefault(rejection.preferred_term, []).append(
                rejection.synonym_text
            )

    for preferred_term, labels in touched.items():
        record = _find_by_preferred(records, preferred_term)
        rendered = ", ".join(repr(label) for label in labels)
        record.setdefault("curation_history", []).append(
            {
                "timestamp": stamp,
                "curator": CURATOR,
                "action": "REJECTED_ION_SYNONYMS",
                "changes": (
                    f"Marked cation/other-salt synonym(s) as REJECTED_LABEL so "
                    f"they cannot leak through SSSOM `other`: {rendered} ({ISSUE})."
                ),
                "llm_assisted": False,
            }
        )
    return rejected


def _reground_record(record: dict, spec: Regrounding, stamp: str) -> int:
    dropped_chemistry = record.get("chemical_properties") or {}
    rejected_synonyms = _reject_wrong_synonyms(record, spec)

    old_ontology = dict(record.get("ontology_mapping") or {})
    ontology_mapping = record.setdefault("ontology_mapping", {})
    _supersede_evidence(ontology_mapping)
    ontology_mapping.update(
        {
            "ontology_id": spec.parent_id,
            "ontology_label": spec.parent_label,
            "ontology_source": "CHEBI",
            "mapping_quality": "NARROW_MATCH",
        }
    )
    ontology_mapping.setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"{spec.rationale} No exact local ChEBI term for "
                f"{spec.preferred_term!r} was found, so MAPPING_SEMANTICS.md "
                "Section 3 uses a kgmicrobe.compound identity with the nearest "
                "whole-substance ChEBI parent."
            ),
        }
    )

    old_identifier = str(record.get("identifier"))
    record["identifier"] = spec.new_identifier
    if record.get("kg_microbe_node_id") in {
        spec.old_identifier,
        old_ontology.get("ontology_id"),
        spec.parent_id,
    }:
        record["kg_microbe_node_id"] = spec.new_identifier
    if dropped_chemistry:
        record["chemical_properties"] = {}

    record.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "REGROUNDED_ION_OVERCLAIM",
            "changes": (
                f"identifier {old_identifier} -> {spec.new_identifier}; "
                f"mapping_quality -> NARROW_MATCH to {spec.parent_id} "
                f"({spec.parent_label!r}). Cleared chemical_properties because "
                f"they described {spec.stale_chemistry}, marked "
                f"{rejected_synonyms} bare-ion synonym(s) as REJECTED_LABEL, "
                f"and kept the complete salt or ion-pair identity distinct "
                f"({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return rejected_synonyms


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
        out.append(token)
        seen.add(key)
        if len(out) >= MAX_OTHER_ENTRIES:
            break
    return "|".join(out)


def _sync_sssom_row(
    row: dict[str, str],
    spec: Regrounding,
    stamp: str,
    other: str,
) -> dict[str, str]:
    synced = dict(row)
    synced["object_id"] = spec.parent_id
    synced["object_label"] = spec.parent_label
    synced["object_source"] = object_source_for(spec.parent_id)
    synced["predicate_id"] = PREDICATE["NARROW_MATCH"]
    synced["mapping_justification"] = JUSTIFICATION["NARROW_MATCH"]
    synced["source"] = _append_source(row.get("source", ""), CURATOR)
    synced["mapping_date"] = stamp[:10]
    synced["confidence"] = CONFIDENCE["NARROW_MATCH"]
    synced["comment"] = (
        f"Local kgmicrobe.compound identity retained because no exact ontology "
        f"term for {spec.preferred_term} was verified; {spec.parent_id} is the "
        f"nearest ChEBI parent ({ISSUE})."
    )
    synced["other"] = other
    synced["validation_method"] = ""
    return synced


def _registry_row(
    row: dict[str, str],
    spec: Regrounding,
    stamp: str,
    other: str,
) -> dict[str, str]:
    registry = dict.fromkeys(row, "")
    registry.update(row)
    registry["predicate_id"] = PREDICATE["EXACT_MATCH"]
    registry["object_id"] = spec.new_identifier
    registry["object_label"] = spec.preferred_term
    registry["object_source"] = object_source_for(spec.new_identifier)
    registry["mapping_justification"] = JUSTIFICATION_MANUAL
    registry["source"] = _append_source(row.get("source", ""), CURATOR)
    registry["mapping_date"] = stamp[:10]
    registry["confidence"] = CONFIDENCE["EXACT_MATCH"]
    registry["comment"] = (
        f"Registry/identity row preserving {spec.new_identifier} alongside "
        f"whole-substance parent {spec.parent_id}."
    )
    registry["other"] = other
    registry["validation_method"] = ""
    return registry


def _scrub_rejected_other(row: dict[str, str]) -> bool:
    rejected_tokens = SSSOM_OTHER_REJECTIONS.get(row.get("subject_id") or "")
    if not rejected_tokens:
        return False
    other = row.get("other") or ""
    kept = [
        token
        for token in other.split("|")
        if token.strip().casefold() not in rejected_tokens
    ]
    row["other"] = "|".join(kept)
    return row["other"] != other


def rewrite_sssom(
    regroundings: tuple[Regrounding, ...],
    records: list[dict],
    stamp: str,
) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    by_subject = {spec.subject_id: spec for spec in regroundings}
    other_by_subject = {
        spec.subject_id: _sssom_other(
            _find_record(records, spec.new_identifier, spec.preferred_term),
            object_label=spec.parent_label,
        )
        for spec in regroundings
    }

    replaced = 0
    scrubbed = 0
    out = io.StringIO()
    writer = csv.DictWriter(
        out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
    )
    out.write(f"{header}\n")
    for line in body[1:]:
        reader = csv.DictReader(io.StringIO(f"{header}\n{line}"), delimiter="\t")
        row = next(reader)
        spec = by_subject.get(row.get("subject_id") or "")
        if spec is None:
            if _scrub_rejected_other(row):
                writer.writerow(row)
                scrubbed += 1
                continue
            out.write(line)
            if not line.endswith("\n"):
                out.write("\n")
            continue
        if row.get("object_id") != spec.old_identifier:
            raise SystemExit(
                f"{spec.subject_id} points at {row.get('object_id')}, expected "
                f"{spec.old_identifier}"
            )
        other = other_by_subject[spec.subject_id]
        writer.writerow(_sync_sssom_row(row, spec, stamp, other))
        writer.writerow(_registry_row(row, spec, stamp, other))
        replaced += 1

    if replaced != len(regroundings):
        raise SystemExit(
            f"rewrote {replaced} SSSOM rows, expected {len(regroundings)}"
        )

    return "".join(preamble) + out.getvalue(), replaced, scrubbed


def rewrite_membership(
    regroundings: tuple[Regrounding, ...],
) -> tuple[str, int, int, int]:
    remap = {spec.old_identifier: spec.new_identifier for spec in regroundings}
    text = MEMBERSHIP.read_text(encoding="utf-8")
    comments = []
    rows = []
    moved = 0
    for line in text.splitlines():
        if line.startswith("#"):
            comments.append(line)
            continue
        fields = line.split("\t")
        if fields and fields[0] in remap:
            fields[0] = remap[fields[0]]
            moved += 1
        rows.append(fields)

    header, data = rows[0], rows[1:]
    remove_keys = {
        (identifier, recipe_id)
        for identifier, recipe_id in NON_SALT_SOURCE_MEMBERSHIP_REMOVALS
    }
    original_len = len(data)
    data = [fields for fields in data if tuple(fields[:2]) not in remove_keys]
    removed = original_len - len(data)

    existing_keys = {(fields[0], fields[1]) for fields in data}
    added = 0
    for identifier, recipe_id, occurrences in SODIUM_CROTONATE_MEMBERSHIP_ADDITIONS:
        key = (identifier, recipe_id)
        if key in existing_keys:
            continue
        data.append([identifier, recipe_id, occurrences])
        existing_keys.add(key)
        added += 1

    data.sort(key=lambda fields: tuple(fields[:2]))
    if comments:
        comments[0] = re.sub(r"\bedges=\d+\b", f"edges={len(data)}", comments[0])
    out = [*(f"{line}\n" for line in comments), "\t".join(header) + "\n"]
    out.extend("\t".join(fields) + "\n" for fields in data)
    return "".join(out), moved, added, removed


def repair_occurrence_statistics(mapped: dict, stamp: str) -> int:
    repaired = 0
    by_identifier = {
        record.get("identifier"): record
        for record in mapped.get("ingredients", [])
        if record.get("mapping_status") == "MAPPED"
    }
    for identifier, (media_count, total_occurrences) in OCCURRENCE_STAT_REPAIRS.items():
        record = by_identifier[identifier]
        stats = record.setdefault("occurrence_statistics", {})
        old = (stats.get("media_count"), stats.get("total_occurrences"))
        new = (media_count, total_occurrences)
        if old == new:
            continue
        stats["media_count"] = media_count
        stats["total_occurrences"] = total_occurrences
        record.setdefault("curation_history", []).append(
            {
                "timestamp": stamp,
                "curator": CURATOR,
                "action": "CORRECTED",
                "changes": (
                    f"occurrence_statistics {old[0]}/{old[1]} -> "
                    f"{media_count}/{total_occurrences} "
                    "(media_count/total_occurrences) to match label-aware "
                    "CultureMech membership routing after the salt/anion "
                    f"split ({ISSUE})."
                ),
                "llm_assisted": False,
            }
        )
        repaired += 1
    return repaired


def merge_sodium_crotonate(mapped: dict, unmapped: dict, stamp: str) -> bool:
    target = next(
        (
            record
            for record in mapped.get("ingredients", [])
            if record.get("preferred_term") == SODIUM_CROTONATE_MERGE["target"]
            and record.get("mapping_status") == "MAPPED"
        ),
        None,
    )
    if target is None:
        raise SystemExit("Na-crotonate target not found for Sodium crotonate merge")

    source = next(
        (
            record
            for record in unmapped.get("ingredients", [])
            if record.get("identifier") == SODIUM_CROTONATE_MERGE["identifier"]
            and record.get("preferred_term") == SODIUM_CROTONATE_MERGE["preferred_term"]
        ),
        None,
    )
    if source is None:
        return False
    if source.get("mapping_status") != "UNMAPPED":
        raise SystemExit("Sodium crotonate source is not UNMAPPED")

    synonyms = target.setdefault("synonyms", [])
    if not any(s.get("synonym_text") == "Sodium crotonate" for s in synonyms):
        synonyms.append(
            {
                "synonym_text": "Sodium crotonate",
                "synonym_type": "RAW_TEXT",
                "source": source["identifier"],
            }
        )
    source_texts = [str(source.get("notes") or "")]
    source_texts.extend(
        str(event.get("changes") or "") for event in source.get("curation_history") or []
    )
    source_ids = sorted(
        {
            source_id
            for text in source_texts
            for source_id in SOURCE_ID_RE.findall(text)
        }
    )
    source_provenance = ""
    if source_ids:
        source_id_text = (
            f"source_id={source_ids[0]}"
            if len(source_ids) == 1
            else f"source_ids={', '.join(source_ids)}"
        )
        source_provenance += (
            f" Deleted source had upstream {source_id_text}."
        )
    if any(
        event.get("curator") == "edison_literature_identity"
        for event in source.get("curation_history") or []
    ):
        source_provenance += (
            " Deleted source also carried Edison literature identity review: "
            "sodium crotonate was a defined sodium carboxylate/aqueous "
            "sodium-crotonate preparation with no ontology CURIE proposed."
        )
    target.setdefault("curation_history", []).append(
        {
            "timestamp": stamp,
            "curator": CURATOR,
            "action": "MERGED_FROM_UNMAPPED_DUPLICATE",
            "changes": (
                "Absorbed UNMAPPED_0524 'Sodium crotonate' as a RAW_TEXT "
                "synonym after Na-crotonate moved off the bare crotonate "
                f"anion and took its own sodium-salt identity (#315).{source_provenance}"
            ),
            "llm_assisted": False,
        }
    )
    unmapped["ingredients"].remove(source)
    unmapped["total_count"] = len(unmapped["ingredients"])
    unmapped["unmapped_count"] = sum(
        1
        for record in unmapped["ingredients"]
        if record.get("mapping_status") == "UNMAPPED"
    )
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    mapped = _read_collection(MAPPED)
    unmapped = _read_collection(UNMAPPED)
    active = {
        record.get("identifier")
        for record in mapped.get("ingredients", [])
        if record.get("mapping_status") != "REJECTED"
    }

    rejected_synonyms = {}
    for spec in REGROUNDINGS:
        if spec.new_identifier in active:
            raise SystemExit(f"{spec.new_identifier} is already held by an active record")
        record = _find_record(
            mapped.get("ingredients", []), spec.old_identifier, spec.preferred_term
        )
        rejected_synonyms[spec.preferred_term] = _reground_record(record, spec, stamp)

    adjacent_rejected = _reject_adjacent_wrong_synonyms(mapped, stamp)

    merged_sodium_crotonate = merge_sodium_crotonate(mapped, unmapped, stamp)
    occurrence_stats_repaired = repair_occurrence_statistics(mapped, stamp)
    sssom_text, sssom_replaced, sssom_scrubbed = rewrite_sssom(
        REGROUNDINGS,
        mapped.get("ingredients", []),
        stamp,
    )
    membership_text, membership_moved, membership_added, membership_removed = (
        rewrite_membership(REGROUNDINGS)
    )

    mapped["generation_date"] = stamp
    unmapped["generation_date"] = stamp
    mapped["total_count"] = len(mapped["ingredients"])
    mapped["mapped_count"] = sum(
        1
        for record in mapped["ingredients"]
        if record.get("mapping_status") == "MAPPED"
    )

    print(f"{'APPLIED' if args.apply else 'DRY RUN'}")
    for spec in REGROUNDINGS:
        print(
            f"  {spec.preferred_term}: {spec.old_identifier} -> "
            f"{spec.new_identifier}; parent {spec.parent_id}; "
            f"rejected synonyms={rejected_synonyms[spec.preferred_term]}"
        )
    print(f"  adjacent wrong synonyms rejected: {adjacent_rejected}")
    print(f"  SSSOM ion rows replaced: {sssom_replaced}")
    print(f"  SSSOM other rows scrubbed: {sssom_scrubbed}")
    print(f"  membership rows moved: {membership_moved}")
    print(f"  membership rows added: {membership_added}")
    print(f"  membership rows removed: {membership_removed}")
    print(f"  occurrence stats repaired: {occurrence_stats_repaired}")
    print(f"  Sodium crotonate merged: {merged_sodium_crotonate}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to write.")
        return 0

    save_yaml(mapped, MAPPED, backup=False, validate=True, target_class="IngredientCollection")
    save_yaml(unmapped, UNMAPPED, backup=False, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text, encoding="utf-8")
    MEMBERSHIP.write_text(membership_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
