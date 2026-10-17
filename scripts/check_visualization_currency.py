#!/usr/bin/env python3
"""Fail when a published visualization references records that no longer exist (#401).

`docs/data/ingredient_umap.json` and `ingredient_graph.json` are outward-facing —
the docs site renders them — and they had not been regenerated since #98. By the
time this was written, **114 of their 382 `UNMAPPED_*` ids named records that had
been merged, promoted or retired**, so roughly one node in three was wrong. They
still showed `X` mapped to NCIT "the 24th letter of the English alphabet" (#356),
`Aromatic hydrocarbon` on a retired mint (#392), and both labels corrected in
#397.

Nothing caught it because nothing regenerates them: `generate_ingredient_umap.py`
is reachable only from `just generate-umap`. The same shape as #217 and #380, for
a third artifact.

## Why this gate is membership-based rather than a no-op diff

#380's gate asserts that regenerating produces no diff. That works there because
`generate_index_files.py` is deterministic. **These are not.** Two consecutive
runs with `random_state=42` give:

    umap_x   max Δ 11.46   median Δ 0.5286
    umap_y   max Δ 12.29   median Δ 0.5550
    id set                 IDENTICAL
    total_occurrences / media_count / num_synonyms   IDENTICAL

PaCMAP's layout jitters (BLAS/thread nondeterminism the seed does not reach), so
a byte-diff gate would be permanently red — and a permanently red gate gets
deleted rather than obeyed, which is the failure #380's docstring warns about.

Everything that is *derived from the corpus* is stable, so this asserts that
instead: **every published node must name one live file-backed record, carry
that record's semantic metadata, and every live record must either have a node
or be listed in `docs/data/ingredient_visualization_exclusions.json` with its
current `(identifier, ontology_id)` when no KG-Microbe embedding exists (#904).**
Visualization `id` values are filename-derived `MIM:` record CURIEs; the
non-unique ingredient `identifier` cannot address sibling records. The check
tolerates layout jitter and needs no regeneration to compare coordinates.

    python scripts/check_visualization_currency.py            # report
    python scripts/check_visualization_currency.py --strict   # exit 1 on key/identity defects
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from collections.abc import Mapping
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402
from mediaingredientmech.synonym_policy import count_resolving_synonyms  # noqa: E402
from mediaingredientmech.utils.yaml_handler import load_yaml  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"
ARTIFACTS = ("ingredient_umap.json", "ingredient_graph.json")
EXCLUSIONS_ARTIFACT = "ingredient_visualization_exclusions.json"
EMBEDDED_PREFIXES = (
    "CHEBI:",
    "FOODON:",
    "NCIT:",
    "MESH:",
    "UBERON:",
    "ENVO:",
    "mediadive.ingredient:",
    "mediadive.solution:",
    "kgmicrobe.compound:",
)
STABLE_NODE_FIELDS = (
    "identifier",
    "name",
    "mapping_status",
    "ontology_source",
    "ontology_id",
    "ontology_label",
    "mapping_quality",
    "total_occurrences",
    "media_count",
    "num_synonyms",
    "molecular_formula",
    "cas_rn",
    "category",
)


def visualization_metadata(
    record: dict,
    category: str,
    record_key: str,
) -> dict[str, object]:
    """Return the non-coordinate visualization fields derived from one record."""
    preferred_term = record.get("preferred_term", "Unknown")
    if preferred_term.startswith("empty_"):
        preferred_term = f"Unnamed Component ({record_key})"

    ontology_mapping = record.get("ontology_mapping") or {}
    stats = record.get("occurrence_statistics", {})
    synonyms = record.get("synonyms", [])
    chem_props = record.get("chemical_properties") or {}
    return {
        "identifier": record.get("identifier", ""),
        "name": preferred_term,
        "mapping_status": record.get("mapping_status", "UNKNOWN"),
        "ontology_source": ontology_mapping.get("ontology_source", ""),
        "ontology_id": ontology_mapping.get("ontology_id", ""),
        "ontology_label": ontology_mapping.get("ontology_label", ""),
        "mapping_quality": ontology_mapping.get("mapping_quality", ""),
        "total_occurrences": stats.get("total_occurrences", 0),
        "media_count": stats.get("media_count", 0),
        "num_synonyms": count_resolving_synonyms(synonyms),
        "molecular_formula": chem_props.get("molecular_formula") or "",
        "cas_rn": chem_props.get("cas_rn") or "",
        "category": category,
    }


def live_records(ingredients_root: Path = INGREDIENTS) -> dict[str, dict[str, object]]:
    """Return file-backed record CURIE -> stable visualization metadata."""
    records: dict[str, dict[str, object]] = {}
    for category in ("mapped", "unmapped"):
        for path in (ingredients_root / category).glob("*.yaml"):
            try:
                record = load_yaml(path)
            except Exception:
                continue
            if not isinstance(record, dict) or record.get("mapping_status") == "REJECTED":
                continue
            record_key = mim_curie_for_stem(path.stem)
            if record_key in records:
                raise ValueError(f"Duplicate visualization record key: {record_key}")
            records[record_key] = visualization_metadata(record, category, record_key)
    return records


def load_exclusions(
    path: Path = ROOT / "docs" / "data" / EXCLUSIONS_ARTIFACT,
) -> dict[str, dict[str, str]]:
    """Return recorded visualization exclusions keyed by MIM record CURIE."""
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return {}
    return {
        str(key): value
        for key, value in payload.items()
        if isinstance(value, dict)
    }


def audit_entries(
    entries: object,
    live: dict[str, dict[str, object]],
    exclusions: Mapping[str, Mapping[str, object]] | None = None,
) -> dict[str, list]:
    """Return stable metadata defects for one published artifact payload."""
    if not isinstance(entries, list):
        return {
            "invalid_entries": ["payload is not a list"],
            "blank_ids": [],
            "duplicate_ids": [],
            "stale": [],
            "missing": [],
            "invalid_exclusions": [],
            "metadata_mismatches": [],
        }

    invalid_entries = [index for index, entry in enumerate(entries) if not isinstance(entry, dict)]
    nodes = [entry for entry in entries if isinstance(entry, dict)]
    node_ids = [str(entry.get("id") or "").strip() for entry in nodes]
    blank_ids = [index for index, node_id in enumerate(node_ids) if not node_id]
    ids = {node_id for node_id in node_ids if node_id}
    duplicate_ids = sorted(
        node_id for node_id, count in Counter(node_ids).items() if node_id and count > 1
    )
    stale = sorted(ids - live.keys())

    exclusions_map = exclusions if isinstance(exclusions, Mapping) else {}
    embedded_ids: set[str] = set()
    for entry in nodes:
        if str(entry.get("identifier") or "").strip().startswith("UNMAPPED"):
            continue
        candidates = {
            value
            for field in ("identifier", "ontology_id")
            if (value := str(entry.get(field) or "").strip()).startswith(EMBEDDED_PREFIXES)
        }
        if len(candidates) == 1:
            embedded_ids.update(candidates)

    missing: list[str] = []
    for record_key in sorted(live.keys() - ids):
        meta = live[record_key]
        if isinstance(meta, Mapping):
            live_identifier = str(meta.get("identifier") or "")
            live_ontology_id = str(meta.get("ontology_id") or "")
            live_status = str(meta.get("mapping_status") or "")
            live_category = str(meta.get("category") or "")
        else:
            live_identifier = str(meta or "")
            live_ontology_id = ""
            live_status = ""
            live_category = ""

        exc = exclusions_map.get(record_key)
        if not isinstance(exc, Mapping):
            missing.append(record_key)
            continue
        if (
            live_status == "UNMAPPED"
            or live_category == "unmapped"
            or live_identifier.startswith("UNMAPPED")
        ):
            missing.append(record_key)
            continue
        if not str(exc.get("reason") or "").strip():
            missing.append(record_key)
            continue
        if (
            str(exc.get("identifier") or "") != live_identifier
            or str(exc.get("ontology_id") or "") != live_ontology_id
        ):
            missing.append(record_key)
            continue
        if (live_identifier and live_identifier in embedded_ids) or (
            live_ontology_id and live_ontology_id in embedded_ids
        ):
            missing.append(record_key)
            continue

    invalid_exclusions = sorted(
        record_key
        for record_key in exclusions_map
        if record_key not in live or record_key in ids
    )

    metadata_mismatches = []
    for entry in nodes:
        record_key = str(entry.get("id") or "").strip()
        if record_key not in live or not isinstance(live[record_key], Mapping):
            continue
        mismatches = {
            field: (entry.get(field), expected)
            for field, expected in live[record_key].items()
            if entry.get(field) != expected
        }
        if mismatches:
            metadata_mismatches.append((record_key, mismatches))
    return {
        "invalid_entries": invalid_entries,
        "blank_ids": blank_ids,
        "duplicate_ids": duplicate_ids,
        "stale": stale,
        "missing": missing,
        "invalid_exclusions": invalid_exclusions,
        "metadata_mismatches": metadata_mismatches,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 on missing, duplicate, or semantically mismatched record keys",
    )
    args = ap.parse_args(argv)

    live = live_records()
    if not live:
        print("CANNOT CHECK: no live per-record ingredients loaded.")
        return 2
    exclusions = load_exclusions()

    worst = 0
    for name in ARTIFACTS:
        path = ROOT / "docs" / "data" / name
        if not path.exists():
            print(f"  {name}: absent — skipped")
            continue
        entries = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(entries, dict):
            entries = entries.get("ingredients", [])
        audit = audit_entries(entries, live, exclusions)
        invalid_entries = audit["invalid_entries"]
        blank_ids = audit["blank_ids"]
        duplicate_ids = audit["duplicate_ids"]
        stale = audit["stale"]
        missing = audit["missing"]
        invalid_exclusions = audit["invalid_exclusions"]
        metadata_mismatches = audit["metadata_mismatches"]
        node_count = len(entries) if isinstance(entries, list) else 0
        nonblank_count = max(node_count - len(blank_ids) - len(invalid_entries), 0)
        pct = (100 * len(stale) // nonblank_count) if nonblank_count else 0
        defects = sum(len(values) for values in audit.values())
        flag = "STALE" if defects else "ok"
        print(
            f"  {flag:<6} {name:<24} nodes {node_count:>5}  naming missing "
            f"records {len(stale):>4} ({pct}%)  missing live records "
            f"{len(missing):>4}  stale exclusions {len(invalid_exclusions):>3}  "
            f"duplicate keys {len(duplicate_ids):>3}  blank keys {len(blank_ids):>3}  "
            f"invalid entries {len(invalid_entries):>3}  "
            f"wrong metadata {len(metadata_mismatches):>3}"
        )
        for s in stale[:8]:
            print(f"            stale node: {s}")
        if len(stale) > 8:
            print(f"            ... {len(stale) - 8} more stale nodes")
        for record_key in missing[:8]:
            print(f"            missing live record: {record_key}")
        if len(missing) > 8:
            print(f"            ... {len(missing) - 8} more missing live records")
        for record_key in invalid_exclusions[:8]:
            print(f"            stale exclusion: {record_key}")
        for record_key in duplicate_ids[:8]:
            print(f"            duplicate record key: {record_key}")
        for index in blank_ids[:8]:
            print(f"            blank record key at node index {index}")
        for index in invalid_entries[:8]:
            print(f"            invalid node entry at index {index}")
        for record_key, mismatches in metadata_mismatches[:8]:
            details = ", ".join(
                f"{field} {observed!r} != {expected!r}"
                for field, (observed, expected) in mismatches.items()
            )
            print(f"            {record_key}: {details}")
        worst = max(worst, defects)

    if worst:
        print(
            "\nVisualization nodes have stale, missing, duplicate, or semantically "
            "mismatched record metadata. Regenerate:\n"
            "    just generate-umap        # writes docs/data/ingredient_umap.json\n"
            "    just generate-graph       # writes docs/data/ingredient_graph.json\n"
            "Layout coordinates will differ between runs (PaCMAP is not fully "
            "deterministic); only the membership above is asserted."
        )
        if args.strict:
            return 1
    else:
        print(
            "\nOK: every published node names one live record and carries its metadata, "
            f"and all {len(exclusions)} excluded MAPPED records are accounted for."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
