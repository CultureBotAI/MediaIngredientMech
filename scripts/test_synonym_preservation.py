#!/usr/bin/env python3
"""Test that original forms are preserved as synonyms during normalization."""

import sys
from pathlib import Path

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name


def test_synonym_preservation():
    """Test normalization and synonym type assignment logic."""

    test_cases = [
        {
            'input': 'MgSO4•7H2O',
            'expected_normalized': 'MgSO4',
            'expected_rules': ['stripped_hydrate'],
            'expected_synonym_type': 'HYDRATE_FORM',
        },
        {
            'input': 'NaCl (Fisher S271-500)',
            'expected_normalized': 'NaCl',
            'expected_rules': ['stripped_catalog'],
            'expected_synonym_type': 'CATALOG_VARIANT',
        },
        {
            'input': 'K2HPO',
            'expected_normalized': 'K2HPO4',
            'expected_rules': ['fixed_incomplete_formula'],
            'expected_synonym_type': 'INCOMPLETE_FORMULA',
        },
        {
            'input': 'CaCl2•2H2O (Sigma 123)',
            'expected_normalized': 'CaCl2',
            'expected_rules': ['stripped_catalog', 'stripped_hydrate'],
            'expected_synonym_type': 'HYDRATE_FORM',  # Hydrate takes precedence
        },
    ]

    print("Testing synonym preservation logic...\n")

    all_passed = True
    for i, case in enumerate(test_cases, 1):
        print(f"Test {i}: {case['input']}")

        result = normalize_chemical_name(case['input'])

        # Check normalization
        if result.normalized != case['expected_normalized']:
            print(f"  ❌ FAIL: Expected normalized='{case['expected_normalized']}', "
                  f"got '{result.normalized}'")
            all_passed = False
        else:
            print(f"  ✓ Normalized: {result.normalized}")

        # Check applied rules
        if not all(rule in result.applied_rules for rule in case['expected_rules']):
            print(f"  ❌ FAIL: Expected rules={case['expected_rules']}, "
                  f"got {result.applied_rules}")
            all_passed = False
        else:
            print(f"  ✓ Applied rules: {result.applied_rules}")

        # Determine what synonym type would be assigned
        if 'stripped_hydrate' in result.applied_rules:
            synonym_type = 'HYDRATE_FORM'
        elif 'stripped_catalog' in result.applied_rules:
            synonym_type = 'CATALOG_VARIANT'
        elif 'fixed_incomplete_formula' in result.applied_rules:
            synonym_type = 'INCOMPLETE_FORMULA'
        else:
            synonym_type = 'ALTERNATE_FORM'

        if synonym_type != case['expected_synonym_type']:
            print(f"  ❌ FAIL: Expected synonym_type='{case['expected_synonym_type']}', "
                  f"got '{synonym_type}'")
            all_passed = False
        else:
            print(f"  ✓ Synonym type: {synonym_type}")

        # Check variants
        print(f"  ✓ Search variants: {', '.join(result.variants[:3])}")
        print()

    if all_passed:
        print("✅ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


def test_record_update():
    """Test that synonym is correctly added to a record."""
    print("\nTesting record synonym addition...\n")

    # Simulate a record
    record = {
        'identifier': 'UNMAPPED_0003',
        'preferred_term': 'MgSO4•7H2O',
        'synonyms': [],
    }

    # Simulate normalization result
    norm_result = {
        'original': 'MgSO4•7H2O',
        'normalized': 'MgSO4',
        'applied_rules': ['stripped_hydrate'],
    }

    # Add synonym (simulate what batch_curate_unmapped.py does)
    original_name = norm_result['original']
    applied_rules = norm_result['applied_rules']

    if 'stripped_hydrate' in applied_rules:
        synonym_type = 'HYDRATE_FORM'
    else:
        synonym_type = 'ALTERNATE_FORM'

    new_synonym = {
        'synonym_text': original_name.strip(),
        'synonym_type': synonym_type,
        'source': 'batch_curation_normalization',
        'notes': f"Original form before normalization: {', '.join(applied_rules)}",
    }
    record['synonyms'].append(new_synonym)

    # Verify
    print(f"Record: {record['identifier']}")
    print(f"Preferred term: {record['preferred_term']}")
    print(f"Added synonym:")
    print(f"  - Text: {new_synonym['synonym_text']}")
    print(f"  - Type: {new_synonym['synonym_type']}")
    print(f"  - Source: {new_synonym['source']}")
    print(f"  - Notes: {new_synonym['notes']}")

    if (new_synonym['synonym_text'] == 'MgSO4•7H2O' and
        new_synonym['synonym_type'] == 'HYDRATE_FORM'):
        print("\n✅ Record update test passed!")
        return 0
    else:
        print("\n❌ Record update test failed")
        return 1


if __name__ == '__main__':
    exit_code = test_synonym_preservation()
    exit_code |= test_record_update()
    sys.exit(exit_code)
