# `data/ingredients/mapped/Pamamycin.yaml`

## Verdict

Needs curation; major. The upgraded exact MeSH identity for generic pamamycin
passes, but the `SELECTIVE_AGENT` role is only a provisional name-list
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Pamamycin.yaml`.
- Identifier and grounding: `identifier: mesh:C024500` with
  `ontology_mapping.ontology_id: mesh:C024500`, label `pamamycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this MeSH primary record.
- A fresh OLS4 exact search for `Pamamycin` resolves `mesh:C024500`
  `pamamycin`.
- The final SSSOM row was inspected directly and maps `MIM:Pamamycin` exactly
  to `mesh:C024500` with no `other` tokens.

## Evidence

- The kg-microbe placeholder was upgraded to `mesh:C024500` on a label-exact
  OLS match, and fresh OLS4 still resolves the generic label to that MeSH
  class.
- Fresh OLS4 also contains several narrower ChEBI entries such as
  `Pamamycin-607`, `Pamamycin-593`, and `Pamamycin-649B`; those are specific
  family members rather than exact replacements for a generic `Pamamycin`
  record.
- The final SSSOM row carries the MeSH exact identity and does not export any
  unsafe synonym text.
- The `SELECTIVE_AGENT` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from `infer_roles_from_name_lists`.

## Completeness

- The exact MeSH grounding is sufficient for the generic pamamycin subject
  while no exact ChEBI family-level term is curated.
- Role evidence remains incomplete because no source-backed selective-agent
  assertion has been curated.

## Recommended Edits

- Major: in `data/ingredients/mapped/Pamamycin.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with cited source evidence that
  supports the selective-agent role for pamamycin, or remove the provisional
  role facet until source-backed role evidence is curated.
