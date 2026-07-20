#!/usr/bin/env python3
"""
Build water variant hierarchy as proof of concept.

Creates parent "Water (base)" record and links all water purity variants:
- Tap water (variant_type: TAP)
- Demineralized water (variant_type: DEMINERALIZED)
- Distilled water (variant_type: PURIFIED)
- Double distilled water (variant_type: ULTRA_PURIFIED)

Run with: PYTHONPATH=src python scripts/build_water_hierarchy.py

NOT CURRENTLY RUNNABLE. This one-shot predates two schema changes and would fail
validation as written:

* it mints `id: MediaIngredientMech:NNNNNN` values, but that dual-identifier
  scheme was rolled back — records are keyed by `identifier` alone;
* it writes `media_roles` with `role: SOLVENT`. The `media_roles` slot was
  retired in #128, and SOLVENT was never a permissible value of any role enum.

Left in place for its hierarchy-linking logic. Before running it again, rewrite
the record scaffolding against the current schema and pick a real role value
from one of the three facet enums (see utils/role_facets.py).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.hierarchy_validator import (
    validate_hierarchy,
    validate_all_hierarchies,
    get_hierarchy_statistics,
)


# Water variant IDs (from curation)
WATER_VARIANTS = {
    'tap': 'MediaIngredientMech:000260',
    'demineralized': 'MediaIngredientMech:000472',
    'distilled': 'MediaIngredientMech:000114',
    'double_distilled': 'MediaIngredientMech:000268',
}

# New parent ID
PARENT_ID = 'MediaIngredientMech:001108'


def create_parent_record() -> dict:
    """Create Water (base) parent record."""

    return {
        'id': PARENT_ID,
        'identifier': 'CHEBI:15377',  # Same CHEBI as all water variants
        'preferred_term': 'Water (base)',
        'mapping_status': 'MAPPED',
        'variant_type': 'BASE_CHEMICAL',
        'child_ingredients': list(WATER_VARIANTS.values()),
        'synonyms': [
            {
                'synonym_text': 'H2O',
                'synonym_type': 'EXACT_SYNONYM',
                'source': 'CHEBI'
            },
            {
                'synonym_text': 'water',
                'synonym_type': 'EXACT_SYNONYM',
                'source': 'common_name'
            }
        ],
        'occurrence_statistics': {
            'total_occurrences': 0,  # Parent is abstract concept
            'distinct_sources': 0,
        },
        'ontology_mapping': {
            'ontology_id': 'CHEBI:15377',
            'ontology_label': 'water',
            'ontology_source': 'CHEBI',
            'mapping_quality': 'EXACT_MATCH',
            'evidence': [
                {
                    'confidence_score': 1.0,
                    'notes': (
                        'Parent concept for all water purity variants.\n'
                        'Children inherit SOLVENT role but may have specific use restrictions.\n'
                        'This is an abstract grouping for hierarchy, not a specific water type.'
                    )
                }
            ]
        },
        'media_roles': [
            {
                'role': 'SOLVENT',
                'confidence': 1.0,
                'notes': 'Universal role inherited by all water variants'
            }
        ],
        'notes': (
            'Parent/base concept for water hierarchy.\n'
            'All water purity variants (tap, distilled, double distilled) are children.\n'
            'Enables queries like "find all media using any form of water".'
        ),
        'curation_history': [
            {
                'timestamp': '2026-03-14T12:00:00Z',
                'curator': 'build_water_hierarchy.py',
                'action': 'CREATED',
                'changes': 'Created parent Water (base) record for hierarchy',
                'llm_assisted': False,
            }
        ]
    }


def link_child_to_parent(
    child_record: dict,
    parent_id: str,
    variant_type: str,
    variant_notes: str
) -> None:
    """
    Add hierarchy fields to child record.

    Modifies record in place.
    """
    child_record['parent_ingredient'] = parent_id
    child_record['variant_type'] = variant_type
    child_record['variant_notes'] = variant_notes
    child_record['role_inheritance'] = True

    # Add curation history event
    if 'curation_history' not in child_record:
        child_record['curation_history'] = []

    child_record['curation_history'].append({
        'timestamp': '2026-03-14T12:00:00Z',
        'curator': 'build_water_hierarchy.py',
        'action': 'HIERARCHY_LINKED',
        'changes': f'Linked to parent Water (base) as variant_type={variant_type}',
        'notes': variant_notes,
        'llm_assisted': False,
    })


def build_water_hierarchy():
    """Build complete water variant hierarchy."""

    print("=" * 80)
    print("BUILDING WATER VARIANT HIERARCHY")
    print("=" * 80)
    print()

    # Load mapped ingredients
    curator = IngredientCurator(data_path='data/curated/mapped_ingredients.yaml')
    curator.load()

    print(f"Loaded {len(curator.records)} ingredient records")
    print()

    # Verify all water variants exist
    print("Verifying water variant records...")
    found_variants = {}

    for name, variant_id in WATER_VARIANTS.items():
        for idx, r in enumerate(curator.records):
            if r.get('id') == variant_id:
                found_variants[name] = (idx, r)
                print(f"  ✓ Found {name}: {r['preferred_term']} (ID: {variant_id})")
                break

    if len(found_variants) != len(WATER_VARIANTS):
        missing = set(WATER_VARIANTS.keys()) - set(found_variants.keys())
        print(f"\n❌ ERROR: Missing water variants: {missing}")
        return False

    print()

    # Check if parent already exists
    parent_exists = any(r.get('id') == PARENT_ID for r in curator.records)

    if parent_exists:
        print(f"⚠️  Parent record {PARENT_ID} already exists - skipping creation")
        parent_idx = next(i for i, r in enumerate(curator.records) if r.get('id') == PARENT_ID)
    else:
        # Create parent record
        print(f"Creating parent record: Water (base) (ID: {PARENT_ID})")
        parent_record = create_parent_record()
        curator.records.append(parent_record)
        parent_idx = len(curator.records) - 1
        print(f"  ✓ Created parent at index {parent_idx}")
        print()

    # Link children to parent
    print("Linking children to parent...")
    print("-" * 80)

    variant_configs = {
        'tap': {
            'variant_type': 'TAP',
            'variant_notes': (
                'Municipal water supply. Contains chlorine (0.2-4 ppm) and minerals (Ca²⁺, Mg²⁺).\n'
                'Variable composition depending on location and season.\n'
                'NOT suitable for trace-metal sensitive work or chlorine-sensitive organisms.'
            )
        },
        'demineralized': {
            'variant_type': 'DEMINERALIZED',
            'variant_notes': (
                'Ion exchange process removes ionic contaminants.\n'
                'Low mineral content (~1-10 µS/cm conductivity).\n'
                'May be equivalent to distilled water in microbiology practice (under expert review).'
            )
        },
        'distilled': {
            'variant_type': 'PURIFIED',
            'variant_notes': (
                'Single thermal distillation process.\n'
                'Standard laboratory water (<1 µS/cm conductivity).\n'
                'Baseline pure water for media preparation.\n'
                'Most common form (4105 occurrences).'
            )
        },
        'double_distilled': {
            'variant_type': 'ULTRA_PURIFIED',
            'variant_notes': (
                'Double distillation process (two cycles).\n'
                'Higher purity than standard distilled (<0.1 µS/cm vs <1 µS/cm).\n'
                '10x purer than single distilled water.\n'
                'Used for trace-metal sensitive work and applications requiring ultra-pure water.'
            )
        },
    }

    for name, (idx, record) in found_variants.items():
        config = variant_configs[name]

        print(f"\n{name.upper()}:")
        print(f"  Record: {record['preferred_term']} (ID: {record['id']})")

        # Add hierarchy fields
        link_child_to_parent(
            record,
            PARENT_ID,
            config['variant_type'],
            config['variant_notes']
        )

        print(f"  ✓ Set parent_ingredient: {PARENT_ID}")
        print(f"  ✓ Set variant_type: {config['variant_type']}")
        print(f"  ✓ Set role_inheritance: True")
        print(f"  ✓ Added curation history event")

    print()
    print("=" * 80)

    # Validate hierarchy
    print("VALIDATING HIERARCHY")
    print("=" * 80)
    print()

    validation_results = validate_all_hierarchies(curator.records)

    # Check parent
    parent_valid = not validation_results.get(PARENT_ID, [])
    if parent_valid:
        print(f"✅ Parent ({PARENT_ID}): VALID")
    else:
        print(f"❌ Parent ({PARENT_ID}): INVALID")
        for error in validation_results[PARENT_ID]:
            print(f"    - {error}")

    # Check children
    print()
    all_valid = True
    for name, variant_id in WATER_VARIANTS.items():
        errors = validation_results.get(variant_id, [])
        if not errors:
            print(f"✅ {name.capitalize()} ({variant_id}): VALID")
        else:
            print(f"❌ {name.capitalize()} ({variant_id}): INVALID")
            for error in errors:
                print(f"    - {error}")
            all_valid = False

    print()

    if not all_valid:
        print("⚠️  Validation failed - not saving changes")
        return False

    # Get hierarchy statistics
    print("=" * 80)
    print("HIERARCHY STATISTICS")
    print("=" * 80)
    print()

    stats = get_hierarchy_statistics(curator.records)

    print(f"Total records: {stats['total_records']}")
    print(f"Parent records: {stats['parent_count']}")
    print(f"Leaf records: {stats['leaf_count']}")
    print(f"Standalone records: {stats['standalone_count']}")
    print(f"Orphan records: {stats['orphan_count']}")
    print()

    print("Variant types:")
    for vtype, count in stats['variant_types'].items():
        print(f"  {vtype}: {count}")
    print()

    # Save changes
    print("=" * 80)
    print("SAVING CHANGES")
    print("=" * 80)
    print()

    curator.save()
    print("✅ Saved data/curated/mapped_ingredients.yaml")
    print()

    # Display hierarchy
    print("=" * 80)
    print("WATER HIERARCHY (COMPLETE)")
    print("=" * 80)
    print()

    parent = curator.records[parent_idx]
    print(f"📁 {parent['preferred_term']} (ID: {PARENT_ID})")
    print(f"   CHEBI: {parent['ontology_mapping']['ontology_id']}")
    print(f"   Variant type: {parent['variant_type']}")
    print(f"   Media roles: {[r['role'] for r in parent.get('media_roles', [])]}")
    print()

    for name, (idx, record) in found_variants.items():
        print(f"  ├─ {record['preferred_term']} (ID: {record['id']})")
        print(f"  │  Variant type: {record['variant_type']}")
        print(f"  │  Quality: {record['ontology_mapping']['mapping_quality']}")
        print(f"  │  Occurrences: {record['occurrence_statistics'].get('total_occurrences', 0)}")
        print(f"  │  Role inheritance: {record.get('role_inheritance', False)}")
        print(f"  │  Notes: {record['variant_notes'][:80]}...")
        print()

    print("=" * 80)
    print("✅ WATER HIERARCHY BUILD COMPLETE")
    print("=" * 80)

    return True


def main():
    """Execute hierarchy build."""

    print("WATER VARIANT HIERARCHY BUILDER")
    print("=" * 80)
    print()
    print("This script will:")
    print("  1. Create parent 'Water (base)' record (MediaIngredientMech:001108)")
    print("  2. Link 4 water variants as children:")
    print("     - Tap water (TAP)")
    print("     - Demineralized water (DEMINERALIZED)")
    print("     - Distilled water (PURIFIED)")
    print("     - Double distilled water (ULTRA_PURIFIED)")
    print("  3. Set role_inheritance=true on all children")
    print("  4. Validate bidirectional links")
    print()
    input("Press Enter to continue or Ctrl+C to cancel...")
    print()

    success = build_water_hierarchy()

    if success:
        print("\n✅ SUCCESS: Water hierarchy built and validated")
        return 0
    else:
        print("\n❌ FAILED: Hierarchy build failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
