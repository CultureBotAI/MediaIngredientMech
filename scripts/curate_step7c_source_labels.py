#!/usr/bin/env python3
"""Guarded #313/#235 source-only curation; dry-run unless --apply.

Four reviewed owners lose seven unsafe resolving aliases; one exact di-keto
record is added from two independently counted source-field occurrences.
The CLI holds the native repository lock. Python apply callers must hold it.
No SSSOM promotion, scientific approval or unified-snapshot change is performed.
"""

from __future__ import annotations

import argparse
import copy
import datetime
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
from scripts import apply_owned_name_policy as policy  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts import step7a_guarded_publication as publication  # noqa: E402

REPORT = Path("reports/step7c_source_labels_313_235_20261102")
EVIDENCE = REPORT / "source-evidence.json"
EVIDENCE_SHA = "1a7185b74de90578fe5f42d3d44cf7c798dccb5e5fd56fc3c1c01885499b85d0"
DIRECTORY = Path("data/ingredients/mapped")
BUTANEDIOL = DIRECTORY / "14-Butanediol.yaml"
PHOSPHATE = DIRECTORY / "24-diamino-67-di-iso-propylpteridine_phosphate.yaml"
MONOKETO = DIRECTORY / "5-dehydro-D-gluconate.yaml"
PHENETHYLAMINE = DIRECTORY / "Phenethylamine_Hydrochloride.yaml"
NEW = DIRECTORY / "25-didehydro-D-gluconate.yaml"
NEW_ID = "CHEBI:11449"
NEW_NAME = "2,5-didehydro-D-gluconate"
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BEFORE = {
    BUTANEDIOL: "74b5887ec491eeb6c5f0105dbf97fd961658618af248d954b372ca8e50ad1696",
    PHOSPHATE: "b3b4232dc560571960f15affe792bafdd0bca88866f212ade3de5beab8377108",
    MONOKETO: "9ec538f8795095f65129d970c0791ffadb6a4468d93e45e8f72830b3d87301db",
    PHENETHYLAMINE: "1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320",
    SSSOM: "55823757c6b15f43de69370da7fe6c4468ff21f14e5f4994cf53115e04ae0d74",
    Path(
        "mappings/other_cross_record_baseline.tsv"
    ): "f52921f8cf4aaf16f070b9b33bb8809e0a7ee809f7a66805bdf7bd01c9610bcb",
    Path(
        "mappings/suppressed_aliases.tsv"
    ): "3d1e6c1f6393aaf05b8f7235c5393372206ea0f73db0699ddbdca14053bf8f84",
    Path(
        "mappings/ingredient_mappings.sssom.tsv.manifest.json"
    ): "1a30715b1e5e5e89bf2063a1e9eecd8c18fea13781ab9dff3214e75a553cca58",
}
TOKENS = {
    BUTANEDIOL: ("Butane-1", "4-diol"),
    PHOSPHATE: ("7-di-iso-propylpteridine Phosphate)", "0129 (2", "4-Diamino-6"),
    MONOKETO: ("5-didehydro-D-gluconate",),
    PHENETHYLAMINE: ("Phenethylamine Hydrochloride",),
}
DECISION_313 = (
    "https://github.com/CultureBotAI/MediaIngredientMech/issues/313#issuecomment-6588292718"
)
DECISION_235 = (
    "https://github.com/CultureBotAI/MediaIngredientMech/issues/235#issuecomment-6588291361"
)
APPROVAL = "NONE: source curation only; changed and new mappings require fresh native review."
NOT_BEFORE = datetime.datetime.fromisoformat("2026-11-02T20:55:18.867251+00:00")
COMMON = (
    f"Hash-bound source captures: {EVIDENCE.as_posix()} (sha256 {EVIDENCE_SHA}). "
    "Source-field counts are not recipe occurrences or positive experimental outcomes. "
    "Preserved superseded source assertions and history. No scientific/release approval is asserted."
)
VERIFICATION = {
    BUTANEDIOL: (
        "Original MicrobeDecoder CSV line 18953, BacDive 134317, utilization field gives the intact "
        "butane-1,4-diol label; Butane-1 and 4-diol are comma-split fragments, not names of a substance. "
        "Preserve the full Butane-1,4-diol alias, identity, chemistry and counts. "
        "Source: https://bacdive.dsmz.de/strain/134317 . " + DECISION_313 + ". " + COMMON
    ),
    PHOSPHATE: (
        "Both original CSV inputs contain the intact 0129 (2,4-Diamino-6,7-di-iso-propylpteridine "
        "phosphate) label (example line 31, BacDive 2); the three comma-split fragments are non-names. "
        "Preserve the local phosphate identity, parent CHEBI:73908 and 1212 source occurrences "
        "(742 resistance plus 470 sensitivity), without conflating the salt with the free base. "
        "Source: https://bacdive.dsmz.de/strain/2 . " + DECISION_313 + ". " + COMMON
    ),
    MONOKETO: (
        "CHEBI:58143 is mono-keto 5-dehydro-D-gluconate, C6H9O7; CHEBI:11449 is distinct di-keto "
        "2,5-didehydro-D-gluconate, C6H7O7. The inherited 5-didehydro-D-gluconate fragment is not "
        "a typo for this mono-keto identity. Original CSVs independently support mono-keto count 288 "
        "(11 production plus 277 utilization); do not subtract the two distinct di-keto entries. "
        "Sources: https://www.ebi.ac.uk/chebi/CHEBI:58143 ; "
        "https://www.ebi.ac.uk/chebi/CHEBI:11449 ; https://bacdive.dsmz.de/strain/34 ; "
        "https://bacdive.dsmz.de/strain/58 . " + DECISION_313 + ". " + COMMON
    ),
    PHENETHYLAMINE: (
        "CHEBI:18397 / PubChem CID 1001 / CAS 64-04-0 denote free-base C8H11N; "
        "Phenethylamine hydrochloride is distinct CID 9075 / CAS 156-28-5 / C8H12ClN. "
        "Preserve #234's free-base identity, Beta-phenylethylamine alias and chemistry; reject only "
        "the incompatible salt alias. CultureBotHT's tracked correction overlay explicitly corrects "
        "the original source pair, but does not identify the original supplier or physical bottle. "
        "Separate salt-record re-ingestion remains open on #235; no direct CAS Registry check is claimed. "
        "Sources: https://www.ebi.ac.uk/chebi/CHEBI:18397 ; "
        "https://pubchem.ncbi.nlm.nih.gov/compound/1001 ; https://pubchem.ncbi.nlm.nih.gov/compound/9075 ; "
        "https://webprod.hc-sc.gc.ca/nhpid-bdipsn/ingredReq?id=11491 ; "
        "https://github.com/CultureBotAI/CultureBotHT/pull/38 . " + DECISION_235 + ". " + COMMON
    ),
    NEW: (
        "Exact original 2,5-didehydro-D-gluconate labels occur twice, both in "
        "BacDive_Metabolite_production: CSV line 2121 / BacDive 34 and line 8749 / BacDive 58. "
        "Each source cell separately contains the mono-keto label. CHEBI:11449 denotes this di-keto "
        "anion, distinct from CHEBI:58143. The live BacDive production values are blank: no positive "
        "production assertion or chemical role is inferred. Recovered legacy damaged label "
        "5-didehydro-D-gluconate is retained as RAW_TEXT on this source-established identity under "
        "the damaged-label exception; it must not resolve to the mono-keto owner. Clarification: "
        "https://github.com/CultureBotAI/MediaIngredientMech/issues/313#issuecomment-6588401935 . "
        "No CAS, recipe occurrence or inherited "
        "mono-keto chemistry is added. Sources: https://www.ebi.ac.uk/chebi/CHEBI:11449 ; "
        "https://www.ebi.ac.uk/chebi/CHEBI:58143 ; https://bacdive.dsmz.de/strain/34 ; "
        "https://bacdive.dsmz.de/strain/58 . " + DECISION_313 + ". " + COMMON
    ),
}
_CODE = Path(__file__).read_bytes()
digest = guarded.digest
regular = policy.regular


def require(condition, message):
    if not condition:
        raise ValueError(message)


def bound_path(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "Input/receipt path must not be aliased")
    return path


def render(record):
    with tempfile.TemporaryDirectory(prefix="mim-step7c-source-validate-") as directory:
        output = Path(directory) / "record.yaml"
        write_validated_ingredient(record, output)
        return output.read_bytes()


def frozen_owners(root=ROOT):
    result = {p: regular(root / REPORT / "preimages" / p.name) for p in TOKENS}
    require(all(digest(b) == BEFORE[p] for p, b in result.items()), "Frozen owner preimage changed")
    return result


def propose_sources(original, *, timestamp):
    parsed = datetime.datetime.fromisoformat(timestamp)
    require(
        parsed.utcoffset() == datetime.timedelta(0) and parsed >= NOT_BEFORE,
        "Timestamp must be UTC and follow inspected evidence",
    )
    require(set(original) == set(TOKENS), "Expected exactly four reviewed source owners")
    outputs = {}
    for path, tokens in TOKENS.items():
        require(digest(original[path]) == BEFORE[path], f"Reviewed owner changed: {path}")
        record = copy.deepcopy(yaml.safe_load(original[path]))
        require(record["mapping_status"] == "MAPPED", "Reviewed owner must remain MAPPED")
        for token in tokens:
            matches = [s for s in record.get("synonyms", []) if s["synonym_text"] == token]
            require(
                len(matches) == 1 and matches[0]["synonym_type"] == "RAW_TEXT",
                f"Expected unique reviewed RAW_TEXT synonym: {token}",
            )
            matches[0]["synonym_type"] = "REJECTED_LABEL"
        record["ontology_mapping"].setdefault("evidence", []).append(
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": DECISION_235 if path == PHENETHYLAMINE else DECISION_313,
                "notes": VERIFICATION[path],
            }
        )
        changes = (
            "Retyped only "
            + json.dumps(tokens)
            + " as provenance-only REJECTED_LABEL. "
            + VERIFICATION[path]
        )
        record_curation_event(
            record,
            curator="Codex",
            action=(
                "REJECTED_SOURCE_LABEL_FRAGMENTS"
                if path != PHENETHYLAMINE
                else "REJECTED_WRONG_FORM_SYNONYM"
            ),
            changes=changes,
            timestamp=timestamp,
            previous_status="MAPPED",
            new_status="MAPPED",
            llm_assisted=True,
            llm_model="gpt-6",
        )
        outputs[path] = render(record)
    added = {
        "identifier": NEW_ID,
        "preferred_term": NEW_NAME,
        "ontology_mapping": {
            "ontology_id": NEW_ID,
            "ontology_label": NEW_NAME,
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
            "evidence": [
                {
                    "evidence_type": "DATABASE_MATCH",
                    "source": "microbedecoder original CSV; BacDive; ChEBI",
                    "notes": VERIFICATION[NEW],
                }
            ],
        },
        "mapping_status": "MAPPED",
        "synonyms": [
            {
                "synonym_text": "5-didehydro-D-gluconate",
                "synonym_type": "RAW_TEXT",
                "source": "microbedecoder",
            }
        ],
        "occurrence_statistics": {
            "total_occurrences": 0,
            "media_count": 0,
            "source_occurrences": [
                {
                    "source": "microbedecoder",
                    "count": 2,
                    "source_columns": "BacDive_Metabolite_production",
                }
            ],
        },
        "ingredient_type": "SINGLE_INGREDIENT",
    }
    record_curation_event(
        added,
        curator="Codex",
        action="CREATED_FROM_ORIGINAL_SOURCE_LABEL",
        changes=VERIFICATION[NEW],
        timestamp=timestamp,
        new_status="MAPPED",
        llm_assisted=True,
        llm_model="gpt-6",
    )
    outputs[NEW] = render(added)
    return outputs


def evidence_inputs(root, evidence):
    raw = regular(evidence)
    require(digest(raw) == EVIDENCE_SHA, "Reviewed source evidence manifest changed")
    doc = json.loads(raw)
    require(
        doc["before_sha256"] == {str(p): h for p, h in BEFORE.items()}
        and doc["scientific_approval_added"] is False
        and doc["source_counts_are_experimental_outcomes"] is False,
        "Evidence contract differs",
    )
    inputs = {evidence: raw}
    for name, info in doc["files"].items():
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts, "Unsafe evidence path")
        data = regular(root / path)
        require(
            digest(data) == info["sha256"] and len(data) == info["bytes"],
            f"Evidence changed: {name}",
        )
        inputs[root / path] = data
    return inputs


def code_inputs():
    require(regular(Path(__file__)) == _CODE, "Loaded writer source changed")
    require(
        regular(Path(publication.__file__)) == publication._CODE, "Loaded journal adapter changed"
    )
    for path, loaded in policy._LOADED_CODE.items():
        require(regular(path) == loaded, "Loaded shared dependency changed")
    paths = [
        Path(__file__),
        Path(publication.__file__),
        Path(policy.__file__),
        Path(guarded.__file__),
        ROOT / "MAPPING_SEMANTICS.md",
        ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml",
        ROOT / "src/mediaingredientmech/validation/write_validated.py",
        ROOT / "src/mediaingredientmech/curate/curation_event.py",
        ROOT / "src/mediaingredientmech/curate/apply_receipt.py",
    ]
    return {p: regular(p) for p in paths}


def validate_scope(root, inputs, paths, *, completed=False):
    policy.validate_scope(root, inputs, paths)
    require(((root / NEW) in paths) == completed, "New owner path exists unexpectedly or is absent")
    for path in paths - {root / NEW}:
        record = yaml.safe_load(inputs[path])
        if isinstance(record, dict):
            require(
                record.get("identifier") != NEW_ID
                and not (
                    record.get("mapping_status") != "REJECTED"
                    and (record.get("ontology_mapping") or {}).get("ontology_id") == NEW_ID
                ),
                f"Destination identity already held: {path}",
            )


def backups(log):
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in BEFORE}


def source_context(root, evidence, outputs, original, *, completed=False):
    paths = policy.ingredient_paths(root)
    inputs = {p: regular(p) for p in paths}
    inputs.update({root / p: regular(root / p) for p in BEFORE})
    inputs.update(evidence_inputs(root, evidence) | code_inputs())
    require(set(original) == set(BEFORE), "Missing source or canonical preimage")
    require(
        all(digest(b) == BEFORE[p] for p, b in original.items()),
        "Reviewed source/canonical anchor changed",
    )
    require(
        all(inputs[root / p] == original[p] for p in BEFORE if p not in TOKENS),
        "Canonical anchor changed; this source receipt is not a promotion receipt",
    )
    historical = dict(inputs)
    historical.pop(root / NEW, None)
    historical.update({root / p: b for p, b in original.items()})
    result = {
        "phase": "sources",
        "approval": APPROVAL,
        "timestamp": yaml.safe_load(outputs[NEW])["curation_history"][-1]["timestamp"],
        "evidence_manifest": str(evidence),
        "evidence_manifest_sha256": EVIDENCE_SHA,
        "input_sha256": {str(p): digest(b) for p, b in historical.items()},
        "output_sha256": {str(p): digest(b) for p, b in outputs.items()},
        "sssom_before_sha256": BEFORE[SSSOM],
        "records": [
            {
                "source_record": str(p),
                "shape": "new_record" if p == NEW else "source_synonym_retirement",
                "before_yaml_sha256": None if p == NEW else BEFORE[p],
                "after_yaml_sha256": digest(b),
                "change": yaml.safe_load(b)["curation_history"][-1]["changes"],
                "verification": VERIFICATION[p],
            }
            for p, b in outputs.items()
        ],
    }
    validate_scope(root, inputs, paths, completed=completed)
    return inputs, result, paths


def source_receipt(root, log):
    """Verify the exact completed source phase, including its created-owner journal."""
    root, log = policy.checked_root(root), bound_path(log)
    saved = json.loads(regular(log))
    original = {p: regular(backup) for p, backup in backups(log).items()}
    outputs = propose_sources({p: original[p] for p in TOKENS}, timestamp=saved["timestamp"])
    require(
        all(regular(root / p) == b for p, b in outputs.items()),
        "Partial or changed source correction",
    )
    inputs, expected, paths = source_context(
        root, bound_path(Path(saved["evidence_manifest"])), outputs, original, completed=True
    )
    inputs[log] = policy.completed_receipt(log, expected, root, changed=set(TOKENS), created={NEW})
    from kg_microbe_write.transaction import JOURNAL_VERSION

    journal = bound_path(Path(saved["transaction"]["journal"]))
    directory = publication._journal_path(log)
    require(
        journal.parent == directory
        and journal.name.startswith("write-")
        and journal.suffix == ".json"
        and sorted(directory.iterdir()) == [journal],
        "Completed journal membership differs",
    )
    raw = regular(journal)
    expected_journal = {
        "version": JOURNAL_VERSION,
        "root": str(root),
        "status": "complete",
        "changed": sorted(str(root / p) for p in TOKENS),
        "created": [str(root / NEW)],
        "previous": {str(root / p): original[p].decode() for p in TOKENS},
    }
    require(
        json.loads(raw) == expected_journal and digest(raw) == saved["journal_sha256"],
        "Completed native journal payload differs",
    )
    inputs[journal] = raw
    inputs.update({backup: original[p] for p, backup in backups(log).items()})
    validate_scope(root, inputs, paths, completed=True)
    return inputs, saved


def apply_sources(root, evidence, log, *, apply=False):
    root, evidence, log = policy.checked_root(root), bound_path(evidence), bound_path(log)
    original = {p: regular(root / p) for p in BEFORE}
    if any(digest(original[p]) != BEFORE[p] for p in TOKENS) or (root / NEW).exists():
        source_receipt(root, log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    outputs = propose_sources(
        {p: original[p] for p in TOKENS},
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    )
    inputs, result, paths = source_context(root, evidence, outputs, original)
    return publication.publish(
        root,
        outputs,
        inputs,
        log,
        {backup: original[p] for p, backup in backups(log).items()},
        result,
        apply=apply,
        validate_scope=lambda: validate_scope(root, inputs, paths),
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--log", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    root = policy.checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "#313/#235 bounded source curation"):
        result = apply_sources(root, args.evidence or root / EVIDENCE, args.log, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
