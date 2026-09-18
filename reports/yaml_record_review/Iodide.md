# `data/ingredients/mapped/Iodide.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
iodide.

## Identity

- Reviewed record: `data/ingredients/mapped/Iodide.yaml`.
- Identifier and grounding: `identifier: CHEBI:16382` with
  `ontology_mapping.ontology_id: CHEBI:16382`, label `iodide`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `I`, InChI `InChI=1S/HI/h1H/p-1`, SMILES
  `[I-]`, and molecular weight `126.904`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iodide.yaml data/ingredients/mapped/Iodonitrotetrazolium_Chloride.yaml data/ingredients/mapped/Irgasan.yaml data/ingredients/mapped/Irigenin.yaml data/ingredients/mapped/Iron.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1620`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1620`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16382` as the active ChEBI class `iodide`, with formula
  `I`, the same InChI and SMILES stored on the record, and no narrower salt,
  acid, or mixture scope.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Iodide` to
  `CHEBI:16382` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Metabolite_utilization` source occurrence without asserting any
  unsupported nutritional, chemical, or production role.
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
