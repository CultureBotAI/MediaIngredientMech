# `data/ingredients/mapped/Indole-3-butyric_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived exact ChEBI mapping, structure fields,
ChEBI synonym, CAS alias, and final SSSOM row all describe
indole-3-butyric acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Indole-3-butyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:33070` with
  `ontology_mapping.ontology_id: CHEBI:33070`, label
  `indole-3-butyric acid`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `133-32-4`, formula `C12H13NO2`, InChI
  `InChI=1S/C12H13NO2/c14-12(15)7-3-4-9-8-13-11-6-2-1-5-10(9)11/h1-2,5-6,8,13H,3-4,7H2,(H,14,15)`,
  and SMILES `O=C(O)CCCc1cnc2ccccc12`.

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

- OLS4 resolves `CHEBI:33070` as the active ChEBI class
  `indole-3-butyric acid`, with CAS xref `133-32-4`, formula `C12H13NO2`,
  the same InChI and SMILES stored on the record, and
  `4-(1H-indol-3-yl)butanoic acid` as an exact synonym.
- PubChem resolves CAS RN `133-32-4` to formula `C12H13NO2` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Indole-3-butyric_Acid` to `CHEBI:33070` and exports only the inspected
  ChEBI synonym plus `CAS:133-32-4` in `other`.
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
