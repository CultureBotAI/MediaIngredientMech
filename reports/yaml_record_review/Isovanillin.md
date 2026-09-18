# `data/ingredients/mapped/Isovanillin.yaml`

## Verdict

Pass. The CultureBotHT exact ChEBI identity, CAS RN, structure fields, exact
systematic synonym, and final SSSOM row all describe isovanillin.

## Identity

- Reviewed record: `data/ingredients/mapped/Isovanillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:193161` with
  `ontology_mapping.ontology_id: CHEBI:193161`, label `isovanillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `621-59-0`, formula `C8H8O3`, InChI
  `InChI=1S/C8H8O3/c1-11-8-3-2-6(5-9)4-7(8)10/h2-5,10H,1H3`, and SMILES
  `[H]C(=O)c1ccc(OC)c(O)c1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isopropyl_Alcohol.yaml data/ingredients/mapped/Isosafrole.yaml data/ingredients/mapped/Isovalerate.yaml data/ingredients/mapped/Isovaleric_Acid.yaml data/ingredients/mapped/Isovanillin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2110`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2110`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:193161` as the active ChEBI class `isovanillin`, with
  CAS xref `621-59-0`, formula `C8H8O3`, the same InChI and SMILES stored on
  the record, and the recorded systematic name as an exact ChEBI synonym.
- PubChem resolves CAS RN `621-59-0` to formula `C8H8O3` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isovanillin` to
  `CHEBI:193161` and exports only the inspected exact synonym plus
  `CAS:621-59-0`.
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
