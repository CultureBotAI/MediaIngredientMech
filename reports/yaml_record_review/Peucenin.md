# `data/ingredients/mapped/Peucenin.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback identity is internally consistent, no exact
CHEBI replacement was found, and the final SSSOM row stays on the CAS registry
identifier.

## Identity

- Reviewed record: `data/ingredients/mapped/Peucenin.yaml`.
- Identifier and grounding: `identifier: cas:578-72-3` with
  `ontology_mapping.ontology_id: cas:578-72-3`, label `Peucenin`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A local CAS checksum calculation confirmed that `578-72-3` has the expected
  check digit.
- Fresh PubChem/OLS4 searches found a PubChem CID for `578-72-3` but no CHEBI
  term, so the current CAS fallback remains appropriate.
- The final SSSOM row was inspected directly and maps `MIM:Peucenin` exactly to
  `cas:578-72-3`.

## Evidence

- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies this row as
  an expected registry identifier: the CAS object matches the YAML identifier
  and `chemical_properties.cas_rn`, and CAS CURIEs are intentionally outside
  OAK/OLS term validation.
- The hidden/ignored-inclusive local search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`,
  and `UNIFIED_INGREDIENT_MAPPING.tsv` found the current fallback-registry row
  and no maintained exact CHEBI replacement for `578-72-3`.
- The final SSSOM row exports only `CAS:578-72-3`.

## Completeness

- The CAS fallback row is complete enough until a source-backed CHEBI primary
  term for this CAS record is curated.

## Recommended Edits

- None.
