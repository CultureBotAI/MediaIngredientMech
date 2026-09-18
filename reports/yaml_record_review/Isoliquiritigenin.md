# `data/ingredients/mapped/Isoliquiritigenin.yaml`

## Verdict

Pass. The CultureBotHT exact ChEBI identity, CAS RN, structure fields, exact
systematic synonym, and final SSSOM row all describe isoliquiritigenin.

## Identity

- Reviewed record: `data/ingredients/mapped/Isoliquiritigenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:310312` with
  `ontology_mapping.ontology_id: CHEBI:310312`, label `isoliquiritigenin`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `961-29-5`, formula `C15H12O4`, InChI
  `InChI=1S/C15H12O4/c16-11-4-1-10(2-5-11)3-8-14(18)13-7-6-12(17)9-15(13)19/h1-9,16-17,19H/b8-3+`,
  and SMILES `O=C(/C=C/c1ccc(O)cc1)c1ccc(O)cc1O`.

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

- OLS4 resolves `CHEBI:310312` as the active ChEBI class
  `isoliquiritigenin`, with CAS xref `961-29-5`, formula `C15H12O4`, the same
  InChI and SMILES stored on the record, and the recorded systematic synonym as
  an exact ChEBI synonym.
- PubChem resolves CAS RN `961-29-5` to formula `C15H12O4` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isoliquiritigenin` to `CHEBI:310312` and exports only the inspected
  exact synonym plus `CAS:961-29-5`.
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
