"""Test role assignment methods in IngredientCurator."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def test_add_media_role():
    """Test adding a media role with DOI citation."""
    curator = IngredientCurator(curator_name="test_curator")

    # Create a test record
    record = {
        "ontology_id": "TEST:001",
        "preferred_term": "potassium nitrate",
        "mapping_status": "UNMAPPED",
    }

    # Test valid role addition with DOI
    result = curator.add_media_role(
        record,
        role="NITROGEN_SOURCE",
        confidence=0.95,
        doi="10.1128/jb.00123-15",
        reference_text="Smith et al. (2015) J. Bacteriol.",
        reference_type="PEER_REVIEWED_PUBLICATION",
        curator_note="Primary nitrogen source in defined medium",
        notes="Well-documented role",
    )

    assert "media_roles" in result
    assert len(result["media_roles"]) == 1
    role_assignment = result["media_roles"][0]
    assert role_assignment["role"] == "NITROGEN_SOURCE"
    assert role_assignment["confidence"] == 0.95
    assert role_assignment["notes"] == "Well-documented role"
    assert len(role_assignment["evidence"]) == 1

    evidence = role_assignment["evidence"][0]
    assert evidence["doi"] == "10.1128/jb.00123-15"
    assert evidence["reference_text"] == "Smith et al. (2015) J. Bacteriol."
    assert evidence["reference_type"] == "PEER_REVIEWED_PUBLICATION"
    assert evidence["curator_note"] == "Primary nitrogen source in defined medium"

    # Check curation history
    assert "curation_history" in result
    assert len(result["curation_history"]) == 1
    assert "NITROGEN_SOURCE" in result["curation_history"][0]["changes"]
    assert "10.1128/jb.00123-15" in result["curation_history"][0]["changes"]

    print("✓ test_add_media_role passed")


def test_add_media_role_without_citation():
    """Test adding a media role without citation."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:002",
        "preferred_term": "sodium chloride",
        "mapping_status": "UNMAPPED",
    }

    result = curator.add_media_role(
        record,
        role="SALT",
        confidence=1.0,
        notes="Standard salt component",
    )

    assert len(result["media_roles"]) == 1
    role_assignment = result["media_roles"][0]
    assert role_assignment["role"] == "SALT"
    assert role_assignment["confidence"] == 1.0
    assert role_assignment["evidence"] == []  # No citation provided

    print("✓ test_add_media_role_without_citation passed")


def test_add_community_organism_role():
    """Test adding a community-organism role with metabolic context."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:003",
        "preferred_term": "toluene",
        "mapping_status": "MAPPED",
    }

    result = curator.add_community_organism_role(
        record,
        role="PRIMARY_DEGRADER",
        metabolic_context="aromatic hydrocarbon degradation",
        confidence=0.9,
        doi="10.1038/nature12345",
        reference_type="PEER_REVIEWED_PUBLICATION",
        curator_note="Primary organism degrading toluene in consortium",
    )

    assert "community_organism_roles" in result
    assert len(result["community_organism_roles"]) == 1
    role_assignment = result["community_organism_roles"][0]
    assert role_assignment["role"] == "PRIMARY_DEGRADER"
    assert role_assignment["metabolic_context"] == "aromatic hydrocarbon degradation"
    assert role_assignment["confidence"] == 0.9
    assert len(role_assignment["evidence"]) == 1
    assert role_assignment["evidence"][0]["doi"] == "10.1038/nature12345"

    assert "aromatic hydrocarbon degradation" in result["curation_history"][0]["changes"]

    print("✓ test_add_community_organism_role passed")


def test_set_solution_type():
    """Test setting solution type."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:004",
        "preferred_term": "vitamin B12 solution",
        "mapping_status": "UNMAPPED",
    }

    result = curator.set_solution_type(record, "VITAMIN_MIX")

    assert result["solution_type"] == "VITAMIN_MIX"
    assert "solution type: VITAMIN_MIX" in result["curation_history"][0]["changes"]

    print("✓ test_set_solution_type passed")


def test_validation_invalid_role():
    """Test validation rejects invalid role."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:005",
        "preferred_term": "test",
        "mapping_status": "UNMAPPED",
    }

    try:
        curator.add_media_role(record, role="INVALID_ROLE")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Invalid media role" in str(e)

    print("✓ test_validation_invalid_role passed")


def test_validation_invalid_doi():
    """Test validation rejects invalid DOI format."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:006",
        "preferred_term": "test",
        "mapping_status": "UNMAPPED",
    }

    try:
        curator.add_media_role(record, role="BUFFER", doi="not-a-valid-doi")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Invalid DOI" in str(e)

    print("✓ test_validation_invalid_doi passed")


def test_validation_invalid_confidence():
    """Test validation rejects confidence out of range."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:007",
        "preferred_term": "test",
        "mapping_status": "UNMAPPED",
    }

    try:
        curator.add_media_role(record, role="BUFFER", confidence=1.5)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Confidence out of range" in str(e)

    print("✓ test_validation_invalid_confidence passed")


def test_validate_role_assignments():
    """Test validate_role_assignments method."""
    curator = IngredientCurator(curator_name="test_curator")

    # Valid record
    valid_record = {
        "ontology_id": "TEST:008",
        "preferred_term": "test",
        "media_roles": [
            {
                "role": "NITROGEN_SOURCE",
                "confidence": 0.9,
                "evidence": [
                    {
                        "doi": "10.1128/jb.00123-15",
                        "reference_type": "PEER_REVIEWED_PUBLICATION",
                    }
                ],
            }
        ],
        "solution_type": "VITAMIN_MIX",
    }

    errors = curator.validate_role_assignments(valid_record)
    assert len(errors) == 0, f"Expected no errors, got: {errors}"

    # Invalid record - bad role
    invalid_record = {
        "ontology_id": "TEST:009",
        "preferred_term": "test",
        "media_roles": [
            {
                "role": "INVALID_ROLE",
                "confidence": 0.9,
            }
        ],
    }

    errors = curator.validate_role_assignments(invalid_record)
    assert len(errors) == 1
    assert "Invalid media role" in errors[0]

    # Invalid record - bad DOI
    invalid_doi_record = {
        "ontology_id": "TEST:010",
        "preferred_term": "test",
        "media_roles": [
            {
                "role": "BUFFER",
                "evidence": [{"doi": "not-a-doi"}],
            }
        ],
    }

    errors = curator.validate_role_assignments(invalid_doi_record)
    assert len(errors) == 1
    assert "Invalid DOI" in errors[0]

    # Invalid record - bad solution type
    invalid_solution_record = {
        "ontology_id": "TEST:011",
        "preferred_term": "test",
        "solution_type": "INVALID_TYPE",
    }

    errors = curator.validate_role_assignments(invalid_solution_record)
    assert len(errors) == 1
    assert "Invalid solution type" in errors[0]

    print("✓ test_validate_role_assignments passed")


def test_multiple_roles():
    """Test adding multiple roles to the same ingredient."""
    curator = IngredientCurator(curator_name="test_curator")

    record = {
        "ontology_id": "TEST:012",
        "preferred_term": "potassium nitrate",
        "mapping_status": "MAPPED",
    }

    # Add nitrogen source role
    curator.add_media_role(record, role="NITROGEN_SOURCE", confidence=0.95)

    # Add electron acceptor role
    curator.add_media_role(record, role="ELECTRON_ACCEPTOR", confidence=0.9)

    assert len(record["media_roles"]) == 2
    roles = [r["role"] for r in record["media_roles"]]
    assert "NITROGEN_SOURCE" in roles
    assert "ELECTRON_ACCEPTOR" in roles

    print("✓ test_multiple_roles passed")


def test_add_nutritional_role():
    """Test adding a nutritional-facet role."""
    curator = IngredientCurator(curator_name="test_curator")
    record = {
        "ontology_id": "CHEBI:17561",
        "preferred_term": "L-cysteine",
        "mapping_status": "MAPPED",
    }

    result = curator.add_nutritional_role(
        record,
        role="AMINO_ACID_SOURCE",
        confidence=0.98,
        doi="10.1128/jb.00456-20",
        reference_type="PEER_REVIEWED_PUBLICATION",
        curator_note="L-cysteine supplies cysteine + sulfur simultaneously in defined media.",
        notes="Round-trip check for notes preservation.",
    )

    assert "nutritional_roles" in result
    assert len(result["nutritional_roles"]) == 1
    assignment = result["nutritional_roles"][0]
    assert assignment["role"] == "AMINO_ACID_SOURCE"
    assert assignment["confidence"] == 0.98
    assert assignment["notes"] == "Round-trip check for notes preservation."
    assert len(assignment["evidence"]) == 1
    assert assignment["evidence"][0]["doi"] == "10.1128/jb.00456-20"

    curator.add_nutritional_role(record, role="SULFUR_SOURCE", confidence=0.9)
    assert len(result["nutritional_roles"]) == 2
    assert result["nutritional_roles"][1]["role"] == "SULFUR_SOURCE"
    # No-citation branch must NOT leak a phantom empty citation.
    assert result["nutritional_roles"][1]["evidence"] == []

    print("✓ test_add_nutritional_role passed")


def test_add_physicochemical_role():
    """Test adding a physicochemical-facet role.

    Includes the no-citation branch (no doi/pmid/reference_text/url provided) —
    `evidence` must be an empty list. Note: passing `curator_note`/`excerpt`
    alone does not trigger citation creation (inherited from add_media_role);
    a real citation needs at least one of doi/pmid/reference_text/url.
    """
    curator = IngredientCurator(curator_name="test_curator")
    record = {
        "ontology_id": "CHEBI:64755",
        "preferred_term": "EDTA(2-)",
        "mapping_status": "MAPPED",
    }

    result = curator.add_physicochemical_role(
        record,
        role="CHELATOR",
        confidence=0.99,
        notes="Round-trip check for notes preservation.",
    )

    assert "physicochemical_roles" in result
    assert len(result["physicochemical_roles"]) == 1
    assignment = result["physicochemical_roles"][0]
    assert assignment["role"] == "CHELATOR"
    assert assignment["confidence"] == 0.99
    assert assignment["notes"] == "Round-trip check for notes preservation."
    # No-citation branch must NOT leak a phantom empty citation.
    assert assignment["evidence"] == []

    # Second call WITH a DOI must attach a citation.
    curator.add_physicochemical_role(
        record,
        role="SURFACTANT",
        confidence=0.9,
        doi="10.1128/aem.02345-19",
        reference_type="PEER_REVIEWED_PUBLICATION",
    )
    assert len(result["physicochemical_roles"]) == 2
    assert len(result["physicochemical_roles"][1]["evidence"]) == 1
    assert result["physicochemical_roles"][1]["evidence"][0]["doi"] == "10.1128/aem.02345-19"

    print("✓ test_add_physicochemical_role passed")


def test_add_cellular_metabolic_role():
    """Test adding a cellular-metabolic-facet role with metabolic_context."""
    curator = IngredientCurator(curator_name="test_curator")
    record = {
        "ontology_id": "CHEBI:17790",
        "preferred_term": "methanol",
        "mapping_status": "MAPPED",
    }

    result = curator.add_cellular_metabolic_role(
        record,
        role="ELECTRON_DONOR",
        metabolic_context="methylotrophs only",
        confidence=0.95,
        doi="10.1128/mmbr.00012-16",
        reference_type="PEER_REVIEWED_PUBLICATION",
        curator_note="Methanol is the electron donor for MDH in methylotrophic C1 metabolism.",
        notes="Round-trip check for notes preservation.",
    )

    assert "cellular_metabolic_roles" in result
    assert len(result["cellular_metabolic_roles"]) == 1
    assignment = result["cellular_metabolic_roles"][0]
    assert assignment["role"] == "ELECTRON_DONOR"
    assert assignment["metabolic_context"] == "methylotrophs only"
    assert assignment["confidence"] == 0.95
    assert assignment["notes"] == "Round-trip check for notes preservation."
    assert len(assignment["evidence"]) == 1
    assert assignment["evidence"][0]["doi"] == "10.1128/mmbr.00012-16"

    assert "methylotrophs only" in result["curation_history"][0]["changes"]

    # No-citation, no-metabolic_context branch: evidence == [] and no metabolic_context key.
    curator.add_cellular_metabolic_role(record, role="SUBSTRATE", confidence=0.9)
    assert len(result["cellular_metabolic_roles"]) == 2
    second = result["cellular_metabolic_roles"][1]
    assert second["evidence"] == []
    assert "metabolic_context" not in second

    print("✓ test_add_cellular_metabolic_role passed")


def test_facet_role_validation_rejects_wrong_facet_value():
    """A physicochemical role token must not be accepted as a nutritional role."""
    import pytest

    curator = IngredientCurator(curator_name="test_curator")
    record = {"ontology_id": "TEST:900", "preferred_term": "x", "mapping_status": "MAPPED"}

    with pytest.raises(ValueError, match="Invalid nutritional role"):
        curator.add_nutritional_role(record, role="BUFFER")  # BUFFER is physicochemical, not nutritional

    with pytest.raises(ValueError, match="Invalid physicochemical role"):
        curator.add_physicochemical_role(record, role="CARBON_SOURCE")  # nutritional, not physicochemical

    with pytest.raises(ValueError, match="Invalid cellular-metabolic role"):
        curator.add_cellular_metabolic_role(record, role="BUFFER")  # not cellular-metabolic

    print("✓ test_facet_role_validation_rejects_wrong_facet_value passed")


def test_validate_role_assignments_walks_new_facet_slots():
    """validate_role_assignments should detect invalid values in the three new facet slots."""
    curator = IngredientCurator(curator_name="test_curator")
    record = {
        "ontology_id": "TEST:901",
        "preferred_term": "y",
        "mapping_status": "MAPPED",
        "nutritional_roles": [{"role": "NOT_A_REAL_ROLE", "confidence": 0.5}],
        "physicochemical_roles": [{"role": "BUFFER", "confidence": 2.5}],  # out-of-range confidence
        "cellular_metabolic_roles": [
            {"role": "SUBSTRATE", "evidence": [{"doi": "not-a-doi"}]}
        ],
    }

    errors = curator.validate_role_assignments(record)
    joined = " | ".join(errors)
    assert "Invalid nutritional role at index 0: NOT_A_REAL_ROLE" in joined
    assert "Confidence out of range at physicochemical role 0" in joined
    assert "Invalid DOI format at cellular-metabolic role 0" in joined

    print("✓ test_validate_role_assignments_walks_new_facet_slots passed")


if __name__ == "__main__":
    test_add_media_role()
    test_add_media_role_without_citation()
    test_add_community_organism_role()
    test_add_nutritional_role()
    test_add_physicochemical_role()
    test_add_cellular_metabolic_role()
    test_facet_role_validation_rejects_wrong_facet_value()
    test_validate_role_assignments_walks_new_facet_slots()
    test_set_solution_type()
    test_validation_invalid_role()
    test_validation_invalid_doi()
    test_validation_invalid_confidence()
    test_validate_role_assignments()
    test_multiple_roles()

    print("\n✅ All tests passed!")
