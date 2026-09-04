#!/usr/bin/env python3
"""Export lists of mapped and unmapped ingredients from curated YAML files.

Generates JSON, CSV, and Markdown lists for both mapped and unmapped ingredients.
Uses the curated collection files as source.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

# Ensure the src package is importable when this file is run directly.
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402

console = Console()


def load_ingredients(yaml_path: Path) -> list[dict]:
    """Load ingredients from YAML file."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Handle collection format
    if isinstance(data, dict) and "ingredients" in data:
        return data["ingredients"]
    elif isinstance(data, list):
        return data
    return []


def _ontology_id(ing: dict) -> str:
    """ontology_id lives under ontology_mapping (not at the record top level)."""
    return (ing.get("ontology_mapping") or {}).get("ontology_id", "") or ""


def _molecular_formula(ing: dict) -> str:
    """Used only to decide whether two records competing for one label are the
    same substance (#232). Absent on ~a third of records, which is why
    `unresolved:*` exists as a verdict rather than defaulting to agreement."""
    return (ing.get("chemical_properties") or {}).get("molecular_formula", "") or ""


_ELEMENT = re.compile(r"([A-Z][a-z]?)(\d*)")


def _formula_elements(formula: str) -> tuple | None:
    """`2K.O3Te` -> (('K',2),('O',3),('Te',1)). None if it cannot be parsed.

    Comparing formulas as RAW STRINGS reported false conflicts (#389): ChEBI
    writes salts in dot notation and other sources collapse them, so
    `2K.O3Te` and `K2O3Te` — one substance, potassium tellurite — read as two.
    Two of the 167 flagged conflicts were that. A false conflict is the worst
    outcome for this column: it tells a consumer to distrust a correct answer.

    Unparseable input returns None and is treated as UNKNOWN by the caller, not
    as disagreement — guessing in either direction would be worse than saying so.
    """
    if not formula:
        return None
    total: dict[str, int] = {}
    for part in formula.split("."):
        m = re.match(r"^(\d+)(.*)$", part)
        mult, body = (int(m.group(1)), m.group(2)) if m else (1, part)
        found = [(el, n) for el, n in _ELEMENT.findall(body) if el]
        if not found:
            return None
        for el, n in found:
            total[el] = total.get(el, 0) + mult * (int(n) if n else 1)
    return tuple(sorted(total.items())) or None


def _ontology_label(ing: dict) -> str:
    """The mapped term's own label, e.g. `potassium hydroxide` for the record `KOH`."""
    return (ing.get("ontology_mapping") or {}).get("ontology_label", "") or ""


# Separator for the CSV synonyms column. `|` is the multi-value separator this
# repo's SSSOM already uses (the `source`, `validation_method` and `other`
# columns), so consumers split on it today.
SYNONYM_SEP = "|"

# Curation strings that live in `synonyms` but are not names anything answers
# to: role/property annotations carried over from the CultureMech import, and
# bare parentheticals like `(sodium salt)` or `(for solid medium, alternative)`
# that are fragments of a name, not a name. Publishing them as resolvable labels
# would make `Role: Carbon source; Properties: ...` "resolve" to 44 different
# CHEBI ids.
#
# The first pattern used to be `Role:.*;\s*Properties:`, requiring BOTH keywords
# in one string. The import also writes them SPLIT — `Role: Carbon source` and
# `Properties: Defined component, Simple component` as separate synonyms — and
# those passed straight through. 183 such rows were published as labels, and
# they were the worst ambiguity in the index by multiplicity: `properties:
# defined component, organic compound, simple component` resolved to 19
# different identifiers, `role: carbon source` to 14 (#232).
#
# Anchoring on the keyword and a colon catches both forms. `Cross-references:`
# is the third shape the same importer emits (53 synonyms).
_NOT_A_LABEL = re.compile(
    r"^\s*(?:role|properties|cross-references?)\s*:|^\s*\([^)]*\)\s*$",
    re.IGNORECASE)


def _synonyms(ing: dict) -> list[str]:
    """Every raw label this record answers to, minus the preferred_term itself.

    Merging a duplicate folds its raw label in here and deletes its record, and
    merges add no SSSOM row (SSSOM subjects are preferred_terms, never
    synonyms). `docs/data/ingredients.json` has always carried synonyms, but the
    backlog exports here did not -- so after a merge the label stopped resolving
    from the CSV/JSON that consumers join against. Issue #229.
    """
    preferred = ing.get("preferred_term", "")
    seen, out = {preferred}, []
    for s in ing.get("synonyms") or []:
        if not is_resolving_synonym(s or {}):
            continue
        text = (s or {}).get("synonym_text")
        if not text or text in seen or _NOT_A_LABEL.match(text):
            continue
        seen.add(text)
        out.append(text)
    return out


def _join_synonyms(ing: dict) -> str:
    """Pack synonyms into the CSV cell, refusing rather than corrupting.

    Nothing in the schema forbids `|` in a synonym_text, and no synonym contains
    one today. If one ever does, joining silently would split it into two bogus
    labels on read, so fail here with the record named -- the coverage gate would
    otherwise report it as an unresolvable label and advise re-running the export,
    which loops forever.
    """
    syns = _synonyms(ing)
    bad = [s for s in syns if SYNONYM_SEP in s]
    if bad:
        raise ValueError(
            f"{ing.get('identifier', '?')}: synonym(s) contain the {SYNONYM_SEP!r} "
            f"separator and cannot be packed into the CSV column: {bad}. "
            "Change the separator or escape it before exporting.")
    return SYNONYM_SEP.join(syns)


def export_to_json(ingredients: list[dict], output_path: Path):
    """Export ingredients to JSON format."""
    records = []
    for ing in ingredients:
        record = {
            "identifier": ing.get("identifier", ""),
            "ontology_id": _ontology_id(ing),
            "preferred_term": ing.get("preferred_term", ""),
            "mapping_status": ing.get("mapping_status", ""),
            "synonyms": _synonyms(ing),
        }

        # Add ontology mapping details if mapped
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            record.update({
                "ontology_label": om.get("ontology_label", ""),
                "ontology_source": om.get("ontology_source", ""),
                "mapping_quality": om.get("mapping_quality", ""),
            })

        # Add statistics
        if ing.get("occurrence_statistics"):
            stats = ing["occurrence_statistics"]
            record.update({
                "total_occurrences": stats.get("total_occurrences", 0),
                "media_count": stats.get("media_count", 0),
            })

        records.append(record)

    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)

    return len(records)


def export_to_csv(ingredients: list[dict], output_path: Path):
    """Export ingredients to CSV format."""
    fieldnames = [
        "identifier",
        "ontology_id",
        "preferred_term",
        "mapping_status",
        "ontology_label",
        "ontology_source",
        "mapping_quality",
        "total_occurrences",
        "media_count",
        # appended, not inserted: a consumer indexing columns positionally keeps
        # working, and one reading by header name picks it up. Issue #229.
        "synonyms",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()

        for ing in ingredients:
            row = {
                "identifier": ing.get("identifier", ""),
                "ontology_id": _ontology_id(ing),
                "preferred_term": ing.get("preferred_term", ""),
                "mapping_status": ing.get("mapping_status", ""),
                "synonyms": _join_synonyms(ing),
            }

            # Add ontology mapping details
            if ing.get("ontology_mapping"):
                om = ing["ontology_mapping"]
                row.update({
                    "ontology_label": om.get("ontology_label", ""),
                    "ontology_source": om.get("ontology_source", ""),
                    "mapping_quality": om.get("mapping_quality", ""),
                })

            # Add statistics
            if ing.get("occurrence_statistics"):
                stats = ing["occurrence_statistics"]
                row.update({
                    "total_occurrences": stats.get("total_occurrences", 0),
                    "media_count": stats.get("media_count", 0),
                })

            writer.writerow(row)

    return len(ingredients)


def export_label_index(ingredients: list[dict], output_path: Path):
    """One row per (label, record) with how the label matched — #232.

    Publishing synonyms (#229) made 87 labels resolve to more than one
    identifier, and a consumer joining a raw ingredient string had no way to
    choose: `Vitamin B12` is the preferred_term of CHEBI:176843 and a synonym of
    two other records. The record-shaped exports cannot express this, because a
    row has one preferred_term and many synonyms — the ambiguity is per LABEL.

    So the precedence is made machine-readable instead of documented in prose:
    **take the first row for the label**. Resolve to its semantic `identifier`;
    `ontology_id` is the separate grounding target and is empty for 594 unmapped
    rows. Neither field is a guaranteed unique document address.
    """
    rows = []
    # Identifiers that some LIVE record actually claims. Rule 0 below lets a
    # record that owns a label outrank a live record's synonym, and a merge
    # tombstone is a legitimate owner because it carries the winner's
    # identifier. But nothing GATES that invariant, and a tombstone left
    # pointing at its own dead accession resolves to nothing — `Bacto Soytone`
    # sat on the obsolete CHEBI:8150 until #360 repointed it. So ownership only
    # jumps the queue when the owner's identifier is one a live record holds.
    resolvable = {ing.get("identifier", "") for ing in ingredients
                  if ing.get("mapping_status") == "MAPPED"}

    for ing in ingredients:
        ident = ing.get("identifier", "")
        preferred = ing.get("preferred_term", "")
        status = ing.get("mapping_status", "")
        ont = _ontology_id(ing)
        seen_labels = {preferred.lower()} | {x.lower() for x in _synonyms(ing)}
        if preferred:
            rows.append({"label": preferred, "match_type": "preferred_term",
                         "identifier": ident, "preferred_term": preferred,
                         "ontology_id": ont, "mapping_status": status})
        for syn in _synonyms(ing):
            rows.append({"label": syn, "match_type": "synonym",
                         "identifier": ident, "preferred_term": preferred,
                         "ontology_id": ont, "mapping_status": status})
        # The mapped TERM's own label, as a third way in. Many records are named
        # by formula (`KOH`, `KI`, `NaH2PO4•H2O`) while consumers write the
        # chemical name, and that name appears nowhere else on the record: it is
        # neither the preferred_term nor a synonym. 59 names CultureMech grounds
        # were unresolvable here for exactly that reason (#365).
        onto_label = _ontology_label(ing)
        if onto_label and onto_label.lower() not in seen_labels:
            rows.append({"label": onto_label, "match_type": "ontology_label",
                         "identifier": ident, "preferred_term": preferred,
                         "ontology_id": ont, "mapping_status": status})
    # Order within a label, most significant first:
    #   0. OWNERSHIP. A record whose own `preferred_term` IS this label makes a
    #      claim about exactly this string; a synonym or term-label on some
    #      other record is a weaker claim about something else. So ownership
    #      outranks even MAPPED-ness: a tombstone that owns the label beats a
    #      live record that merely lists it. That follows LABEL_INDEX_CONTRACT —
    #      REJECTED is not "no answer", since a tombstone carries the merge
    #      winner's identifier and resolves correctly.
    #      Without this, `FeSO4 x 7H2O` resolved to CHEBI:75832 `FeSO4 x 5 H2O`:
    #      a heptahydrate label answered with the PENTAhydrate. Same for
    #      `MnSO4 x 1 H2O` (got the heptahydrate) and `NiCl2 x 6 H2O` (got
    #      anhydrous NiCl2).
    #   1. MAPPED before anything else. Without this a REJECTED record's
    #      preferred_term outranks a MAPPED record's synonym, so `Bacto Soytone`
    #      resolved to the rejected CHEBI:8150 tombstone instead of the live
    #      FOODON:03315720 — 21 labels did that. Rule 0 is deliberately narrower
    #      than "match_type beats status": promoting match_rank wholesale also
    #      lets a tombstone's SYNONYM beat a live record's term label, which
    #      sent `EDTA disodium salt (anhydrous)` back to the rejected dihydrate.
    #      Only rank 0 jumps the queue.
    #   2. preferred_term before synonym.
    #   3. identifier, then preferred_term: `identifier` is NOT a unique record
    #      key (46 identifiers are held by 117 records), so without the final
    #      term 188 labels tie completely and the winner is decided by record
    #      order in the YAML.
    #   4. `label` LAST. It used to sort second, right after `label.lower()`,
    #      which put raw-string ordering above every semantic key — so among
    #      case variants of one label ASCII picked the winner, and uppercase
    #      won. `FRUCTOSE` (a synonym on `Fructooligosaccharides (FOS)`) beat
    #      `Fructose`, the owning record; `Citric Acid` (a synonym on
    #      `Trisodium citrate`) beat `Citric acid`; `ASPARAGINE` and `CYSTEINE`
    #      returned the L-enantiomer for a stereo-unspecified label. 16 labels
    #      resolved to the wrong record. Grouping is by `label.lower()`, so
    #      contiguity never needed `label` to sort early — only determinism
    #      does, and last position gives that.
    # Pinned by tests/test_label_index_precedence.py.
    # `ontology_label` ranks LAST of the three match types: a term label is the
    # ontology's name for the concept, not a name this record claims, so it is
    # the weakest signal. Measured over the corpus, adding it made 623 labels
    # newly resolvable, lost none, and changed exactly ONE existing answer:
    #
    #   EDTA disodium salt (anhydrous)
    #     was  CHEBI:64758  via a synonym on `Na2-EDTA x 2 H2O`  (REJECTED)
    #     now  CHEBI:64734  via the ontology_label of `Na2-EDTA` (MAPPED)
    #
    # That is the #232 rule working: MAPPED outranks match_type, so a live
    # record's term label beats a tombstone's synonym. The new answer is also the
    # right one — CHEBI:64734 IS the anhydrous disodium salt the label names.
    match_rank = {"preferred_term": 0, "synonym": 1, "ontology_label": 2}
    def owns_and_resolves(r: dict) -> bool:
        return (match_rank.get(r["match_type"], 9) == 0
                and r["identifier"] in resolvable)

    rows.sort(key=lambda r: (r["label"].lower(),
                             not owns_and_resolves(r),
                             r["mapping_status"] != "MAPPED",
                             match_rank.get(r["match_type"], 9),
                             r["identifier"], r["preferred_term"], r["label"]))
    # --- ambiguity verdict, per LABEL (#232) ------------------------------
    # `take the first row` is a promise the index cannot keep for every label:
    # 167 labels are carried as a synonym by records that are NOT the same
    # substance, so an arbitrary first row hands a consumer the wrong compound.
    # The partition below says which case a label is, so a consumer can refuse
    # the ones that are genuinely undecided instead of trusting all of them
    # equally. Nothing is suppressed and no curation is deleted — the ambiguity
    # is published rather than resolved by guess.
    # First NON-EMPTY formula per identifier, not last-wins (#388). `identifier`
    # is not unique across records — 75 are held by several, since a merge
    # tombstone carries the winner's identifier — and 28 of those disagree on
    # formula. A dict comprehension would let YAML record order decide the
    # verdict, so a label's published ambiguity would change when records are
    # reordered.
    formula_of: dict[str, str] = {}
    for ing in ingredients:
        key = ing.get("identifier", "")
        if not formula_of.get(key):
            formula_of[key] = _molecular_formula(ing)
    groups: dict[str, list[dict]] = {}
    for r in rows:
        groups.setdefault(r["label"].strip().lower(), []).append(r)

    def _verdict(group: list[dict]) -> str:
        ids = {r["identifier"] for r in group}
        if len(ids) < 2:
            return "unique"
        # A record whose own name IS the label answers it, and the sort above
        # puts it first. Without this, 97 correctly-resolved labels — `Citric
        # acid`, which CHEBI:30769 owns — would be marked untrustworthy.
        if any(r["match_type"] == "preferred_term" for r in group):
            return "resolved:owned"
        parsed = [_formula_elements(formula_of.get(i, "")) for i in sorted(ids)]
        known = {p for p in parsed if p is not None}
        if not known:
            return "unresolved:no_chemistry"
        if len(known) > 1:
            return "conflict:different_substances"
        if all(p is not None for p in parsed):
            return "agree:same_substance"
        return "unresolved:partial_chemistry"

    for _label_key, group in groups.items():
        v = _verdict(group)
        for r in group:
            r["ambiguity"] = v

    # Appended last so a consumer indexing columns positionally keeps working
    # and one reading by header name picks it up — same rule as the synonyms
    # column in #229.
    fieldnames = ["label", "match_type", "identifier", "preferred_term",
                  "ontology_id", "mapping_status", "ambiguity"]
    with open(output_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def export_to_markdown(ingredients: list[dict], output_path: Path, title: str):
    """Export ingredients to Markdown table format.

    Deliberately carries NO synonyms column, unlike the CSV and JSON exports
    (#229): the pipe-joined list would collide with the table's own cell
    separator, and this artifact is for reading rather than for resolving raw
    strings. Consumers doing lookups should use the CSV or JSON.
    """
    lines = [
        f"# {title}",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Total: {len(ingredients)} ingredients",
        "",
        "| Identifier | Ontology ID | Preferred Term | Status | Source | Quality | Occurrences |",
        "|---|---|---|---|---|---|---|",
    ]

    for ing in ingredients:
        id_val = ing.get("identifier", "")
        ont_id = _ontology_id(ing)
        term = ing.get("preferred_term", "")
        status = ing.get("mapping_status", "")

        source = ""
        quality = ""
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            source = om.get("ontology_source", "")
            quality = om.get("mapping_quality", "")

        occurrences = ""
        if ing.get("occurrence_statistics"):
            occurrences = str(ing["occurrence_statistics"].get("total_occurrences", 0))

        lines.append(f"| {id_val} | {ont_id} | {term} | {status} | {source} | {quality} | {occurrences} |")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return len(ingredients)


@click.command()
@click.option(
    "--mapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Input YAML file with mapped ingredients",
)
@click.option(
    "--unmapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Input YAML file with unmapped ingredients",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default=Path("docs/data"),
    help="Output directory for exported files",
)
@click.option(
    "--format",
    type=click.Choice(["json", "csv", "markdown", "all"]),
    default="all",
    help="Output format",
)
def main(
    mapped_input: Path,
    unmapped_input: Path,
    output_dir: Path,
    format: str,
):
    """Export lists of mapped and unmapped ingredients."""
    console.print("\n[bold]Ingredient List Exporter[/bold]")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load ingredients
    console.print(f"\nLoading mapped ingredients from {mapped_input}...")
    mapped = load_ingredients(mapped_input)
    console.print(f"  Found {len(mapped)} mapped ingredients")

    console.print(f"\nLoading unmapped ingredients from {unmapped_input}...")
    unmapped = load_ingredients(unmapped_input)
    console.print(f"  Found {len(unmapped)} unmapped ingredients")

    all_ingredients = mapped + unmapped
    console.print(f"\n[bold]Total: {len(all_ingredients)} ingredients[/bold]")

    # Export in requested formats
    formats_to_export = ["json", "csv", "markdown"] if format == "all" else [format]

    for fmt in formats_to_export:
        console.print(f"\n[cyan]Exporting {fmt.upper()} files...[/cyan]")

        if fmt == "json":
            # Mapped JSON
            mapped_json = output_dir / "mapped_ingredients.json"
            count = export_to_json(mapped, mapped_json)
            console.print(f"  ✓ {mapped_json} ({count} records)")

            # Unmapped JSON
            unmapped_json = output_dir / "unmapped_ingredients.json"
            count = export_to_json(unmapped, unmapped_json)
            console.print(f"  ✓ {unmapped_json} ({count} records)")

            # All JSON
            all_json = output_dir / "all_ingredients.json"
            count = export_to_json(all_ingredients, all_json)
            console.print(f"  ✓ {all_json} ({count} records)")

        elif fmt == "csv":
            # Mapped CSV
            mapped_csv = output_dir / "mapped_ingredients.csv"
            count = export_to_csv(mapped, mapped_csv)
            console.print(f"  ✓ {mapped_csv} ({count} records)")

            # Unmapped CSV
            unmapped_csv = output_dir / "unmapped_ingredients.csv"
            count = export_to_csv(unmapped, unmapped_csv)
            console.print(f"  ✓ {unmapped_csv} ({count} records)")

            # All CSV
            all_csv = output_dir / "all_ingredients.csv"
            count = export_to_csv(all_ingredients, all_csv)
            console.print(f"  ✓ {all_csv} ({count} records)")

            # per-LABEL resolution with explicit precedence (#232)
            label_csv = output_dir / "label_index.csv"
            count = export_label_index(all_ingredients, label_csv)
            console.print(f"  ✓ {label_csv} ({count} labels)")

        elif fmt == "markdown":
            # Mapped MD
            mapped_md = output_dir / "mapped_ingredients.md"
            count = export_to_markdown(mapped, mapped_md, "Mapped Ingredients")
            console.print(f"  ✓ {mapped_md} ({count} records)")

            # Unmapped MD
            unmapped_md = output_dir / "unmapped_ingredients.md"
            count = export_to_markdown(unmapped, unmapped_md, "Unmapped Ingredients")
            console.print(f"  ✓ {unmapped_md} ({count} records)")

            # All MD
            all_md = output_dir / "all_ingredients.md"
            count = export_to_markdown(all_ingredients, all_md, "All Ingredients")
            console.print(f"  ✓ {all_md} ({count} records)")

    # Summary
    console.print("\n[bold green]✅ Export complete![/bold green]")
    console.print(f"\nFiles saved to: {output_dir}")

    # Show sample
    console.print("\n[bold]Sample Records:[/bold]")
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Identifier", style="yellow")
    table.add_column("Ontology ID", style="green")
    table.add_column("Preferred Term", style="white")
    table.add_column("Status", style="magenta")

    for ing in all_ingredients[:5]:
        table.add_row(
            ing.get("identifier", "")[:25],
            _ontology_id(ing)[:25],
            ing.get("preferred_term", "")[:40],
            ing.get("mapping_status", ""),
        )

    console.print(table)
    console.print(f"\n... and {len(all_ingredients) - 5} more")


if __name__ == "__main__":
    main()
