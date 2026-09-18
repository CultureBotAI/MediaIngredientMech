# `data/ingredients/mapped/Oxaloacetic_Acid.yaml`

## Verdict

Needs curation; major. The `CHEBI:30744` oxaloacetic-acid identity and CAS
value pass, but a provisional `CARBON_SOURCE` role and the anion label
`oxaloacetate` are both exported from unsupported YAML assertions.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxaloacetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30744` with
  `ontology_mapping.ontology_id: CHEBI:30744`, label `oxaloacetic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `328-42-7`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:Oxaloacetic_Acid` exactly to `CHEBI:30744`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:30744` as active `oxaloacetic acid`,
  reports CAS `328-42-7`, and lists `2-Oxobutanedioic acid` as an exact
  synonym, matching the record's CAS and reviewed ChEBI synonym.
- A fresh exact OLS4 search for `oxaloacetate` resolves the token to related
  anion classes, including `CHEBI:16452` oxaloacetate(2-), rather than as a
  synonym for `CHEBI:30744` oxaloacetic acid. The YAML synonym therefore
  crosses the protonation boundary and should not be exported as a final SSSOM
  `other` token for the acid record.
- The row-review manifest only confirmed the `CHEBI:30744` identity and that
  `oxaloacetate` was already represented; it did not make the anion label a
  true same-subject synonym.
- The `CARBON_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists`.

## Completeness

- The active ChEBI term, acid CAS-RN, formula, structure, and exact final SSSOM
  object agree.
- The record still needs curation to remove the anion synonym and to either
  source or drop the provisional nutritional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Oxaloacetic_Acid.yaml`, remove
  `oxaloacetate` from `synonyms`, preserve it only as rejected or
  historical provenance if useful, rebuild the final SSSOM, and rerun
  `scripts/validate_sssom_invariants.py` plus the id-label product check to
  prove the anion label no longer appears in `other`.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with cited
  experimental or recipe evidence, or remove the provisional role facet until
  source-backed role evidence is curated.
