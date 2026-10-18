# `data/ingredients/mapped/Indole-3-acetate.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active ChEBI anion structure,
source-occurrence count, empty synonym export, and final SSSOM row all describe
indole-3-acetate.

## Identity

- Reviewed record: `data/ingredients/mapped/Indole-3-acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30854` with
  `ontology_mapping.ontology_id: CHEBI:30854`, label `indole-3-acetate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C10H8NO2`, InChI
  `InChI=1S/C10H9NO2/c12-10(13)5-7-6-11-9-4-2-1-3-8(7)9/h1-4,6,11H,5H2,(H,12,13)/p-1`,
  SMILES `O=C([O-])Cc1cnc2ccccc12`, and molecular weight `174.179`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Impenum_Monohydrate.yaml data/ingredients/mapped/Indigocarmine.yaml data/ingredients/mapped/Indochrome.yaml data/ingredients/mapped/Indole-3-acetate.yaml data/ingredients/mapped/Indole-3-butyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4-file CHEBI/OBO subset;
  `Indochrome` was outside adapter scope because it uses a local
  `kgmicrobe.compound` identifier.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1545`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1545`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:30854` as the active ChEBI class
  `indole-3-acetate`, with formula `C10H8NO2` and the same InChI and SMILES
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Indole-3-acetate` to `CHEBI:30854` with empty `other`.
- The record carries the MicrobeDecoder import evidence and five
  `BacDive_Metabolite_production` source occurrences without asserting any
  unsupported production role.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and reviewed
  MicrobeDecoder promotion row.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
