# Per-record structured review: (R)-lactate (data/ingredients/mapped/(R)-lactate.yaml)

- Review: 20261017T083000Z-r-lactate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for (R)-lactate (data/ingredients/mapped/(R)-lactate.yaml, record-1b12eab882a87e59, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/(R)-lactate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/(R)-lactate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1b12eab882a87e59 | data/ingredients/mapped/(R)-lactate.yaml | maintained | (R)-lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | failed | True | record-1b12eab882a87e59 | Explain curation-history timestamp order: (R)-lactate |
| Role evidence and plausibility check | passed | True | record-1b12eab882a87e59 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1b12eab882a87e59 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1b12eab882a87e59.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1b12eab882a87e59.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T04:48:31Z; reviewed SHA-256=5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d; current SHA-256=5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d; hash_changed=False. Reports=["reports/yaml_record_review/(R)-lactate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active identity passes, but source_occurrences appears to omit the absorbed D-lactate row with count 17.

### Non-monotonic curation-history timestamps

provenance: concern. Targets: record-1b12eab882a87e59.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Findings

### rec-f-d55db516999a041d: Explain curation-history timestamp order: (R)-lactate

minor / open / confirmed; issue key: mim-reconciliation-history-order-1b12eab882a87e59.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Recommended Actions And Acceptance Checks

### rec-action-d55db516999a041d

Explain curation-history timestamp order: (R)-lactate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-db804ac2554d80de | data/ingredients/mapped/(R)-lactate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2095],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16004","line":2097,"mapping_status":"MAPPED","ontology_id":"CHEBI:16004","preferred_term":"(R)-lactate"}],"identifier":"CHEBI:16004","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16004","ontology_label":"(R)-lactate","ontology_source":"CHEBI"},"preferred_term":"(R)-lactate","sssom_rows":[],"sssom_subject":"MIM:(R)-lactate","synonym_count":1} |
| ev-efc10ef882f6d263 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2095] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-483b95638148e1e0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:(R)-lactate; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-20b118e4de347468 | docs/data/mapped_ingredients.csv; CSV lines=[2097] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16004","line":2097,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16004","preferred_term":"(R)-lactate","total_occurrences":"0"}] |
| ev-cf9aa5c14e5766a7 | reports/yaml_record_review/(R)-lactate.md; &#96;data/ingredients/mapped/(R)-lactate.yaml&#96;:2; Verdict:4; Identity:11; Validation:31; Evidence:45; Completeness:76; Recommended Edits:90 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1f72aa82b2211be2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[6] | context_only | [{"current_record_sha256":"5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d","finding_id":"SEM:c34d7b8854b455ca38bf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-68cb732dc553c3e0 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-d55db516999a041d] | context_only | Predecessor structured review finding f-d55db516999a041d in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-r-lactate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: (R)-lactate (data/ingredients/mapped/(R)-lactate.yaml)'
started_at: '2026-10-17T08:25:00Z'
finished_at: '2026-10-17T08:30:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent per-record structured review and reconciliation
    against current HEAD and historical review inputs.
skill: review-yaml-record
completion: partial
verdict: needs_curation
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for (R)-lactate (data/ingredients/mapped/(R)-lactate.yaml,
  record-1b12eab882a87e59, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/(R)-lactate.yaml
    sha256: 5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/mapped_ingredients.csv
    sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
    role: context
  - path: reports/yaml_record_review/(R)-lactate.md
    sha256: 09df8c53863c10b037f17d00098ced3fce5d27b68b68cf8fb5bb3eb79591330f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1b12eab882a87e59
  path: data/ingredients/mapped/(R)-lactate.yaml
  label: (R)-lactate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(R)-lactate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/(R)-lactate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/(R)-lactate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1b12eab882a87e59
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: failed
  required: true
  summary: 'Explain curation-history timestamp order: (R)-lactate'
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-db804ac2554d80de
  - ev-efc10ef882f6d263
  - ev-483b95638148e1e0
  - ev-20b118e4de347468
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-db804ac2554d80de
  - ev-1f72aa82b2211be2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-cf9aa5c14e5766a7
  - ev-1f72aa82b2211be2
  - ev-68cb732dc553c3e0
evidence:
- evidence_id: ev-db804ac2554d80de
  kind: record_content
  reference: data/ingredients/mapped/(R)-lactate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2095],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16004","line":2097,"mapping_status":"MAPPED","ontology_id":"CHEBI:16004","preferred_term":"(R)-lactate"}],"identifier":"CHEBI:16004","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16004","ontology_label":"(R)-lactate","ontology_source":"CHEBI"},"preferred_term":"(R)-lactate","sssom_rows":[],"sssom_subject":"MIM:(R)-lactate","synonym_count":1}'
  snapshot_sha256: 5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d
- evidence_id: ev-efc10ef882f6d263
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2095]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-483b95638148e1e0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:(R)-lactate; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-20b118e4de347468
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2097]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16004","line":2097,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16004","preferred_term":"(R)-lactate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cf9aa5c14e5766a7
  kind: prior_review
  reference: reports/yaml_record_review/(R)-lactate.md
  locator: '`data/ingredients/mapped/(R)-lactate.yaml`:2; Verdict:4; Identity:11;
    Validation:31; Evidence:45; Completeness:76; Recommended Edits:90'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 09df8c53863c10b037f17d00098ced3fce5d27b68b68cf8fb5bb3eb79591330f
  quote: "Recommended Edits:\n1. Update the maintained per-record input\n   `data/ingredients/mapped/(R)-lactate.yaml`\
    \ so\n   `occurrence_statistics.source_occurrences` accounts for both microbedecoder\n\
    \   rows: `kgmicrobe.trait:r_lactate` with count `19` and\n   `kgmicrobe.trait:d_lactate`\
    \ with count `17`. Append a curation-history event\n   that names the `data/custom/microbedecoder`\
    \ rows as the source, then run\n   `just sync-curated` and regenerate the flat\
    \ docs exports.\n2. On a future provenance cleanup pass, fix or annotate the coarse\n\
    \   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic\n\
    \   order as well as append order.\n3. Regenerate `mappings/record_research_validation.tsv`\
    \ from its maintained\n   recipe, or mark the stale `(R)-lactate` rows resolved,\
    \ after the\n   occurrence-source fix lands."
- evidence_id: ev-1f72aa82b2211be2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[6]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d","finding_id":"SEM:c34d7b8854b455ca38bf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-68cb732dc553c3e0
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-d55db516999a041d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d55db516999a041d in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-d0544e03e26fb92f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-db804ac2554d80de
  - ev-efc10ef882f6d263
  - ev-483b95638148e1e0
  - ev-20b118e4de347468
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6d0f3fe7cbdc71a4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-cf9aa5c14e5766a7
  - ev-db804ac2554d80de
  - ev-1f72aa82b2211be2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T04:48:31Z;
    reviewed SHA-256=5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d;
    current SHA-256=5ecdb54c8474811127e8bb01b8d7753004065329b1574864c8140d635c6ae93d;
    hash_changed=False. Reports=["reports/yaml_record_review/(R)-lactate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active identity
    passes, but source_occurrences appears to omit the absorbed D-lactate row with
    count 17.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cf9aa5c14e5766a7
    - ev-db804ac2554d80de
  - name: legacy-native-ids
    value: '["SEM:c34d7b8854b455ca38bf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-db804ac2554d80de
    - ev-cf9aa5c14e5766a7
    - ev-1f72aa82b2211be2
- assessment_id: a-b67772c73a87cf7d
  area: provenance
  topic: Non-monotonic curation-history timestamps
  outcome: concern
  summary: 'The reported timestamp-order problem is still observable in these adjacent
    append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status
    MAPPED -> PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded
    by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the
    mapping does not reach the published SSSOM before a review-ingredients pass. See
    reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status
    PENDING_REVIEW -> MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed
    by review-ingredients: id resolves in local OAK adapter and its canonical label
    exact-matches the record ontology_label (case-insensitive). This does NOT check
    for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW
    -> MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-cf9aa5c14e5766a7
  - ev-db804ac2554d80de
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cf9aa5c14e5766a7
    - ev-db804ac2554d80de
findings:
- finding_id: rec-f-d55db516999a041d
  issue_key: mim-reconciliation-history-order-1b12eab882a87e59
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: 'Explain curation-history timestamp order: (R)-lactate'
  description: 'The reported timestamp-order problem is still observable in these
    adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status
    MAPPED -> PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded
    by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the
    mapping does not reach the published SSSOM before a review-ingredients pass. See
    reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status
    PENDING_REVIEW -> MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed
    by review-ingredients: id resolves in local OAK adapter and its canonical label
    exact-matches the record ontology_label (case-insensitive). This does NOT check
    for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW
    -> MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-1b12eab882a87e59
  evidence_ids:
  - ev-cf9aa5c14e5766a7
  - ev-db804ac2554d80de
  - ev-68cb732dc553c3e0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(R)-lactate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - history-order
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-d55db516999a041d
actions:
- action_id: rec-action-d55db516999a041d
  description: 'Explain curation-history timestamp order: (R)-lactate'
  finding_ids:
  - rec-f-d55db516999a041d
  target_ids:
  - record-1b12eab882a87e59
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(R)-lactate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
limitations:
- 'Read-only per-record structured review (scientific_review: false); no ingredient
  YAML, curated aggregate, or SSSOM files were modified.'
- Confirmed local evidence gaps and structural issues are recorded as open with bounded
  remediation actions; historical or source-context claims requiring primary recipe/literature
  verification remain deferred (provisional).
tags:
- record-review
- per-record
- reconciliation
- bundle-by-owner
notes:
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb)
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
