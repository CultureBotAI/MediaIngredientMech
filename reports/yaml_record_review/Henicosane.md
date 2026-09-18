# `data/ingredients/mapped/Henicosane.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active `henicosane` target,
structure fields, source-occurrence count, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Henicosane.yaml`.
- Identifier and grounding: `identifier: CHEBI:32931` with
  `ontology_mapping.ontology_id: CHEBI:32931`, label `henicosane`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C21H44`, InChI
  `InChI=1S/C21H44/c1-3-5-7-9-11-13-15-17-19-21-20-18-16-14-12-10-8-6-4-2/h3-21H2,1-2H3`,
  SMILES `CCCCCCCCCCCCCCCCCCCCC`, and molecular weight `296.583`.
- Source occurrences: two MicrobeDecoder occurrences from
  `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Helenine.yaml data/ingredients/mapped/Hemin_solution_see_below.yaml data/ingredients/mapped/Hemoglobin.yaml data/ingredients/mapped/Henicosane.yaml data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:32931`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1418`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1418`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:32931` as active `henicosane`.
- The MicrobeDecoder source label exact-matches the ChEBI label after
  case-normalization and does not introduce a salt, hydrate, stereochemical,
  mixture, catalog, or process boundary.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Henicosane` to
  `CHEBI:32931` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, the MicrobeDecoder review row, and no
  contradictory live curated record.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  occurrence statistics, and final SSSOM row are present and consistent.
- No unsupported nutritional, physicochemical, or community roles are asserted.

## Recommended Edits

- None.
