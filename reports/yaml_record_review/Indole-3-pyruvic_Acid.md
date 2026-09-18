# `data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml`

## Verdict

Needs curation. The direct CAS fallback still preserves the intended
indole-3-pyruvic acid identity, but ChEBI now has an exact active
`CHEBI:29750` term for CAS RN `392-12-1`, formula `C11H9NO3`, and the same
PubChem structure.

## Identity

- Reviewed record: `data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml`.
- Identifier and grounding: `identifier: cas:392-12-1` with
  `ontology_mapping.ontology_id: cas:392-12-1`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `392-12-1`; formula, InChI, SMILES, and
  PubChem CID are not populated.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indole-3-propionic_Acid.yaml data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml data/ingredients/mapped/Indole.yaml data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml data/ingredients/mapped/Indolicidin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was unavailable for this direct-CAS fallback:
  `linkml-term-validator` attempted to resolve `cas:392-12-1` in the CHEBI/OBO
  adapter and failed on the missing `rdfs_label_statement` table.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1555`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1555`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 now resolves `CHEBI:29750` as active
  `3-(indol-3-yl)pyruvic acid`, with CAS xref `392-12-1`, synonym
  `indole-3-pyruvic acid`, formula `C11H9NO3`, InChI
  matching the PubChem CAS lookup, and SMILES for the same compound.
- PubChem resolves CAS RN `392-12-1` to formula `C11H9NO3` and the same InChI
  as active `CHEBI:29750`.
- The final SSSOM still publishes only an exact local registry row from
  `MIM:Indole-3-pyruvic_Acid` to `cas:392-12-1`, with `CAS:392-12-1` in
  `other`.
- Major: the row-review manifest intentionally kept the CAS registry target
  when the review table still had `cas:0392-12-1` as an OAK/OLS `UNKNOWN_TERM`,
  but the current active ChEBI term means this is no longer a no-hit CAS
  fallback.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and stale CAS fallback
  unknown-term triage.

## Completeness

- The CAS fallback identity is internally consistent, but the record is no
  longer complete because an exact, CAS-backed ChEBI term now exists.

## Recommended Edits

- Major: promote the record to `CHEBI:29750`, set `ontology_label` to
  `3-(indol-3-yl)pyruvic acid`, grade the mapping from the current promotion
  evidence, keep `CAS:392-12-1` as an alias, backfill formula `C11H9NO3` plus
  PubChem/ChEBI structure fields, and rerun strict, term, round-trip,
  id-label, component, and SSSOM validation.
