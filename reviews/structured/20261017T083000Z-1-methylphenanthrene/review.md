# Per-record structured review: 1-methylphenanthrene (data/ingredients/mapped/1-methylphenanthrene.yaml)

- Review: 20261017T083000Z-1-methylphenanthrene
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 1-methylphenanthrene (data/ingredients/mapped/1-methylphenanthrene.yaml, record-8bb8ac8a0e5de018, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/1-methylphenanthrene.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/1-methylphenanthrene.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8bb8ac8a0e5de018 | data/ingredients/mapped/1-methylphenanthrene.yaml | maintained | 1-methylphenanthrene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | failed | True | record-8bb8ac8a0e5de018 | Explain curation-history timestamp order: 1-methylphenanthrene |
| Role evidence and plausibility check | passed | True | record-8bb8ac8a0e5de018 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8bb8ac8a0e5de018 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8bb8ac8a0e5de018.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8bb8ac8a0e5de018.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:12:30Z; reviewed SHA-256=8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04; current SHA-256=8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04; hash_changed=False. Reports=["reports/yaml_record_review/1-methylphenanthrene.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity and synchronized products pass; optional CAS, stale validation rows, and a timestamp-ordering nit remain.

### Non-monotonic curation-history timestamps

provenance: concern. Targets: record-8bb8ac8a0e5de018.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Findings

### rec-f-8724f3e14c641797: Explain curation-history timestamp order: 1-methylphenanthrene

minor / open / confirmed; issue key: mim-reconciliation-history-order-8bb8ac8a0e5de018.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"FLAGGED_FOR_REVIEW","changes":"mapping_status MAPPED -&gt; PENDING_REVIEW","curator":"microbedecoder-import-review","llm_assisted":true,"notes":"Auto-grounded by the microbedecoder import via ols-label-exact. Held at PENDING_REVIEW so the mapping does not reach the published SSSOM before a review-ingredients pass. See reports/microbedecoder_auto_mapped_review.tsv.","timestamp":"2026-08-04T03:08:34.142678+00:00"},"earlier_index":1,"later_event":{"action":"REVIEWED_AND_PROMOTED","changes":"mapping_status PENDING_REVIEW -&gt; MAPPED","curator":"review-ingredients","llm_assisted":true,"new_status":"MAPPED","notes":"Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical label exact-matches the record ontology_label (case-insensitive). This does NOT check for homonyms or wrong-sense class-level matches (see #203). Promoted PENDING_REVIEW -&gt; MAPPED.","previous_status":"PENDING_REVIEW","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":2}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Recommended Actions And Acceptance Checks

### rec-action-8724f3e14c641797

Explain curation-history timestamp order: 1-methylphenanthrene

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-32f94c0266962a6f | data/ingredients/mapped/1-methylphenanthrene.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2099],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35860","line":2101,"mapping_status":"MAPPED","ontology_id":"CHEBI:35860","preferred_term":"1-methylphenanthrene"}],"identifier":"CHEBI:35860","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35860","ontology_label":"1-methylphenanthrene","ontology_source":"CHEBI"},"preferred_term":"1-methylphenanthrene","sssom_rows":[{"data_row":23,"object_id":"CHEBI:35860","object_label":"1-methylphenanthrene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-methylphenanthrene","synonym_count":0} |
| ev-824b8b2c3002754c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2099] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d01405900864671a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:1-methylphenanthrene; data-row positions=[23] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":23,"object_id":"CHEBI:35860","object_label":"1-methylphenanthrene","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:1-methylphenanthrene","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-5dae8d5fe76444fc | docs/data/mapped_ingredients.csv; CSV lines=[2101] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:35860","line":2101,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35860","preferred_term":"1-methylphenanthrene","total_occurrences":"0"}] |
| ev-097bb94c08da9b12 | reports/yaml_record_review/1-methylphenanthrene.md; &#96;data/ingredients/mapped/1-methylphenanthrene.yaml&#96;:2; Verdict:4; Identity:12; Validation:27; Evidence:57; Completeness:87; Recommended Edits:99 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-289e2bfc5b10024c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[20] | context_only | [{"current_record_sha256":"8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04","finding_id":"SEM:9f82dddc361f96ec319d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4e9876d4b59bba17 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-8724f3e14c641797] | context_only | Predecessor structured review finding f-8724f3e14c641797 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-1-methylphenanthrene
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 1-methylphenanthrene (data/ingredients/mapped/1-methylphenanthrene.yaml)'
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
summary: Per-record structured review for 1-methylphenanthrene (data/ingredients/mapped/1-methylphenanthrene.yaml,
  record-8bb8ac8a0e5de018, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/1-methylphenanthrene.yaml
    sha256: 8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04
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
  - path: reports/yaml_record_review/1-methylphenanthrene.md
    sha256: 9ef7af6c4dea654f717918e19b46cd0c3bc63de443325b2e1ef6a94a2ee3cd80
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8bb8ac8a0e5de018
  path: data/ingredients/mapped/1-methylphenanthrene.yaml
  label: 1-methylphenanthrene
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-methylphenanthrene.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/1-methylphenanthrene.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/1-methylphenanthrene.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8bb8ac8a0e5de018
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: failed
  required: true
  summary: 'Explain curation-history timestamp order: 1-methylphenanthrene'
  target_ids:
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-32f94c0266962a6f
  - ev-824b8b2c3002754c
  - ev-d01405900864671a
  - ev-5dae8d5fe76444fc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-32f94c0266962a6f
  - ev-289e2bfc5b10024c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-097bb94c08da9b12
  - ev-289e2bfc5b10024c
  - ev-4e9876d4b59bba17
evidence:
- evidence_id: ev-32f94c0266962a6f
  kind: record_content
  reference: data/ingredients/mapped/1-methylphenanthrene.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2099],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35860","line":2101,"mapping_status":"MAPPED","ontology_id":"CHEBI:35860","preferred_term":"1-methylphenanthrene"}],"identifier":"CHEBI:35860","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35860","ontology_label":"1-methylphenanthrene","ontology_source":"CHEBI"},"preferred_term":"1-methylphenanthrene","sssom_rows":[{"data_row":23,"object_id":"CHEBI:35860","object_label":"1-methylphenanthrene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-methylphenanthrene","synonym_count":0}'
  snapshot_sha256: 8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04
- evidence_id: ev-824b8b2c3002754c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2099]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d01405900864671a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:1-methylphenanthrene; data-row positions=[23]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":23,"object_id":"CHEBI:35860","object_label":"1-methylphenanthrene","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:1-methylphenanthrene","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5dae8d5fe76444fc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2101]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:35860","line":2101,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35860","preferred_term":"1-methylphenanthrene","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-097bb94c08da9b12
  kind: prior_review
  reference: reports/yaml_record_review/1-methylphenanthrene.md
  locator: '`data/ingredients/mapped/1-methylphenanthrene.yaml`:2; Verdict:4; Identity:12;
    Validation:27; Evidence:57; Completeness:87; Recommended Edits:99'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9ef7af6c4dea654f717918e19b46cd0c3bc63de443325b2e1ef6a94a2ee3cd80
  quote: "Recommended Edits:\n1. If `mappings/record_research_validation.tsv` is meant\
    \ to be a live triage\n   queue, regenerate it from its maintained recipe or mark\
    \ the stale\n   methylphenanthrene rows resolved.\n2. Optionally add ChEBI-backed\
    \ `chemical_properties.cas_rn: 832-69-9` through a\n   normal enrichment pass.\n\
    3. Optionally correct the `REVIEWED_AND_PROMOTED` timestamp so curation history\n\
    \   sorts in true event order."
- evidence_id: ev-289e2bfc5b10024c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[20]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04","finding_id":"SEM:9f82dddc361f96ec319d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4e9876d4b59bba17
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-8724f3e14c641797]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8724f3e14c641797 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-4045a613b0e84011
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-32f94c0266962a6f
  - ev-824b8b2c3002754c
  - ev-d01405900864671a
  - ev-5dae8d5fe76444fc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-06728a30e41e5ae9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-097bb94c08da9b12
  - ev-32f94c0266962a6f
  - ev-289e2bfc5b10024c
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:12:30Z;
    reviewed SHA-256=8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04;
    current SHA-256=8cc4a3001604adfe0a69ddf0c97834feb9c579731ac23c8aa5a3d2d27bfddd04;
    hash_changed=False. Reports=["reports/yaml_record_review/1-methylphenanthrene.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity and synchronized products pass; optional CAS, stale validation rows,
    and a timestamp-ordering nit remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-097bb94c08da9b12
    - ev-32f94c0266962a6f
  - name: legacy-native-ids
    value: '["SEM:9f82dddc361f96ec319d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-32f94c0266962a6f
    - ev-097bb94c08da9b12
    - ev-289e2bfc5b10024c
- assessment_id: a-b9c2e0566be1ec4d
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
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-097bb94c08da9b12
  - ev-32f94c0266962a6f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-097bb94c08da9b12
    - ev-32f94c0266962a6f
findings:
- finding_id: rec-f-8724f3e14c641797
  issue_key: mim-reconciliation-history-order-8bb8ac8a0e5de018
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: 'Explain curation-history timestamp order: 1-methylphenanthrene'
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
  - record-8bb8ac8a0e5de018
  evidence_ids:
  - ev-097bb94c08da9b12
  - ev-32f94c0266962a6f
  - ev-4e9876d4b59bba17
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-methylphenanthrene.yaml
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
    finding_id: f-8724f3e14c641797
actions:
- action_id: rec-action-8724f3e14c641797
  description: 'Explain curation-history timestamp order: 1-methylphenanthrene'
  finding_ids:
  - rec-f-8724f3e14c641797
  target_ids:
  - record-8bb8ac8a0e5de018
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-methylphenanthrene.yaml
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
