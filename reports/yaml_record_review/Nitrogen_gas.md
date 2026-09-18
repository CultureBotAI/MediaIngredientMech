# `data/ingredients/mapped/Nitrogen_gas.yaml`

## Verdict

Needs curation - major. The manual headspace-gas identity exact-maps to active
`CHEBI:17997` dinitrogen and the structure block agrees, but final SSSOM
`other` still publishes the unsupported `#N2` token.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrogen_gas.yaml`.
- Identifier and grounding: `identifier: CHEBI:17997` with
  `ontology_mapping.ontology_id: CHEBI:17997`, label `dinitrogen`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1109 CultureMech recipe occurrences across 980 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17997` as active `dinitrogen` with
  formula `N2`, CAS `7727-37-9`, InChI `InChI=1S/N2/c1-2`, and SMILES
  `N#N`, matching the record.
- OLS also lists `Nitrogen`, `dinitrogen`, `N#N`, `N(2)`, `N2`, and
  `molecular nitrogen` as synonyms for `CHEBI:17997`, so the non-hash SSSOM
  `other` tokens are same-substance aliases.
- Major: `#N2` appears in the curated synonym list and in the final SSSOM
  `other` column, but a gitignore-independent search across `data`, `src`,
  `tests`, `mappings`, and `scripts` found no source occurrence or curation
  note demonstrating that `#N2` denotes nitrogen gas. Unlike the neighboring
  nitrous oxide `#N2O` record, this record has no local review event tying the
  hash-prefixed token to a raw source surface.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, formula, structure, occurrence count, and final exact
  row otherwise agree.
- The remaining consequential gap is the unsupported hash-prefixed synonym in
  both YAML and the final SSSOM `other` value.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nitrogen_gas.yaml`, either add inspected
  evidence that `#N2` is a real raw label for nitrogen gas or remove it from
  active synonyms so a rebuild drops it from final `other`.
