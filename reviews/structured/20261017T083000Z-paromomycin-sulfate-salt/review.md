# Per-record structured review: Paromomycin_Sulfate_Salt (data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml)

- Review: 20261017T083000Z-paromomycin-sulfate-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Paromomycin_Sulfate_Salt (data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml, record-c4a1845e3ea71940, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c4a1845e3ea71940 | data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml | maintained | Paromomycin_Sulfate_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c4a1845e3ea71940 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c4a1845e3ea71940 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c4a1845e3ea71940 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c4a1845e3ea71940.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c4a1845e3ea71940.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z; reviewed SHA-256=aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5; current SHA-256=aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5; hash_changed=False. Reports=["reports/yaml_record_review/Paromomycin_Sulfate_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-derived CHEBI:7935 identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-c4a1845e3ea71940.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-879d70ac99408a3e: Reassess prediction-only role support: Paromomycin sulfate salt

major / open / confirmed; issue key: mim-reconciliation-role-support-c4a1845e3ea71940.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-879d70ac99408a3e

Reassess prediction-only role support: Paromomycin sulfate salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-622e0450d5bbf9ad | data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7935","line":1622,"mapping_status":"MAPPED","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin sulfate salt"}],"identifier":"CHEBI:7935","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:7935","ontology_label":"paromomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Paromomycin sulfate salt","sssom_rows":[{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Paromomycin_Sulfate_Salt","synonym_count":1} |
| ev-7eb7302e4caf24a6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1620] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-398952f6e8792b87 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Paromomycin_Sulfate_Salt; data-row positions=[2207] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin sulfate","other":"(1R,2R,3S,4R,6S)-4,6-diamino-2-{[3-O-(2,6-diamino-2,6-dideoxy-beta-L-idopyranosyl)-beta-D-ribofuranosyl]oxy}-3-hydroxycyclohexyl 2-amino-2-deoxy-alpha-D-glucopyranoside sulfate&#124;CAS:1263-89-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Paromomycin_Sulfate_Salt","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-53cdae5c098b9595 | docs/data/mapped_ingredients.csv; CSV lines=[1622] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:7935","line":1622,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin sulfate salt","total_occurrences":"0"}] |
| ev-49b5a0d9e964758e | reports/yaml_record_review/Paromomycin_Sulfate_Salt.md; &#96;data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml&#96;:2; Verdict:4; Identity:9; Validation:18; Evidence:29; Completeness:40; Recommended Edits:46 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-94ebeeb2912ee229 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1097,1944] | context_only | [{"current_record_sha256":"aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5","finding_id":"SEM:7803dc4eeb162b5b5f2d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5","finding_id":"SEM:2091815294b85405d79b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-41f795b45f47d019 | data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7935","line":1622,"mapping_status":"MAPPED","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin sulfate salt"}],"identifier":"CHEBI:7935","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:7935","ontology_label":"paromomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Paromomycin sulfate salt","sssom_rows":[{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Paromomycin_Sulfate_Salt","synonym_count":1} |
| ev-91f417cd6cde1e5c | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-879d70ac99408a3e] | context_only | Predecessor structured review finding f-879d70ac99408a3e in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-paromomycin-sulfate-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Paromomycin_Sulfate_Salt (data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml)'
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
summary: Per-record structured review for Paromomycin_Sulfate_Salt (data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml,
  record-c4a1845e3ea71940, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
    sha256: aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Paromomycin_Sulfate_Salt.md
    sha256: 810b2c72a2508a5f72eccc95c757c60b7bea31ebf309e822e9786efd07596d35
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c4a1845e3ea71940
  path: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
  label: Paromomycin_Sulfate_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c4a1845e3ea71940
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-622e0450d5bbf9ad
  - ev-7eb7302e4caf24a6
  - ev-398952f6e8792b87
  - ev-53cdae5c098b9595
  - ev-41f795b45f47d019
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-622e0450d5bbf9ad
  - ev-94ebeeb2912ee229
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-49b5a0d9e964758e
  - ev-94ebeeb2912ee229
  - ev-91f417cd6cde1e5c
evidence:
- evidence_id: ev-622e0450d5bbf9ad
  kind: record_content
  reference: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7935","line":1622,"mapping_status":"MAPPED","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin
    sulfate salt"}],"identifier":"CHEBI:7935","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:7935","ontology_label":"paromomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Paromomycin sulfate salt","sssom_rows":[{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Paromomycin_Sulfate_Salt","synonym_count":1}'
  snapshot_sha256: aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5
- evidence_id: ev-7eb7302e4caf24a6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1620]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-398952f6e8792b87
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Paromomycin_Sulfate_Salt; data-row positions=[2207]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin
    sulfate","other":"(1R,2R,3S,4R,6S)-4,6-diamino-2-{[3-O-(2,6-diamino-2,6-dideoxy-beta-L-idopyranosyl)-beta-D-ribofuranosyl]oxy}-3-hydroxycyclohexyl
    2-amino-2-deoxy-alpha-D-glucopyranoside sulfate|CAS:1263-89-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Paromomycin_Sulfate_Salt","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-53cdae5c098b9595
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1622]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:7935","line":1622,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin
    sulfate salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-49b5a0d9e964758e
  kind: prior_review
  reference: reports/yaml_record_review/Paromomycin_Sulfate_Salt.md
  locator: '`data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml`:2; Verdict:4;
    Identity:9; Validation:18; Evidence:29; Completeness:40; Recommended Edits:46'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 810b2c72a2508a5f72eccc95c757c60b7bea31ebf309e822e9786efd07596d35
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml`,\
    \ either\n  replace `physicochemical_roles.SELECTIVE_AGENT` with cited source\
    \ evidence\n  that supports the selective-agent role for paromomycin sulfate,\
    \ or remove the\n  provisional role facet until source-backed role evidence is\
    \ curated."
- evidence_id: ev-94ebeeb2912ee229
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1097,1944]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5","finding_id":"SEM:7803dc4eeb162b5b5f2d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5","finding_id":"SEM:2091815294b85405d79b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-41f795b45f47d019
  kind: record_content
  reference: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7935","line":1622,"mapping_status":"MAPPED","ontology_id":"CHEBI:7935","preferred_term":"Paromomycin
    sulfate salt"}],"identifier":"CHEBI:7935","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:7935","ontology_label":"paromomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Paromomycin sulfate salt","sssom_rows":[{"data_row":2207,"object_id":"CHEBI:7935","object_label":"paromomycin
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Paromomycin_Sulfate_Salt","synonym_count":1}'
  snapshot_sha256: aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5
- evidence_id: ev-91f417cd6cde1e5c
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-879d70ac99408a3e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-879d70ac99408a3e in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-738447c45350f3c3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-622e0450d5bbf9ad
  - ev-7eb7302e4caf24a6
  - ev-398952f6e8792b87
  - ev-53cdae5c098b9595
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-09ed31240a170caa
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-49b5a0d9e964758e
  - ev-622e0450d5bbf9ad
  - ev-94ebeeb2912ee229
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z;
    reviewed SHA-256=aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5;
    current SHA-256=aef109d09c857f66543bd72b0d96aa4c89c6e30b5502c03377bf6ace94d14ab5;
    hash_changed=False. Reports=["reports/yaml_record_review/Paromomycin_Sulfate_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-derived
    CHEBI:7935 identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-49b5a0d9e964758e
    - ev-622e0450d5bbf9ad
  - name: legacy-native-ids
    value: '["SEM:7803dc4eeb162b5b5f2d","SEM:2091815294b85405d79b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-622e0450d5bbf9ad
    - ev-49b5a0d9e964758e
    - ev-94ebeeb2912ee229
- assessment_id: a-41f795b45f47d019
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-49b5a0d9e964758e
  - ev-41f795b45f47d019
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-49b5a0d9e964758e
    - ev-41f795b45f47d019
findings:
- finding_id: rec-f-879d70ac99408a3e
  issue_key: mim-reconciliation-role-support-c4a1845e3ea71940
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Paromomycin sulfate salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c4a1845e3ea71940
  evidence_ids:
  - ev-49b5a0d9e964758e
  - ev-41f795b45f47d019
  - ev-91f417cd6cde1e5c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-879d70ac99408a3e
actions:
- action_id: rec-action-879d70ac99408a3e
  description: 'Reassess prediction-only role support: Paromomycin sulfate salt'
  finding_ids:
  - rec-f-879d70ac99408a3e
  target_ids:
  - record-c4a1845e3ea71940
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
