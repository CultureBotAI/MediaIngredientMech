# `data/ingredients/mapped/Cisplatin.yaml`

## Verdict

Pass. The CultureBotHT cisplatin record is exactly grounded to active
`CHEBI:27899`; its CAS RN, formula, InChI, SMILES, ChEBI exact synonyms, zero
occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cisplatin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27899`,
  `ontology_mapping.ontology_id: CHEBI:27899`,
  `ontology_label: cisplatin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `cisplatin` returns active `CHEBI:27899` labelled
  `cisplatin`, plus more specific cisplatin-adduct terms and inactive
  siblings that do not match this record.
- PubChem lookup by `cisplatin` returns CID 5702198, formula `Cl2H6N2Pt`, and
  the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cisplatin` SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:27899` only in this active record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:27899`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The four curated exact synonyms all appear as ChEBI exact synonyms for
  `CHEBI:27899` in live OLS.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
