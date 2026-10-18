# `data/ingredients/mapped/Piperacillin_Sodium_Salt.yaml`

## Verdict

Needs curation; major. The CultureBotHT CAS lookup maps to active `CHEBI:8233`
piperacillin sodium and the final SSSOM synonyms are exact for the salt, but
`SELECTIVE_AGENT` is still supported only by a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Piperacillin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:8233` with
  `ontology_mapping.ontology_id: CHEBI:8233`, label `piperacillin sodium`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8233` resolves `CHEBI:8233`
  `piperacillin sodium` and the exported systematic synonym on the same term.
- A fresh PubChem lookup for CAS `59703-84-3` resolves to Piperacillin Sodium.
- The final SSSOM row was inspected directly and maps
  `MIM:Piperacillin_Sodium_Salt` exactly to `CHEBI:8233`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `59703-84-3`, structured
  formula, SMILES, and InChI all describe piperacillin sodium rather than the
  free acid.
- `CAS_RN_LOOKUP` accurately records the row's CAS-to-CHEBI grounding method,
  while the final own-identifier SSSOM predicate is correctly
  `skos:exactMatch`.
- The final SSSOM `other` values contain only the long systematic CHEBI synonym
  and `CAS:59703-84-3`.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from a provisional curated name-pattern
  rule.

## Completeness

- The salt-specific CHEBI identity and final synonym surface are complete
  enough.
- Physicochemical-role evidence remains incomplete while the selective-agent
  role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Piperacillin_Sodium_Salt.yaml`, replace
  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence or remove
  the provisional role facet until it is curated.
