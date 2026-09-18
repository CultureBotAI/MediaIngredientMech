# `data/ingredients/mapped/Oxonitine.yaml`

## Verdict

Pass. The CultureBotHT `Oxonitine` record maps exactly to active
`CHEBI:132646` oxonitine, and the final SSSOM `other` token is the same
ChEBI IUPAC synonym stored in YAML.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxonitine.yaml`.
- Identifier and grounding: `identifier: CHEBI:132646` with
  `ontology_mapping.ontology_id: CHEBI:132646`, label `oxonitine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxonitine`
  exactly to `CHEBI:132646`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132646` as active `oxonitine` and
  reports the same formula, InChI, and SMILES stored in the YAML.
- The exported
  `8-(acetyloxy)-20-formyl-3,13,15alpha-trihydroxy-1alpha,6alpha,16beta-trimethoxy-4-(methoxymethyl)aconitan-14alpha-yl benzoate`
  token is the ChEBI exact IUPAC synonym for this term.
- The row-review manifest already confirmed the `CHEBI:132646` ontology row.
- No roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, formula, structure, exact synonym, and final SSSOM row
  agree.

## Recommended Edits

- None.
