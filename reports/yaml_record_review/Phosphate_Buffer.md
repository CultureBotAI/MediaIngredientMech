# `data/ingredients/mapped/Phosphate_Buffer.yaml`

## Verdict

Needs curation; major. The mim-queue import maps exactly to active
`NCIT:C29321` Phosphate Buffer and the final SSSOM row has no unsafe `other`
values, but `BUFFER` is still supported only by a provisional name-list
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Phosphate_Buffer.yaml`.
- Identifier and grounding: `identifier: NCIT:C29321` with
  `ontology_mapping.ontology_id: NCIT:C29321`, label `Phosphate Buffer`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 10 CultureMech occurrences across 10 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `NCIT:C29321` resolves `NCIT:C29321`
  `Phosphate Buffer`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` also
  records `NCIT:C29321` as a resolved exact NCIT CURIE; the older
  `UNKNOWN_TERM` row-review result is a local OAK/OLS coverage artifact.
- The final SSSOM row was inspected directly and maps `MIM:Phosphate_Buffer`
  exactly to `NCIT:C29321`.

## Evidence

- The mim-queue lexical import exactly matched MediaDive ingredient 625 to the
  NCIT phosphate-buffer class, which fits a generic phosphate-buffer reagent.
- The #337 occurrence refresh corrected occurrence statistics to 10 distinct
  CultureMech recipes.
- The final SSSOM row exports no `other` tokens.
- Major: the `BUFFER` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from a provisional curated name-pattern rule.

## Completeness

- The identity and final synonym surface are complete enough for this exact
  NCIT mapping.
- Physicochemical-role evidence remains incomplete while the buffer role is
  provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phosphate_Buffer.yaml`, replace
  `physicochemical_roles.BUFFER` with source-backed evidence or remove the
  provisional role facet until it is curated.
