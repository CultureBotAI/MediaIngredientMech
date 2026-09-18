# `data/ingredients/mapped/Octane.yaml`

## Verdict

Pass. The CultureBotHT CAS import exact-maps to active `CHEBI:17590` octane,
and the final SSSOM row only exports the structured CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Octane.yaml`.
- Identifier and grounding: `identifier: CHEBI:17590` with
  `ontology_mapping.ontology_id: CHEBI:17590`, label `octane`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Structure: `cas_rn: 111-65-9`, formula `C8H18`, and matching InChI and
  SMILES populated from the CAS-backed CultureBotHT import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17590` as active `octane`, carries
  CAS xref `111-65-9`, and reports the same formula, InChI, and SMILES stored
  in the YAML.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms the final
  `CHEBI:17590` mapping.
- The final SSSOM row maps `MIM:Octane` exactly to `CHEBI:17590`; its only
  `other` token is structured `CAS:111-65-9`.
- No unsupported synonyms, roles, components, supplied forms, or environmental
  contexts are asserted.

## Completeness

- The active ChEBI term, CAS xref, formula, structure fields, final SSSOM CAS
  token, and SSSOM row-review result agree.
- No optional occurrence or role slots need to be filled for this CultureBotHT
  CAS import.

## Recommended Edits

- None.
