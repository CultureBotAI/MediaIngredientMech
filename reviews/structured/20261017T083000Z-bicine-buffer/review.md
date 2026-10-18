# Per-record structured review: Bicine_Buffer (data/ingredients/mapped/Bicine_Buffer.yaml)

- Review: 20261017T083000Z-bicine-buffer
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bicine_Buffer (data/ingredients/mapped/Bicine_Buffer.yaml, record-402707baebee4157, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bicine_Buffer.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bicine_Buffer.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-402707baebee4157 | data/ingredients/mapped/Bicine_Buffer.yaml | maintained | Bicine_Buffer |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-402707baebee4157 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-402707baebee4157 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-402707baebee4157 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-402707baebee4157.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-402707baebee4157.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:49:52Z; reviewed SHA-256=690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab; current SHA-256=690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab; hash_changed=False. Reports=["reports/yaml_record_review/Bicine_Buffer.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The surviving exact CHEBI BICINE buffer identity, absorbed Bicine synonym, CAS, structure fields, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-402707baebee4157.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-402707baebee4157: Reassess prediction-only or empty role support: Bicine_Buffer

major / open / confirmed; issue key: mim-reconciliation-role-support-402707baebee4157.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-402707baebee4157

Reassess prediction-only or empty role support: Bicine_Buffer

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-469b2ece2ff01669 | data/ingredients/mapped/Bicine_Buffer.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[586],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:40957","line":588,"mapping_status":"MAPPED","ontology_id":"CHEBI:40957","preferred_term":"BICINE buffer"}],"identifier":"CHEBI:40957","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:40957","ontology_label":"N,N-bis(2-hydroxyethyl)glycine","ontology_source":"CHEBI"},"preferred_term":"BICINE buffer","sssom_rows":[{"data_row":543,"object_id":"CHEBI:40957","object_label":"N,N-bis(2-hydroxyethyl)glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bicine_Buffer","synonym_count":2} |
| ev-0db03dbce461835a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [586] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1c97701166205502 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bicine_Buffer; data-row positions=[543] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":543,"object_id":"CHEBI:40957","object_label":"N,N-bis(2-hydroxyethyl)glycine","other":"Bicine&#124;CAS:150-25-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Bicine_Buffer","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-149260e229fd2f55 | docs/data/mapped_ingredients.csv; CSV lines=[588] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:40957","line":588,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:40957","preferred_term":"BICINE buffer","total_occurrences":"7"}] |
| ev-d7e266dea73b680d | reports/yaml_record_review/Bicine_Buffer.md; &#96;data/ingredients/mapped/Bicine_Buffer.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:32; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4df02e779267b860 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1699] | context_only | [{"current_record_sha256":"690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab","finding_id":"SEM:aebe10ac1866729e8ccc","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-767cd3387c3fbfd5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Bicine_Buffer.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bicine-buffer
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bicine_Buffer (data/ingredients/mapped/Bicine_Buffer.yaml)'
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
summary: Per-record structured review for Bicine_Buffer (data/ingredients/mapped/Bicine_Buffer.yaml,
  record-402707baebee4157, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bicine_Buffer.yaml
    sha256: 690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Bicine_Buffer.md
    sha256: b27679b7fdf433e79092498a55f90d580bc764b8249df63cfbdd2afe685e17bd
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-402707baebee4157
  path: data/ingredients/mapped/Bicine_Buffer.yaml
  label: Bicine_Buffer
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bicine_Buffer.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bicine_Buffer.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bicine_Buffer.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-402707baebee4157
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-402707baebee4157
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-402707baebee4157
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-402707baebee4157
evidence:
- evidence_id: ev-469b2ece2ff01669
  kind: record_content
  reference: data/ingredients/mapped/Bicine_Buffer.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[586],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:40957","line":588,"mapping_status":"MAPPED","ontology_id":"CHEBI:40957","preferred_term":"BICINE
    buffer"}],"identifier":"CHEBI:40957","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:40957","ontology_label":"N,N-bis(2-hydroxyethyl)glycine","ontology_source":"CHEBI"},"preferred_term":"BICINE
    buffer","sssom_rows":[{"data_row":543,"object_id":"CHEBI:40957","object_label":"N,N-bis(2-hydroxyethyl)glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bicine_Buffer","synonym_count":2}'
  snapshot_sha256: 690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab
- evidence_id: ev-0db03dbce461835a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [586]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1c97701166205502
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bicine_Buffer; data-row positions=[543]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":543,"object_id":"CHEBI:40957","object_label":"N,N-bis(2-hydroxyethyl)glycine","other":"Bicine|CAS:150-25-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Bicine_Buffer","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-149260e229fd2f55
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[588]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:40957","line":588,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:40957","preferred_term":"BICINE
    buffer","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d7e266dea73b680d
  kind: prior_review
  reference: reports/yaml_record_review/Bicine_Buffer.md
  locator: '`data/ingredients/mapped/Bicine_Buffer.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:32; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b27679b7fdf433e79092498a55f90d580bc764b8249df63cfbdd2afe685e17bd
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-4df02e779267b860
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1699]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab","finding_id":"SEM:aebe10ac1866729e8ccc","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-767cd3387c3fbfd5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Bicine_Buffer.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d3c08001853bdd0a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-402707baebee4157
  evidence_ids:
  - ev-469b2ece2ff01669
  - ev-0db03dbce461835a
  - ev-1c97701166205502
  - ev-149260e229fd2f55
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1cf57d7a84dd5d69
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-402707baebee4157
  evidence_ids:
  - ev-d7e266dea73b680d
  - ev-469b2ece2ff01669
  - ev-4df02e779267b860
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:49:52Z;
    reviewed SHA-256=690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab;
    current SHA-256=690ca43a7c43f5b5c70498026ac073fefcc8d9d066015c57129bd93755f42aab;
    hash_changed=False. Reports=["reports/yaml_record_review/Bicine_Buffer.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The surviving exact
    CHEBI BICINE buffer identity, absorbed Bicine synonym, CAS, structure fields,
    SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:aebe10ac1866729e8ccc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-469b2ece2ff01669
    - ev-d7e266dea73b680d
    - ev-4df02e779267b860
- assessment_id: a-role-402707baebee4157
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-402707baebee4157
  evidence_ids:
  - ev-469b2ece2ff01669
  - ev-767cd3387c3fbfd5
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-469b2ece2ff01669
    - ev-767cd3387c3fbfd5
findings:
- finding_id: rec-f-role-402707baebee4157
  issue_key: mim-reconciliation-role-support-402707baebee4157
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Bicine_Buffer'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-402707baebee4157
  evidence_ids:
  - ev-469b2ece2ff01669
  - ev-767cd3387c3fbfd5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bicine_Buffer.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-402707baebee4157
  description: 'Reassess prediction-only or empty role support: Bicine_Buffer'
  finding_ids:
  - rec-f-role-402707baebee4157
  target_ids:
  - record-402707baebee4157
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bicine_Buffer.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
