"""Numeric prefix aliases cannot impersonate a second registered owner (#1276)."""

import pytest

from mediaingredientmech.stable_ids import (
    Mint,
    Registry,
    StableIdError,
    build_record_index,
    validate_records,
)


def validated_index(alias):
    registry = Registry(
        tuple(Mint(f"MIM:{number:07d}", f"Owner {number}", "2026-11-08") for number in (1, 2))
    )
    records = {
        "owner1.yaml": {
            "mim_id": "MIM:0000001",
            "preferred_term": "Owner 1",
            "legacy_identifiers": [alias, "mim:Old_text"],
        },
        "owner2.yaml": {"mim_id": "MIM:0000002", "preferred_term": "Owner 2"},
    }
    from mediaingredientmech.validation.write_validated import validate_ingredient

    for number, record in enumerate(records.values(), start=1):
        record.update(identifier=f"UNMAPPED_{number:04d}", mapping_status="UNMAPPED")
        assert validate_ingredient(record) == []
    validate_records(registry, records)
    index = build_record_index(records)
    assert index.aliases[alias] == ("owner1.yaml",), "Preserve original alias bytes"
    assert index.lookup("mim:Old_text") == "owner1.yaml"
    return index


@pytest.mark.parametrize("prefix", ["MIM", "mim", "MiM"])
def test_numeric_reference_uses_registered_owner_before_conflicting_alias(prefix):
    reference = f"{prefix}:0000002"
    index = validated_index(reference)
    assert index.lookup("MIM:0000002") == "owner2.yaml"
    assert index.lookup(reference) == "owner2.yaml"


@pytest.mark.parametrize("prefix", ["MIM", "mim", "MiM"])
@pytest.mark.parametrize(
    "local", ["12", "0000000", "0000003", "00000001", "٠٠٠٠٠٠١", "００００００１"]
)
def test_invalid_or_unknown_numeric_reference_never_uses_preserved_alias(prefix, local):
    reference = f"{prefix}:{local}"
    index = validated_index(reference)
    with pytest.raises(StableIdError):
        index.lookup(reference)


@pytest.mark.parametrize("reference", [" MIM:0000002 ", " mim:0000002 "])
def test_numeric_reference_padding_cannot_redirect_registered_owner(reference):
    assert validated_index(reference).lookup(reference) == "owner2.yaml"


@pytest.mark.parametrize("reference", [" MiM:12 ", " MIM:٠٠٠٠٠٠١ "])
def test_padded_malformed_numeric_alias_still_refuses(reference):
    with pytest.raises(StableIdError):
        validated_index(reference).lookup(reference)
