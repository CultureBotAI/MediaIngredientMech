# `data/ingredients/mapped/Piericidin.yaml`

## Verdict

Pass. The local `kgmicrobe.compound:piericidin` placeholder is intentionally
retained for the unqualified piericidin family label, and the final SSSOM row
preserves only that local identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Piericidin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:piericidin` with
  matching `ontology_mapping.ontology_id`, label `Piericidin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from
  `kg-microbe` metatraits unmapped placeholders.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The row-review and unknown-term triage tables were inspected directly; they
  record `kgmicrobe.compound:piericidin` as an expected local registry
  identifier pending curator promotion.
- A fresh OLS4 search for `piericidin` across CHEBI, NCIT, MICRO, BTO, FOODON,
  and MeSH returned specific piericidin variants, not an unqualified piericidin
  family class.
- The final SSSOM row was inspected directly and preserves the exact local
  `kgmicrobe.compound:piericidin` registry identity.

## Evidence

- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  already rejected promotion to variant-specific CHEBI candidates such as
  `CHEBI:138511`, `CHEBI:207690`, and `CHEBI:199655` because the source label
  is family-level.
- The record notes the same manual candidate review, and the final SSSOM row
  exports no `other` tokens.
- The record carries no role, parent, component, or environment claims.

## Completeness

- The local placeholder identity is complete enough while no exact external
  piericidin family term exists in the searched ontologies.

## Recommended Edits

- None.
