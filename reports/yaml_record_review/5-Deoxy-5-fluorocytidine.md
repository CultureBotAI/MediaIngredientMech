# `data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml`

## Verdict

Pass, none. The exact `CHEBI:80627` identity, CultureBotHT CAS provenance,
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:80627` with
  `ontology_mapping.ontology_id: CHEBI:80627`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:80627` is active and resolves to
  `5'-Deoxy-5-fluorocytidine`.
- The current ChEBI page reports formula `C9H12FN3O4`, the stored SMILES, and
  the stored InChI for `CHEBI:80627`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml data/ingredients/mapped/5-Hydroxydodecanoate.yaml data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The active ChEBI term, formula, SMILES, and InChI all support the exact
  5'-deoxy-5-fluorocytidine identity.
- The CultureBotHT CAS value `66335-38-4` is retained in
  `chemical_properties.cas_rn` and exported only as `CAS:66335-38-4` in the
  SSSOM `other` column.
- The SSSOM row maps `MIM:5-Deoxy-5-fluorocytidine` to `CHEBI:80627` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the CAS payload.
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
