# `data/ingredients/mapped/Maltodextrin.yaml`

## Verdict

Needs curation. The exact ChEBI maltodextrin identity, occurrence count, empty
exported `other` field, and final SSSOM row pass, but `CARBON_SOURCE` is still
supported only by provisional ChEBI-ancestry evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltodextrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:25140` with
  `ontology_mapping.ontology_id: CHEBI:25140`, label `maltodextrin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one total occurrence in one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malt_Extract_Broth` through `Maltose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:25140` as active `maltodextrin`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Maltodextrin`
  to `CHEBI:25140` with an empty `other` field.

## Completeness

- The identity and final SSSOM predicate are consistent, and no unreviewed
  synonyms publish.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from
  ChEBI carbohydrate ancestry with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for maltodextrin as a
  media carbon source can be attached.
