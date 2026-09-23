#!/usr/bin/env python3
"""Apply the verified #312 batch-3 corrections: five registry mints.

Batches 1 and 2 (#739, #746) held the regrades, parent re-anchors and identity
re-groundings. This batch holds the records whose identifier was a term they
are *narrower* than: a specific recipe on the class of all trace-element
solutions, a purified oat polysaccharide on the linkage-agnostic glucan class,
a vitamin-assay grade on the generic casamino acids, and two malformed
MediaDive hydrate labels sharing the anhydrous salt's identifier with the
anhydrous record. The sixth, ``Cooked meat medium`` (a formulated anaerobe
medium grounded to the food "meat (cooked)"), is deferred: two mixtures
reference that FOODON identifier as a MIM_CATALOG part and both are pinned
byte-for-byte by the resolution review's component ledger and a completion
cohort approval (see the #312 deferral issue).

MAPPING_SEMANTICS.md Section 3 step 3: no exact term and no CAS of its own, so
mint ``kgmicrobe.ingredient:<slug>`` (materials, recipes) or
``kgmicrobe.compound:<slug>`` (pure compounds), ``broadMatch`` to the nearest
parent, and publish the Rule B1 registry row. The malformed hydrates follow
the #344 shape instead (``closeMatch`` to the anhydrous parent, chemistry
blanked, anhydrous aliases ``REJECTED_LABEL``).

Because these records shared CultureMech's resolved identifier with siblings
(``CHEBI:23414`` with ``CuSO4``, ``MICRO:0000455`` with the WC solution), the
recipe membership and occurrence counts follow the *source label* through
``SOURCE_LABEL_IDENTIFIER_OVERRIDES``; ``--finish-artifacts`` rebuilds the
membership edges for the labels the overrides now own (#344 shape), refreshes the affected records'
``occurrence_statistics`` from it, and updates ``hydrate_review.tsv``.

Dry-run by default; ``--apply`` writes the records and an apply log;
``--finish-sssom`` (after ``reconcile_sssom --apply``) adds the registry rows,
turns the remapped food row into the identity row, and scrubs rejected tokens; ``--finish-artifacts`` does the
membership / occurrence / hydrate-review work.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
from collections import defaultdict
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
HYDRATE_REVIEW = ROOT / "mappings" / "hydrate_review.tsv"
ISSUE = "#312"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-22"
EVIDENCE_SOURCE = "MIM curation (#312); chebi.db"


@dataclass(frozen=True)
class Mint:
    slug: str
    old_identifier: str
    new_identifier: str
    ontology_id: str  # the parent, or the registry id itself for a registry-only record
    ontology_label: str
    ontology_source: str
    old_quality: str
    new_quality: str
    rationale: str
    old_ontology_id: str | None = None
    reject_synonyms: tuple[str, ...] = ()
    blank_chemistry: bool = False
    drop_node_id: bool = False
    supersede_sources: tuple[str, ...] = ()
    drop_ontology_row: str | None = None  # an ontology row to remove outright
    source_labels: tuple[str, ...] = ()  # CultureMech source labels this record owns
    hydrate_review: bool = False
    mediadive_compound_id: str = ""


MINTS: tuple[Mint, ...] = (
    Mint(
        "Algal_Trace_Elements_Solution", "MICRO:0000455",
        "kgmicrobe.ingredient:algal_trace_elements_solution",
        "MICRO:0000455", "trace elements solution", "MICRO", "LEXICAL_MATCH", "NARROW_MATCH",
        "MICRO:0000455 'trace elements solution' is a class ('a solution of trace elements ..., "
        "sometimes also having an organic chelator'), and two MIM records held it as their "
        "identifier (this one and WC Trace Elements Solution): two different recipes collapsed "
        "onto one node. This is the UTEX algal trace-element recipe, a specific formulation. "
        "Section 3 step 3: mint a registry identity, broadMatch to the class, the "
        "Proteose_Peptone_No_2 shape.",
        supersede_sources=("MICRO via OLS (resolve_unmapped_v2 strategy=stem-match)",),
        source_labels=("Algal Trace Elements Solution",),
    ),
    Mint(
        "B-Glucan_From_Oat", "CHEBI:28793", "kgmicrobe.ingredient:b-glucan_from_oat",
        "CHEBI:18504", "(1->3,1->4)-beta-D-glucan", "CHEBI", "CAS_RN_LOOKUP", "NARROW_MATCH",
        "CHEBI:28793 'beta-D-glucan' is the linkage-agnostic class with 18 subclasses "
        "(cellulose, nitrocellulose, schizophyllan, ...); an exactMatch licensed substituting "
        "oat beta-glucan for the whole class, and MIM:Cellulose already sits under it. Oat "
        "beta-glucan is the mixed-linkage (1->3,1->4)-beta-D-glucan, CHEBI:18504, and the "
        "record is source-qualified ('from Oat'), so it is narrower than that term too. "
        "Section 3 step 3, the Amylopectin_From_Maize / Lichenan shape: registry identity, "
        "broadMatch CHEBI:18504. CAS 9041-22-9 is the generic beta-glucan registration "
        "(ChEBI xrefs it on CHEBI:28793) and stays in chemical_properties as such.",
        supersede_sources=("CultureBotHT",),
    ),
    Mint(
        "Casamino_Acids_Vitamin_Assay", "mesh:C017721",
        "kgmicrobe.ingredient:casamino_acids_vitamin_assay",
        "mesh:C017721", "casamino acids", "MESH", "LEXICAL_MATCH", "NARROW_MATCH",
        "mesh:C017721 'casamino acids' is the generic acid-hydrolysed casein (scope note "
        "'acid hydrolyzed casein'); this record is the vitamin-depleted Difco/BD vitamin-assay "
        "grade, ordered separately, and MIM holds a separate generic Casamino_Acids record. An "
        "exactMatch collapsed a narrower product into its parent. Section 3 step 3: registry "
        "identity, broadMatch to the MeSH descriptor.",
        supersede_sources=("MESH via OLS (resolve_unmapped_v2 strategy=stem-match)",),
        source_labels=("Casamino acids, vitamin assay (BD-Difco)", "Casamino acids, vitamin assay (Difco)"),
    ),
    Mint(
        "Cuso4_X_4_H2o", "CHEBI:23414", "kgmicrobe.compound:cuso4_x_4_h2o",
        "CHEBI:23414", "copper(II) sulfate", "CHEBI", "EXACT_MATCH", "CLOSE_MATCH",
        "CuSO4 x 4 H2O is a MediaDive label for a hydration state no source verifies "
        "(hydrate_review: 'Probably CuSO4 x 5 H2O; no stable copper(II) sulfate tetrahydrate'). "
        "It shared CHEBI:23414 'copper(II) sulfate' with the anhydrous CuSO4 record and the "
        "dihydrate label, pooling 187 recipe memberships across three records. The #344 "
        "malformed-hydrate shape (Caso4_X_7_H2o, Cucl2_X_6_H2o): local identity, closeMatch to "
        "the anhydrous parent, chemistry blank until the upstream count is corrected, anhydrous "
        "aliases REJECTED_LABEL, memberships only for recipes whose source label names this row.",
        reject_synonyms=("cupric sulfate anhydrous", "copper(2+) sulfate"),
        blank_chemistry=True, drop_node_id=True,
        supersede_sources=("CultureMech",),
        source_labels=("CuSO4 x 4 H2O",),
        hydrate_review=True, mediadive_compound_id="MediaDive compound for 'CuSO4 x 4 H2O'",
    ),
    Mint(
        "Cuso4_X_2_H2o", "CHEBI:23414", "kgmicrobe.compound:cuso4_x_2_h2o",
        "CHEBI:23414", "copper(II) sulfate", "CHEBI", "SYNONYM_MATCH", "CLOSE_MATCH",
        "CuSO4 x 2 H2O is a MediaDive label for a hydration state no source verifies "
        "(hydrate_review: WRONG_TERM_ANHYDROUS, 'Probably CuSO4 x 5 H2O; phase studies "
        "establish the pentahydrate'). It shared CHEBI:23414 with the anhydrous CuSO4 record; "
        "the 2026-08-10 regrade to SYNONYM_MATCH still published exactMatch. The #344 "
        "malformed-hydrate shape: local identity, closeMatch to the anhydrous parent, "
        "chemistry blank, anhydrous aliases REJECTED_LABEL, memberships only for recipes whose "
        "source label names this row ('CuSO4 x 2 H2O', 'CuSO4 . 2H2O').",
        reject_synonyms=("cupric sulfate anhydrous", "copper(2+) sulfate"),
        blank_chemistry=True, drop_node_id=True,
        supersede_sources=("CultureMech",),
        source_labels=("CuSO4 x 2 H2O", "CuSO4 . 2H2O"),
        hydrate_review=True, mediadive_compound_id="MediaDive compound 719",
    ),
)

# Every identifier whose memberships move in this batch: the minted ones plus the
# siblings that used to pool them.
AFFECTED_IDENTIFIERS = {spec.new_identifier for spec in MINTS} | {"CHEBI:23414", "MICRO:0000455"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(slug: str) -> tuple[Path, dict]:
    path = MAPPED / f"{slug}.yaml"
    return path, yaml.safe_load(path.read_text())


def evidence(notes: str) -> dict:
    return {"evidence_type": "MANUAL_CURATION", "source": EVIDENCE_SOURCE, "notes": notes}


def verify() -> None:
    """The overrides this batch relies on must be in place, and no active record may hold a minted id."""
    problems = []
    for spec in MINTS:
        for label in spec.source_labels:
            if SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(_source_label_key(label)) != spec.new_identifier:
                problems.append(f"{spec.slug}: SOURCE_LABEL_IDENTIFIER_OVERRIDES lacks {label!r} -> {spec.new_identifier}")
    holders = defaultdict(list)
    for path in (ROOT / "data" / "ingredients").glob("*/*.yaml"):
        record = yaml.safe_load(path.read_text()) or {}
        if record.get("mapping_status") != "REJECTED":
            holders[record.get("identifier")].append(path.stem)
    for spec in MINTS:
        others = [h for h in holders.get(spec.new_identifier, []) if h != spec.slug]
        if others:
            problems.append(f"{spec.slug}: {spec.new_identifier} already held by {others}")
    if problems:
        raise SystemExit("Preconditions fail:\n  " + "\n  ".join(problems))


def apply_mint(spec: Mint, log: list, write: bool) -> None:
    path, record = load(spec.slug)
    mapping = record["ontology_mapping"]
    if record["identifier"] == spec.new_identifier:
        print(f"SKIP     {spec.slug}: already {spec.new_identifier}")
        return
    assert record["identifier"] == spec.old_identifier, (spec.slug, record["identifier"])
    assert mapping["mapping_quality"] == spec.old_quality, (spec.slug, mapping["mapping_quality"])
    before = sha(path)
    old_ontology = (mapping["ontology_id"], mapping.get("ontology_label"))
    record["identifier"] = spec.new_identifier
    mapping["ontology_id"] = spec.ontology_id
    mapping["ontology_label"] = spec.ontology_label
    mapping["ontology_source"] = spec.ontology_source
    mapping["mapping_quality"] = spec.new_quality
    for entry in mapping.get("evidence") or []:
        if entry.get("source") in spec.supersede_sources and not str(entry.get("notes", "")).startswith("SUPERSEDED"):
            entry["notes"] = f"SUPERSEDED ({ISSUE}): " + str(entry.get("notes", ""))
    rejected = []
    for synonym in record.get("synonyms") or []:
        if synonym.get("synonym_text") in spec.reject_synonyms and synonym.get("synonym_type") != "REJECTED_LABEL":
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected.append(synonym["synonym_text"])
    if spec.blank_chemistry and record.get("chemical_properties"):
        record["chemical_properties"] = {}
    if spec.drop_node_id and record.get("kg_microbe_node_id"):
        record.pop("kg_microbe_node_id")
    note = (
        f"identifier {spec.old_identifier} -> {spec.new_identifier}; ontology {old_ontology[0]} ('{old_ontology[1]}') "
        f"-> {spec.ontology_id} ('{spec.ontology_label}'); mapping_quality {spec.old_quality} -> {spec.new_quality}. "
        + spec.rationale
    )
    mapping.setdefault("evidence", []).append(evidence(note))
    changes = note + f" ({ISSUE})"
    if rejected:
        changes += " REJECTED_LABEL: " + ", ".join(rejected) + "."
    if spec.blank_chemistry:
        changes += " chemical_properties blanked: the recorded structure was the anhydrous salt's."
    record_curation_event(
        record, curator=CURATOR, action="MINTED_REGISTRY_IDENTIFIER", changes=changes,
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
    )
    print(f"MINT     {spec.slug}: {spec.old_identifier} -> {spec.new_identifier} [{spec.new_quality} -> {spec.ontology_id}] rejected={rejected}")
    if write:
        write_validated_ingredient(record, path)
    log.append({
        "source_record": str(path.relative_to(ROOT)), "shape": "registry_mint",
        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
        "change": f"identifier {spec.old_identifier} -> {spec.new_identifier}; ontology_id {old_ontology[0]} -> {spec.ontology_id}; mapping_quality {spec.old_quality} -> {spec.new_quality}",
        "verification": spec.rationale,
    })


def rescope_components(log: list, write: bool) -> None:
    """A part that referenced the medium's old FOODON identifier is the food itself, an external term."""
    retired = {spec.old_identifier: spec for spec in MINTS if spec.old_identifier == spec.drop_ontology_row}
    for path in sorted((ROOT / "data" / "ingredients").glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text()) or {}
        hits = [
            (index, component)
            for index, component in enumerate(record.get("components") or [])
            if component.get("component_id") in retired and component.get("reference_scope") == "MIM_CATALOG"
        ]
        if not hits:
            continue
        before = sha(path)
        notes = []
        for index, component in hits:
            component["reference_scope"] = "EXTERNAL_TERM"
            notes.append(f"components[{index}] '{component.get('component_name')}' {component['component_id']} reference_scope MIM_CATALOG -> EXTERNAL_TERM")
        changes = (
            "; ".join(notes)
            + f": the MIM record that held that identifier was a formulated medium, not the food; the part is the "
              f"FOODON term itself ({ISSUE})."
        )
        record_curation_event(record, curator=CURATOR, action="RESCOPED_COMPONENT", changes=changes,
                              llm_assisted=True, llm_model=LLM_MODEL)
        print(f"COMPONENT {path.stem}: {'; '.join(notes)}")
        if write:
            write_validated_ingredient(record, path)
        log.append({
            "source_record": str(path.relative_to(ROOT)), "shape": "component_rescope",
            "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
            "change": "; ".join(notes),
            "verification": "The component names cooked meat, the food; only the reference scope changes.",
        })


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
    row["validation_method"] = f"manual:apply_312_batch3|{method}|{MAPPING_DATE}"


def finish_sssom() -> None:
    comments, fields, rows = _read_rows()
    by_slug = {spec.slug: spec for spec in MINTS}
    records = {slug: load(slug)[1] for slug in by_slug}
    dropped = scrubbed = added = synced = cas_fixed = 0
    kept = []
    for row in rows:
        slug = row["subject_id"][4:] if row["subject_id"].startswith("MIM:") else None
        spec = by_slug.get(slug)
        if not spec:
            kept.append(row)
            continue
        if spec.drop_ontology_row and row["object_id"] == spec.drop_ontology_row:
            dropped += 1
            continue
        record = records[slug]
        if row["object_id"] == record["identifier"]:
            # Rule D: the identity row is exactMatch whatever the ontology grade says.
            want = ("skos:exactMatch", "semapv:ManualMappingCuration", "0.99")
            have = (row["predicate_id"], row["mapping_justification"], row["confidence"])
            if have != want:
                row["predicate_id"], row["mapping_justification"], row["confidence"] = want
                row["object_label"] = record["preferred_term"]
                row["object_source"] = "kgm:" + record["identifier"].split(":")[0].split(".")[1]
                row["comment"] = f"Registry/identity row: local identity for a formulated medium with no whole-substance ontology term ({ISSUE})."
                _stamp(row, f"[own-identifier row: exactMatch per Rule D ({ISSUE})]", "REGISTRY")
                synced += 1
        rejected = {s["synonym_text"] for s in record.get("synonyms") or [] if s.get("synonym_type") == "REJECTED_LABEL"}
        tokens = [t for t in row["other"].split("|") if t]
        keep_tokens = [t for t in tokens if t not in rejected]
        if keep_tokens != tokens:
            row["other"] = "|".join(keep_tokens)
            _stamp(row, f"[other: dropped {[t for t in tokens if t in rejected]}: REJECTED_LABEL on the record ({ISSUE})]", "OTHER")
            scrubbed += 1
        # #403: the orderable CAS travels in `other` on symmetric rows only.
        cas_rn = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
        tokens = [t for t in row["other"].split("|") if t]
        symmetric = row["predicate_id"] in {"skos:exactMatch", "skos:closeMatch"}
        if symmetric and cas_rn:
            wanted = [t for t in tokens if not t.upper().startswith("CAS:")] + [f"CAS:{cas_rn}"]
            if tokens != wanted:
                row["other"] = "|".join(wanted)
                _stamp(row, f"[other: CAS token follows the record's cas_rn on a symmetric row, #403 ({ISSUE})]", "OTHER")
                cas_fixed += 1
        elif not symmetric and any(t.upper().startswith("CAS:") for t in tokens):
            row["other"] = "|".join(t for t in tokens if not t.upper().startswith("CAS:"))
            _stamp(row, f"[other: CAS token removed from an asymmetric row, #403 ({ISSUE})]", "OTHER")
            cas_fixed += 1
        kept.append(row)
    rows = kept
    existing = {(r["subject_id"], r["object_id"]) for r in rows}
    for spec in MINTS:
        record = records[spec.slug]
        subject = f"MIM:{spec.slug}"
        if (subject, spec.new_identifier) in existing:
            continue
        parent_rows = [r for r in rows if r["subject_id"] == subject]
        source = (parent_rows[0]["source"] if parent_rows else "MIM:MIM curation (#312)") + "|MIM:curator=claude"
        prefix = spec.new_identifier.split(":")[0]
        if spec.ontology_id == spec.new_identifier:
            comment = f"Registry/identity row: local {prefix} identity for a formulated medium with no whole-substance ontology term ({ISSUE})."
        elif spec.new_quality == "CLOSE_MATCH":
            comment = f"Registry/identity row preserving {spec.new_identifier} alongside anhydrous parent {spec.ontology_id}."
        else:
            comment = f"Registry/identity row (Rule B1) for broadMatch subject; kg-microbe primary id {spec.new_identifier} alongside parent {spec.ontology_id}."
        cas_rn = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
        rows.append({
            "subject_id": subject, "subject_label": record["preferred_term"], "predicate_id": "skos:exactMatch",
            "object_id": spec.new_identifier, "object_label": record["preferred_term"],
            "object_source": "kgm:" + prefix.split(".")[1], "mapping_justification": "semapv:ManualMappingCuration",
            "source": source, "mapping_date": MAPPING_DATE, "confidence": "0.99", "comment": comment,
            "other": f"CAS:{cas_rn}" if cas_rn else "",
            "validation_method": f"manual:apply_312_batch3|REGISTRY|{MAPPING_DATE}",
        })
        added += 1
    _write_rows(comments, fields, rows)
    print(f"ontology rows dropped {dropped}; own-identifier rows synced {synced}; registry rows added {added}; "
          f"rejected tokens scrubbed from {scrubbed} row(s); CAS tokens fixed on {cas_fixed} row(s)")


# --- membership, occurrence counts, hydrate review --------------------------


def move_memberships(occurrences: Path) -> dict[str, int]:
    """Move only the edges whose source label this batch's overrides now own.

    A full rebuild with build_culturemech_membership.py would also pull in every
    identifier MIM has minted since the artifact was last built (175 of them),
    which is a separate refresh; #344 moved its sulfate edges the same narrow way.
    """
    by_old = {spec.old_identifier: spec for spec in MINTS}
    moves: dict[tuple[str, str], str] = {}
    with occurrences.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            old = (row.get("resolved_identifier") or "").strip()
            if old not in by_old:
                continue
            new = SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(_source_label_key(row.get("preferred_term") or ""))
            if new and new != old:
                moves[(old, row["recipe_id"])] = new
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments, header, data, counts = [], None, [], defaultdict(int)
    for line in lines:
        if line.startswith("#"):
            comments.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if header is None:
            header = cells
            continue
        replacement = moves.get((cells[0], cells[1]))
        if replacement:
            cells[0] = replacement
            counts[replacement] += 1
        data.append(cells)
    data.sort(key=lambda cells: tuple(cells[:2]))
    keys = [(c[0], c[1]) for c in data]
    if len(keys) != len(set(keys)):
        raise SystemExit("membership moves would create duplicate edge keys")
    out = [*comments, "\t".join(header) + "\n", *("\t".join(c) + "\n" for c in data)]
    MEMBERSHIP.write_text("".join(out), encoding="utf-8")
    print(f"membership edges moved: {dict(sorted(counts.items()))}")
    return dict(counts)


def refresh_affected_occurrences(write: bool) -> int:
    """Refresh occurrence_statistics only for the records whose memberships this batch moved."""
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    lines = [line for line in MEMBERSHIP.read_text(encoding="utf-8").splitlines() if not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        if row["mim_identifier"] in AFFECTED_IDENTIFIERS:
            counts[row["mim_identifier"]][0] += 1
            counts[row["mim_identifier"]][1] += int(row["occurrences"])
    changed = 0
    for path in sorted(MAPPED.glob("*.yaml")):
        record = yaml.safe_load(path.read_text()) or {}
        identifier = str(record.get("identifier") or "")
        if identifier not in AFFECTED_IDENTIFIERS or record.get("mapping_status") == "REJECTED":
            continue
        stats = record.get("occurrence_statistics") or {}
        old = (stats.get("media_count") or 0, stats.get("total_occurrences") or 0)
        if identifier not in counts:
            # No edge names this identifier: leave the stored counts alone rather than
            # zeroing them (refresh_occurrence_statistics.py's contract, #449).
            continue
        new = tuple(counts[identifier])
        if old == new:
            continue
        record["occurrence_statistics"] = {**stats, "media_count": new[0], "total_occurrences": new[1]}
        record_curation_event(
            record, curator=CURATOR, action="REFRESHED_OCCURRENCE_STATISTICS",
            changes=(f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]} after the #312 registry mints moved "
                     "memberships off the shared identifier; counts follow the source label through "
                     "SOURCE_LABEL_IDENTIFIER_OVERRIDES."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"OCCURRENCES {path.stem}: {old[0]}/{old[1]} -> {new[0]}/{new[1]}")
        if write:
            write_validated_ingredient(record, path)
        changed += 1
    return changed


def rewrite_hydrate_review() -> int:
    rows = list(csv.DictReader(HYDRATE_REVIEW.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    by_label = {spec.slug: spec for spec in MINTS if spec.hydrate_review}
    labels = {load(slug)[1]["preferred_term"]: spec for slug, spec in by_label.items()}
    changed = 0
    for row in rows:
        spec = labels.get(row.get("preferred_term") or "")
        if spec is None or row.get("identifier") == spec.new_identifier:
            continue
        row["identifier"] = spec.new_identifier
        row["cas_rn_current"] = ""
        row["grounding_verdict"] = "CORRECT"
        row["recommended_target_curie"] = spec.new_identifier
        row["action"] = "LOCAL_IDENTITY_RETAINED"
        if "sssom_predicate_published" in row:
            row["sssom_predicate_published"] = "skos:closeMatch|skos:exactMatch"
        row["notes"] = (
            f"MIM keeps {row['preferred_term']} as a local unresolved source identity ({spec.mediadive_compound_id}). "
            f"{spec.ontology_id} ({spec.ontology_label}) is published only as a skos:closeMatch anhydrous parent; no "
            "exact formula, CAS, InChI, or SMILES is published until the malformed MediaDive hydration count is "
            f"corrected upstream ({ISSUE}, #344 shape)."
        )
        changed += 1
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    HYDRATE_REVIEW.write_text(out.getvalue(), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the records (default: dry-run)")
    parser.add_argument("--log", type=Path, help="apply-log JSON path (written with --apply)")
    parser.add_argument("--finish-sssom", action="store_true", help="after reconcile: registry rows, dropped food row, scrubs")
    parser.add_argument("--finish-artifacts", action="store_true",
                        help="rebuild recipe membership, refresh affected occurrence counts, update hydrate_review")
    parser.add_argument("--occurrences", type=Path, help="CultureMech output/ingredient_occurrences.tsv (for --finish-artifacts)")
    args = parser.parse_args()
    if args.finish_sssom:
        finish_sssom()
        return 0
    if args.finish_artifacts:
        if not args.occurrences:
            raise SystemExit("--finish-artifacts needs --occurrences")
        move_memberships(args.occurrences)
        log_entries: list = []
        changed = refresh_affected_occurrences(write=True)
        print(f"occurrence_statistics refreshed on {changed} record(s); hydrate_review rows updated: {rewrite_hydrate_review()}")
        if args.log:
            previous = json.loads(args.log.read_text())["records"] if args.log.is_file() else []
            merged = {entry["source_record"]: entry for entry in previous}
            for path in sorted(MAPPED.glob("*.yaml")):
                record = yaml.safe_load(path.read_text()) or {}
                if record.get("identifier") in AFFECTED_IDENTIFIERS:
                    rel = str(path.relative_to(ROOT))
                    entry = merged.get(rel)
                    current = sha(path)
                    if entry is None:
                        merged[rel] = {"source_record": rel, "shape": "occurrence_refresh",
                                       "before_yaml_sha256": _git_head_sha(rel), "after_yaml_sha256": current,
                                       "change": "occurrence_statistics refreshed from the rebuilt recipe membership",
                                       "verification": "Counts follow the source label through SOURCE_LABEL_IDENTIFIER_OVERRIDES."}
                    elif entry["after_yaml_sha256"] != current:
                        entry["after_yaml_sha256"] = current
                        entry["change"] += "; occurrence_statistics refreshed from the rebuilt recipe membership"
            args.log.write_text(json.dumps({"issue": ISSUE, "batch": "batch3", "records": list(merged.values())}, indent=2) + "\n")
            log_entries = list(merged.values())
        print(f"apply log now covers {len(log_entries)} record(s)")
        return 0
    verify()
    log: list = []
    for spec in MINTS:
        apply_mint(spec, log, args.apply)
    rescope_components(log, args.apply)
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    if args.apply and args.log:
        args.log.write_text(json.dumps({"issue": ISSUE, "batch": "batch3", "records": log}, indent=2) + "\n")
        print(f"apply log: {args.log}")
    return 0


def _git_head_sha(relative: str) -> str:
    blob = subprocess.run(["git", "show", f"HEAD:{relative}"], capture_output=True, cwd=ROOT, check=True).stdout
    return hashlib.sha256(blob).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
