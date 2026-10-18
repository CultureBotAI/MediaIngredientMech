# Per-record structured review: Neomycin_Trisulfate_Salt_Hydrate (data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml)

- Review: 20261017T083000Z-neomycin-trisulfate-salt-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Neomycin_Trisulfate_Salt_Hydrate (data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml, record-182112569204d966, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-182112569204d966 | data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml | maintained | Neomycin_Trisulfate_Salt_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-182112569204d966 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-182112569204d966 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-182112569204d966 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-182112569204d966.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-182112569204d966.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z; reviewed SHA-256=876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf; current SHA-256=876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf; hash_changed=False. Reports=["reports/yaml_record_review/Neomycin_Trisulfate_Salt_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local hydrate registry identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-182112569204d966.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4505fbb8be33edcd: Reassess prediction-only role support: Neomycin trisulfate salt hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-182112569204d966.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4505fbb8be33edcd

Reassess prediction-only role support: Neomycin trisulfate salt hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5261dea957cee92d | data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_status":"MAPPED","ontology_id":"CHEBI:31635","preferred_term":"Neomycin trisulfate salt hydrate"}],"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:31635","ontology_label":"neomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Neomycin trisulfate salt hydrate","sssom_rows":[{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin sulfate","predicate_id":"skos:closeMatch"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin trisulfate salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Neomycin_Trisulfate_Salt_Hydrate","synonym_count":0} |
| ev-720785ad4bdb2ffe | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1539] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-047d337bd1e346e1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Neomycin_Trisulfate_Salt_Hydrate; data-row positions=[2058, 2059] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin sulfate","other":"CAS:1405-10-3","predicate_id":"skos:closeMatch","subject_id":"MIM:Neomycin_Trisulfate_Salt_Hydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin trisulfate salt hydrate","other":"CAS:1405-10-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Neomycin_Trisulfate_Salt_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-e2d99b44040fdd42 | docs/data/mapped_ingredients.csv; CSV lines=[1541] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31635","preferred_term":"Neomycin trisulfate salt hydrate","total_occurrences":"0"}] |
| ev-5ff6d603faa04991 | reports/yaml_record_review/Neomycin_Trisulfate_Salt_Hydrate.md; &#96;data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:29; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-34673ce959d4e9bf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1038,1708] | context_only | [{"current_record_sha256":"876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf","finding_id":"SEM:f2ded8802b8ea586dba6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf","finding_id":"SEM:0a5c433e21c7985f96c3","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a3c5394d9e68fe46 | data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_status":"MAPPED","ontology_id":"CHEBI:31635","preferred_term":"Neomycin trisulfate salt hydrate"}],"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:31635","ontology_label":"neomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Neomycin trisulfate salt hydrate","sssom_rows":[{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin sulfate","predicate_id":"skos:closeMatch"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin trisulfate salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Neomycin_Trisulfate_Salt_Hydrate","synonym_count":0} |
| ev-3b09ead0beb6cca6 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-4505fbb8be33edcd] | context_only | Predecessor structured review finding f-4505fbb8be33edcd in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-neomycin-trisulfate-salt-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Neomycin_Trisulfate_Salt_Hydrate (data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml)'
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
summary: Per-record structured review for Neomycin_Trisulfate_Salt_Hydrate (data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml,
  record-182112569204d966, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
    sha256: 876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf
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
  - path: reports/yaml_record_review/Neomycin_Trisulfate_Salt_Hydrate.md
    sha256: 060882a0272b6fc1b59719dfbcb1073779356ba4fef1eef9360d685d16268e5c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-182112569204d966
  path: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
  label: Neomycin_Trisulfate_Salt_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-182112569204d966
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5261dea957cee92d
  - ev-720785ad4bdb2ffe
  - ev-047d337bd1e346e1
  - ev-e2d99b44040fdd42
  - ev-a3c5394d9e68fe46
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5261dea957cee92d
  - ev-34673ce959d4e9bf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5ff6d603faa04991
  - ev-34673ce959d4e9bf
  - ev-3b09ead0beb6cca6
evidence:
- evidence_id: ev-5261dea957cee92d
  kind: record_content
  reference: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_status":"MAPPED","ontology_id":"CHEBI:31635","preferred_term":"Neomycin
    trisulfate salt hydrate"}],"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:31635","ontology_label":"neomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Neomycin trisulfate salt
    hydrate","sssom_rows":[{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin
    trisulfate salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Neomycin_Trisulfate_Salt_Hydrate","synonym_count":0}'
  snapshot_sha256: 876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf
- evidence_id: ev-720785ad4bdb2ffe
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1539]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-047d337bd1e346e1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Neomycin_Trisulfate_Salt_Hydrate; data-row positions=[2058,
    2059]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin
    sulfate","other":"CAS:1405-10-3","predicate_id":"skos:closeMatch","subject_id":"MIM:Neomycin_Trisulfate_Salt_Hydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin
    trisulfate salt hydrate","other":"CAS:1405-10-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Neomycin_Trisulfate_Salt_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e2d99b44040fdd42
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1541]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31635","preferred_term":"Neomycin
    trisulfate salt hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5ff6d603faa04991
  kind: prior_review
  reference: reports/yaml_record_review/Neomycin_Trisulfate_Salt_Hydrate.md
  locator: '`data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml`:2; Verdict:4;
    Identity:11; Validation:22; Evidence:29; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 060882a0272b6fc1b59719dfbcb1073779356ba4fef1eef9360d685d16268e5c
  quote: "Recommended Edits:\n- Major: in\n  `data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml`,\
    \ either\n  replace the provisional `SELECTIVE_AGENT` assertion with database\
    \ or\n  publication evidence at the role claim or remove it before rebuilding\n\
    \  downstream products."
- evidence_id: ev-34673ce959d4e9bf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1038,1708]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf","finding_id":"SEM:f2ded8802b8ea586dba6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf","finding_id":"SEM:0a5c433e21c7985f96c3","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a3c5394d9e68fe46
  kind: record_content
  reference: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","line":1541,"mapping_status":"MAPPED","ontology_id":"CHEBI:31635","preferred_term":"Neomycin
    trisulfate salt hydrate"}],"identifier":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:31635","ontology_label":"neomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Neomycin trisulfate salt
    hydrate","sssom_rows":[{"data_row":2058,"object_id":"CHEBI:31635","object_label":"neomycin
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":2059,"object_id":"kgmicrobe.compound:neomycin_trisulfate_salt_hydrate","object_label":"Neomycin
    trisulfate salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Neomycin_Trisulfate_Salt_Hydrate","synonym_count":0}'
  snapshot_sha256: 876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf
- evidence_id: ev-3b09ead0beb6cca6
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-4505fbb8be33edcd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4505fbb8be33edcd in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-4fdbfe2ea2ef58a3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5261dea957cee92d
  - ev-720785ad4bdb2ffe
  - ev-047d337bd1e346e1
  - ev-e2d99b44040fdd42
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6f6f7a90aa48c457
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5ff6d603faa04991
  - ev-5261dea957cee92d
  - ev-34673ce959d4e9bf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z;
    reviewed SHA-256=876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf;
    current SHA-256=876380652f045ae42f54946f4e769cbeed9e65f065eab12acd77de386ebe00cf;
    hash_changed=False. Reports=["reports/yaml_record_review/Neomycin_Trisulfate_Salt_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    hydrate registry identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5ff6d603faa04991
    - ev-5261dea957cee92d
  - name: legacy-native-ids
    value: '["SEM:f2ded8802b8ea586dba6","SEM:0a5c433e21c7985f96c3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5261dea957cee92d
    - ev-5ff6d603faa04991
    - ev-34673ce959d4e9bf
- assessment_id: a-a3c5394d9e68fe46
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5ff6d603faa04991
  - ev-a3c5394d9e68fe46
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5ff6d603faa04991
    - ev-a3c5394d9e68fe46
findings:
- finding_id: rec-f-4505fbb8be33edcd
  issue_key: mim-reconciliation-role-support-182112569204d966
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Neomycin trisulfate salt hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-182112569204d966
  evidence_ids:
  - ev-5ff6d603faa04991
  - ev-a3c5394d9e68fe46
  - ev-3b09ead0beb6cca6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
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
    finding_id: f-4505fbb8be33edcd
actions:
- action_id: rec-action-4505fbb8be33edcd
  description: 'Reassess prediction-only role support: Neomycin trisulfate salt hydrate'
  finding_ids:
  - rec-f-4505fbb8be33edcd
  target_ids:
  - record-182112569204d966
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml
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
