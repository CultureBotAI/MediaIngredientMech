# `data/ingredients/mapped/Hexanoate.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active `hexanoate` target,
structure fields, source-occurrence count, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hexanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17120` with
  `ontology_mapping.ontology_id: CHEBI:17120`, label `hexanoate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H11O2`, InChI
  `InChI=1S/C6H12O2/c1-2-3-4-5-6(7)8/h2-5H2,1H3,(H,7,8)/p-1`, SMILES
  `CCCCCC(=O)[O-]`, and molecular weight `115.152`.
- Source occurrences: eleven MicrobeDecoder occurrences from
  `BacDive_Metabolite_production` and `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hexanoate.yaml data/ingredients/mapped/Hexanol.yaml data/ingredients/mapped/Hippuric_Acid.yaml data/ingredients/mapped/Histamine.yaml data/ingredients/mapped/Hitachimycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:17120`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1428`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1428`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17120` as active `hexanoate`, the conjugate base of
  hexanoic acid.
- The MicrobeDecoder source label exact-matches the ChEBI label after
  case-normalization and does not introduce an unsupported hydrate, salt,
  stereochemical, mixture, catalog, or process boundary.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hexanoate` to
  `CHEBI:17120` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and MicrobeDecoder review row.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  source-occurrence statistics, and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
