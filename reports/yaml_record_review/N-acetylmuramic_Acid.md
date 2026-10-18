# `data/ingredients/mapped/N-acetylmuramic_Acid.yaml`

## Verdict

Pass. The active `CHEBI:47965` N-acetylmuramic acid merge winner, supplied
commercial CAS, folded aldehydo synonyms, occurrence count, and final exact row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetylmuramic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:47965` with
  `ontology_mapping.ontology_id: CHEBI:47965`, label
  `N-acetylmuramic acid`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 12 CultureMech recipe occurrences after the #398 loser merge and
  #337 count refresh.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetyl-lysine` through `N-acetylmuramic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- Fresh EBI OLS4 lookups resolve `CHEBI:47965` as active
  `N-acetylmuramic acid` and `CHEBI:47966` as active
  `aldehydo-N-acetylmuramic acid`; together they account for the winner's
  native ChEBI synonyms, the folded aldehydo aliases, and the `10597-89-4` CAS
  carried in `supplied_form`.
- The #398 curation history documents the intentional fold of
  `n-Acetyl-muramic acid` and the aldehydo aliases onto the active record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetylmuramic_Acid` to `CHEBI:47965`; its `other` values are the
  winner's ChEBI synonyms, the folded loser label and aldehydo aliases, and
  `CAS:10597-89-4`.

## Completeness

- The active ChEBI target, folded synonym surface, supplied-form CAS, 12/12
  occurrence count, label-index rows, and final SSSOM row agree.
- The SSSOM comment explicitly marks the aldehydo payload as synonym enrichment,
  so the broader final synonym surface is traceable to the #398 merge decision.

## Recommended Edits

- None.
