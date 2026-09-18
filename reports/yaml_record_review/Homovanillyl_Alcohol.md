# `data/ingredients/mapped/Homovanillyl_Alcohol.yaml`

## Verdict

Pass. The CAS-derived `CHEBI:173769` mapping, structure fields, curated ChEBI
synonym, CAS alias, and final SSSOM row all describe homovanillyl alcohol.

## Identity

- Reviewed record: `data/ingredients/mapped/Homovanillyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:173769` with
  `ontology_mapping.ontology_id: CHEBI:173769`, label
  `(4-Hydroxy-3-methoxyphenyl)ethanol`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `2380-78-1`, formula `C9H12O3`, InChI
  `InChI=1S/C9H12O3/c1-12-9-6-7(4-5-10)2-3-8(9)11/h2-3,6,10-11H,4-5H2,1H3`,
  and SMILES `COc1cc(CCO)ccc1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Homovanillic_Acid.yaml data/ingredients/mapped/Homovanillyl_Alcohol.yaml data/ingredients/mapped/Hopanoid.yaml data/ingredients/mapped/Horse_Serum.yaml data/ingredients/mapped/Horse_blood.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Homovanillyl_Alcohol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1438`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1438`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:173769` as the active ChEBI class
  `(4-Hydroxy-3-methoxyphenyl)ethanol` and lists
  `4-(2-hydroxyethyl)-2-methoxyphenol` as an exact synonym.
- PubChem resolves CAS RN `2380-78-1` to `Homovanillyl alcohol`, formula
  `C9H12O3`, and the same InChI stored on the record.
- The row-review surfaces already record the older OAK/OLS
  `SYNONYM_ENRICH` candidate as `ALREADY_REPRESENTED`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Homovanillyl_Alcohol` to `CHEBI:173769` and exports only the inspected
  ChEBI synonym plus `CAS:2380-78-1` in `other`.
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
