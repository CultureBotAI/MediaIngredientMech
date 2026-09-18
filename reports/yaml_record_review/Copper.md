# `data/ingredients/mapped/Copper.yaml`

## Verdict

Pass. The record uses the deliberate `kgmicrobe.compound:copper` fallback
introduced in #631 after removing the over-specific `CHEBI:28694` copper-atom
grounding; its 2/2 residual CultureMech count, final SSSOM row, aggregate copy,
and docs row agree, and no roles, components, or misleading synonyms are
present.

## Identity

- Reviewed record: `data/ingredients/mapped/Copper.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:copper`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:copper`,
  `ontology_label: Copper`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The September 2026 `fix_element_atom_overclaims` curation history changed the
  identifier from `CHEBI:28694` to `kgmicrobe.compound:copper` and records the
  reason: the source rows are TAP trace-element entries and CultureMech only
  recorded `KEGG:cu` with no charge or counter-ion.
- The record carries no CAS RN, structure, `ingredient_type`, roles, or
  synonyms, avoiding an over-specific copper atom or salt claim.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Congocidin.yaml data/ingredients/mapped/Coniferyl_Alcohol.yaml data/ingredients/mapped/Coniferyl_Aldehyde.yaml data/ingredients/mapped/Cooked_Meat_Medium.yaml data/ingredients/mapped/Copper.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Coniferyl_Alcohol.yaml data/ingredients/mapped/Coniferyl_Aldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-identified records in this batch. `Congocidin`,
  `Cooked_Meat_Medium`, and `Copper` were intentionally skipped because their
  local `kgmicrobe.compound` and FOODON identifiers are outside this
  CHEBI-focused LinkML term-validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active `MIM:Copper` final SSSOM row, the
  `culturemech_residual_groundings.tsv` 2/2 source row, the #631 curation
  history, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `kgmicrobe.compound:copper`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no local fallback rows;
  the 2/2 count is instead backed by `mappings/culturemech_residual_groundings.tsv`.
- The final SSSOM row has no `other` tokens to review. Its comment column
  documents the removed ChEBI atom grounding and the local fallback.

## Completeness

- The local fallback identifier, residual occurrence count, SSSOM row, aggregate
  copy, docs row, and lack of over-specific chemistry are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
