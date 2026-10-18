# `data/ingredients/mapped/Pactamycin.yaml`

## Verdict

Needs curation; major. The upgraded exact MeSH identity for pactamycin passes,
but the `SELECTIVE_AGENT` role is only a provisional name-list prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Pactamycin.yaml`.
- Identifier and grounding: `identifier: mesh:D010142` with
  `ontology_mapping.ontology_id: mesh:D010142`, label `Pactamycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this MeSH primary record.
- A fresh OLS4 exact search for `Pactamycin` resolves `mesh:D010142`
  `Pactamycin`.
- The final SSSOM row was inspected directly and maps `MIM:Pactamycin`
  exactly to `mesh:D010142` with no `other` tokens.

## Evidence

- The kg-microbe placeholder was upgraded to `mesh:D010142` on a label-exact
  OLS match, and `mappings/ingredient_mappings_unknown_term_triage.tsv`
  classifies the final SSSOM row as a missing-prefix validator coverage issue,
  not a bad MeSH identifier.
- The final SSSOM row carries the MeSH exact identity and does not export any
  unsafe synonym text.
- The `SELECTIVE_AGENT` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from `infer_roles_from_name_lists`.

## Completeness

- The exact MeSH grounding is sufficient while CHEBI lacks a pactamycin primary
  in this record.
- Role evidence remains incomplete because no source-backed selective-agent
  assertion has been curated.

## Recommended Edits

- Major: in `data/ingredients/mapped/Pactamycin.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with cited source evidence that
  supports the selective-agent role for pactamycin, or remove the provisional
  role facet until source-backed role evidence is curated.
