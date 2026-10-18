# `data/ingredients/mapped/Imidazole.yaml`

## Verdict

Pass with minor issues. The CultureBotHT CAS-derived exact ChEBI identity, CAS
alias, formula, and final SSSOM row all describe imidazole, but the record is
missing InChI and SMILES structure fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Imidazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:14434` with
  `ontology_mapping.ontology_id: CHEBI:14434`, label `imidazole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `288-32-4` and formula `C3H4N2`; InChI and
  SMILES are not populated.

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

- OLS4 resolves `CHEBI:14434` as the active ChEBI class `imidazole`, with
  formula `C3H4N2` and `imidazole` as an exact IUPAC synonym.
- PubChem resolves CAS RN `288-32-4` to formula `C3H4N2` and an InChI for the
  imidazole structure.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Imidazole` to
  `CHEBI:14434` and exports only `CAS:288-32-4` in `other`.
- Minor: the existing ChEBI/PubChem enrichment copied only the formula even
  though the CAS RN resolves to a PubChem structure with InChI and SMILES.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, aggregate copy, and final SSSOM
  row are present and consistent.
- `chemical_properties.inchi` and `chemical_properties.smiles` should be
  backfilled from PubChem for parity with neighboring ChEBI small-molecule
  records.

## Recommended Edits

- Minor: backfill InChI and SMILES from PubChem, then rerun strict, term,
  round-trip, id-label, component, and SSSOM validation.
