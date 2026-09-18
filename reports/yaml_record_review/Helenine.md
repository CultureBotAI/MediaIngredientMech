# `data/ingredients/mapped/Helenine.yaml`

## Verdict

Pass. The CAS-derived `alantolactone` ChEBI identity, CAS RN, ChEBI synonym,
structure fields, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Helenine.yaml`.
- Identifier and grounding: `identifier: CHEBI:2540` with
  `ontology_mapping.ontology_id: CHEBI:2540`, label `alantolactone`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `546-43-0`, formula `C15H20O2`, InChI
  `InChI=1S/C15H20O2/c1-9-5-4-6-15(3)8-13-11(7-12(9)15)10(2)14(16)17-13/h7,9,11,13H,2,4-6,8H2,1,3H3/t9-,11+,13+,15+/m0/s1`,
  and SMILES `[H][C@@]12C[C@@]3(C)CCC[C@H](C)C3=C[C@]1([H])C(=C)C(=O)O2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Helenine.yaml data/ingredients/mapped/Hemin_solution_see_below.yaml data/ingredients/mapped/Hemoglobin.yaml data/ingredients/mapped/Henicosane.yaml data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:2540`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1418`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1418`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:2540` as active `alantolactone`, and the record's
  `Helenine` preferred term is a ChEBI synonym for that exact ID.
- OLS4 lists the same IUPAC synonym exported by the final SSSOM `other` column.
- The final SSSOM also exports `CAS:546-43-0`, matching
  `chemical_properties.cas_rn`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, a row-review `CONFIRMED` decision, and
  no contradictory live curated record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, ChEBI synonym,
  final SSSOM row, and synchronized aggregate entry are present and consistent.
- No nutritional or physicochemical roles are asserted.

## Recommended Edits

- None.
