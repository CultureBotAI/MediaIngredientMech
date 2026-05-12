# External Prefix OLS Validation

- Input: `mappings/ingredient_mappings_unknown_term_triage.tsv`
- Current UNKNOWN_TERM external-prefix rows checked: 193
- Unique external-prefix terms checked: 167
- Method: EBI OLS4 `/api/search` with explicit ontology slugs for `mesh`, `ncit`, `micro`, and `bto`; exact `obo_id` match required for `RESOLVED_EXACT_CURIE`.

## Status Counts

| OLS status | Count |
|---|---:|
| RESOLVED_EXACT_CURIE | 167 |

## Prefix x Status

| Prefix | OLS status | Count |
|---|---|---:|
| BTO | RESOLVED_EXACT_CURIE | 1 |
| MICRO | RESOLVED_EXACT_CURIE | 34 |
| NCIT | RESOLVED_EXACT_CURIE | 50 |
| mesh | RESOLVED_EXACT_CURIE | 82 |

## Exact CURIE Label Differences

None.

## Interpretation

Terms with `RESOLVED_EXACT_CURIE` were false-positive `UNKNOWN_TERM` results from the serial synonym-review dispatcher, which does not fully validate these prefixes through its default OAK/OLS path.
Terms with `NOT_RESOLVED`, `SEARCH_HIT_NONEXACT`, or `ERROR` need curator review before mapping changes.
