# `data/ingredients/mapped/Norfloxacin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:100246` norfloxacin identity,
structure block, reviewed synonym, and final SSSOM row pass, but
`SELECTIVE_AGENT` is still backed only by a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Norfloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:100246` with
  `ontology_mapping.ontology_id: CHEBI:100246`, label `norfloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:100246` as active `norfloxacin` with
  formula `C16H18FN3O3`, CAS `70458-96-7`, and the same InChI and SMILES as the
  record.
- The final SSSOM row maps `MIM:Norfloxacin` exactly to `CHEBI:100246`; its
  `other` values are the reviewed ChEBI synonym plus `CAS:70458-96-7`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only the
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` evidence object.
  That name-pattern rule is explicitly provisional and does not independently
  support the selective-agent role.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final
  SSSOM row otherwise agree.
- Empty occurrence statistics are expected for this CultureBotHT antimicrobial
  panel entry.

## Recommended Edits

- Major: in `data/ingredients/mapped/Norfloxacin.yaml`, replace the
  `SELECTIVE_AGENT` role evidence with inspected source-backed evidence, or
  remove the role until that evidence exists.
