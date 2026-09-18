# `data/ingredients/mapped/Calcium_Chloride.yaml`

## Verdict

Needs curation, minor. The rejected duplicate correctly points at the anhydrous
`CHEBI:3312` calcium dichloride representative and has no live SSSOM row, but
it still carries pre-merge synonyms, chemistry, a KG-Microbe node ID, and a
nutritional-role assertion that should have been stripped when occurrences
moved to `Cacl2`.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:3312`,
  `ontology_mapping.ontology_id: CHEBI:3312`,
  `ontology_label: calcium dichloride`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: REJECTED`.
- Direct OLS lookup for `CHEBI:3312` returns active label
  `calcium dichloride` with CAS `10043-52-4`, formula `Ca.2Cl`,
  InChI `InChI=1S/Ca.2ClH/h;2*1H/q+2;;/p-2`, and SMILES
  `[Ca+2].[Cl-].[Cl-]`, matching the anhydrous local structure fields.

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

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found no live
  `MIM:Calcium_Chloride` SSSOM row; `CHEBI:3312` is represented in SSSOM by
  the surviving `Cacl2` record.
- The same search found three calcium chloride dihydrate aliases on this
  rejected record's docs exports: `CaCl2 x 2 H2O`, `CaCl2*2H2O`, and
  `CaCl22H2O`. Those hydrated forms also remain in the per-record YAML as
  `HYDRATE_FORM` synonyms even though the record was merged into the anhydrous
  `CaCl2` record on 2026-08-20.
- The rejected tombstone still has anhydrous `chemical_properties`,
  `kg_microbe_node_id: CHEBI:3312`, and a `MINERAL_SOURCE` role sourced from 15
  old CultureMech occurrences; those are live-record fields rather than
  tombstone metadata.

## Completeness

- The identifier, rejected status, 0/0 occurrence count, aggregate rejected
  row, and absence of a live SSSOM row are synchronized.
- The anhydrous CAS and formula are historically coherent with the mapped
  target, but they are redundant on this rejected duplicate and keep the
  tombstone looking actionable in generated docs.

## Recommended Edits

- In `data/ingredients/mapped/Calcium_Chloride.yaml`, remove the stale
  dihydrate synonyms, raw CultureMech role text, chemistry, KG-Microbe node ID,
  and nutritional role from the rejected tombstone, leaving the representative
  pointer and merge history.
- Regenerate `data/curated/mapped_ingredients.yaml`, SSSOM/docs surfaces, and
  the label index; prove the cleanup with strict validation, round-trip
  verification, and `scripts/validate_sssom_invariants.py`.
