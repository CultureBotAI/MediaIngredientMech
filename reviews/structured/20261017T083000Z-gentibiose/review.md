# Per-record structured review: Gentibiose (data/ingredients/mapped/Gentibiose.yaml)

- Review: 20261017T083000Z-gentibiose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Gentibiose (data/ingredients/mapped/Gentibiose.yaml, record-ce967ff2a602818f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Gentibiose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Gentibiose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ce967ff2a602818f | data/ingredients/mapped/Gentibiose.yaml | maintained | Gentibiose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ce967ff2a602818f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ce967ff2a602818f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ce967ff2a602818f | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ce967ff2a602818f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ce967ff2a602818f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z; reviewed SHA-256=c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b; current SHA-256=c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b; hash_changed=False. Reports=["reports/yaml_record_review/Gentibiose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed gentiobiose identity passes, but CARBON_SOURCE is computational and the preferred term is misspelled.

### Historical provisional-role concern

evidence: concern. Targets: record-ce967ff2a602818f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8c55b534f16437ad: Reassess prediction-only role support: Gentibiose

major / open / confirmed; issue key: mim-reconciliation-role-support-ce967ff2a602818f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8c55b534f16437ad

Reassess prediction-only role support: Gentibiose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-88c813c3d181197c | data/ingredients/mapped/Gentibiose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28066","line":1049,"mapping_status":"MAPPED","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose"}],"identifier":"CHEBI:28066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28066","ontology_label":"gentiobiose","ontology_source":"CHEBI"},"preferred_term":"Gentibiose","sssom_rows":[{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentibiose","synonym_count":1} |
| ev-51e8076040c85de4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1047] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cf8f325f2f65b32c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Gentibiose; data-row positions=[1292] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","other":"beta-D-glucopyranosyl-(1-&gt;6)-D-glucopyranose&#124;CAS:554-91-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Gentibiose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-395daf954767c2c7 | docs/data/mapped_ingredients.csv; CSV lines=[1049] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28066","line":1049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose","total_occurrences":"0"}] |
| ev-e9447a1bbce0c7d6 | reports/yaml_record_review/Gentibiose.md; &#96;data/ingredients/mapped/Gentibiose.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:35; Completeness:56; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3f978b6bff684568 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[658,1545] | context_only | [{"current_record_sha256":"c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b","finding_id":"SEM:2182da5a9a975b91c87c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b","finding_id":"SEM:685ec2e2f888269efab8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2d74636f1f0a777c | data/ingredients/mapped/Gentibiose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28066","line":1049,"mapping_status":"MAPPED","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose"}],"identifier":"CHEBI:28066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28066","ontology_label":"gentiobiose","ontology_source":"CHEBI"},"preferred_term":"Gentibiose","sssom_rows":[{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentibiose","synonym_count":1} |
| ev-a26bf8060e6c0c89 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-8c55b534f16437ad] | context_only | Predecessor structured review finding f-8c55b534f16437ad in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-gentibiose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Gentibiose (data/ingredients/mapped/Gentibiose.yaml)'
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
summary: Per-record structured review for Gentibiose (data/ingredients/mapped/Gentibiose.yaml,
  record-ce967ff2a602818f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Gentibiose.yaml
    sha256: c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Gentibiose.md
    sha256: 5fd45331fb1b6fa1d30acb5481636ca7e1d027d78241e7c02a575a839fd89561
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ce967ff2a602818f
  path: data/ingredients/mapped/Gentibiose.yaml
  label: Gentibiose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gentibiose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Gentibiose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Gentibiose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ce967ff2a602818f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-88c813c3d181197c
  - ev-51e8076040c85de4
  - ev-cf8f325f2f65b32c
  - ev-395daf954767c2c7
  - ev-2d74636f1f0a777c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-88c813c3d181197c
  - ev-3f978b6bff684568
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-e9447a1bbce0c7d6
  - ev-3f978b6bff684568
  - ev-a26bf8060e6c0c89
evidence:
- evidence_id: ev-88c813c3d181197c
  kind: record_content
  reference: data/ingredients/mapped/Gentibiose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28066","line":1049,"mapping_status":"MAPPED","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose"}],"identifier":"CHEBI:28066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28066","ontology_label":"gentiobiose","ontology_source":"CHEBI"},"preferred_term":"Gentibiose","sssom_rows":[{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentibiose","synonym_count":1}'
  snapshot_sha256: c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b
- evidence_id: ev-51e8076040c85de4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1047]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cf8f325f2f65b32c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Gentibiose; data-row positions=[1292]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","other":"beta-D-glucopyranosyl-(1->6)-D-glucopyranose|CAS:554-91-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Gentibiose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-395daf954767c2c7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1049]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28066","line":1049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e9447a1bbce0c7d6
  kind: prior_review
  reference: reports/yaml_record_review/Gentibiose.md
  locator: '`data/ingredients/mapped/Gentibiose.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:35; Completeness:56; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5fd45331fb1b6fa1d30acb5481636ca7e1d027d78241e7c02a575a839fd89561
  quote: "Recommended Edits:\n- Major: replace `CARBON_SOURCE` with source-backed\
    \ evidence or remove the role,\n  then rerun strict validation.\n- Minor: change\
    \ `preferred_term` from `Gentibiose` to `Gentiobiose`; regenerate\n  final SSSOM\
    \ and rerun SSSOM invariants so the subject label updates too."
- evidence_id: ev-3f978b6bff684568
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[658,1545]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b","finding_id":"SEM:2182da5a9a975b91c87c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b","finding_id":"SEM:685ec2e2f888269efab8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2d74636f1f0a777c
  kind: record_content
  reference: data/ingredients/mapped/Gentibiose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28066","line":1049,"mapping_status":"MAPPED","ontology_id":"CHEBI:28066","preferred_term":"Gentibiose"}],"identifier":"CHEBI:28066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28066","ontology_label":"gentiobiose","ontology_source":"CHEBI"},"preferred_term":"Gentibiose","sssom_rows":[{"data_row":1292,"object_id":"CHEBI:28066","object_label":"gentiobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentibiose","synonym_count":1}'
  snapshot_sha256: c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b
- evidence_id: ev-a26bf8060e6c0c89
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-8c55b534f16437ad]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8c55b534f16437ad in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-b7774708ad31c762
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-88c813c3d181197c
  - ev-51e8076040c85de4
  - ev-cf8f325f2f65b32c
  - ev-395daf954767c2c7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-facbb8ad3db3567c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-e9447a1bbce0c7d6
  - ev-88c813c3d181197c
  - ev-3f978b6bff684568
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z;
    reviewed SHA-256=c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b;
    current SHA-256=c1ec749eb289b72ffcbab4e33ee66694259a5de1ab9c4df8769859f2f062341b;
    hash_changed=False. Reports=["reports/yaml_record_review/Gentibiose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    gentiobiose identity passes, but CARBON_SOURCE is computational and the preferred
    term is misspelled.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e9447a1bbce0c7d6
    - ev-88c813c3d181197c
  - name: legacy-native-ids
    value: '["SEM:2182da5a9a975b91c87c","SEM:685ec2e2f888269efab8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-88c813c3d181197c
    - ev-e9447a1bbce0c7d6
    - ev-3f978b6bff684568
- assessment_id: a-2d74636f1f0a777c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-e9447a1bbce0c7d6
  - ev-2d74636f1f0a777c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e9447a1bbce0c7d6
    - ev-2d74636f1f0a777c
findings:
- finding_id: rec-f-8c55b534f16437ad
  issue_key: mim-reconciliation-role-support-ce967ff2a602818f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Gentibiose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce967ff2a602818f
  evidence_ids:
  - ev-e9447a1bbce0c7d6
  - ev-2d74636f1f0a777c
  - ev-a26bf8060e6c0c89
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gentibiose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-8c55b534f16437ad
actions:
- action_id: rec-action-8c55b534f16437ad
  description: 'Reassess prediction-only role support: Gentibiose'
  finding_ids:
  - rec-f-8c55b534f16437ad
  target_ids:
  - record-ce967ff2a602818f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gentibiose.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
