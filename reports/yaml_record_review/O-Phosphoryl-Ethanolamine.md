# `data/ingredients/mapped/O-Phosphoryl-Ethanolamine.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup resolves to active `CHEBI:17553`
`O-phosphoethanolamine`, and both final SSSOM `other` tokens are real
same-subject synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/O-Phosphoryl-Ethanolamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17553` with
  `ontology_mapping.ontology_id: CHEBI:17553`, label `O-phosphoethanolamine`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Structure: `cas_rn: 1071-23-4`, formula `C2H8NO4P`, and matching InChI and
  SMILES populated from the CAS-backed CultureBotHT import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17553` as active
  `O-phosphoethanolamine`, carries CAS xref `1071-23-4`, lists
  `2-aminoethyl dihydrogen phosphate` as an exact synonym, and reports the same
  formula, InChI, and SMILES stored in the YAML.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records the synonym
  review for `CHEBI:17553` as `ALREADY_REPRESENTED`, matching the curated YAML
  synonym.
- The final SSSOM row maps `MIM:O-Phosphoryl-Ethanolamine` exactly to
  `CHEBI:17553`; its `other` values are the exact ChEBI synonym and the
  structured `CAS:1071-23-4` token for the same subject.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS xref, exact synonym, formula, structure, and final
  SSSOM row agree.
- No additional optional role or occurrence evidence is needed for this
  CultureBotHT CAS-grounded record.

## Recommended Edits

- None.
