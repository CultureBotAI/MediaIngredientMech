# `data/ingredients/mapped/Noformicin.yaml`

## Verdict

Needs curation - major. The `mesh:C005642` noformicin identity and final
SSSOM row pass, but `SELECTIVE_AGENT` is still backed only by a provisional
name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Noformicin.yaml`.
- Identifier and grounding: `identifier: mesh:C005642` with
  `ontology_mapping.ontology_id: mesh:C005642`, label `noformicin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH record.

## Evidence

- A fresh NLM MeSH lookup resolves `C005642` as active `noformicin`.
- The final SSSOM row maps `MIM:Noformicin` exactly to `mesh:C005642` and has
  no `other` tokens.
- The final SSSOM `validation_method` still carries the older
  `none|UNKNOWN_TERM|2026-07-07` stamp, but
  `mappings/ingredient_mappings_unknown_term_triage.tsv` already classifies
  this as a missing prefix-validator coverage issue and recommends keeping the
  mapping.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only the
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` evidence object.
  That name-pattern rule is explicitly provisional and does not independently
  support the selective-agent role.

## Completeness

- The active MeSH term, final exact row, and reviewed missing-prefix triage
  otherwise agree.
- The remaining consequential gap is the unsupported selective-agent role
  evidence.

## Recommended Edits

- Major: in `data/ingredients/mapped/Noformicin.yaml`, replace the
  `SELECTIVE_AGENT` role evidence with inspected source-backed evidence, or
  remove the role until that evidence exists.
