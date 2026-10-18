# `data/ingredients/mapped/Malt_Extract.yaml`

## Verdict

Needs curation. The FoodOn malt-extract identity, undefined-mixture
classification, occurrence count, catalog variants, CAS value, and final SSSOM
row pass, but `CARBON_SOURCE` is still supported only by provisional
computational name-pattern evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Malt_Extract.yaml`.
- Identifier and grounding: `identifier: FOODON:03301056` with
  `ontology_mapping.ontology_id: FOODON:03301056`, label `malt extract`,
  source `FOODON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 274 total occurrences in 274 CultureMech recipes.
- CAS: `8002-48-0`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malonic_Acid` through `Malt_Extract_Agar_Oxoid`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  FOODON-primary record.

## Evidence

- EBI OLS4 resolves `FOODON:03301056` as active `malt extract`.
- The 2026-04-18 FoodOn promotion explicitly treated malt extract as a
  multi-component food extract rather than a ChEBI chemical.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Malt_Extract`
  to `FOODON:03301056`; its `other` field contains malt-extract catalog
  variants, `Malt extract powder`, and `CAS:8002-48-0`.

## Completeness

- The undefined-mixture identity and exported surface forms are aligned to the
  active FoodOn malt-extract term.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from a
  curated media-role name-pattern rule with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for malt extract as a
  media carbon source can be attached.
