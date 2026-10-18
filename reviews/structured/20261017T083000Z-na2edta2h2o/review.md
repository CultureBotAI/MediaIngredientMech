# Per-record structured review: Na2edta2h2o (data/ingredients/mapped/Na2edta2h2o.yaml)

- Review: 20261017T083000Z-na2edta2h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2edta2h2o (data/ingredients/mapped/Na2edta2h2o.yaml, record-bcfb2c5a4216de6d, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2edta2h2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2edta2h2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bcfb2c5a4216de6d | data/ingredients/mapped/Na2edta2h2o.yaml | maintained | Na2edta2h2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bcfb2c5a4216de6d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-bcfb2c5a4216de6d | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bcfb2c5a4216de6d | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bcfb2c5a4216de6d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bcfb2c5a4216de6d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z; reviewed SHA-256=9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d; current SHA-256=9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d; hash_changed=False. Reports=["reports/yaml_record_review/Na2edta2h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:64758 EDTA disodium salt dihydrate identity passes, but CHELATOR is provisional and final other includes a catalog token.

### Historical provisional-role concern

evidence: concern. Targets: record-bcfb2c5a4216de6d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-3e2b9974207e4e65: Reassess prediction-only role support: Na2EDTA·2H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-bcfb2c5a4216de6d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-3e2b9974207e4e65

Reassess prediction-only role support: Na2EDTA·2H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-174897fb046eecb2 | data/ingredients/mapped/Na2edta2h2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1485],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1487,"mapping_status":"MAPPED","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":139,"total_occurrences":140},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2EDTA\u00b72H2O","sssom_rows":[{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA disodium salt dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2edta2h2o","synonym_count":17} |
| ev-7ad2d69c620719f3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1485] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6fdc10b1ef96a092 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2edta2h2o; data-row positions=[1993] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA disodium salt dihydrate","other":"EDTA disodium dihydrate&#124;Na2EDTA . 2H2O&#124;Na2EDTA \u00b7 2H2O&#124;Na2EDTA.2H2O&#124;Na2EDTA\u00b7 2H2O&#124;Na2H2EDTA.2H2O&#124;disodium (ethylenedinitrilo)tetraacetate dihydrate&#124;disodium EDTA dihydrate&#124;disodium edetate dihydrate&#124;ethylenediaminetetraacetic acid disodium salt dihydrate&#124;Na2EDTA\u20222H2O&#124;Na2EDTA\u20222H2O(Sigma ED255)&#124;disodium 2,2',2'',2'''-(ethane-1,2-diyldiammonio)tetraacetate--water (1/2)&#124;Na2-EDTA x 2 H2O&#124;CAS:6381-92-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2edta2h2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-72461ba8d03be2b8 | docs/data/mapped_ingredients.csv; CSV lines=[1487] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:64758","line":1487,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"139","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O","total_occurrences":"140"}] |
| ev-1787279f11d26d40 | reports/yaml_record_review/Na2edta2h2o.md; &#96;data/ingredients/mapped/Na2edta2h2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:48; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5c1b6603085003e9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[992,1648] | context_only | [{"current_record_sha256":"9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d","finding_id":"SEM:07c2d9f8ba538af3ac6b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d","finding_id":"SEM:27ada2bf3dcab970c342","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9cd6cf357721ccf2 | data/ingredients/mapped/Na2edta2h2o.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1485],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1487,"mapping_status":"MAPPED","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":139,"total_occurrences":140},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2EDTA\u00b72H2O","sssom_rows":[{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA disodium salt dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2edta2h2o","synonym_count":17} |
| ev-2bbf5013edf4ae1c | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-3e2b9974207e4e65] | context_only | Predecessor structured review finding f-3e2b9974207e4e65 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2edta2h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2edta2h2o (data/ingredients/mapped/Na2edta2h2o.yaml)'
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
summary: Per-record structured review for Na2edta2h2o (data/ingredients/mapped/Na2edta2h2o.yaml,
  record-bcfb2c5a4216de6d, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2edta2h2o.yaml
    sha256: 9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d
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
  - path: reports/yaml_record_review/Na2edta2h2o.md
    sha256: e4b8f42f54f49b14ddbdf6906522f587c2c98f3041453b1fdd9849fc12c9d75e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bcfb2c5a4216de6d
  path: data/ingredients/mapped/Na2edta2h2o.yaml
  label: Na2edta2h2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2edta2h2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2edta2h2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2edta2h2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bcfb2c5a4216de6d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-174897fb046eecb2
  - ev-7ad2d69c620719f3
  - ev-6fdc10b1ef96a092
  - ev-72461ba8d03be2b8
  - ev-9cd6cf357721ccf2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-174897fb046eecb2
  - ev-5c1b6603085003e9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-1787279f11d26d40
  - ev-5c1b6603085003e9
  - ev-2bbf5013edf4ae1c
evidence:
- evidence_id: ev-174897fb046eecb2
  kind: record_content
  reference: data/ingredients/mapped/Na2edta2h2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1485],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1487,"mapping_status":"MAPPED","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":139,"total_occurrences":140},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA
    disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2EDTA\u00b72H2O","sssom_rows":[{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA
    disodium salt dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2edta2h2o","synonym_count":17}'
  snapshot_sha256: 9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d
- evidence_id: ev-7ad2d69c620719f3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1485]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6fdc10b1ef96a092
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2edta2h2o; data-row positions=[1993]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA
    disodium salt dihydrate","other":"EDTA disodium dihydrate|Na2EDTA . 2H2O|Na2EDTA
    \u00b7 2H2O|Na2EDTA.2H2O|Na2EDTA\u00b7 2H2O|Na2H2EDTA.2H2O|disodium (ethylenedinitrilo)tetraacetate
    dihydrate|disodium EDTA dihydrate|disodium edetate dihydrate|ethylenediaminetetraacetic
    acid disodium salt dihydrate|Na2EDTA\u20222H2O|Na2EDTA\u20222H2O(Sigma ED255)|disodium
    2,2'',2'''',2''''''-(ethane-1,2-diyldiammonio)tetraacetate--water (1/2)|Na2-EDTA
    x 2 H2O|CAS:6381-92-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2edta2h2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-72461ba8d03be2b8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1487]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:64758","line":1487,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"139","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O","total_occurrences":"140"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1787279f11d26d40
  kind: prior_review
  reference: reports/yaml_record_review/Na2edta2h2o.md
  locator: '`data/ingredients/mapped/Na2edta2h2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:48; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e4b8f42f54f49b14ddbdf6906522f587c2c98f3041453b1fdd9849fc12c9d75e
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2edta2h2o.yaml`,\
    \ either remove\n  `physicochemical_roles.CHELATOR` or replace its ChEBI-ancestry\
    \ placeholder\n  with source-backed evidence from maintained role-text or literature\
    \ inputs.\n- Major: keep the Sigma ED255 source label as provenance only, or retype\
    \ it to a\n  catalog/provenance slot that is filtered from final SSSOM; rebuild\
    \ final SSSOM\n  and rerun the final SSSOM plus product label validators."
- evidence_id: ev-5c1b6603085003e9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[992,1648]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d","finding_id":"SEM:07c2d9f8ba538af3ac6b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d","finding_id":"SEM:27ada2bf3dcab970c342","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9cd6cf357721ccf2
  kind: record_content
  reference: data/ingredients/mapped/Na2edta2h2o.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1485],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1487,"mapping_status":"MAPPED","ontology_id":"CHEBI:64758","preferred_term":"Na2EDTA\u00b72H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":139,"total_occurrences":140},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA
    disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2EDTA\u00b72H2O","sssom_rows":[{"data_row":1993,"object_id":"CHEBI:64758","object_label":"EDTA
    disodium salt dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2edta2h2o","synonym_count":17}'
  snapshot_sha256: 9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d
- evidence_id: ev-2bbf5013edf4ae1c
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-3e2b9974207e4e65]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-3e2b9974207e4e65 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-bb1dd2ab7f93bab0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-174897fb046eecb2
  - ev-7ad2d69c620719f3
  - ev-6fdc10b1ef96a092
  - ev-72461ba8d03be2b8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c91f1c9484cdc00f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-1787279f11d26d40
  - ev-174897fb046eecb2
  - ev-5c1b6603085003e9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z;
    reviewed SHA-256=9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d;
    current SHA-256=9941e9676116dc1b9686f3219372b319ffdc423e28274f700fd3fc16d2ba944d;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2edta2h2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:64758
    EDTA disodium salt dihydrate identity passes, but CHELATOR is provisional and
    final other includes a catalog token.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1787279f11d26d40
    - ev-174897fb046eecb2
  - name: legacy-native-ids
    value: '["SEM:07c2d9f8ba538af3ac6b","SEM:27ada2bf3dcab970c342"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-174897fb046eecb2
    - ev-1787279f11d26d40
    - ev-5c1b6603085003e9
- assessment_id: a-9cd6cf357721ccf2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-1787279f11d26d40
  - ev-9cd6cf357721ccf2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1787279f11d26d40
    - ev-9cd6cf357721ccf2
findings:
- finding_id: rec-f-3e2b9974207e4e65
  issue_key: mim-reconciliation-role-support-bcfb2c5a4216de6d
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2EDTA·2H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bcfb2c5a4216de6d
  evidence_ids:
  - ev-1787279f11d26d40
  - ev-9cd6cf357721ccf2
  - ev-2bbf5013edf4ae1c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2edta2h2o.yaml
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
    finding_id: f-3e2b9974207e4e65
actions:
- action_id: rec-action-3e2b9974207e4e65
  description: 'Reassess prediction-only role support: Na2EDTA·2H2O'
  finding_ids:
  - rec-f-3e2b9974207e4e65
  target_ids:
  - record-bcfb2c5a4216de6d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2edta2h2o.yaml
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
