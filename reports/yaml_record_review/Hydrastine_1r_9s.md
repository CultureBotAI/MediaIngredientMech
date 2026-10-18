# `data/ingredients/mapped/Hydrastine_1r_9s.yaml`

## Verdict

Pass. The CAS-derived `CHEBI:69919` mapping, stereospecific structure fields,
CAS alias, and final SSSOM row all describe the same hydrastine structure.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrastine_1r_9s.yaml`.
- Identifier and grounding: `identifier: CHEBI:69919` with
  `ontology_mapping.ontology_id: CHEBI:69919`, label `Hydrastine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `118-08-1`, formula `C21H21NO6`, InChI
  `InChI=1S/C21H21NO6/c1-22-7-6-11-8-15-16(27-10-26-15)9-13(11)18(22)19-12-4-5-14(24-2)20(25-3)17(12)21(23)28-19/h4-5,8-9,18-19H,6-7,10H2,1-3H3/t18-,19+/m1/s1`,
  and SMILES
  `[H][C@]1([C@@]2([H])c3cc4c(cc3CCN2C)OCO4)OC(=O)c2c1ccc(OC)c2OC`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrastine_1r_9s.yaml data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/Hydrocarbon.yaml data/ingredients/mapped/Hydrogen_Peroxide.yaml data/ingredients/mapped/Hydrogen_Sulfide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrastine_1r_9s.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1454`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1454`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:69919` as the active ChEBI class `Hydrastine`.
- PubChem resolves CAS RN `118-08-1` to `(-)-Hydrastine`, formula
  `C21H21NO6`, and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydrastine_1r_9s` to `CHEBI:69919` and exports only `CAS:118-08-1` in
  `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, legacy MIM CURIE alias, docs projections, and
  synonym-enrichment review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
