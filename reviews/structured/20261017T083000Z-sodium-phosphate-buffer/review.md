# Per-record structured review: Sodium_Phosphate_Buffer (data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml)

- Review: 20261017T083000Z-sodium-phosphate-buffer
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Phosphate_Buffer (data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml, record-83eeb69b0585d6f4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-83eeb69b0585d6f4 | data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml | maintained | Sodium_Phosphate_Buffer |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-83eeb69b0585d6f4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-83eeb69b0585d6f4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-83eeb69b0585d6f4 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-83eeb69b0585d6f4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-83eeb69b0585d6f4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:39:29Z; reviewed SHA-256=ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29; current SHA-256=ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Phosphate_Buffer.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock-solution identity and close NCIT parent pass, but final SSSOM exports concentration/pH variants and BUFFER is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-83eeb69b0585d6f4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-84a952452c1bbbad: Reassess prediction-only role support: Sodium phosphate buffer

major / open / confirmed; issue key: mim-reconciliation-role-support-83eeb69b0585d6f4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-84a952452c1bbbad

Reassess prediction-only role support: Sodium phosphate buffer

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-26fc0c1929509db2 | data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1863],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Sodium phosphate buffer"}],"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate Buffer","ontology_source":"NCIT"},"preferred_term":"Sodium phosphate buffer","sssom_rows":[{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate Buffer","predicate_id":"skos:closeMatch"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Phosphate_Buffer","synonym_count":5} |
| ev-dafb129b63ddd401 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1863] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4a38c91bfd3b24f3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Phosphate_Buffer; data-row positions=[2595, 2596] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate Buffer","other":"Sodium phosphate buffer (10 mM; pH7.1)&#124;Sodium phosphate buffer (25 mM; pH 3.4)&#124;Sodium phosphate buffer (10 mM, pH 7.1)&#124;Sodium phosphate buffer (25 mM, pH 3.4)","predicate_id":"skos:closeMatch","subject_id":"MIM:Sodium_Phosphate_Buffer","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium phosphate buffer","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Phosphate_Buffer","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-861552643e4d2f7d | docs/data/mapped_ingredients.csv; CSV lines=[1865] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"NCIT:C29321","preferred_term":"Sodium phosphate buffer","total_occurrences":"19"}] |
| ev-b573132e4c56e662 | reports/yaml_record_review/Sodium_Phosphate_Buffer.md; &#96;data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:31; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cfe1054eccc3245c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1228,1992] | context_only | [{"current_record_sha256":"ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29","finding_id":"SEM:60d3271db8936719a28c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29","finding_id":"SEM:cf7c681a4686a8d77eef","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-572c3fb1e8102fe5 | data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1863],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Sodium phosphate buffer"}],"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate Buffer","ontology_source":"NCIT"},"preferred_term":"Sodium phosphate buffer","sssom_rows":[{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate Buffer","predicate_id":"skos:closeMatch"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Phosphate_Buffer","synonym_count":5} |
| ev-66163b107051dcdc | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-84a952452c1bbbad] | context_only | Predecessor structured review finding f-84a952452c1bbbad in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-phosphate-buffer
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Phosphate_Buffer (data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml)'
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
summary: Per-record structured review for Sodium_Phosphate_Buffer (data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml,
  record-83eeb69b0585d6f4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
    sha256: ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sodium_Phosphate_Buffer.md
    sha256: beee7ebacc6c58551ca09f5c841fc8f175e47fa7befcad1f0cf0ed2d218ccf43
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-83eeb69b0585d6f4
  path: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
  label: Sodium_Phosphate_Buffer
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-83eeb69b0585d6f4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-26fc0c1929509db2
  - ev-dafb129b63ddd401
  - ev-4a38c91bfd3b24f3
  - ev-861552643e4d2f7d
  - ev-572c3fb1e8102fe5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-26fc0c1929509db2
  - ev-cfe1054eccc3245c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-b573132e4c56e662
  - ev-cfe1054eccc3245c
  - ev-66163b107051dcdc
evidence:
- evidence_id: ev-26fc0c1929509db2
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1863],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Sodium
    phosphate buffer"}],"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate
    Buffer","ontology_source":"NCIT"},"preferred_term":"Sodium phosphate buffer","sssom_rows":[{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate
    Buffer","predicate_id":"skos:closeMatch"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium
    phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Phosphate_Buffer","synonym_count":5}'
  snapshot_sha256: ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29
- evidence_id: ev-dafb129b63ddd401
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1863]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4a38c91bfd3b24f3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Phosphate_Buffer; data-row positions=[2595, 2596]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate
    Buffer","other":"Sodium phosphate buffer (10 mM; pH7.1)|Sodium phosphate buffer
    (25 mM; pH 3.4)|Sodium phosphate buffer (10 mM, pH 7.1)|Sodium phosphate buffer
    (25 mM, pH 3.4)","predicate_id":"skos:closeMatch","subject_id":"MIM:Sodium_Phosphate_Buffer","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium
    phosphate buffer","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Phosphate_Buffer","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-861552643e4d2f7d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1865]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"NCIT:C29321","preferred_term":"Sodium
    phosphate buffer","total_occurrences":"19"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b573132e4c56e662
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Phosphate_Buffer.md
  locator: '`data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:31; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: beee7ebacc6c58551ca09f5c841fc8f175e47fa7befcad1f0cf0ed2d218ccf43
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml`,\
    \ retype or\n  suppress the four concentration and pH-qualified CultureMech surface\
    \ forms so\n  final SSSOM no longer emits them in `other`.\n- Major: remove `physicochemical_roles.BUFFER`\
    \ unless the buffer role is\n  supported by checked source evidence for this record."
- evidence_id: ev-cfe1054eccc3245c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1228,1992]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29","finding_id":"SEM:60d3271db8936719a28c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29","finding_id":"SEM:cf7c681a4686a8d77eef","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-572c3fb1e8102fe5
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1863],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","line":1865,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Sodium
    phosphate buffer"}],"identifier":"kgmicrobe.ingredient:sodium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate
    Buffer","ontology_source":"NCIT"},"preferred_term":"Sodium phosphate buffer","sssom_rows":[{"data_row":2595,"object_id":"NCIT:C29321","object_label":"Phosphate
    Buffer","predicate_id":"skos:closeMatch"},{"data_row":2596,"object_id":"kgmicrobe.ingredient:sodium_phosphate_buffer","object_label":"Sodium
    phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Phosphate_Buffer","synonym_count":5}'
  snapshot_sha256: ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29
- evidence_id: ev-66163b107051dcdc
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-84a952452c1bbbad]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-84a952452c1bbbad in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-afc2d0a63ba08b9e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-26fc0c1929509db2
  - ev-dafb129b63ddd401
  - ev-4a38c91bfd3b24f3
  - ev-861552643e4d2f7d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-349cec704d9e2505
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-b573132e4c56e662
  - ev-26fc0c1929509db2
  - ev-cfe1054eccc3245c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:39:29Z;
    reviewed SHA-256=ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29;
    current SHA-256=ce046dc294a3b03325e251676ea7f5e3c978dd81a122d187a110a35c58df5c29;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Phosphate_Buffer.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock-solution identity and close NCIT parent pass, but final SSSOM exports concentration/pH
    variants and BUFFER is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b573132e4c56e662
    - ev-26fc0c1929509db2
  - name: legacy-native-ids
    value: '["SEM:60d3271db8936719a28c","SEM:cf7c681a4686a8d77eef"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-26fc0c1929509db2
    - ev-b573132e4c56e662
    - ev-cfe1054eccc3245c
- assessment_id: a-572c3fb1e8102fe5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-b573132e4c56e662
  - ev-572c3fb1e8102fe5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b573132e4c56e662
    - ev-572c3fb1e8102fe5
findings:
- finding_id: rec-f-84a952452c1bbbad
  issue_key: mim-reconciliation-role-support-83eeb69b0585d6f4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sodium phosphate buffer'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-83eeb69b0585d6f4
  evidence_ids:
  - ev-b573132e4c56e662
  - ev-572c3fb1e8102fe5
  - ev-66163b107051dcdc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-84a952452c1bbbad
actions:
- action_id: rec-action-84a952452c1bbbad
  description: 'Reassess prediction-only role support: Sodium phosphate buffer'
  finding_ids:
  - rec-f-84a952452c1bbbad
  target_ids:
  - record-83eeb69b0585d6f4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Phosphate_Buffer.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
