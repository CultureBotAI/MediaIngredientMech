#!/usr/bin/env python3
"""Bounded #1004 source merge and native-candidate promotion; dry-run by default.

The immutable preimages are part of this one-time migration, not a permanent
constraint on live occurrence counts. Neither phase grants scientific approval.
The CLI holds the configured repository lock; callers of the Python apply API
must hold the same lock. Production generation is deliberately separate.
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime
import gzip
import io
import json
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

SURVIVOR = Path("data/ingredients/mapped/Carnitine_Hydrochloride.yaml")
TOMBSTONE = Path("data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml")
COMPONENT_OWNER = Path("data/ingredients/mapped/NLDM_metabolites.yaml")
OWNERS = (SURVIVOR, TOMBSTONE, COMPONENT_OWNER)
LEDGER = Path("mappings/unified_mapping_rejections.tsv")
MEMBERSHIP = Path("mappings/culturemech_recipe_membership.tsv")
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BASELINE = Path("mappings/other_cross_record_baseline.tsv")
SOURCE_PATHS = (*OWNERS, LEDGER, MEMBERSHIP)
FIXTURES = ROOT / "tests/fixtures/issue1004-before"
EVIDENCE = Path("reports/carnitine_hydrochloride_1004_20261101/sources")
MANIFEST_SHA = "d5bf100092c4a16d29552e79475b1a8a8891a797c046377365a46f0fb85ce911"
BEFORE = {
    SURVIVOR: "c03c1c66b9e70436da2e841d1edf2a700f05830674c715fc265ac7fde9705722",
    TOMBSTONE: "8a7e0ac23a72c403bf9cce38a20abe817ee83e0231b558f2ca07ed05d134d190",
    COMPONENT_OWNER: "7332021e0d760384bc0381f5e00e3a87bd4dfe4b7c5b2eb1140853f7c17d78a0",
    LEDGER: "717289ca0e45046dcb96f6839b843838a6636fd8e120cf4d9b9ac48de3d9016d",
    MEMBERSHIP: "55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897",
    SSSOM: "68552edd452d5dccf1262b5d03190a6b668341952a554f349149f269403cca67",
    BASELINE: "170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008",
}
OLD = "kgmicrobe.compound:carnitine_hydrochloride"
NEW = "NCIT:C216679"
NAME = "Carnitine Hydrochloride"
RAW_NAME = "Carnitine (Dl) Hydrochloride"
LABEL = "DL-Carnitine Hydrochloride"
FREE_NAME = "3-hydroxy-4-(trimethylammonio)butanoate"
AMIDE_NAME = "4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride"
SUBJECT = "MIM:Carnitine_Hydrochloride"
RETIRED_SUBJECT = "MIM:Carnitine_Dl_Hydrochloride"
COMPONENT_SUBJECT = "MIM:NLDM_metabolites"
SUBJECTS = {SUBJECT, RETIRED_SUBJECT, COMPONENT_SUBJECT}
RECIPES = frozenset("CultureMech:" + n for n in (
    "015654", "015655", "015656", "015665", "015666", "015667", "015668",
    "015669", "015670", "015671", "015740", "015741", "015742", "015749",
))
ACTION = "CORRECTED_AND_MERGED_CARNITINE_HYDROCHLORIDE"
APPROVAL = "NONE: source correction only; all changed owners require fresh mapping-specific review."
NCI_URL = "https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C216679?include=full"
PUBCHEM_URL = "https://pubchem.ncbi.nlm.nih.gov/compound/5970"
CHEBI_URL = "https://www.ebi.ac.uk/chebi/CHEBI:48601"
DECISION = "https://github.com/CultureBotAI/MediaIngredientMech/issues/1004#issuecomment-6555569867"
CHEMISTRY = {
    "cas_rn": "461-05-2", "molecular_formula": "C7H16ClNO3",
    "molecular_weight": 197.66,
    "smiles": "C[N+](C)(C)CC(CC(=O)O)O.[Cl-]",
    "inchi": "InChI=1S/C7H15NO3.ClH/c1-8(2,3)5-6(9)4-7(10)11;/h6,9H,4-5H2,1-3H3;1H",
    "pubchem_cid": 5970,
    "data_source": f"NCI EVS C216679 (CAS); PubChem CID 5970 (structure/properties); {NCI_URL}; {PUBCHEM_URL}",
    "retrieval_date": "2026-11-01T05:29:21.337754+00:00",
}
VERIFICATION = (
    f"NCI EVS NCIt 26.10d {NEW} '{LABEL}' is active, CAS 461-05-2, UNII F64264D63N: "
    f"{NCI_URL}. PubChem CID 5970 supplies chloride-bearing C7H16ClNO3 chemistry, "
    f"197.66 g/mol: {PUBCHEM_URL}. CHEBI:48601 is the distinct carnitinamide chloride "
    f"despite its conflicting CAS cross-reference: {CHEBI_URL}. Inspected 2026-11-01; "
    f"hash-bound captures and retrieval receipts: {EVIDENCE.as_posix()}/manifest.json "
    f"(sha256 {MANIFEST_SHA}). Sigma C9500 supplier evidence supports the original "
    "racemate. CultureBotHT raw CSV is a hash-bound local snapshot associated with "
    "checkout context, not a commit-attested blob. Direct CAS API returned 401; "
    "no CAS Registry verification is claimed. Historical CHEBI/KG source tokens "
    "are retained provenance, not independent support for the NCIT identity. "
    f"Approved decision: {DECISION}. No scientific/release approval is asserted."
)
MAPPING = {"ontology_id": NEW, "ontology_label": LABEL,
           "ontology_source": "NCIT", "mapping_quality": "EXACT_MATCH"}
MAPPING_EVIDENCE = {"evidence_type": "DATABASE_MATCH", "source": NCI_URL,
                    "notes": "Supersedes prior identity interpretation without erasing it. " + VERIFICATION}

digest = guarded.digest


def frozen_bytes(path: Path) -> bytes:
    """Load the immutable migration preimage, checking its hard-coded digest."""
    archived = FIXTURES / (path.name + (".gz" if path in (SSSOM, MEMBERSHIP) else ""))
    raw = archived.read_bytes()
    data = gzip.decompress(raw) if archived.suffix == ".gz" else raw
    if digest(data) != BEFORE[path]:
        raise ValueError(f"Immutable preimage changed: {path}")
    return data


def render(record: dict) -> bytes:
    with tempfile.TemporaryDirectory(prefix="mim-1004-validate-") as directory:
        output = Path(directory) / "record.yaml"
        write_validated_ingredient(record, output)
        return output.read_bytes()


def validate_timestamp(timestamp: str) -> None:
    try:
        parsed = datetime.datetime.fromisoformat(timestamp)
    except (TypeError, ValueError) as error:
        raise ValueError("Invalid correction timestamp") from error
    if parsed.utcoffset() != datetime.timedelta(0) or parsed.date() < datetime.date(2026, 11, 1):
        raise ValueError("Correction timestamp must be UTC and follow inspected evidence")


def corrected_ledger(before: bytes) -> bytes:
    if digest(before) != BEFORE[LEDGER]:
        raise ValueError("Rejection ledger differs from the frozen preimage")
    old_prefix = f"{NAME}\tCHEBI:91318\t{OLD}\t".encode()
    reason = (f"Exact {NEW} {LABEL}, CAS 461-05-2, is distinct from the acylcarnitine "
              f"CHEBI:91318. Reject that source identity in every unified identity column. "
              f"This supersedes the former local-identity/no-exact-term rationale (#1004). "
              f"{NCI_URL}; {SURVIVOR.as_posix()}. No release approval.")
    amide = (f"{NAME}\tCHEBI:48601\t{NEW}\tThe reviewed salt identity {NEW}, CAS 461-05-2, "
             f"is not carnitinamide chloride CHEBI:48601 despite its conflicting CAS xref. "
             f"Reject the amide in every unified identity column for this owner only (#1004). "
             f"{NCI_URL}; {CHEBI_URL}; {SURVIVOR.as_posix()}. No release approval.\n").encode()
    lines = before.splitlines(keepends=True)
    if sum(line.startswith(old_prefix) for line in lines) != 1:
        raise ValueError("Expected exactly one coupled old-owner rejection")
    return b"".join((f"{NAME}\tCHEBI:91318\t{NEW}\t{reason}\n".encode() + amide)
                    if line.startswith(old_prefix) else line for line in lines)


def corrected_membership(before: bytes) -> bytes:
    if digest(before) != BEFORE[MEMBERSHIP]:
        raise ValueError("Membership differs from the frozen preimage")
    lines = before.splitlines(keepends=True)
    header = []
    while lines and lines[0].startswith(b"#"):
        header.append(lines.pop(0))
    if not lines or lines[0] != b"mim_identifier\trecipe_id\toccurrences\n":
        raise ValueError("Unexpected membership columns")
    header.append(lines.pop(0))
    selected, output = set(), []
    for line in lines:
        fields = line.rstrip(b"\r\n").decode().split("\t")
        if len(fields) != 3 or not all(fields):
            raise ValueError("Malformed membership row")
        identifier, recipe, count = fields
        if identifier == NEW:
            raise ValueError("Destination membership exists or migration is partial")
        if identifier == OLD:
            if recipe in selected or recipe not in RECIPES or count != "1":
                raise ValueError("Historical membership recipe/count cohort changed")
            selected.add(recipe)
            identifier = NEW
            line = NEW.encode() + b"\t" + line.split(b"\t", 1)[1]
        output.append(((identifier, recipe), line))
    if selected != RECIPES or len({key for key, _ in output}) != len(output):
        raise ValueError("Incomplete historical cohort or duplicate membership key")
    return b"".join(header) + b"".join(line for _, line in sorted(output))


def propose_sources(owner_bytes: dict[Path, bytes], ledger: bytes, membership: bytes,
                    *, timestamp: str) -> dict[Path, bytes]:
    """Return only bounded outputs from exact immutable preimages, without writes."""
    validate_timestamp(timestamp)
    if set(owner_bytes) != set(OWNERS) or any(digest(owner_bytes[p]) != BEFORE[p] for p in OWNERS):
        raise ValueError("Owner inputs differ from the exact three reviewed preimages")
    records = {p: yaml.safe_load(owner_bytes[p]) for p in OWNERS}
    survivor, tombstone, component = (records[p] for p in OWNERS)
    old_chemistry = copy.deepcopy(tombstone["chemical_properties"])
    if (survivor["identifier"] != OLD or tombstone["identifier"] != "cas:461-06-3"
            or component["components"][58] != {
                "component_name": NAME, "component_id": OLD, "reference_scope": "MIM_CATALOG",
                "concentration_value": "17.5", "concentration_unit": "UM"}):
        raise ValueError("Unexpected reviewed identity or component scope")
    for record in (survivor, tombstone):
        record["identifier"] = NEW
        record["ontology_mapping"].update(MAPPING)
        record["ontology_mapping"].setdefault("evidence", []).append(copy.deepcopy(MAPPING_EVIDENCE))
    rejected = copy.deepcopy(tombstone["synonyms"][0])
    if rejected != {"synonym_text": FREE_NAME, "synonym_type": "EXACT_SYNONYM", "source": "chebi_synonym_review"}:
        raise ValueError("Unexpected free-substance synonym")
    rejected["synonym_type"] = "REJECTED_LABEL"
    tombstone["synonyms"][0] = rejected
    survivor["synonyms"].extend([copy.deepcopy(rejected), {
        "synonym_text": RAW_NAME, "synonym_type": "RAW_TEXT", "source": "CultureBotHT"}])
    survivor["chemical_properties"] = copy.deepcopy(CHEMISTRY)
    tombstone.pop("chemical_properties")
    tombstone["mapping_status"] = "REJECTED"
    tombstone["representative"] = NEW
    component["components"][58]["component_id"] = NEW
    changes = {
        SURVIVOR: (f"Corrected {OLD} to exact {NEW}; restored correct hydrochloride CAS/chemistry "
                   "from CID 5970. Merged the duplicate raw source name as RAW_TEXT; retained the "
                   "amide and free-substance names as attributed REJECTED_LABEL. Explicitly "
                   "supersedes the 2026-07-05 surface-form non-merge ruling and the old statement "
                   "that CAS 461-05-2 was erroneous. Preserved all previous history/evidence and "
                   "14/14 historical counts. " + VERIFICATION),
        TOMBSTONE: (f"Merged into {SURVIVOR.as_posix()} with corrected identity/representative {NEW}, "
                    "REJECTED status and zero counts. Rejected the free-substance systematic name; "
                    "removed active CID 288/free-parent chemistry. Exact prior chemical_properties "
                    "preserved here and in the immutable preimage: " + json.dumps(old_chemistry, sort_keys=True)
                    + ". Prior identifier cas:461-06-3 is historical, not current salt identity. "
                    "Supersedes the 2026-07-05 surface-form non-merge ruling; all prior history "
                    "and mapping evidence remain. " + VERIFICATION),
        COMPONENT_OWNER: (f"Retargeted component position 59 {NAME} from {OLD} to {NEW}; retained "
                          "MIM_CATALOG, 17.5 UM and every other component/evidence field. This "
                          "identity reference repair withdraws inherited mapping/component/role "
                          "approvals through the native receipt chain; no approval is carried. "
                          + VERIFICATION),
    }
    output = {}
    for path, record in records.items():
        record_curation_event(record, curator="Codex", action=ACTION, changes=changes[path],
                              previous_status="MAPPED", new_status=record["mapping_status"],
                              llm_assisted=True, llm_model="gpt-6", timestamp=timestamp)
        output[path] = render(record)
    output[LEDGER] = corrected_ledger(ledger)
    output[MEMBERSHIP] = corrected_membership(membership)
    return output


def complete_sources(current: dict[Path, bytes]) -> dict[Path, bytes]:
    """Recognize exact completion by replaying immutable beforeimages, not flags."""
    try:
        timestamps = {yaml.safe_load(current[p])["curation_history"][-1]["timestamp"] for p in OWNERS}
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete source correction") from error
    if len(timestamps) != 1:
        raise ValueError("Source events do not share the same correction timestamp")
    expected = propose_sources({p: frozen_bytes(p) for p in OWNERS}, frozen_bytes(LEDGER),
                               frozen_bytes(MEMBERSHIP), timestamp=timestamps.pop())
    if current != expected:
        raise ValueError("Partial source migration or changed completed correction")
    return expected


def validate_scope(root: Path) -> None:
    """Include ignored/nested files; only the two authored salt paths may share NCIT."""
    for path in (root / "data/ingredients").rglob("*.yaml"):
        if path.relative_to(root) in OWNERS:
            continue
        record = yaml.safe_load(path.read_text())
        if isinstance(record, dict) and (
            record.get("identifier") == NEW
            or (record.get("mapping_status") == "MAPPED"
                and (record.get("ontology_mapping") or {}).get("ontology_id") == NEW)
        ):
            raise ValueError(f"Destination identity already held by another owner: {path}")


def evidence_inputs(directory: Path) -> dict[Path, bytes]:
    manifest_path = directory / "manifest.json"
    raw = manifest_path.read_bytes()
    if digest(raw) != MANIFEST_SHA:
        raise ValueError("Reviewed source manifest changed")
    manifest = json.loads(raw)
    inputs = {manifest_path: raw}
    for name, item in manifest["files"].items():
        if Path(name).name != name:
            raise ValueError("Evidence path is not a direct source filename")
        path = directory / name
        data = path.read_bytes()
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError(f"Reviewed evidence bytes changed: {name}")
        inputs[path] = data
    term = json.loads(inputs[directory / "ncit-c216679.json"])
    props = {p["type"]: p["value"] for p in term["properties"]}
    compound = json.loads(inputs[directory / "pubchem-5970-properties.json"])["PropertyTable"]["Properties"]
    amide = json.loads(inputs[directory / "chebi-48601-primary.json"])
    if (term.get("code") != "C216679" or term.get("name") != LABEL or term.get("active") is not True
            or term.get("version") != "26.10d" or props.get("CAS_Registry") != "461-05-2"
            or props.get("FDA_UNII_Code") != "F64264D63N" or len(compound) != 1
            or any(compound[0].get(k) != v for k, v in {
                "CID": 5970, "MolecularFormula": CHEMISTRY["molecular_formula"],
                "MolecularWeight": "197.66", "SMILES": CHEMISTRY["smiles"], "InChI": CHEMISTRY["inchi"]}.items())
            or amide.get("chebi_accession") != "CHEBI:48601" or amide.get("name") != "carnitinamide chloride"):
        raise ValueError("Primary evidence does not verify the approved exact substance")
    return inputs


def backup_paths(log: Path, paths) -> dict[Path, Path]:
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in paths}


def apply_sources(root: Path, evidence: Path, log: Path, *, apply: bool = False) -> dict:
    root, evidence, log = root.resolve(), evidence.resolve(), log.absolute()
    inputs = {root / p: (root / p).read_bytes() for p in (*SOURCE_PATHS, SSSOM, BASELINE)}
    inputs.update(evidence_inputs(evidence))
    current = {p: inputs[root / p] for p in SOURCE_PATHS}
    validate_scope(root)
    if not all(digest(current[p]) == BEFORE[p] for p in SOURCE_PATHS):
        complete_sources(current)
        validate_completed_anchors(inputs[root / SSSOM], inputs[root / BASELINE], current)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if any(digest(inputs[root / p]) != BEFORE[p] for p in (SSSOM, BASELINE)):
        raise ValueError("Canonical/baseline anchor differs from the reviewed preimage")
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    output = propose_sources({p: current[p] for p in OWNERS}, current[LEDGER], current[MEMBERSHIP], timestamp=timestamp)
    result = {"phase": "sources", "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1004",
              "approval": APPROVAL, "timestamp": timestamp, "evidence_manifest_sha256": MANIFEST_SHA,
              "evidence_directory": str(evidence),
              "input_sha256": {str(p): digest(b) for p, b in inputs.items()},
              "output_sha256": {str(p): digest(b) for p, b in output.items()},
              "sssom_before_sha256": BEFORE[SSSOM], "baseline_before_sha256": BEFORE[BASELINE],
              "records": [{"source_record": str(p), "shape": "exact_hydrochloride_merge" if p != COMPONENT_OWNER else "component_reference",
                           "before_yaml_sha256": BEFORE[p], "after_yaml_sha256": digest(output[p]),
                           "change": yaml.safe_load(output[p])["curation_history"][-1]["changes"],
                           "verification": VERIFICATION} for p in OWNERS]}
    backups = {q: inputs[root / p] for p, q in backup_paths(log, (*SOURCE_PATHS, SSSOM, BASELINE)).items()}
    return guarded.publish(root, output, inputs, log, backups, result, apply=apply,
                           validate_scope=lambda: validate_scope(root))


def table(data: bytes) -> tuple[list[str], list[dict]]:
    return guarded.table(data)


def retired_baseline(before: bytes) -> bytes:
    if digest(before) != BEFORE[BASELINE]:
        raise ValueError("Rule K baseline preimage changed")
    removed = {f"{s}\tDL-carnitine\tMIM:Dl-carnitine\tUNREVIEWED\n".encode()
               for s in (SUBJECT, RETIRED_SUBJECT)}
    lines = before.splitlines(keepends=True)
    if any(lines.count(line) != 1 for line in removed):
        raise ValueError("Expected both reviewed free-substance alias obligations")
    return b"".join(line for line in lines if line not in removed)


def promoted_sssom(before: bytes, candidate: bytes, owners: dict[Path, bytes]) -> bytes:
    if digest(before) != BEFORE[SSSOM]:
        raise ValueError("Canonical SSSOM preimage changed")
    fields, rows = table(before)
    candidate_fields, candidates = table(candidate)
    selected = [r for r in candidates if r["subject_id"] in SUBJECTS]
    if candidate_fields != fields or len(selected) != 2 or {r["subject_id"] for r in selected} != {SUBJECT, COMPONENT_SUBJECT}:
        raise ValueError("Native candidate must have one survivor, one NLDM and no tombstone row")
    corrected = {}
    for path, subject in ((SURVIVOR, SUBJECT), (COMPONENT_OWNER, COMPONENT_SUBJECT)):
        record = yaml.safe_load(owners[path])
        row = dict(next(r for r in selected if r["subject_id"] == subject))
        old = [r for r in rows if r["subject_id"] == subject]
        evidence = {"MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]}
        if set(row["source"].split("|")) != evidence | {"MIM:curator=Codex"}:
            raise ValueError("Candidate lacks exact source/curator provenance")
        date = max(e["timestamp"][:10] for e in record["curation_history"])
        expected = ({"subject_label": NAME, "predicate_id": "skos:exactMatch", "object_id": NEW,
                     "object_label": LABEL, "object_source": "obo:ncit.owl", "mapping_justification": "semapv:LexicalMatching",
                     "confidence": "0.99", "comment": "", "other": RAW_NAME + "|CAS:461-05-2"}
                    if path == SURVIVOR else {k: v for k, v in old[0].items()
                                             if k not in {"source", "mapping_date", "validation_method"}})
        expected.update(mapping_date=date, validation_method="")
        if any(row.get(k) != v for k, v in expected.items()):
            raise ValueError(f"Candidate differs from the bounded native claim: {subject}")
        prior_sources = [s for r in old for s in r["source"].split("|")]
        row["source"] = "|".join(dict.fromkeys(prior_sources + row["source"].split("|")))
        corrected[subject] = row
    output, seen = [], set()
    for line in before.decode().splitlines(keepends=True):
        subject = line.split("\t", 1)[0]
        if subject in SUBJECTS:
            if subject in corrected and subject not in seen:
                buffer = io.StringIO(newline="")
                csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n").writerow(corrected[subject])
                output.append(buffer.getvalue())
            seen.add(subject)
        else:
            output.append(line)
    if seen != SUBJECTS:
        raise ValueError("Expected both salt subjects and NLDM in canonical preimage")
    newest = newest_row_date(output)
    if not newest:
        raise ValueError("Cannot derive native mapping header date")
    return "".join(rewrite(output, newest)[0]).encode()


def validate_completed_anchors(canonical: bytes, baseline: bytes, current: dict[Path, bytes]) -> None:
    """A repeated source command accepts only the before or complete promotion."""
    if digest(canonical) == BEFORE[SSSOM] and digest(baseline) == BEFORE[BASELINE]:
        return
    if baseline != retired_baseline(frozen_bytes(BASELINE)):
        raise ValueError("Completed correction has a changed/partial baseline anchor")
    fields, rows = table(canonical)
    for row in rows:
        path = {SUBJECT: SURVIVOR, COMPONENT_SUBJECT: COMPONENT_OWNER}.get(row["subject_id"])
        if path is not None:
            record = yaml.safe_load(current[path])
            row["source"] = "|".join(["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]]
                                      + ["MIM:curator=Codex"])
    buffer = io.StringIO(newline="")
    stream = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    stream.writeheader()
    stream.writerows(rows)
    expected = promoted_sssom(frozen_bytes(SSSOM), buffer.getvalue().encode(), current)
    if canonical != expected:
        raise ValueError("Completed correction has a changed canonical anchor")


def promote(root: Path, candidate: Path, source_log: Path, log: Path, *, apply: bool = False,
            candidate_sha256: str | None = None) -> dict:
    root, candidate, source_log, log = root.resolve(), candidate.resolve(), source_log.resolve(), log.absolute()
    source_bytes = source_log.read_bytes()
    source = json.loads(source_bytes)
    current = {p: (root / p).read_bytes() for p in SOURCE_PATHS}
    complete_sources(current)
    if (source.get("phase") != "sources" or source.get("state") != "complete" or source.get("applied") is not True
            or source.get("approval") != APPROVAL or source.get("evidence_manifest_sha256") != MANIFEST_SHA
            or source.get("output_sha256") != {str(p): digest(b) for p, b in current.items()}
            or len(source.get("records", [])) != 3
            or {r["source_record"]: (r["before_yaml_sha256"], r["after_yaml_sha256"]) for r in source["records"]}
            != {str(p): (BEFORE[p], digest(current[p])) for p in OWNERS}):
        raise ValueError("Completed source receipt does not bind all current owners/ledger/membership")
    inputs = {root / p: b for p, b in current.items()}
    inputs[source_log] = source_bytes
    inputs.update(evidence_inputs(Path(source["evidence_directory"])))
    for path, backup in backup_paths(source_log, (*SOURCE_PATHS, SSSOM, BASELINE)).items():
        data = backup.read_bytes()
        if digest(data) != BEFORE[path]:
            raise ValueError(f"Source receipt beforeimage changed: {path}")
        inputs[backup] = data
    proposed = candidate.read_bytes()
    if candidate_sha256 is not None and digest(proposed) != candidate_sha256:
        raise ValueError("Supplied candidate hash changed")
    inputs[candidate] = proposed
    before = inputs[backup_paths(source_log, (SSSOM,))[SSSOM]]
    baseline_before = inputs[backup_paths(source_log, (BASELINE,))[BASELINE]]
    after = promoted_sssom(before, proposed, {p: current[p] for p in OWNERS})
    baseline_after = retired_baseline(baseline_before)
    output = {SSSOM: after, BASELINE: baseline_after}
    actual = {p: (root / p).read_bytes() for p in output}
    validate_scope(root)
    if actual == output:
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if actual != {SSSOM: before, BASELINE: baseline_before}:
        raise ValueError("Canonical/baseline changed or promotion is partial")
    inputs.update({root / p: b for p, b in actual.items()})
    result = {"phase": "promote", "approval": APPROVAL, "records": source["records"],
              "source_receipt_sha256": digest(source_bytes), "candidate_sha256": digest(proposed),
              "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(after),
              "baseline_before_sha256": digest(baseline_before), "baseline_after_sha256": digest(baseline_after),
              "changed_rows": 2, "removed_rows": 4, "removed_baseline_rows": 2,
              "preserved_historical_source_tokens": True}
    return guarded.publish(root, output, inputs, log,
                           {q: actual[p] for p, q in backup_paths(log, output).items()}, result, apply=apply,
                           validate_scope=lambda: validate_scope(root))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("sources", "promote"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--source-log", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-sha256")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.phase == "promote" and not all((args.source_log, args.candidate, args.candidate_sha256)):
        parser.error("promote requires --source-log, --candidate and --candidate-sha256")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    if target.path.resolve() != args.root.resolve():
        raise ValueError("Configured MIM root differs from the requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", f"#1004 {args.phase}"):
        if args.phase == "sources":
            result = apply_sources(target.path, args.evidence or target.path / EVIDENCE, args.log, apply=args.apply)
        else:
            result = promote(target.path, args.candidate, args.source_log, args.log, apply=args.apply,
                             candidate_sha256=args.candidate_sha256)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
