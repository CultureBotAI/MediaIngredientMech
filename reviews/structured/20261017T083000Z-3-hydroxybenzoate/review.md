# Per-record structured review: 3-hydroxybenzoate (data/ingredients/mapped/3-hydroxybenzoate.yaml)

- Review: 20261017T083000Z-3-hydroxybenzoate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-hydroxybenzoate (data/ingredients/mapped/3-hydroxybenzoate.yaml, record-1fa655110d9c0a46, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-hydroxybenzoate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-hydroxybenzoate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1fa655110d9c0a46 | data/ingredients/mapped/3-hydroxybenzoate.yaml | maintained | 3-hydroxybenzoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | failed | True | record-1fa655110d9c0a46 | Explain curation-history timestamp order: 3-hydroxybenzoate |
| Role evidence and plausibility check | passed | True | record-1fa655110d9c0a46 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1fa655110d9c0a46 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1fa655110d9c0a46.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1fa655110d9c0a46.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:03:57Z; reviewed SHA-256=1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28; current SHA-256=1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28; hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybenzoate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, microbedecoder occurrence count, SSSOM, and aggregate pass; only stale advisory rows and a timestamp-ordering nit remain.

### Non-monotonic curation-history timestamps

provenance: concern. Targets: record-1fa655110d9c0a46.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Findings

### rec-f-0f9fc988bb20137c: Explain curation-history timestamp order: 3-hydroxybenzoate

minor / open / confirmed; issue key: mim-reconciliation-history-order-1fa655110d9c0a46.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Recommended Actions And Acceptance Checks

### rec-action-0f9fc988bb20137c

Explain curation-history timestamp order: 3-hydroxybenzoate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-885f279d25349381 | data/ingredients/mapped/3-hydroxybenzoate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2109],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16193","line":2111,"mapping_status":"MAPPED","ontology_id":"CHEBI:16193","preferred_term":"3-hydroxybenzoate"}],"identifier":"CHEBI:16193","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16193","ontology_label":"3-hydroxybenzoate","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybenzoate","sssom_rows":[{"data_row":143,"object_id":"CHEBI:16193","object_label":"3-hydroxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybenzoate","synonym_count":0} |
| ev-c3e0d910342844cc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2109] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-917c1186a402cd7c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-hydroxybenzoate; data-row positions=[143] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":143,"object_id":"CHEBI:16193","object_label":"3-hydroxybenzoate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybenzoate","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-46deb80d5fd886b6 | docs/data/mapped_ingredients.csv; CSV lines=[2111] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16193","line":2111,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16193","preferred_term":"3-hydroxybenzoate","total_occurrences":"0"}] |
| ev-81001cf3b333cc2f | reports/yaml_record_review/3-hydroxybenzoate.md; &#96;data/ingredients/mapped/3-hydroxybenzoate.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:38; Completeness:56; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d31bd195769b60ca | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[119] | context_only | [{"current_record_sha256":"1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28","finding_id":"SEM:a904b81690165d10ae0b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-34360e94d8cca3a8 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-0f9fc988bb20137c] | context_only | Predecessor structured review finding f-0f9fc988bb20137c in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-hydroxybenzoate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-hydroxybenzoate (data/ingredients/mapped/3-hydroxybenzoate.yaml)'
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
summary: Per-record structured review for 3-hydroxybenzoate (data/ingredients/mapped/3-hydroxybenzoate.yaml,
  record-1fa655110d9c0a46, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-hydroxybenzoate.yaml
    sha256: 1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28
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
  - path: reports/yaml_record_review/3-hydroxybenzoate.md
    sha256: 938b28c546e15e9988e7904fc552ee6e638fa74b5d0120a86fec21c97b2fa1a2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1fa655110d9c0a46
  path: data/ingredients/mapped/3-hydroxybenzoate.yaml
  label: 3-hydroxybenzoate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybenzoate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-hydroxybenzoate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-hydroxybenzoate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1fa655110d9c0a46
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: failed
  required: true
  summary: 'Explain curation-history timestamp order: 3-hydroxybenzoate'
  target_ids:
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-885f279d25349381
  - ev-c3e0d910342844cc
  - ev-917c1186a402cd7c
  - ev-46deb80d5fd886b6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-885f279d25349381
  - ev-d31bd195769b60ca
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-81001cf3b333cc2f
  - ev-d31bd195769b60ca
  - ev-34360e94d8cca3a8
evidence:
- evidence_id: ev-885f279d25349381
  kind: record_content
  reference: data/ingredients/mapped/3-hydroxybenzoate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2109],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16193","line":2111,"mapping_status":"MAPPED","ontology_id":"CHEBI:16193","preferred_term":"3-hydroxybenzoate"}],"identifier":"CHEBI:16193","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16193","ontology_label":"3-hydroxybenzoate","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybenzoate","sssom_rows":[{"data_row":143,"object_id":"CHEBI:16193","object_label":"3-hydroxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybenzoate","synonym_count":0}'
  snapshot_sha256: 1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28
- evidence_id: ev-c3e0d910342844cc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2109]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-917c1186a402cd7c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-hydroxybenzoate; data-row positions=[143]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":143,"object_id":"CHEBI:16193","object_label":"3-hydroxybenzoate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybenzoate","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-46deb80d5fd886b6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2111]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16193","line":2111,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16193","preferred_term":"3-hydroxybenzoate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-81001cf3b333cc2f
  kind: prior_review
  reference: reports/yaml_record_review/3-hydroxybenzoate.md
  locator: '`data/ingredients/mapped/3-hydroxybenzoate.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:38; Completeness:56; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 938b28c546e15e9988e7904fc552ee6e638fa74b5d0120a86fec21c97b2fa1a2
  quote: 'Recommended Edits:

    No YAML edit is required for this record. The stale advisory rows can be

    ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt;

    the timestamp-ordering nit can be left alone unless the curation history is

    normalized later.'
- evidence_id: ev-d31bd195769b60ca
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[119]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28","finding_id":"SEM:a904b81690165d10ae0b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-34360e94d8cca3a8
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-0f9fc988bb20137c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0f9fc988bb20137c in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-6e7dc4d184c71960
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-885f279d25349381
  - ev-c3e0d910342844cc
  - ev-917c1186a402cd7c
  - ev-46deb80d5fd886b6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6fde1e642981bd7d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-81001cf3b333cc2f
  - ev-885f279d25349381
  - ev-d31bd195769b60ca
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:03:57Z;
    reviewed SHA-256=1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28;
    current SHA-256=1495533eb79cc610126c9e534834fc1ec4bd4eb56fe73afd8c655829efcada28;
    hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybenzoate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, microbedecoder occurrence count, SSSOM, and aggregate pass;
    only stale advisory rows and a timestamp-ordering nit remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-81001cf3b333cc2f
    - ev-885f279d25349381
  - name: legacy-native-ids
    value: '["SEM:a904b81690165d10ae0b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-885f279d25349381
    - ev-81001cf3b333cc2f
    - ev-d31bd195769b60ca
- assessment_id: a-a67152a7b1787223
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
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-81001cf3b333cc2f
  - ev-885f279d25349381
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-81001cf3b333cc2f
    - ev-885f279d25349381
findings:
- finding_id: rec-f-0f9fc988bb20137c
  issue_key: mim-reconciliation-history-order-1fa655110d9c0a46
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: 'Explain curation-history timestamp order: 3-hydroxybenzoate'
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
  - record-1fa655110d9c0a46
  evidence_ids:
  - ev-81001cf3b333cc2f
  - ev-885f279d25349381
  - ev-34360e94d8cca3a8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybenzoate.yaml
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
    finding_id: f-0f9fc988bb20137c
actions:
- action_id: rec-action-0f9fc988bb20137c
  description: 'Explain curation-history timestamp order: 3-hydroxybenzoate'
  finding_ids:
  - rec-f-0f9fc988bb20137c
  target_ids:
  - record-1fa655110d9c0a46
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybenzoate.yaml
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
