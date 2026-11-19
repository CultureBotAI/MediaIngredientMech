"""#1265 portable inherited cohort: source proof, exclusions and capability gate."""
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import identity_projection as ip
from mediaingredientmech import identity_projection_bundle as bundle
from mediaingredientmech.ingredient_bundle_contract import reviewed_products

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def inputs():
    review = ip.document((ROOT / bundle.REVIEW).read_bytes())
    return review, {name: (ROOT / name).read_bytes() for name in bundle.declared_sources(review)}


def test_portable_projection_preserves_every_nonidentity_field(inputs):
    review, sources = inputs
    _, current = reviewed_products(review, sources)
    original = ip.document(sources[bundle.ARCHIVE + bundle.OLD_REVIEW])
    old_sources = {name: sources[bundle.ARCHIVE + name] for name in bundle.declared_sources(original)}
    _, old = reviewed_products(original, old_sources)
    aliases = {key: yaml.safe_load(sources[owner])["mim_id"] for key, owner in old["owners"].items()}
    assert current["owners"] == {aliases[key]: value for key, value in old["owners"].items()}
    assert len(current["mappings"]) == len(old["mappings"]) == 20
    for group, address in (("identifiers", "owner_id"), ("products", "ingredient_id"), ("occurrences", "ingredient_id")):
        assert len(current[group]) == len(old[group])
        for before, after in zip(old[group], current[group], strict=True):
            expected = deepcopy(before)
            expected[address] = aliases.get(expected[address], expected[address])
            if group == "identifiers":
                from mediaingredientmech.ingredient_bundle_contract import annotation_id
                if before[address] in aliases:
                    expected["annotation_id"] = annotation_id(expected)
            assert ip.exact(after, expected)
    # This corpus includes historical/invalid/ineligible registry claims. Their
    # exact payloads above must remain so; this is not a fixture with all approval.
    assert any(not row["xref_eligible"] for row in current["identifiers"])
    assert any(row["source_currentness"] == "HISTORICAL" for row in current["identifiers"])


@pytest.mark.parametrize("attack", ["scientific_field", "history", "authority", "original_review"])
def test_rehashed_portable_projection_cannot_refresh_science(inputs, attack):
    review, sources = deepcopy(inputs)
    owner = next(iter(review["record_inputs"]))
    if attack in {"scientific_field", "history"}:
        record = yaml.safe_load(sources[owner])
        if attack == "scientific_field":
            record["preferred_term"] += " revised science"
        else:
            record["curation_history"][0]["changes"] = "rewritten"
        sources[owner] = yaml.safe_dump(record).encode()
        review["record_inputs"][owner] = ip.sha(sources[owner])
        manifest = ip.document(sources[ip.MANIFEST])
        next(entry for entry in manifest["records"] if entry["path"] == owner)["after_sha256"] = ip.sha(sources[owner])
        sources[ip.MANIFEST] = ip.encode(manifest)
        review["inputs"][ip.MANIFEST] = ip.sha(sources[ip.MANIFEST])
        review["identity_projection"]["manifest_sha256"] = ip.sha(sources[ip.MANIFEST])
    elif attack == "authority":
        review["identity_projection"]["scientific_approval_added"] = True
    else:
        name = bundle.ARCHIVE + bundle.OLD_REVIEW
        original = ip.document(sources[name])
        original["decisions"][0]["review_reason"] = "new scientific decision"
        sources[name] = ip.encode(original)
        review["inputs"][name] = ip.sha(sources[name])
    with pytest.raises(ValueError, match="Identity projection"):
        reviewed_products(review, sources)


def test_native_companion_owner_uses_current_id_but_archive_keeps_legacy_address():
    from mediaingredientmech.ingredient_bundle_contract import _owner_id
    owner = "data/ingredients/mapped/New_Label.yaml"
    assert _owner_id(owner, {"mim_id": "MIM:0000007"}) == "MIM:0000007"
    assert _owner_id(owner, {"identifier": "CHEBI:7"}) == "MIM:New_Label"
    with pytest.raises(ValueError):
        _owner_id(owner, {"mim_id": "MIM:arbitrary"})


def test_coherently_shifted_complete_mint_inventory_is_not_portable_authority(inputs):
    """#1269: all attacker-controlled hashes agree, but fixed Git mint order must win."""
    from dataclasses import replace
    from mediaingredientmech.stable_ids import Mint, Registry, dump_registry, parse_registry
    review, sources = deepcopy(inputs)
    manifest = ip.document(sources[ip.MANIFEST])
    registry = parse_registry(sources[ip.REGISTRY], sources[ip.LIFECYCLE])
    shifted = Registry((Mint("MIM:0000001", "Fabricated inventory insertion", manifest["minted_on"]),
                        *(replace(mint, mim_id=f"MIM:{index+1:07d}") for index, mint in enumerate(registry.entries, 1))), registry.events)
    for index, entry in enumerate(manifest["records"], 2):
        entry["mim_id"] = f"MIM:{index:07d}"
        owner = entry["path"]
        if owner in review["record_inputs"]:
            record = yaml.safe_load(sources[owner])
            record["mim_id"] = entry["mim_id"]
            record["curation_history"][-1]["changes"] = f"#1265: assigned permanent {entry['mim_id']}; retained mapping identifier and legacy aliases."
            sources[owner] = yaml.safe_dump(record, sort_keys=False).encode()
            entry["after_sha256"] = review["record_inputs"][owner] = ip.sha(sources[owner])
    manifest["records"].insert(0, {"path": "data/ingredients/mapped/!Fabricated.yaml", "mim_id": "MIM:0000001",
                                  "legacy_identifiers": ["MIM:!Fabricated"], "before_sha256": "0"*64, "after_sha256": "0"*64})
    sources[ip.REGISTRY] = dump_registry(shifted)
    manifest["registry_sha256"] = review["inputs"][ip.REGISTRY] = ip.sha(sources[ip.REGISTRY])
    sources[ip.MANIFEST] = ip.encode(manifest)
    review["inputs"][ip.MANIFEST] = review["identity_projection"]["manifest_sha256"] = ip.sha(sources[ip.MANIFEST])
    base = ip.document(sources[ip.MAPPING_REVIEW])
    base["identity_projection"]["manifest_sha256"] = ip.sha(sources[ip.MANIFEST])
    sources[ip.MAPPING_REVIEW] = ip.encode(base)
    review["base_review_sha256"] = review["inputs"][ip.MAPPING_REVIEW] = ip.sha(sources[ip.MAPPING_REVIEW])
    with pytest.raises(ValueError, match="complete baseline mint inventory differs"):
        reviewed_products(review, sources)
