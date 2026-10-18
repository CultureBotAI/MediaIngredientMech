#!/usr/bin/env python3
"""Put the NaH2PO4 hydrate spellings on the records they name (#758).

``Nah2po4_X_2_H2o`` (the dihydrate label's local identity) carried six
kg-microbe ``HYDRATE_FORM`` spellings, three of which name the *monohydrate*:
``NaH2PO4 x H2O``, ``NaH2PO4·H2O``, ``NaH2PO4・H2O``. The monohydrate has its
own record, ``Sodium_phosphate_monobasic_monohydrate`` (CHEBI:114249).
CultureMech resolves all six spellings to the anhydrous ``NaH2PO4``
(CHEBI:37585), so 40 recipes were counted under the wrong form.

This moves the three monohydrate strings onto the monohydrate record
(``REJECTED_LABEL`` on the dihydrate), and, through
``SOURCE_LABEL_IDENTIFIER_OVERRIDES``, moves the recipe-membership edges of
all six spellings off the anhydrous record onto the form each names, then
refreshes the three records' ``occurrence_statistics`` from the edges (the
batch-3/4 shape). Dry-run by default; ``--apply`` writes records and
membership.

**Blocked until #740 is resolved.** ``Nah2po4.yaml`` (the anhydrous record whose
counts must drop by 40) is pinned byte-for-byte by
``reports/semantic_review_20260921/corrections/identity-plan.json``, so the
resolution review refuses any edit to it. Run this once that pin is supersedable,
together with the six ``SOURCE_LABEL_IDENTIFIER_OVERRIDES`` entries the
``verify()`` step requires (three monohydrate spellings -> CHEBI:114249, three
dihydrate spellings -> kgmicrobe.compound:nah2po4_x_2_h2o).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.culturemech_occurrences import (  # noqa: E402
    SOURCE_LABEL_IDENTIFIER_OVERRIDES,
    _source_label_key,
)
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

MAPPED = ROOT / "data" / "ingredients" / "mapped"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
ISSUE = "#758"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"

DIHYDRATE = "Nah2po4_X_2_H2o"
MONOHYDRATE = "Sodium_phosphate_monobasic_monohydrate"
ANHYDROUS = "Nah2po4"
MONOHYDRATE_STRINGS = ("NaH2PO4 x H2O", "NaH2PO4·H2O", "NaH2PO4・H2O")
DIHYDRATE_STRINGS = ("NaH2PO4 x 2H2O", "NaH2PO4·2H2O", "NaH2PO4・2H2O")
FROM_IDENTIFIER = "CHEBI:37585"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(slug: str) -> tuple[Path, dict]:
    path = MAPPED / f"{slug}.yaml"
    return path, yaml.safe_load(path.read_text())


def verify() -> dict[str, str]:
    targets = {}
    _, mono = load(MONOHYDRATE)
    _, di = load(DIHYDRATE)
    for text in MONOHYDRATE_STRINGS:
        targets[text] = mono["identifier"]
    for text in DIHYDRATE_STRINGS:
        targets[text] = di["identifier"]
    missing = [t for t, ident in targets.items() if SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(_source_label_key(t)) != ident]
    if missing:
        raise SystemExit(f"SOURCE_LABEL_IDENTIFIER_OVERRIDES lacks: {missing}")
    return targets


def move_synonyms(log: list, write: bool) -> None:
    path, di = load(DIHYDRATE)
    before = sha(path)
    retired = []
    for synonym in di.get("synonyms") or []:
        if synonym.get("synonym_text") in MONOHYDRATE_STRINGS and synonym.get("synonym_type") != "REJECTED_LABEL":
            synonym["synonym_type"] = "REJECTED_LABEL"
            retired.append(synonym["synonym_text"])
    if retired:
        record_curation_event(
            di, curator=CURATOR, action="REJECTED_WRONG_FORM_SYNONYMS",
            changes=(f"Retyped REJECTED_LABEL: {retired}: monohydrate spellings on the dihydrate label's record; they "
                     f"now live on {MONOHYDRATE} (CHEBI:114249) ({ISSUE})."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"RETIRE {DIHYDRATE}: {retired}")
        if write:
            write_validated_ingredient(di, path)
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "synonym_retirement",
                    "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                    "change": f"REJECTED_LABEL: {retired}",
                    "verification": "Each string names the monohydrate (one water); the record is the dihydrate label."})
    path, mono = load(MONOHYDRATE)
    before = sha(path)
    existing = {s.get("synonym_text") for s in mono.get("synonyms") or []}
    added = [t for t in MONOHYDRATE_STRINGS if t not in existing]
    for text in added:
        mono.setdefault("synonyms", []).append({"synonym_text": text, "synonym_type": "HYDRATE_FORM", "source": f"moved from {DIHYDRATE} ({ISSUE})"})
    if added:
        record_curation_event(
            mono, curator=CURATOR, action="ADDED_SYNONYMS",
            changes=(f"Added HYDRATE_FORM spellings {added}, moved off {DIHYDRATE}: each names the monohydrate this "
                     f"record denotes (CHEBI:114249), and CultureMech names them in 36 recipes ({ISSUE})."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"ADD    {MONOHYDRATE}: {added}")
        if write:
            write_validated_ingredient(mono, path)
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "synonym_move",
                    "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                    "change": f"HYDRATE_FORM synonyms added: {added}",
                    "verification": "Monohydrate spellings moved from the dihydrate record."})


def move_memberships(occurrences: Path, targets: dict[str, str], write: bool) -> dict[str, int]:
    wanted = {_source_label_key(t): ident for t, ident in targets.items()}
    moves: dict[tuple[str, str], str] = {}
    with occurrences.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            target = wanted.get(_source_label_key(row.get("preferred_term") or ""))
            if target and (row.get("resolved_identifier") or "").strip() == FROM_IDENTIFIER:
                moves[(FROM_IDENTIFIER, row["recipe_id"])] = target
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments, header, data, counts = [], None, [], defaultdict(int)
    for line in lines:
        if line.startswith("#"):
            comments.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if header is None:
            header = cells
            continue
        replacement = moves.get((cells[0], cells[1]))
        if replacement:
            cells[0] = replacement
            counts[replacement] += 1
        data.append(cells)
    data.sort(key=lambda cells: tuple(cells[:2]))
    keys = [(c[0], c[1]) for c in data]
    if len(keys) != len(set(keys)):
        raise SystemExit("membership moves would create duplicate edge keys")
    print(f"membership edges moved off {FROM_IDENTIFIER}: {dict(sorted(counts.items()))}")
    if write:
        MEMBERSHIP.write_text("".join(comments) + "\t".join(header) + "\n" + "".join("\t".join(c) + "\n" for c in data), encoding="utf-8")
    return dict(counts)


def refresh_counts(log: list, write: bool) -> None:
    affected = {load(s)[1]["identifier"]: s for s in (ANHYDROUS, DIHYDRATE, MONOHYDRATE)}
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for row in csv.DictReader([line for line in MEMBERSHIP.read_text(encoding="utf-8").splitlines() if not line.startswith("#")], delimiter="\t"):
        if row["mim_identifier"] in affected:
            counts[row["mim_identifier"]][0] += 1
            counts[row["mim_identifier"]][1] += int(row["occurrences"])
    for identifier, slug in affected.items():
        path, record = load(slug)
        if identifier not in counts:
            continue
        stats = record.get("occurrence_statistics") or {}
        old = (stats.get("media_count") or 0, stats.get("total_occurrences") or 0)
        new = tuple(counts[identifier])
        if old == new:
            continue
        before = sha(path)
        record["occurrence_statistics"] = {**stats, "media_count": new[0], "total_occurrences": new[1]}
        record_curation_event(
            record, curator=CURATOR, action="REFRESHED_OCCURRENCE_STATISTICS",
            changes=(f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]} after the NaH2PO4 hydrate spellings' "
                     f"recipe memberships moved to the form each names ({ISSUE})."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"OCCURRENCES {slug}: {old[0]}/{old[1]} -> {new[0]}/{new[1]}")
        if write:
            write_validated_ingredient(record, path)
        entry = next((e for e in log if e["source_record"] == str(path.relative_to(ROOT))), None)
        if entry:
            entry["after_yaml_sha256"] = sha(path) if write else None
            entry["change"] += f"; occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]}"
        else:
            log.append({"source_record": str(path.relative_to(ROOT)), "shape": "occurrence_refresh",
                        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                        "change": f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]}",
                        "verification": "Counts follow the source label through SOURCE_LABEL_IDENTIFIER_OVERRIDES."})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--occurrences", type=Path, required=True)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    targets = verify()
    log: list = []
    move_synonyms(log, args.apply)
    move_memberships(args.occurrences, targets, args.apply)
    refresh_counts(log, args.apply)
    if args.apply and args.log:
        previous = json.loads(args.log.read_text())["records"] if args.log.is_file() else []
        merged = {e["source_record"]: e for e in previous}
        for entry in log:
            if entry["source_record"] in merged:
                merged[entry["source_record"]]["after_yaml_sha256"] = entry["after_yaml_sha256"]
                merged[entry["source_record"]]["change"] += "; " + entry["change"]
            else:
                merged[entry["source_record"]] = entry
        args.log.write_text(json.dumps({"issue": "#232", "batch": "wrong-form-names", "records": list(merged.values())}, indent=2) + "\n")
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
