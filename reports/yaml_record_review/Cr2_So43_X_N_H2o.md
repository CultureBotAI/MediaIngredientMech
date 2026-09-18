# `data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`

## Verdict

Needs curation; major. The variable chromium(III) sulfate hydrate identity is
now correctly minted under `kgmicrobe.compound:cr2_so43_x_n_h2o`, keeps active
`CHEBI:53471` only as a narrow anhydrous parent, clears the stale anhydrous
chemical properties, and has a matching 3/3 CultureMech occurrence count. The
remaining gap is that `TRACE_ELEMENT` is supported solely by a provisional
in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:cr2_so43_x_n_h2o`,
  `ontology_mapping.ontology_id: CHEBI:53471`,
  `ontology_label: chromium(III) sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:53471` returns active `CHEBI:53471` labelled
  `chromium(III) sulfate`, the anhydrous parent for the variable hydrate label.
- `reports/hydrate_grounding.tsv` classifies the local registry identifier as
  `OK_LOCAL_REGISTRY_ID`, and the September 2026 curation history records that
  the stale anhydrous CAS RN, formula, and synonyms were removed.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cotarnine_Chloride.yaml data/ingredients/mapped/Coumarate.yaml data/ingredients/mapped/Cows_Milk.yaml data/ingredients/mapped/Cr1_Soil.yaml data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Coumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the only CHEBI-identified record in this batch.
  `Cotarnine_Chloride`, `Cows_Milk`, `Cr1_Soil`, and
  `Cr2_So43_X_N_H2o` were intentionally skipped because their CAS, FOODON,
  ENVO, and local `kgmicrobe.compound` identifiers are outside this
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
  `reports` found the two active `MIM:Cr2_So43_X_N_H2o` final SSSOM rows, the
  hydrate audit row, stale pre-mint row-review artifacts under `CHEBI:53471`,
  and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `kgmicrobe.compound:cr2_so43_x_n_h2o`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 3 rows for
  `kgmicrobe.compound:cr2_so43_x_n_h2o` whose occurrence weights sum to 3,
  matching the explicit 3/3 `occurrence_statistics`.
- The exact local final SSSOM row has no `other` tokens to review, and the
  narrow anhydrous parent row carries no `other` token.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `claude_in_session_curation` and is explicitly marked "Provisional
  in-session LLM role assignment; review recommended."

## Completeness

- The local variable-hydrate identity, narrow ChEBI parent, removal of stale
  anhydrous chemistry, SSSOM rows, aggregate copy, docs row, and occurrence
  count are populated and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`, either replace
  `nutritional_roles.TRACE_ELEMENT` with inspected evidence for chromium(III)
  sulfate hydrate as a trace element in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
