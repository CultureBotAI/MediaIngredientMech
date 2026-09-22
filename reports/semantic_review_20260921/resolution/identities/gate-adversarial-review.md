# Independent adversarial review of the new semantic release gate

Reviewed `src/mediaingredientmech/validation/semantic_release.py` and the
content-bound review-status changes in `src/mediaingredientmech/export/kgx.py`
during implementation. These findings concern the initial implementation; the
parent workflow owns repairs and final verification.

1. **Major: graph projection can diverge while provenance payloads still pass.**
   The release validator's edge comparison includes `source_record`,
   `assertion_type`, `source_position`, and `assertion_json`, but ignores the
   actual `subject`, `predicate`, `object`, and `relation`. Its ingredient-node
   comparison checks source coverage and `record_json`, but ignores exported
   node identity and label. Updating member/report hashes after a projection
   error would therefore validate the wrong scientific graph. Require the
   exported triples, node identities, and endpoints to agree with an independently
   reconstructed source projection, including broad/narrow direction and
   component IDs. Add a negative case that mutates a mapping triple while
   leaving its source JSON untouched and refreshes all freshness hashes.
2. **Major: unrelated tombstones can hide active historical findings.**
   `adjudicate_findings` accepts any `current_record` present in the corpus.
   No continuity check ties it to the original finding's `source_record`.
   A finding on an active record can point at a different rejected record and
   select `EXCLUDED_REJECTED`, removing that blocker. A direct reproducer returned
   `[]` for a major active identity finding redirected to an unrelated tombstone.
   Default to exact source-path continuity, and require an explicit, hash-bound
   record lineage plan for renames and merges. A moved survivor must not be
   replaceable by any unrelated rejected record.

The KGX review-status change correctly prevents a stale/unhashed historical
`pass` or `pass_with_minor_issues` string from appearing as a current positive
verdict in `review_status`. Keeping the original ledger row in `review_json` is
acceptable provenance because the separate effective status and manifest
limitations state its historical status.

## Remediation

The parent opened [#711](https://github.com/CultureBotAI/MediaIngredientMech/issues/711)
for graph projection and [#712](https://github.com/CultureBotAI/MediaIngredientMech/issues/712)
for record continuity. Both defects are repaired in
`src/mediaingredientmech/validation/semantic_release.py`:

- The gate independently reconstructs every scientific node and edge from source,
  including mapping direction, actual role/component/recipe endpoints, organism
  context, publications, concentrations, and content-derived edge IDs. It also
  checks source primary identity and ontology grounding against SSSOM.
- Every historical finding keeps its original source path or follows a hashed
  move/merge plan tied to the historical source hash and current destination hash.
  A merge must follow the rejected record's explicit representative.
- [#713](https://github.com/CultureBotAI/MediaIngredientMech/issues/713) additionally
  requires an explicit current disposition for every assertion. Payload and
  source hashes must match, and a positive decision requires a reason plus a
  hashed local evidence artifact. New or changed claims cannot inherit an old
  approval merely by including a citation field. OPEN decisions block release.

Regression coverage is in `tests/test_semantic_release.py` and independently
authored `tests/test_semantic_release_adversarial.py`. The full-report tests
include a wrong graph predicate with refreshed artifact hashes and an altered
review-evidence file. The scientific adequacy of evidence remains a curator's
judgment; these guards enforce provenance, coverage, projection, and truthful
reporting of the recorded decisions.
