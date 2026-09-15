#!/usr/bin/env python3
"""Generate interactive UMAP visualization of media ingredient embedding space."""

import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

import click
import numpy as np
import pandas as pd
from rich.console import Console

# Ensure the src package is importable
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

# Ensure sibling script modules (e.g. sfdp_layout) are importable regardless of
# how this file is invoked (as a script, via uv run, or imported).
_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402
from mediaingredientmech.utils.yaml_handler import load_yaml  # noqa: E402

console = Console()

# Latest canonical kg-microbe deepwalk artifact, shared across all Mech repos.
# Resolution order:
#   1. ``KG_MICROBE_EMBEDDINGS`` env var (absolute path or repo-rooted)
#   2. ``data/embeddings/<filename>`` next to this script's repo
#   3. ``../CommunityMech/CommunityMech/data/embeddings/<filename>`` —
#      the 5.7 GB artifact is only vendored once per developer machine.
# All three locations are resolved relative to the script so the file works
# on any machine that has the Mech repos checked out as siblings.
_EMBEDDINGS_FILENAME = (
    "DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz"
)
_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_EMBEDDINGS = _REPO_ROOT / "data" / "embeddings" / _EMBEDDINGS_FILENAME
_COMMUNITYMECH_EMBEDDINGS = (
    Path(os.environ.get("COMMUNITYMECH_ROOT") or _REPO_ROOT.parent / "CommunityMech")
    / "data"
    / "embeddings"
    / _EMBEDDINGS_FILENAME
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


from mediaingredientmech.graph_embedding_receipts import (  # noqa: E402
    GraphSource,
    corpus_receipt,
    make_receipt,
    matrix_receipt,
    projection_receipt,
    publish_artifacts,
)


class IngredientEmbeddingLoader:
    """Load and filter embeddings for ingredients."""

    def __init__(self, embeddings_path: Path, cache_dir: Path):
        self.embeddings_path = embeddings_path
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)

    def _cache_key(self, prefixes: list[str]) -> str:
        """Historical key for compatibility; source loading never uses it.

        Basename, size and mtime cannot establish the identity of graph bytes.
        """
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
        prefixes: list[str] = None,
        force_reload: bool = False,
        node_ids=None,
    ) -> dict[str, np.ndarray]:
        """Read source bytes directly and retain only requested node vectors."""
        if prefixes is None:
            # Ontology prefixes used by mapped records, plus the non-ontology
            # ingredient node families that KG-Microbe carries — these let
            # UNMAPPED_* records anchor to their mediadive.ingredient source ID
            # (or kgmicrobe.compound / mediadive.solution) instead of falling
            # back to a synthetic centroid. bacdive.isolation_source is
            # excluded — it describes where an organism was sampled from, not
            # a growth-medium component.
            prefixes = [
                "CHEBI",
                "FOODON",
                "NCIT",
                "MESH",
                "UBERON",
                "ENVO",
                "mediadive.ingredient",
                "mediadive.solution",
                "kgmicrobe.compound",
            ]

        # #679: legacy basename/size/mtime pickle caches cannot prove lineage.
        source = GraphSource(self.embeddings_path, prefixes, node_ids=node_ids)
        embeddings = {node: np.asarray(vector, dtype=np.float64) for node, vector in source}
        self.source_receipt = source.receipt
        return embeddings


class IngredientUMAPGenerator:
    """Generate UMAP visualization for ingredients."""

    def __init__(self, embeddings: dict[str, np.ndarray]):
        self.embeddings = embeddings

    def generate_umap(
        self,
        ingredients_dir: Path,
        min_coverage: float = 0.5,
        method: str = "pacmap",
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        random_state: int = 42,
    ) -> pd.DataFrame:
        """Generate a 2D projection for ingredients.

        Args:
            ingredients_dir: Directory with individual ingredient YAML files
            min_coverage: Minimum coverage to include ingredient
            method: 2D reducer to use — "pacmap" (default; PCA-init, fixed seed,
                L2-normalized rows to mirror cosine) or "umap".
            n_neighbors: UMAP n_neighbors parameter (UMAP branch only)
            min_dist: UMAP min_dist parameter (UMAP branch only)
            random_state: Random seed

        Returns:
            DataFrame with ingredient_id, umap_x, umap_y (coordinate field names
            are kept as umap_x/umap_y regardless of method for HTML/JS compatibility)
        """
        ingredient_vectors = []
        ingredient_ids = []
        matches = []
        missing = []
        seen = set()
        ledger = []
        rejected = []
        for category in ["mapped", "unmapped"]:
            for yaml_file in sorted((ingredients_dir / category).glob("*.yaml")):
                ingredient = load_yaml(yaml_file)
                if ingredient.get("mapping_status") == "REJECTED":
                    rejected.append(yaml_file.relative_to(ingredients_dir).as_posix())
                    continue
                record_key = mim_curie_for_stem(yaml_file.stem)
                if record_key in seen:
                    raise ValueError(f"Duplicate visualization record key: {record_key}")
                seen.add(record_key)
                match = self.match_embedding(ingredient)
                if match is None:
                    missing.append(record_key)
                    ledger.append(
                        {
                            "identifier": record_key,
                            "source_nodes": [],
                            "status": "missing_vector",
                            "match_method": "no_match",
                            "source_path": yaml_file.relative_to(ingredients_dir).as_posix(),
                            "candidate_nodes": [
                                node for node, _ in self.candidate_nodes(ingredient)
                            ],
                        }
                    )
                    continue
                node_id, match_method = match
                ledger.append(
                    {
                        "identifier": record_key,
                        "source_nodes": [node_id],
                        "status": "projected",
                        "match_method": match_method,
                        "source_path": yaml_file.relative_to(ingredients_dir).as_posix(),
                    }
                )
                ingredient_ids.append(record_key)
                ingredient_vectors.append(self.embeddings[node_id])
                matches.append({"embedding_method": match_method, "embedding_source_node": node_id})
        if not ingredient_vectors:
            raise ValueError("No ingredient embeddings found; missing records have no coordinates")
        X = np.asarray(ingredient_vectors)
        if not np.isfinite(X).all():
            raise ValueError("Ingredient vectors must be finite")
        console.print(
            f"Found {len(ingredient_ids)} graph vectors; omitted {len(missing)} missing records"
        )

        # Run the selected 2D reducer.
        method = (method or "pacmap").lower()
        if method == "pacmap":
            import pacmap
            from sklearn.preprocessing import normalize

            parameters = {
                "n_components": 2,
                "random_state": random_state,
                "n_neighbors": None,
                "MN_ratio": 0.5,
                "FP_ratio": 2.0,
                "distance": "euclidean",
                "lr": 1.0,
                "num_iters": (100, 100, 250),
                "apply_pca": True,
                "knn_backend": "faiss",
            }
            X_norm = normalize(X.astype("float32"))
            vectors_receipt = matrix_receipt(X_norm, ingredient_ids)
            reducer = pacmap.PaCMAP(**parameters)
            embedding_2d = reducer.fit_transform(X_norm, init="pca")
            projection = projection_receipt(
                method, parameters, reducer=reducer, normalization="l2", initialization="pca"
            )
        elif method == "umap":
            import umap

            parameters = {
                "n_neighbors": n_neighbors,
                "min_dist": min_dist,
                "random_state": random_state,
                "n_components": 2,
                "metric": "euclidean",
            }
            vectors_receipt = matrix_receipt(X, ingredient_ids, dtype="float64-le")
            reducer = umap.UMAP(**parameters)
            embedding_2d = reducer.fit_transform(X)
            projection = projection_receipt(
                method, parameters, reducer=reducer, normalization="none"
            )
        elif method == "sfdp":
            from sfdp_layout import sfdp_layout

            embedding_2d, graph = sfdp_layout(
                X, k=15, seed=random_state, return_receipt=True, record_ids=ingredient_ids
            )
            vectors_receipt = graph.pop("matrix")
            projection = projection_receipt(
                method, {"k": 15, "seed": random_state}, normalization="l2", graph=graph
            )
        else:
            raise ValueError(f"Unknown projection method: {method}")
        if (
            np.asarray(embedding_2d).shape != (len(ingredient_ids), 2)
            or not np.isfinite(embedding_2d).all()
        ):
            raise ValueError(
                "Projection did not return finite coordinates for all selected ingredients"
            )

        # Create DataFrame. Coordinate columns stay umap_x/umap_y for every
        # method so the static docs/ingredient_umap.html + JS keep working.
        df = pd.DataFrame(
            {
                "ingredient_id": ingredient_ids,
                "umap_x": embedding_2d[:, 0],
                "umap_y": embedding_2d[:, 1],
                "embedding_method": [match["embedding_method"] for match in matches],
                "embedding_source_node": [match["embedding_source_node"] for match in matches],
            }
        )

        console.print(
            f"[green]{method.upper()} completed: {len(df)} ingredients projected to 2D[/green]"
        )

        df.attrs["coverage"] = {
            "eligible_records": len(seen),
            "embedded_records": len(ingredient_ids),
            "missing_records": missing,
            "synthetic_records": 0,
        }
        df.attrs["coverage"].update(
            eligible=len(seen),
            projected=len(ingredient_ids),
            omitted=len(missing),
            rejected_records=rejected,
        )
        df.attrs["projection"] = projection
        df.attrs["matrix"] = vectors_receipt
        df.attrs["ledger"] = ledger
        return df

    @staticmethod
    def candidate_nodes(ingredient: dict):
        """Enumerate source candidates in the same priority used for matching."""
        identifier = ingredient.get("identifier", "")
        if identifier:
            yield identifier, "direct_identifier"
        ontology_id = (ingredient.get("ontology_mapping") or {}).get("ontology_id", "")
        if ontology_id:
            yield ontology_id, "ontology_mapping"
        if identifier.startswith("UNMAPPED"):
            for synonym in ingredient.get("synonyms", []) or []:
                for local_id in re.findall(
                    r"CHEBI:?\s*(\d+)", synonym.get("synonym_text", ""), re.I
                ):
                    yield f"CHEBI:{local_id}", "synonym_reference"
            history = "\n".join(
                [ingredient.get("notes", "") or ""]
                + [
                    event.get("changes", "") or ""
                    for event in ingredient.get("curation_history", []) or []
                ]
            )
            for prefix, local_id in re.findall(
                r"(mediadive\.ingredient|mediadive\.solution|kgmicrobe\.compound):([A-Za-z0-9_.\-]+)",
                history,
            ):
                yield f"{prefix}:{local_id}", "history_reference"

    def match_embedding(self, ingredient: dict) -> tuple[str, str] | None:
        for node, method in self.candidate_nodes(ingredient):
            if node in self.embeddings:
                return node, method
        return None


def build_visualization_data(umap_df: pd.DataFrame, ingredients_dir: Path) -> list[dict[str, Any]]:
    """Build JSON data for visualization.

    Args:
        umap_df: DataFrame with ingredient_id, umap_x, umap_y
        ingredients_dir: Directory with ingredient YAML files

    Returns:
        List of ingredient data dictionaries
    """
    visualization_data = []

    # Index every per-record YAML once by its filename-derived MIM record CURIE.
    # `identifier` is a semantic identity and reviewed sibling records may share
    # it, so it cannot safely address one record. Previously this function
    # re-globbed and re-parsed the entire corpus for every UMAP row (O(rows x
    # files) ~= millions of YAML loads), which made "Step 3" take far longer than
    # the UMAP fit itself. One pass + dict lookup makes it near-instant.
    # MIM record CURIE -> (parsed record, category, source YAML path)
    records_by_key: dict[str, tuple[dict, str, Path]] = {}
    for category in ["mapped", "unmapped"]:
        category_dir = ingredients_dir / category
        for candidate in category_dir.glob("*.yaml"):
            try:
                ing = load_yaml(candidate)
            except Exception:
                continue
            if ing.get("mapping_status") == "REJECTED":
                continue
            record_key = mim_curie_for_stem(candidate.stem)
            if record_key in records_by_key:
                raise ValueError(f"Duplicate visualization record key: {record_key}")
            records_by_key[record_key] = (ing, category, candidate)

    for _, row in umap_df.iterrows():
        record_key = row["ingredient_id"]
        entry = records_by_key.get(record_key)
        if entry is None:
            continue
        ingredient, category, src_path = entry

        # Build the visualization record from the indexed ingredient.
        try:
            # Extract metadata
            preferred_term = ingredient.get("preferred_term", "Unknown")

            # Better display name for empty placeholders
            if preferred_term.startswith("empty_"):
                # Use identifier instead for empty placeholders
                preferred_term = f"Unnamed Component ({record_key})"

            mapping_status = ingredient.get("mapping_status", "UNKNOWN")

            # Ontology info
            ontology_mapping = ingredient.get("ontology_mapping") or {}
            ontology_id = ontology_mapping.get("ontology_id", "")
            ontology_label = ontology_mapping.get("ontology_label", "")
            ontology_source = ontology_mapping.get("ontology_source", "")
            mapping_quality = ontology_mapping.get("mapping_quality", "")

            # Statistics
            stats = ingredient.get("occurrence_statistics", {})
            total_occurrences = stats.get("total_occurrences", 0)
            media_count = stats.get("media_count", 0)

            # Synonyms
            synonyms = ingredient.get("synonyms", [])
            num_synonyms = len(synonyms)

            # Chemical properties (populated for CHEBI-enriched records and
            # any record that carries a CAS-RN — see chemical_properties_enrichment.md).
            chem_props = ingredient.get("chemical_properties") or {}
            molecular_formula = chem_props.get("molecular_formula") or ""
            cas_rn = chem_props.get("cas_rn") or ""

            visualization_data.append(
                {
                    "id": record_key,
                    "identifier": ingredient.get("identifier", ""),
                    "name": preferred_term,
                    "umap_x": float(row["umap_x"]),
                    "umap_y": float(row["umap_y"]),
                    "mapping_status": mapping_status,
                    "ontology_source": ontology_source,
                    "ontology_id": ontology_id,
                    "ontology_label": ontology_label,
                    "mapping_quality": mapping_quality,
                    "total_occurrences": total_occurrences,
                    "media_count": media_count,
                    "num_synonyms": num_synonyms,
                    "molecular_formula": molecular_formula,
                    "cas_rn": cas_rn,
                    "category": category,
                    "embedding_method": row.get("embedding_method", "legacy_unverified"),
                    "embedding_source_node": row.get("embedding_source_node"),
                }
            )

        except Exception as e:
            console.print(f"[red]Error processing {record_key} ({src_path}): {e}[/red]")

    return _require_unique_record_keys(visualization_data)


def _require_unique_record_keys(nodes: list[dict]) -> list[dict]:
    """Reject duplicate file-backed record keys instead of collapsing records."""
    keys = [str(node.get("id") or "") for node in nodes]
    missing = [index for index, key in enumerate(keys) if not key]
    if missing:
        raise ValueError(f"Visualization node(s) lack a record key: {missing[:8]}")
    seen: set[str] = set()
    duplicates: set[str] = set()
    for key in keys:
        if key in seen:
            duplicates.add(key)
        seen.add(key)
    if duplicates:
        raise ValueError(f"Duplicate visualization record key(s): {sorted(duplicates)[:8]}")
    return nodes


@click.command()
@click.option(
    "--embeddings-path",
    type=click.Path(exists=True),
    default=KG_MICROBE_EMBEDDINGS,
    help="Path to embeddings TSV.gz file (default: 2026-06-26 v3 512-D, "
    "shared across Mech repos via CommunityMech location)",
)
@click.option(
    "--ingredients-dir",
    type=click.Path(exists=True),
    default="data/ingredients",
    help="Directory with individual ingredient YAML files",
)
@click.option(
    "--output",
    type=click.Path(),
    default="docs/ingredient_umap.html",
    help="Output path. If it ends in .json the visualization JSON is written "
    "directly there (e.g. docs/data/ingredient_graph.json); otherwise it "
    "is treated as an HTML path and JSON is written to "
    "<parent>/data/ingredient_umap.json",
)
@click.option(
    "--cache-dir", type=click.Path(), default=".umap_cache", help="Cache directory for embeddings"
)
@click.option("--force-reload", is_flag=True, help="Force reload embeddings from TSV.gz")
@click.option(
    "--method",
    type=click.Choice(["pacmap", "umap", "sfdp"], case_sensitive=False),
    default="pacmap",
    help="2D reducer: pacmap (default; PCA-init, fixed seed), umap, or sfdp "
    "(Graphviz force-directed graph layout of a symmetric union-kNN embedding graph)",
)
@click.option(
    "--n-neighbors", type=int, default=15, help="UMAP n_neighbors parameter (umap method only)"
)
@click.option(
    "--min-dist", type=float, default=0.1, help="UMAP min_dist parameter (umap method only)"
)
def main(
    embeddings_path: str,
    ingredients_dir: str,
    output: str,
    cache_dir: str,
    force_reload: bool,
    method: str,
    n_neighbors: int,
    min_dist: float,
):
    """Generate interactive 2D visualization of ingredient embeddings."""
    console.print("\n[bold]🔬 MediaIngredientMech UMAP Visualization Generator[/bold]\n")

    embeddings_path = Path(embeddings_path)
    ingredients_dir = Path(ingredients_dir)
    output_path = Path(output)
    cache_dir_path = Path(cache_dir)

    # Step 1: Load embeddings
    console.print("[bold]Step 1:[/bold] Loading embeddings...")
    corpus_paths = sorted(
        path
        for category in ("mapped", "unmapped")
        for path in (ingredients_dir / category).glob("*.yaml")
    )
    corpus = corpus_receipt(corpus_paths, ingredients_dir)
    required_nodes = set()
    for path in corpus_paths:
        record = load_yaml(path)
        if record.get("mapping_status") != "REJECTED":
            required_nodes.update(
                node for node, _ in IngredientUMAPGenerator.candidate_nodes(record)
            )
    loader = IngredientEmbeddingLoader(embeddings_path, cache_dir_path)
    embeddings = loader.load_embeddings(force_reload=force_reload, node_ids=required_nodes)

    # Step 2: Generate 2D projection
    console.print(f"\n[bold]Step 2:[/bold] Generating {method.upper()} projection...")
    generator = IngredientUMAPGenerator(embeddings)
    umap_df = generator.generate_umap(
        ingredients_dir, method=method, n_neighbors=n_neighbors, min_dist=min_dist
    )

    # Step 3: Build visualization data
    console.print("\n[bold]Step 3:[/bold] Building visualization data...")
    viz_data = build_visualization_data(umap_df, ingredients_dir)
    console.print(f"[green]Generated data for {len(viz_data)} ingredients[/green]")

    # Step 4: Save intermediate JSON for inspection. When --output is itself a
    # .json path, honor it verbatim so alternate layouts (e.g. the sfdp graph
    # layout at docs/data/ingredient_graph.json) can be written to a second
    # output without clobbering the default pacmap JSON.
    if output_path.suffix.lower() == ".json":
        json_output = output_path
    else:
        json_output = output_path.parent / "data" / "ingredient_umap.json"
    metadata = make_receipt(
        source=loader.source_receipt,
        corpus=corpus,
        ledger=umap_df.attrs["ledger"],
        matrix=umap_df.attrs["matrix"],
        projection=umap_df.attrs["projection"],
        coverage=umap_df.attrs["coverage"],
    )
    if len(viz_data) != metadata["coverage"]["projected"]:
        raise ValueError("Visualization metadata dropped projected ingredients")
    if (
        corpus_receipt(
            sorted(
                path
                for category in ("mapped", "unmapped")
                for path in (ingredients_dir / category).glob("*.yaml")
            ),
            ingredients_dir,
        )
        != corpus
    ):
        raise ValueError("Ingredient corpus changed during graph generation")
    json_output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".ingredient-graph-", dir=json_output.parent
    ) as temporary:
        staged = Path(temporary) / json_output.name
        staged.write_text(json.dumps(viz_data, indent=2))
        publish_artifacts(
            {json_output: staged}, json_output.with_suffix(".metadata.json"), metadata
        )
    console.print(f"[green]Saved verified JSON and receipt to {json_output}[/green]")

    # Step 5: Generate HTML (will be done separately)
    console.print(f"\n[yellow]Next: Create HTML template at {output_path}[/yellow]")
    console.print(f"[yellow]JSON data ready at {json_output}[/yellow]")

    console.print("\n[bold green]✅ UMAP generation complete![/bold green]\n")


if __name__ == "__main__":
    main()
