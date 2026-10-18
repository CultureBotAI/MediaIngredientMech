# `data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml`

## Verdict

Pass. The `cas:83846-92-8` fallback remains an intentional local registry
identity for cholinium dihydrogen phosphate; PubChem resolves the CAS to the
stored formula, InChI, and SMILES, current OLS has no exact ontology term, and
the zero occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml`.
- Identifier and grounding: `identifier: cas:83846-92-8`,
  `ontology_mapping.ontology_id: cas:83846-92-8`,
  `ontology_label: Cholinium dihydrogen phosphate`,
  `ontology_source: CAS`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS search for `cholinium dihydrogen phosphate` found 0 terms,
  preserving the original no-ChEBI fallback rationale.
- PubChem lookup of CAS `83846-92-8` resolves to CID `150067` with formula
  `C5H16NO5P` and the same standard InChI and SMILES stored in the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml data/ingredients/mapped/Cholinium_Lysinate.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  `cas:83846-92-8` is outside Engine A term-validation scope. A narrowed run
  over the three CHEBI-scoped records in this batch passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cholinium_Dihydrogen_Phosphate` SSSOM
  row, expected CAS unknown-term triage row, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:83846-92-8` rows,
  matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The CAS fallback identifier, formula, InChI, SMILES, zero occurrence count,
  SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
