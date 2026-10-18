# `data/ingredients/mapped/Homovanillic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, stored structure fields,
ChEBI synonym, CAS alias, and final SSSOM row all describe homovanillic acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Homovanillic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:545959` with
  `ontology_mapping.ontology_id: CHEBI:545959`, label `homovanillic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `306-08-1`, formula `C9H10O4`, InChI
  `InChI=1S/C9H10O4/c1-13-8-4-6(5-9(11)12)2-3-7(8)10/h2-4,10H,5H2,1H3,(H,11,12)`,
  and SMILES `COc1cc(CC(=O)O)ccc1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Homovanillic_Acid.yaml data/ingredients/mapped/Homovanillyl_Alcohol.yaml data/ingredients/mapped/Hopanoid.yaml data/ingredients/mapped/Horse_Serum.yaml data/ingredients/mapped/Horse_blood.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Homovanillic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1438`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1438`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:545959` as the active ChEBI class
  `homovanillic acid` and lists
  `2-(4-hydroxy-3-methoxyphenyl)acetic acid` as an exact synonym.
- PubChem resolves CAS RN `306-08-1` to `Homovanillic Acid`, formula
  `C9H10O4`, and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Homovanillic_Acid` to `CHEBI:545959` and exports only the inspected
  ChEBI synonym plus `CAS:306-08-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and the OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
