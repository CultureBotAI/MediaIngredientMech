# Per-record structured review: Ceftazidime_Hydrate (data/ingredients/mapped/Ceftazidime_Hydrate.yaml)

- Review: 20261017T083000Z-ceftazidime-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ceftazidime_Hydrate (data/ingredients/mapped/Ceftazidime_Hydrate.yaml, record-53b2b7722b584ebb, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ceftazidime_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ceftazidime_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-53b2b7722b584ebb | data/ingredients/mapped/Ceftazidime_Hydrate.yaml | maintained | Ceftazidime_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-53b2b7722b584ebb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-53b2b7722b584ebb | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-53b2b7722b584ebb | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-53b2b7722b584ebb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-53b2b7722b584ebb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:29:39Z; reviewed SHA-256=405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb; current SHA-256=405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb; hash_changed=False. Reports=["reports/yaml_record_review/Ceftazidime_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity and Section 3 SSSOM rows are internally consistent, but the unspecified hydrate source and provisional SELECTIVE_AGENT role need inspection.

### Historical provisional-role concern

evidence: concern. Targets: record-53b2b7722b584ebb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6f9738b2517ff20c: Reassess prediction-only role support: Ceftazidime hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-53b2b7722b584ebb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6f9738b2517ff20c

Reassess prediction-only role support: Ceftazidime hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b8d81df3a0a582bc | data/ingredients/mapped/Ceftazidime_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[681],"raw_equal":true},"docs_rows":[{"identifier":"cas:120618-65-7","line":683,"mapping_status":"MAPPED","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime hydrate"}],"identifier":"cas:120618-65-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:3508","ontology_label":"ceftazidime","ontology_source":"CHEBI"},"preferred_term":"Ceftazidime hydrate","sssom_rows":[{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","predicate_id":"skos:closeMatch"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ceftazidime_Hydrate","synonym_count":0} |
| ev-98968ae417591d30 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [681] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8b7d6b89a59b997f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ceftazidime_Hydrate; data-row positions=[699, 700] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","other":"CAS:120618-65-7","predicate_id":"skos:closeMatch","subject_id":"MIM:Ceftazidime_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime hydrate","other":"CAS:120618-65-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ceftazidime_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-671e850a4c09589b | docs/data/mapped_ingredients.csv; CSV lines=[683] | supports | Published identity and count rows inspected: [{"identifier":"cas:120618-65-7","line":683,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime hydrate","total_occurrences":"0"}] |
| ev-99ff40a156eef7a3 | reports/yaml_record_review/Ceftazidime_Hydrate.md; &#96;data/ingredients/mapped/Ceftazidime_Hydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:67; Recommended Edits:75 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-de3c7d6c62cfbe55 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[383,2105] | context_only | [{"current_record_sha256":"405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb","finding_id":"SEM:6a6bb860c3c8175f89b9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb","finding_id":"SEM:7244f717e65283340193","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-80dfb0015ea336c5 | data/ingredients/mapped/Ceftazidime_Hydrate.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[681],"raw_equal":true},"docs_rows":[{"identifier":"cas:120618-65-7","line":683,"mapping_status":"MAPPED","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime hydrate"}],"identifier":"cas:120618-65-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:3508","ontology_label":"ceftazidime","ontology_source":"CHEBI"},"preferred_term":"Ceftazidime hydrate","sssom_rows":[{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","predicate_id":"skos:closeMatch"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ceftazidime_Hydrate","synonym_count":0} |
| ev-32f237edaf3dcf46 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-6f9738b2517ff20c] | context_only | Predecessor structured review finding f-6f9738b2517ff20c in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ceftazidime-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ceftazidime_Hydrate (data/ingredients/mapped/Ceftazidime_Hydrate.yaml)'
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
summary: Per-record structured review for Ceftazidime_Hydrate (data/ingredients/mapped/Ceftazidime_Hydrate.yaml,
  record-53b2b7722b584ebb, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
    sha256: 405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Ceftazidime_Hydrate.md
    sha256: 1fbff7a24f11cdd6fe95c7843a72937c52a1ef56f85a13b19f4f584919b4f447
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-53b2b7722b584ebb
  path: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
  label: Ceftazidime_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ceftazidime_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ceftazidime_Hydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-53b2b7722b584ebb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-b8d81df3a0a582bc
  - ev-98968ae417591d30
  - ev-8b7d6b89a59b997f
  - ev-671e850a4c09589b
  - ev-80dfb0015ea336c5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-b8d81df3a0a582bc
  - ev-de3c7d6c62cfbe55
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-99ff40a156eef7a3
  - ev-de3c7d6c62cfbe55
  - ev-32f237edaf3dcf46
evidence:
- evidence_id: ev-b8d81df3a0a582bc
  kind: record_content
  reference: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[681],"raw_equal":true},"docs_rows":[{"identifier":"cas:120618-65-7","line":683,"mapping_status":"MAPPED","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime
    hydrate"}],"identifier":"cas:120618-65-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:3508","ontology_label":"ceftazidime","ontology_source":"CHEBI"},"preferred_term":"Ceftazidime
    hydrate","sssom_rows":[{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","predicate_id":"skos:closeMatch"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ceftazidime_Hydrate","synonym_count":0}'
  snapshot_sha256: 405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb
- evidence_id: ev-98968ae417591d30
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [681]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8b7d6b89a59b997f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ceftazidime_Hydrate; data-row positions=[699, 700]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","other":"CAS:120618-65-7","predicate_id":"skos:closeMatch","subject_id":"MIM:Ceftazidime_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime
    hydrate","other":"CAS:120618-65-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ceftazidime_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-671e850a4c09589b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[683]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:120618-65-7","line":683,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime
    hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-99ff40a156eef7a3
  kind: prior_review
  reference: reports/yaml_record_review/Ceftazidime_Hydrate.md
  locator: '`data/ingredients/mapped/Ceftazidime_Hydrate.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:39; Completeness:67; Recommended Edits:75'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1fbff7a24f11cdd6fe95c7843a72937c52a1ef56f85a13b19f4f584919b4f447
  quote: "Recommended Edits:\n- Major: inspect the original CultureBotHT source or\
    \ supplier record for the\n  intended ceftazidime hydrate and either keep the\
    \ CAS identity as explicitly\n  verified, or retarget to a more specific hydrate\
    \ if the source names one.\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ with inspected\n  evidence for ceftazidime hydrate as a selective agent in this\
    \ media scope, or\n  remove the role, then rerun strict validation, SSSOM QC,\
    \ aggregate roundtrip,\n  hydrate audits, and `git diff --check`."
- evidence_id: ev-de3c7d6c62cfbe55
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[383,2105]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb","finding_id":"SEM:6a6bb860c3c8175f89b9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb","finding_id":"SEM:7244f717e65283340193","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-80dfb0015ea336c5
  kind: record_content
  reference: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[681],"raw_equal":true},"docs_rows":[{"identifier":"cas:120618-65-7","line":683,"mapping_status":"MAPPED","ontology_id":"CHEBI:3508","preferred_term":"Ceftazidime
    hydrate"}],"identifier":"cas:120618-65-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:3508","ontology_label":"ceftazidime","ontology_source":"CHEBI"},"preferred_term":"Ceftazidime
    hydrate","sssom_rows":[{"data_row":699,"object_id":"CHEBI:3508","object_label":"ceftazidime","predicate_id":"skos:closeMatch"},{"data_row":700,"object_id":"cas:120618-65-7","object_label":"Ceftazidime
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ceftazidime_Hydrate","synonym_count":0}'
  snapshot_sha256: 405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb
- evidence_id: ev-32f237edaf3dcf46
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-6f9738b2517ff20c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6f9738b2517ff20c in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-0de9a00bf4f847c2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-b8d81df3a0a582bc
  - ev-98968ae417591d30
  - ev-8b7d6b89a59b997f
  - ev-671e850a4c09589b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-eafb3a3f421b15d5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-99ff40a156eef7a3
  - ev-b8d81df3a0a582bc
  - ev-de3c7d6c62cfbe55
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:29:39Z;
    reviewed SHA-256=405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb;
    current SHA-256=405c394375f6df48a0b77acc3d01c6c24e6fce844cf7470ef838792b8f9895cb;
    hash_changed=False. Reports=["reports/yaml_record_review/Ceftazidime_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity and Section 3 SSSOM rows are internally consistent, but the unspecified
    hydrate source and provisional SELECTIVE_AGENT role need inspection.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-99ff40a156eef7a3
    - ev-b8d81df3a0a582bc
  - name: legacy-native-ids
    value: '["SEM:6a6bb860c3c8175f89b9","SEM:7244f717e65283340193"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b8d81df3a0a582bc
    - ev-99ff40a156eef7a3
    - ev-de3c7d6c62cfbe55
- assessment_id: a-80dfb0015ea336c5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-99ff40a156eef7a3
  - ev-80dfb0015ea336c5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-99ff40a156eef7a3
    - ev-80dfb0015ea336c5
findings:
- finding_id: rec-f-6f9738b2517ff20c
  issue_key: mim-reconciliation-role-support-53b2b7722b584ebb
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Ceftazidime hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-53b2b7722b584ebb
  evidence_ids:
  - ev-99ff40a156eef7a3
  - ev-80dfb0015ea336c5
  - ev-32f237edaf3dcf46
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-6f9738b2517ff20c
actions:
- action_id: rec-action-6f9738b2517ff20c
  description: 'Reassess prediction-only role support: Ceftazidime hydrate'
  finding_ids:
  - rec-f-6f9738b2517ff20c
  target_ids:
  - record-53b2b7722b584ebb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ceftazidime_Hydrate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
