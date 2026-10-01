"""Write review reports for ingredient YAML records missing from the ledger.

This is a dated repair for the September 2026 record-review ledger: the first
ledger covered the mapped record corpus, then later curation added two mapped
records and moved the CMC/PY/horse-serum record back to the unmapped corpus.
The unmapped corpus still needed per-record review reports. Some September
reviews also predated later mapped-record edits; those rows need fresh
content-bound reports instead of reusing stale judgements by path.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import UTC, datetime, timedelta
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "reports" / "yaml_record_review"
MANIFEST = REPORT_DIR / "manifest.tsv"
SEMANTIC_MANIFEST = ROOT / "reports" / "semantic_review_20260921" / "manifest.json"
FIELDNAMES = [
    "path",
    "verdict",
    "severity",
    "reviewed_at",
    "record_sha256",
    "report",
    "notes",
]
SEVERITY_RANK = {"none": 0, "minor": 1, "major": 2, "blocker": 3}
VERDICT_BY_SEVERITY = {
    "none": "pass",
    "minor": "pass_with_minor_issues",
    "major": "needs_curation",
    "blocker": "needs_curation",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def report_slug(stem: str) -> str:
    if re.fullmatch(r"[-._()A-Za-z0-9Α-Ωα-ωß]+", stem):
        return stem
    slug = re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()
    return slug or "record"


def load_manifest() -> list[dict[str, str]]:
    with MANIFEST.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    seen: set[str] = set()
    for row in rows:
        path = row["path"]
        if path in seen:
            raise ValueError(f"duplicate manifest path: {path}")
        seen.add(path)
    return rows


def semantic_record_hashes() -> dict[str, str]:
    manifest = json.loads(SEMANTIC_MANIFEST.read_text())
    inputs = manifest.get("inputs", {})
    return {
        path: digest
        for path, digest in inputs.items()
        if path.startswith("data/ingredients/") and path.endswith(".yaml")
    }


def active_record_paths() -> list[Path]:
    return sorted((ROOT / "data" / "ingredients").glob("*/*.yaml"))


def aggregate_index() -> dict[tuple[str, str], tuple[str, dict]]:
    index: dict[tuple[str, str], tuple[str, dict]] = {}
    for path in sorted((ROOT / "data" / "curated").glob("*.yaml")):
        doc = read_yaml(path)
        if not isinstance(doc, dict) or not isinstance(doc.get("ingredients"), list):
            continue
        for record in doc["ingredients"]:
            key = (record.get("identifier", ""), record.get("preferred_term", ""))
            if key in index:
                raise ValueError(f"duplicate aggregate record for {key}")
            index[key] = (rel(path), record)
    return index


def sssom_rows() -> list[dict[str, str]]:
    rows = [
        line
        for line in (ROOT / "mappings" / "ingredient_mappings.sssom.tsv").read_text().splitlines()
        if line and not line.startswith("#")
    ]
    return list(csv.DictReader(rows, delimiter="\t"))


def current_reviews(
    refresh_limit: int | None,
) -> tuple[list[tuple[Path, dict[str, str] | None, str]], list[dict[str, str]], set[str], int]:
    records = active_record_paths()
    active = {rel(path) for path in records}
    old_rows = load_manifest()
    semantic_hashes = semantic_record_hashes()
    retained: list[dict[str, str]] = []
    stale_legacy: list[tuple[Path, dict[str, str], str]] = []
    filled_legacy_hashes = 0
    reviewed = {row["path"] for row in old_rows if row["path"] in active}

    for row in old_rows:
        path_text = row["path"]
        if path_text not in active:
            continue

        current_row = {field: row.get(field, "") for field in FIELDNAMES}
        if current_row["record_sha256"]:
            retained.append(current_row)
            continue

        semantic_hash = semantic_hashes.get(path_text)
        if not semantic_hash:
            raise ValueError(f"missing September semantic hash for {path_text}")

        path = ROOT / path_text
        current_hash = sha256(path)
        if current_hash == semantic_hash:
            current_row["record_sha256"] = current_hash
            filled_legacy_hashes += 1
            retained.append(current_row)
        else:
            stale_legacy.append((path, current_row, semantic_hash))

    if refresh_limit is None:
        refresh_now = stale_legacy
        deferred = []
    else:
        refresh_now = stale_legacy[:refresh_limit]
        deferred = stale_legacy[refresh_limit:]

    retained.extend(row for _path, row, _old_hash in deferred)
    missing = [(path, None, "") for path in records if rel(path) not in reviewed]
    refresh_targets = [
        (path, previous_row, old_hash)
        for path, previous_row, old_hash in refresh_now
    ]
    stale = {row["path"] for row in old_rows if row["path"] not in active}
    return missing + refresh_targets, retained, stale, filled_legacy_hashes


def manifest_header_matches() -> bool:
    header = MANIFEST.read_text().splitlines()[0].split("\t")
    return header == FIELDNAMES


def source_occurrence_summary(record: dict) -> str:
    stats = record.get("occurrence_statistics") or {}
    total = stats.get("total_occurrences", 0)
    media = stats.get("media_count", 0)
    sources = stats.get("source_occurrences") or []
    if not sources:
        return f"{total} occurrence(s) across {media} medium/media."
    source_text = "; ".join(
        f"{item.get('source', 'unknown')}: {item.get('count', 0)}"
        for item in sources
    )
    return f"{total} active occurrence(s) across {media} medium/media; source rows: {source_text}."


def latest_history(record: dict) -> str:
    history = record.get("curation_history") or []
    if not history:
        return "No curation_history event is present."
    event = history[-1]
    return (
        f"{event.get('action', '<unknown>')} by {event.get('curator', '<unknown>')} "
        f"at {event.get('timestamp', '<unknown>')}: "
        f"{str(event.get('changes', '')).strip() or 'no change summary'}"
    )


def status_review(path: str, record: dict, own_sssom: list[dict[str, str]]) -> tuple[str, str, str, str, list[str]]:
    status = record.get("mapping_status")
    ingredient_type = record.get("ingredient_type", "")
    if status == "MAPPED":
        if path.endswith("Na2-citrate.yaml"):
            notes = (
                "CAS-primary disodium citrate identity, parent broadMatch to citric acid, "
                "Rule B1 registry row, and three reassigned CultureMech occurrences pass."
            )
        elif path.endswith("Nitrilotriacetic_Acid_Trisodium_Salt.yaml"):
            notes = (
                "Restored trisodium nitrilotriacetate identity, CHEBI exact mapping, "
                "chemistry, synonyms, and singleton occurrence pass."
            )
        else:
            notes = "Mapped identity and active SSSOM rows pass the focused review."
        finding = "None found."
        return "pass", "none", notes, finding, []

    if status == "REJECTED":
        notes = "Rejected tombstone is retained for provenance and is not an active mapping target."
        finding = "None found."
        return "pass", "none", notes, finding, []

    if status == "AMBIGUOUS":
        notes = (
            "Record is intentionally AMBIGUOUS after source review showed the flattened "
            "label should not be represented as one CMC/PY/horse-serum mixture."
        )
        finding = (
            f"- **major**: `{path}` has no exact identity mapping because the source "
            "expression remains ambiguous; keep it out of `mappings/ingredient_mappings.sssom.tsv` "
            "until the separate source preparations are represented."
        )
        return "needs_curation", "major", notes, finding, [
            f"Represent the separate source preparations for `{path}` before promoting a mapping."
        ]

    if ingredient_type == "NAMED_MEDIUM":
        notes = (
            "Named medium/formulation is intentionally left unmapped until a "
            "recipe-level CultureMech representation owns the formulation."
        )
        reason = "the label denotes a named medium or formulation rather than one exact chemical substance"
    elif ingredient_type == "UNDEFINED_MIXTURE":
        notes = (
            "Mixture/extract/preparation is intentionally left unmapped until the "
            "source supports a component decomposition or exact preparation identity."
        )
        reason = "the label denotes a mixture, extract, or incompletely specified preparation"
    elif ingredient_type == "SINGLE_INGREDIENT":
        notes = (
            "Specific single-ingredient residual remains unresolved: current evidence "
            "does not support an exact ontology or stable-registry identity."
        )
        reason = "no exact ontology term or independently supported registry identity is recorded"
    else:
        notes = "Unmapped residual lacks an ingredient_type classification."
        reason = "ingredient_type is missing, so the intended unmapped lane is underspecified"
    finding = (
        f"- **major**: `{path}` remains `UNMAPPED`; {reason}. Do not exact-match "
        "it to a broader parent, component, hydrate, salt, or lookalike label."
    )
    return "needs_curation", "major", notes, finding, [
        f"Curate an exact same-form identity or decomposition for `{path}` before mapping it."
    ]


def strict_validation_summary(path_text: str) -> str:
    if "/mapped/" in path_text:
        return (
            "Passed: `just validate-strict data/ingredients/mapped "
            "--out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`."
        )
    return (
        "Passed: `just validate-strict data/ingredients/unmapped "
        "--out /tmp/mim_unmapped_review_validation.tsv --workers 4 --quiet`."
    )


def carry_forward_previous_review(
    *,
    previous_row: dict[str, str] | None,
    previous_sha256: str,
    current_sha256: str,
    verdict: str,
    severity: str,
    notes: str,
    finding: str,
    edits: list[str],
) -> tuple[str, str, str, str, list[str], list[str]]:
    if previous_row is None:
        return verdict, severity, notes, finding, edits, []

    previous_severity = previous_row.get("severity", "none") or "none"
    previous_verdict = (
        previous_row.get("verdict")
        or VERDICT_BY_SEVERITY.get(previous_severity)
        or verdict
    )
    previous_report = previous_row.get("report", "<missing report>")
    previous_notes = previous_row.get("notes", "").strip() or "See the previous report."

    if SEVERITY_RANK.get(previous_severity, 0) >= SEVERITY_RANK.get(severity, 0):
        severity = previous_severity
        verdict = previous_verdict

    if previous_severity != "none":
        finding = (
            f"- **{previous_severity}**: The previous finding set in "
            f"`{previous_report}` was tied to the prior record content; carry "
            "it forward as an unresolved curation floor until a targeted "
            f"current review retires it. Previous summary: {previous_notes}"
        )
        if not edits:
            edits = [
                "Resolve or explicitly retire the findings provisionally carried forward "
                f"from `{previous_report}`."
            ]

    if previous_severity == "none":
        notes = (
            f"Refreshed `{previous_report}` after the record changed from "
            f"{previous_sha256} to {current_sha256}; no prior finding is carried forward."
        )
    else:
        notes = (
            f"Refreshed `{previous_report}` after the record changed from "
            f"{previous_sha256} to {current_sha256}; preserved the previous "
            f"{previous_severity} finding floor pending targeted retirement."
        )
    evidence = [
        f"- Previous review: `{previous_report}`.",
        f"- Previous record SHA-256: `{previous_sha256}`.",
    ]
    return verdict, severity, notes, finding, edits, evidence


def render_report(
    *,
    path: Path,
    record: dict,
    aggregate_path: str,
    aggregate_matches: bool,
    own_sssom: list[dict[str, str]],
    reviewed_at: datetime,
    previous_row: dict[str, str] | None = None,
    previous_sha256: str = "",
) -> tuple[str, dict[str, str]]:
    path_text = rel(path)
    record_hash = sha256(path)
    verdict, severity, notes, finding, edits = status_review(path_text, record, own_sssom)
    verdict, severity, notes, finding, edits, legacy_evidence = carry_forward_previous_review(
        previous_row=previous_row,
        previous_sha256=previous_sha256,
        current_sha256=record_hash,
        verdict=verdict,
        severity=severity,
        notes=notes,
        finding=finding,
        edits=edits,
    )
    status = record.get("mapping_status", "<missing>")
    ontology = record.get("ontology_mapping") or {}
    term_status = (
        "Passed: `just validate-terms "
        f"{path_text}`."
        if ontology.get("ontology_id")
        else "Not checked: this record has no `ontology_mapping.ontology_id`."
    )
    sssom_subject = "MIM:" + path.stem
    sssom_summary = (
        f"{len(own_sssom)} active row(s) for `{sssom_subject}`."
        if own_sssom
        else f"No active row for `{sssom_subject}`, as expected for `{status}`."
    )
    aggregate_status = (
        f"Per-record YAML is identical to its keyed row in `{aggregate_path}`."
        if aggregate_matches
        else f"Major: per-record YAML differs from its keyed row in `{aggregate_path}`."
    )
    if not aggregate_matches:
        severity = "major"
        verdict = "needs_curation"
        aggregate_finding = (
            f"- **major**: `{path_text}` is not synchronized with `{aggregate_path}`."
        )
        edits.insert(
            0,
            f"Synchronize `{path_text}` and `{aggregate_path}` with `just sync-curated` "
            "or an equivalent maintained-input update.",
        )
        if finding == "None found.":
            finding = aggregate_finding
        else:
            finding = f"{finding}\n{aggregate_finding}"

    recommended = edits or ["None."]
    if edits:
        recommended.append(
            "After any edit, run `just sync-curated`, `just validate-strict "
            f"{path_text}`, `just validate-terms {path_text}` where applicable, and `just qc-sssom`."
        )

    evidence_lines = [
        f"- Current record SHA-256: `{record_hash}`.",
        *legacy_evidence,
        f"- Source occurrence traceability: {source_occurrence_summary(record)}",
        f"- Latest curation event: {latest_history(record)}",
        f"- Active SSSOM state: {sssom_summary}",
        f"- Aggregate state: {aggregate_status}",
    ]
    if status == "UNMAPPED":
        evidence_lines.append(
            "- The 2026-09-01 unmapped review explains the residual unmapped policy: "
            "named media, undefined mixtures, and exact single-ingredient residuals "
            "must stay unmapped until exact same-form evidence is available."
        )
    if path.name == "Na2-citrate.yaml":
        evidence_lines.append(
            "- `scripts/apply_669_704_rulings.py` and "
            "`reports/sssom_completion_20260921/mapping_changes/issue669-704-rulings.json` "
            "record the PubChem CID 8950 / CAS 144-33-2 evidence and the split from "
            "`Trisodium_Citrate.yaml`."
        )
    if path.name == "Nitrilotriacetic_Acid_Trisodium_Salt.yaml":
        evidence_lines.append(
            "- `reports/sssom_completion_20260921/mapping_review/issue-intersections.json` "
            "records why the trisodium salt had to be restored as a distinct CHEBI "
            "identity instead of sharing the 0.5 M disodium-stock record."
        )
    if path.name == "CMC_PY_Horse_Serum.yaml":
        evidence_lines.append(
            "- `reports/semantic_review_20260921/resolution/components/README.md` "
            "records the Love et al. 1979 source review that invalidated the former "
            "single CMC/PY/horse-serum component assertion."
        )

    text = f"""# YAML Record Review: {record.get('preferred_term', path.stem)}

- Repository: CultureBotAI/MediaIngredientMech
- Record: `{path_text}`
- Started UTC: {reviewed_at.isoformat().replace('+00:00', 'Z')}
- Finished UTC: {(reviewed_at + timedelta(seconds=1)).isoformat().replace('+00:00', 'Z')}
- Verdict: {verdict}

## Target

- Class: `IngredientRecord`
- Path: `{path_text}`
- Identifier: `{record.get('identifier', '<missing>')}`
- Preferred term: {record.get('preferred_term', '<missing>')}
- Mapping status: `{status}`
- Ingredient type: `{record.get('ingredient_type', '<missing>')}`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- {strict_validation_summary(path_text)}
- {term_status}
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `{status}`.
- Ontology ID: `{ontology.get('ontology_id', 'None')}`.
- Ontology label: `{ontology.get('ontology_label', 'None')}`.
- Mapping quality: `{ontology.get('mapping_quality', 'None')}`.
- Active SSSOM rows for this subject: {len(own_sssom)}.
- Identity judgement: {notes}

## Evidence

{chr(10).join(evidence_lines)}

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- {aggregate_status}
- Consequential unresolved item: {notes if verdict == 'needs_curation' else 'None found.'}

## Findings

{finding}

## Recommended Edits

{chr(10).join(f'- {item}' for item in recommended)}

## Follow-up Checks

- Re-run strict schema validation on `{path_text}` after any future curation edit.
- Re-run `just validate-terms {path_text}` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
"""

    row = {
        "path": path_text,
        "verdict": verdict,
        "severity": severity,
        "reviewed_at": reviewed_at.isoformat().replace("+00:00", "Z"),
        "report": "",
        "notes": notes,
        "record_sha256": record_hash,
    }
    return text, row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--limit",
        type=int,
        help="Refresh at most this many stale legacy reviews in one run.",
    )
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error("--limit must be non-negative")
    return args


def main() -> None:
    args = parse_args()
    targets, retained, stale, filled_legacy_hashes = current_reviews(args.limit)
    if not targets and not stale and not filled_legacy_hashes and manifest_header_matches():
        print("manifest already matches active records")
        return

    aggregate = aggregate_index()
    sssom_by_subject: dict[str, list[dict[str, str]]] = {}
    for row in sssom_rows():
        sssom_by_subject.setdefault(row["subject_id"], []).append(row)

    now = datetime.now(UTC).replace(microsecond=0)
    new_rows: list[dict[str, str]] = []
    for offset, (path, previous_row, previous_sha256) in enumerate(targets):
        record = read_yaml(path)
        key = (record.get("identifier", ""), record.get("preferred_term", ""))
        aggregate_path, aggregate_record = aggregate.get(key, ("", {}))
        if not aggregate_path:
            raise ValueError(f"missing aggregate row for {rel(path)}")
        reviewed_at = now + timedelta(seconds=offset)
        text, row = render_report(
            path=path,
            record=record,
            aggregate_path=aggregate_path,
            aggregate_matches=aggregate_record == record,
            own_sssom=sssom_by_subject.get("MIM:" + path.stem, []),
            reviewed_at=reviewed_at,
            previous_row=previous_row,
            previous_sha256=previous_sha256,
        )
        report = REPORT_DIR / f"{reviewed_at:%Y%m%dT%H%M%SZ}-{report_slug(path.stem)}.md"
        if report.exists():
            raise FileExistsError(report)
        row["report"] = rel(report)
        report.write_text(text)
        new_rows.append(row)

    rows = sorted(retained + new_rows, key=lambda row: row["path"])
    with MANIFEST.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, FIELDNAMES, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(new_rows)} review reports")
    print(f"filled {filled_legacy_hashes} unchanged legacy record hashes")
    print(f"removed {len(stale)} stale manifest rows")


if __name__ == "__main__":
    main()
