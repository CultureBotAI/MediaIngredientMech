# `data/ingredients/mapped/Isobutyrate.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active isobutyrate structure
fields, source-occurrence count, empty synonym export, and final SSSOM row all
describe the 2-methylpropanoate anion.

## Identity

- Reviewed record: `data/ingredients/mapped/Isobutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:48944` with
  `ontology_mapping.ontology_id: CHEBI:48944`, label `isobutyrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C4H7O2`, InChI
  `InChI=1S/C4H8O2/c1-3(2)4(5)6/h3H,1-2H3,(H,5,6)/p-1`, SMILES
  `CC(C)C(=O)[O-]`, and molecular weight `87.098`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isobutyrate.yaml data/ingredients/mapped/Isobutyric_Acid.yaml data/ingredients/mapped/Isocaproate.yaml data/ingredients/mapped/Isocitrate.yaml data/ingredients/mapped/Isoliquiritigenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2050`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2050`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:48944` as the active ChEBI class `isobutyrate`, with
  formula `C4H7O2` and the same InChI and SMILES stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isobutyrate`
  to `CHEBI:48944` with empty `other`.
- The record carries the MicrobeDecoder import evidence and 12
  `BacDive_Metabolite_production` or `BacDive_Metabolite_utilization` source
  occurrences without asserting any unsupported production or utilization role.
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
