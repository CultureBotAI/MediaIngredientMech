#!/usr/bin/env python3
"""Export collection YAML files to individual ingredient records.

This script transforms the collection-based YAML files into individual YAML files
following the DisMech methodology: one file per ingredient with sanitized filenames
based on the preferred_term.

Usage:
    python scripts/export_individual_records.py
    python scripts/export_individual_records.py --input-dir data/curated --output-dir data/ingredients
    python scripts/export_individual_records.py --dry-run
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# Ensure the src package is importable when running the script directly
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.utils.yaml_handler import load_yaml, save_yaml

console = Console()

# Fields authored directly on the per-record files and never carried in the
# curated collection. The collection is the export source, so a naive
# collection->per-record projection silently wipes these. `discussions` is
# written into per-record files by culturebotai-claw's kgscan tool (see
# `just gen-discussions-data`), not by the MIM curator, and has never been
# aggregated back into data/curated/. Preserve it across a round-trip.
PER_RECORD_AUTHORED_FIELDS: tuple[str, ...] = ("discussions",)


@dataclass
class PreservedFields:
    """Per-record-authored fields recovered from disk, looked up by a move-stable key.

    Two indexes, because neither key is stable across every move:
    * `by_identifier` — survives a display-name normalisation when the semantic
      identifier is unique among records (identifier stable,
      filename/preferred_term change). Shared identifiers are deliberately not
      indexed because they cannot address one sibling safely.
    * `by_preferred_term` — survives an identifier change (promotion
      UNMAPPED_NNNN->CHEBI:x, demotion, or a CHEBI remap), where the semantic
      identity is exactly what moves. Only unambiguous terms are indexed; a
      preferred_term shared by more than one record is dropped rather than risk
      attributing a discussion to the wrong record.
    """

    by_identifier: dict[str, dict] = field(default_factory=dict)
    by_preferred_term: dict[str, dict] = field(default_factory=dict)

    def for_record(self, record: dict) -> dict:
        """Authored fields to merge into `record`, or {} if none. Identifier first."""
        ident = record.get("identifier")
        if ident and ident in self.by_identifier:
            return self.by_identifier[ident]
        term = record.get("preferred_term")
        if term and term in self.by_preferred_term:
            return self.by_preferred_term[term]
        return {}


def collect_preserved_fields(ingredients_root: Path) -> PreservedFields:
    """Index per-record-authored fields before files are cleared.

    Scans the whole `data/ingredients/` tree (both mapped/ and unmapped/) so a
    record that moves between them still keeps its authored fields. Indexed by
    both `identifier` and `preferred_term` — see `PreservedFields`. The semantic
    identifier changes on promotion/remap and may also be shared by reviewed
    sibling records, so neither field is an unconditional document key.

    Rebuilt from current disk state each run, so an edit that removes a
    discussion survives (it is simply absent from the index), while an export
    that would otherwise drop it does not.
    """
    result = PreservedFields()
    if not ingredients_root.exists():
        return result
    seen_identifiers: set[str] = set()
    identifier_collisions: set[str] = set()
    seen_terms: set[str] = set()
    term_collisions: set[str] = set()
    for path in ingredients_root.rglob("*.yaml"):
        try:
            record = load_yaml(path)
        except Exception:
            continue
        if not isinstance(record, dict):
            continue
        authored = {
            fname: record[fname] for fname in PER_RECORD_AUTHORED_FIELDS if record.get(fname)
        }
        ident = record.get("identifier")
        if ident:
            if ident in seen_identifiers:
                result.by_identifier.pop(ident, None)
                identifier_collisions.add(ident)
            else:
                seen_identifiers.add(ident)
                if authored:
                    result.by_identifier[ident] = authored
        term = record.get("preferred_term")
        if term:
            # Two records sharing a term make term-based lookup ambiguous,
            # even if only one currently carries an authored field.
            if term in seen_terms:
                result.by_preferred_term.pop(term, None)
                term_collisions.add(term)
            else:
                seen_terms.add(term)
                if authored:
                    result.by_preferred_term[term] = authored
    return result


@dataclass
class FilenameIndex:
    """Existing per-record filename stems, so an export never renames a record.

    The filename is otherwise re-derived from `preferred_term` on every run, which
    makes the naming rule retroactive: any change to `sanitize_filename` silently
    renames the whole corpus, and every `MIM:<stem>` SSSOM subject derived from a
    filename goes with it. The committed corpus was in fact written by more than
    one historical rule, so no single rule reproduces it — reusing the name a
    record already has is the only stable answer.

    Indexed by both keys for the same reason as `PreservedFields`: `identifier`
    survives a display-name change, `preferred_term` survives an identifier change
    (promotion UNMAPPED_NNNN->CHEBI:x, demotion, remap).
    """

    by_identifier: dict[str, str] = field(default_factory=dict)
    by_preferred_term: dict[str, str] = field(default_factory=dict)

    def for_record(self, record: dict) -> str | None:
        """The stem this record already uses, or None if it is new."""
        ident = record.get("identifier")
        if ident and ident in self.by_identifier:
            return self.by_identifier[ident]
        term = record.get("preferred_term")
        if term and term in self.by_preferred_term:
            return self.by_preferred_term[term]
        return None


def collect_existing_filenames(ingredients_root: Path) -> FilenameIndex:
    """Index current filename stems before files are cleared.

    Scans the whole tree (mapped/ and unmapped/) so a record that moves between
    them keeps its name — a promotion should not also re-slug the file.
    """
    result = FilenameIndex()
    if not ingredients_root.exists():
        return result
    term_collisions: set[str] = set()
    for path in ingredients_root.rglob("*.yaml"):
        try:
            record = load_yaml(path)
        except Exception:
            continue
        if not isinstance(record, dict):
            continue
        stem = path.stem
        ident = record.get("identifier")
        if ident:
            # A duplicate identifier cannot pick a single name; leave those
            # records to the term index or to sanitize_filename.
            if ident in result.by_identifier:
                result.by_identifier.pop(ident, None)
                term_collisions.add(f"\0ident\0{ident}")
            elif f"\0ident\0{ident}" not in term_collisions:
                result.by_identifier[ident] = stem
        term = record.get("preferred_term")
        if term:
            if term in result.by_preferred_term or term in term_collisions:
                result.by_preferred_term.pop(term, None)
                term_collisions.add(term)
            else:
                result.by_preferred_term[term] = stem
    return result


def assert_unambiguous_record_moves(
    ingredients: list[dict],
    existing_names: FilenameIndex,
    shared_identifiers: set[str] | None = None,
) -> None:
    """Reject incoming records whose two continuity keys name different files.

    A unique semantic identifier and a unique preferred term are both useful
    continuity hints, but neither is an unconditional document key. If they
    resolve to different old records, choosing either would silently move the
    wrong filename and per-record-authored fields onto the incoming record. A
    typical ambiguous shape is an incoming remap to an identifier whose former
    holder was retired in the same export.

    Shared incoming identifiers are excluded: identifier lookup is deliberately
    disabled for those records and the unambiguous preferred term is the only
    continuity hint. All other two-key conflicts must be curated explicitly.
    """
    shared_identifiers = set(shared_identifiers or ())
    conflicts: list[str] = []
    for ingredient in ingredients:
        ident = ingredient.get("identifier")
        term = ingredient.get("preferred_term")
        if not ident or not term or ident in shared_identifiers:
            continue
        identifier_stem = existing_names.by_identifier.get(ident)
        term_stem = existing_names.by_preferred_term.get(term)
        if (
            identifier_stem is not None
            and term_stem is not None
            and identifier_stem.casefold() != term_stem.casefold()
        ):
            conflicts.append(
                f"{term!r} ({ident}): identifier -> {identifier_stem}.yaml; "
                f"preferred_term -> {term_stem}.yaml"
            )

    if conflicts:
        details = "\n".join(f"  - {conflict}" for conflict in conflicts)
        raise click.ClickException(
            "Incoming records conflict with existing record keys. Refusing to "
            "clear per-record files because filename/authored-field continuity "
            f"is ambiguous:\n{details}"
        )


def sanitize_filename(preferred_term: str) -> str:
    """Convert preferred term to a safe filename.

    Examples:
        "sodium chloride" -> "Sodium_chloride"
        "D-glucose" -> "D-glucose"
        "NaCl (99%)" -> "NaCl_99"
        "(-)-Epinephrine" -> "Epinephrine"
        "(R)-3-hydroxybutyrate" -> "R-3-hydroxybutyrate"
        "H₂O" -> "H2O"

    Args:
        preferred_term: The preferred term to sanitize.

    Returns:
        Sanitized filename (without .yaml extension).
    """
    # Replace spaces with underscores
    name = preferred_term.replace(" ", "_")

    # Remove parentheses and their contents but preserve what's inside
    name = re.sub(r"\(([^)]*)\)", r"_\1", name)

    # Remove special characters but keep hyphens and underscores
    name = re.sub(r"[^\w\-]", "", name)

    # Collapse repeated underscores/hyphens left by stripped punctuation
    name = re.sub(r"_+", "_", name)
    name = re.sub(r"-+", "-", name)

    # Remove leading/trailing underscores and hyphens (e.g. from a leading
    # "(-)-"/"(R)-" stereodescriptor) so filenames don't start with a dash
    name = name.strip("_-")

    # Uppercase the leading character only. str.capitalize() would lowercase
    # everything after it, which destroys chemical casing that carries meaning
    # here (NaCl, KI, TAPSO, MnCl2 -> Nacl, Ki, Tapso, Mncl2).
    if name:
        name = name[0].upper() + name[1:]

    # Ensure we have a valid name
    if not name:
        name = "Unnamed"

    return name


def export_collection_to_individual_files(
    collection_path: Path,
    output_dir: Path,
    dry_run: bool = False,
    preserved: PreservedFields | None = None,
    existing_names: FilenameIndex | None = None,
    shared_identifiers: set[str] | None = None,
) -> dict[str, int]:
    """Export a collection YAML file to individual ingredient files.

    Args:
        collection_path: Path to the collection YAML file.
        output_dir: Directory to write individual files.
        dry_run: If True, only show what would be done.
        preserved: Per-record-authored fields (from ``collect_preserved_fields``),
            merged into records whose collection copy lacks them. Pass None to
            skip preservation.
        existing_names: Filename stems already in use (from
            ``collect_existing_filenames``), so records keep the names they have.
            Pass None to name every record from scratch.
        shared_identifiers: Semantic identifiers known to be shared across the
            full incoming export. Identifier-keyed preservation and filename
            lookup are disabled for these values.

    Returns:
        Dictionary with statistics: 'total', 'created', 'collisions', 'renamed'.
    """
    preserved = preserved or PreservedFields()
    existing_names = existing_names or FilenameIndex()
    stats = {"total": 0, "created": 0, "collisions": 0, "renamed": 0}

    # Load collection
    try:
        collection = load_yaml(collection_path)
    except Exception as e:
        console.print(f"[red]Error loading {collection_path}: {e}[/red]")
        return stats

    ingredients = collection.get("ingredients", [])
    if not ingredients:
        console.print(f"[yellow]No ingredients found in {collection_path}[/yellow]")
        return stats

    stats["total"] = len(ingredients)

    # Identifiers held by more than one record in *this collection*. A merge
    # tombstone deliberately keeps its winner's identifier, so `by_identifier`
    # would hand both records the same stable filename and the second would
    # overwrite the first. `collect_existing_filenames` drops such identifiers,
    # but only when both files are still on disk — once one has been lost the
    # index can no longer see the duplicate and the loss is self-perpetuating.
    # Deciding it from the collection instead is stable across runs.
    ident_counts: Counter[str] = Counter(
        str(i.get("identifier")) for i in ingredients if i.get("identifier")
    )
    shared_identifiers = set(shared_identifiers or ()) | {
        key for key, count in ident_counts.items() if count > 1
    }

    # Both continuity hints are safe only when they resolve to the same old
    # record. Run this before clearing anything so an ambiguous remap fails
    # closed and leaves the per-record tree untouched.
    assert_unambiguous_record_moves(
        ingredients, existing_names, shared_identifiers=shared_identifiers
    )

    # Create output directory and clear any stale per-record files, so
    # deletions/renames in the source propagate (otherwise a removed record's
    # file lingers forever). The corpus is *almost* a pure projection of the
    # collection — the exception is the per-record-authored fields captured in
    # `preserved` above, which are merged back after this clear.
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        for stale in output_dir.glob("*.yaml"):
            stale.unlink()

    # Names already claimed in this directory, so a reused name and a freshly
    # derived one cannot land on the same file. Compared case-INSENSITIVELY:
    # `Sodium_Tartrate` and `Sodium_tartrate` are distinct Python strings but the
    # same file on a case-insensitive filesystem, so a case-sensitive set lets
    # the second record silently overwrite the first (cf. #299).
    taken: set[str] = set()

    for ingredient in ingredients:
        preferred_term = ingredient.get("preferred_term", "Unknown")

        # Keep the name this record already has. Re-deriving it from
        # preferred_term on every run is what makes the naming rule retroactive
        # and renames the corpus behind git's back on a case-insensitive
        # filesystem. Only genuinely new records get a name from scratch.
        stable = existing_names.for_record(ingredient)
        if ingredient.get("identifier") in shared_identifiers:
            # Fall back to the term index / a derived name; the identifier
            # cannot pick between the records that share it.
            stable = existing_names.by_preferred_term.get(preferred_term)
        if stable is not None and stable.lower() not in taken:
            filename = stable
        else:
            base_filename = sanitize_filename(preferred_term)
            filename = base_filename
            suffix = 1
            while filename.lower() in taken:
                suffix += 1
                filename = f"{base_filename}_{suffix}"
            if suffix > 1:
                stats["collisions"] += 1
                console.print(
                    f"[yellow]Collision detected: {preferred_term} -> {filename}.yaml[/yellow]"
                )
            if stable is not None and stable != filename:
                stats["renamed"] += 1
                console.print(
                    f"[yellow]Renamed: {stable}.yaml -> {filename}.yaml "
                    f"({preferred_term})[/yellow]"
                )

        taken.add(filename.lower())
        output_path = output_dir / f"{filename}.yaml"

        # Re-attach per-record-authored fields (e.g. discussions) that the
        # collection does not carry, so export does not wipe them. Only fill
        # gaps — a value present in the collection wins.
        authored = preserved.for_record(ingredient)
        if ingredient.get("identifier") in shared_identifiers:
            # The incoming collection can introduce a new shared identifier
            # that the old per-record tree could not know was ambiguous. Fall
            # back to the unambiguous term or preserve nothing; never graft one
            # sibling's authored fields onto another.
            authored = preserved.by_preferred_term.get(preferred_term, {})
        for fname, value in authored.items():
            if not ingredient.get(fname):
                ingredient[fname] = value

        if dry_run:
            console.print(f"[dim]Would create: {output_path}[/dim]")
        else:
            # Write individual file (no collection wrapper, just the IngredientRecord)
            save_yaml(ingredient, output_path, backup=False)
            stats["created"] += 1

    return stats


@click.command()
@click.option(
    "--input-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory containing collection YAML files (default: data/curated/)",
)
@click.option(
    "--output-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory to write individual files (default: data/ingredients/)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be done without creating files",
)
def main(input_dir: str | None, output_dir: str | None, dry_run: bool):
    """Export collection YAML files to individual ingredient records."""
    # Set default paths
    if input_dir is None:
        input_dir_path = _project_root / "data" / "curated"
    else:
        input_dir_path = Path(input_dir)

    if output_dir is None:
        output_dir_path = _project_root / "data" / "ingredients"
    else:
        output_dir_path = Path(output_dir)

    if not input_dir_path.exists():
        console.print(f"[red]Input directory not found: {input_dir_path}[/red]")
        sys.exit(1)

    # Find collection files
    mapped_file = input_dir_path / "mapped_ingredients.yaml"
    unmapped_file = input_dir_path / "unmapped_ingredients.yaml"

    collection_files = []
    if mapped_file.exists():
        collection_files.append(("mapped", mapped_file))
    if unmapped_file.exists():
        collection_files.append(("unmapped", unmapped_file))

    if not collection_files:
        console.print(f"[yellow]No collection files found in {input_dir_path}[/yellow]")
        console.print(
            "[yellow]Expected: mapped_ingredients.yaml, unmapped_ingredients.yaml[/yellow]"
        )
        sys.exit(0)

    # Header
    mode = "[yellow]DRY RUN MODE[/yellow]" if dry_run else ""
    console.print(f"\n[bold]Export Individual Ingredient Records {mode}[/bold]")
    console.print(f"Input:  {input_dir_path}")
    console.print(f"Output: {output_dir_path}\n")

    # Index per-record-authored fields BEFORE the per-category clear loop wipes
    # any files (a record may move mapped<->unmapped, so scan the whole tree).
    preserved = collect_preserved_fields(output_dir_path)
    n_preserved = len(preserved.by_identifier)
    if n_preserved:
        console.print(
            f"[dim]Preserving per-record fields "
            f"({', '.join(PER_RECORD_AUTHORED_FIELDS)}) for {n_preserved} record(s)[/dim]"
        )

    # Index current filenames BEFORE the clear loop, for the same reason and
    # over the same whole tree.
    existing_names = collect_existing_filenames(output_dir_path)

    # Ambiguity must be decided from the entire incoming export, not only one
    # old directory or one collection partition. A promotion/remap can create a
    # shared identifier that neither on-disk index could see beforehand.
    incoming_identifier_counts: Counter[str] = Counter()
    incoming_records: list[dict] = []
    for _, collection_file in collection_files:
        incoming = load_yaml(collection_file)
        records = incoming.get("ingredients", [])
        incoming_records.extend(records)
        incoming_identifier_counts.update(
            str(record.get("identifier")) for record in records if record.get("identifier")
        )
    incoming_shared_identifiers = {
        key for key, count in incoming_identifier_counts.items() if count > 1
    }

    # Validate the whole mapped+unmapped export before either output directory
    # is cleared. Otherwise a conflict found in the second collection could
    # leave the first collection partially rewritten.
    assert_unambiguous_record_moves(
        incoming_records,
        existing_names,
        shared_identifiers=incoming_shared_identifiers,
    )

    # Process each collection
    total_stats = {"total": 0, "created": 0, "collisions": 0, "renamed": 0}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for category, collection_file in collection_files:
            task = progress.add_task(f"Processing {category}...", total=None)

            output_subdir = output_dir_path / category
            stats = export_collection_to_individual_files(
                collection_file,
                output_subdir,
                dry_run=dry_run,
                preserved=preserved,
                existing_names=existing_names,
                shared_identifiers=incoming_shared_identifiers,
            )

            total_stats["total"] += stats["total"]
            total_stats["created"] += stats["created"]
            total_stats["collisions"] += stats["collisions"]
            total_stats["renamed"] += stats["renamed"]

            progress.update(
                task,
                description=f"[green]{category}: {stats['created']}/{stats['total']} files[/green]",
            )

    # Summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Total ingredients: {total_stats['total']}")
    if dry_run:
        console.print(f"  Would create: {total_stats['created']} files")
    else:
        console.print(f"  Created: {total_stats['created']} files")

    if total_stats["collisions"] > 0:
        console.print(f"  [yellow]Filename collisions: {total_stats['collisions']}[/yellow]")

    if total_stats["renamed"] > 0:
        console.print(f"  [yellow]Renamed: {total_stats['renamed']}[/yellow]")

    if not dry_run:
        console.print(f"\n[green]Individual files written to: {output_dir_path}[/green]")
        console.print(f"  - Mapped: {output_dir_path / 'mapped'}")
        console.print(f"  - Unmapped: {output_dir_path / 'unmapped'}")

    sys.exit(0)


if __name__ == "__main__":
    main()
