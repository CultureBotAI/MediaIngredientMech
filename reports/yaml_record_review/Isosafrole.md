# `data/ingredients/mapped/Isosafrole.yaml`

## Verdict

Pass. The CultureBotHT exact ChEBI identity, CAS RN, structure fields, empty
synonym list, and final SSSOM row all describe isosafrole.

## Identity

- Reviewed record: `data/ingredients/mapped/Isosafrole.yaml`.
- Identifier and grounding: `identifier: CHEBI:6054` with
  `ontology_mapping.ontology_id: CHEBI:6054`, label `Isosafrole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `120-58-1`, formula `C10H10O2`, InChI
  `InChI=1S/C10H10O2/c1-2-3-8-4-5-9-10(6-8)12-7-11-9/h2-6H,7H2,1H3/b3-2+`,
  and SMILES `C/C=C/c1ccc2c(c1)OCO2`.

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

- OLS4 resolves `CHEBI:6054` as the active ChEBI class `Isosafrole`, with CAS
  xref `120-58-1`, formula `C10H10O2`, and the same InChI and SMILES stored on
  the record.
- PubChem resolves CAS RN `120-58-1` to formula `C10H10O2` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isosafrole` to
  `CHEBI:6054` and exports only `CAS:120-58-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
