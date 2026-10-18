# `data/ingredients/mapped/Isovitexin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
isovitexin.

## Identity

- Reviewed record: `data/ingredients/mapped/Isovitexin.yaml`.
- Identifier and grounding: `identifier: CHEBI:18330` with
  `ontology_mapping.ontology_id: CHEBI:18330`, label `isovitexin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C21H20O10`, InChI
  `InChI=1S/C21H20O10/c22-7-14-17(26)19(28)20(29)21(31-14)16-11(25)6-13-15(18(16)27)10(24)5-12(30-13)8-1-3-9(23)4-2-8/h1-6,14,17,19-23,25-29H,7H2/t14-,17-,19+,20-,21+/m1/s1`,
  SMILES
  `O=c1cc(-c2ccc(O)cc2)oc2cc(O)c([C@@H]3O[C@H](CO)[C@@H](O)[C@H](O)[C@H]3O)c(O)c12`,
  and molecular weight `432.381`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isovitalex.yaml data/ingredients/mapped/Isovitexin.yaml data/ingredients/mapped/Itaconate.yaml data/ingredients/mapped/Itaconic_Acid.yaml data/ingredients/mapped/Izalpinin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 3 CHEBI records.
  `Isovitalex` and `Izalpinin` were outside adapter scope because their primary
  identifiers are local `kgmicrobe.ingredient` and CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2120`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2120`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:18330` as the active ChEBI class `isovitexin`, with
  formula `C21H20O10` and the same InChI and SMILES stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isovitexin` to
  `CHEBI:18330` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Metabolite_utilization` source occurrence without asserting any
  unsupported utilization role.
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
