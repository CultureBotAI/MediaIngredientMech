# `data/ingredients/mapped/Hypotaurine.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, structure fields, ChEBI
synonym, CAS alias, and final SSSOM row all describe hypotaurine.

## Identity

- Reviewed record: `data/ingredients/mapped/Hypotaurine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16668` with
  `ontology_mapping.ontology_id: CHEBI:16668`, label `hypotaurine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `300-84-5`, formula `C2H7NO2S`, InChI
  `InChI=1S/C2H7NO2S/c3-1-2-6(4)5/h1-3H2,(H,4,5)`, and SMILES `NCCS(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hygromycin.yaml data/ingredients/mapped/Hygromycin_A.yaml data/ingredients/mapped/Hygromycin_B.yaml data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml data/ingredients/mapped/Hypotaurine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hypotaurine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1520`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1520`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16668` as the active ChEBI class `hypotaurine` and
  lists `2-Aminoethanesulfinic acid` as an exact synonym.
- PubChem resolves CAS RN `300-84-5` to `Hypotaurine`, formula `C2H7NO2S`, and
  the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hypotaurine`
  to `CHEBI:16668` and exports only the inspected ChEBI synonym plus
  `CAS:300-84-5` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
