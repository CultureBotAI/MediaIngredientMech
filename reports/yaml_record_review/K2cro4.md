# `data/ingredients/mapped/K2cro4.yaml`

## Verdict

Pass. The CultureMech exact match to ChEBI potassium chromate is active and
specific, and the CAS RN, formula, InChI, SMILES, kg-microbe synonyms,
occurrence count, and final SSSOM row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/K2cro4.yaml`.
- Identifier and grounding: `identifier: CHEBI:75249` with
  `ontology_mapping.ontology_id: CHEBI:75249`, label `potassium chromate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7789-00-6`, formula `CrO4.2K`, InChI
  `InChI=1S/Cr.2K.4O/q;2*+1;;;2*-1`, and SMILES
  `[K+].[K+].[O]=[Cr](=[O])([O-])[O-]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2cro4.yaml data/ingredients/mapped/K2hpo4.yaml data/ingredients/mapped/K2hpo4_X_3_H2o.yaml data/ingredients/mapped/K2s4o6.yaml data/ingredients/mapped/K2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2140`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2140`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:75249` as the active ChEBI class `potassium chromate`,
  with CAS xref `7789-00-6`, formula `CrO4.2K`, the same InChI and SMILES
  stored on the record, and the exported kg-microbe labels as synonyms.
- PubChem resolves CAS RN `7789-00-6` to the same potassium chromate InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:K2cro4` to
  `CHEBI:75249` and exports only specific potassium chromate labels plus
  `CAS:7789-00-6`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing OAK/OLS
  synonym-enrichment disposition for this record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, reviewed
  kg-microbe synonyms, aggregate copy, occurrence count, and final SSSOM row are
  present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
