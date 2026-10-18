# Per-record structured review: Palatinose_Hydrate (data/ingredients/mapped/Palatinose_Hydrate.yaml)

- Review: 20261017T083000Z-palatinose-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Palatinose_Hydrate (data/ingredients/mapped/Palatinose_Hydrate.yaml, record-db42c1305957dc5c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Palatinose_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Palatinose_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-db42c1305957dc5c | data/ingredients/mapped/Palatinose_Hydrate.yaml | maintained | Palatinose_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-db42c1305957dc5c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-db42c1305957dc5c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-db42c1305957dc5c | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-db42c1305957dc5c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-db42c1305957dc5c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:28:40Z; reviewed SHA-256=7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651; current SHA-256=7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651; hash_changed=False. Reports=["reports/yaml_record_review/Palatinose_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS hydrate identity and close parent row pass, but a registry sibling is missing and CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-db42c1305957dc5c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b72270c86b646407: Reassess prediction-only role support: palatinose hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-db42c1305957dc5c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b72270c86b646407

Reassess prediction-only role support: palatinose hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-379b78deb8107361 | data/ingredients/mapped/Palatinose_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1608],"raw_equal":true},"docs_rows":[{"identifier":"cas:343336-76-5","line":1610,"mapping_status":"MAPPED","ontology_id":"CHEBI:18394","preferred_term":"palatinose hydrate"}],"identifier":"cas:343336-76-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:18394","ontology_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","ontology_source":"CHEBI"},"preferred_term":"palatinose hydrate","sssom_rows":[{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","predicate_id":"skos:closeMatch"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Palatinose_Hydrate","synonym_count":0} |
| ev-b95c1d9c64e1e499 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1608] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9bb36c0285ba1c82 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Palatinose_Hydrate; data-row positions=[2191, 2192] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","other":"CAS:343336-76-5","predicate_id":"skos:closeMatch","subject_id":"MIM:Palatinose_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose hydrate","other":"CAS:343336-76-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Palatinose_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-001b8b26f25dd79c | docs/data/mapped_ingredients.csv; CSV lines=[1610] | supports | Published identity and count rows inspected: [{"identifier":"cas:343336-76-5","line":1610,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18394","preferred_term":"palatinose hydrate","total_occurrences":"0"}] |
| ev-0c56e53a687885fe | reports/yaml_record_review/Palatinose_Hydrate.md; &#96;data/ingredients/mapped/Palatinose_Hydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8114952aa531447b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1094,1407] | context_only | [{"current_record_sha256":"7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651","finding_id":"SEM:08d7cd089859cd906df9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651","finding_id":"SEM:20ea0b5654db8eb97bfb","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-085e29b75373042d | data/ingredients/mapped/Palatinose_Hydrate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1608],"raw_equal":true},"docs_rows":[{"identifier":"cas:343336-76-5","line":1610,"mapping_status":"MAPPED","ontology_id":"CHEBI:18394","preferred_term":"palatinose hydrate"}],"identifier":"cas:343336-76-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:18394","ontology_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","ontology_source":"CHEBI"},"preferred_term":"palatinose hydrate","sssom_rows":[{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","predicate_id":"skos:closeMatch"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Palatinose_Hydrate","synonym_count":0} |
| ev-1c82b5cc54bee1ee | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-b72270c86b646407] | context_only | Predecessor structured review finding f-b72270c86b646407 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-palatinose-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Palatinose_Hydrate (data/ingredients/mapped/Palatinose_Hydrate.yaml)'
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
summary: Per-record structured review for Palatinose_Hydrate (data/ingredients/mapped/Palatinose_Hydrate.yaml,
  record-db42c1305957dc5c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Palatinose_Hydrate.yaml
    sha256: 7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651
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
  - path: reports/yaml_record_review/Palatinose_Hydrate.md
    sha256: 32a8e9bc7025e8d55021623c51780d7d568fbb7450c6a718deef46572ee0d495
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-db42c1305957dc5c
  path: data/ingredients/mapped/Palatinose_Hydrate.yaml
  label: Palatinose_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Palatinose_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Palatinose_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Palatinose_Hydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-db42c1305957dc5c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-379b78deb8107361
  - ev-b95c1d9c64e1e499
  - ev-9bb36c0285ba1c82
  - ev-001b8b26f25dd79c
  - ev-085e29b75373042d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-379b78deb8107361
  - ev-8114952aa531447b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-0c56e53a687885fe
  - ev-8114952aa531447b
  - ev-1c82b5cc54bee1ee
evidence:
- evidence_id: ev-379b78deb8107361
  kind: record_content
  reference: data/ingredients/mapped/Palatinose_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1608],"raw_equal":true},"docs_rows":[{"identifier":"cas:343336-76-5","line":1610,"mapping_status":"MAPPED","ontology_id":"CHEBI:18394","preferred_term":"palatinose
    hydrate"}],"identifier":"cas:343336-76-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:18394","ontology_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","ontology_source":"CHEBI"},"preferred_term":"palatinose
    hydrate","sssom_rows":[{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","predicate_id":"skos:closeMatch"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Palatinose_Hydrate","synonym_count":0}'
  snapshot_sha256: 7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651
- evidence_id: ev-b95c1d9c64e1e499
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1608]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9bb36c0285ba1c82
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Palatinose_Hydrate; data-row positions=[2191, 2192]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","other":"CAS:343336-76-5","predicate_id":"skos:closeMatch","subject_id":"MIM:Palatinose_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose
    hydrate","other":"CAS:343336-76-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Palatinose_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-001b8b26f25dd79c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1610]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:343336-76-5","line":1610,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18394","preferred_term":"palatinose
    hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0c56e53a687885fe
  kind: prior_review
  reference: reports/yaml_record_review/Palatinose_Hydrate.md
  locator: '`data/ingredients/mapped/Palatinose_Hydrate.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:33; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 32a8e9bc7025e8d55021623c51780d7d568fbb7450c6a718deef46572ee0d495
  quote: "Recommended Edits:\n- Major: restore the exact `kgmicrobe.compound:palatinose_hydrate`\
    \ registry row\n  for `MIM:Palatinose_Hydrate` in the maintained SSSOM build path,\
    \ rebuild\n  `mappings/ingredient_mappings.sssom.tsv`, and rerun\n  `scripts/validate_sssom_invariants.py`.\n\
    - Major: in `data/ingredients/mapped/Palatinose_Hydrate.yaml`, either replace\n\
    \  `nutritional_roles.CARBON_SOURCE` with cited experimental or recipe evidence,\n\
    \  or remove the provisional role facet until source-backed role evidence is\n\
    \  curated."
- evidence_id: ev-8114952aa531447b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1094,1407]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651","finding_id":"SEM:08d7cd089859cd906df9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651","finding_id":"SEM:20ea0b5654db8eb97bfb","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-085e29b75373042d
  kind: record_content
  reference: data/ingredients/mapped/Palatinose_Hydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1608],"raw_equal":true},"docs_rows":[{"identifier":"cas:343336-76-5","line":1610,"mapping_status":"MAPPED","ontology_id":"CHEBI:18394","preferred_term":"palatinose
    hydrate"}],"identifier":"cas:343336-76-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:18394","ontology_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","ontology_source":"CHEBI"},"preferred_term":"palatinose
    hydrate","sssom_rows":[{"data_row":2191,"object_id":"CHEBI:18394","object_label":"6-O-alpha-D-glucopyranosyl-D-fructofuranose","predicate_id":"skos:closeMatch"},{"data_row":2192,"object_id":"cas:343336-76-5","object_label":"palatinose
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Palatinose_Hydrate","synonym_count":0}'
  snapshot_sha256: 7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651
- evidence_id: ev-1c82b5cc54bee1ee
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-b72270c86b646407]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b72270c86b646407 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-40faa8725968165c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-379b78deb8107361
  - ev-b95c1d9c64e1e499
  - ev-9bb36c0285ba1c82
  - ev-001b8b26f25dd79c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-efe5fced68b649c0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-0c56e53a687885fe
  - ev-379b78deb8107361
  - ev-8114952aa531447b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:28:40Z;
    reviewed SHA-256=7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651;
    current SHA-256=7d473a85cf46e31086d1cc784bff87a46f063740da598f5463454a6d70cce651;
    hash_changed=False. Reports=["reports/yaml_record_review/Palatinose_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    hydrate identity and close parent row pass, but a registry sibling is missing
    and CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0c56e53a687885fe
    - ev-379b78deb8107361
  - name: legacy-native-ids
    value: '["SEM:08d7cd089859cd906df9","SEM:20ea0b5654db8eb97bfb"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-379b78deb8107361
    - ev-0c56e53a687885fe
    - ev-8114952aa531447b
- assessment_id: a-085e29b75373042d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-0c56e53a687885fe
  - ev-085e29b75373042d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0c56e53a687885fe
    - ev-085e29b75373042d
findings:
- finding_id: rec-f-b72270c86b646407
  issue_key: mim-reconciliation-role-support-db42c1305957dc5c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: palatinose hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-db42c1305957dc5c
  evidence_ids:
  - ev-0c56e53a687885fe
  - ev-085e29b75373042d
  - ev-1c82b5cc54bee1ee
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Palatinose_Hydrate.yaml
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
    finding_id: f-b72270c86b646407
actions:
- action_id: rec-action-b72270c86b646407
  description: 'Reassess prediction-only role support: palatinose hydrate'
  finding_ids:
  - rec-f-b72270c86b646407
  target_ids:
  - record-db42c1305957dc5c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Palatinose_Hydrate.yaml
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
