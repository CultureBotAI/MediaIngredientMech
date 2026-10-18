# `data/ingredients/mapped/Oat_Flour_B-glucan.yaml`

## Verdict

Needs curation, major. The record for `Oat flour B-glucan` exact-maps to
`FOODON:03301312` `oat flour`, which drops the beta-glucan qualifier, and its
`CARBON_SOURCE` role is only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Oat_Flour_B-glucan.yaml`.
- Current grounding: `identifier: FOODON:03301312` with
  `ontology_mapping.ontology_id: FOODON:03301312`, label `oat flour`, source
  `FOODON`, `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- The record was promoted by `resolve_unmapped_v2` through a `stem-match` from
  the whole label `Oat flour B-glucan` to FOODON's `oat flour` food-product
  term.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `FOODON:03301312` as active `oat flour`, and
  the term has no synonyms that include beta-glucan.
- A fresh exact EBI OLS4 search for `Oat flour B-glucan` across indexed
  ontologies returned zero hits, so the current exact FOODON row is not backed
  by a synonym of the whole source label.
- The final SSSOM row maps `MIM:Oat_Flour_B-glucan` exactly to
  `FOODON:03301312`, which would make an oat beta-glucan ingredient
  substitutable with plain oat flour in downstream consumers.
- `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note.

## Completeness

- The current record lacks evidence distinguishing whole oat flour from an oat
  beta-glucan preparation, purified beta-glucan, or another narrower source
  material.
- The final SSSOM has no `other` tokens, so this review found no published
  synonym payload to repair.

## Recommended Edits

- In `data/ingredients/mapped/Oat_Flour_B-glucan.yaml`, re-curate the source
  label against the original CultureBotHT row and ontology candidates. Use a
  beta-glucan-specific term if one resolves exactly; otherwise mint a
  `kgmicrobe` fallback for the distinct ingredient and keep `oat flour` out of
  `skos:exactMatch`.
- Remove or replace `nutritional_roles.CARBON_SOURCE` unless source evidence
  supports the role for this exact ingredient.
- After curation, sync the aggregate record, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation,
  `validate_sssom_invariants.py`, `validate_id_label_correspondence.py`, and
  `check_flat_export_coverage.py`.
