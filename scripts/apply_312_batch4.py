#!/usr/bin/env python3
"""Finish the verified #312 batch-4 merges around ``merge_mapped_records.py``.

Two #312 proposals are merges under MAPPING_SEMANTICS.md Section 3 ("two
records share one identifier or one substance sits under two identifiers ->
same substance -> merge"), each re-verified against ``chebi.db``:

* ``Cinnamic_Acid`` (CHEBI:27386, geometry-unspecified) into
  ``Trans-cinnamic_Acid`` (CHEBI:35697). The record's only source-supplied
  identity is CAS 140-10-3, which ChEBI xrefs on the trans term only; the
  geometry-free term's sole CAS is 621-82-9. Section 3 step 4's evidence hatch
  picks the trans isomer, and that term is already held, so it is a merge.
* ``Nah2po4h2o`` (cas:10049-21-5, ``NaH2PO4•H2O``) into
  ``Sodium_phosphate_monobasic_monohydrate`` (CHEBI:114249). The 2026-08-06
  promotion used the step-2 ``cas:`` fallback on the premise that ChEBI has no
  monohydrate term; CHEBI:114249 'sodium dihydrogenphosphate monohydrate'
  exists, xrefs that very CAS, and is already held.

The third merge proposal, ``6-deoxy-d-galactose`` into ``D-fucose``, sits at
SSSOM row 286, before the position-bound frozen release hold, and is blocked
by #745.

The maintained helper does the merge itself (synonyms carried as RAW_TEXT,
occurrence counts transferred, source tombstoned REJECTED, its SSSOM rows
dropped, survivor ``other`` extended). This script does what the helper
leaves to the caller, in order:

1. ``--post-merge`` (after the helper and ``just sync-individual``): re-point
   each tombstone's identifier to the survivor's, so Rule K credits the
   merged name to the live record (the #414 precedent for Mgcl2x_6_H2o);
   retype the carried ``3-phenylprop-2-enoic acid`` REJECTED_LABEL on the
   trans record, because it is the exact synonym of the geometry-free parent,
   not of the trans isomer; record the source-supplied CAS in an evidence
   note. Then ``just sync-curated``.
2. ``--finish-sssom``: scrub REJECTED_LABEL tokens from the survivors' rows
   and keep the #403 CAS-token rule.
3. ``--finish-artifacts --occurrences PATH``: add the recipe-membership edges
   the merged ``NaH2PO4•H2O`` occurrences now contribute to CHEBI:114249
   (they were never in the artifact, which predates the cas: record), so the
   transferred counts stay reproducible from the edges.

Every step is idempotent. ``--log`` writes the apply log the review-chain
receipt is built from.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.culturemech_occurrences import (  # noqa: E402
    SOURCE_LABEL_IDENTIFIER_OVERRIDES,
    _source_label_key,
)
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

MAPPED = ROOT / "data" / "ingredients" / "mapped"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
ISSUE = "#312"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-22"
EVIDENCE_SOURCE = "MIM curation (#312); chebi.db"


@dataclass(frozen=True)
class Merge:
    source_slug: str
    source_identifier: str
    target_slug: str
    target_identifier: str
    reason: str
    reject_on_target: tuple[tuple[str, str], ...] = ()
    target_note: str | None = None
    source_labels: tuple[str, ...] = ()  # CultureMech labels whose edges now belong to the target


MERGES: tuple[Merge, ...] = (
    Merge(
        "Cinnamic_Acid", "CHEBI:27386", "Trans-cinnamic_Acid", "CHEBI:35697",
        "The record's only source-supplied identity is CAS 140-10-3 (CultureBotHT), which ChEBI "
        "xrefs on CHEBI:35697 trans-cinnamic acid only; the geometry-unspecified CHEBI:27386's "
        "sole CAS is 621-82-9. Section 3 step 4's evidence hatch picks the trans isomer, which "
        "Trans-cinnamic_Acid already holds, so the two records denote one substance (#312).",
        reject_on_target=(("3-phenylprop-2-enoic acid", "the exact synonym of the geometry-unspecified parent CHEBI:27386, not of the trans isomer"),),
        target_note=(
            "Absorbed Cinnamic_Acid (#312). Its CAS 140-10-3 is a second ChEBI xref of CHEBI:35697 "
            "alongside the recorded 621-82-9; both denote trans-cinnamic acid. The carried synonym "
            "'3-phenylprop-2-enoic acid' names the geometry-free parent and is REJECTED_LABEL."
        ),
    ),
    Merge(
        "Nah2po4h2o", "cas:10049-21-5", "Sodium_phosphate_monobasic_monohydrate", "CHEBI:114249",
        "The 2026-08-06 promotion used the Section 3 step 2 cas: fallback on the premise that "
        "ChEBI has no hydrate term. CHEBI:114249 'sodium dihydrogenphosphate monohydrate' "
        "(H2O.H2O4P.Na, InChIKey BBMHARZCALWXSL-UHFFFAOYSA-M) exists and xrefs cas:10049-21-5, "
        "the very CAS the record was keyed on, and Sodium_phosphate_monobasic_monohydrate already "
        "holds it: one substance under two identifiers -> merge (#312).",
        target_note=(
            "Absorbed Nah2po4h2o (#312): the raw labels 'NaH2PO4•H2O' and 'NaH2PO4•H2O(MCIB 742)' "
            "and their 4 CultureMech occurrences now belong here; the cas: identity was the step-2 "
            "fallback for a term that exists."
        ),
        source_labels=("NaH2PO4•H2O", "NaH2PO4•H2O(MCIB 742)"),
    ),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(slug: str) -> tuple[Path, dict]:
    path = MAPPED / f"{slug}.yaml"
    return path, yaml.safe_load(path.read_text())


def post_merge(log: list, write: bool) -> None:
    for spec in MERGES:
        for label in spec.source_labels:
            if SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(_source_label_key(label)) != spec.target_identifier:
                raise SystemExit(f"SOURCE_LABEL_IDENTIFIER_OVERRIDES lacks {label!r} -> {spec.target_identifier}")
        # tombstone
        path, record = load(spec.source_slug)
        if record.get("mapping_status") != "REJECTED":
            raise SystemExit(f"{spec.source_slug} is not REJECTED yet; run merge_mapped_records.py first")
        if record["identifier"] != spec.target_identifier:
            before = _git_head_sha(path)
            old = record["identifier"]
            record["identifier"] = spec.target_identifier
            record_curation_event(
                record, curator=CURATOR, action="CORRECTED",
                changes=(f"identifier {old} -> {spec.target_identifier} on the merge tombstone, so the merged "
                         f"name is credited to the live record that holds the identifier (Rule K; the #414 "
                         f"Mgcl2x_6_H2o precedent). {spec.reason}"),
                previous_status="REJECTED", new_status="REJECTED", llm_assisted=True, llm_model=LLM_MODEL,
            )
            print(f"TOMBSTONE {spec.source_slug}: identifier {old} -> {spec.target_identifier}")
            if write:
                write_validated_ingredient(record, path)
            log.append({"source_record": str(path.relative_to(ROOT)), "shape": "merge_tombstone",
                        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                        "change": f"merged into {spec.target_slug}; mapping_status REJECTED; identifier {old} -> {spec.target_identifier}",
                        "verification": spec.reason})
        else:
            print(f"SKIP      {spec.source_slug}: tombstone already re-pointed")
        # survivor
        path, record = load(spec.target_slug)
        before = _git_head_sha(path)
        changed = []
        for text, why in spec.reject_on_target:
            for synonym in record.get("synonyms") or []:
                if synonym.get("synonym_text") == text and synonym.get("synonym_type") != "REJECTED_LABEL":
                    synonym["synonym_type"] = "REJECTED_LABEL"
                    changed.append(f"'{text}' -> REJECTED_LABEL ({why})")
        mapping = record["ontology_mapping"]
        if spec.target_note and not any(spec.target_note == e.get("notes") for e in mapping.get("evidence") or []):
            mapping.setdefault("evidence", []).append(
                {"evidence_type": "MANUAL_CURATION", "source": EVIDENCE_SOURCE, "notes": spec.target_note}
            )
            changed.append("evidence note added")
        if changed:
            record_curation_event(
                record, curator=CURATOR, action="CORRECTED",
                changes="; ".join(changed) + f". {spec.reason}",
                previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
            )
            print(f"SURVIVOR  {spec.target_slug}: {'; '.join(changed)}")
            if write:
                write_validated_ingredient(record, path)
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "merge_survivor",
                    "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                    "change": f"absorbed {spec.source_slug} (synonyms, occurrences); " + ("; ".join(changed) or "no further change"),
                    "verification": spec.reason})


def _git_head_sha(path: Path) -> str:
    blob = subprocess.run(["git", "show", f"HEAD:{path.relative_to(ROOT)}"], capture_output=True, cwd=ROOT, check=True).stdout
    return hashlib.sha256(blob).hexdigest()


# --- SSSOM ------------------------------------------------------------------


def _read_rows() -> tuple[list[str], list[str], list[dict]]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    return comments, list(reader.fieldnames or []), list(reader)


def _write_rows(comments: list[str], fields: list[str], rows: list[dict]) -> None:
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    SSSOM.write_text(out.getvalue(), encoding="utf-8")


def _stamp(row: dict, note: str, method: str) -> None:
    row["mapping_date"] = MAPPING_DATE
    row["comment"] = (row["comment"] + " " + note).strip()
    row["validation_method"] = f"manual:apply_312_batch4|{method}|{MAPPING_DATE}"


def finish_sssom() -> None:
    comments, fields, rows = _read_rows()
    targets = {f"MIM:{spec.target_slug}": load(spec.target_slug)[1] for spec in MERGES}
    stale = [r for r in rows if r["subject_id"] in {f"MIM:{spec.source_slug}" for spec in MERGES}]
    if stale:
        raise SystemExit(f"{len(stale)} row(s) still name a merged subject; reconcile first")
    scrubbed = cas_fixed = 0
    for row in rows:
        record = targets.get(row["subject_id"])
        if not record:
            continue
        rejected = {s["synonym_text"] for s in record.get("synonyms") or [] if s.get("synonym_type") == "REJECTED_LABEL"}
        tokens = [t for t in row["other"].split("|") if t]
        keep = [t for t in tokens if t not in rejected]
        if keep != tokens:
            row["other"] = "|".join(keep)
            _stamp(row, f"[other: dropped {[t for t in tokens if t in rejected]}: REJECTED_LABEL on the record ({ISSUE})]", "OTHER")
            scrubbed += 1
        cas_rn = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
        tokens = [t for t in row["other"].split("|") if t]
        symmetric = row["predicate_id"] in {"skos:exactMatch", "skos:closeMatch"}
        if symmetric and cas_rn:
            wanted = [t for t in tokens if not t.upper().startswith("CAS:")] + [f"CAS:{cas_rn}"]
            if tokens != wanted:
                row["other"] = "|".join(wanted)
                _stamp(row, f"[other: CAS token follows the record's cas_rn on a symmetric row, #403 ({ISSUE})]", "OTHER")
                cas_fixed += 1
    _write_rows(comments, fields, rows)
    print(f"rejected tokens scrubbed from {scrubbed} row(s); CAS tokens fixed on {cas_fixed} row(s)")


# --- membership ---------------------------------------------------------------


def add_membership_edges(occurrences: Path) -> int:
    """Add the merged labels' recipe edges to the survivor's identifier (kept sorted)."""
    wanted = {}
    for spec in MERGES:
        for label in spec.source_labels:
            wanted[_source_label_key(label)] = spec.target_identifier
    edges: dict[tuple[str, str], int] = {}
    with occurrences.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            target = wanted.get(_source_label_key(row.get("preferred_term") or ""))
            if target:
                edges[(target, row["recipe_id"])] = edges.get((target, row["recipe_id"]), 0) + 1
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments, header, data = [], None, []
    for line in lines:
        if line.startswith("#"):
            comments.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if header is None:
            header = cells
            continue
        data.append(cells)
    existing = {(c[0], c[1]): i for i, c in enumerate(data)}
    added = 0
    for (identifier, recipe), count in sorted(edges.items()):
        if (identifier, recipe) in existing:
            continue
        data.append([identifier, recipe, str(count)])
        added += 1
    data.sort(key=lambda cells: tuple(cells[:2]))
    MEMBERSHIP.write_text("".join(comments) + "\t".join(header) + "\n" + "".join("\t".join(c) + "\n" for c in data), encoding="utf-8")
    print(f"membership edges added: {added}")
    return added


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--post-merge", action="store_true", help="after merge_mapped_records.py + sync-individual")
    parser.add_argument("--apply", action="store_true", help="write (default: dry-run) for --post-merge")
    parser.add_argument("--log", type=Path, help="apply-log JSON path (written with --post-merge --apply)")
    parser.add_argument("--finish-sssom", action="store_true")
    parser.add_argument("--finish-artifacts", action="store_true")
    parser.add_argument("--occurrences", type=Path)
    args = parser.parse_args()
    if args.post_merge:
        log: list = []
        post_merge(log, args.apply)
        if args.apply and args.log:
            args.log.write_text(json.dumps({"issue": ISSUE, "batch": "batch4", "records": log}, indent=2) + "\n")
            print(f"apply log: {args.log}")
        return 0
    if args.finish_sssom:
        finish_sssom()
        return 0
    if args.finish_artifacts:
        if not args.occurrences:
            raise SystemExit("--finish-artifacts needs --occurrences")
        add_membership_edges(args.occurrences)
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
