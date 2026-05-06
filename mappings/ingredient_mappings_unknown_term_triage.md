# UNKNOWN_TERM Mapping Triage

- Source review: `mappings/ingredient_mappings_oak_ols_review.tsv`
- Source SSSOM: `mappings/ingredient_mappings.sssom.tsv`
- External-prefix OLS validation: `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`
- Rows triaged: 690

## Classification Counts

| Classification | Count |
|---|---:|
| expected_registry_identifier | 497 |
| missing_prefix_validator_coverage_issue | 193 |

## Prefix x Classification

| Prefix | Classification | Count |
|---|---|---:|
| BTO | missing_prefix_validator_coverage_issue | 1 |
| MICRO | missing_prefix_validator_coverage_issue | 47 |
| NCIT | missing_prefix_validator_coverage_issue | 61 |
| cas | expected_registry_identifier | 249 |
| kgmicrobe.compound | expected_registry_identifier | 219 |
| kgmicrobe.ingredient | expected_registry_identifier | 29 |
| mesh | missing_prefix_validator_coverage_issue | 84 |

## External Prefix OLS Status

| OLS status | Row count |
|---|---:|
| RESOLVED_EXACT_CURIE | 193 |

## Interpretation

- `cas:` rows are registry identifiers. Rows where the CAS CURIE matches `chemical_properties.cas_rn` and/or the YAML `identifier` are expected OAK/OLS unknowns, not mapping failures.
- `kgmicrobe.compound:` and `kgmicrobe.ingredient:` rows are local registry identifiers. This includes Rule B1 identity rows and placeholder primary identifiers with `mapping_quality: PLACEHOLDER`.
- `mesh`, `NCIT`, `MICRO`, and `BTO` rows all resolve by exact CURIE in prefix-specific EBI OLS queries with matching labels. Their `UNKNOWN_TERM` status is a validator-dispatch coverage issue in the serial synonym-review script, not evidence that these mappings are bad.

## Rows Needing Curator Review

Fifty-three `kgmicrobe.compound:*` placeholder rows remain queued for future
manual promotion review. The OAK/OLS follow-up pass promoted
`Poly_L_Lysine_Polymer` to `CHEBI:61490`; no other high-confidence replacement
was supported. A later all-ontology OLS normalized label/synonym scan over the
53 remaining placeholders found 0 additional identity candidates.

## Next Actions

1. Keep expected `cas:` and `kgmicrobe.*` registry rows unless a row-specific curation issue is found.
2. Extend the synonym-review OLS dispatch table to include `mesh`, `NCIT`, `MICRO`, and `BTO` if future validation should stop reporting those rows as `UNKNOWN_TERM`.
3. Continue manual review of the 53 remaining placeholder rows; do not promote
   family/member lexical hits without exact identity evidence.
