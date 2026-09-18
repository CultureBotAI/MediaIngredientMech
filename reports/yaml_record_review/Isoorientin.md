# `data/ingredients/mapped/Isoorientin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
isoorientin.

## Identity

- Reviewed record: `data/ingredients/mapped/Isoorientin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17965` with
  `ontology_mapping.ontology_id: CHEBI:17965`, label `isoorientin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C21H20O11`, InChI
  `InChI=1S/C21H20O11/c22-6-14-17(27)19(29)20(30)21(32-14)16-11(26)5-13-15(18(16)28)10(25)4-12(31-13)7-1-2-8(23)9(24)3-7/h1-5,14,17,19-24,26-30H,6H2/t14-,17-,19+,20-,21+/m1/s1`,
  SMILES
  `O=c1cc(-c2ccc(O)c(O)c2)oc2cc(O)c([C@@H]3O[C@H](CO)[C@@H](O)[C@H](O)[C@H]3O)c(O)c12`,
  and molecular weight `448.38`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isomaltose.yaml data/ingredients/mapped/Isoniazid.yaml data/ingredients/mapped/Isoorientin.yaml data/ingredients/mapped/Isophthalate.yaml data/ingredients/mapped/Isopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Isopropionate` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.compound` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2100`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2100`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17965` as the active ChEBI class `isoorientin`, with
  formula `C21H20O11` and the same InChI and SMILES stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isoorientin`
  to `CHEBI:17965` with empty `other`.
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
