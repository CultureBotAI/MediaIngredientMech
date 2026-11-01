"""Bounded #669/#1019/#1020 source correction and canonical projection.

Dry-run unless --apply. The CLI holds the native MIM repository lock; direct
Python application requires that same caller-held lock. No scientific approval.
"""
from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
from pathlib import Path
import stat
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
NATIVE = ROOT
FIXTURES = ROOT / "tests/fixtures/issue669-owned-name-before"
EVIDENCE = Path("reports/owned_name_policy_669_20261101/sources")
REPORT = ROOT / EVIDENCE.parent
sys.path.insert(0, str(NATIVE / "src"))
sys.path.insert(0, str(NATIVE))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from scripts import promote_heptahydrate_ncit as guarded
from scripts.bump_sssom_header import newest_row_date, rewrite

SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BASELINE = Path("mappings/other_cross_record_baseline.tsv")
SIDECAR = Path("mappings/suppressed_aliases.tsv")
_OWNER_META_BYTES = (FIXTURES / "owner-manifest.json").read_bytes()
OWNER_META_SHA = "a29eb0316ec9ae0525eecd3a3b1c067bc580053c94bb8268e314c8ceb43d84e4"
if hashlib.sha256(_OWNER_META_BYTES).hexdigest() != OWNER_META_SHA:
    raise ValueError("Reviewed owner manifest changed before import")
OWNER_META = json.loads(_OWNER_META_BYTES)
OWNERS = tuple(Path(p) for p, x in OWNER_META.items() if x["source_yaml_changes_authorized"])
AFFECTED = tuple(Path(p) for p, x in OWNER_META.items() if x["affected_receipt_owner"])
_SOURCE_NAMES = {"Beta-lactose", "Glycerol_3-phosphate", "Na2glycerophosphate5h2o"}
_AFFECTED_NAMES = _SOURCE_NAMES | {
    "24-diamino-67-di-iso-propylpteridine_phosphate", "D-mannitol", "L-asparagine",
    "L-cysteine", "L-glutamic_Acid", "L-proline", "L-tryptophan", "Magnesium_Chloride",
    "Nh42ni_So42", "Sodium_Succinate_Dibasic",
}
if (set(OWNERS) != {Path("data/ingredients/mapped") / (n + ".yaml") for n in _SOURCE_NAMES}
        or set(AFFECTED) != {Path("data/ingredients/mapped") / (n + ".yaml") for n in _AFFECTED_NAMES}):
    raise ValueError("Exactly the reviewed three source and thirteen receipt owners are required")
PLAN = json.loads((REPORT / "decisions/pair-plan.json").read_bytes())
G, BETA, NA = (Path("data/ingredients/mapped/" + x + ".yaml") for x in
               ("Glycerol_3-phosphate", "Beta-lactose", "Na2glycerophosphate5h2o"))
SOURCE_SHA = "bf267a1ea9f459a56552d57c4aff5defb14d92f14516ed28d71475f558948191"
CANON_SHA = "beef5e184ea0895d41d80f1b1b813f6983c5534ea59f9b4585feb71940e7c6f9"
BASELINE_SHA = "8305c7f06d05466de1c49bd76c9ddaba17e53ecbd28a5d9dde1d36e59db0e707"
POLICY = "https://github.com/CultureBotAI/MediaIngredientMech/issues/669#issuecomment-6559004728"
GLY_URL = "https://www.ebi.ac.uk/chebi/backend/api/public/compound/17754/"
BETA_URL = "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36218"
PARENT_URLS = ('https://www.ebi.ac.uk/chebi/backend/api/public/compound/17270/', 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/13408-09-8/property/Title,MolecularFormula,IUPACName,InChI,InChIKey/JSON', 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2735049/property/Title,MolecularFormula,IUPACName,InChI,InChIKey/JSON')
APPROVAL = "NONE: bounded source/export correction; native reviews remain authoritative."
COLS = ("subject_id", "token_key", "token", "owner_subject_ids", "disposition", "input_surfaces", "source_refs", "evidence_refs")
FIXTURE_SHA = "709ab7d344df1cced5c96c0d27859a3c85ff012debc6431a82a8c954587ab384"
PLAN_SHA = "8be9057cd06ff995cf00818bda8d660925228fac6d9ea54abe5489668e6b0893"
PROMOTION_MANIFEST = Path("mappings/ingredient_mappings.sssom.tsv.manifest.json")
CODE_PATHS = (Path(__file__), Path(guarded.__file__), ROOT / "scripts/bump_sssom_header.py",
              ROOT / "src/mediaingredientmech/curate/apply_receipt.py",
              ROOT / "src/mediaingredientmech/curate/curation_event.py",
              ROOT / "src/mediaingredientmech/validation/write_validated.py",
              ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml")
_LOADED_CODE = {p: p.read_bytes() for p in CODE_PATHS}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def regular(path):
    path = Path(path).absolute()
    if path.resolve() != path or not stat.S_ISREG(path.lstat().st_mode) or path.stat().st_nlink != 1:
        raise ValueError(f"Input is aliased or nonregular: {path}")
    return path.read_bytes()


def frozen(path):
    path = Path(path)
    if path == SSSOM:
        data = gzip.decompress(regular(FIXTURES / "ingredient_mappings.sssom.tsv.gz"))
        expected = CANON_SHA
    elif path == BASELINE:
        data, expected = regular(FIXTURES / "other_cross_record_baseline.tsv"), BASELINE_SHA
    else:
        item = OWNER_META[str(path)]
        data, expected = regular(FIXTURES / "owners" / path.name), item["sha256"]
    if digest(data) != expected:
        raise ValueError(f"Reviewed preimage changed: {path}")
    return data


def evidence_inputs(directory):
    raw = regular(directory / "manifest.json")
    if digest(raw) != SOURCE_SHA:
        raise ValueError("Reviewed primary manifest changed")
    result = {directory / "manifest.json": raw}
    for name, item in json.loads(raw)["files"].items():
        if Path(name).name != name:
            raise ValueError("Primary evidence requires direct filenames")
        data = regular(directory / name)
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError(f"Primary evidence changed: {name}")
        result[directory / name] = data
    return result


def render(record):
    with tempfile.TemporaryDirectory(prefix="mim-step5-draft-") as directory:
        path = Path(directory) / "record.yaml"
        write_validated_ingredient(record, path)
        return path.read_bytes()


def propose_sources(owner_bytes, *, timestamp):
    if set(owner_bytes) != set(OWNERS):
        raise ValueError("Exactly three reviewed source owners required")
    parsed = dt.datetime.fromisoformat(timestamp)
    if parsed.utcoffset() != dt.timedelta(0) or parsed.date() < dt.date(2026, 11, 1):
        raise ValueError("Timestamp must be UTC after the source capture")
    evidence = evidence_inputs(ROOT / EVIDENCE)
    result = {}
    for path in OWNERS:
        if owner_bytes[path] != frozen(path):
            raise ValueError(f"Owner differs from reviewed preimage: {path}")
        record = copy.deepcopy(yaml.safe_load(owner_bytes[path]))
        if path == G:
            for entry in record["synonyms"]:
                if entry["synonym_text"] in {"Gro", "glycerolum", "glycyl alcohol"}:
                    if entry["synonym_type"] != "RAW_TEXT" or entry["source"] != "sssom_other_backfill":
                        raise ValueError("Unexpected attributed glycerol alias")
                    entry["synonym_type"] = "REJECTED_LABEL"
            reason = ("#1019: Gro, glycerolum and glycyl alcohol name glycerol, not this phosphate. "
                      "Retyped those existing aliases RAW_TEXT to REJECTED_LABEL; retained original "
                      "source=sssom_other_backfill and prior history. Negative alias evidence (not "
                      "support for the phosphate mapping): " + GLY_URL + " sha256=" +
                      digest(evidence[ROOT / EVIDENCE / "chebi-17754-primary.json"]) + ".")
        elif path == BETA:
            entry = record["synonyms"][0]
            if entry != {"synonym_text": "lactose", "synonym_type": "EXACT_SYNONYM", "source": "merged_from_duplicate_mim_record"}:
                raise ValueError("Unexpected lactose alias")
            entry["synonym_type"] = "RELATED_SYNONYM"
            reason = ("#669: retyped lactose EXACT_SYNONYM to RELATED_SYNONYM, preserving original "
                      "source. Captured OLS LACTOSE hasRelatedSynonym, pdb-ccd: " + BETA_URL +
                      " sha256=" + digest(evidence[ROOT / EVIDENCE / "chebi-36218-ols.json"]) +
                      ". This source correction is separate from export SUPPRESS.")
        else:
            mapping = record["ontology_mapping"]
            if record["identifier"] != "cas:13408-09-8" or mapping["mapping_quality"] != "NARROW_MATCH":
                raise ValueError("Unexpected salt identity or parent quality")
            mapping["ontology_id"], mapping["ontology_label"] = "CHEBI:17270", "glycerol 2-phosphate"
            mapping["evidence"][0]["notes"] = ("Historical evidence superseded by #1020 parent correction; "
                                                  "the original text is preserved verbatim below. " + mapping["evidence"][0]["notes"])
            reason = ("#1020: corrected parent CHEBI:15978 to CHEBI:17270 / glycerol 2-phosphate; "
                      "retained cas:13408-09-8, NARROW_MATCH (published broadMatch), raw labels, counts "
                      "and chemistry. PubChem CID2735049 describes disodium 2-glycerophosphate "
                      "pentahydrate; the CAS-routed and CID-routed responses are byte-identical, one "
                      "evidence payload rather than independent confirmations. The old contradictory "
                      "mapping evidence is explicitly superseded and preserved. DROP the generated-only "
                      "Glycerol 3-phosphate token without inventing a YAML synonym. ")
            for url in PARENT_URLS:
                receipt = next(json.loads(data) for p, data in evidence.items()
                               if p.name.endswith(".receipt.json") and json.loads(data).get("url") == url)
                mapping["evidence"].append({"evidence_type": "MANUAL_CURATION", "source": url,
                    "notes": reason + "Captured response sha256=" + receipt["sha256"] + "."})
            reason += "Correction sources: " + "; ".join(PARENT_URLS) + "."
        reason += " " + APPROVAL + " Policy: " + POLICY
        record_curation_event(record, curator="Codex", action="CORRECTED_OWNED_NAME_SOURCE", changes=reason,
            timestamp=timestamp, previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model="gpt-6")
        result[path] = render(record)
    return result


def verify_complete_sources(current):
    try:
        stamps = {yaml.safe_load(b)["curation_history"][-1]["timestamp"] for b in current.values()}
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete source correction") from error
    if len(stamps) != 1 or current != propose_sources({p: frozen(p) for p in OWNERS}, timestamp=stamps.pop()):
        raise ValueError("Partial or changed source correction")


def table(raw):
    lines = raw.decode().splitlines(keepends=True)
    while lines and lines[0].startswith("#"):
        lines.pop(0)
    reader = csv.DictReader(io.StringIO("".join(lines)), delimiter="\t")
    rows = list(reader)
    if not reader.fieldnames or any(None in row or None in row.values() for row in rows):
        raise ValueError("Malformed table")
    return reader.fieldnames, rows


def tsv(fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def remove_tokens(text, forbidden):
    return "|".join(x for x in text.split("|") if x.strip().casefold() not in forbidden)


def promoted_sssom(before, candidate, current, *, kg_sources_by_target):
    """Pure bounded projection. Runtime must separately bind/replay native generation.

    kg_sources_by_target is an exact-source-index result, not a scientific claim.
    It must be bound to the fresh generation input by the future runtime gate.
    """
    if digest(before) != CANON_SHA:
        raise ValueError("Canonical preimage changed")
    verify_complete_sources(current)
    fields, prior = table(before)
    candidate_fields, rows = table(candidate)
    if fields != candidate_fields:
        raise ValueError("Candidate column contract changed")
    old_index = {(r["subject_id"], r["object_id"]): r for r in prior}
    selected = {("MIM:" + p.stem): yaml.safe_load(data) for p, data in current.items()}
    crows = [r for r in rows if r["subject_id"] in selected]
    expected_keys = {k for k in old_index if k[0] in selected}
    expected_keys.remove(("MIM:" + NA.stem, "CHEBI:15978"))
    expected_keys.add(("MIM:" + NA.stem, "CHEBI:17270"))
    if len(crows) != len(expected_keys) or {(r["subject_id"], r["object_id"]) for r in crows} != expected_keys:
        raise ValueError("Expected exactly the five corrected-source candidate rows")
    candidate_index = {(r["subject_id"], r["object_id"]): r for r in crows}
    removals = {x["subject_id"]: {x["token_key"]} for x in PLAN}
    removals["MIM:" + G.stem] = {"gro", "glycerolum", "glycyl alcohol"}
    replacements = {}
    for key, old in old_index.items():
        subject, obj = key
        if subject not in removals:
            continue
        projected = dict(old, other=remove_tokens(old["other"], removals[subject]))
        if subject in selected:
            record = selected[subject]
            new_parent = subject == "MIM:" + NA.stem and obj == "CHEBI:15978"
            target = "CHEBI:17270" if new_parent else obj
            native = candidate_index[(subject, target)]
            expected = dict(projected, mapping_date=record["curation_history"][-1]["timestamp"][:10])
            if new_parent:
                expected.update(object_id=target, object_label="glycerol 2-phosphate", validation_method="")
            expected["comment"] = old["comment"].replace("CHEBI:15978", "CHEBI:17270") if subject == "MIM:" + NA.stem and not new_parent else ""
            kg = list(kg_sources_by_target.get(record["ontology_mapping"]["ontology_id"], ()))
            if not all(x.startswith("kgm:") and "|" not in x for x in kg):
                raise ValueError("Invalid target-specific KG source token")
            expected["source"] = "|".join(["MIM:" + e["source"] for e in record["ontology_mapping"].get("evidence", [])]
                                            + ["MIM:curator=Codex"] + kg)
            if native != expected:
                raise ValueError(f"Candidate differs from bounded native row: {key}")
            projected["mapping_date"] = expected["mapping_date"]
            additions = ["MIM:curator=Codex"]
            if subject == "MIM:" + NA.stem:
                additions = ["MIM:" + u for u in PARENT_URLS] + additions
                projected["comment"] = expected["comment"]
            if new_parent:
                projected.update(object_id=target, object_label="glycerol 2-phosphate", validation_method="",
                    source="|".join(additions + kg),
                    comment=old["comment"] + " [Historical predicate-direction correction on prior CHEBI:15978; #1020 now corrects the parent to CHEBI:17270.]")
            else:
                projected["source"] = "|".join(dict.fromkeys(old["source"].split("|") + additions))
        replacements[key] = projected
    output = []
    for line in before.decode().splitlines(keepends=True):
        if line.startswith("# mapping_set_description: "):
            description = json.loads(line.split(": ", 1)[1])
            marker = "owned-name-policy-v1; suppression-sidecar-required"
            if marker not in description:
                line = "# mapping_set_description: " + json.dumps(description + " " + marker, ensure_ascii=False) + "\n"
        if line.startswith("MIM:"):
            row = next(csv.DictReader(io.StringIO("\t".join(fields) + "\n" + line), delimiter="\t"))
            key = (row["subject_id"], row["object_id"])
            if key in replacements and replacements[key] != row:
                line = tsv(fields, [replacements[key]]).decode().split("\n", 1)[1]
        output.append(line)
    newest = newest_row_date(output)
    if not newest:
        raise ValueError("No canonical row date")
    return "".join(rewrite(output, newest)[0]).encode()


def retired_baseline(before):
    if digest(before) != BASELINE_SHA:
        raise ValueError("Baseline preimage changed")
    selected = {(x["subject_id"], x["token_key"]) for x in PLAN}
    fields, rows = table(before)
    retired = [r for r in rows if (r["subject_id"], r["token"].strip().casefold()) in selected]
    if len(retired) != len(selected):
        raise ValueError("Selected baseline membership changed")
    raw = before.splitlines(keepends=True)
    keep = [raw[0]]
    for line in raw[1:]:
        row = next(csv.DictReader(io.StringIO("\t".join(fields) + "\n" + line.decode()), delimiter="\t"))
        if (row["subject_id"], row["token"].strip().casefold()) not in selected:
            keep.append(line)
    return b"".join(keep)


def canonical_sidecar(promoted, *, candidate_sidecar):
    """Adopt only reviewed SUPPRESS pairs; retain all fresh candidate origins."""
    _, rows = table(promoted)
    fields, diagnostic = table(candidate_sidecar)
    if fields != list(COLS):
        raise ValueError("Diagnostic sidecar contract changed")
    index = {(r["subject_id"], r["token_key"]): r for r in diagnostic}
    if len(index) != len(diagnostic):
        raise ValueError("Duplicate diagnostic pair")
    result = []
    for item in PLAN:
        if item["disposition"] != "SUPPRESS":
            continue
        subject, token = item["subject_id"], item["token_key"]
        if any(r["subject_id"] == subject and token in {s.strip().casefold() for s in r["other"].split("|")} for r in rows):
            raise ValueError("Cannot claim a still-published suppression")
        owners = sorted(x["subject_id"] for x in item["credited_owners"])
        if item["yaml_alias_basis"]:
            row = copy.deepcopy(index[(subject, token)])
            if json.loads(row["owner_subject_ids"]) != owners or row["disposition"] != "SUPPRESS":
                raise ValueError("Diagnostic credited ownership changed")
        else:
            row = {"subject_id": subject, "token_key": token, "token": item["token"], "disposition": "SUPPRESS",
                   "owner_subject_ids": json.dumps(owners), "input_surfaces": json.dumps(["prior_sssom"]),
                   "source_refs": json.dumps(sorted(x["selector"] + "@sha256=" + CANON_SHA for x in item["prior_canonical"]["rows"])),
                   "evidence_refs": json.dumps([POLICY])}
            observed = index.get((subject, token))
            if observed is not None:
                if json.loads(observed["owner_subject_ids"]) != owners or observed["disposition"] != "SUPPRESS":
                    raise ValueError("Diagnostic credited ownership changed")
                for field in ("input_surfaces", "source_refs", "evidence_refs"):
                    row[field] = json.dumps(sorted(set(json.loads(row[field])) | set(json.loads(observed[field]))))
                row["token"] = min(row["token"], observed["token"])
        result.append(row)
    return tsv(COLS, sorted(result, key=lambda x: (x["subject_id"], x["token_key"])))


def source_records(current):
    return [{"source_record": str(p), "shape": "owned_name_source_correction" if p in OWNERS else "export_only_owned_name_suppression",
             "before_yaml_sha256": digest(frozen(p)), "after_yaml_sha256": digest(current.get(p, frozen(p))),
             "change": yaml.safe_load(current[p])["curation_history"][-1]["changes"] if p in OWNERS else "Export-only suppression; source YAML byte-identical, no history event fabricated.",
             "verification": APPROVAL + " " + POLICY} for p in AFFECTED]


def fixed_inputs():
    """Bind the complete small reviewed fixture/decision selection, not mutable globals."""
    path = FIXTURES / "manifest.json"
    raw = regular(path)
    if digest(raw) != FIXTURE_SHA:
        raise ValueError("Immutable fixture manifest changed")
    result = {path: raw}
    declared = json.loads(raw)["files"]
    actual = {str(p.relative_to(FIXTURES)) for p in FIXTURES.rglob("*") if p.is_file()}
    if actual != set(declared) | {"manifest.json"}:
        raise ValueError("Immutable fixture path set changed")
    for name, item in declared.items():
        path = FIXTURES / name
        data = regular(path)
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError(f"Immutable fixture changed: {name}")
        result[path] = data
    if (result[FIXTURES / "owner-manifest.json"] != _OWNER_META_BYTES
            or json.loads(_OWNER_META_BYTES) != OWNER_META
            or set(OWNERS) != {Path("data/ingredients/mapped") / (n + ".yaml") for n in _SOURCE_NAMES}
            or set(AFFECTED) != {Path("data/ingredients/mapped") / (n + ".yaml") for n in _AFFECTED_NAMES}):
        raise ValueError("Loaded owner manifest or reviewed owner membership changed")
    decision = REPORT / "decisions/pair-plan.json"
    result[decision] = regular(decision)
    if digest(result[decision]) != PLAN_SHA or json.loads(result[decision]) != PLAN:
        raise ValueError("Reviewed pair plan changed")
    for path in (REPORT / "decisions").glob("*.md"):
        result[path] = regular(path)
    posted = REPORT / "decisions/posted.json"
    result[posted] = regular(posted)
    if digest(result[posted]) != "b1a4631c72fcb50fce91cc1d65d606885819e7a0a9c5b441872b3e6cbcb26019":
        raise ValueError("Posted decision receipt changed")
    for item in json.loads(result[posted]):
        path = REPORT / "decisions" / Path(item["body"]).name
        if digest(result[path]) != item["body_sha256"]:
            raise ValueError("Posted decision body changed")
    return result


def code_inputs():
    result = {p: regular(p) for p in CODE_PATHS}
    if result != _LOADED_CODE:
        raise ValueError("Loaded source-writer code changed")
    return result


def checked_root(root):
    root = Path(root).absolute()
    if root.resolve() != root or not root.is_dir():
        raise ValueError("Repository root must be its original directory")
    return root


def snapshot_sources(root):
    paths = ingredient_paths(root)
    return {p: regular(p) for p in paths}


def ingredient_paths(root):
    """Include ignored/nested owners and reject directory aliases (#1051)."""
    directory = root / "data/ingredients"
    if directory.resolve() != directory:
        raise ValueError("Ingredient directory is aliased")
    result = set()
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Ingredient path is aliased: {path}")
        if path.suffix == ".yaml":
            result.add(path)
    return result


def validate_scope(root, inputs, source_paths):
    if ingredient_paths(root) != source_paths:
        raise ValueError("Ingredient owner path set changed")
    for path, expected in inputs.items():
        if regular(path) != expected:
            raise ValueError(f"Bound input changed: {path}")


def before_promotion(root):
    """The first source phase cannot coexist with partial promotion artifacts."""
    if any((root / p).exists() or (root / p).is_symlink() for p in (SIDECAR, PROMOTION_MANIFEST)):
        raise ValueError("Unexpected partial promotion artifacts")


def backups(log):
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in (*OWNERS, SSSOM, BASELINE)}


def completed_receipt(log, expected, root, *, changed, created=()):
    raw = regular(log)
    value = json.loads(raw)
    tx = value.get("transaction") or {}
    if (any(value.get(k) != v for k, v in expected.items()) or value.get("state") != "complete"
            or value.get("applied") is not True or tx.get("applied") is not True
            or set(tx.get("changed", [])) != {str(root / p) for p in changed}
            or len(tx.get("changed", [])) != len(changed)
            or set(tx.get("created", [])) != {str(root / p) for p in created}
            or len(tx.get("created", [])) != len(created) or tx.get("unchanged") != []):
        raise ValueError("Completed receipt does not bind this exact execution")
    return raw


def source_context(root, evidence, current):
    verify_complete_sources(current)
    sources = snapshot_sources(root)
    for p in set(map(Path, OWNER_META)) - set(OWNERS):
        if sources.get(root / p) != frozen(p):
            raise ValueError(f"Unchanged source/name owner changed: {p}")
    inputs = sources | evidence_inputs(evidence) | fixed_inputs() | code_inputs()
    inputs.update({root / p: regular(root / p) for p in (SSSOM, BASELINE)})
    original = dict(inputs)
    original.update({root / p: frozen(p) for p in (*OWNERS, SSSOM, BASELINE)})
    expected = {"phase": "sources", "approval": APPROVAL,
                "timestamp": yaml.safe_load(current[OWNERS[0]])["curation_history"][-1]["timestamp"],
                "evidence_directory": str(evidence), "evidence_manifest_sha256": SOURCE_SHA,
                "input_sha256": {str(p): digest(data) for p, data in original.items()},
                "output_sha256": {str(p): digest(data) for p, data in current.items()},
                "sssom_before_sha256": CANON_SHA, "baseline_before_sha256": BASELINE_SHA,
                "records": source_records(current)}
    return inputs, expected, set(sources)


def source_receipt(root, log):
    root, log = checked_root(root), Path(log).absolute()
    current = {p: regular(root / p) for p in OWNERS}
    value = json.loads(regular(log))
    evidence = Path(value["evidence_directory"])
    inputs, expected, paths = source_context(root, evidence, current)
    inputs[log] = completed_receipt(log, expected, root, changed=set(OWNERS))
    for p, path in backups(log).items():
        data = regular(path)
        if data != frozen(p):
            raise ValueError(f"Source beforeimage changed: {p}")
        inputs[path] = data
    validate_scope(root, inputs, paths)
    return inputs, value


def apply_sources(root, evidence, log, *, apply=False, promotion_log=None):
    root, evidence, log = checked_root(root), Path(evidence).absolute(), Path(log).absolute()
    current = {p: regular(root / p) for p in OWNERS}
    if any(current[p] != frozen(p) for p in OWNERS):
        bound, _ = source_receipt(root, log)
        if all(regular(root / p) == frozen(p) for p in (SSSOM, BASELINE)):
            before_promotion(root)
        else:
            if promotion_log is None:
                raise ValueError("Completed source with changed canonical anchors requires --promotion-log")
            from scripts.promote_owned_name_policy import verify_completed
            verify_completed(root, Path(promotion_log).absolute(), source_log=log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if any(regular(root / p) != frozen(p) for p in (SSSOM, BASELINE)):
        raise ValueError("Canonical or baseline anchor changed")
    before_promotion(root)
    current = propose_sources(current, timestamp=dt.datetime.now(dt.timezone.utc).isoformat())
    inputs, result, paths = source_context(root, evidence, current)
    def check():
        validate_scope(root, inputs, paths)
        before_promotion(root)
    check()
    return guarded.publish(root, current, inputs, log,
        {backup: frozen(p) for p, backup in backups(log).items()}, result, apply=apply,
        validate_scope=check)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--promotion-log", type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings
    root = checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    if target.path.resolve() != root:
        raise ValueError("Configured MIM root differs from requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", "#669 source corrections"):
        result = apply_sources(root, args.evidence or root / EVIDENCE, args.log,
                               apply=args.apply, promotion_log=args.promotion_log)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


