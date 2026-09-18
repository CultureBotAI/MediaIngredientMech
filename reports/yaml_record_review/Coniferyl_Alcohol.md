# `data/ingredients/mapped/Coniferyl_Alcohol.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record is grounded to active `CHEBI:17745`
coniferol, the CAS RN, formula, InChI, SMILES, exact synonym, zero occurrence
count, final SSSOM row, and aggregate copy agree, and the `CAS_RN_LOOKUP` grade
accurately records the CAS-to-ChEBI mapping path.

## Identity

- Reviewed record: `data/ingredients/mapped/Coniferyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17745`,
  `ontology_mapping.ontology_id: CHEBI:17745`, `ontology_label: coniferol`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:17745` returns active `CHEBI:17745` labelled
  `coniferol` with related synonym `Coniferyl alcohol` and exact synonym
  `4-[(1E)-3-hydroxyprop-1-en-1-yl]-2-methoxyphenol`.
- The record stores CAS RN `458-35-5`, formula `C10H12O3`, and populated InChI
  and SMILES values for the exact ChEBI identity.

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
  `reports` found the active `MIM:Coniferyl_Alcohol` final SSSOM row, the
  OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:17745`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:17745` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The final SSSOM `other` column contains the exact ChEBI synonym and
  `CAS:458-35-5`, with no role-like, concentration-like, or salt-qualified
  residue.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No recommended edits.

## Recommended Edits

- None.
