#!/usr/bin/env python3
"""Retire curated synonyms that are ChEBI's names for an unrelated compound (#669).

`Ca(NO3)2` is calcium nitrate (CHEBI:64205). It was once mis-mapped to cadmium
nitrate (CHEBI:77732); the mapping was corrected, but the six synonyms harvested
from kg-microbe while it was wrong stayed behind as EXACT_SYNONYMs:

    Cadmium(II) nitrate | Cd(NO3)2 | Nitric acid, cadmium salt | ... | cadmium nitrate

They publish through the SSSOM `other` column on an `exactMatch` row, and
kg-microbe merges `other` into the object's synonym set -- so the calcium nitrate
node answered to a toxic heavy-metal salt's names. Rule K saw one of the six,
because only one happens to be another record's preferred_term.

The same shape recurs. Twelve of the affected synonyms carry the source
`sssom_other_backfill`: a backfill copied SSSOM `other` tokens back into curated
YAML, round-tripping kg-microbe's contamination into MIM's records.

Criterion -- deliberately narrow, and re-derived from ChEBI on every run:

  * the synonym is a name (label or synonym) ChEBI gives the WRONG term,
  * it is NOT a name ChEBI gives the record's own term, and
  * the (own, wrong) pair is listed below, each one checked by hand: no ChEBI
    edge joins the two in either direction, and their InChIKey connectivity
    blocks differ. Related forms -- a salt and its parent, a stereoisomer and
    its racemate -- are a curator's call and are not touched here.

Synonyms are marked REJECTED_LABEL rather than deleted. The label did arrive on
this record, so the provenance is real; and claw's builder filters every
candidate alternate -- kg-microbe's included -- through the record's rejected
labels, so the tombstone keeps the name out even while kg-microbe still supplies
it. Deleting it would let the next rebuild put it straight back.

Usage:
    python scripts/retire_wrong_compound_synonyms.py            # dry run
    python scripts/retire_wrong_compound_synonyms.py --apply
"""

from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "ingredients" / "mapped"
CHEBI_DB = Path(os.environ.get("CHEBI_DB", Path.home() / ".data" / "oaklib" / "chebi.db"))
CURATOR = "retire_wrong_compound_synonyms"
TIMESTAMP = "2026-09-20T00:00:00Z"

#: (the record's own term, the unrelated term whose names leaked onto it, why).
TARGETS: tuple[tuple[str, str, str], ...] = (
    ("CHEBI:64205", "CHEBI:77732", "calcium nitrate is not cadmium nitrate"),
    ("CHEBI:16411", "CHEBI:87514", "indole-3-acetic acid is not ethyl 2-hexenoate"),
    ("CHEBI:18101", "CHEBI:156387", "4-hydroxyphenylacetic acid is not aspyrone"),
    ("CHEBI:29125", "CHEBI:29242", "arsenate is not arsenite: a different oxidation state"),
    ("CHEBI:6650", "CHEBI:65947", "malic acid is not garciniaxanthone F"),
    ("CHEBI:16325", "CHEBI:39063", "lithocholic acid is not tricine"),
    ("CHEBI:16325", "CHEBI:35920", "lithocholic acid is not berbaman"),
    ("CHEBI:132112", "CHEBI:59168", "sodium thiosulfate is not a nonaethylene glycol ether"),
    ("CHEBI:30745", "CHEBI:103822", "phenylacetic acid is not LSM-15166"),
    ("CHEBI:9532", "CHEBI:45395", "thiamine pyrophosphate is not pyrithiamine pyrophosphate, its antagonist"),
    ("CHEBI:53258", "CHEBI:30769", "trisodium citrate is a salt of citric acid, not citric acid (Section 3)"),
)

_NAME_PREDICATES = (
    "rdfs:label", "oio:hasExactSynonym", "oio:hasRelatedSynonym",
    "oio:hasBroadSynonym", "oio:hasNarrowSynonym",
)


def chebi_names(connection: sqlite3.Connection, curie: str) -> set[str]:
    """
    Return every name ChEBI gives a term, casefolded.

    :param connection: An open connection to a semantic-sql ChEBI build.
    :param curie: The term, e.g. ``CHEBI:77732``.
    :return: Its label and synonyms, casefolded.
    """
    marks = ",".join("?" for _ in _NAME_PREDICATES)
    query = f"select value from statements where subject=? and predicate in ({marks})"  # noqa: S608
    return {(value or "").casefold() for (value,) in connection.execute(query, (curie, *_NAME_PREDICATES))}


def wrong_synonyms(record: dict, own: set[str], wrong: set[str]) -> list[dict]:
    """
    Return the record's live synonyms that name the wrong term and not its own.

    :param record: One ingredient record.
    :param own: Names ChEBI gives the record's own term.
    :param wrong: Names ChEBI gives the unrelated term.
    :return: The synonym entries to retire, in file order.
    """
    out = []
    for synonym in record.get("synonyms") or []:
        if str(synonym.get("synonym_type") or "").upper() == "REJECTED_LABEL":
            continue
        key = str(synonym.get("synonym_text") or "").strip().casefold()
        if key and key in wrong and key not in own:
            out.append(synonym)
    return out


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write the change")
    args = parser.parse_args(argv)

    if not CHEBI_DB.is_file() or CHEBI_DB.stat().st_size == 0:
        print(f"ChEBI build not found at {CHEBI_DB}; set CHEBI_DB.", file=sys.stderr)
        return 2
    connection = sqlite3.connect(CHEBI_DB)

    by_identifier: dict[str, list[Path]] = {}
    for path in sorted(MAPPED.glob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if record.get("mapping_status") == "MAPPED":
            by_identifier.setdefault(str(record.get("identifier") or ""), []).append(path)

    retired = 0
    for own_curie, wrong_curie, reason in TARGETS:
        own, wrong = chebi_names(connection, own_curie), chebi_names(connection, wrong_curie)
        for path in by_identifier.get(own_curie, []):
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
            hits = wrong_synonyms(record, own, wrong)
            if not hits:
                continue
            names = [hit["synonym_text"] for hit in hits]
            print(f"{path.name}: {len(hits)} name(s) of {wrong_curie} -> REJECTED_LABEL")
            for name in names:
                print(f"    - {name}")
            retired += len(hits)
            if not args.apply:
                continue
            for hit in hits:
                hit["synonym_type"] = "REJECTED_LABEL"
            record.setdefault("curation_history", []).append({
                "timestamp": TIMESTAMP,
                "curator": CURATOR,
                "action": "CORRECTED",
                "changes": (
                    f"Marked {len(hits)} synonym(s) non-resolving: {names}. ChEBI gives "
                    f"these names to {wrong_curie}, not to this record's {own_curie} -- "
                    f"{reason}. Kept as REJECTED_LABEL so a rebuild cannot restore them "
                    f"from kg-microbe's synonym list (#669)."
                ),
                "llm_assisted": True,
            })
            save_yaml(record, path)
    verb = "Retired" if args.apply else "Would retire"
    print(f"\n{verb} {retired} synonym(s).")
    if not args.apply:
        print("Dry run. Re-run with --apply, then `just sync-curated`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
