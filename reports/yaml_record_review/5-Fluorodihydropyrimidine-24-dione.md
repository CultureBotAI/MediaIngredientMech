# `data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml`

## Verdict

Pass, none. The CAS-backed `CHEBI:80624` 5,6-dihydro-5-fluorouracil identity,
CAS, chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml`.
- Identifier and grounding: `identifier: CHEBI:80624` with
  `ontology_mapping.ontology_id: CHEBI:80624`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:80624` is active and resolves to
  `5,6-Dihydro-5-fluorouracil`.
- The current ChEBI page reports CAS `696-06-0`, formula `C4H5FN2O2`, the
  stored SMILES, and the stored InChI for `CHEBI:80624`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml data/ingredients/mapped/5-Hydroxydodecanoate.yaml data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, and InChI all support the
  CAS-based grounding to `CHEBI:80624`.
- The explicit CAS regrade is appropriate: the record was created through
  CultureBotHT CAS `696-06-0` resolving by ChEBI xref to `CHEBI:80624`, so
  `CAS_RN_LOOKUP` preserves the mapping method better than a lexical grade.
- The SSSOM row maps `MIM:5-Fluorodihydropyrimidine-24-dione` to
  `CHEBI:80624` with `skos:exactMatch`, `semapv:ManualMappingCuration`, and
  `CAS:696-06-0` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, generated docs, source review outputs, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
