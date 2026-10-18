#!/usr/bin/env python3
"""Generate dense text embeddings for all live MediaIngredientMech records.

Walks data/ingredients/{mapped,unmapped}/*.yaml (excluding REJECTED records),
constructs a structured natural-language text representation for each ingredient,
embeds with BAAI/bge-large-en-v1.5 (normalized 1024-d vectors), and writes
data/embeddings/records.npz.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import numpy as np
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402

DEFAULT_MODEL = "BAAI/bge-large-en-v1.5"


def slug_for_source(category: str, path: Path) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", path.stem).strip("_") or "ingredient"
    return f"{category}/{stem}"


def record_key_for_stem(stem: str) -> str:
    return mim_curie_for_stem(stem)


def record_to_text(rec: dict[str, Any], record_id: str) -> str:
    parts: list[str] = []
    preferred = str(rec.get("preferred_term") or record_id).strip()
    identifier = str(rec.get("identifier") or "").strip()
    status = str(rec.get("mapping_status") or "UNKNOWN").strip()
    ing_type = str(rec.get("ingredient_type") or "").strip()

    header = f"Media Ingredient: {preferred} ({record_id})"
    if identifier:
        header += f" [ID: {identifier}]"
    parts.append(header)

    meta_bits = [f"Mapping Status: {status}"]
    if ing_type:
        meta_bits.append(f"Ingredient Type: {ing_type}")
    parts.append("; ".join(meta_bits))

    ont = rec.get("ontology_mapping") or {}
    if isinstance(ont, dict) and ont:
        ont_id = str(ont.get("ontology_id") or "").strip()
        ont_label = str(ont.get("ontology_label") or "").strip()
        ont_src = str(ont.get("ontology_source") or "").strip()
        ont_qual = str(ont.get("mapping_quality") or "").strip()
        ont_bits = [x for x in [ont_label, ont_id, ont_src, ont_qual] if x]
        if ont_bits:
            parts.append("Ontology Mapping: " + " | ".join(ont_bits))

    chem = rec.get("chemical_properties") or {}
    if isinstance(chem, dict) and chem:
        formula = str(chem.get("molecular_formula") or "").strip()
        cas_rn = str(chem.get("cas_rn") or "").strip()
        chem_bits = []
        if formula:
            chem_bits.append(f"Formula: {formula}")
        if cas_rn:
            chem_bits.append(f"CAS: {cas_rn}")
        if chem_bits:
            parts.append("; ".join(chem_bits))

    syns = rec.get("synonyms") or []
    if isinstance(syns, list) and syns:
        syn_texts = []
        for s in syns:
            if isinstance(s, dict):
                if s.get("synonym_type") == "REJECTED_LABEL":
                    continue
                st = str(s.get("synonym_text") or "").strip()
                if st and st not in syn_texts:
                    syn_texts.append(st)
        if syn_texts:
            parts.append("Synonyms: " + ", ".join(syn_texts[:20]))

    role_names: list[str] = []
    for role_field in (
        "nutritional_roles",
        "physicochemical_roles",
        "cellular_metabolic_roles",
    ):
        for r in rec.get(role_field) or []:
            if isinstance(r, dict) and r.get("role"):
                role_names.append(str(r["role"]))
            elif isinstance(r, str):
                role_names.append(r)
    if role_names:
        parts.append("Roles: " + ", ".join(role_names))

    comps = rec.get("components") or []
    if isinstance(comps, list) and comps:
        comp_names = []
        for c in comps:
            if isinstance(c, dict) and c.get("component_name"):
                comp_names.append(str(c["component_name"]))
        if comp_names:
            parts.append("Components: " + ", ".join(comp_names[:20]))

    notes = str(rec.get("notes") or rec.get("definition") or "").strip()
    if notes:
        parts.append(f"Notes: {notes}")

    return "\n".join(parts)


def collect_records(ingredients_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for category in ("mapped", "unmapped"):
        cat_dir = ingredients_dir / category
        if not cat_dir.exists():
            continue
        for path in sorted(cat_dir.glob("*.yaml")):
            try:
                rec = yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if not isinstance(rec, dict):
                continue
            status = str(rec.get("mapping_status") or "UNKNOWN").strip()
            if status == "REJECTED":
                continue

            record_id = record_key_for_stem(path.stem)
            preferred = str(rec.get("preferred_term") or path.stem).strip()
            if preferred.startswith("empty_"):
                preferred = f"Unnamed Component ({record_id})"
            identifier = str(rec.get("identifier") or "").strip()
            ing_type = str(rec.get("ingredient_type") or "UNSPECIFIED").strip()

            ont = rec.get("ontology_mapping") or {}
            ont_source = (
                str(ont.get("ontology_source") or "UNMAPPED").strip()
                if isinstance(ont, dict)
                else "UNMAPPED"
            )
            if not ont_source:
                ont_source = "UNMAPPED"
            ont_quality = (
                str(ont.get("mapping_quality") or "UNMAPPED").strip()
                if isinstance(ont, dict)
                else "UNMAPPED"
            )
            if not ont_quality:
                ont_quality = "UNMAPPED"
            ont_id = (
                str(ont.get("ontology_id") or "").strip()
                if isinstance(ont, dict)
                else ""
            )

            stats = rec.get("occurrence_statistics") or {}
            media_count = (
                int(stats.get("media_count") or 0)
                if isinstance(stats, dict)
                else 0
            )
            slug = slug_for_source(category, path)
            detail_url = f"records/ingredient/{slug}.html"

            records.append(
                {
                    "id": record_id,
                    "title": preferred,
                    "identifier": identifier,
                    "mapping_status": status,
                    "ontology_source": ont_source,
                    "mapping_quality": ont_quality,
                    "ontology_id": ont_id,
                    "ingredient_type": ing_type,
                    "media_count": media_count,
                    "url": detail_url,
                    "text": record_to_text(rec, record_id),
                }
            )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ingredients-dir",
        type=Path,
        default=REPO_ROOT / "data" / "ingredients",
        help="Path to data/ingredients directory",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "data" / "embeddings" / "records.npz",
        help="Output .npz path",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"SentenceTransformer model name (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="Encoding batch size",
    )
    args = parser.parse_args()

    records = collect_records(args.ingredients_dir)
    if not records:
        print(f"No ingredient records found in {args.ingredients_dir}", file=sys.stderr)
        return 1

    print(f"Collected {len(records)} live ingredient records. Loading {args.model}...")
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(args.model)
    texts = [r["text"] for r in records]
    embeddings = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )
    embeddings = np.asarray(embeddings, dtype=np.float32)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output,
        embeddings=embeddings,
        ids=np.array([r["id"] for r in records], dtype=object),
        titles=np.array([r["title"] for r in records], dtype=object),
        identifiers=np.array([r["identifier"] for r in records], dtype=object),
        mapping_statuses=np.array([r["mapping_status"] for r in records], dtype=object),
        ontology_sources=np.array([r["ontology_source"] for r in records], dtype=object),
        mapping_qualities=np.array([r["mapping_quality"] for r in records], dtype=object),
        ontology_ids=np.array([r["ontology_id"] for r in records], dtype=object),
        ingredient_types=np.array([r["ingredient_type"] for r in records], dtype=object),
        media_counts=np.array([r["media_count"] for r in records], dtype=np.int32),
        urls=np.array([r["url"] for r in records], dtype=object),
        texts=np.array(texts, dtype=object),
        model=np.array(args.model, dtype=object),
    )
    print(f"Saved {embeddings.shape[0]}x{embeddings.shape[1]} embeddings to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
