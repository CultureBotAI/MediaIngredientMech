# `data/ingredients/mapped/K2co3.yaml`

## Verdict

Pass. The CultureMech exact match to ChEBI potassium carbonate is active and
specific, the CAS RN, formula, InChI, SMILES, kg-microbe synonyms, occurrence
count, and final SSSOM row all agree, and the raw CultureMech `Properties:`
payload is filtered from the published SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/K2co3.yaml`.
- Identifier and grounding: `identifier: CHEBI:131526` with
  `ontology_mapping.ontology_id: CHEBI:131526`, label `potassium carbonate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `584-08-7`, formula `CO3.2K`, InChI
  `InChI=1S/CH2O3.2K/c2-1(3)4;;/h(H2,2,3,4);;/q;2*+1/p-2`, and SMILES
  `O=C([O-])[O-].[K+].[K+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Jasmonic_Acid.yaml data/ingredients/mapped/Juglone.yaml data/ingredients/mapped/K-acetate.yaml data/ingredients/mapped/K-phosphate_Buffer.yaml data/ingredients/mapped/K2co3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for this CHEBI record.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2130`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2130`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:131526` as the active ChEBI class
  `potassium carbonate`, with CAS xref `584-08-7`, formula `CO3.2K`, the same
  InChI and SMILES stored on the record, and `Carbonate of potash`,
  `Carbonic acid, dipotassium salt`, `K2CO3`, `Kaliumcarbonat`, and
  `dipotassium carbonate` as synonyms.
- PubChem resolves CAS RN `584-08-7` to the same potassium carbonate InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:K2co3` to
  `CHEBI:131526` and exports only specific potassium carbonate labels plus
  `CAS:584-08-7`; the raw CultureMech `Properties:` string is correctly
  filtered.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, current 10-recipe
  CultureMech membership table, and existing OAK/OLS confirmation for this
  record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, reviewed
  kg-microbe synonyms, aggregate copy, occurrence count, and final SSSOM row are
  present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
