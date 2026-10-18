# Per-record structured review: Racemomycin_E (data/ingredients/mapped/Racemomycin_E.yaml)

- Review: 20261017T083000Z-racemomycin-e
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Racemomycin_E (data/ingredients/mapped/Racemomycin_E.yaml, record-487c7813e991fbd8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Racemomycin_E.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Racemomycin_E.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-487c7813e991fbd8 | data/ingredients/mapped/Racemomycin_E.yaml | maintained | Racemomycin_E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-487c7813e991fbd8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-487c7813e991fbd8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-487c7813e991fbd8 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-487c7813e991fbd8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-487c7813e991fbd8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:45:49Z; reviewed SHA-256=da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592; current SHA-256=da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592; hash_changed=False. Reports=["reports/yaml_record_review/Racemomycin_E.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local Racemomycin E identity and MeSH parent pass, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-487c7813e991fbd8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6b368abad8e12dc7: Reassess prediction-only role support: Racemomycin E

major / open / confirmed; issue key: mim-reconciliation-role-support-487c7813e991fbd8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6b368abad8e12dc7

Reassess prediction-only role support: Racemomycin E

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e02fa5a49f42e57f | data/ingredients/mapped/Racemomycin_E.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1742],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_status":"MAPPED","ontology_id":"mesh:C019594","preferred_term":"Racemomycin E"}],"identifier":"kgmicrobe.compound:racemomycin_e","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C019594","ontology_label":"racemomycin","ontology_source":"MESH"},"preferred_term":"Racemomycin E","sssom_rows":[{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","predicate_id":"skos:broadMatch"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin E","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Racemomycin_E","synonym_count":0} |
| ev-56f7a94cd48ae0a3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1742] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5ebddb397cf050a1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Racemomycin_E; data-row positions=[2412, 2413] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Racemomycin_E","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin E","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Racemomycin_E","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-6e2afa2741c5af57 | docs/data/mapped_ingredients.csv; CSV lines=[1744] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C019594","preferred_term":"Racemomycin E","total_occurrences":"0"}] |
| ev-b7691c1badbbbfbe | reports/yaml_record_review/Racemomycin_E.md; &#96;data/ingredients/mapped/Racemomycin_E.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-21fd3bedb0a737cc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1164,1424] | context_only | [{"current_record_sha256":"da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592","finding_id":"SEM:d8fa366db256f3a6aad7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592","finding_id":"SEM:64949a9af58ca310c729","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-55fe9d244b1d116d | data/ingredients/mapped/Racemomycin_E.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1742],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_status":"MAPPED","ontology_id":"mesh:C019594","preferred_term":"Racemomycin E"}],"identifier":"kgmicrobe.compound:racemomycin_e","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C019594","ontology_label":"racemomycin","ontology_source":"MESH"},"preferred_term":"Racemomycin E","sssom_rows":[{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","predicate_id":"skos:broadMatch"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin E","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Racemomycin_E","synonym_count":0} |
| ev-a8f55f04a65aabe0 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-6b368abad8e12dc7] | context_only | Predecessor structured review finding f-6b368abad8e12dc7 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-racemomycin-e
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Racemomycin_E (data/ingredients/mapped/Racemomycin_E.yaml)'
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
summary: Per-record structured review for Racemomycin_E (data/ingredients/mapped/Racemomycin_E.yaml,
  record-487c7813e991fbd8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Racemomycin_E.yaml
    sha256: da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Racemomycin_E.md
    sha256: 7b89a8f701b0c00c61e6d45e6085a3c335dddef15a34bbd5dc8738749ab2e534
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-487c7813e991fbd8
  path: data/ingredients/mapped/Racemomycin_E.yaml
  label: Racemomycin_E
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Racemomycin_E.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Racemomycin_E.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Racemomycin_E.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-487c7813e991fbd8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-e02fa5a49f42e57f
  - ev-56f7a94cd48ae0a3
  - ev-5ebddb397cf050a1
  - ev-6e2afa2741c5af57
  - ev-55fe9d244b1d116d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-e02fa5a49f42e57f
  - ev-21fd3bedb0a737cc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-b7691c1badbbbfbe
  - ev-21fd3bedb0a737cc
  - ev-a8f55f04a65aabe0
evidence:
- evidence_id: ev-e02fa5a49f42e57f
  kind: record_content
  reference: data/ingredients/mapped/Racemomycin_E.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1742],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_status":"MAPPED","ontology_id":"mesh:C019594","preferred_term":"Racemomycin
    E"}],"identifier":"kgmicrobe.compound:racemomycin_e","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C019594","ontology_label":"racemomycin","ontology_source":"MESH"},"preferred_term":"Racemomycin
    E","sssom_rows":[{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","predicate_id":"skos:broadMatch"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin
    E","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Racemomycin_E","synonym_count":0}'
  snapshot_sha256: da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592
- evidence_id: ev-56f7a94cd48ae0a3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1742]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5ebddb397cf050a1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Racemomycin_E; data-row positions=[2412, 2413]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Racemomycin_E","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin
    E","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Racemomycin_E","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6e2afa2741c5af57
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1744]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C019594","preferred_term":"Racemomycin
    E","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b7691c1badbbbfbe
  kind: prior_review
  reference: reports/yaml_record_review/Racemomycin_E.md
  locator: '`data/ingredients/mapped/Racemomycin_E.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7b89a8f701b0c00c61e6d45e6085a3c335dddef15a34bbd5dc8738749ab2e534
- evidence_id: ev-21fd3bedb0a737cc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1164,1424]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592","finding_id":"SEM:d8fa366db256f3a6aad7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592","finding_id":"SEM:64949a9af58ca310c729","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-55fe9d244b1d116d
  kind: record_content
  reference: data/ingredients/mapped/Racemomycin_E.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1742],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:racemomycin_e","line":1744,"mapping_status":"MAPPED","ontology_id":"mesh:C019594","preferred_term":"Racemomycin
    E"}],"identifier":"kgmicrobe.compound:racemomycin_e","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C019594","ontology_label":"racemomycin","ontology_source":"MESH"},"preferred_term":"Racemomycin
    E","sssom_rows":[{"data_row":2412,"object_id":"mesh:C019594","object_label":"racemomycin","predicate_id":"skos:broadMatch"},{"data_row":2413,"object_id":"kgmicrobe.compound:racemomycin_e","object_label":"Racemomycin
    E","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Racemomycin_E","synonym_count":0}'
  snapshot_sha256: da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592
- evidence_id: ev-a8f55f04a65aabe0
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-6b368abad8e12dc7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6b368abad8e12dc7 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-ceb3f63ef4c3ac06
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-e02fa5a49f42e57f
  - ev-56f7a94cd48ae0a3
  - ev-5ebddb397cf050a1
  - ev-6e2afa2741c5af57
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7864106edc8efb46
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-b7691c1badbbbfbe
  - ev-e02fa5a49f42e57f
  - ev-21fd3bedb0a737cc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:45:49Z;
    reviewed SHA-256=da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592;
    current SHA-256=da451fa75decffab222bf5609caa734bb00c5b345e999c2c086e4ed33269a592;
    hash_changed=False. Reports=["reports/yaml_record_review/Racemomycin_E.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local Racemomycin
    E identity and MeSH parent pass, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b7691c1badbbbfbe
    - ev-e02fa5a49f42e57f
  - name: legacy-native-ids
    value: '["SEM:d8fa366db256f3a6aad7","SEM:64949a9af58ca310c729"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e02fa5a49f42e57f
    - ev-b7691c1badbbbfbe
    - ev-21fd3bedb0a737cc
- assessment_id: a-55fe9d244b1d116d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-b7691c1badbbbfbe
  - ev-55fe9d244b1d116d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b7691c1badbbbfbe
    - ev-55fe9d244b1d116d
findings:
- finding_id: rec-f-6b368abad8e12dc7
  issue_key: mim-reconciliation-role-support-487c7813e991fbd8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Racemomycin E'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-487c7813e991fbd8
  evidence_ids:
  - ev-b7691c1badbbbfbe
  - ev-55fe9d244b1d116d
  - ev-a8f55f04a65aabe0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Racemomycin_E.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-6b368abad8e12dc7
actions:
- action_id: rec-action-6b368abad8e12dc7
  description: 'Reassess prediction-only role support: Racemomycin E'
  finding_ids:
  - rec-f-6b368abad8e12dc7
  target_ids:
  - record-487c7813e991fbd8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Racemomycin_E.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
