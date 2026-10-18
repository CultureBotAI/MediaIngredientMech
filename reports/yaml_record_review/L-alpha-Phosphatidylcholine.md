# `data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml`

## Verdict

Pass. The transliterated OLS exact match to active CHEBI:86658, preserved
Greek-letter source synonym, occurrence count, ChEBI chemistry, and final SSSOM
row are consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml`.
- Identifier and grounding: `identifier: CHEBI:86658` with
  `ontology_mapping.ontology_id: CHEBI:86658`, label
  `L-alpha-Phosphatidylcholine`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Chemical properties: molecular weight `758.075` from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-alanylglycine.yaml data/ingredients/mapped/L-alliin.yaml data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml data/ingredients/mapped/L-arginine.yaml data/ingredients/mapped/L-arginine_X_Hcl.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:86658` as active
  `L-alpha-Phosphatidylcholine` with the same molecular weight as the YAML
  record.
- The source spelling with the Greek alpha was preserved as an exact synonym
  after transliteration to the ChEBI primary label; that is a same-substance
  label, not a broader parent or provenance note.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:86658` and
  includes only the Greek-letter original label in `other`.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, occurrence membership rows, and the
  `unmapped_ingredients_ols_exact_audit.tsv` candidate that originally
  supported the promotion.

## Completeness

- The ChEBI exact identity, occurrence count, preserved source synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported role, component, or environment claims are present.

## Recommended Edits

- None.
