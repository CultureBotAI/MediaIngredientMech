# `data/ingredients/mapped/Isepamicin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
isepamicin.

## Identity

- Reviewed record: `data/ingredients/mapped/Isepamicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:37951` with
  `ontology_mapping.ontology_id: CHEBI:37951`, label `isepamicin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C22H43N5O12`, InChI
  `InChI=1S/C22H43N5O12/c1-22(35)6-36-20(15(33)18(22)26-2)39-17-8(27-19(34)9(28)4-23)3-7(25)16(14(17)32)38-21-13(31)12(30)11(29)10(5-24)37-21/h7-18,20-21,26,28-33,35H,3-6,23-25H2,1-2H3,(H,27,34)/t7-,8+,9-,10+,11+,12-,13+,14-,15+,16+,17-,18+,20+,21+,22-/m0/s1`,
  SMILES
  `[H][C@]1(O[C@H]2[C@H](O)[C@@H](O[C@@]3([H])OC[C@](C)(O)[C@H](NC)[C@H]3O)[C@H](NC(=O)[C@@H](O)CN)C[C@@H]2N)O[C@H](CN)[C@@H](O)[C@H](O)[C@H]1O`,
  and molecular weight `569.609`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iron_Powder.yaml data/ingredients/mapped/Iron_Stock.yaml data/ingredients/mapped/Isepamicin.yaml data/ingredients/mapped/Isobutyl_Alcohol.yaml data/ingredients/mapped/Isobutyramide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Iron_Stock` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.ingredient` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1645`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1645`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:37951` as the active ChEBI class `isepamicin`, with
  formula `C22H43N5O12` and the same InChI and SMILES stored on the record.
- PubChem resolves the ChEBI CAS xref `58152-03-7` to formula `C22H43N5O12`
  and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isepamicin` to
  `CHEBI:37951` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Antibiotic_sensitivity` source occurrence without asserting an
  unsupported antibiotic role.
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
