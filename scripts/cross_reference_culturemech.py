#!/usr/bin/env python3
"""Cross-reference MediaIngredientMech entries with CultureMech media recipes.

This script searches CultureMech for media recipes that match ingredient names,
particularly useful for identifying defined media entries that should link to
their full recipe formulations.

Usage:
    python scripts/cross_reference_culturemech.py --complex-media-only
    python scripts/cross_reference_culturemech.py --ingredient "R2A agar"
    python scripts/cross_reference_culturemech.py --update-links
"""

import argparse
import csv
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

console = Console()


class CultureMechMatcher:
    """Match MediaIngredientMech entries to CultureMech media."""

    def __init__(self, culturemech_path: Path):
        """
        Args:
            culturemech_path: CultureMech `data/normalized_yaml/` recipe tree.
        """
        self.culturemech_path = culturemech_path
        self.media_by_id: dict[str, dict] = {}
        self.media_by_name: dict[str, list[dict]] = {}
        self._load_culturemech()

    def provenance(self) -> str:
        """Which CultureMech tree produced these candidates (#491, cf. #486).

        Ids are stable but the SET of recipes is not, so a candidate list read
        later cannot be checked against the tree that produced it without this.
        """
        sha = "unknown"
        try:
            result = subprocess.run(
                ["git", "-C", str(self.culturemech_path), "rev-parse", "--short", "HEAD"],
                capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                sha = result.stdout.strip() or "unknown"
        except (OSError, subprocess.SubprocessError):
            pass
        shared = sum(1 for v in self.media_by_name.values() if len(v) > 1)
        return (f"source=normalized_yaml culturemech_rev={sha} "
                f"recipes={len(self.media_by_id)} "
                f"distinct_names={len(self.media_by_name)} shared_names={shared}")

    def _load_culturemech(self) -> None:
        """Index the recipe tree by stable id, and by name MULTI-VALUED.

        Fails closed. The previous version warned and returned on a missing
        source, leaving an empty index, so every lookup returned "no match" --
        indistinguishable from "the source could not be read". Its default path
        (`../CultureMech/output/media.yaml`) did not exist, so that was the
        normal case, not an edge one (#447, and the same shape as CultureMech#339).

        The name index maps to a LIST because CultureMech names are not unique:
        2291 names are shared by more than one recipe (`defined_freshwater_medium_cocl2`
        names 29) and 4784 recipes have no name at all. A one-value dict silently
        dropped 3190 recipes, keeping whichever happened to be indexed last.
        """
        if not self.culturemech_path.exists():
            raise SystemExit(
                f"error: CultureMech recipe tree not found at {self.culturemech_path}. "
                "Nothing was read. Pass --culturemech-path pointing at CultureMech's "
                "data/normalized_yaml/ directory."
            )

        for path in sorted(self.culturemech_path.rglob("*.yaml")):
            try:
                recipe = yaml.safe_load(path.read_text(encoding="utf-8"))
            except yaml.YAMLError:
                continue
            if not isinstance(recipe, dict):
                continue
            medium_id = str(recipe.get("id") or "").strip()
            if not medium_id.startswith("CultureMech:"):
                continue  # only stable-id-bearing recipes can be linked to
            recipe["_source_path"] = str(path.relative_to(self.culturemech_path.parent.parent))
            self.media_by_id[medium_id] = recipe
            name = str(recipe.get("name") or "").lower().strip()
            if name:
                self.media_by_name.setdefault(name, []).append(recipe)

        if not self.media_by_id:
            raise SystemExit(
                f"error: no recipes carrying a CultureMech: id found under "
                f"{self.culturemech_path}. Refusing to report 'no matches' from an "
                "empty index."
            )

        shared = sum(1 for v in self.media_by_name.values() if len(v) > 1)
        console.print(
            f"[green]Indexed {len(self.media_by_id)} recipes by stable id "
            f"({len(self.media_by_name)} distinct names, {shared} shared by more "
            f"than one recipe)[/green]"
        )

    def find_medium_matches(self, ingredient_name: str) -> list[dict[str, Any]]:
        """CANDIDATES for a name, never accepted links.

        Every result is a proposal for a curator. Name agreement is not evidence
        of recipe identity -- both existing links in the corpus were verified by
        composition, and the one whose names matched exactly (`GYPS` /
        `gyps_medium`) turned out NOT to be the same formulation. So this returns
        candidates and the caller may not promote them on its own; see
        `report_candidates`.

        Every candidate carries the stable `CultureMech:` id, because a name
        cannot identify a recipe: 2291 names are shared, and the worst names 29
        distinct recipes.
        """
        matches: list[dict[str, Any]] = []
        search_name = ingredient_name.lower().strip()
        if not search_name:
            return []

        def add(recipes: list[dict], match_type: str, confidence: float) -> None:
            for recipe in recipes:
                matches.append({
                    "medium": recipe,
                    "medium_id": recipe.get("id"),
                    "match_type": match_type,
                    "confidence": confidence,
                })

        # Exact name. Still only a candidate, and still possibly several recipes.
        if search_name in self.media_by_name:
            add(self.media_by_name[search_name], "exact_name", 1.0)
            return matches

        for name, recipes in self.media_by_name.items():
            if search_name in name:
                add(recipes, "contains", 0.8)
            elif name in search_name:
                add(recipes, "contained_by", 0.7)

        if not matches:
            search_tokens = set(search_name.split())
            for name, recipes in self.media_by_name.items():
                name_tokens = set(name.split())
                overlap = search_tokens & name_tokens
                if len(overlap) >= 2:
                    add(recipes, "fuzzy",
                        len(overlap) / max(len(search_tokens), len(name_tokens)))

        matches.sort(key=lambda x: (-x["confidence"], str(x["medium_id"])))
        return matches

    def get_medium_ingredients(self, medium: dict) -> list[str]:
        """Extract ingredient list from a CultureMech medium record.

        Args:
            medium: CultureMech medium record.

        Returns:
            List of ingredient names.
        """
        ingredients = []

        # Get ingredients from components
        for component in medium.get("components", []):
            ing_name = component.get("ingredient_name", "")
            if ing_name:
                ingredients.append(ing_name)

        return ingredients


def cross_reference_all(
    curator: IngredientCurator,
    matcher: CultureMechMatcher,
    complex_media_only: bool = True
) -> dict[int, list[dict]]:
    """Cross-reference all ingredients with CultureMech.

    Args:
        curator: IngredientCurator instance.
        matcher: CultureMechMatcher instance.
        complex_media_only: If True, only check NAMED_MEDIUM entries.

    Returns:
        Dict mapping ingredient index to list of CultureMech matches.
    """
    results = {}

    for idx, record in enumerate(curator.records):
        # Skip rejected
        if record.get("mapping_status") == "REJECTED":
            continue

        # Filter by type if requested
        if complex_media_only and record.get("ingredient_type") not in WHOLE_MEDIUM_TYPES:
            continue

        ingredient_name = record.get("preferred_term", "")
        matches = matcher.find_medium_matches(ingredient_name)

        if matches:
            results[idx] = matches

    return results


def display_cross_reference_results(
    curator: IngredientCurator,
    results: dict[int, list[dict]],
    matcher: CultureMechMatcher,
    max_display: int = 50
) -> None:
    """Display cross-reference results.

    Args:
        curator: IngredientCurator instance.
        results: Cross-reference results.
        matcher: CultureMechMatcher instance.
        max_display: Maximum number of results to display.
    """
    console.print(f"\n[bold]Cross-Reference Results[/bold]")
    console.print(f"Found CultureMech matches for {len(results)} ingredients\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("MediaIngredientMech", style="green", width=40)
    table.add_column("CultureMech Medium", style="cyan", width=40)
    table.add_column("Match", style="yellow")
    table.add_column("Ingredients", justify="right")

    count = 0
    for idx in sorted(results.keys()):
        if count >= max_display:
            break

        record = curator.records[idx]
        ingredient_name = record.get("preferred_term", "")

        # Show best match
        best_match = results[idx][0]
        medium = best_match["medium"]
        medium_name = medium.get("name", "N/A")
        match_type = best_match["match_type"]
        confidence = best_match["confidence"]

        # Get ingredient count
        ingredients = matcher.get_medium_ingredients(medium)
        ing_count = len(ingredients)

        table.add_row(
            ingredient_name,
            medium_name,
            f"{match_type} ({confidence:.2f})",
            str(ing_count) if ing_count > 0 else "N/A"
        )

        count += 1

    console.print(table)

    if len(results) > max_display:
        console.print(f"\n[dim]... and {len(results) - max_display} more matches[/dim]")


def display_medium_details(medium: dict, matcher: CultureMechMatcher) -> None:
    """Display detailed information about a CultureMech medium.

    Args:
        medium: CultureMech medium record.
        matcher: CultureMechMatcher instance.
    """
    medium_name = medium.get("medium_name", "Unknown")
    medium_id = medium.get("medium_id", "N/A")

    ingredients = matcher.get_medium_ingredients(medium)

    panel_content = f"[bold]Medium ID:[/bold] {medium_id}\n\n"
    panel_content += f"[bold]Ingredients ({len(ingredients)}):[/bold]\n"

    if ingredients:
        for ing in ingredients[:20]:  # Show first 20
            panel_content += f"  • {ing}\n"
        if len(ingredients) > 20:
            panel_content += f"  ... and {len(ingredients) - 20} more\n"
    else:
        panel_content += "  [dim]No ingredients listed[/dim]\n"

    console.print(Panel(panel_content, title=medium_name, border_style="cyan"))


# A record can be a whole named medium AND compositionally undefined, and
# IngredientTypeEnum makes it pick one (#478). BHI -- a named medium and one of
# only two records carrying a CultureMech link -- is filed UNDEFINED_MIXTURE,
# its own note saying "state no composition to split on". Filtering on
# NAMED_MEDIUM alone therefore excluded 100% of the records that actually have a
# link, and the run returned a clean, confident 0 candidates (#490).
WHOLE_MEDIUM_TYPES = frozenset({"NAMED_MEDIUM", "UNDEFINED_MIXTURE"})

CANDIDATE_REPORT = Path("reports/culturemech_link_candidates.tsv")


def report_candidates(
    curator: IngredientCurator,
    results: dict[int, list[dict]],
    confidence_threshold: float = 0.8,
    provenance: str = "",
) -> int:
    """Write candidates for curator review. Writes NO links into any record.

    This replaces `update_culturemech_links`, which took `matches[0]` -- possibly
    a substring or two-token-overlap match -- and stored it as an accepted link
    keyed on a display name. Three things were wrong with that, and only the
    third is fixed by storing an id instead:

      1. a name match is not evidence of recipe identity. `GYPS` and
         `gyps_medium` match exactly and are NOT the same formulation;
      2. a confidence threshold cannot separate "right" from "plausible" here --
         `contains` scored 0.8 and cleared the default threshold;
      3. the stored value could not identify a recipe at all.

    So acceptance is a curator's act. The tool proposes; a human writes the
    `culturemech_reference` with a relationship and evidence. Ambiguous
    candidates -- PYG matches six CultureMech variants -- are reported as
    ambiguous and stay unlinked, which is the required behaviour, not a
    limitation.
    """
    CANDIDATE_REPORT.parent.mkdir(parents=True, exist_ok=True)
    rows = 0
    with CANDIDATE_REPORT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        if provenance:
            writer.writerow([f"# {provenance}"])
        writer.writerow([
            "mim_identifier", "preferred_term", "candidate_count", "ambiguous",
            "candidate_medium_id", "candidate_medium_name", "match_type",
            "confidence", "source_path",
        ])
        for idx, matches in sorted(results.items()):
            record = curator.records[idx]
            keep = [m for m in matches if m["confidence"] >= confidence_threshold]
            if not keep:
                continue
            ambiguous = "YES" if len(keep) > 1 else "no"
            for match in keep:
                medium = match["medium"]
                writer.writerow([
                    record.get("identifier", ""), record.get("preferred_term", ""),
                    len(keep), ambiguous, match.get("medium_id", ""),
                    medium.get("name", ""), match["match_type"],
                    f"{match['confidence']:.2f}", medium.get("_source_path", ""),
                ])
                rows += 1

    console.print(
        f"[bold]{rows} candidate row(s) written to {CANDIDATE_REPORT}[/bold]\n"
        "No record was modified. A candidate becomes a link only when a curator "
        "adds `culturemech_reference` with a relationship and the evidence for it."
    )
    return rows


def main():
    """Main workflow."""
    parser = argparse.ArgumentParser(
        description="Cross-reference MediaIngredientMech with CultureMech"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/mapped_ingredients.yaml"),
        help="Path to MediaIngredientMech data file",
    )
    parser.add_argument(
        "--culturemech-path",
        type=Path,
        default=Path("../CultureMech/data/normalized_yaml"),
        help="Path to CultureMech media file",
    )
    parser.add_argument(
        "--complex-media-only",
        action="store_true",
        help="Only search for NAMED_MEDIUM entries",
    )
    parser.add_argument(
        "--ingredient",
        type=str,
        help="Search for specific ingredient name",
    )
    parser.add_argument(
        "--report-candidates",
        action="store_true",
        help="Write a curator-review candidate report. Never writes links (#447)",
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.8,
        help="Minimum confidence for a candidate to be reported (default: 0.8)",
    )
    parser.add_argument(
        "--show-details",
        action="store_true",
        help="Show detailed medium information",
    )

    args = parser.parse_args()

    # Load MediaIngredientMech
    console.print(f"\n[bold]Loading MediaIngredientMech from {args.data_path}[/bold]")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()
    console.print(f"Loaded {len(curator.records)} ingredient records\n")

    # Load CultureMech
    console.print(f"[bold]Loading CultureMech from {args.culturemech_path}[/bold]")
    matcher = CultureMechMatcher(args.culturemech_path)

    if not matcher.media_by_name:
        console.print("[red]No CultureMech data loaded. Exiting.[/red]")
        return 1

    # Single ingredient search
    if args.ingredient:
        console.print(f"\n[bold]Searching for: {args.ingredient}[/bold]\n")
        matches = matcher.find_medium_matches(args.ingredient)

        if matches:
            console.print(f"Found {len(matches)} matches:\n")
            for match in matches:
                medium = match["medium"]
                medium_name = medium.get("medium_name", "N/A")
                console.print(
                    f"  • {medium_name} ({match['match_type']}, "
                    f"confidence: {match['confidence']:.2f})"
                )

                if args.show_details:
                    console.print()
                    display_medium_details(medium, matcher)
                    console.print()
        else:
            console.print("[yellow]No matches found[/yellow]")

        return 0

    # Cross-reference all
    console.print("\n[bold cyan]Cross-referencing all ingredients...[/bold cyan]")
    results = cross_reference_all(curator, matcher, args.complex_media_only)

    # Display results
    display_cross_reference_results(curator, results, matcher)

    # Candidates for review. This tool no longer writes links (#447): acceptance
    # requires a relationship and evidence, which is a curator's judgement.
    if args.report_candidates:
        console.print(f"\n[bold]Collecting candidates (threshold: {args.confidence_threshold})[/bold]")
        report_candidates(curator, results, args.confidence_threshold,
                          provenance=matcher.provenance())

    return 0


if __name__ == "__main__":
    sys.exit(main())
