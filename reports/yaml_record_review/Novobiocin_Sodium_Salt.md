# `data/ingredients/mapped/Novobiocin_Sodium_Salt.yaml`

## Verdict

Needs curation - major. The CAS-backed `CHEBI:31924` novobiocin sodium
identity, salt-specific structure block, and final SSSOM row pass, but
`SELECTIVE_AGENT` is still backed only by a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Novobiocin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:31924` with
  `ontology_mapping.ontology_id: CHEBI:31924`, label `Novobiocin sodium`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:31924` as active
  `Novobiocin sodium` with formula `C31H35N2O11.Na`, CAS `1476-53-5`, and the
  same salt-specific InChI and SMILES as the record.
- The final SSSOM row maps `MIM:Novobiocin_Sodium_Salt` exactly to
  `CHEBI:31924`; its only `other` value is `CAS:1476-53-5`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only the
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` evidence object.
  That name-pattern rule is explicitly provisional and does not independently
  support the selective-agent role.

## Completeness

- The active ChEBI term, CAS RN, salt-specific formula, salt-specific
  structure, CAS lookup grade, and final SSSOM row otherwise agree.
- Empty occurrence statistics are expected for this CultureBotHT antimicrobial
  panel entry.

## Recommended Edits

- Major: in `data/ingredients/mapped/Novobiocin_Sodium_Salt.yaml`, replace the
  `SELECTIVE_AGENT` role evidence with inspected source-backed evidence, or
  remove the role until that evidence exists.
