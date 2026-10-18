# `data/ingredients/mapped/Hexane.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active `hexane` target, structure
fields, source-occurrence count, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hexane.yaml`.
- Identifier and grounding: `identifier: CHEBI:29021` with
  `ontology_mapping.ontology_id: CHEBI:29021`, label `hexane`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H14`, InChI
  `InChI=1S/C6H14/c1-3-5-6-4-2/h3-6H2,1-2H3`, SMILES `CCCCCC`, and molecular
  weight `86.178`.
- Source occurrences: one MicrobeDecoder occurrence from
  `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hesperidin.yaml data/ingredients/mapped/Hexachlorocyclo-hexane.yaml data/ingredients/mapped/Hexadecane.yaml data/ingredients/mapped/Hexadecanoate.yaml data/ingredients/mapped/Hexane.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:29021`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1424`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1424`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:29021` as active `hexane`.
- The MicrobeDecoder source label exact-matches the ChEBI label after
  case-normalization and does not introduce an unsupported hydrate, salt,
  stereochemical, mixture, catalog, or process boundary.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hexane` to
  `CHEBI:29021` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and MicrobeDecoder review row.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  source-occurrence statistics, and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
