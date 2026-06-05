#!/usr/bin/env python3
"""Generate interactive UMAP visualization of media ingredient embedding space."""

import gzip
import hashlib
import json
import os
import pickle
import sys
from pathlib import Path
from typing import Dict, List, Any

import click
import numpy as np
import pandas as pd
import umap
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# Ensure the src package is importable
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.utils.yaml_handler import load_yaml

console = Console()

# Latest canonical kg-microbe deepwalk artifact, shared across all Mech repos.
# Resolution order:
#   1. ``KG_MICROBE_EMBEDDINGS`` env var (absolute path or repo-rooted)
#   2. ``data/embeddings/<filename>`` next to this script's repo
#   3. ``../CommunityMech/CommunityMech/data/embeddings/<filename>`` —
#      the 5.7 GB artifact is only vendored once per developer machine.
# All three locations are resolved relative to the script so the file works
# on any machine that has the Mech repos checked out as siblings.
_EMBEDDINGS_FILENAME = "DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v2_2026-05-26_00_56_15.tsv.gz"
_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_EMBEDDINGS = _REPO_ROOT / "data" / "embeddings" / _EMBEDDINGS_FILENAME
_COMMUNITYMECH_EMBEDDINGS = (
    _REPO_ROOT.parent / "CommunityMech" / "CommunityMech"
    / "data" / "embeddings" / _EMBEDDINGS_FILENAME
)


def _resolve_default_embeddings() -> str:
    """Return the first existing default embeddings path. Env override wins.

    Falls back to whichever candidate is reachable. If none exist on disk,
    returns the local path so an obvious ENOENT surfaces at load time
    (better than silently using a stale cache from a different artifact).
    """
    env_override = os.environ.get("KG_MICROBE_EMBEDDINGS")
    if env_override:
        return env_override
    for candidate in (_LOCAL_EMBEDDINGS, _COMMUNITYMECH_EMBEDDINGS):
        if candidate.exists():
            return str(candidate)
    return str(_LOCAL_EMBEDDINGS)


KG_MICROBE_EMBEDDINGS = _resolve_default_embeddings()


class IngredientEmbeddingLoader:
    """Load and filter embeddings for ingredients."""

    def __init__(self, embeddings_path: Path, cache_dir: Path):
        self.embeddings_path = embeddings_path
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)

    def _cache_key(self, prefixes: List[str]) -> str:
        """Cache filename keyed on (embedding source identity, prefix set).
        Embedding identity is the basename plus an mtime+size fingerprint, so
        bumping the embedding file (e.g. 2026-02-01 → 2026-04-25) automatically
        invalidates the pickle without manual `rm -rf .umap_cache/`."""
        try:
            stat = self.embeddings_path.stat()
            fp = f"{stat.st_size}-{int(stat.st_mtime)}"
        except FileNotFoundError:
            fp = "missing"
        prefix_tag = "_".join(sorted(prefixes))
        digest = hashlib.sha1(
            f"{self.embeddings_path.name}|{fp}|{prefix_tag}".encode()
        ).hexdigest()[:12]
        return f"ingredient_embeddings__{prefix_tag}__{digest}.pkl"

    def load_embeddings(
        self,
        prefixes: List[str] = None,
        force_reload: bool = False
    ) -> Dict[str, np.ndarray]:
        """Load embeddings from TSV.gz, filter by prefixes, and cache."""
        if prefixes is None:
            # Ontology prefixes used by mapped records, plus the non-ontology
            # ingredient node families that KG-Microbe carries — these let
            # UNMAPPED_* records anchor to their mediadive.ingredient source ID
            # (or kgmicrobe.compound / mediadive.solution) instead of falling
            # back to a synthetic centroid. bacdive.isolation_source is
            # excluded — it describes where an organism was sampled from, not
            # a growth-medium component.
            prefixes = [
                "CHEBI", "FOODON", "NCIT", "MESH", "UBERON", "ENVO",
                "mediadive.ingredient", "mediadive.solution",
                "kgmicrobe.compound",
            ]

        cache_file = self.cache_dir / self._cache_key(prefixes)

        if cache_file.exists() and not force_reload:
            console.print(f"[green]Loading cached embeddings from {cache_file}[/green]")
            with open(cache_file, 'rb') as f:
                return pickle.load(f)

        console.print(f"[yellow]Loading embeddings from {self.embeddings_path}[/yellow]")
        console.print(f"[yellow]This may take a few minutes...[/yellow]")

        embeddings = {}

        with gzip.open(self.embeddings_path, 'rt') as f:
            for i, line in enumerate(f):
                if i % 100000 == 0 and i > 0:
                    console.print(f"  Processed {i:,} lines, found {len(embeddings):,} ingredient embeddings")

                parts = line.strip().split('\t')
                if len(parts) < 2:
                    continue

                entity_id = parts[0]

                # Filter by prefix
                if not any(entity_id.startswith(prefix + ':') for prefix in prefixes):
                    continue

                # Parse embedding vector
                try:
                    vector = np.array([float(x) for x in parts[1:]])
                    embeddings[entity_id] = vector
                except (ValueError, IndexError):
                    continue

        console.print(f"[green]Loaded {len(embeddings):,} ingredient embeddings[/green]")

        # Cache for future use
        with open(cache_file, 'wb') as f:
            pickle.dump(embeddings, f)
        console.print(f"[green]Cached embeddings to {cache_file}[/green]")

        return embeddings


class IngredientUMAPGenerator:
    """Generate UMAP visualization for ingredients."""

    def __init__(self, embeddings: Dict[str, np.ndarray]):
        self.embeddings = embeddings

    def generate_umap(
        self,
        ingredients_dir: Path,
        min_coverage: float = 0.5,
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        random_state: int = 42
    ) -> pd.DataFrame:
        """Generate UMAP projection for ingredients.

        Args:
            ingredients_dir: Directory with individual ingredient YAML files
            min_coverage: Minimum coverage to include ingredient
            n_neighbors: UMAP n_neighbors parameter
            min_dist: UMAP min_dist parameter
            random_state: Random seed

        Returns:
            DataFrame with ingredient_id, umap_x, umap_y
        """
        # Collect ingredient data
        ingredient_vectors = []
        ingredient_ids = []
        unmapped_ids = []  # Track which ones are unmapped without embeddings

        # First pass: collect all ingredients with real embeddings
        for category in ['mapped', 'unmapped']:
            category_dir = ingredients_dir / category
            if not category_dir.exists():
                continue

            for yaml_file in sorted(category_dir.glob('*.yaml')):
                try:
                    ingredient = load_yaml(yaml_file)
                    ingredient_id = ingredient.get('identifier', '')
                    found_embedding = False

                    # Strategy 1: Try direct identifier match
                    if ingredient_id in self.embeddings:
                        ingredient_vectors.append(self.embeddings[ingredient_id])
                        ingredient_ids.append(ingredient_id)
                        found_embedding = True

                    # Strategy 2: Try ontology_mapping ID
                    if not found_embedding:
                        ontology_mapping = ingredient.get('ontology_mapping') or {}
                        ontology_id = ontology_mapping.get('ontology_id', '')
                        if ontology_id and ontology_id in self.embeddings:
                            ingredient_vectors.append(self.embeddings[ontology_id])
                            ingredient_ids.append(ingredient_id)
                            found_embedding = True

                    # Strategy 3: For unmapped ingredients, try to find embeddings from synonyms
                    if not found_embedding and ingredient_id.startswith('UNMAPPED'):
                        synonyms = ingredient.get('synonyms', [])
                        for syn in synonyms:
                            syn_text = syn.get('synonym_text', '')
                            import re
                            chebi_matches = re.findall(r'CHEBI:?\s*(\d+)', syn_text, re.IGNORECASE)
                            for chebi_id in chebi_matches:
                                potential_id = f"CHEBI:{chebi_id}"
                                if potential_id in self.embeddings:
                                    ingredient_vectors.append(self.embeddings[potential_id])
                                    ingredient_ids.append(ingredient_id)
                                    found_embedding = True
                                    break
                            if found_embedding:
                                break

                    # Strategy 3b: For unmapped ingredients, pull the mim-queue
                    # source ID out of curation_history / notes and try it as a
                    # KG-Microbe node. ~186 UNMAPPED_* records carry a
                    # `source_id=mediadive.ingredient:NNNN` (or kgmicrobe.compound /
                    # mediadive.solution / bacdive.isolation_source) reference
                    # written by the mim-queue importer.
                    if not found_embedding and ingredient_id.startswith('UNMAPPED'):
                        import re
                        haystack_parts = [ingredient.get('notes', '') or '']
                        for event in ingredient.get('curation_history', []) or []:
                            haystack_parts.append(event.get('changes', '') or '')
                        haystack = '\n'.join(haystack_parts)
                        source_id_re = re.compile(
                            r'(mediadive\.ingredient|mediadive\.solution|'
                            r'kgmicrobe\.compound):([A-Za-z0-9_.\-]+)'
                        )
                        for prefix, local in source_id_re.findall(haystack):
                            potential_id = f"{prefix}:{local}"
                            if potential_id in self.embeddings:
                                ingredient_vectors.append(self.embeddings[potential_id])
                                ingredient_ids.append(ingredient_id)
                                found_embedding = True
                                break

                    # Strategy 4: If still not found and it's unmapped, add to unmapped list
                    if not found_embedding and ingredient_id.startswith('UNMAPPED'):
                        unmapped_ids.append(ingredient_id)

                except Exception as e:
                    console.print(f"[red]Error loading {yaml_file.name}: {e}[/red]")

        console.print(f"[green]Found embeddings for {len(ingredient_ids)} ingredients[/green]")
        console.print(f"[yellow]Adding {len(unmapped_ids)} unmapped ingredients with synthetic embeddings[/yellow]")

        # Second pass: Add unmapped ingredients with synthetic embeddings
        if len(ingredient_vectors) > 0:
            # Create mean embedding for reference
            mean_embedding = np.mean(ingredient_vectors, axis=0)

            for unmapped_id in unmapped_ids:
                # Create a synthetic embedding: mean + small random noise
                # This will place unmapped ingredients in a cluster near the center
                noise_scale = 0.1 * np.std(ingredient_vectors, axis=0)
                synthetic_embedding = mean_embedding + np.random.randn(len(mean_embedding)) * noise_scale
                ingredient_vectors.append(synthetic_embedding)
                ingredient_ids.append(unmapped_id)

        if len(ingredient_vectors) == 0:
            raise ValueError("No ingredient embeddings found!")

        # Convert to numpy array
        X = np.array(ingredient_vectors)

        # Run UMAP
        console.print(f"[yellow]Running UMAP (n_neighbors={n_neighbors}, min_dist={min_dist})...[/yellow]")
        reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            random_state=random_state,
            n_components=2
        )
        embedding_2d = reducer.fit_transform(X)

        # Create DataFrame
        df = pd.DataFrame({
            'ingredient_id': ingredient_ids,
            'umap_x': embedding_2d[:, 0],
            'umap_y': embedding_2d[:, 1]
        })

        console.print(f"[green]UMAP completed: {len(df)} ingredients projected to 2D[/green]")

        return df


def build_visualization_data(
    umap_df: pd.DataFrame,
    ingredients_dir: Path
) -> List[Dict[str, Any]]:
    """Build JSON data for visualization.

    Args:
        umap_df: DataFrame with ingredient_id, umap_x, umap_y
        ingredients_dir: Directory with ingredient YAML files

    Returns:
        List of ingredient data dictionaries
    """
    visualization_data = []

    # Index every per-record YAML once by identifier. Previously this function
    # re-globbed and re-parsed the entire corpus for every UMAP row (O(rows x
    # files) ~= millions of YAML loads), which made "Step 3" take far longer than
    # the UMAP fit itself. One pass + dict lookup makes it near-instant.
    records_by_id: Dict[str, Any] = {}
    for category in ['mapped', 'unmapped']:
        category_dir = ingredients_dir / category
        for candidate in category_dir.glob('*.yaml'):
            try:
                ing = load_yaml(candidate)
            except Exception:
                continue
            ident = ing.get('identifier')
            if ident and ident not in records_by_id:
                records_by_id[ident] = (ing, category)

    for _, row in umap_df.iterrows():
        ingredient_id = row['ingredient_id']
        entry = records_by_id.get(ingredient_id)
        if entry is None:
            continue
        ingredient, category = entry

        # Build the visualization record from the indexed ingredient.
        try:
            # Extract metadata
            preferred_term = ingredient.get('preferred_term', 'Unknown')

            # Better display name for empty placeholders
            if preferred_term.startswith('empty_'):
                # Use identifier instead for empty placeholders
                preferred_term = f"Unnamed Component ({ingredient_id})"

            mapping_status = ingredient.get('mapping_status', 'UNKNOWN')

            # Ontology info
            ontology_mapping = ingredient.get('ontology_mapping') or {}
            ontology_id = ontology_mapping.get('ontology_id', '')
            ontology_label = ontology_mapping.get('ontology_label', '')
            ontology_source = ontology_mapping.get('ontology_source', '')
            mapping_quality = ontology_mapping.get('mapping_quality', '')

            # Statistics
            stats = ingredient.get('occurrence_statistics', {})
            total_occurrences = stats.get('total_occurrences', 0)
            media_count = stats.get('media_count', 0)

            # Synonyms
            synonyms = ingredient.get('synonyms', [])
            num_synonyms = len(synonyms)

            # Chemical properties (populated for CHEBI-enriched records and
            # any record that carries a CAS-RN — see chemical_properties_enrichment.md).
            chem_props = ingredient.get('chemical_properties') or {}
            molecular_formula = chem_props.get('molecular_formula') or ''
            cas_rn = chem_props.get('cas_rn') or ''

            visualization_data.append({
                'id': ingredient_id,
                'name': preferred_term,
                'umap_x': float(row['umap_x']),
                'umap_y': float(row['umap_y']),
                'mapping_status': mapping_status,
                'ontology_source': ontology_source,
                'ontology_id': ontology_id,
                'ontology_label': ontology_label,
                'mapping_quality': mapping_quality,
                'total_occurrences': total_occurrences,
                'media_count': media_count,
                'num_synonyms': num_synonyms,
                'molecular_formula': molecular_formula,
                'cas_rn': cas_rn,
                'category': category
            })

        except Exception as e:
            console.print(f"[red]Error processing {ingredient_id}: {e}[/red]")

    return visualization_data


@click.command()
@click.option(
    '--embeddings-path',
    type=click.Path(exists=True),
    default=KG_MICROBE_EMBEDDINGS,
    help='Path to embeddings TSV.gz file (default: 2026-04-25 v2 512-D, '
         'shared across Mech repos via CommunityMech location)'
)
@click.option(
    '--ingredients-dir',
    type=click.Path(exists=True),
    default='data/ingredients',
    help='Directory with individual ingredient YAML files'
)
@click.option(
    '--output',
    type=click.Path(),
    default='docs/ingredient_umap.html',
    help='Output HTML file'
)
@click.option(
    '--cache-dir',
    type=click.Path(),
    default='.umap_cache',
    help='Cache directory for embeddings'
)
@click.option(
    '--force-reload',
    is_flag=True,
    help='Force reload embeddings from TSV.gz'
)
@click.option(
    '--n-neighbors',
    type=int,
    default=15,
    help='UMAP n_neighbors parameter'
)
@click.option(
    '--min-dist',
    type=float,
    default=0.1,
    help='UMAP min_dist parameter'
)
def main(
    embeddings_path: str,
    ingredients_dir: str,
    output: str,
    cache_dir: str,
    force_reload: bool,
    n_neighbors: int,
    min_dist: float
):
    """Generate interactive UMAP visualization of ingredient embeddings."""
    console.print("\n[bold]🔬 MediaIngredientMech UMAP Visualization Generator[/bold]\n")

    embeddings_path = Path(embeddings_path)
    ingredients_dir = Path(ingredients_dir)
    output_path = Path(output)
    cache_dir_path = Path(cache_dir)

    # Step 1: Load embeddings
    console.print("[bold]Step 1:[/bold] Loading embeddings...")
    loader = IngredientEmbeddingLoader(embeddings_path, cache_dir_path)
    embeddings = loader.load_embeddings(force_reload=force_reload)

    # Step 2: Generate UMAP
    console.print("\n[bold]Step 2:[/bold] Generating UMAP projection...")
    generator = IngredientUMAPGenerator(embeddings)
    umap_df = generator.generate_umap(
        ingredients_dir,
        n_neighbors=n_neighbors,
        min_dist=min_dist
    )

    # Step 3: Build visualization data
    console.print("\n[bold]Step 3:[/bold] Building visualization data...")
    viz_data = build_visualization_data(umap_df, ingredients_dir)
    console.print(f"[green]Generated data for {len(viz_data)} ingredients[/green]")

    # Step 4: Save intermediate JSON for inspection
    json_output = output_path.parent / 'data' / 'ingredient_umap.json'
    json_output.parent.mkdir(parents=True, exist_ok=True)
    with open(json_output, 'w') as f:
        json.dump(viz_data, f, indent=2)
    console.print(f"[green]Saved JSON data to {json_output}[/green]")

    # Step 5: Generate HTML (will be done separately)
    console.print(f"\n[yellow]Next: Create HTML template at {output_path}[/yellow]")
    console.print(f"[yellow]JSON data ready at {json_output}[/yellow]")

    console.print("\n[bold green]✅ UMAP generation complete![/bold green]\n")


if __name__ == '__main__':
    main()
