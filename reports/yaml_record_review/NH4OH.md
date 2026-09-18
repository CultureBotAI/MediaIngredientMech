# `data/ingredients/mapped/NH4OH.yaml`

## Verdict

Pass. The residual CultureMech `NH4OH` surface is grounded to exact ChEBI
synonym `CHEBI:18219` ammonium hydroxide with restored structured provenance
and a clean final exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/NH4OH.yaml`.
- Identifier and grounding: `identifier: CHEBI:18219` with
  `ontology_mapping.ontology_id: CHEBI:18219`, label `ammonium hydroxide`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `match_level: NORMALIZED`.
- Occurrences: one CultureMech occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-lauroylsarcosine_Sodium_Salt` through
  `NNNN-Tetramethylethylenediamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:18219` as active
  `ammonium hydroxide` and includes `NH4OH` as a synonym of the same solution.
- `mappings/culturemech_residual_groundings.tsv` records `NH4OH` as a
  one-mention CultureMech residual grounded to `CHEBI:18219`.
- The #541 correction restored the CultureMech occurrence table to
  `ontology_mapping.evidence`, and the final SSSOM row now includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Completeness

- The active ChEBI target, residual-source provenance, exact-synonym grounding,
  occurrence count, and final row agree.
- The record does not assert components, roles, or unsupported synonyms.

## Recommended Edits

- None.
