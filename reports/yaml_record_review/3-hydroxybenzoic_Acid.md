# `data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:30764` 3-hydroxybenzoic acid identity,
CAS, structure fields, occurrence count, SSSOM row, and generated exports pass,
but the active `CARBON_SOURCE` role is supported only by a provisional
in-session computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30764`,
  `ontology_mapping.ontology_id: CHEBI:30764`,
  `ontology_label: 3-hydroxybenzoic acid`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:30764` returns the active label
  `3-hydroxybenzoic acid`, CAS `99-06-9`, and formula `C7H6O3`.
- PubChem resolves CAS `99-06-9` to CID `7420` with formula `C7H6O3`, InChI
  `InChI=1S/C7H6O3/c8-6-3-1-2-5(4-6)7(9)10/h1-4,8H,(H,9,10)`, and an
  equivalent meta-hydroxybenzoic-acid SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  review-report directories, found the active `MIM:3-hydroxybenzoic_Acid`
  SSSOM row mapping to `CHEBI:30764` with CAS `99-06-9` and the ChEBI-backed
  synonyms `3-carboxyphenol`, `m-Hydroxybenzoic acid`, and
  `m-salicylic acid`.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain five
  distinct recipes and six occurrences, matching `occurrence_statistics`.
- The `CARBON_SOURCE` role has only `reference_type: COMPUTATIONAL_PREDICTION`
  and explicitly says it was assigned by in-session Claude reasoning with no
  external API. That is not evidence that 3-hydroxybenzoic acid was the carbon
  source in any inspected source recipe.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, occurrence count,
  ChEBI synonyms, SSSOM row, aggregate copy, and docs row are present.
- The record has no open identity conflict or stale advisory row; the remaining
  gap is the unsupported active role.

## Recommended Edits

- In `data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml`, remove the
  unsupported `CARBON_SOURCE` role unless a future curator can attach
  record-specific evidence showing 3-hydroxybenzoic acid served that role in
  the cited media.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and round-trip verification.
