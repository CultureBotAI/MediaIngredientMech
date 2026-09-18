# `data/ingredients/mapped/Bimuno.yaml`

## Verdict

Pass. The `NCIT:C187267` Bimuno/Galacto-oligosaccharide Prebiotic Supplement
identity, exact synonym evidence, undefined-mixture classification, SSSOM row,
and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bimuno.yaml`.
- Identifier and grounding: `identifier: NCIT:C187267` with
  `ontology_mapping.ontology_id: NCIT:C187267`,
  `ontology_label: Galacto-oligosaccharide Prebiotic Supplement`,
  `ontology_source: NCIT`, `mapping_quality: EXACT_MATCH`,
  `ingredient_type: UNDEFINED_MIXTURE`, and `mapping_status: MAPPED`.
- Live OLS search in NCIT returns `NCIT:C187267` and lists `Bimuno` as an exact
  synonym of `Galacto-oligosaccharide Prebiotic Supplement`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biochanin_A_Diacetate.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biotin_Vitamin_Solution.yaml data/ingredients/mapped/Biphenyl.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT/CHEBI records in this batch.
- Engine A term validation is intentionally skipped for the CAS registry record
  and the `kgmicrobe.ingredient` record. The previous full-corpus SSSOM
  validator passed, with Rule B4 skipped because sibling kg-microbe ontology
  transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative NCIT SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 595, the original exact-synonym
  audit row in `mappings/unmapped_ingredients_ols_exact_audit.tsv`, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact NCIT identifier, kg-microbe node ID mirror, undefined-mixture
  classification, exact synonym evidence, SSSOM row, zero occurrence count, and
  aggregate copy are populated.
- No CAS, formula, InChI, SMILES, or component list is required for this branded
  galacto-oligosaccharide prebiotic supplement class.

## Recommended Edits

- None.
