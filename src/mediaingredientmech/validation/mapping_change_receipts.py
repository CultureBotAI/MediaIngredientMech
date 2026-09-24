"""Mapping-change receipts as supersedable links for the resolution review (#740, #745, #748).

The completed reviews of 2026-09-21 pin records and SSSOM rows byte-for-byte:
identity plans, role plans and component dispositions pin a record's hash, and
the frozen release-hold resolution pins an assertion id that includes the row's
position in the SSSOM. A later, verified correction to one of those records or
rows therefore could not land at all, however unrelated it was to what the
review decided.

The completion side (``reports/sssom_completion_20260921/assemble_review.py``)
already chains **mapping-change receipts**: one JSON document per verified batch
under ``mapping_changes/``, recording the SSSOM digest before and after, every
owner record's before/after YAML hash, every changed/added/removed row and a
position map. This module lets the resolution side read the same receipts as
explicit links:

* a plan pin on record *R* with expected hash *H* is **superseded**, not
  violated, when the receipts chain *R* from *H* to its current hash; a
  superseded pin grants nothing (the plan's approval does not carry), it only
  stops the build from failing on a documented later correction;
* a frozen release-hold resolution whose assertion id was computed at a
  baseline row position is **re-derived** at the row's current position by
  composing the receipts' position maps, and accepted only when recomputing
  the baseline id from the current payload reproduces the frozen id exactly.

Nothing here turns a receipt into an approval, and every receipt is a
hash-bound review input.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

RECEIPTS_DIR = "reports/sssom_completion_20260921/mapping_changes"
SSSOM_SOURCE = "mappings/ingredient_mappings.sssom.tsv"


def load_receipts(root: Path, directory: str = RECEIPTS_DIR) -> list[dict]:
    """Return the receipts in sequence order, refusing gaps or approval-bearing links."""
    folder = root / directory
    receipts = (
        [json.loads(path.read_text()) for path in sorted(folder.glob("*.json"))]
        if folder.is_dir()
        else []
    )
    receipts.sort(key=lambda receipt: receipt["sequence"])
    if [r["sequence"] for r in receipts] != list(range(1, len(receipts) + 1)):
        raise ValueError("Mapping-change receipts must be numbered 1..n without gaps")
    for receipt in receipts:
        if (
            receipt.get("schema_version") != 1
            or str(receipt.get("approval", "")).split(":")[0] != "NONE"
        ):
            raise ValueError(
                f"Mapping-change receipt {receipt.get('batch')} is not an approval-free link"
            )
        if len(receipt["position_map"]) != receipt["before_row_count"]:
            raise ValueError(
                f"Mapping-change receipt {receipt.get('batch')} position map is incomplete"
            )
    for previous, receipt in zip(receipts, receipts[1:], strict=False):
        if receipt["before_sha256"] != previous["after_sha256"]:
            raise ValueError(
                f"Mapping-change receipt {receipt.get('batch')} does not chain from the previous link"
            )
        if receipt["before_row_count"] != previous["after_row_count"]:
            raise ValueError(
                f"Mapping-change receipt {receipt.get('batch')} does not chain row counts"
            )
    return receipts


def receipt_paths(root: Path, directory: str = RECEIPTS_DIR) -> list[str]:
    folder = root / directory
    return (
        [str(path.relative_to(root)) for path in sorted(folder.glob("*.json"))]
        if folder.is_dir()
        else []
    )


def record_digest(record) -> str:
    """Canonical digest of a parsed record, independent of YAML formatting."""
    packed = json.dumps(
        record, sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str
    )
    return hashlib.sha256(packed.encode()).hexdigest()


def record_chains(receipts: list[dict]) -> dict[str, list[dict]]:
    """source_record -> links in sequence order.

    Each link carries ``before`` / ``after`` (file digests) and ``before_record``
    (the canonical content digest of the pre-batch record, when the receipt
    recorded one).
    """
    chains: dict[str, list[dict]] = {}
    for receipt in receipts:
        for entry in receipt.get("records", []):
            chains.setdefault(entry["source_record"], []).append(
                {
                    "before": entry.get("before_yaml_sha256"),
                    "after": entry["after_yaml_sha256"],
                    "before_record": entry.get("before_record_sha256"),
                }
            )
    return chains


def _walk(links: list[dict], start: int, current: str) -> bool:
    running = links[start]["before"]
    for link in links[start:]:
        if link["before"] != running:
            return False
        running = link["after"]
    return running == current


def supersedes(chains: dict[str, list[dict]], name: str, expected: str, current: str) -> bool:
    """True when receipts chain ``name`` from the pinned file hash ``expected`` to ``current``.

    The chain must start exactly at the pinned hash and every later link must
    start where the previous one ended; a gap means an undocumented change and
    the pin stands. Equal hashes are not a supersession: the caller has already
    found the pin violated, and unchanged bytes with changed content is a defect.
    """
    if expected == current:
        return False
    links = chains.get(name, [])
    starts = [i for i, link in enumerate(links) if link["before"] == expected]
    return bool(starts) and _walk(links, starts[0], current)


def supersedes_content(
    chains: dict[str, list[dict]], name: str, pinned_record, current: str
) -> bool:
    """Like ``supersedes`` for a plan that pins parsed content rather than a file hash.

    The first link must have recorded ``before_record_sha256`` equal to the
    canonical digest of ``pinned_record``: that is the only proof that the
    receipt started from the state the plan describes.
    """
    links = chains.get(name, [])
    wanted = record_digest(pinned_record)
    starts = [i for i, link in enumerate(links) if link["before_record"] == wanted]
    return bool(starts) and _walk(links, starts[0], current)


def forward_map(receipts: list[dict]) -> list[int | None]:
    """baseline position (1-based index into the list) -> current position, or None if removed."""
    if not receipts:
        return []
    forward: list[int | None] = list(range(1, receipts[0]["before_row_count"] + 1))
    for receipt in receipts:
        position_map = receipt["position_map"]
        forward = [position_map[p - 1] if p is not None else None for p in forward]
    return forward


def baseline_position(forward: list[int | None], current: int) -> int | None:
    """Invert the composed map for one current position (None for a row a receipt added)."""
    for index, target in enumerate(forward, 1):
        if target == current:
            return index
    return None


def _assertion_id(position: int, payload_sha: str, source: str = SSSOM_SOURCE) -> str:
    from mediaingredientmech.validation.semantic_release import assertion_identity

    return assertion_identity(source, "mapping", position, payload_sha)


# The columns a *mapping* edge carries when ``Graph.edge`` hashes it. The KGX TSV
# adds every optional column (publications, reference_scope, ...) as an empty
# string, which was not part of the hashed row, so the recomputation must use
# exactly this set (#765).
MAPPING_EDGE_KEYS = frozenset(
    {
        "subject",
        "predicate",
        "object",
        "relation",
        "primary_knowledge_source",
        "provided_by",
        "assertion_type",
        "source_record",
        "source_position",
        "confidence",
        "assertion_json",
    }
)


def _edge_id_at(edge: dict, position: int) -> str:
    """The KGX edge id a *mapping* edge carried when its SSSOM row sat at ``position``.

    Mirrors ``mediaingredientmech.export.kgx.Graph.edge`` (the id is the digest
    of the packed row without ``id``) for the mapping kind, whose rows carry
    exactly ``MAPPING_EDGE_KEYS``; ``tests/test_mapping_change_receipts.py``
    pins the two together, on an in-memory edge and on a TSV-shaped one.
    """
    from mediaingredientmech.export.kgx import packed

    row = {key: value for key, value in edge.items() if key in MAPPING_EDGE_KEYS}
    row["source_position"] = str(position)
    return "MIM.assertion:" + hashlib.sha256(packed(row).encode()).hexdigest()


def hold_lineage(
    receipts: list[dict], assertions: list[dict], edges: list[dict], resolutions: list[dict]
) -> dict[str, dict]:
    """Map each frozen hold resolution's baseline ids to the ids the same row carries now.

    A frozen resolution names an assertion id and an edge id computed when its
    SSSOM row sat at a baseline position. Rows before it may since have been
    removed by a receipt. For each resolution whose ids no longer exist, find the
    current mapping assertion with the same payload hash, invert the composed
    position map to its baseline position, and recompute both ids there; only an
    exact reproduction of the frozen ids establishes the lineage.
    """
    if not receipts:
        return {}
    forward = forward_map(receipts)
    current_ids = {row["assertion_id"] for row in assertions}
    edge_index = {
        (edge["source_record"], edge["assertion_type"], str(edge["source_position"])): edge
        for edge in edges
    }
    lineage: dict[str, dict] = {}
    for resolution in resolutions:
        frozen_id = resolution.get("assertion_id")
        if frozen_id in current_ids:
            continue
        for row in assertions:
            if row.get("assertion_type") != "mapping" or row.get(
                "assertion_sha256"
            ) != resolution.get("assertion_sha256"):
                continue
            current_position = int(row["source_position"])
            origin = baseline_position(forward, current_position)
            if origin is None or _assertion_id(origin, row["assertion_sha256"]) != frozen_id:
                continue
            edge = edge_index.get((row["source_record"], "mapping", str(current_position)))
            if edge is None or _edge_id_at(edge, origin) != resolution.get("edge_id"):
                continue
            lineage[frozen_id] = {
                "assertion_id": row["assertion_id"],
                "edge_id": edge["id"],
                "baseline_position": origin,
                "current_position": current_position,
            }
            break
    return lineage
