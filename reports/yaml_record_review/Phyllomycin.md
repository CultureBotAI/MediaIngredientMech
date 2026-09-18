# `data/ingredients/mapped/Phyllomycin.yaml`

## Verdict

Needs curation; major. The local `kgmicrobe.compound:phyllomycin` placeholder
is intentionally retained because no exact external term or normalized local
duplicate was found, but `SELECTIVE_AGENT` is still supported only by a
provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Phyllomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:phyllomycin` with
  matching `ontology_mapping.ontology_id`, label `Phyllomycin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from
  `kg-microbe` metatraits unmapped placeholders.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The row-review and unknown-term triage tables were inspected directly; they
  record `kgmicrobe.compound:phyllomycin` as an expected local registry
  identifier pending curator promotion.
- A fresh OLS4 exact search for `phyllomycin` across CHEBI, NCIT, MICRO, BTO,
  FOODON, and MeSH returned no hits.
- The final SSSOM row was inspected directly and preserves the exact local
  `kgmicrobe.compound:phyllomycin` registry identity.

## Evidence

- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records no exact
  OLS candidate and no normalized local mapped duplicate for phyllomycin.
- The record notes the same no-hit review, and the final SSSOM row exports no
  `other` tokens.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from a provisional curated name-pattern
  rule.

## Completeness

- The local placeholder identity is complete enough while no exact external
  phyllomycin term exists in the searched ontologies.
- Physicochemical-role evidence remains incomplete while the selective-agent
  role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phyllomycin.yaml`, replace
  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence or remove
  the provisional role facet until it is curated.
