# `data/ingredients/mapped/Cotarnine_Chloride.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback keeps `cas:10018-19-6` as the primary
identity while mapping narrowly to active `NCIT:C79997` Cotarnine Chloride; the
CAS RN, 0/0 occurrence count, registry SSSOM companion rows, aggregate copy, and
docs row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cotarnine_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:10018-19-6`,
  `ontology_mapping.ontology_id: NCIT:C79997`,
  `ontology_label: Cotarnine Chloride`, `ontology_source: NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `NCIT:C79997` returns active `NCIT:C79997` labelled
  `Cotarnine Chloride`.
- The CAS-primary pattern is intentional for this no-ChEBI small molecule: the
  final SSSOM contains the NCIT parent row plus exact `cas:10018-19-6` and
  `kgmicrobe.compound:cotarnine_chloride` registry rows.

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
  `reports` found the three active `MIM:Cotarnine_Chloride` final SSSOM rows,
  the unknown-term triage rows marking NCIT/CAS/kg-microbe as expected in this
  pattern, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `cas:10018-19-6` or the `NCIT:C79997` parent.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:10018-19-6` or
  `NCIT:C79997` rows, matching the explicit 0/0 `occurrence_statistics`.
- The only final SSSOM `other` token is expected: `CAS:10018-19-6` on the exact
  registry companion rows.

## Completeness

- The CAS primary identity, NCIT parent, registry companion rows, CAS RN, SSSOM
  rows, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No recommended edits.

## Recommended Edits

- None.
