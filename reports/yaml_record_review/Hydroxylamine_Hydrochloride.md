# `data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, hydrochloride salt structure,
raw abbreviation, CAS alias, and final SSSOM row are internally consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:5807` with
  `ontology_mapping.ontology_id: CHEBI:5807`, label
  `Hydroxylamine hydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `5470-11-1`, formula `H3NO.HCl`, InChI
  `InChI=1S/ClH.H3NO/c;1-2/h1H;2H,1H2`, and SMILES `Cl.NO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydroxyacetophenone.yaml data/ingredients/mapped/Hydroxyethylcellulose.yaml data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml data/ingredients/mapped/Hydroxystreptomycin.yaml data/ingredients/mapped/Hydroxyurea.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1510`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1510`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:5807` as the active ChEBI class
  `Hydroxylamine hydrochloride`.
- PubChem resolves CAS RN `5470-11-1` to the same hydrochloride salt formula
  and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydroxylamine_Hydrochloride` to `CHEBI:5807` and exports the raw
  abbreviation `hydroxylamine hcl` plus `CAS:5470-11-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and synonym-enrichment
  review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, raw
  abbreviation, aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
