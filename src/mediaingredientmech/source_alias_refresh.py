"""Prove the #1149 source-alias successor; never carry approval across new bytes.

This bounded projection changes one owner and one mapping row outside the
companion cohort. All prior policy history is retained. Scientific approval is
separately checked by the native full mapping review, not granted here.
"""

from __future__ import annotations

import subprocess
from copy import deepcopy
from pathlib import Path

import yaml  # type: ignore[import-untyped]

from mediaingredientmech.ingredient_bundle_contract import canonical_json, content_sha256, read_json
from mediaingredientmech.registry_correction_refresh import receipt_inventory
from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

OWNER = "data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml"
NOTE_OWNER = "data/ingredients/unmapped/3-methylacetate.yaml"
SUBJECT = "MIM:Sodium_Acetate_Trihydrate"
ALIAS = "Na acetate x 3 H2O"
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
MANIFEST = SOURCE + ".manifest.json"
SIDECAR = "mappings/suppressed_aliases.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
UPDATE = "source_alias_addition_updates"
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/1149"
TOKEN_SOURCE = "https://mediadive.dsmz.de/download/ingredient/1315/json"
ADDED_SOURCE = "MIM:MediaDive ingredient 1315; MIM issue 1149"
CODE = "src/mediaingredientmech/source_alias_refresh.py"
_LOADED = Path(__file__).read_bytes()


def require(condition, message):
    if not condition:
        raise ValueError("Source alias addition: " + message)


def verify_owner(before: bytes, after: bytes) -> None:
    """Check the complete owner; no chemistry, counts, roles or identity edits."""
    old, new = yaml.safe_load(before), yaml.safe_load(after)
    expected = deepcopy(old)
    expected["synonyms"].append(
        {
            "synonym_text": ALIAS,
            "synonym_type": "HYDRATE_FORM",
            "source": TOKEN_SOURCE,
        }
    )
    history = new.get("curation_history", [])
    require(len(history) == len(old["curation_history"]) + 1, "expected one history event")
    event = history[-1]
    require(
        event.get("action") == "ADDED_SOURCE_ALIAS"
        and event.get("llm_assisted") is True
        and event.get("previous_status") == event.get("new_status") == "MAPPED"
        and event.get("curator") == "claude"
        and "#1149" in event.get("changes", ""),
        "history does not identify the scoped source correction",
    )
    expected["curation_history"].append(event)
    require(canonical_json(new) == canonical_json(expected), "unaccounted owner change")
    require(
        old["identifier"] == old["ontology_mapping"]["ontology_id"] == "CHEBI:32138",
        "wrong hydrate identity",
    )
    require(old["chemical_properties"]["cas_rn"] == "6131-90-4", "wrong hydrate CAS")


def verify_row(old, new):
    expected = dict(old)
    require(
        old["subject_id"] == SUBJECT
        and old["object_id"] == "CHEBI:32138"
        and old["predicate_id"] == "skos:exactMatch",
        "wrong exact mapping",
    )
    require(ALIAS not in old["other"].split("|"), "alias already published")
    expected["other"] += "|" + ALIAS
    expected["source"] += "|" + ADDED_SOURCE
    expected["mapping_date"] = new["mapping_date"]
    require(new == expected, "unaccounted row change")


def verify_provenance_owner(before: bytes, after: bytes) -> None:
    """#1151 changes active provenance, preserving rejection and every assertion."""
    old, new = yaml.safe_load(before), yaml.safe_load(after)
    expected = deepcopy(old)
    require(
        old["identifier"] == "UNMAPPED_0736"
        and old["mapping_status"] == "REJECTED"
        and not old.get("ontology_mapping"),
        "wrong provenance-only owner",
    )
    history = new.get("curation_history", [])
    require(len(history) == len(old["curation_history"]) + 1, "expected one provenance event")
    event = history[-1]
    require(
        event.get("action") == "CORRECTED_SOURCE_PROVENANCE"
        and event.get("llm_assisted") is True
        and event.get("previous_status") == event.get("new_status") == "REJECTED"
        and "#1151" in event.get("changes", ""),
        "provenance history differs",
    )
    require(
        isinstance(new.get("notes"), str)
        and "No replacement compound is inferred." in new["notes"]
        and "Retain REJECTED status" in new["notes"],
        "missing unresolved-identity boundary",
    )
    expected["notes"] = new["notes"]
    expected["curation_history"].append(event)
    require(canonical_json(new) == canonical_json(expected), "unaccounted provenance-owner change")


def verify_source_alias_addition(prior, before, current, context):
    from mediaingredientmech.ingredient_bundle_refresh import (
        SourceAliasAdditionContext,
        _form_member,
    )

    require(isinstance(context, SourceAliasAdditionContext), "typed context required")
    root = context.root
    require(root.absolute() == root.resolve(), "aliased root")
    require(content_sha256(current[MANIFEST]) == context.manifest_sha256, "manifest pin differs")
    require(_form_member(root, CODE).read_bytes() == _LOADED, "loaded verifier differs")
    old, new = read_json(before[MANIFEST]), read_json(current[MANIFEST])
    require(set(new) == set(old) | {UPDATE}, "manifest membership changed")
    mutable = {"artifacts", "source_owner_sha256", UPDATE}
    require(
        canonical_json({k: v for k, v in old.items() if k not in mutable})
        == canonical_json({k: v for k, v in new.items() if k not in mutable}),
        "retained policy history changed",
    )
    prefix = old.get(UPDATE, [])
    require(
        isinstance(prefix, list)
        and isinstance(new[UPDATE], list)
        and new[UPDATE][:-1] == prefix
        and len(new[UPDATE]) == len(prefix) + 1,
        "exactly one append required",
    )
    update = new[UPDATE][-1]
    require(
        set(update)
        == {
            "issue",
            "approval",
            "prior_manifest_sha256",
            "mapping_receipt",
            "mapping_receipt_sha256",
            "generation_manifest",
            "generation_manifest_sha256",
        },
        "unexpected update fields",
    )
    require(
        update["issue"] == ISSUE and update["approval"] == "NONE: scientific review is separate",
        "update confers approval or changes issue",
    )
    require(
        update["prior_manifest_sha256"] == content_sha256(before[MANIFEST]), "prior pin differs"
    )
    require(
        not {OWNER, NOTE_OWNER}.intersection(prior["record_inputs"]),
        "selected companion owner changed",
    )
    bound: dict[str, str] = {}

    def read(name):
        raw = _form_member(root, name).read_bytes()
        digest = content_sha256(raw)
        require(name not in bound or bound[name] == digest, "input changed during proof")
        bound[name] = digest
        return raw

    def historical(name):
        return subprocess.check_output(["git", "show", context.baseline + ":" + name], cwd=root)

    for path in (MANIFEST, SOURCE, SIDECAR, BASELINE):
        require(historical(path) == before[path], "durable baseline differs")
        require(read(path) == current[path], "current artifact differs")
    require(
        before[SIDECAR] == current[SIDECAR] and before[BASELINE] == current[BASELINE],
        "suppression sidecar/baseline changed",
    )
    for doc, values in ((old, before), (new, current)):
        require(
            doc["artifacts"] == {p: content_sha256(values[p]) for p in (SOURCE, SIDECAR, BASELINE)},
            "manifest artifact pins differ",
        )
    old_owner, new_owner = historical(OWNER), read(OWNER)
    verify_owner(old_owner, new_owner)
    require(old["source_owner_sha256"][OWNER] == content_sha256(old_owner), "old owner pin differs")
    expected_owners = dict(old["source_owner_sha256"])
    expected_owners[OWNER] = content_sha256(new_owner)
    note_before, note_after = historical(NOTE_OWNER), read(NOTE_OWNER)
    verify_provenance_owner(note_before, note_after)
    require(
        old["source_owner_sha256"][NOTE_OWNER] == content_sha256(note_before),
        "old note-owner pin differs",
    )
    expected_owners[NOTE_OWNER] = content_sha256(note_after)
    require(new["source_owner_sha256"] == expected_owners, "unaccounted owner inventory change")
    proof = verify_mapping_chain(root)
    require(receipt_inventory(root) == set(proof["receipt_paths"]), "receipt inventory differs")
    require(proof["receipt_paths"][-1] == update["mapping_receipt"], "not final native receipt")
    receipt_bytes = read(update["mapping_receipt"])
    require(
        content_sha256(receipt_bytes) == update["mapping_receipt_sha256"], "receipt pin differs"
    )
    receipt = proof["receipts"][-1]
    require(receipt == read_json(receipt_bytes), "replayed receipt differs")
    require(
        receipt["issue"] == ISSUE
        and receipt["before_sha256"] == content_sha256(before[SOURCE])
        and receipt["after_sha256"] == content_sha256(current[SOURCE]),
        "receipt endpoints differ",
    )
    require(
        len(receipt["records"]) == 2 and receipt["touched_subjects"] == [SUBJECT],
        "unexpected native owner scope",
    )
    owners = {r["source_record"]: r for r in receipt["records"]}
    require(set(owners) == {OWNER, NOTE_OWNER}, "unexpected native owner set")
    owner = owners[OWNER]
    require(
        owner["source_record"] == OWNER
        and owner["shape"] == "source_alias_addition"
        and owner["before_yaml_sha256"] == content_sha256(old_owner)
        and owner["after_yaml_sha256"] == content_sha256(new_owner),
        "native owner pins differ",
    )
    note = owners[NOTE_OWNER]
    require(
        note["shape"] == "source_provenance_note"
        and note["before_yaml_sha256"] == content_sha256(note_before)
        and note["after_yaml_sha256"] == content_sha256(note_after),
        "native note-owner pins differ",
    )
    require(len(receipt["changes"]) == 1, "expected one changed mapping")
    change = receipt["changes"][0]
    require(
        change["kind"] == "changed" and change["before_position"] == change["after_position"],
        "mapping membership or order changed",
    )
    require(
        receipt["position_map"] == list(range(1, len(receipt["position_map"]) + 1)),
        "mapping positions changed",
    )
    verify_row(change["before"], change["after"])
    event = yaml.safe_load(new_owner)["curation_history"][-1]
    require(
        change["after"]["mapping_date"] == event["timestamp"][:10], "row date differs from curation"
    )
    generation = read_json(read(update["generation_manifest"]))
    require(
        bound[update["generation_manifest"]] == update["generation_manifest_sha256"],
        "generation manifest pin differs",
    )
    # The generator's complete input/artifact inventory remains explicit evidence.
    # Attribution is hash-bound here; publication also checks the actual candidate row.
    require(
        generation["external_sssom_validation"] == "passed", "native generation did not validate"
    )
    for name, digest in proof["input_hashes"].items():
        require(content_sha256(read(name)) == digest, "replayed input changed")
    for name in (CODE, "src/mediaingredientmech/ingredient_bundle_refresh.py"):
        read(name)
    return {
        "scientific_approval_added": False,
        "baseline": context.baseline,
        "source_records": [OWNER, NOTE_OWNER],
        "appended_update": update,
        "receipt_paths": proof["receipt_paths"],
        "input_sha256": bound,
        "attribution_contract": "Native generation attribution hash-bound; full canonical and owner transition replayed.",
    }
