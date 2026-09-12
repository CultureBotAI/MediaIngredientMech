#!/usr/bin/env python3
"""Reject hidden hydrate synonyms on anhydrous or sibling-hydrate records (#251).

The hydrate report originally found only preferred terms with hydrate notation.
That missed hydrate labels that were folded into the wrong record as synonyms:
anhydrous records answered to hydrate labels, and some specific hydrate records
answered to sibling hydration states. Keep the historical labels on the record
as provenance, but mark the false labels ``REJECTED_LABEL`` so the SSSOM
``other`` channel and the flat label exports cannot resolve through them.

Dry-run by default; pass ``--apply`` to write.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curation.hydrate_guard import (  # noqa: E402
    HYDRATE_NOTATION,
    implausible_water_counts,
    water_multiplicity,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

STAMP = "2026-09-12T00:00:00+00:00"
CURATOR = "reject_hidden_hydrate_synonym_collapses"
ANHYDROUS_KIND = "anhydrous_term"
HYDRATE_KIND = "specific_hydrate"
INVALID_WATER_STATE = "INVALID"
VARIABLE_WATER_STATE = "VARIABLE"

ONE_WATER_NOTATION = re.compile(r"[xX×·•・⋅∙.]\s*H2\s*O(?![0-9])")
VARIABLE_WATER_NOTATION = re.compile(r"[xX×·•・⋅∙.]\s*n\s*H2\s*O(?![0-9])")

TargetKey = tuple[str, str]

ANHYDROUS_TARGETS: frozenset[TargetKey] = frozenset(
    {
        ("CHEBI:22653", "Asparagine"),
        ("CHEBI:3312", "CaCl2"),
        ("CHEBI:30769", "Citric acid"),
        ("CHEBI:35696", "CoCl2"),
        ("CHEBI:53470", "CoSO4"),
        ("CHEBI:49553", "CuCl2"),
        ("CHEBI:23414", "CuSO4"),
        ("CHEBI:91249", "Diammonium molybdate"),
        ("CHEBI:131527", "K2HPO4"),
        ("CHEBI:17716", "Lactose"),
        ("CHEBI:32599", "Magnesium sulfate"),
        ("CHEBI:17306", "Maltose"),
        ("CHEBI:86360", "MnSO4"),
        ("CHEBI:60720", "Na-silicate"),
        ("CHEBI:34683", "Na2HPO4"),
        ("CHEBI:75215", "Na2MoO4"),
        ("CHEBI:76208", "Na2S"),
        ("CHEBI:48843", "Na2SeO3"),
        ("CHEBI:77775", "Na2SeO4"),
        ("CHEBI:32149", "Na2SO4"),
        ("CHEBI:63940", "Na2WO4"),
        ("CHEBI:64220", "Na glutamate"),
        ("CHEBI:37585", "NaH2PO4"),
        ("CHEBI:34887", "NiCl2"),
        ("CHEBI:63675", "Sodium succinate"),
    }
)

HYDRATE_TARGETS: frozenset[TargetKey] = frozenset(
    {
        ("cas:12054-85-2", "ammonium molybdate tetrahydrate"),
        ("kgmicrobe.compound:cocl2_x_2_h2o", "CoCl2 x 2 H2O"),
        ("kgmicrobe.compound:cocl2_x_4_h2o", "CoCl2 x 4 H2O"),
        ("CHEBI:23414", "CuSO4 x 2 H2O"),
        ("CHEBI:23414", "CuSO4 x 4 H2O"),
        (
            "kgmicrobe.ingredient:disodium_phosphate_heptahydrate_~28002_m_stock~29",
            "Disodium phosphate heptahydrate (0.02 M stock)",
        ),
        ("CHEBI:75832", "FeSO4 x 5 H2O"),
        ("CHEBI:75832", "FeSO4 x 6 H2O"),
        ("CHEBI:32599", "MgSO4 x 6 H2O"),
        ("CHEBI:86360", "MnSO4 x 7 H2O"),
        ("CHEBI:91259", "Na2HPO4 x 12 H2O"),
        ("CHEBI:91258", "Na2HPO4 x 2 H2O"),
        ("kgmicrobe.compound:na2hpo4_x_7_h2o", "Na2HPO4 x 7 H2O"),
        ("CHEBI:32142", "Na3-citrate x 2 H2O"),
        ("kgmicrobe.compound:nicl2_x_2_h2o", "NiCl2 x 2 H2O"),
        ("CHEBI:53504", "NiSO4 x 7 H2O"),
        ("CHEBI:86345", "MgCl2 x 6 H2O"),
    }
)

TARGET_KINDS: dict[TargetKey, str] = {
    **dict.fromkeys(ANHYDROUS_TARGETS, ANHYDROUS_KIND),
    **dict.fromkeys(HYDRATE_TARGETS, HYDRATE_KIND),
}


def water_state(text: object) -> str | None:
    text = str(text or "")
    if implausible_water_counts(text):
        return INVALID_WATER_STATE
    if VARIABLE_WATER_NOTATION.search(text):
        return VARIABLE_WATER_STATE
    count = water_multiplicity(text)
    if count:
        return count
    if HYDRATE_NOTATION.search(text) and ONE_WATER_NOTATION.search(text):
        return "1"
    return None


def false_hydrate_reason(
    target_kind: str,
    preferred_term: object,
    synonym: dict,
) -> str | None:
    if not is_resolving_synonym(synonym):
        return None

    return false_hydrate_text_reason(
        target_kind,
        preferred_term,
        synonym.get("synonym_text"),
    )


def false_hydrate_text_reason(
    target_kind: str,
    preferred_term: object,
    synonym_text: object,
) -> str | None:
    synonym_text = str(synonym_text or "")
    if not HYDRATE_NOTATION.search(synonym_text):
        return None
    if target_kind == ANHYDROUS_KIND:
        return "hydrate synonym on an anhydrous record"

    owner_state = water_state(preferred_term)
    synonym_state = water_state(synonym_text)
    if synonym_state == INVALID_WATER_STATE:
        return "malformed hydrate notation"
    if synonym_state == VARIABLE_WATER_STATE:
        return "variable hydrate synonym on a specific hydrate record"
    if owner_state and synonym_state and synonym_state != owner_state:
        return f"{synonym_state} H2O synonym on a {owner_state} H2O record"
    return None


def is_rejected_label(synonym: dict) -> bool:
    return str(synonym.get("synonym_type") or "").strip().upper() == "REJECTED_LABEL"


def reject_false_synonyms(record: dict, target_kind: str) -> tuple[list[str], list[str]]:
    preferred_term = record.get("preferred_term")
    changed: list[str] = []
    false_labels: list[str] = []
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict):
            continue
        if not false_hydrate_text_reason(
            target_kind,
            preferred_term,
            synonym.get("synonym_text"),
        ):
            continue
        if is_resolving_synonym(synonym) or is_rejected_label(synonym):
            false_labels.append(str(synonym.get("synonym_text") or ""))
        if not is_resolving_synonym(synonym):
            continue
        synonym["synonym_type"] = "REJECTED_LABEL"
        changed.append(str(synonym.get("synonym_text") or ""))
    return changed, false_labels


def append_history(record: dict, rejected: list[str]) -> None:
    labels = ", ".join(repr(label) for label in rejected)
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REJECTED_HIDDEN_HYDRATE_SYNONYMS",
            "changes": (
                "Marked hidden hydrate synonym(s) as REJECTED_LABEL so this "
                f"record no longer resolves sibling hydrate identities (#251): {labels}."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )


def reject_records(
    records: list[dict],
    targets: dict[TargetKey, str] = TARGET_KINDS,
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    seen: set[TargetKey] = set()
    rejected_by_label: dict[str, list[str]] = {}
    false_by_label: dict[str, list[str]] = {}
    for record in records:
        if record.get("mapping_status") == "REJECTED":
            continue
        key = (
            str(record.get("identifier") or ""),
            str(record.get("preferred_term") or ""),
        )
        target_kind = targets.get(key)
        if not target_kind:
            continue
        seen.add(key)
        rejected, false_labels = reject_false_synonyms(record, target_kind)
        if rejected:
            append_history(record, rejected)
            rejected_by_label[str(record["preferred_term"])] = rejected
        if false_labels:
            false_by_label[str(record["preferred_term"])] = false_labels

    missing = sorted(set(targets) - seen, key=lambda key: key[1].casefold())
    if missing:
        rendered = ", ".join(f"{identifier} {label!r}" for identifier, label in missing)
        raise SystemExit(f"expected #251 target record(s) were not found: {rendered}")

    return rejected_by_label, false_by_label


def scrub_sssom_other(
    sssom_text: str,
    rejected_by_label: dict[str, list[str]],
) -> tuple[str, int, int]:
    reader_lines = sssom_text.splitlines(keepends=True)
    header_index = next(
        index for index, line in enumerate(reader_lines) if line.startswith("subject_id")
    )
    columns = reader_lines[header_index].rstrip("\n").split("\t")
    column = {name: index for index, name in enumerate(columns)}
    out: list[str] = []
    scrubbed_rows = 0
    scrubbed_tokens = 0

    for line in reader_lines:
        fields = line.rstrip("\n").split("\t")
        eol = "\n" if line.endswith("\n") else ""
        if len(fields) < len(columns) or fields[0].startswith("#") or fields[0] == "subject_id":
            out.append(line)
            continue

        rejected = {
            label.casefold() for label in rejected_by_label.get(fields[column["subject_label"]], [])
        }
        if rejected:
            tokens = fields[column["other"]].split("|") if fields[column["other"]] else []
            kept = [token for token in tokens if token.casefold() not in rejected]
            if kept != tokens:
                fields[column["other"]] = "|".join(kept)
                scrubbed_rows += 1
                scrubbed_tokens += len(tokens) - len(kept)

        out.append("\t".join(fields) + eol)

    if out and not out[-1].endswith("\n"):
        out[-1] += "\n"
    return "".join(out), scrubbed_rows, scrubbed_tokens


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    doc = yaml.safe_load(COLLECTION.read_text(encoding="utf-8")) or {}
    rejected_by_label, false_by_label = reject_records(doc.get("ingredients") or [])
    sssom_text, scrubbed_rows, scrubbed_tokens = scrub_sssom_other(
        SSSOM.read_text(encoding="utf-8"),
        false_by_label,
    )

    rejected_synonyms = sum(len(labels) for labels in rejected_by_label.values())
    print(f"{rejected_synonyms} synonym(s) rejected across {len(rejected_by_label)} #251 record(s)")
    for label, rejected in sorted(rejected_by_label.items(), key=lambda item: item[0].casefold()):
        print(f"  {label}: {len(rejected)}")
    print(f"scrubbed {scrubbed_tokens} SSSOM `other` token(s) from {scrubbed_rows} row(s)")

    if args.apply:
        save_yaml(doc, COLLECTION, validate=True, target_class="IngredientCollection")
        SSSOM.write_text(sssom_text, encoding="utf-8")
        print(f"\nwrote {COLLECTION.relative_to(ROOT)} and {SSSOM.relative_to(ROOT)}")
    else:
        print("\ndry-run; pass --apply to write")

    return 0


if __name__ == "__main__":
    sys.exit(main())
