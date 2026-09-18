# `data/ingredients/mapped/Hydroquinone.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, structure fields, ChEBI
synonym, CAS alias, and final SSSOM row all describe hydroquinone.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroquinone.yaml`.
- Identifier and grounding: `identifier: CHEBI:17594` with
  `ontology_mapping.ontology_id: CHEBI:17594`, label `hydroquinone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `123-31-9`, formula `C6H6O2`, InChI
  `InChI=1S/C6H6O2/c7-5-1-2-6(8)4-3-5/h1-4,7-8H`, and SMILES
  `Oc1ccc(O)cc1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrogen_gas.yaml data/ingredients/mapped/Hydroquinone.yaml data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml data/ingredients/mapped/Hydroxy-l-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroquinone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1501`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1501`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17594` as the active ChEBI class `hydroquinone` and
  lists `Benzene-1,4-diol` as an exact synonym.
- PubChem resolves CAS RN `123-31-9` to `Hydroquinone`, formula `C6H6O2`, and
  the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydroquinone` to `CHEBI:17594` and exports only the inspected ChEBI
  synonym plus `CAS:123-31-9` in `other`.
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
