#!/usr/bin/env python3
"""Generate interactive UMAP visualization of media ingredient embedding space."""

import gzip
import json
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


class IngredientEmbeddingLoader:
    """Load and filter embeddings for ingredients."""

    def __init__(self, embeddings_path: Path, cache_dir: Path):
        self.embeddings_path = embeddings_path
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)

    def load_embeddings(
        self,
        prefixes: List[str] = None,
        force_reload: bool = False
    ) -> Dict[str, np.ndarray]:
        """Load embeddings from TSV.gz, filter by prefixes, and cache."""
        if prefixes is None:
            prefixes = ["CHEBI", "FOODON", "NCIT", "MESH", "UBERON", "ENVO"]

        cache_file = self.cache_dir / "ingredient_embeddings.pkl"

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
                        ontology_mapping = ingredient.get('ontology_mapping', {})
                        ontology_id = ontology_mapping.get('ontology_id', '')
                        if ontology_id and ontology_id in self.embeddings:
                            ingredient_vectors.append(self.embeddings[ontology_id])
                            ingredient_ids.append(ingredient_id)
                            found_embedding = True

                    # Strategy 3: For unmapped ingredients, try to find embeddings from synonyms
                    # Look for CHEBI/ontology IDs mentioned in synonyms
                    if not found_embedding and ingredient_id.startswith('UNMAPPED'):
                        synonyms = ingredient.get('synonyms', [])
                        for syn in synonyms:
                            syn_text = syn.get('synonym_text', '')
                            # Look for patterns like "CAS: XXXX" or chemical formulas
                            # Try common chemical name patterns
                            import re
                            # Extract potential CHEBI IDs from text
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

                    # Strategy 4: Use preferred_term to search for similar chemical names
                    # (This would require fuzzy matching - skip for now but could be added)

                except Exception as e:
                    console.print(f"[red]Error loading {yaml_file.name}: {e}[/red]")

        console.print(f"[green]Found embeddings for {len(ingredient_ids)} ingredients[/green]")

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

    for _, row in umap_df.iterrows():
        ingredient_id = row['ingredient_id']

        # Find the YAML file
        yaml_file = None
        for category in ['mapped', 'unmapped']:
            category_dir = ingredients_dir / category
            for candidate in category_dir.glob('*.yaml'):
                try:
                    ing = load_yaml(candidate)
                    if ing.get('identifier') == ingredient_id:
                        yaml_file = candidate
                        break
                except:
                    continue
            if yaml_file:
                break

        if not yaml_file:
            continue

        # Load ingredient data
        try:
            ingredient = load_yaml(yaml_file)

            # Extract metadata
            preferred_term = ingredient.get('preferred_term', 'Unknown')
            mapping_status = ingredient.get('mapping_status', 'UNKNOWN')

            # Ontology info
            ontology_mapping = ingredient.get('ontology_mapping', {})
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
                'category': category if yaml_file else 'unknown'
            })

        except Exception as e:
            console.print(f"[red]Error processing {yaml_file}: {e}[/red]")

    return visualization_data


@click.command()
@click.option(
    '--embeddings-path',
    type=click.Path(exists=True),
    default='data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_2026-02-01_05_54_01.tsv.gz',
    help='Path to embeddings TSV.gz file'
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
