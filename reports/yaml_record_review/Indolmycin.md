# `data/ingredients/mapped/Indolmycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
indolmycin.

## Identity

- Reviewed record: `data/ingredients/mapped/Indolmycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:79394` with
  `ontology_mapping.ontology_id: CHEBI:79394`, label `indolmycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C14H15N3O2`, InChI
  `InChI=1S/C14H15N3O2/c1-8(12-13(18)17-14(15-2)19-12)10-7-16-11-6-4-3-5-9(10)11/h3-8,12,16H,1-2H3,(H,15,17,18)/t8-,12+/m1/s1`,
  SMILES `[H][C@@]1([C@H](C)c2cnc3ccccc23)OC(NC)=NC1=O`, and molecular
  weight `257.293`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indolmycin.yaml data/ingredients/mapped/Indoxyl_Acetate.yaml data/ingredients/mapped/Inosine.yaml data/ingredients/mapped/Inositol.yaml data/ingredients/mapped/Inulin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1610`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1610`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:79394` as the active ChEBI class `indolmycin`, with
  formula `C14H15N3O2` and the same InChI and SMILES stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Indolmycin`
  to `CHEBI:79394` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Metabolite_production` source occurrence without asserting any
  unsupported production role.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and reviewed
  MicrobeDecoder promotion row.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
