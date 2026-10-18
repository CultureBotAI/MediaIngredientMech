# `data/ingredients/mapped/Irgasan.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived identity correctly maps Irgasan CAS RN
`3380-34-5` to triclosan, and the ChEBI structure fields, exact systematic
synonym, CAS alias, and final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Irgasan.yaml`.
- Identifier and grounding: `identifier: CHEBI:164200` with
  `ontology_mapping.ontology_id: CHEBI:164200`, label `triclosan`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `3380-34-5`, formula `C12H7Cl3O2`, InChI
  `InChI=1S/C12H7Cl3O2/c13-7-1-3-11(9(15)5-7)17-12-4-2-8(14)6-10(12)16/h1-6,16H`,
  and SMILES `Oc1cc(Cl)ccc1Oc1ccc(Cl)cc1Cl`.

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

- OLS4 resolves `CHEBI:164200` as the active ChEBI class `triclosan`, with CAS
  xref `3380-34-5`, formula `C12H7Cl3O2`, and the same InChI and SMILES stored
  on the record.
- PubChem resolves CAS RN `3380-34-5` to formula `C12H7Cl3O2` and the same
  InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Irgasan` to
  `CHEBI:164200` and exports only the inspected exact synonym plus
  `CAS:3380-34-5`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and synonym-enrichment
  review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
