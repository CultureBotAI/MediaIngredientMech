# `data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml`

## Verdict

Needs curation; major. The `CHEBI:31953` oxytetracycline-hydrochloride salt
identity passes, but the `SELECTIVE_AGENT` role is only a provisional
name-list prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:31953` with
  `ontology_mapping.ontology_id: CHEBI:31953`, label
  `Oxytetracycline hydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `2058-46-0`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:Oxytetracycline_Hydrochloride` exactly to `CHEBI:31953`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:31953` as active
  `Oxytetracycline hydrochloride` and reports CAS `2058-46-0`, the formula,
  the InChI, and the SMILES stored in the YAML.
- The final SSSOM row keeps the structured salt CAS as `CAS:2058-46-0` and
  does not export free-base oxytetracycline synonyms.
- The row-review manifest already confirmed the `CHEBI:31953` ontology row.
- The `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists`. The Hans80 anti-infective panel import makes
  the role plausible, but the record still needs source-backed role evidence
  instead of a name-pattern annotation.

## Completeness

- The active ChEBI term, salt CAS-RN, formula, structure, and final SSSOM
  identity row agree.

## Recommended Edits

- Major: in `data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml`,
  either replace `physicochemical_roles.SELECTIVE_AGENT` with cited
  experimental or recipe evidence, or remove the provisional role facet until
  source-backed role evidence is curated. Then rebuild the final SSSOM and
  rerun `scripts/validate_sssom_invariants.py`.
