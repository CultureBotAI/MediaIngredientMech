# `data/ingredients/mapped/Jasmonic_Acid.yaml`

## Verdict

Pass. The CultureBotHT import maps the record to the active ChEBI jasmonic acid
term, the exact IUPAC synonym, CAS RN, formula, InChI, SMILES, and final SSSOM
row all describe the same structure.

## Identity

- Reviewed record: `data/ingredients/mapped/Jasmonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18292` with
  `ontology_mapping.ontology_id: CHEBI:18292`, label `jasmonic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `6894-38-8`, formula `C12H18O3`, InChI
  `InChI=1S/C12H18O3/c1-2-3-4-5-10-9(8-12(14)15)6-7-11(10)13/h3-4,9-10H,2,5-8H2,1H3,(H,14,15)/b4-3-/t9-,10-/m1/s1`,
  and SMILES `CC/C=CC[C@H]1C(=O)CC[C@@H]1CC(=O)O`.

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

- OLS4 resolves `CHEBI:18292` as the active ChEBI class `jasmonic acid`, with
  CAS xref `6894-38-8`, formula `C12H18O3`, the same InChI and SMILES stored on
  the record, and the stored IUPAC synonym
  `{(1R,2R)-3-oxo-2-[(2Z)-pent-2-en-1-yl]cyclopentyl}acetic acid`.
- PubChem resolves CAS RN `6894-38-8` to formula `C12H18O3` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Jasmonic_Acid` to `CHEBI:18292` and exports only the reviewed IUPAC
  synonym plus `CAS:6894-38-8`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing OAK/OLS
  confirmation for this record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
