"""Exercise real reviewed cases and adversarial owner/payload/transport changes."""

import copy
import shutil
from pathlib import Path

import pytest

from mediaingredientmech.export.ingredient_bundle import export_bundle
from mediaingredientmech.ingredient_bundle_contract import (
    ARTIFACTS,
    CAPABILITIES,
    annotation_id,
    canonical_json,
    content_sha256,
    product_id,
    read_annotation_table,
    read_json,
    reviewed_products,
    safe_member,
    validate_bundle,
    validate_payload,
)

ROOT = Path(__file__).resolve().parents[1]
REVIEW = Path("reports/ingredient_bundle_20260924/review.json")


@pytest.fixture(scope="module")
def inputs():
    review = read_json((ROOT / REVIEW).read_bytes())
    names = {
        review["base_review"],
        review["claims_file"],
        *review["inputs"],
        *review["record_inputs"],
    }
    sources = {name: (ROOT / name).read_bytes() for name in names}
    return review, sources


@pytest.fixture(scope="module")
def compiled(inputs):
    return reviewed_products(*inputs)


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    output = tmp_path_factory.mktemp("reviewed-bundle") / "release"
    result = export_bundle(ROOT, REVIEW, output)
    return output, result


def test_scoped_case_identities_and_registry_ownership(compiled):
    artifacts, loaded = compiled
    assert len(loaded["mappings"]) == 20
    assert loaded["identities"]["MIM:Rifamycin"] == "CHEBI:26580"
    assert loaded["identities"]["MIM:Rifamycin_Sv"] == "CHEBI:29673"
    assert loaded["identities"]["MIM:Xanthine"] == "CHEBI:17712"
    assert "CHEBI:15318" not in loaded["identities"].values()
    assert loaded["identities"]["MIM:Polymyxin_B"] == "NCIT:C61894"
    assert loaded["identities"]["MIM:Proteose_Peptone_No_2"] == "MICRO:0002393"
    annotations = read_annotation_table(artifacts[ARTIFACTS["identifiers"]])
    assert sorted(annotations, key=lambda r: r["annotation_id"]) == sorted(
        loaded["identifiers"], key=lambda r: r["annotation_id"]
    )
    assert len(annotations) == 18
    assert not any(
        a["owner_id"] in {"MIM:Rifamycin", "MIM:Sorbitan_Monooleate"} for a in annotations
    )
    assert [a["identifier"] for a in annotations if a["owner_id"] == "MIM:Rifamycin_Sv"] == [
        "cas:6998-60-3"
    ]
    assert [a["identifier"] for a in annotations if a["owner_id"] == "MIM:Xanthine"] == [
        "cas:69-89-6"
    ]


def test_source_status_review_status_and_invalid_values_are_distinct(compiled):
    annotations = compiled[1]["identifiers"]
    acriflavine = [a for a in annotations if a["owner_id"] == "MIM:Acriflavine"]
    assert len(acriflavine) == 3
    historical = next(a for a in acriflavine if a["source_status"] == "SUPERSEDED")
    assert historical["identifier"] == "cas:8048-52-0"
    assert historical["review_status"] == "SUPPORTED"
    assert historical["source_currentness"] == "HISTORICAL"
    assert not historical["xref_eligible"]
    original = next(a for a in acriflavine if a["source_id"].startswith("CultureBotHT:"))
    assert original["identifier"] == historical["identifier"]
    assert original["source_status"] == "REPORTED" and original["source_currentness"] == "UNKNOWN"
    assert original["annotation_id"] != historical["annotation_id"]
    assert [(a["identifier"], a["source_status"]) for a in acriflavine if a["xref_eligible"]] == [
        ("cas:65589-70-0", "PRIMARY")
    ]
    bsa = next(a for a in annotations if a["owner_id"] == "MIM:Bovine_Serum_Albumin")
    assert bsa["source_status"] == "GENERIC (FAMILY)" and bsa["identifier_scope"] == "material"
    lysozyme = next(a for a in annotations if a["owner_id"] == "MIM:Lysozyme")
    assert lysozyme["raw_identifier"] == "2650-88-3" and lysozyme["identifier"] == ""
    assert lysozyme["identifier_validity"] == "INVALID" and not lysozyme["xref_eligible"]
    assert "12650-88-3" not in canonical_json(annotations).decode()


def test_seven_bsa_recipes_and_explicit_product_alternatives(compiled):
    loaded = compiled[1]
    original = read_json(
        (
            ROOT
            / "reports/sssom_completion_20260921/mapping_review/identity-review-20260924/bsa-recipe-occurrences.json"
        ).read_bytes()
    )["occurrences"]
    occurrences = [
        o for o in loaded["occurrences"] if o["ingredient_id"] == "MIM:Bovine_Serum_Albumin"
    ]
    recipes = {o["source_id"]: o for o in occurrences if o["source_kind"] == "recipe"}
    assert len(recipes) == len(original) == 7
    for entry in original:
        occurrence = recipes[entry["recipe_id"]]
        assert occurrence["source_payload"] == entry
        assert occurrence["quantity"] == entry["components"][0]["concentration"]
        assert occurrence["preparation"] == entry["preparation_notes"]
        assert occurrence["product_id"] is None
    group = recipes["CultureMech:015191"]["alternatives"][0]
    assert group["operator"] == "one_of" and group["selection_status"] == "UNSPECIFIED"
    assert {m["product_id"] for m in group["members"]} == {
        product_id("Sigma-Aldrich", "A9647"),
        product_id("Sigma-Aldrich", "A7409"),
    }
    source = next(o for o in occurrences if o["source_kind"] == "observation")
    assert source["product_id"] == product_id("Sigma-Aldrich", "A7030")
    assert "heat shock" in source["preparation"]
    assert all("heat shock" not in (o["preparation"] or "") for o in recipes.values())
    products = {p["catalog_number"]: p for p in loaded["products"]}
    assert set(products) == {"A7030", "A9647", "A7409"}
    assert not any(a["owner_id"] == products["A7409"]["product_id"] for a in loaded["identifiers"])
    sorbitan = [o for o in loaded["occurrences"] if o["ingredient_id"] == "MIM:Sorbitan_Monooleate"]
    assert {o["source_id"] for o in sorbitan} == {"CultureMech:008837", "CultureMech:008839"}
    assert all(o["product_id"] is None for o in sorbitan)
    assert (
        loaded["identities"]["MIM:Sorbitan_Monooleate"]
        == "kgmicrobe.ingredient:sorbitan_monooleate"
    )


def test_deterministic_immutable_export_and_manifest_pin(exported, tmp_path):
    first, result = exported
    second = tmp_path / "second"
    assert export_bundle(ROOT, REVIEW, second) == result
    files = [p.relative_to(first) for p in first.rglob("*") if p.is_file()]
    assert all((first / p).read_bytes() == (second / p).read_bytes() for p in files)
    assert (
        validate_bundle(first, expected_manifest_sha256=result["manifest_sha256"])["fingerprint"]
        == result["manifest_sha256"]
    )
    with pytest.raises(ValueError, match="activation pin"):
        validate_bundle(first, expected_manifest_sha256="0" * 64)
    with pytest.raises(ValueError, match="immutable"):
        export_bundle(ROOT, REVIEW, first)


def rehash_member(bundle, name):
    manifest = read_json((bundle / "manifest.json").read_bytes())
    content = (bundle / name).read_bytes()
    manifest["members"][name] = {"sha256": content_sha256(content), "bytes": len(content)}
    (bundle / "manifest.json").write_bytes(canonical_json(manifest) + b"\n")


@pytest.mark.parametrize("artifact", list(ARTIFACTS.values()))
def test_rehashed_artifacts_cannot_replace_reviewed_projection(exported, tmp_path, artifact):
    bundle = tmp_path / "changed"
    shutil.copytree(exported[0], bundle)
    path = bundle / artifact
    path.write_bytes(path.read_bytes() + b"\n")
    rehash_member(bundle, artifact)
    with pytest.raises(ValueError, match="reviewed reconstruction"):
        validate_bundle(bundle)


@pytest.mark.parametrize(
    "attack",
    ["missing", "undeclared", "schema", "boolean_version", "capability", "optional", "cohort"],
)
def test_bundle_layout_and_capability_fail_closed(exported, tmp_path, attack):
    bundle = tmp_path / "changed"
    shutil.copytree(exported[0], bundle)
    manifest = read_json((bundle / "manifest.json").read_bytes())
    if attack == "missing":
        name = ARTIFACTS["occurrences"]
        (bundle / name).unlink()
        del manifest["members"][name]
    elif attack == "undeclared":
        (bundle / ".ignored-claims.json").write_text("{}")
    elif attack == "schema":
        manifest["schema_version"] = 2
    elif attack == "boolean_version":
        manifest["schema_version"] = True
    elif attack == "capability":
        manifest["required_capabilities"].append("unknown-v9")
    elif attack == "optional":
        manifest["artifacts"]["products"] = None
    else:
        manifest["cohort"] = []
    (bundle / "manifest.json").write_bytes(canonical_json(manifest))
    with pytest.raises(ValueError):
        validate_bundle(bundle)


def test_consumer_must_support_occurrences(exported):
    with pytest.raises(ValueError, match="lacks required"):
        validate_bundle(exported[0], capabilities=CAPABILITIES - {"ingredient-occurrences-v1"})


def mutated_inputs(inputs, kind, mutate, *, update_test_proof=False):
    """Model coherent tampering; optional proof edits are synthetic test approvals only."""
    review, sources = copy.deepcopy(inputs)
    claims = read_json(sources[review["claims_file"]])
    claim = next(c for c in claims["claims"] if c["kind"] == kind)
    mutate(claim)
    sources[review["claims_file"]] = canonical_json(claims)
    review["claims_sha256"] = content_sha256(sources[review["claims_file"]])
    decision = next(d for d in review["decisions"] if d["claim_id"] == claim["claim_id"])
    decision["row_sha256"] = content_sha256(canonical_json(claim))
    if update_test_proof:
        name = decision["review_evidence"]
        proof = read_json(sources[name])
        proof["entries"][decision["evidence_key"]]["row_sha256"] = decision["row_sha256"]
        sources[name] = canonical_json(proof)
        review["inputs"][name] = content_sha256(sources[name])
    return review, sources


@pytest.mark.parametrize("kind", ["mapping", "identifier", "product", "occurrence"])
def test_changed_complete_payload_requires_matching_evidence(inputs, kind):
    def mutate(claim):
        key = {
            "mapping": "comment",
            "identifier": "raw_identifier",
            "product": "preparation",
            "occurrence": "preparation",
        }[kind]
        claim["payload"][key] = "unreviewed change"

    with pytest.raises(ValueError, match="disagrees"):
        reviewed_products(*mutated_inputs(inputs, kind, mutate))


@pytest.mark.parametrize("kind", ["identifier", "product", "occurrence"])
def test_owner_is_checked_independently_of_review_claim(inputs, kind):
    field = "owner_id" if kind == "identifier" else "ingredient_id"

    def mutate(claim):
        claim["payload"][field] = "MIM:Rifamycin"
        if kind == "identifier":
            claim["payload"]["annotation_id"] = annotation_id(claim["payload"])

    with pytest.raises(ValueError, match="another ingredient"):
        reviewed_products(*mutated_inputs(inputs, kind, mutate, update_test_proof=True))


def test_scope_cannot_be_authorized_from_matching_vocabulary_only(inputs):
    def mutate(claim):
        claim["payload"]["ext_subject_scope"] = "mimscope:chemical_family"
        claim["payload"]["ext_object_scope"] = "mimscope:defined_substance"

    with pytest.raises(ValueError, match="matching scope"):
        reviewed_products(*mutated_inputs(inputs, "mapping", mutate, update_test_proof=True))


@pytest.mark.parametrize("status", ["SUPERSEDED", "HISTORICAL", "DEPRECATED", "WITHDRAWN"])
def test_source_history_cannot_be_mislabeled_current(compiled, status):
    payload = copy.deepcopy(next(a for a in compiled[1]["identifiers"] if a["xref_eligible"]))
    payload["source_status"] = status
    payload["annotation_id"] = annotation_id(payload)
    with pytest.raises(ValueError, match="historical source"):
        validate_payload("identifier", payload)


def test_ids_keep_distinct_catalog_products_and_claim_sources(compiled):
    # Synthetic catalog keys test identity behavior, not real supplier chemistry.
    first = product_id("Example Supplier", "TEST-1")
    second = product_id("Example Supplier", "TEST-2")
    assert first != second
    assert first == product_id(" example supplier ", "TEST-1")
    original = copy.deepcopy(next(a for a in compiled[1]["identifiers"] if a["xref_eligible"]))
    one = dict(original, owner_id=first)
    two = dict(original, owner_id=second)
    assert one["identifier"] == two["identifier"]
    assert annotation_id(one) != annotation_id(two)
    changed = dict(original, source_status="NEW_SOURCE_STATUS")
    assert annotation_id(changed) != annotation_id(original)
    changed = dict(original, xref_eligible=False)
    assert annotation_id(changed) == annotation_id(original)
    assert content_sha256(canonical_json(changed)) != content_sha256(canonical_json(original))


def test_selected_product_and_alternatives_are_exclusive(compiled):
    payload = copy.deepcopy(next(o for o in compiled[1]["occurrences"] if o["alternatives"]))
    payload["product_id"] = payload["alternatives"][0]["members"][0]["product_id"]
    with pytest.raises(ValueError, match="selected product"):
        validate_payload("occurrence", payload)


@pytest.mark.parametrize(
    "name",
    ["../outside", "/outside", "sources/../../outside", "sources//duplicate", "sources\\outside"],
)
def test_bundle_member_paths_are_confined(tmp_path, name):
    with pytest.raises(ValueError, match="Unsafe"):
        safe_member(tmp_path, name)


def test_json_rejects_duplicate_and_nonfinite_values():
    with pytest.raises(ValueError, match="Duplicate"):
        read_json(b'{"a": 1, "a": 2}')
    with pytest.raises(ValueError, match="Non-finite"):
        read_json(b'{"a": NaN}')
    with pytest.raises(ValueError):
        canonical_json({"a": float("nan")})


def test_tsv_claim_tuples_reject_duplicate_rows_and_invalid_booleans(compiled):
    table = compiled[0][ARTIFACTS["identifiers"]]
    lines = table.splitlines(keepends=True)
    with pytest.raises(ValueError, match="Duplicate"):
        read_annotation_table(table + lines[1])
    with pytest.raises(ValueError, match="TSV boolean"):
        read_annotation_table(table.replace(b"\ttrue\n", b"\tTRUE\n", 1))


def synthetic_review_changes(inputs, mutate):
    """Create test-only matching proofs to exercise constraints beyond evidence hashes."""
    review, sources = copy.deepcopy(inputs)
    document = read_json(sources[review["claims_file"]])
    decisions = {d["claim_id"]: d for d in review["decisions"]}
    proof_files = {}
    for claim in document["claims"]:
        decision = decisions[claim["claim_id"]]
        mutate(claim)
        decision["claim_id"] = claim["claim_id"]
        decision["row_sha256"] = content_sha256(canonical_json(claim))
        decision["disposition"] = (
            "SUPPORTED" if claim["kind"] == "mapping" else claim["payload"]["review_status"]
        )
        name = decision["review_evidence"]
        proof = proof_files.setdefault(name, read_json(sources[name]))
        proof["entries"][decision["evidence_key"]].update(
            row_sha256=decision["row_sha256"], disposition=decision["disposition"]
        )
    for name, proof in proof_files.items():
        sources[name] = canonical_json(proof)
        review["inputs"][name] = content_sha256(sources[name])
    sources[review["claims_file"]] = canonical_json(document)
    review["claims_sha256"] = content_sha256(sources[review["claims_file"]])
    return review, sources


@pytest.mark.parametrize("kind", ["mapping", "identifier", "product", "occurrence"])
def test_claim_envelope_id_must_match_payload_identity(inputs, kind):
    def mutate(claim):
        if claim["kind"] == kind:
            claim["claim_id"] += "-unexpected"

    with pytest.raises(ValueError, match="claim ID"):
        reviewed_products(*synthetic_review_changes(inputs, mutate))


@pytest.mark.parametrize("keep_active", ["xref", "occurrence", "neither"])
def test_supported_facts_cannot_activate_a_withheld_product(inputs, keep_active):
    product = product_id("Sigma-Aldrich", "A7030")

    def mutate(claim):
        payload = claim["payload"]
        if claim["kind"] == "product" and payload["product_id"] == product:
            payload["review_status"] = "WITHHOLD"
        if (
            keep_active != "xref"
            and claim["kind"] == "identifier"
            and payload["owner_id"] == product
        ):
            payload["xref_eligible"] = False
        if (
            keep_active != "occurrence"
            and claim["kind"] == "occurrence"
            and payload["product_id"] == product
        ):
            payload["review_status"] = "WITHHOLD"

    changed = synthetic_review_changes(inputs, mutate)
    if keep_active == "neither":
        assert reviewed_products(*changed)[1]["products"]
    else:
        with pytest.raises(ValueError, match="withheld product"):
            reviewed_products(*changed)


def test_whitespace_cannot_hide_historical_status(compiled):
    payload = copy.deepcopy(next(a for a in compiled[1]["identifiers"] if a["xref_eligible"]))
    payload["source_status"] = " SUPERSEDED "
    payload["annotation_id"] = annotation_id(payload)
    with pytest.raises(ValueError, match="historical source"):
        validate_payload("identifier", payload)


def test_synthetic_products_sharing_cas_survive_reviewed_export(inputs, compiled):
    """Synthetic supplier specifications test joins; they are not BSA product evidence."""
    review, sources = copy.deepcopy(inputs)
    document = read_json(sources[review["claims_file"]])
    owner = "data/ingredients/mapped/Bovine_Serum_Albumin.yaml"
    template = next(c for c in document["claims"] if c["kind"] == "product")
    decision_template = next(
        d for d in review["decisions"] if d["claim_id"] == template["claim_id"]
    )
    proof_name = decision_template["review_evidence"]
    proof = read_json(sources[proof_name])
    fixture = canonical_json(
        {
            "synthetic_software_fixture": True,
            "products": ["TEST-1", "TEST-2"],
            "shared_cas": "9048-46-8",
        }
    )
    sources["synthetic-products.json"] = fixture
    review["inputs"]["synthetic-products.json"] = content_sha256(fixture)
    evidence = [{"document_id": "urn:sha256:" + content_sha256(fixture), "locator": "/"}]
    identifiers = []
    for catalog in ("TEST-1", "TEST-2"):
        product = copy.deepcopy(template["payload"])
        identifier = product_id("Example Supplier", catalog)
        identifiers.append(identifier)
        product.update(
            product_id=identifier,
            supplier="Example Supplier",
            catalog_number=catalog,
            label=catalog,
            preparation=None,
            source_id="example:synthetic-products",
            source_payload={"synthetic_software_fixture": True, "catalog": catalog},
            evidence=evidence,
        )
        annotation = copy.deepcopy(
            next(
                a for a in compiled[1]["identifiers"] if a["owner_id"] == "MIM:Bovine_Serum_Albumin"
            )
        )
        annotation.update(
            owner_id=identifier,
            source_id="example:synthetic-products",
            source_status="TEST_ASSERTION",
            source_version="test-v1",
            evidence=evidence,
        )
        annotation["annotation_id"] = annotation_id(annotation)
        for kind, payload, key in (
            ("product", product, identifier),
            ("identifier", annotation, annotation["annotation_id"]),
        ):
            claim = {"claim_id": key, "kind": kind, "owner_record": owner, "payload": payload}
            decision = dict(
                decision_template,
                claim_id=key,
                evidence_key=key,
                row_sha256=content_sha256(canonical_json(claim)),
                review_reason="Synthetic software fixture only; retain separate catalog identities despite shared CAS.",
            )
            proof["entries"][key] = {
                k: decision[k]
                for k in ("row_sha256", "owner_record", "disposition", "review_reason")
            }
            proof["entries"][key]["owner_record_sha256"] = review["record_inputs"][owner]
            document["claims"].append(claim)
            review["decisions"].append(decision)
    sources[proof_name] = canonical_json(proof)
    review["inputs"][proof_name] = content_sha256(sources[proof_name])
    sources[review["claims_file"]] = canonical_json(document)
    review["claims_sha256"] = content_sha256(sources[review["claims_file"]])
    artifacts, loaded = reviewed_products(review, sources)
    assert len(loaded["products"]) == 5
    assert len(set(identifiers)) == 2
    assert not set(identifiers) & set(loaded["identities"])
    annotations = read_annotation_table(artifacts[ARTIFACTS["identifiers"]])
    assert [
        (a["owner_id"], a["identifier"])
        for a in sorted(annotations, key=lambda a: a["owner_id"])
        if a["owner_id"] in identifiers
    ] == [(p, "cas:9048-46-8") for p in sorted(identifiers)]
