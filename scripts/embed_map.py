#!/usr/bin/env python3
"""Project MediaIngredientMech text embeddings to 2D (PaCMAP + PCA) and render docs/text_map.html."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pacmap
from sklearn.decomposition import PCA

REPO_ROOT = Path(__file__).resolve().parent.parent


def normalize_coords(coords: np.ndarray) -> np.ndarray:
    mins = coords.min(axis=0)
    maxs = coords.max(axis=0)
    span = np.where((maxs - mins) == 0, 1.0, maxs - mins)
    return 2.0 * (coords - mins) / span - 1.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data" / "embeddings" / "records.npz",
        help="Input .npz file from embed_records.py",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=REPO_ROOT / "data" / "embeddings" / "corpus_map.json",
        help="Output JSON coordinates/metadata path",
    )
    parser.add_argument(
        "--html-out",
        type=Path,
        default=REPO_ROOT / "docs" / "text_map.html",
        help="Output interactive HTML path",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=REPO_ROOT / "src" / "mediaingredientmech" / "templates" / "text_map.html",
        help="HTML template path",
    )
    args = parser.parse_args()

    data = np.load(args.input, allow_pickle=True)
    embeddings = np.asarray(data["embeddings"], dtype=np.float32)
    ids = [str(x) for x in data["ids"]]
    titles = [str(x) for x in data["titles"]]
    identifiers = [str(x) for x in data["identifiers"]]
    mapping_statuses = [str(x) for x in data["mapping_statuses"]]
    ontology_sources = [str(x) for x in data["ontology_sources"]]
    mapping_qualities = [str(x) for x in data["mapping_qualities"]]
    ontology_ids = [str(x) for x in data["ontology_ids"]]
    ingredient_types = [str(x) for x in data["ingredient_types"]]
    media_counts = [int(x) for x in data["media_counts"]]
    urls = [str(x) for x in data["urls"]]
    model_name = str(data["model"]) if "model" in data else "BAAI/bge-large-en-v1.5"

    n = embeddings.shape[0]
    print(f"Projecting {n} embeddings ({embeddings.shape[1]}-d) with PCA and PaCMAP...")

    pca = PCA(n_components=2, random_state=42)
    pca_coords = normalize_coords(pca.fit_transform(embeddings))

    n_neighbors = min(15, max(2, n - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=42,
    )
    pacmap_coords = normalize_coords(reducer.fit_transform(embeddings))

    points = []
    for i in range(n):
        points.append(
            {
                "id": ids[i],
                "title": titles[i],
                "identifier": identifiers[i],
                "mapping_status": mapping_statuses[i],
                "ontology_source": ontology_sources[i],
                "mapping_quality": mapping_qualities[i],
                "ontology_id": ontology_ids[i],
                "ingredient_type": ingredient_types[i],
                "media_count": media_counts[i],
                "url": urls[i],
                "x": round(float(pacmap_coords[i, 0]), 5),
                "y": round(float(pacmap_coords[i, 1]), 5),
                "px": round(float(pca_coords[i, 0]), 5),
                "py": round(float(pca_coords[i, 1]), 5),
            }
        )

    payload = {
        "model": model_name,
        "dim": int(embeddings.shape[1]),
        "count": n,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "points": points,
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.json_out}")

    template_html = args.template.read_text(encoding="utf-8")
    rendered_html = template_html.replace("__MAP_DATA_JSON__", json.dumps(payload).replace("</", "<\\/"))
    args.html_out.parent.mkdir(parents=True, exist_ok=True)
    args.html_out.write_text(rendered_html, encoding="utf-8")
    print(f"Wrote {args.html_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
