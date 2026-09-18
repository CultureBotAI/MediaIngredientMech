# `data/ingredients/mapped/Calcium_D-Pantothenate.yaml`

## Verdict

Needs curation, minor. The duplicate was correctly rejected into
`Calcium_Pantothenate` and does not publish a live SSSOM row, but stale
pre-merge notes, structure fields, KG-Microbe linkage, and an inferred vitamin
role remain on the tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium_D-Pantothenate.yaml`.
- Identifier and grounding: `identifier: CHEBI:31345`,
  `ontology_mapping.ontology_id: CHEBI:31345`,
  `ontology_label: Calcium pantothenate`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: REJECTED`.
- Direct OLS lookup for `CHEBI:31345` returns the active label
  `Calcium pantothenate` and the CAS `137-08-6`; PubChem resolves that CAS to
  CID `443753`, the calcium pantothenate salt also used by the surviving
  record.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The 2026-08-05 `MERGED_INTO` event records the same-substance merge into the
  surviving `CHEBI:31345` `Calcium pantothenate` record.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found no live
  `MIM:Calcium_D-Pantothenate` row in
  `mappings/ingredient_mappings.sssom.tsv`; the only live `CHEBI:31345` row is
  `MIM:Calcium_Pantothenate`.
- The same search found `Calcium D-Pantothenate` as a raw synonym on the active
  `Calcium_Pantothenate` record and in generated label indexes, preserving the
  absorbed surface form.

## Completeness

- The rejected status, 0/0 occurrence count, merge history, aggregate row, and
  absence of a live SSSOM row are synchronized.
- `notes` still say no CAS/CHEBI/NCIT match and curator review needed even
  though the record has been resolved and merged.
- The tombstone still carries live-record fields:
  `ingredient_type: SINGLE_INGREDIENT`, the calcium pantothenate structure
  bundle, `kg_microbe_node_id: CHEBI:31345`, and an inferred
  `VITAMIN_SOURCE` role.

## Recommended Edits

- In `data/ingredients/mapped/Calcium_D-Pantothenate.yaml`, remove the stale
  notes and live-record fields from the rejected tombstone, leaving the raw
  synonym, ontology pointer, 0/0 occurrence count, and merge history.
- Regenerate `data/curated/mapped_ingredients.yaml`, SSSOM/docs surfaces, and
  the label index; prove the cleanup with strict validation, round-trip
  verification, and `scripts/validate_sssom_invariants.py`.
