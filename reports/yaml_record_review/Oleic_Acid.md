# `data/ingredients/mapped/Oleic_Acid.yaml`

## Verdict

Pass. The CultureMech oleic-acid record exact-maps to active `CHEBI:16196`, its
carbon-source role preserves original CultureMech role text, and the final
SSSOM synonym payload contains only same-subject chemical aliases and the
structured CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Oleic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16196` with
  `ontology_mapping.ontology_id: CHEBI:16196`, label `oleic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Structure: `cas_rn: 112-80-1`, formula `C18H34O2`, and matching InChI and
  SMILES.
- Occurrences: 17 CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16196` as active `oleic acid`,
  carries CAS xref `112-80-1`, and reports the same formula, InChI, and SMILES
  stored in the YAML.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms the final
  `CHEBI:16196` mapping.
- The `CARBON_SOURCE` role has `DATABASE_ENTRY` evidence that preserves the
  original CultureMech role text `Carbon Source`; it is not only a
  name-pattern inference.
- The final SSSOM row maps `MIM:Oleic_Acid` exactly to `CHEBI:16196`; its
  `other` tokens are the curated ChEBI-compatible chemical synonyms plus
  structured `CAS:112-80-1`.
- The raw `Role:` and `Properties:` provenance strings stay out of final
  SSSOM `other`.

## Completeness

- The active ChEBI term, CAS xref, formula, structure, role evidence,
  occurrence count, and final SSSOM row agree.
- The hidden and ignored-inclusive search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found `Oleic Acid (Sigma Cat # O-1008)` as
  a separate unresolved CultureMech residual, but that catalog-qualified label
  is not present on this record or exported as an unsafe synonym.

## Recommended Edits

- None for this record.
