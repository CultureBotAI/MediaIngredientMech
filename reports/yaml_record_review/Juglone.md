# `data/ingredients/mapped/Juglone.yaml`

## Verdict

Pass. The CultureBotHT import maps the record to the active ChEBI juglone term,
and the CAS RN, formula, InChI, SMILES, exact synonym, and final SSSOM row all
agree with that identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Juglone.yaml`.
- Identifier and grounding: `identifier: CHEBI:15794` with
  `ontology_mapping.ontology_id: CHEBI:15794`, label `juglone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `481-39-0`, formula `C10H6O3`, InChI
  `InChI=1S/C10H6O3/c11-7-4-5-9(13)10-6(7)2-1-3-8(10)12/h1-5,12H`, and SMILES
  `O=C1C=CC(=O)c2c(O)cccc21`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Jasmonic_Acid.yaml data/ingredients/mapped/Juglone.yaml data/ingredients/mapped/K-acetate.yaml data/ingredients/mapped/K-phosphate_Buffer.yaml data/ingredients/mapped/K2co3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for this CHEBI record.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2130`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2130`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:15794` as the active ChEBI class `juglone`, with CAS xref
  `481-39-0`, formula `C10H6O3`, the same InChI and SMILES stored on the
  record, and `5-Hydroxy-1,4-naphthoquinone` as an exact synonym.
- PubChem resolves CAS RN `481-39-0` to formula `C10H6O3` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Juglone` to
  `CHEBI:15794` and exports only `5-Hydroxy-1,4-naphthoquinone` plus
  `CAS:481-39-0`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing OAK/OLS
  confirmation for this record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
