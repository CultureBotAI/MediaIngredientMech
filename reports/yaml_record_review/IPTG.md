# `data/ingredients/mapped/IPTG.yaml`

## Verdict

Pass with minor issues. The CultureMech residual label is grounded to active
`CHEBI:61448` via the `IPTG` synonym and the final SSSOM row is clean, but
the record has not yet received the standard ChEBI enrichment fields.

## Identity

- Reviewed record: `data/ingredients/mapped/IPTG.yaml`.
- Identifier and grounding: `identifier: CHEBI:61448` with
  `ontology_mapping.ontology_id: CHEBI:61448`, label
  `isopropyl beta-D-thiogalactopyranoside`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- The record has no `ingredient_type` or `chemical_properties` block.

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

- OLS4 resolves `CHEBI:61448` as the active ChEBI class
  `isopropyl beta-D-thiogalactopyranoside`, lists `IPTG` as a synonym, and
  exposes formula `C9H18O5S`, CAS xref `367-93-1`, InChI, and SMILES.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:IPTG` to
  `CHEBI:61448` with empty `other`.
- Minor: `ingredient_type` and ChEBI/PubChem structure fields are still
  missing, although OLS has enough structure metadata to backfill them.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and residual-grounding
  provenance already restored into `ontology_mapping.evidence`.

## Completeness

- The active ChEBI identifier, CultureMech source provenance, aggregate copy,
  and final SSSOM row are present and consistent.
- Standard `SINGLE_INGREDIENT` classification and chemical-structure
  enrichment remain to be copied onto the record.

## Recommended Edits

- Minor: backfill `ingredient_type: SINGLE_INGREDIENT` plus CAS RN
  `367-93-1`, formula `C9H18O5S`, InChI, SMILES, and molecular weight from
  ChEBI/PubChem, then rerun strict, term, round-trip, component, and SSSOM
  validation.
