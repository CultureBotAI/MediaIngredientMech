# `data/ingredients/mapped/Penicillin.yaml`

## Verdict

Pass. The CultureMech import maps the broad `Penicillin` ingredient exactly to
active `CHEBI:17334` penicillin, and the final SSSOM synonym is a real
same-class synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Penicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17334` with
  `ontology_mapping.ontology_id: CHEBI:17334`, label `penicillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 CultureMech occurrences across 5 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:17334` resolves `CHEBI:17334`
  `penicillin`.
- The final SSSOM row was inspected directly and maps `MIM:Penicillin` exactly
  to `CHEBI:17334`.

## Evidence

- The CHEBI primary identifier, wildcard formula, and wildcard SMILES all
  describe the generic penicillin class.
- The `SELECTIVE_AGENT` role is backed by imported CultureMech database
  evidence whose original role text was `Selective Agent`.
- `penicillins` is an OLS4 exact synonym of `CHEBI:17334`, and it is the only
  value exported in final SSSOM `other`.

## Completeness

- No consequential gap was found for this broad, class-level CHEBI mapping.

## Recommended Edits

- None.
