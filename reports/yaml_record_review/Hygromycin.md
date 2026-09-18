# `data/ingredients/mapped/Hygromycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active generic `hygromycin` class,
source-occurrence count, empty synonym set, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hygromycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:24753` with
  `ontology_mapping.ontology_id: CHEBI:24753`, label `hygromycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Source occurrences: 24 MicrobeDecoder occurrences from
  `BacDive_Antibiotic_resistance`, `BacDive_Antibiotic_sensitivity`, and
  `BacDive_Metabolite_production`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hygromycin.yaml data/ingredients/mapped/Hygromycin_A.yaml data/ingredients/mapped/Hygromycin_B.yaml data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml data/ingredients/mapped/Hypotaurine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hygromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1520`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1520`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24753` as the active ChEBI class `hygromycin`.
- The MicrobeDecoder source label exact-matches the generic ChEBI label and
  does not specify hygromycin A or hygromycin B.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hygromycin` to
  `CHEBI:24753` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and MicrobeDecoder review
  row.

## Completeness

- The active ChEBI identifier, MicrobeDecoder occurrence count, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
