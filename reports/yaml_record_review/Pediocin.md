# `data/ingredients/mapped/Pediocin.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback identity is internally consistent, no exact
CHEBI replacement was found, and the final SSSOM row stays on the CAS registry
identifier.

## Identity

- Reviewed record: `data/ingredients/mapped/Pediocin.yaml`.
- Identifier and grounding: `identifier: cas:133108-87-9` with
  `ontology_mapping.ontology_id: cas:133108-87-9`, label `Pediocin`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The CAS checksum for `133108-87-9` is valid.
- Fresh OLS4/PubChem searches did not find a same-identifier or same-label
  CHEBI/PubChem replacement for `cas:133108-87-9`; the live CHEBI hit for
  `Pediocin` is `CHEBI:202090` Pediocin A and is not a replacement for this
  CAS fallback.
- The final SSSOM row was inspected directly and maps `MIM:Pediocin` exactly to
  `cas:133108-87-9`.

## Evidence

- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies this row as
  an expected registry identifier: the CAS object matches the YAML identifier
  and `chemical_properties.cas_rn`, and CAS CURIEs are intentionally outside
  OAK/OLS term validation.
- The hidden/ignored-inclusive local search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`,
  and `UNIFIED_INGREDIENT_MAPPING.tsv` found the current fallback-registry row
  and no maintained exact CHEBI replacement for `133108-87-9`.
- The final SSSOM row exports `Pediocin from Pediococcus acidilactici` and
  `CAS:133108-87-9`, both scoped to the maintained local registry subject.

## Completeness

- The CAS fallback row is complete enough until a source-backed CHEBI primary
  term for this CAS record is curated.

## Recommended Edits

- None.
