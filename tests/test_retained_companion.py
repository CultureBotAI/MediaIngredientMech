"""Issue #1222: TEST ONLY current review, preserving the complete fixed cohort."""

from __future__ import annotations

import csv
import io
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import ingredient_bundle_contract as native
from mediaingredientmech.export.companion_producer import PATHS
from mediaingredientmech.export.ingredient_bundle import export_bundle
from mediaingredientmech.identity_projection import MANIFEST
from mediaingredientmech.identity_projection_bundle import (
    ARCHIVE,
    OLD_REVIEW,
    OLD_REVIEW_SHA,
    declared_sources,
)
from mediaingredientmech.identity_projection_inventory import INVENTORY
from mediaingredientmech.retained_companion import ARTIFACT, CAPABILITY
from mediaingredientmech.stable_ids import LIFECYCLE_PATH, MIM_PREFIX, REGISTRY_PATH

ROOT = Path(__file__).resolve().parents[1]
BSA = "data/ingredients/mapped/Bovine_Serum_Albumin.yaml"
CLAIMS = "test-only/claims.json"
PROOF = "test-only/claim-proof.json"
BASE = "test-only/base-review.json"
BASE_PROOF = "test-only/base-proof.json"
REVIEW = "test-only/companion-review.json"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"


def encoded(value):
    return native.canonical_json(value) + b"\n"


def table(metadata, fields, rows):
    stream = io.StringIO()
    stream.write(
        "\n".join("# " + line for line in yaml.safe_dump(metadata, sort_keys=False).splitlines())
        + "\n"
    )
    writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def decision(claim, owner_sha, key):
    payload = claim["payload"]
    status = payload.get("ext_scope_review_status", payload.get("review_status"))
    value = {
        "claim_id": claim["claim_id"],
        "row_sha256": native.content_sha256(native.canonical_json(claim)),
        "owner_record": claim["owner_record"],
        "disposition": status,
        "review_reason": "TEST ONLY complete current claim judgment",
        "review_evidence": PROOF,
        "evidence_key": key,
    }
    entry = {k: value[k] for k in ["row_sha256", "owner_record", "disposition", "review_reason"]}
    entry["owner_record_sha256"] = owner_sha
    return value, entry


@pytest.fixture(scope="module")
def original():
    raw = (ROOT / ARCHIVE / OLD_REVIEW).read_bytes()
    assert native.content_sha256(raw) == OLD_REVIEW_SHA
    report = native.read_json(raw)
    return report, {name: (ROOT / ARCHIVE / name).read_bytes() for name in declared_sources(report)}


@pytest.fixture(scope="module")
def current(original):
    old, old_sources = original
    previous = native.read_json(old_sources[old["claims_file"]])["claims"]
    claims = deepcopy(previous)
    sources = {"history/" + name: raw for name, raw in old_sources.items()}
    sources["history/review.json"] = (ROOT / ARCHIVE / OLD_REVIEW).read_bytes()
    transport = {
        name: {"path": "history/" + name, "sha256": native.content_sha256(raw)}
        for name, raw in old_sources.items()
    }
    # Complete real mint inventory and current records are fixture inputs, never
    # changed on disk. Only this test's explicit current claim/table is synthetic.
    for path in sorted((ROOT / "data/ingredients").glob("*/*.yaml")):
        sources[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for name in [REGISTRY_PATH.as_posix(), LIFECYCLE_PATH.as_posix(), MANIFEST, INVENTORY]:
        sources[name] = (ROOT / name).read_bytes()
    for name in PATHS:
        sources[name] = (ROOT / name).read_bytes()
    owner_paths = {c["owner_record"] for c in claims}
    owners = {name: yaml.safe_load(sources[name]) for name in owner_paths}
    records = {name: native.content_sha256(sources[name]) for name in owner_paths}
    for claim in claims:
        payload = claim["payload"]
        owner = claim["owner_record"]
        mim_id = owners[owner]["mim_id"]
        if claim["kind"] == "mapping":
            payload["subject_id"] = mim_id
            payload["subject_label"] = owners[owner]["preferred_term"]
            if owner == BSA:
                payload["ext_scope_review_status"] = "WITHHOLD"
                payload["ext_identity_authorized"] = "false"
            claim["claim_id"] = native.stable_id(
                "mapping", [payload[k] for k in ["subject_id", "predicate_id", "object_id"]]
            )
        elif claim["kind"] == "identifier":
            if payload["owner_id"].startswith("MIM:"):
                payload["owner_id"] = mim_id
            payload["annotation_id"] = native.annotation_id(payload)
            claim["claim_id"] = payload["annotation_id"]
        else:
            payload["ingredient_id"] = mim_id
            if claim["kind"] == "occurrence" and payload["source_id"] == "CultureMech:012955":
                payload["review_status"] = "WITHHOLD"
    old_base = native.read_json(old_sources[old["base_review"]])
    metadata, fields, _ = native._base_table(old_sources[old_base["source_sssom"]])
    metadata["curie_map"]["MIM"] = MIM_PREFIX
    mappings = [c for c in claims if c["kind"] == "mapping"]
    rows = [{k: c["payload"][k] for k in fields} for c in mappings]
    sources[CANONICAL] = table(metadata, fields, rows)
    base_decisions, base_entries = [], {}
    for i, (claim, row) in enumerate(zip(mappings, rows, strict=True), 1):
        key = str(i)
        d = {
            "source_position": i,
            "row_sha256": native.content_sha256(native.canonical_json(row)),
            "owner_record": claim["owner_record"],
            "disposition": claim["payload"]["ext_scope_review_status"],
            "review_reason": "TEST ONLY complete current mapping judgment",
            "review_evidence": BASE_PROOF,
            "evidence_key": key,
        }
        base_decisions.append(d)
        base_entries[key] = {k: d[k] for k in ["row_sha256", "disposition", "review_reason"]}
        base_entries[key]["owner_record_sha256"] = records[claim["owner_record"]]
    sources[BASE_PROOF] = encoded({"entries": base_entries})
    base = {
        "schema_version": 1,
        "source_sssom": CANONICAL,
        "source_sha256": native.content_sha256(sources[CANONICAL]),
        "inputs": {name: native.content_sha256(raw) for name, raw in sources.items()},
        "record_inputs": records,
        "decisions": base_decisions,
    }
    sources[BASE] = encoded(base)
    decisions, entries = [], {}
    for i, claim in enumerate(claims):
        d, entry = decision(claim, records[claim["owner_record"]], str(i))
        decisions.append(d)
        entries[str(i)] = entry
    sources[PROOF] = encoded({"entries": entries})
    review = {
        "schema_version": 1,
        "claims_file": CLAIMS,
        "claims_sha256": "",
        "base_review": BASE,
        "base_review_sha256": native.content_sha256(sources[BASE]),
        "inputs": {name: native.content_sha256(raw) for name, raw in sources.items()},
        "record_inputs": records,
        "decisions": decisions,
        "retained_obligations": {
            "capability": CAPABILITY,
            "historical_review": {"path": "history/review.json", "sha256": OLD_REVIEW_SHA},
            "historical_sources": transport,
            "lineage": [],
        },
    }
    sources[CLAIMS] = encoded({"schema_version": 1, "claims": claims})
    refresh(review, sources, previous)
    return review, sources, previous


def refresh(review, sources, previous):
    """Rehash attack fixtures so negative tests exercise semantics, not stale bytes."""
    claims = native.read_json(sources[CLAIMS])["claims"]
    entries, decisions, lineage = {}, [], []
    for i, claim in enumerate(claims):
        d, entry = decision(claim, review["record_inputs"][claim["owner_record"]], str(i))
        entries[str(i)] = entry
        decisions.append(d)
        old = previous[i] if i < len(previous) else previous[-1]
        lineage.append(
            {
                "previous_claim_id": old["claim_id"],
                "previous_sha256": native.content_sha256(native.canonical_json(old)),
                "claim_id": claim["claim_id"],
                "sha256": native.content_sha256(native.canonical_json(claim)),
            }
        )
    sources[PROOF] = encoded({"entries": entries})
    review["inputs"][PROOF] = native.content_sha256(sources[PROOF])
    review["claims_sha256"] = native.content_sha256(sources[CLAIMS])
    review["decisions"] = decisions
    review["retained_obligations"]["lineage"] = lineage


def mutate(current, change):
    review, sources, previous = deepcopy(current)
    document = native.read_json(sources[CLAIMS])
    change(document["claims"])
    sources[CLAIMS] = encoded(document)
    refresh(review, sources, previous)
    return review, sources


def test_full_cohort_native_retention_and_no_active_leak(current):
    review, sources, _ = current
    products, loaded = native.reviewed_products(review, sources)
    account = native.read_json(products[ARTIFACT])
    assert (
        account["claim_count"],
        account["owner_count"],
        account["emitted_claim_count"],
        account["retained_claim_count"],
    ) == (51, 20, 37, 14)
    assert len(loaded["owners"]) == 20
    assert len(loaded["mappings"]) == 19
    assert len(loaded["identifiers"]) == 16
    assert any(
        x["review_status"] == "WITHHOLD" and not x["xref_eligible"] for x in loaded["identifiers"]
    )
    assert len(loaded["occurrences"]) == 2
    assert loaded["products"] == []
    assert "MIM:0000522" not in loaded["identities"]
    assert all(
        "MIM:0000522" not in native.canonical_json(x).decode()
        for k in ["mappings", "identifiers", "products", "occurrences"]
        for x in loaded[k]
    )
    retained = [e for e in account["entries"] if e["partition"] == "retained"]
    occurrence = next(
        e for e in retained if e["claim"]["payload"].get("source_id") == "CultureMech:012955"
    )
    assert occurrence["claim"]["payload"]["review_status"] == "WITHHOLD"
    assert (
        occurrence["claim"]["payload"]["quantity"]
        == occurrence["previous_claim"]["payload"]["quantity"]
    )
    assert any(e["decision"]["disposition"] == "SUPPORTED" for e in retained)
    assert all(e["blocked_by"] for e in retained)
    assert review == current[0] and sources == current[1]


@pytest.mark.parametrize(
    "attack",
    [
        "omit_bsa_mapping",
        "omit_bsa_product",
        "duplicate",
        "raw_quantity",
        "alternate_product",
        "scope_authorized",
        "scope_supported",
        "wrong_owner",
    ],
)
def test_rehashed_claim_attacks_fail(current, attack):
    def change(claims):
        mapping = next(c for c in claims if c["kind"] == "mapping" and c["owner_record"] == BSA)
        occurrence = next(
            c for c in claims if c["kind"] == "occurrence" and c["payload"].get("alternatives")
        )
        if attack == "omit_bsa_mapping":
            claims.remove(mapping)
        elif attack == "omit_bsa_product":
            claims.remove(next(c for c in claims if c["kind"] == "product"))
        elif attack == "duplicate":
            claims[-1] = deepcopy(claims[0])
        elif attack == "raw_quantity":
            occurrence["payload"]["quantity"]["value"] = "999"
        elif attack == "alternate_product":
            occurrence["payload"]["alternatives"][0]["members"][0][
                "product_id"
            ] = "MIM.product:missing"
        elif attack == "scope_authorized":
            mapping["payload"]["ext_identity_authorized"] = "true"
        elif attack == "scope_supported":
            mapping["payload"]["ext_scope_review_status"] = "SUPPORTED"
        elif attack == "wrong_owner":
            mapping["owner_record"] = next(
                c["owner_record"] for c in claims if c["owner_record"] != BSA
            )

    with pytest.raises(ValueError):
        native.reviewed_products(*mutate(current, change))


@pytest.mark.parametrize(
    "attack",
    [
        "claim_bool",
        "claim_float",
        "review_bool",
        "base_bool",
        "position_bool",
        "capability",
        "lineage",
        "history",
        "history_ref",
        "owner",
        "registry",
    ],
)
def test_control_type_currentness_and_history_refusals(current, attack):
    review, sources, previous = deepcopy(current)
    if attack.startswith("claim_"):
        document = native.read_json(sources[CLAIMS])
        document["schema_version"] = True if attack == "claim_bool" else 1.0
        sources[CLAIMS] = encoded(document)
        review["claims_sha256"] = native.content_sha256(sources[CLAIMS])
    elif attack == "review_bool":
        review["schema_version"] = True
    elif attack in {"base_bool", "position_bool"}:
        base = native.read_json(sources[BASE])
        if attack == "base_bool":
            base["schema_version"] = True
        else:
            base["decisions"][0]["source_position"] = True
        sources[BASE] = encoded(base)
        review["base_review_sha256"] = native.content_sha256(sources[BASE])
        review["inputs"][BASE] = review["base_review_sha256"]
    elif attack == "capability":
        review["retained_obligations"]["capability"] += "-unknown"
    elif attack == "lineage":
        review["retained_obligations"]["lineage"].pop()
    elif attack == "history":
        name = next(iter(review["retained_obligations"]["historical_sources"].values()))["path"]
        sources[name] += b" "
        review["inputs"][name] = native.content_sha256(sources[name])
    elif attack == "history_ref":
        review["retained_obligations"]["historical_review"]["sha256"] = "0" * 64
    elif attack == "owner":
        sources[BSA] += b"\n"
    elif attack == "registry":
        name = REGISTRY_PATH.as_posix()
        sources[name] = sources[name].replace(b"MIM:0000522", b"MIM:9999999", 1)
        review["inputs"][name] = native.content_sha256(sources[name])
    with pytest.raises(ValueError):
        native.reviewed_products(review, sources)


def test_original_positive_contract_unchanged(original):
    products, loaded = native.reviewed_products(*original)
    assert ARTIFACT not in products
    assert "retained_obligations" not in loaded
    assert len(loaded["mappings"]) == 20
    assert len(loaded["identifiers"]) == 18
    assert len(loaded["products"]) == 3
    assert len(loaded["occurrences"]) == 10


def test_rehashed_current_base_support_cannot_enter_held_path(current):
    review, sources, _ = deepcopy(current)
    base = native.read_json(sources[BASE])
    proof = native.read_json(sources[BASE_PROOF])
    d = next(x for x in base["decisions"] if x["owner_record"] == BSA)
    d["disposition"] = "SUPPORTED"
    proof["entries"][d["evidence_key"]]["disposition"] = "SUPPORTED"
    sources[BASE_PROOF] = encoded(proof)
    base["inputs"][BASE_PROOF] = native.content_sha256(sources[BASE_PROOF])
    sources[BASE] = encoded(base)
    review["base_review_sha256"] = native.content_sha256(sources[BASE])
    for name in [BASE, BASE_PROOF]:
        review["inputs"][name] = native.content_sha256(sources[name])
    with pytest.raises(ValueError, match="held mapping has positive base"):
        native.reviewed_products(review, sources)


def test_alias_cannot_replace_authenticated_mint_assignment(current):
    review, sources, previous = deepcopy(current)
    other = "data/ingredients/mapped/Cotarnine_Chloride.yaml"
    records = {n: yaml.safe_load(sources[n]) for n in [BSA, other]}
    records[BSA]["mim_id"], records[other]["mim_id"] = (
        records[other]["mim_id"],
        records[BSA]["mim_id"],
    )
    for name, record in records.items():
        sources[name] = yaml.safe_dump(record).encode()
        digest = native.content_sha256(sources[name])
        review["inputs"][name] = digest
        review["record_inputs"][name] = digest
    refresh(review, sources, previous)
    with pytest.raises(ValueError, match="authenticated original mint assignment"):
        native.reviewed_products(review, sources)


@pytest.fixture(scope="module")
def exported(current, tmp_path_factory):
    review, sources, _ = current
    root = tmp_path_factory.mktemp("retained-native")
    for name, raw in sources.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    (root / REVIEW).write_bytes(encoded(review))
    output = root / "output"
    result = export_bundle(root, Path(REVIEW), output)
    return output, result


def test_real_native_export_and_capability_refusal(exported):
    output, result = exported
    loaded = native.validate_bundle(output, expected_manifest_sha256=result["manifest_sha256"])
    assert loaded["retained_obligations"]["claim_count"] == 51
    assert len(loaded["manifest"]["cohort"]) == 20
    assert loaded["manifest"]["artifacts"]["retained_obligations"] == ARTIFACT
    with pytest.raises(ValueError, match="capabilities"):
        native.validate_bundle(output, capabilities=native.CAPABILITIES - {CAPABILITY})


@pytest.mark.parametrize(
    "attack", ["tamper", "drop_capability", "drop_member", "promote_partition"]
)
def test_rehashed_transport_tampering_refused(exported, tmp_path, attack):
    import shutil

    original, _ = exported
    output = tmp_path / "bundle"
    shutil.copytree(original, output)
    manifest = native.read_json((output / "manifest.json").read_bytes())
    if attack in {"tamper", "promote_partition"}:
        doc = native.read_json((output / ARTIFACT).read_bytes())
        if attack == "tamper":
            doc["entries"].pop()
        else:
            next(e for e in doc["entries"] if e["partition"] == "retained")["partition"] = "emitted"
        raw = encoded(doc)
        (output / ARTIFACT).write_bytes(raw)
        manifest["members"][ARTIFACT] = {"sha256": native.content_sha256(raw), "bytes": len(raw)}
    elif attack == "drop_capability":
        manifest["required_capabilities"].remove(CAPABILITY)
    else:
        (output / ARTIFACT).unlink()
        del manifest["members"][ARTIFACT]
        del manifest["artifacts"]["retained_obligations"]
    (output / "manifest.json").write_bytes(encoded(manifest))
    with pytest.raises(ValueError):
        native.validate_bundle(output)
