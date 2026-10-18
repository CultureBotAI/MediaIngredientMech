# Per-record structured review: Na3-edta (data/ingredients/mapped/Na3-edta.yaml)

- Review: 20261017T083000Z-na3-edta
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na3-edta (data/ingredients/mapped/Na3-edta.yaml, record-9bd12c791d986e3f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na3-edta.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na3-edta.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9bd12c791d986e3f | data/ingredients/mapped/Na3-edta.yaml | maintained | Na3-edta |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9bd12c791d986e3f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9bd12c791d986e3f | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9bd12c791d986e3f | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9bd12c791d986e3f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9bd12c791d986e3f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z; reviewed SHA-256=ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a; current SHA-256=ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a; hash_changed=False. Reports=["reports/yaml_record_review/Na3-edta.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63125 EDTA trisodium identity passes, but final other has a disodium alias and CHELATOR is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-9bd12c791d986e3f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-54cef632675df65b: Reassess prediction-only role support: Na3-EDTA

major / open / confirmed; issue key: mim-reconciliation-role-support-9bd12c791d986e3f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-54cef632675df65b

Reassess prediction-only role support: Na3-EDTA

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b0671b70b8ea27be | data/ingredients/mapped/Na3-edta.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63125","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA"}],"identifier":"CHEBI:63125","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63125","ontology_label":"EDTA trisodium salt","ontology_source":"CHEBI"},"preferred_term":"Na3-EDTA","sssom_rows":[{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA trisodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-edta","synonym_count":16} |
| ev-3e83fe2f04b702c1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1514] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-512879968abdaa91 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na3-edta; data-row positions=[2026] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA trisodium salt","other":"EDTA-3Na&#124;EDTA\u00b73Na&#124;EDTA\u30fb3Na&#124;EDTA 3Na&#124;(ethylenedinitrilo)tetraacetic acid trisodium salt&#124;EDTA di sodium salt&#124;EDTA trisodium&#124;N,N'-1,2-ethanediylbis[N-(carboxymethyl)glycine] trisodium salt&#124;edetate trisodium&#124;ethylenediaminetetraacetic acid trisodium salt&#124;trisodium 2,2'-({2-[(carboxylatomethyl)(carboxymethyl)amino]ethyl}imino)diacetate&#124;trisodium ethylenediaminetetraacetate&#124;trisodium salt of ethylenediaminetetraacetic acid&#124;CAS:150-38-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Na3-edta","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-fce2f02c2ba66847 | docs/data/mapped_ingredients.csv; CSV lines=[1516] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63125","line":1516,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"30","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA","total_occurrences":"30"}] |
| ev-73b2a86dcbe85585 | reports/yaml_record_review/Na3-edta.md; &#96;data/ingredients/mapped/Na3-edta.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:41; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-17f4f919a619c3d5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1021,1460] | context_only | [{"current_record_sha256":"ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a","finding_id":"SEM:f28d44ab9d4f7dedcbd2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a","finding_id":"SEM:b01c017814ef4cc0de50","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2d05a527991dd10c | data/ingredients/mapped/Na3-edta.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63125","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA"}],"identifier":"CHEBI:63125","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63125","ontology_label":"EDTA trisodium salt","ontology_source":"CHEBI"},"preferred_term":"Na3-EDTA","sssom_rows":[{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA trisodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-edta","synonym_count":16} |
| ev-4a2f941148c69f65 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-54cef632675df65b] | context_only | Predecessor structured review finding f-54cef632675df65b in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na3-edta
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na3-edta (data/ingredients/mapped/Na3-edta.yaml)'
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
summary: Per-record structured review for Na3-edta (data/ingredients/mapped/Na3-edta.yaml,
  record-9bd12c791d986e3f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na3-edta.yaml
    sha256: ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a
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
  - path: reports/yaml_record_review/Na3-edta.md
    sha256: dccace7183994dccc00d1fee044c2d3a548a54bcb515c1b401582d7460720c09
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9bd12c791d986e3f
  path: data/ingredients/mapped/Na3-edta.yaml
  label: Na3-edta
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na3-edta.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na3-edta.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na3-edta.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9bd12c791d986e3f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-b0671b70b8ea27be
  - ev-3e83fe2f04b702c1
  - ev-512879968abdaa91
  - ev-fce2f02c2ba66847
  - ev-2d05a527991dd10c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-b0671b70b8ea27be
  - ev-17f4f919a619c3d5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-73b2a86dcbe85585
  - ev-17f4f919a619c3d5
  - ev-4a2f941148c69f65
evidence:
- evidence_id: ev-b0671b70b8ea27be
  kind: record_content
  reference: data/ingredients/mapped/Na3-edta.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63125","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA"}],"identifier":"CHEBI:63125","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63125","ontology_label":"EDTA
    trisodium salt","ontology_source":"CHEBI"},"preferred_term":"Na3-EDTA","sssom_rows":[{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA
    trisodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-edta","synonym_count":16}'
  snapshot_sha256: ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a
- evidence_id: ev-3e83fe2f04b702c1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1514]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-512879968abdaa91
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na3-edta; data-row positions=[2026]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA
    trisodium salt","other":"EDTA-3Na|EDTA\u00b73Na|EDTA\u30fb3Na|EDTA 3Na|(ethylenedinitrilo)tetraacetic
    acid trisodium salt|EDTA di sodium salt|EDTA trisodium|N,N''-1,2-ethanediylbis[N-(carboxymethyl)glycine]
    trisodium salt|edetate trisodium|ethylenediaminetetraacetic acid trisodium salt|trisodium
    2,2''-({2-[(carboxylatomethyl)(carboxymethyl)amino]ethyl}imino)diacetate|trisodium
    ethylenediaminetetraacetate|trisodium salt of ethylenediaminetetraacetic acid|CAS:150-38-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Na3-edta","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fce2f02c2ba66847
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1516]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63125","line":1516,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"30","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA","total_occurrences":"30"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-73b2a86dcbe85585
  kind: prior_review
  reference: reports/yaml_record_review/Na3-edta.md
  locator: '`data/ingredients/mapped/Na3-edta.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:27; Completeness:41; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dccace7183994dccc00d1fee044c2d3a548a54bcb515c1b401582d7460720c09
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na3-edta.yaml`,\
    \ reject or delete\n  `EDTA di sodium salt` so it no longer publishes as an exact\
    \ `CHEBI:63125`\n  synonym. Rebuild final SSSOM and rerun final SSSOM validation\
    \ plus product\n  label validation.\n- Major: either remove `physicochemical_roles.CHELATOR`\
    \ or replace its\n  name-pattern placeholder with source-backed evidence from\
    \ maintained role-text\n  or literature inputs. Rerun strict validation and the\
    \ role/output SSSOM checks\n  after the role facet change."
- evidence_id: ev-17f4f919a619c3d5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1021,1460]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a","finding_id":"SEM:f28d44ab9d4f7dedcbd2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a","finding_id":"SEM:b01c017814ef4cc0de50","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2d05a527991dd10c
  kind: record_content
  reference: data/ingredients/mapped/Na3-edta.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63125","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:63125","preferred_term":"Na3-EDTA"}],"identifier":"CHEBI:63125","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63125","ontology_label":"EDTA
    trisodium salt","ontology_source":"CHEBI"},"preferred_term":"Na3-EDTA","sssom_rows":[{"data_row":2026,"object_id":"CHEBI:63125","object_label":"EDTA
    trisodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-edta","synonym_count":16}'
  snapshot_sha256: ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a
- evidence_id: ev-4a2f941148c69f65
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-54cef632675df65b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-54cef632675df65b in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-b0d5b60b0006df15
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-b0671b70b8ea27be
  - ev-3e83fe2f04b702c1
  - ev-512879968abdaa91
  - ev-fce2f02c2ba66847
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-05d8ea6360a7d4ca
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-73b2a86dcbe85585
  - ev-b0671b70b8ea27be
  - ev-17f4f919a619c3d5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z;
    reviewed SHA-256=ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a;
    current SHA-256=ea8dbade6d6bfd0bbb478bd146a1266dbb2742c7d022a3de16904465ea73238a;
    hash_changed=False. Reports=["reports/yaml_record_review/Na3-edta.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63125 EDTA
    trisodium identity passes, but final other has a disodium alias and CHELATOR is
    provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-73b2a86dcbe85585
    - ev-b0671b70b8ea27be
  - name: legacy-native-ids
    value: '["SEM:f28d44ab9d4f7dedcbd2","SEM:b01c017814ef4cc0de50"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b0671b70b8ea27be
    - ev-73b2a86dcbe85585
    - ev-17f4f919a619c3d5
- assessment_id: a-2d05a527991dd10c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-73b2a86dcbe85585
  - ev-2d05a527991dd10c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-73b2a86dcbe85585
    - ev-2d05a527991dd10c
findings:
- finding_id: rec-f-54cef632675df65b
  issue_key: mim-reconciliation-role-support-9bd12c791d986e3f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na3-EDTA'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9bd12c791d986e3f
  evidence_ids:
  - ev-73b2a86dcbe85585
  - ev-2d05a527991dd10c
  - ev-4a2f941148c69f65
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na3-edta.yaml
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
    finding_id: f-54cef632675df65b
actions:
- action_id: rec-action-54cef632675df65b
  description: 'Reassess prediction-only role support: Na3-EDTA'
  finding_ids:
  - rec-f-54cef632675df65b
  target_ids:
  - record-9bd12c791d986e3f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na3-edta.yaml
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
