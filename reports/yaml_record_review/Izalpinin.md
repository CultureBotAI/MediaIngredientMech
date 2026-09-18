# `data/ingredients/mapped/Izalpinin.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback is internally consistent: no active ChEBI
term was found for Izalpinin, the CAS primary identifier matches CAS RN
`480-14-4`, the final SSSOM row uses the same registry CURIE, and the
`UNKNOWN_TERM` OAK/OLS row is expected for a CAS CURIE.

## Identity

- Reviewed record: `data/ingredients/mapped/Izalpinin.yaml`.
- Identifier and grounding: `identifier: cas:480-14-4` with
  `ontology_mapping.ontology_id: cas:480-14-4`, label `Izalpinin`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `480-14-4`, intentionally without ChEBI-derived
  formula, InChI, SMILES, or molecular-weight fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isovitalex.yaml data/ingredients/mapped/Isovitexin.yaml data/ingredients/mapped/Itaconate.yaml data/ingredients/mapped/Itaconic_Acid.yaml data/ingredients/mapped/Izalpinin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 3 CHEBI records.
  `Isovitalex` and `Izalpinin` were outside adapter scope because their primary
  identifiers are local `kgmicrobe.ingredient` and CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2120`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2120`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- A fresh exact ChEBI OLS4 search for `Izalpinin` returned zero hits, matching
  the CAS-fallback decision stored on the record.
- A fresh PubChem PUG lookup for CAS RN `480-14-4` returned 404, so there is no
  immediate PubChem CID/property enrichment to backfill.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Izalpinin` to
  `cas:480-14-4` and exports only `CAS:480-14-4` in `other`.
- The `UNKNOWN_TERM` OAK/OLS review row is triaged as an expected registry
  identifier because the `cas:480-14-4` object matches the YAML identifier and
  `chemical_properties.cas_rn`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, unknown-term triage row,
  and no newer exact ChEBI grounding for Izalpinin.

## Completeness

- The CAS primary identifier, CAS RN, aggregate copy, and final SSSOM row are
  present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
