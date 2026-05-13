#!/usr/bin/env python3
"""
Merge distilled water variants.

Actions:
1. Merge 7 distilled water variants into canonical "Distilled water" record
2. Downgrade "Double distilled water" quality to CLOSE_MATCH
3. Map "Tap water" with CLOSE_MATCH

Run with: PYTHONPATH=src python scripts/merge_distilled_water.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.curation.synonym_manager import SynonymManager


def merge_distilled_water_variants():
    """Merge all distilled water variants into canonical record."""

    print("=" * 80)
    print("MERGING DISTILLED WATER VARIANTS")
    print("=" * 80)
    print()

    # Load mapped and unmapped
    mapped = IngredientCurator(data_path='data/curated/mapped_ingredients.yaml')
    mapped.load()

    unmapped = IngredientCurator(data_path='data/curated/unmapped_ingredients.yaml')
    unmapped.load()

    # Find target: "Distilled water" (highest occurrences)
    target_idx = None
    for idx, r in enumerate(mapped.records):
        if r.get('preferred_term') == 'Distilled water':
            target_idx = idx
            break

    if target_idx is None:
        print("ERROR: Target 'Distilled water' not found!")
        return False

    print(f"TARGET: [mapped:{target_idx}] Distilled water")
    print(f"  ID: {mapped.records[target_idx]['id']}")
    print(f"  Occurrences: {mapped.records[target_idx]['occurrence_statistics']['total_occurrences']}")
    print()

    # Find sources to merge (from mapped)
    sources_mapped = []
    for idx, r in enumerate(mapped.records):
        if idx == target_idx:
            continue
        term = r.get('preferred_term', '')
        if term in ['distilled water', 'Distilled Water', 'Distilled water ']:
            sources_mapped.append(idx)

    print(f"SOURCES FROM MAPPED ({len(sources_mapped)}):")
    for idx in sources_mapped:
        r = mapped.records[idx]
        print(f"  [mapped:{idx}] {r['preferred_term']!r}")
        print(f"    ID: {r['id']}")
        print(f"    Occurrences: {r['occurrence_statistics']['total_occurrences']}")
    print()

    # Find sources to merge (from unmapped - these are actually mapped)
    sources_unmapped = []
    for idx, r in enumerate(unmapped.records):
        term = r.get('preferred_term', '')
        if term in ['dH2O', 'sterile dH2O', 'Sterile dH2O']:
            sources_unmapped.append(idx)

    print(f"SOURCES FROM UNMAPPED FILE ({len(sources_unmapped)}):")
    for idx in sources_unmapped:
        r = unmapped.records[idx]
        print(f"  [unmapped:{idx}] {r['preferred_term']!r}")
        print(f"    ID: {r['id']}")
        print(f"    Occurrences: {r['occurrence_statistics'].get('total_occurrences', 0)}")
    print()

    # Perform merges (mapped → mapped)
    print("MERGING MAPPED VARIANTS...")
    print("-" * 80)

    synonym_manager = SynonymManager(mapped.records)

    for source_idx in reversed(sorted(sources_mapped)):  # Reverse to preserve indices
        source = mapped.records[source_idx]
        print(f"\nMerging [{source_idx}] {source['preferred_term']!r} → [{target_idx}] Distilled water")

        # Add source term as synonym
        synonym_manager.add_synonym(
            record_index=target_idx,
            synonym_text=source['preferred_term'],
            synonym_type='EXACT',
            source='merge_case_variation'
        )

        # Combine occurrence statistics
        target_occ = mapped.records[target_idx]['occurrence_statistics']
        source_occ = source['occurrence_statistics']

        target_occ['total_occurrences'] += source_occ.get('total_occurrences', 0)
        target_occ['distinct_sources'] = target_occ.get('distinct_sources', 0) + source_occ.get('distinct_sources', 0)

        # Add curation history event
        mapped._add_event(
            mapped.records[target_idx],
            action='merge_duplicate',
            notes=f"Merged {source['preferred_term']!r} (ID: {source['id']}) into canonical record. Case variation only."
        )

        # Mark source as REJECTED
        mapped.change_status(
            mapped.records[source_idx],
            'REJECTED',
            notes='Duplicate of Distilled water (MediaIngredientMech:000114)'
        )
        mapped._add_event(
            mapped.records[source_idx],
            action='reject_duplicate',
            notes=f"Merged into Distilled water (MediaIngredientMech:000114). See target record for combined data."
        )

        print(f"  ✓ Added synonym: {source['preferred_term']!r}")
        print(f"  ✓ Added {source_occ.get('total_occurrences', 0)} occurrences")
        print(f"  ✓ Marked source as REJECTED")

    # Merge unmapped variants (add as synonyms, don't delete yet)
    print("\nMERGING UNMAPPED FILE VARIANTS...")
    print("-" * 80)

    for idx in sources_unmapped:
        source = unmapped.records[idx]
        print(f"\nAdding [{idx}] {source['preferred_term']!r} as synonym to Distilled water")

        # Add as synonym
        synonym_manager.add_synonym(
            record_index=target_idx,
            synonym_text=source['preferred_term'],
            synonym_type='EXACT',
            source='merge_abbreviation'
        )

        # Combine occurrences
        target_occ = mapped.records[target_idx]['occurrence_statistics']
        source_occ = source['occurrence_statistics']

        target_occ['total_occurrences'] += source_occ.get('total_occurrences', 0)

        # Add curation history
        mapped._add_event(
            mapped.records[target_idx],
            action='merge_abbreviation',
            notes=f"Merged {source['preferred_term']!r} (ID: {source['id']}) - abbreviation/sterile variant of distilled water."
        )

        print(f"  ✓ Added synonym: {source['preferred_term']!r}")
        print(f"  ✓ Added {source_occ.get('total_occurrences', 0)} occurrences")
        print(f"  Note: Source record remains in unmapped file (will be removed in cleanup)")

    # Save mapped file
    print("\nSAVING CHANGES...")
    mapped.save()
    print("✓ Saved data/curated/mapped_ingredients.yaml")

    # Display final target record
    target = mapped.records[target_idx]
    print("\n" + "=" * 80)
    print("FINAL MERGED RECORD")
    print("=" * 80)
    print(f"Preferred term: {target['preferred_term']}")
    print(f"ID: {target['id']}")
    print(f"CHEBI: {target['ontology_mapping']['ontology_id']}")
    print(f"Quality: {target['ontology_mapping']['mapping_quality']}")
    print(f"Total occurrences: {target['occurrence_statistics']['total_occurrences']}")
    print(f"\nSynonyms ({len(target.get('synonyms', []))}):")
    for syn in target.get('synonyms', [])[:10]:
        if isinstance(syn, dict):
            print(f"  - {syn.get('text', syn)} (source: {syn.get('source', 'unknown')})")
        else:
            print(f"  - {syn}")
    if len(target.get('synonyms', [])) > 10:
        print(f"  ... and {len(target['synonyms']) - 10} more")

    return True


def downgrade_double_distilled_quality():
    """Downgrade Double distilled water from EXACT_MATCH to CLOSE_MATCH."""

    print("\n" + "=" * 80)
    print("DOWNGRADING DOUBLE DISTILLED WATER QUALITY")
    print("=" * 80)
    print()

    # Load mapped
    mapped = IngredientCurator(data_path='data/curated/mapped_ingredients.yaml')
    mapped.load()

    # Find Double distilled water
    target_idx = None
    for idx, r in enumerate(mapped.records):
        if r.get('preferred_term') == 'Double distilled water':
            target_idx = idx
            break

    if target_idx is None:
        print("ERROR: 'Double distilled water' not found!")
        return False

    record = mapped.records[target_idx]
    print(f"TARGET: [mapped:{target_idx}] Double distilled water")
    print(f"  ID: {record['id']}")
    print(f"  Current quality: {record['ontology_mapping']['mapping_quality']}")
    print()

    # Change quality to CLOSE_MATCH
    old_quality = record['ontology_mapping']['mapping_quality']
    record['ontology_mapping']['mapping_quality'] = 'CLOSE_MATCH'

    # Update evidence
    evidence = record['ontology_mapping'].get('evidence', [])
    if evidence:
        evidence[0]['confidence_score'] = 0.85
        evidence[0]['notes'] = (
            "Double distilled water (ddH2O) = two distillation cycles.\n"
            "Higher purity than standard distilled water (<0.1 µS/cm vs <1 µS/cm).\n"
            "CLOSE_MATCH instead of EXACT_MATCH to prevent merging with single-distilled water.\n"
            "Used for trace-metal sensitive work and applications requiring ultra-pure water."
        )
    else:
        record['ontology_mapping']['evidence'] = [{
            'confidence_score': 0.85,
            'notes': (
                "Double distilled water (ddH2O) = two distillation cycles.\n"
                "Higher purity than standard distilled water (<0.1 µS/cm vs <1 µS/cm).\n"
                "CLOSE_MATCH instead of EXACT_MATCH to prevent merging with single-distilled water.\n"
                "Used for trace-metal sensitive work and applications requiring ultra-pure water."
            )
        }]

    # Add curation history
    mapped._add_event(
        record,
        action='update_quality',
        notes=f"Downgraded quality from {old_quality} to CLOSE_MATCH. Prevents inappropriate merging with standard distilled water due to different purity levels (10x difference)."
    )

    # Save
    mapped.save()
    print(f"✓ Changed quality: {old_quality} → CLOSE_MATCH")
    print(f"✓ Updated evidence with purity distinction notes")
    print(f"✓ Saved changes")

    return True


def map_tap_water():
    """Map tap water with CLOSE_MATCH quality."""

    print("\n" + "=" * 80)
    print("MAPPING TAP WATER")
    print("=" * 80)
    print()

    # Load unmapped
    unmapped = IngredientCurator(data_path='data/curated/unmapped_ingredients.yaml')
    unmapped.load()

    # Find Tap water variants
    tap_variants = []
    for idx, r in enumerate(unmapped.records):
        term = r.get('preferred_term', '')
        if term.lower() == 'tap water':
            tap_variants.append((idx, term))

    if not tap_variants:
        print("No tap water variants found in unmapped file.")
        return True

    print(f"Found {len(tap_variants)} tap water variant(s):")
    for idx, term in tap_variants:
        print(f"  [unmapped:{idx}] {term}")
    print()

    # Map each variant
    for idx, term in tap_variants:
        record = unmapped.records[idx]

        print(f"Mapping: {term}")

        # Accept mapping
        unmapped.accept_mapping(
            index=idx,
            ontology_id='CHEBI:15377',
            ontology_label='water',
            ontology_source='CHEBI',
            quality='CLOSE_MATCH',
            evidence_notes=(
                "Tap water = municipal water supply.\n"
                "Contains chlorine (0.2-4 ppm), minerals (Ca²⁺, Mg²⁺), variable composition.\n"
                "Lower confidence due to impurity - not pure H₂O.\n"
                "NOT suitable for trace-metal work or chlorine-sensitive organisms.\n"
                "CLOSE_MATCH prevents merging with distilled water (different purity levels)."
            ),
            confidence_score=0.70,
            curator='merge_distilled_water.py'
        )

        print(f"  ✓ Mapped to CHEBI:15377 (water)")
        print(f"  ✓ Quality: CLOSE_MATCH (impure variant)")
        print(f"  ✓ Confidence: 0.70")

    # Save
    unmapped.save()
    print(f"\n✓ Saved changes to unmapped file")

    return True


def main():
    """Execute all immediate actions."""

    print("WATER VARIANT CURATION - IMMEDIATE ACTIONS")
    print("=" * 80)
    print()
    print("This script will:")
    print("  1. Merge 7 distilled water variants → 1 canonical record")
    print("  2. Downgrade Double distilled water quality (EXACT_MATCH → CLOSE_MATCH)")
    print("  3. Map Tap water with CLOSE_MATCH")
    print()
    input("Press Enter to continue or Ctrl+C to cancel...")
    print()

    # Execute actions
    success = True

    # Action 1: Merge distilled water
    if not merge_distilled_water_variants():
        print("\n❌ Failed to merge distilled water variants")
        success = False

    # Action 2: Downgrade double distilled
    if not downgrade_double_distilled_quality():
        print("\n❌ Failed to downgrade double distilled water quality")
        success = False

    # Action 3: Map tap water
    if not map_tap_water():
        print("\n❌ Failed to map tap water")
        success = False

    # Summary
    print("\n" + "=" * 80)
    if success:
        print("✅ ALL IMMEDIATE ACTIONS COMPLETED SUCCESSFULLY")
    else:
        print("⚠️ SOME ACTIONS FAILED - CHECK OUTPUT ABOVE")
    print("=" * 80)

    return success


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
