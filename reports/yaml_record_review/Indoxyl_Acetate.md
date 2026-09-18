# `data/ingredients/mapped/Indoxyl_Acetate.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
Indoxyl acetate.

## Identity

- Reviewed record: `data/ingredients/mapped/Indoxyl_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:169991` with
  `ontology_mapping.ontology_id: CHEBI:169991`, label `Indoxyl acetate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C10H9NO2`, InChI
  `InChI=1S/C10H9NO2/c1-7(12)13-10-6-11-9-5-3-2-4-8(9)10/h2-6,11H,1H3`,
  SMILES `CC(=O)Oc1cnc2ccccc12`, and molecular weight `175.187`.

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

- OLS4 resolves `CHEBI:169991` as the active ChEBI class `Indoxyl acetate`,
  with formula `C10H9NO2` and the same InChI and SMILES stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Indoxyl_Acetate` to `CHEBI:169991` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Metabolite_utilization` source occurrence without asserting any
  unsupported nutritional role.
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
