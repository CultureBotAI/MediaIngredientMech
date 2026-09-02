#!/usr/bin/env python3
"""Move the SSSOM `other` surface forms that only MIM knows onto the records.

`other` is the column kg-microbe merges into an ontology entity's synonyms, so it
reaches KGX. Today it carries content the curated records cannot reproduce: a rebuild
from `data/ingredients/` drops 9,533 tokens. That makes the published artifact
unregenerable, which is the defect (#520).

Most of the gap is not worth keeping. kg-microbe transforms ChEBI itself, so 82% of
those tokens are a second, stale copy of synonyms the consumer already holds from
ChEBI directly -- for CHEBI:16004 its node carries a superset of MIM's row. Re-emitting
them from the builder would institutionalise that redundancy.

The remaining 18% is MIM's actual contribution: recipe surface forms no ontology has
(`n-propyl chloride`, `1,1,2--Trichloroethane`, `1,2-propandiol`). Only MIM sees the
recipes, so only a record can hold them. This tool moves exactly those onto the records,
after which a rebuild reproduces `other` and the artifact becomes regenerable.

Selection, per published row:
    token is absent from a fresh rebuild of the same row      (it would be lost)
AND token is absent from the kg-microbe node for that object  (not already in KGX)
AND token is not role text                                    (a defect, not a synonym)

Written as RAW_TEXT: these are raw surface forms recovered from a published artifact
whose per-token provenance cannot be verified, so claiming EXACT_SYNONYM would overstate
them. Only REJECTED_LABEL is withheld from `other` by the builder, so RAW_TEXT
round-trips.

Read-only by default. Writes per-record files; follow with `just sync-curated`.

Usage:
    python scripts/backfill_sssom_surface_forms.py --rebuild <path> --kgm-nodes <dir>
    python scripts/backfill_sssom_surface_forms.py ... --apply
"""

from __future__ import annotations

import argparse
import csv
import glob
import io
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
PUBLISHED = _REPO / "mappings" / "ingredient_mappings.sssom.tsv"
CURATOR = "claude_sssom_surface_form_backfill"
SOURCE = "sssom_other_backfill"

# Role/property text that leaked into a synonym list. Not chemical names, and the
# builder already refuses the `Role:`-prefixed spellings -- these are the variants it
# does not catch, which is why they reached the published artifact.
_ROLE_TEXT = re.compile(
    r"^\s*(utilizes|utilises|role|carbon source|nitrogen source|sulfur source|"
    r"energy source|electron donor|electron acceptor|cross-references|properties|"
    r"aerobic|anaerobic)\s*[:\-]",
    re.IGNORECASE,
)
# ChEBI writes a hydrate as `<compound>--water (1/n)`. That doubled hyphen is the
# ontology's own convention, not damage, and treating it as damage discarded real
# labels for the citrate, cobalt-sulfate and phosphate hydrates.
_CHEBI_HYDRATE = re.compile(r"--\s*water\s*\(\d+/\d+\)\s*$", re.IGNORECASE)
# Recipe punctuation damage: a doubled separator, or a dangling opener/separator.
_DAMAGED = re.compile(r"--|[(\[,;\-]\s*$")


# CAS index nomenclature inverts the name and ends on the substituent's hyphen:
# `beta-D-glucopyranose, 4-O-beta-D-galactopyranosyl-`. That trailing hyphen is the
# convention, not truncation, so it must not be read as damage.
_CAS_INVERTED = re.compile(r",\s+\S.*-$")


def repair(token: str) -> str | None:
    """Deterministically undo recipe damage, or None if the token cannot be trusted.

    A doubled hyphen is ASCII mangling of a real name and collapses cleanly; a trailing
    comma is a truncated list and strips cleanly. Neither invents information -- and
    because the repaired form then goes back through the same redundancy test, a repair
    that merely reproduces a name the record or the ontology already has is dropped
    rather than added twice.

    Truncation inside a parenthetical (`... (methyl alpha-`) is NOT repairable: the lost
    text cannot be recovered, and guessing it would fabricate a synonym.
    """
    if token.count("(") != token.count(")"):
        return None
    fixed = token.replace("--", "-").rstrip().rstrip(",").rstrip()
    return fixed or None


def is_damaged(token: str) -> bool:
    if _CHEBI_HYDRATE.search(token) or _CAS_INVERTED.search(token):
        return False
    return bool(_DAMAGED.search(token))


def read_sssom(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    if not path.is_file():
        raise SystemExit(f"SSSOM not found: {path}")
    body = [line for line in path.read_text(encoding="utf-8").splitlines(keepends=True)
            if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    return {(r["subject_id"], r["object_id"]): r for r in reader}


def kgm_node_synonyms(nodes_dir: Path) -> dict[str, set[str]]:
    """CURIE -> {casefolded name and synonyms} from kg-microbe's ontology transforms."""
    if not nodes_dir.is_dir():
        raise SystemExit(
            f"kg-microbe ontology transforms not found: {nodes_dir}\n"
            "Without them every token looks unique and the backfill would copy ChEBI "
            "wholesale into the records. Run kg-microbe's `just transform` first."
        )
    csv.field_size_limit(10_000_000)
    out: dict[str, set[str]] = defaultdict(set)
    files = sorted(glob.glob(str(nodes_dir / "*_nodes.tsv")))
    if not files:
        raise SystemExit(f"no *_nodes.tsv under {nodes_dir}")
    for path in files:
        with open(path, encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                curie = (row.get("id") or "").strip()
                if not curie:
                    continue
                if row.get("name"):
                    out[curie].add(row["name"].strip().casefold())
                for token in (row.get("synonym") or "").split("|"):
                    if token.strip():
                        out[curie].add(token.strip().casefold())
    return out


def tokens(row: dict[str, str]) -> list[str]:
    return [t.strip() for t in (row.get("other") or "").split("|") if t.strip()]


def mim_curie(stem: str) -> str:
    """The subject CURIE claw's builder emits for a record file.

    Mirrors `build_mim_ingredient_sssom._mim_curie`: non-URL-safe characters become
    `~HEX`. Matching on the raw stem instead misses every record whose filename has a
    parenthesis or a Greek letter -- 19 subjects and 1,409 of their surface-form
    tokens, which would otherwise have been silently reported as having no record.
    """
    return "MIM:" + re.sub(r"[^A-Za-z0-9_\-.]", lambda m: f"~{ord(m.group(0)):02X}", stem)


def records_by_subject() -> dict[str, Path]:
    out: dict[str, Path] = {}
    for path in (_REPO / "data" / "ingredients").rglob("*.yaml"):
        out[f"MIM:{path.stem}"] = path
        out.setdefault(mim_curie(path.stem), path)
    return out


def published_labels() -> dict[str, set[str]]:
    """Casefolded surface form -> the record identifiers that already publish it.

    `docs/data/label_index.csv` is what CultureMech resolves against, and it fails
    CLOSED on a name two records claim. So a synonym is only safe to add if no OTHER
    record already answers to it -- and many ontology synonyms are legitimately shared
    across a family: `L-aspartic acid` belongs to the acid, its potassium salt and its
    sodium salt alike. Migrating it onto each would make the name ambiguous and take
    the label from resolvable to unresolvable, which is strictly worse than the
    missing synonym it was meant to fix.
    """
    index = _REPO / "docs" / "data" / "label_index.csv"
    if not index.is_file():
        raise SystemExit(f"label index not found: {index}; run `just export-lists` first")
    owners: dict[str, set[str]] = defaultdict(set)
    with index.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            owners[row["label"].strip().casefold()].add(row["identifier"])
    return owners


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--published", type=Path, default=PUBLISHED)
    parser.add_argument("--rebuild", type=Path, required=True,
                        help="freshly built working copy to compare against")
    parser.add_argument("--kgm-nodes", type=Path, required=True,
                        help="kg-microbe data/transformed/ontologies directory")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--date", default=datetime.now(timezone.utc).isoformat())
    args = parser.parse_args(argv)

    published, rebuilt = read_sssom(args.published), read_sssom(args.rebuild)
    known = kgm_node_synonyms(args.kgm_nodes)
    records = records_by_subject()

    owners = published_labels()
    identifier_of = {}
    for subject, path in records.items():
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            identifier_of[subject] = str(data.get("identifier") or "")

    claimed: dict[str, str] = {}
    planned: dict[Path, list[str]] = defaultdict(list)
    stats = {"redundant": 0, "role_text": 0, "repaired_redundant": 0, "repaired": 0,
             "unrepairable": 0, "no_record": 0, "would_collide": 0, "kept": 0}
    collision_examples: list[tuple[str, str, list[str]]] = []
    damaged_examples: list[tuple[str, str]] = []

    for key, pub_row in published.items():
        new_row = rebuilt.get(key)
        if new_row is None:
            continue
        surviving = {t.casefold() for t in tokens(new_row)}
        already = known.get(key[1], set())
        key_subject = key[0]
        for token in tokens(pub_row):
            if token.casefold() in surviving:
                continue
            if token.casefold() in already:
                stats["redundant"] += 1
                continue
            if _ROLE_TEXT.match(token):
                stats["role_text"] += 1
                continue
            if is_damaged(token):
                # Repair what can be repaired deterministically, then re-test: 23 of
                # these collapse to a name the record and the kg-microbe node already
                # carry, so they add nothing and are dropped rather than migrated.
                fixed = repair(token)
                if fixed is None:
                    stats["unrepairable"] += 1
                    if len(damaged_examples) < 10:
                        damaged_examples.append((key[0], token))
                    continue
                if fixed.casefold() in surviving or fixed.casefold() in already:
                    stats["repaired_redundant"] += 1
                    continue
                token = fixed
                stats["repaired"] += 1
            path = records.get(key[0])
            if path is None:
                stats["no_record"] += 1
                continue
            # Would this name then be claimed by more than one record?
            #
            # NOT named `key`: that is the loop's (subject_id, object_id) tuple, and
            # rebinding it here made `records.get(key[0])` look up the token's first
            # CHARACTER for every later token in the same row -- so each row migrated
            # its first token and silently counted the rest as having no record.
            label_key = token.casefold()
            mine = identifier_of.get(key_subject, "")
            if owners.get(label_key, set()) - {mine}:
                stats["would_collide"] += 1
                if len(collision_examples) < 8:
                    collision_examples.append((key_subject, token, sorted(owners[label_key])[:2]))
                continue
            if claimed.get(label_key, key_subject) != key_subject:
                stats["would_collide"] += 1
                continue
            claimed[label_key] = key_subject
            planned[path].append(token)
            stats["kept"] += 1

    print(f"published rows compared: {len(published)}")
    print(f"  redundant (already on the kg-microbe node): {stats['redundant']}")
    print(f"  role text, not a synonym                  : {stats['role_text']}")
    print(f"  damaged, repaired to something already known: {stats['repaired_redundant']}")
    print(f"  damaged, repaired and migrated              : {stats['repaired']}")
    print(f"  damaged beyond repair, not migrated         : {stats['unrepairable']}")
    print(f"  no matching record                        : {stats['no_record']}")
    print(f"  would make the label ambiguous, skipped     : {stats['would_collide']}")
    for subject, token, who in collision_examples:
        print(f"      collides: {subject} {token!r} already published by {who}")
    print(f"  TO MIGRATE                                : {stats['kept']}"
          f" across {len(planned)} records")
    for subject, token in damaged_examples:
        print(f"      unrepairable: {subject} {token!r}")

    if not args.apply:
        for path, toks in sorted(planned.items())[:8]:
            print(f"\n  {path.relative_to(_REPO)}")
            for t in toks[:4]:
                print(f"      + {t!r}")
        print("\nDry run. Re-run with --apply to write.")
        return 0

    for path, toks in sorted(planned.items()):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        existing = {(s.get("synonym_text") or "").casefold()
                    for s in data.get("synonyms") or [] if isinstance(s, dict)}
        existing.add(str(data.get("preferred_term") or "").casefold())
        fresh = [t for t in dict.fromkeys(toks) if t.casefold() not in existing]
        if not fresh:
            continue
        data.setdefault("synonyms", []).extend(
            {"synonym_text": t, "synonym_type": "RAW_TEXT", "source": SOURCE} for t in fresh
        )
        data.setdefault("curation_history", []).append({
            "timestamp": args.date,
            "curator": CURATOR,
            "action": "ADDED_SYNONYMS",
            "changes": (
                f"Recovered {len(fresh)} surface form(s) that the published SSSOM `other` "
                f"carried but no curated record did, so a rebuild would have dropped them "
                f"from KGX: " + "; ".join(repr(t) for t in fresh) + ". Tokens already "
                "present on the kg-microbe ontology node were left out as redundant "
                "(#520)."
            ),
            "llm_assisted": False,
        })
        path.write_text(
            yaml.dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False),
            encoding="utf-8",
        )
    print(f"\nWrote {stats['kept']} surface forms across {len(planned)} records.")
    print("Next: `just sync-curated`, then rebuild the SSSOM and confirm `other` round-trips.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
