# `data/ingredients/mapped/Isoniazid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived identity correctly maps Isoniazid CAS RN
`54-85-3` to isoniazide, and the ChEBI structure fields, exact systematic
synonym, CAS alias, and final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Isoniazid.yaml`.
- Identifier and grounding: `identifier: CHEBI:6030` with
  `ontology_mapping.ontology_id: CHEBI:6030`, label `isoniazide`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `54-85-3`, formula `C6H7N3O`, InChI
  `InChI=1S/C6H7N3O/c7-9-6(10)5-1-3-8-4-2-5/h1-4H,7H2,(H,9,10)`, and SMILES
  `NNC(=O)c1ccncc1`.

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

- OLS4 resolves `CHEBI:6030` as the active ChEBI class `isoniazide`, with CAS
  xref `54-85-3`, formula `C6H7N3O`, the same InChI and SMILES stored on the
  record, and the recorded systematic name as an exact ChEBI synonym.
- PubChem resolves CAS RN `54-85-3` to formula `C6H7N3O` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isoniazid` to
  `CHEBI:6030` and exports only the inspected exact synonym plus `CAS:54-85-3`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
