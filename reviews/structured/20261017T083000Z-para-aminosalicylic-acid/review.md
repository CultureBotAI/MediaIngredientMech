# Per-record structured review: Para-aminosalicylic_Acid (data/ingredients/mapped/Para-aminosalicylic_Acid.yaml)

- Review: 20261017T083000Z-para-aminosalicylic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Para-aminosalicylic_Acid (data/ingredients/mapped/Para-aminosalicylic_Acid.yaml, record-2987a2a6310f8ad8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Para-aminosalicylic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Para-aminosalicylic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2987a2a6310f8ad8 | data/ingredients/mapped/Para-aminosalicylic_Acid.yaml | maintained | Para-aminosalicylic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2987a2a6310f8ad8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2987a2a6310f8ad8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2987a2a6310f8ad8 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2987a2a6310f8ad8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2987a2a6310f8ad8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:38:53Z; reviewed SHA-256=3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10; current SHA-256=3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10; hash_changed=False. Reports=["reports/yaml_record_review/Para-aminosalicylic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-derived CHEBI:27565 identity passes, but AMINO_ACID_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-2987a2a6310f8ad8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1f3279ef3e4dc47e: Reassess prediction-only role support: para-aminosalicylic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-2987a2a6310f8ad8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1f3279ef3e4dc47e

Reassess prediction-only role support: para-aminosalicylic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b03b76b12fd3ac2f | data/ingredients/mapped/Para-aminosalicylic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1616],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27565","line":1618,"mapping_status":"MAPPED","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic acid"}],"identifier":"CHEBI:27565","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:27565","ontology_label":"4-aminosalicylic acid","ontology_source":"CHEBI"},"preferred_term":"para-aminosalicylic acid","sssom_rows":[{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Para-aminosalicylic_Acid","synonym_count":1} |
| ev-a999e95018a52b69 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1616] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-becaec876172aae5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Para-aminosalicylic_Acid; data-row positions=[2201] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic acid","other":"4-amino-2-hydroxybenzoic acid&#124;CAS:65-49-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Para-aminosalicylic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-2f398016495802f4 | docs/data/mapped_ingredients.csv; CSV lines=[1618] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27565","line":1618,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic acid","total_occurrences":"0"}] |
| ev-4511f54874436552 | reports/yaml_record_review/Para-aminosalicylic_Acid.md; &#96;data/ingredients/mapped/Para-aminosalicylic_Acid.yaml&#96;:2; Verdict:4; Identity:9; Validation:19; Evidence:30; Completeness:40; Recommended Edits:46 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f40773c3bce6db63 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1096,1627] | context_only | [{"current_record_sha256":"3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10","finding_id":"SEM:e55de3b5738f68010c1f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10","finding_id":"SEM:2d4e7a6c8ffc8cd1a453","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-703853506344ac4e | data/ingredients/mapped/Para-aminosalicylic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1616],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27565","line":1618,"mapping_status":"MAPPED","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic acid"}],"identifier":"CHEBI:27565","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:27565","ontology_label":"4-aminosalicylic acid","ontology_source":"CHEBI"},"preferred_term":"para-aminosalicylic acid","sssom_rows":[{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Para-aminosalicylic_Acid","synonym_count":1} |
| ev-834e3f9bc074e4ae | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-1f3279ef3e4dc47e] | context_only | Predecessor structured review finding f-1f3279ef3e4dc47e in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-para-aminosalicylic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Para-aminosalicylic_Acid (data/ingredients/mapped/Para-aminosalicylic_Acid.yaml)'
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
summary: Per-record structured review for Para-aminosalicylic_Acid (data/ingredients/mapped/Para-aminosalicylic_Acid.yaml,
  record-2987a2a6310f8ad8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
    sha256: 3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10
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
  - path: reports/yaml_record_review/Para-aminosalicylic_Acid.md
    sha256: 1da2d54c64e16241b7b94c3ea9d462162dad828b4474560afb1030aa8c3e095d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2987a2a6310f8ad8
  path: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
  label: Para-aminosalicylic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Para-aminosalicylic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2987a2a6310f8ad8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-b03b76b12fd3ac2f
  - ev-a999e95018a52b69
  - ev-becaec876172aae5
  - ev-2f398016495802f4
  - ev-703853506344ac4e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-b03b76b12fd3ac2f
  - ev-f40773c3bce6db63
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-4511f54874436552
  - ev-f40773c3bce6db63
  - ev-834e3f9bc074e4ae
evidence:
- evidence_id: ev-b03b76b12fd3ac2f
  kind: record_content
  reference: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1616],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27565","line":1618,"mapping_status":"MAPPED","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic
    acid"}],"identifier":"CHEBI:27565","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:27565","ontology_label":"4-aminosalicylic
    acid","ontology_source":"CHEBI"},"preferred_term":"para-aminosalicylic acid","sssom_rows":[{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Para-aminosalicylic_Acid","synonym_count":1}'
  snapshot_sha256: 3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10
- evidence_id: ev-a999e95018a52b69
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1616]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-becaec876172aae5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Para-aminosalicylic_Acid; data-row positions=[2201]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic
    acid","other":"4-amino-2-hydroxybenzoic acid|CAS:65-49-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Para-aminosalicylic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2f398016495802f4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1618]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27565","line":1618,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4511f54874436552
  kind: prior_review
  reference: reports/yaml_record_review/Para-aminosalicylic_Acid.md
  locator: '`data/ingredients/mapped/Para-aminosalicylic_Acid.yaml`:2; Verdict:4;
    Identity:9; Validation:19; Evidence:30; Completeness:40; Recommended Edits:46'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1da2d54c64e16241b7b94c3ea9d462162dad828b4474560afb1030aa8c3e095d
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Para-aminosalicylic_Acid.yaml`,\
    \ either\n  replace `nutritional_roles.AMINO_ACID_SOURCE` with cited source evidence,\
    \ or\n  remove the provisional role facet until source-backed role evidence is\n\
    \  curated."
- evidence_id: ev-f40773c3bce6db63
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1096,1627]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10","finding_id":"SEM:e55de3b5738f68010c1f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10","finding_id":"SEM:2d4e7a6c8ffc8cd1a453","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-703853506344ac4e
  kind: record_content
  reference: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1616],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27565","line":1618,"mapping_status":"MAPPED","ontology_id":"CHEBI:27565","preferred_term":"para-aminosalicylic
    acid"}],"identifier":"CHEBI:27565","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:27565","ontology_label":"4-aminosalicylic
    acid","ontology_source":"CHEBI"},"preferred_term":"para-aminosalicylic acid","sssom_rows":[{"data_row":2201,"object_id":"CHEBI:27565","object_label":"4-aminosalicylic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Para-aminosalicylic_Acid","synonym_count":1}'
  snapshot_sha256: 3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10
- evidence_id: ev-834e3f9bc074e4ae
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-1f3279ef3e4dc47e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1f3279ef3e4dc47e in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-6be22fb4ef992067
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-b03b76b12fd3ac2f
  - ev-a999e95018a52b69
  - ev-becaec876172aae5
  - ev-2f398016495802f4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0f97923e3bbf0ad7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-4511f54874436552
  - ev-b03b76b12fd3ac2f
  - ev-f40773c3bce6db63
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:38:53Z;
    reviewed SHA-256=3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10;
    current SHA-256=3786e5420419e1692f1c87c804e1faf19ae88b5940f3e7314fc109942de15d10;
    hash_changed=False. Reports=["reports/yaml_record_review/Para-aminosalicylic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-derived
    CHEBI:27565 identity passes, but AMINO_ACID_SOURCE is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4511f54874436552
    - ev-b03b76b12fd3ac2f
  - name: legacy-native-ids
    value: '["SEM:e55de3b5738f68010c1f","SEM:2d4e7a6c8ffc8cd1a453"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b03b76b12fd3ac2f
    - ev-4511f54874436552
    - ev-f40773c3bce6db63
- assessment_id: a-703853506344ac4e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-4511f54874436552
  - ev-703853506344ac4e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4511f54874436552
    - ev-703853506344ac4e
findings:
- finding_id: rec-f-1f3279ef3e4dc47e
  issue_key: mim-reconciliation-role-support-2987a2a6310f8ad8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: para-aminosalicylic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2987a2a6310f8ad8
  evidence_ids:
  - ev-4511f54874436552
  - ev-703853506344ac4e
  - ev-834e3f9bc074e4ae
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-1f3279ef3e4dc47e
actions:
- action_id: rec-action-1f3279ef3e4dc47e
  description: 'Reassess prediction-only role support: para-aminosalicylic acid'
  finding_ids:
  - rec-f-1f3279ef3e4dc47e
  target_ids:
  - record-2987a2a6310f8ad8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Para-aminosalicylic_Acid.yaml
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
