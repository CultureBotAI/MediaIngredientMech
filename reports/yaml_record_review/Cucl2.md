# `data/ingredients/mapped/Cucl2.yaml`

## Verdict

Pass. The anhydrous `CHEBI:49553` copper(II) chloride identity, structure,
174/174 count, CultureMech mineral role, rejected hydrate labels, and final
SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Cucl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:49553`,
  `ontology_mapping.ontology_id: CHEBI:49553`,
  `ontology_label: copper(II) chloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT` by equality of the record and ontology identifiers.
- Live OLS lookup by `CHEBI:49553` returns active `CHEBI:49553` labelled
  `copper(II) chloride` with the anhydrous synonyms retained by the record.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:49553` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cu_No32_X_3_H2o.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cu_No32_X_3_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the active `MIM:Cucl2` final SSSOM
  row, generated docs rows, and synonym-enrichment review rows showing hydrate
  labels were already represented and then rejected on the anhydrous record.
- The same searches found the distinct `Cucl2_X_6_H2o` local hydrate using
  `CHEBI:49553` only as a close parent with a registry identity row, not as a
  second active exact copper(II) chloride record.
- `mappings/culturemech_recipe_membership.tsv` contains 174 `CHEBI:49553`
  rows and a total occurrence sum of 174, matching `occurrence_statistics`
  `174/174`.
- The final SSSOM `other` tokens are anhydrous ChEBI synonyms for
  `CHEBI:49553` or the structured `CAS:7447-39-4` value from
  `chemical_properties.cas_rn`; rejected hydrate labels are filtered out.
- The `TRACE_ELEMENT` role is backed by the imported CultureMech role text
  rather than inferred from the compound name or ChEBI class.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, occurrence count, and generated docs rows are populated and
  agree.
- The anhydrous/hydrate boundary is explicit: hydrate labels are retained as
  `REJECTED_LABEL` provenance on this anhydrous record and modeled as their own
  local or exact hydrate records where applicable.

## Recommended Edits

- None.
