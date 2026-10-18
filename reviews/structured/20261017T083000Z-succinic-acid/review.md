# Per-record structured review: Succinic_Acid (data/ingredients/mapped/Succinic_Acid.yaml)

- Review: 20261017T083000Z-succinic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Succinic_Acid (data/ingredients/mapped/Succinic_Acid.yaml, record-222db89547a201c2, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Succinic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Succinic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-222db89547a201c2 | data/ingredients/mapped/Succinic_Acid.yaml | maintained | Succinic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-222db89547a201c2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-222db89547a201c2 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-222db89547a201c2 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-222db89547a201c2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-222db89547a201c2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z; reviewed SHA-256=eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158; current SHA-256=eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158; hash_changed=False. Reports=["reports/yaml_record_review/Succinic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15741 identity, CAS, synonyms, and final SSSOM row pass, but carbon and energy roles are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-222db89547a201c2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-aeb09198ba32f71b: Reassess prediction-only role support: Succinic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-222db89547a201c2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-aeb09198ba32f71b

Reassess prediction-only role support: Succinic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-903f67deeb9bced5 | data/ingredients/mapped/Succinic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1906],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15741","line":1908,"mapping_status":"MAPPED","ontology_id":"CHEBI:15741","preferred_term":"Succinic acid"}],"identifier":"CHEBI:15741","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15741","ontology_label":"succinic acid","ontology_source":"CHEBI"},"preferred_term":"Succinic acid","sssom_rows":[{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinic_Acid","synonym_count":17} |
| ev-691486e7b588d7df | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1906] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5bd577e5dbb2c741 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Succinic_Acid; data-row positions=[2663] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic acid","other":"1,2-ethanedicarboxylic acid&#124;Bernsteinsaeure&#124;Butandisaeure&#124;Butanedionic acid&#124;Dihydrofumaric acid&#124;E363&#124;Ethylenesuccinic acid&#124;HOOC-CH2-CH2-COOH&#124;acide butanedioique&#124;acide succinique&#124;acidum succinicum&#124;amber acid&#124;asuccin&#124;butanedioic acid&#124;spirit of amber&#124;CAS:110-15-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Succinic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-1081714bbae30038 | docs/data/mapped_ingredients.csv; CSV lines=[1908] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15741","line":1908,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:15741","preferred_term":"Succinic acid","total_occurrences":"36"}] |
| ev-9aa6f03206e67cf5 | reports/yaml_record_review/Succinic_Acid.md; &#96;data/ingredients/mapped/Succinic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fbb36f3847eba870 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1255,1562,2064] | context_only | [{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:f2cc4cd510bb4b70f415","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:10f95710b1e7902dbe9d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:1c0f062bfdaf62200c57","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-eb7089747da32f97 | data/ingredients/mapped/Succinic_Acid.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1906],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15741","line":1908,"mapping_status":"MAPPED","ontology_id":"CHEBI:15741","preferred_term":"Succinic acid"}],"identifier":"CHEBI:15741","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15741","ontology_label":"succinic acid","ontology_source":"CHEBI"},"preferred_term":"Succinic acid","sssom_rows":[{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinic_Acid","synonym_count":17} |
| ev-64a302985c653e96 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-aeb09198ba32f71b] | context_only | Predecessor structured review finding f-aeb09198ba32f71b in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-succinic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Succinic_Acid (data/ingredients/mapped/Succinic_Acid.yaml)'
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
summary: Per-record structured review for Succinic_Acid (data/ingredients/mapped/Succinic_Acid.yaml,
  record-222db89547a201c2, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Succinic_Acid.yaml
    sha256: eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158
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
  - path: reports/yaml_record_review/Succinic_Acid.md
    sha256: ab45b649cede9a3a8be2f08281c76dab0f2c64215d9e10cd3e06b83522796787
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-222db89547a201c2
  path: data/ingredients/mapped/Succinic_Acid.yaml
  label: Succinic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Succinic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Succinic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-222db89547a201c2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-903f67deeb9bced5
  - ev-691486e7b588d7df
  - ev-5bd577e5dbb2c741
  - ev-1081714bbae30038
  - ev-eb7089747da32f97
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-903f67deeb9bced5
  - ev-fbb36f3847eba870
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-9aa6f03206e67cf5
  - ev-fbb36f3847eba870
  - ev-64a302985c653e96
evidence:
- evidence_id: ev-903f67deeb9bced5
  kind: record_content
  reference: data/ingredients/mapped/Succinic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1906],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15741","line":1908,"mapping_status":"MAPPED","ontology_id":"CHEBI:15741","preferred_term":"Succinic
    acid"}],"identifier":"CHEBI:15741","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15741","ontology_label":"succinic
    acid","ontology_source":"CHEBI"},"preferred_term":"Succinic acid","sssom_rows":[{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinic_Acid","synonym_count":17}'
  snapshot_sha256: eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158
- evidence_id: ev-691486e7b588d7df
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1906]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5bd577e5dbb2c741
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Succinic_Acid; data-row positions=[2663]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic
    acid","other":"1,2-ethanedicarboxylic acid|Bernsteinsaeure|Butandisaeure|Butanedionic
    acid|Dihydrofumaric acid|E363|Ethylenesuccinic acid|HOOC-CH2-CH2-COOH|acide butanedioique|acide
    succinique|acidum succinicum|amber acid|asuccin|butanedioic acid|spirit of amber|CAS:110-15-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Succinic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1081714bbae30038
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1908]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15741","line":1908,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:15741","preferred_term":"Succinic
    acid","total_occurrences":"36"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9aa6f03206e67cf5
  kind: prior_review
  reference: reports/yaml_record_review/Succinic_Acid.md
  locator: '`data/ingredients/mapped/Succinic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:30; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ab45b649cede9a3a8be2f08281c76dab0f2c64215d9e10cd3e06b83522796787
  quote: "Recommended Edits:\n- Major: either replace the provisional `CARBON_SOURCE`\
    \ and `ENERGY_SOURCE`\n  assertions in `data/ingredients/mapped/Succinic_Acid.yaml`\
    \ with inspected\n  CultureMech or literature evidence, or remove those role facets."
- evidence_id: ev-fbb36f3847eba870
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1255,1562,2064]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:f2cc4cd510bb4b70f415","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:10f95710b1e7902dbe9d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158","finding_id":"SEM:1c0f062bfdaf62200c57","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-eb7089747da32f97
  kind: record_content
  reference: data/ingredients/mapped/Succinic_Acid.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1906],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15741","line":1908,"mapping_status":"MAPPED","ontology_id":"CHEBI:15741","preferred_term":"Succinic
    acid"}],"identifier":"CHEBI:15741","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15741","ontology_label":"succinic
    acid","ontology_source":"CHEBI"},"preferred_term":"Succinic acid","sssom_rows":[{"data_row":2663,"object_id":"CHEBI:15741","object_label":"succinic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinic_Acid","synonym_count":17}'
  snapshot_sha256: eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158
- evidence_id: ev-64a302985c653e96
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-aeb09198ba32f71b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-aeb09198ba32f71b in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-842ef64b10c24922
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-903f67deeb9bced5
  - ev-691486e7b588d7df
  - ev-5bd577e5dbb2c741
  - ev-1081714bbae30038
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-55cc68945b4ee6a1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-9aa6f03206e67cf5
  - ev-903f67deeb9bced5
  - ev-fbb36f3847eba870
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z;
    reviewed SHA-256=eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158;
    current SHA-256=eb67f0d82fa4c400905625bc6638673db27639ace55ffc06440b1429dfc2d158;
    hash_changed=False. Reports=["reports/yaml_record_review/Succinic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15741
    identity, CAS, synonyms, and final SSSOM row pass, but carbon and energy roles
    are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9aa6f03206e67cf5
    - ev-903f67deeb9bced5
  - name: legacy-native-ids
    value: '["SEM:f2cc4cd510bb4b70f415","SEM:10f95710b1e7902dbe9d","SEM:1c0f062bfdaf62200c57"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-903f67deeb9bced5
    - ev-9aa6f03206e67cf5
    - ev-fbb36f3847eba870
- assessment_id: a-eb7089747da32f97
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-9aa6f03206e67cf5
  - ev-eb7089747da32f97
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9aa6f03206e67cf5
    - ev-eb7089747da32f97
findings:
- finding_id: rec-f-aeb09198ba32f71b
  issue_key: mim-reconciliation-role-support-222db89547a201c2
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Succinic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-222db89547a201c2
  evidence_ids:
  - ev-9aa6f03206e67cf5
  - ev-eb7089747da32f97
  - ev-64a302985c653e96
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinic_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-aeb09198ba32f71b
actions:
- action_id: rec-action-aeb09198ba32f71b
  description: 'Reassess prediction-only role support: Succinic acid'
  finding_ids:
  - rec-f-aeb09198ba32f71b
  target_ids:
  - record-222db89547a201c2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinic_Acid.yaml
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
