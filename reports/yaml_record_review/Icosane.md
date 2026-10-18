# `data/ingredients/mapped/Icosane.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI structure fields,
source-occurrence count, empty synonym export, and final SSSOM row all describe
icosane.

## Identity

- Reviewed record: `data/ingredients/mapped/Icosane.yaml`.
- Identifier and grounding: `identifier: CHEBI:43619` with
  `ontology_mapping.ontology_id: CHEBI:43619`, label `icosane`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C20H42`, InChI
  `InChI=1S/C20H42/c1-3-5-7-9-11-13-15-17-19-20-18-16-14-12-10-8-6-4-2/h3-20H2,1-2H3`,
  SMILES `CCCCCCCCCCCCCCCCCCCC`, and molecular weight `282.556`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hypoxanthine.yaml data/ingredients/mapped/IPTG.yaml data/ingredients/mapped/Icosane.yaml data/ingredients/mapped/Imidazole.yaml data/ingredients/mapped/Imipenem.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 5-file CHEBI batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1530`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1530`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:43619` as the active ChEBI class `icosane`, with formula
  `C20H42`, the same InChI and SMILES stored on the record, and the synonym
  `n-eicosane`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Icosane` to
  `CHEBI:43619` with empty `other`.
- The record carries the MicrobeDecoder import evidence and the single
  `BacDive_Metabolite_utilization` source occurrence without asserting any
  unsupported nutritional or physicochemical roles.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
