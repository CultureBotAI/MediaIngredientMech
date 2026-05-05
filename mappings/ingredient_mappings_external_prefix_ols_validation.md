# External Prefix OLS Validation

- Input: `mappings/ingredient_mappings_unknown_term_triage.tsv`
- Unique external-prefix terms checked: 159
- Method: EBI OLS4 `/api/search` with explicit ontology slugs for `mesh`, `ncit`, `micro`, and `bto`; exact `obo_id` match required for `RESOLVED_EXACT_CURIE`.

## Status Counts

| OLS status | Count |
|---|---:|
| RESOLVED_EXACT_CURIE | 159 |

## Prefix x Status

| Prefix | OLS status | Count |
|---|---|---:|
| BTO | RESOLVED_EXACT_CURIE | 1 |
| MICRO | RESOLVED_EXACT_CURIE | 34 |
| NCIT | RESOLVED_EXACT_CURIE | 48 |
| mesh | RESOLVED_EXACT_CURIE | 76 |

## Exact CURIE Label Differences

None.

## Interpretation

Terms with `RESOLVED_EXACT_CURIE` were false-positive `UNKNOWN_TERM` results from the serial synonym-review dispatcher, which did not include these prefixes in its OLS dispatch table.
Terms with `NOT_RESOLVED`, `SEARCH_HIT_NONEXACT`, or `ERROR` need curator review before mapping changes.
