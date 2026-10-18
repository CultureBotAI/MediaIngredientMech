# `data/ingredients/mapped/Atrazin.yaml`

## Verdict

Needs curation; severity blocker. The record exact-maps `Atrazin` to the
fallback registry CURIE `cas:1924-24-9`, but PubChem has no CID for
`1924-24-9`, the known atrazine CAS `1912-24-9` resolves to PubChem `Atrazine`,
and this corpus already has an exact `CHEBI:15930` atrazine record under
`data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`.

## Identity

- Reviewed record: `data/ingredients/mapped/Atrazin.yaml`.
- Identifier and grounding: `identifier: cas:1924-24-9` with
  `ontology_mapping.ontology_id: cas:1924-24-9`,
  `ontology_label: Atrazin`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem lookup for the recorded CAS `1924-24-9` returned no CID.
- PubChem lookup for CAS `1912-24-9` resolved to `Atrazine` with formula
  `C8H14ClN5` and the same InChI used by the existing `CHEBI:15930` atrazine
  record.
- OLS search for `Atrazin` in ChEBI returned `CHEBI:15930` `atrazine`, and the
  existing MIM record for that term is already mapped and published.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Atrazin.yaml data/ingredients/mapped/Atrop_Abyssomicin_C.yaml data/ingredients/mapped/Auraptene.yaml data/ingredients/mapped/Aureothricin.yaml data/ingredients/mapped/Avermectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was skipped for `Atrazin.yaml` because the only
  ontology identifier uses the non-OBO `cas:` prefix; product correspondence
  validation owns CAS registry rows.
- PubChem lookup for `1924-24-9` failed to resolve the CAS-backed identity.
- PubChem lookup for `1912-24-9` and OLS search for `Atrazin` both point to
  atrazine rather than to a novel CAS-only substance.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over the repository, excluding
  `data/curated/backups`, `reports/yaml_record_review`,
  `reports/yaml_record_review_batch`, and the validator TSV, found no raw
  CultureBotHT source row in this checkout beyond the active YAML, aggregate,
  SSSOM, and generated exports.
- `mappings/ingredient_mappings.sssom.tsv` row 494 publishes
  `MIM:Atrazin skos:exactMatch cas:1924-24-9`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` only establish that the
  CAS CURIE was an expected registry identifier when it matched the YAML; they
  do not verify that `1924-24-9` is a valid Atrazin registry number.
- `mappings/ingredient_mappings.sssom.tsv` row 115 already publishes
  `CHEBI:15930` `atrazine` for
  `2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine`, so a corrected
  `Atrazin` row would collide with an existing exact atrazine identity.

## Completeness

- The local YAML, aggregate, and SSSOM rows are internally synchronized, but
  they are synchronized around an unsupported CAS.
- `chemical_properties` lacks formula, InChI, and SMILES because the CAS lookup
  never reached a resolvable structure.
- The record has no CultureMech memberships and no source occurrences, so there
  is no local occurrence table row that disambiguates `Atrazin` away from
  atrazine.

## Recommended Edits

- Verify the upstream CultureBotHT entry for `Atrazin`; if it intended
  atrazine, retire or merge `data/ingredients/mapped/Atrazin.yaml` into
  `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`
  and preserve `Atrazin` only as a reviewed alias of `CHEBI:15930`.
- Remove or correct `cas:1924-24-9` from the individual YAML, aggregate
  collection, and SSSOM row; regenerate the flat exports and rerun focused
  strict validation, product id/label correspondence, SSSOM invariants, and
  flat-export coverage.
