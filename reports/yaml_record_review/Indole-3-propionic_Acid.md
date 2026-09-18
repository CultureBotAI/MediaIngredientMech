# `data/ingredients/mapped/Indole-3-propionic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup grounds the source label to active
`CHEBI:43580`, the CAS RN, structure fields, and final SSSOM row are
consistent, and the own-identifier exact SSSOM row follows the current CAS
lookup grading rule.

## Identity

- Reviewed record: `data/ingredients/mapped/Indole-3-propionic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:43580` with
  `ontology_mapping.ontology_id: CHEBI:43580`, label
  `3-(1H-indol-3-yl)propanoic acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `830-96-6`, formula `C11H11NO2`, InChI
  `InChI=1S/C11H11NO2/c13-11(14)6-5-8-7-12-10-4-2-1-3-9(8)10/h1-4,7,12H,5-6H2,(H,13,14)`,
  and SMILES `O=C(O)CCc1cnc2ccccc12`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indole-3-propionic_Acid.yaml data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml data/ingredients/mapped/Indole.yaml data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml data/ingredients/mapped/Indolicidin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI/OBO-compatible
  records; `Indole-3-pyruvic_Acid` was outside adapter scope because its
  primary identifier is a CAS registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1555`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1555`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:43580` as the active ChEBI class
  `3-(1H-indol-3-yl)propanoic acid`, with CAS xref `830-96-6`, formula
  `C11H11NO2`, and the same InChI and SMILES stored on the record.
- PubChem resolves CAS RN `830-96-6` to formula `C11H11NO2` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Indole-3-propionic_Acid` to `CHEBI:43580` and exports only
  `CAS:830-96-6` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
