"""Check semantic scope independently of logical type and identifier namespace."""

from copy import deepcopy

import pytest

from mediaingredientmech.mapping_scope import (
    PROFILE_CURIE,
    PROFILE_ID,
    profile_metadata,
    read_profile_table,
    scope_profile,
    validate_scope_row,
    write_profile_table,
)


def reviewed_row(**overrides):
    """Build a reviewed family alignment with explicit authorization."""
    row = {
        "subject_id": "MIM:Rifamycin",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:26580",
        "ext_subject_scope": "mimscope:chemical_family",
        "ext_object_scope": "mimscope:chemical_family",
        "ext_subject_composition": "mimscope:unknown",
        "ext_object_composition": "mimscope:unknown",
        "ext_scope_review_status": "SUPPORTED",
        "ext_scope_evidence": "https://example.org/review#rifamycin",
        "ext_identity_authorized": "true",
    }
    row.update(overrides)
    return row


def test_exact_mapping_is_application_authorized_and_never_implied_by_scope():
    """Matching scope still needs an explicit supported identity review."""
    metadata = profile_metadata({})
    assert validate_scope_row(reviewed_row(), metadata)
    assert not validate_scope_row(reviewed_row(ext_identity_authorized="false"), metadata)
    assert not validate_scope_row(
        reviewed_row(
            predicate_id="skos:broadMatch",
            ext_identity_authorized="false",
            ext_subject_scope="mimscope:defined_substance",
        ),
        metadata,
    )


@pytest.mark.parametrize(
    "updates",
    [
        {"predicate_modifier": "Not"},
        {"ext_object_scope": "mimscope:defined_substance"},
        {"ext_subject_scope": "mimscope:unknown", "ext_object_scope": "mimscope:unknown"},
        {"ext_scope_review_status": "WITHHOLD"},
        {"ext_scope_review_status": "UNREVIEWED"},
        {"predicate_id": "skos:broadMatch"},
        {"predicate_id": "skos:closeMatch"},
        {"ext_scope_evidence": ""},
        {"ext_scope_evidence": "undeclared:review"},
        {"ext_identity_authorized": "yes"},
        {"ext_subject_composition": "mimscope:mixture"},
        {"ext_subject_scope": "owl:Class"},
    ],
)
def test_identity_overclaims_are_rejected(updates):
    """Type/category, confidence and CAS namespaces cannot bypass review."""
    with pytest.raises(ValueError):
        validate_scope_row(reviewed_row(**updates), profile_metadata({}))


def test_registry_namespace_does_not_choose_scope():
    """A reviewed CAS/material equivalence follows the same scope rule as other IDs."""
    row = reviewed_row(
        subject_id="cas:1404-26-8",
        object_id="NCIT:C61894",
        ext_subject_scope="mimscope:material",
        ext_object_scope="mimscope:material",
        ext_subject_composition="mimscope:mixture",
        ext_object_composition="mimscope:mixture",
    )
    assert validate_scope_row(row, profile_metadata({}))


def test_unknown_scope_is_representable_without_canonicalization():
    """Unreviewed local material records can remain explicit without inventing identity."""
    row = reviewed_row(
        ext_subject_scope="mimscope:unknown",
        ext_object_scope="mimscope:unknown",
        ext_scope_review_status="UNREVIEWED",
        ext_scope_evidence="",
        ext_identity_authorized="false",
    )
    assert not validate_scope_row(row, profile_metadata({}))


def test_legacy_and_mixed_release_require_explicit_profile_selection():
    """Legacy rows cannot acquire scoped behavior from undeclared extension values."""
    assert validate_scope_row({"subject_id": "legacy:one"}, {}) is None
    with pytest.raises(ValueError, match="require a declared"):
        validate_scope_row(reviewed_row(), {})
    mixed = profile_metadata({}, default_profile=False)
    assert validate_scope_row({"subject_id": "legacy:one"}, mixed) is None
    assert validate_scope_row(reviewed_row(ext_scope_profile=PROFILE_ID), mixed)
    with pytest.raises(ValueError, match="Unsupported ingredient scope profile"):
        validate_scope_row(reviewed_row(), {"ext_scope_profile": PROFILE_ID + "-future"})


def test_definitions_and_curie_expansion_round_trip():
    """The declared standard extension shape expands the same compact and full IRIs."""
    metadata = profile_metadata({})
    assert profile_metadata(metadata) == metadata
    expanded = reviewed_row()
    for field in ("ext_subject_scope", "ext_object_scope"):
        expanded[field] = "https://w3id.org/mediaingredientmech/scope/chemical_family"
    assert validate_scope_row(expanded, metadata)
    assert validate_scope_row(reviewed_row(ext_scope_profile=PROFILE_ID), metadata)
    assert validate_scope_row(reviewed_row(ext_scope_profile=PROFILE_CURIE), metadata)
    full_default = deepcopy(metadata)
    full_default["ext_scope_profile"] = PROFILE_ID
    assert validate_scope_row(reviewed_row(ext_scope_profile=PROFILE_CURIE), full_default)
    conflicting = deepcopy(metadata)
    conflicting["extension_definitions"][1]["property"] = "https://example.org/wrong"
    with pytest.raises(ValueError, match="Conflicting scope extension"):
        validate_scope_row(reviewed_row(), conflicting)
    missing = deepcopy(metadata)
    missing["extension_definitions"].pop()
    with pytest.raises(ValueError, match="definitions are missing"):
        validate_scope_row(reviewed_row(), missing)
    with pytest.raises(ValueError, match="Conflicting scope profile prefix"):
        profile_metadata({"curie_map": {"mimscope": "https://example.org/wrong/"}})
    duplicate = deepcopy(metadata)
    duplicate["extension_definitions"].append(
        {"slot_name": "ext_duplicate", "property": "mimprofile:subjectScope"}
    )
    with pytest.raises(ValueError, match="Duplicate SSSOM extension property"):
        profile_metadata(duplicate)
    copy = scope_profile()
    copy["scope_values"].clear()
    assert scope_profile()["scope_values"]


def serialization_example():
    """Provide a scope example with declared core and evidence CURIEs."""
    metadata = profile_metadata(
        {
            "mapping_set_id": "https://example.org/test-scope",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "curie_map": {
                "MIM": "https://w3id.org/mediaingredientmech/ingredient/",
                "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
                "skos": "http://www.w3.org/2004/02/skos/core#",
                "semapv": "https://w3id.org/semapv/vocab/",
                "review": "https://example.org/review#",
            },
        }
    )
    row = reviewed_row(mapping_justification="semapv:ManualMappingCuration")
    return metadata, list(row), [row]


def test_serialization_preserves_every_extension_and_multiline_comment():
    """Read/write retains tuples and quoted lines beginning with a metadata marker."""
    metadata, fields, rows = serialization_example()
    fields.append("comment")
    rows[0]["comment"] = "source note\n# this is part of the value"
    payload = write_profile_table(metadata, fields, rows)
    restored_meta, restored_fields, restored_rows = read_profile_table(payload)
    assert restored_fields == fields
    assert restored_rows[0]["comment"] == rows[0]["comment"]
    assert restored_rows[0]["ext_scope_evidence"] == "review:rifamycin"
    assert validate_scope_row(restored_rows[0], restored_meta)
    assert write_profile_table(restored_meta, restored_fields, restored_rows) == payload


def test_profile_reader_rejects_extension_loss_in_an_intermediate_converter():
    """An exactMatch without its profile cannot fall back to legacy authorization."""
    legacy = (
        b"# mapping_set_id: https://example.org/stripped\n"
        b"# license: https://creativecommons.org/publicdomain/zero/1.0/\n"
        b"subject_id\tpredicate_id\tobject_id\tmapping_justification\n"
        b"MIM:Rifamycin\tskos:exactMatch\tCHEBI:26580\tsemapv:ManualMappingCuration\n"
    )
    with pytest.raises(ValueError, match="Required scope profile lost"):
        read_profile_table(legacy)


def test_duplicate_profile_metadata_is_rejected():
    """A second metadata key cannot replace a profile or prefix map."""
    metadata, fields, rows = serialization_example()
    payload = write_profile_table(metadata, fields, rows)
    with pytest.raises(ValueError, match="Duplicate SSSOM metadata key"):
        read_profile_table(b"# ext_scope_profile: mimprofile:ingredient-scope/v2\n" + payload)


@pytest.mark.parametrize(
    "subject,target,scope,composition,authorized",
    [
        ("MIM:Rifamycin", "CHEBI:26580", "chemical_family", "unknown", True),
        ("MIM:Rifamycin_Sv", "CHEBI:29673", "defined_substance", "single_component", True),
        ("MIM:Xanthine", "CHEBI:17712", "defined_substance", "single_component", True),
        ("CHEBI:15318", "CHEBI:15318", "chemical_family", "unknown", True),
        ("MIM:Bovine_Serum_Albumin", "NCIT:C85253", "material", "unknown", True),
        ("MIM:Lysozyme", "kgmicrobe.ingredient:lysozyme", "unknown", "unknown", False),
        (
            "MIM:Sorbitan_Monooleate",
            "kgmicrobe.ingredient:sorbitan_monooleate",
            "material",
            "unknown",
            True,
        ),
    ],
)
def test_reviewed_case_scopes_round_trip(subject, target, scope, composition, authorized):
    """Keep reviewed source concepts distinct without requiring a molecular identity."""
    metadata, _, _ = serialization_example()
    metadata["curie_map"].update(
        NCIT="http://purl.obolibrary.org/obo/NCIT_",
        **{"kgmicrobe.ingredient": "https://w3id.org/kg-microbe/ingredient/"},
    )
    row = reviewed_row(
        subject_id=subject,
        object_id=target,
        ext_subject_scope=f"mimscope:{scope}",
        ext_object_scope=f"mimscope:{scope}",
        ext_subject_composition=f"mimscope:{composition}",
        ext_object_composition=f"mimscope:{composition}",
        ext_identity_authorized=str(authorized).lower(),
        mapping_justification="semapv:ManualMappingCuration",
    )
    restored_meta, _, restored = read_profile_table(write_profile_table(metadata, list(row), [row]))
    assert validate_scope_row(restored[0], restored_meta) is authorized
    assert restored[0]["subject_id"] == subject
    assert restored[0]["object_id"] == target
