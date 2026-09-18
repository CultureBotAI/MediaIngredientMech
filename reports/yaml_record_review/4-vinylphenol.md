# `data/ingredients/mapped/4-vinylphenol.yaml`

## Verdict

Needs curation, major. The CAS-backed `CHEBI:1883` 4-hydroxystyrene identity,
CAS, chemistry, and SSSOM exact-match row pass, but two trace-minerals source
labels are stored and exported as exact synonyms of the chemical.

## Identity

- Reviewed record: `data/ingredients/mapped/4-vinylphenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:1883` with
  `ontology_mapping.ontology_id: CHEBI:1883`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:1883` is active and resolves to
  `4-hydroxystyrene`.
- The current ChEBI page reports CAS `2628-17-3`, formula `C8H8O`, the stored
  SMILES, and the stored InChI for `CHEBI:1883`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml data/ingredients/mapped/5-Azacytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-vinylphenol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and exact synonym
  `4-vinylphenol` support the CAS-based grounding to `CHEBI:1883`.
- The explicit CAS regrade is appropriate: the record was created through
  CultureBotHT CAS `2628-17-3` resolving by ChEBI xref to `CHEBI:1883`, so
  `CAS_RN_LOOKUP` preserves the mapping method better than a lexical grade.
- The exact ChEBI synonym `4-ethenylphenol` is acceptable.
- Major: `Trace minerals (see Medium No.151` and
  `Trace minerals(see Medium No.151)` are media note fragments, not names for
  4-vinylphenol. They leak through the aggregate copy, SSSOM `other`, generated
  ingredient JSON, and generated `label_index` as synonyms for `CHEBI:1883`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`,
  `UNIFIED_INGREDIENT_MAPPING.tsv`, `src`, `scripts`, `tests`, `conf`,
  `.github`, and `.claude` found the active YAML, aggregate copy, SSSOM row,
  generated docs, row-review outputs, stale advisory rows, and ignored
  aggregate backups for this identifier and the bad trace-minerals strings.

## Completeness

- CAS, formula, InChI, SMILES, `ingredient_type`, and the legitimate
  `4-ethenylphenol` exact synonym are populated.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

1. Remove or reject the two `Trace minerals...` `RAW_TEXT` synonyms in
   `data/ingredients/mapped/4-vinylphenol.yaml` and
   `data/curated/mapped_ingredients.yaml`, then regenerate SSSOM and docs so
   those medium-note fragments no longer publish as exact synonym labels.
