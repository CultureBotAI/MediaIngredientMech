#!/usr/bin/env python3
"""Apply Step 7b Edison-derived role research results to MIM ingredient records.

Reads a JSON batch (emitted by CultureMech `scripts/extract_roles_from_edison.py`
from `research/ingredients/roles/*-edison-literature.md` output) and writes
faceted role assignments back to `MediaIngredientMech/data/ingredients/**/*.yaml`
with full `RoleCitation` evidence.

Per-facet "never overwrite" guard: an ingredient whose `nutritional_roles`
slot is already populated will NOT receive new nutritional-role proposals
(but is still eligible for `physicochemical_roles` / `cellular_metabolic_roles`
if those are empty). Matches the `apply_insession_role_curation.py` pattern.

Idempotent: re-running against the same batch on an already-populated record
skips it silently.

Companion of `apply_insession_role_curation.py` — differs in:
  - `curator: "edison-deep-research"` (vs `claude_in_session_curation`).
  - Confidence sourced FROM Edison output (per-role field), not a fixed 0.6.
  - `reference_type` per-evidence (typically PEER_REVIEWED_PUBLICATION with DOI)
    rather than the flat `COMPUTATIONAL_PREDICTION`.
  - Input is a JSON batch keyed by ingredient identifier, not a hard-coded
    dict — the input is data, not code.

Input JSON shape (produced by PR4's extractor):

    {
      "proposals": [
        {
          "ingredient_identifier": "CHEBI:17561",         # or a MIM/MICRO/… identifier
          "ingredient_path": "data/ingredients/mapped/L-cysteine.yaml",  # optional
          "source_run": "research/ingredients/roles/L-cysteine-edison-literature.md",
          "role_assignments": {
            "nutritional_roles": [
              {
                "role": "AMINO_ACID_SOURCE",
                "confidence": 0.95,
                "metabolic_context": "...",     # optional, cellular-metabolic only
                "evidence": [                   # optional, list may be empty
                  {
                    "reference_type": "PEER_REVIEWED_PUBLICATION",
                    "doi": "10.1128/jb.00456-20",
                    "pmid": "12345678",         # optional if doi given
                    "reference_text": "...",
                    "excerpt": "...",
                    "curator_note": "..."
                  }
                ]
              }
            ],
            "physicochemical_roles": [...],
            "cellular_metabolic_roles": [...]
          }
        }
      ]
    }

Usage:

    just apply-role-research-results reports/edison_role_extraction.json --dry-run
    just apply-role-research-results reports/edison_role_extraction.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mediaingredientmech.utils.role_facets import (
    CELLULAR_METABOLIC,
    NUTRITIONAL,
    PHYSICOCHEMICAL,
    facet_slot_for,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
INGREDIENTS_DIR = REPO_ROOT / "data" / "ingredients"

DEFAULT_CURATOR = "edison-deep-research"
DEFAULT_REFERENCE_TYPE = "PEER_REVIEWED_PUBLICATION"

FACET_SLOTS = (NUTRITIONAL, PHYSICOCHEMICAL, CELLULAR_METABOLIC)


def _load_batch(path: Path) -> list[dict[str, Any]]:
    """Load and shape-check the extractor JSON batch."""
    data = json.loads(path.read_text())
    if not isinstance(data, dict) or "proposals" not in data:
        raise SystemExit(
            f"Batch file {path} must be a JSON object with a top-level 'proposals' list."
        )
    proposals = data["proposals"]
    if not isinstance(proposals, list):
        raise SystemExit(f"'proposals' in {path} must be a list, got {type(proposals).__name__}.")
    return proposals


def _resolve_ingredient_path(proposal: dict[str, Any]) -> Path | None:
    """Return the MIM YAML path for a proposal, or None if unresolvable."""
    p = proposal.get("ingredient_path")
    if p:
        candidate = Path(p) if Path(p).is_absolute() else REPO_ROOT / p
        if candidate.is_file():
            return candidate
    ident = proposal.get("ingredient_identifier") or ""
    if not ident:
        return None
    # Try both status buckets (mapped/, unmapped/) using identifier as slug/id match.
    # First cheap check: filename == "{local_part}.yaml".
    if ":" in ident:
        local = ident.split(":", 1)[1]
    else:
        local = ident
    for status_dir in sorted(p for p in INGREDIENTS_DIR.iterdir() if p.is_dir()):
        # Try the local part directly, then a case-insensitive search.
        candidate = status_dir / f"{local}.yaml"
        if candidate.is_file():
            return candidate
    # Slow path — walk and match by `identifier:` field inside each YAML.
    import yaml
    for yml in INGREDIENTS_DIR.rglob("*.yaml"):
        try:
            doc = yaml.safe_load(yml.read_text())
        except Exception:
            continue
        if isinstance(doc, dict) and doc.get("identifier") == ident:
            return yml
    return None


def _build_assignment(
    role: str,
    confidence: float,
    metabolic_context: str | None,
    evidence_entries: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build a single RoleAssignment dict matching the LinkML schema shape."""
    assignment: dict[str, Any] = {"role": role, "confidence": confidence, "evidence": []}
    for ev in evidence_entries:
        cite: dict[str, Any] = {}
        for k in ("reference_type", "doi", "pmid", "reference_text", "url", "excerpt", "curator_note"):
            if ev.get(k):
                cite[k] = ev[k]
        if cite:
            assignment["evidence"].append(cite)
    if metabolic_context:
        # Schema note: metabolic_context is only on `CellularMetabolicRoleAssignment`.
        # Caller must have already vetted the slot; we just carry the value through.
        assignment["metabolic_context"] = metabolic_context
    return assignment


def _add_curation_event(
    record: dict[str, Any],
    curator_name: str,
    fields_changed: list[str],
    notes: str,
) -> None:
    """Append a curation_history event to the record."""
    history = record.setdefault("curation_history", [])
    history.append({
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "curator": curator_name,
        "action": "ANNOTATED",
        "changes": ", ".join(fields_changed),
        "notes": notes,
    })


def _apply_proposal(
    record: dict[str, Any],
    proposal: dict[str, Any],
    curator_name: str,
    dry_run: bool,
) -> tuple[int, list[str], bool]:
    """Apply one proposal to one record. Returns (roles_applied, skip_reasons, dirty)."""
    role_assignments = proposal.get("role_assignments") or {}
    applied = 0
    reasons: list[str] = []
    dirty = False
    source_run = proposal.get("source_run") or ""
    fields_changed: list[str] = []

    for slot in FACET_SLOTS:
        proposals_for_slot = role_assignments.get(slot) or []
        if not proposals_for_slot:
            continue
        # Per-facet never-overwrite guard.
        if record.get(slot):
            reasons.append(f"skipped {slot}: already populated ({len(record[slot])} existing)")
            continue

        new_assignments: list[dict[str, Any]] = []
        for role_prop in proposals_for_slot:
            if not isinstance(role_prop, dict):
                continue
            role = role_prop.get("role")
            if not role:
                continue

            # Cross-check: role name must belong to this facet.
            try:
                expected_slot = facet_slot_for(role)
            except Exception:
                expected_slot = None
            if expected_slot is not None and expected_slot != slot:
                reasons.append(
                    f"skipped {slot}[{role}]: role belongs to {expected_slot}, not {slot}"
                )
                continue

            confidence = float(role_prop.get("confidence", 0.8))
            metabolic_context = role_prop.get("metabolic_context")
            if metabolic_context and slot != CELLULAR_METABOLIC:
                # Schema-illegal placement — drop the field but keep the role.
                metabolic_context = None

            evidence_list = role_prop.get("evidence") or []
            if not evidence_list:
                # Fabricate one COMPUTATIONAL_PREDICTION citation pointing at the source run
                # so the audit trail is preserved even without primary evidence.
                evidence_list = [{
                    "reference_type": "COMPUTATIONAL_PREDICTION",
                    "reference_text": f"Edison deep-research run (no primary citation given): {source_run}",
                    "curator_note": "Provisional Edison-derived role; primary citation was not extracted.",
                }]

            assignment = _build_assignment(role, confidence, metabolic_context, evidence_list)
            new_assignments.append(assignment)
            applied += 1

        if new_assignments and not dry_run:
            record.setdefault(slot, []).extend(new_assignments)
            fields_changed.append(slot)
            dirty = True

    if dirty:
        _add_curation_event(
            record,
            curator_name,
            fields_changed,
            f"Applied Edison role research results ({source_run})",
        )

    return applied, reasons, dirty


def _summary(applied: int, files_written: int, skipped: list[str], errors: list[str]) -> str:
    lines = [
        f"Role assignments applied: {applied}",
        f"Ingredient records written: {files_written}",
    ]
    if skipped:
        lines.append(f"Records with per-facet skips: {len(skipped)}")
        for line in skipped[:10]:
            lines.append(f"  - {line}")
        if len(skipped) > 10:
            lines.append(f"  - ... {len(skipped) - 10} more")
    if errors:
        lines.append(f"Errors: {len(errors)}")
        for err in errors[:10]:
            lines.append(f"  - {err}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path, help="JSON batch from extract_roles_from_edison.py")
    parser.add_argument("--curator", default=DEFAULT_CURATOR,
                        help=f"Curator name for the curation-history event (default: {DEFAULT_CURATOR})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Compute + report what would apply; write nothing.")
    parser.add_argument("--limit", type=int, default=None,
                        help="Cap number of proposals processed (for smoke tests).")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    if not args.batch.is_file():
        print(f"Batch file not found: {args.batch}", file=sys.stderr)
        return 2

    proposals = _load_batch(args.batch)
    if args.limit is not None:
        proposals = proposals[: args.limit]
    print(f"Loaded {len(proposals)} proposals from {args.batch}")

    total_applied = 0
    total_skipped: list[str] = []
    total_errors: list[str] = []
    # {path: (record_dict, dirty_flag)} — MIM per-ingredient YAMLs are one
    # record per file (top-level mapping, not a `ingredients:` collection).
    records_by_path: dict[Path, dict[str, Any]] = {}
    dirty_paths: set[Path] = set()

    for proposal in proposals:
        ing_path = _resolve_ingredient_path(proposal)
        if ing_path is None:
            total_errors.append(
                f"unresolved ingredient: identifier={proposal.get('ingredient_identifier')!r} "
                f"path={proposal.get('ingredient_path')!r}"
            )
            continue

        if ing_path not in records_by_path:
            try:
                records_by_path[ing_path] = yaml.safe_load(ing_path.read_text()) or {}
            except Exception as exc:
                total_errors.append(f"failed to load {ing_path}: {exc}")
                continue
            if not isinstance(records_by_path[ing_path], dict):
                total_errors.append(f"{ing_path} is not a YAML mapping")
                records_by_path.pop(ing_path)
                continue
        record = records_by_path[ing_path]

        applied, reasons, dirty = _apply_proposal(record, proposal, args.curator, args.dry_run)
        total_applied += applied
        if dirty:
            dirty_paths.add(ing_path)
        for reason in reasons:
            total_skipped.append(f"{ing_path.name}: {reason}")
        if args.verbose:
            print(f"  {ing_path.name}: applied {applied} role(s)")
            for reason in reasons:
                print(f"    - {reason}")

    files_written = 0
    if not args.dry_run:
        for path in dirty_paths:
            path.write_text(yaml.safe_dump(records_by_path[path], sort_keys=False, allow_unicode=True))
            files_written += 1

    print()
    print(_summary(total_applied, files_written, total_skipped, total_errors))
    if args.dry_run:
        print("\n[dry-run] no files were written.")
    return 0 if not total_errors else 1


if __name__ == "__main__":
    sys.exit(main())
