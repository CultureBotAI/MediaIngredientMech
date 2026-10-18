# `data/ingredients/mapped/Huperzine_A.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, stereospecific structure
fields, ChEBI synonym, CAS alias, and final SSSOM row all describe
huperzine A.

## Identity

- Reviewed record: `data/ingredients/mapped/Huperzine_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:78330` with
  `ontology_mapping.ontology_id: CHEBI:78330`, label `huperzine A`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `102518-79-6`, formula `C15H18N2O`, InChI
  `InChI=1S/C15H18N2O/c1-3-11-10-6-9(2)8-15(11,16)12-4-5-14(18)17-13(12)7-10/h3-6,10H,7-8,16H2,1-2H3,(H,17,18)/b11-3+/t10-,15+/m0/s1`,
  and SMILES `[H][C@@]12C=C(C)C[C@@](N)(/C1=C/C)c1ccc(=O)nc1C2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hortesin.yaml data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml data/ingredients/mapped/Huperzine_A.yaml data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml data/ingredients/mapped/Hydantoin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Huperzine_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1448`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1448`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:78330` as the active ChEBI class `huperzine A` and
  lists the stored stereospecific systematic name as an exact synonym.
- PubChem resolves CAS RN `102518-79-6` to `Huperzine A`, formula
  `C15H18N2O`, and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Huperzine_A` to `CHEBI:78330` and exports only the inspected ChEBI
  synonym plus `CAS:102518-79-6` in `other`.
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
