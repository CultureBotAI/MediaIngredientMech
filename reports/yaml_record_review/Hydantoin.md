# `data/ingredients/mapped/Hydantoin.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, structure fields, ChEBI
synonym, CAS alias, and final SSSOM row all describe hydantoin.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydantoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27612` with
  `ontology_mapping.ontology_id: CHEBI:27612`, label `hydantoin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `461-72-3`, formula `C3H4N2O2`, InChI
  `InChI=1S/C3H4N2O2/c6-2-1-4-3(7)5-2/h1H2,(H2,4,5,6,7)`, and SMILES
  `O=C1CNC(=O)N1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hortesin.yaml data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml data/ingredients/mapped/Huperzine_A.yaml data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml data/ingredients/mapped/Hydantoin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydantoin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1448`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1448`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:27612` as the active ChEBI class `hydantoin` and lists
  `imidazolidine-2,4-dione` as an exact synonym.
- PubChem resolves CAS RN `461-72-3` to `Hydantoin`, formula `C3H4N2O2`, and
  the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hydantoin` to
  `CHEBI:27612` and exports only the inspected ChEBI synonym plus `CAS:461-72-3`
  in `other`.
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
