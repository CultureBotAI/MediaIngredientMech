# Per-record structured review: Bromocresol_Purple (data/ingredients/mapped/Bromocresol_Purple.yaml)

- Review: 20261017T083000Z-bromocresol-purple
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bromocresol_Purple (data/ingredients/mapped/Bromocresol_Purple.yaml, record-037402dc74758530, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bromocresol_Purple.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bromocresol_Purple.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-037402dc74758530 | data/ingredients/mapped/Bromocresol_Purple.yaml | maintained | Bromocresol_Purple |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-037402dc74758530 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-037402dc74758530 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-037402dc74758530 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-037402dc74758530.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-037402dc74758530.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z; reviewed SHA-256=9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb; current SHA-256=9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb; hash_changed=False. Reports=["reports/yaml_record_review/Bromocresol_Purple.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bromocresol purple identity, CAS, pH-indicator role, structure fields, occurrence count, SSSOM row, and aggregate copy pass, but one synonym is malformed.

### Historical provisional-role concern

evidence: concern. Targets: record-037402dc74758530.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-037402dc74758530: Reassess prediction-only or empty role support: Bromocresol_Purple

major / open / confirmed; issue key: mim-reconciliation-role-support-037402dc74758530.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-037402dc74758530

Reassess prediction-only or empty role support: Bromocresol_Purple

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c06b4db9f1b639fe | data/ingredients/mapped/Bromocresol_Purple.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[604],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86154","line":606,"mapping_status":"MAPPED","ontology_id":"CHEBI:86154","preferred_term":"Bromocresol purple"}],"identifier":"CHEBI:86154","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86154","ontology_label":"bromocresol purple","ontology_source":"CHEBI"},"preferred_term":"Bromocresol purple","sssom_rows":[{"data_row":581,"object_id":"CHEBI:86154","object_label":"bromocresol purple","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromocresol_Purple","synonym_count":4} |
| ev-51f2c20a402e9ea4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [604] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-42235dd38cbfd1c4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bromocresol_Purple; data-row positions=[581] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":581,"object_id":"CHEBI:86154","object_label":"bromocresol purple","other":"3,3-bis(3-bromo-4-hydroxy-5-methylphenyl)-2,1lambda(6)-benzoxathiole-1,1(3H)-dione&#124;5',5\"\"-dibromo-o-cresolsulfophthalein&#124;HSDB 7729&#124;bromocresol purple\"&#124;CAS:115-40-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromocresol_Purple","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ae18f9f1268046f8 | docs/data/mapped_ingredients.csv; CSV lines=[606] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86154","line":606,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:86154","preferred_term":"Bromocresol purple","total_occurrences":"9"}] |
| ev-d8916b8b9e98aee4 | reports/yaml_record_review/Bromocresol_Purple.md; &#96;data/ingredients/mapped/Bromocresol_Purple.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:35; Completeness:51; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0a495fda5ab23d2b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[332,1728] | context_only | [{"current_record_sha256":"9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb","finding_id":"SEM:1d36959c1496b9350e59","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb","finding_id":"SEM:64d82ceaa9447eb58d80","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-20c921e6ad3f3589 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Bromocresol_Purple.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bromocresol-purple
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bromocresol_Purple (data/ingredients/mapped/Bromocresol_Purple.yaml)'
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
summary: Per-record structured review for Bromocresol_Purple (data/ingredients/mapped/Bromocresol_Purple.yaml,
  record-037402dc74758530, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bromocresol_Purple.yaml
    sha256: 9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb
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
  - path: reports/yaml_record_review/Bromocresol_Purple.md
    sha256: 30db249d4c8cfdd5af1a3f5d48837ab14714deebd8295b8d63dacab8d3889b4c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-037402dc74758530
  path: data/ingredients/mapped/Bromocresol_Purple.yaml
  label: Bromocresol_Purple
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromocresol_Purple.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bromocresol_Purple.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bromocresol_Purple.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-037402dc74758530
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-037402dc74758530
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-037402dc74758530
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-037402dc74758530
evidence:
- evidence_id: ev-c06b4db9f1b639fe
  kind: record_content
  reference: data/ingredients/mapped/Bromocresol_Purple.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[604],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86154","line":606,"mapping_status":"MAPPED","ontology_id":"CHEBI:86154","preferred_term":"Bromocresol
    purple"}],"identifier":"CHEBI:86154","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86154","ontology_label":"bromocresol
    purple","ontology_source":"CHEBI"},"preferred_term":"Bromocresol purple","sssom_rows":[{"data_row":581,"object_id":"CHEBI:86154","object_label":"bromocresol
    purple","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromocresol_Purple","synonym_count":4}'
  snapshot_sha256: 9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb
- evidence_id: ev-51f2c20a402e9ea4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [604]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-42235dd38cbfd1c4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bromocresol_Purple; data-row positions=[581]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":581,"object_id":"CHEBI:86154","object_label":"bromocresol
    purple","other":"3,3-bis(3-bromo-4-hydroxy-5-methylphenyl)-2,1lambda(6)-benzoxathiole-1,1(3H)-dione|5'',5\"\"-dibromo-o-cresolsulfophthalein|HSDB
    7729|bromocresol purple\"|CAS:115-40-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromocresol_Purple","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ae18f9f1268046f8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[606]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86154","line":606,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:86154","preferred_term":"Bromocresol
    purple","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d8916b8b9e98aee4
  kind: prior_review
  reference: reports/yaml_record_review/Bromocresol_Purple.md
  locator: '`data/ingredients/mapped/Bromocresol_Purple.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:35; Completeness:51; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 30db249d4c8cfdd5af1a3f5d48837ab14714deebd8295b8d63dacab8d3889b4c
  quote: "Recommended Edits:\n- Minor: remove the malformed `bromocresol purple\"\
    ` synonym from\n  `data/ingredients/mapped/Bromocresol_Purple.yaml`, regenerate\
    \ the SSSOM row,\n  then run `just sync-curated` and focused strict/term/SSSOM\
    \ validation."
- evidence_id: ev-0a495fda5ab23d2b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[332,1728]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb","finding_id":"SEM:1d36959c1496b9350e59","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb","finding_id":"SEM:64d82ceaa9447eb58d80","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-20c921e6ad3f3589
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Bromocresol_Purple.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-de63e655a26a622b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-037402dc74758530
  evidence_ids:
  - ev-c06b4db9f1b639fe
  - ev-51f2c20a402e9ea4
  - ev-42235dd38cbfd1c4
  - ev-ae18f9f1268046f8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4e12157042ea76ab
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-037402dc74758530
  evidence_ids:
  - ev-d8916b8b9e98aee4
  - ev-c06b4db9f1b639fe
  - ev-0a495fda5ab23d2b
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z;
    reviewed SHA-256=9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb;
    current SHA-256=9fb254c410e9df1a296ee04529f2612ffd82e240c5f3a9d9c46894fb36e948eb;
    hash_changed=False. Reports=["reports/yaml_record_review/Bromocresol_Purple.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bromocresol purple identity, CAS, pH-indicator role, structure fields, occurrence
    count, SSSOM row, and aggregate copy pass, but one synonym is malformed.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8916b8b9e98aee4
    - ev-c06b4db9f1b639fe
  - name: legacy-native-ids
    value: '["SEM:1d36959c1496b9350e59","SEM:64d82ceaa9447eb58d80"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c06b4db9f1b639fe
    - ev-d8916b8b9e98aee4
    - ev-0a495fda5ab23d2b
- assessment_id: a-role-037402dc74758530
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-037402dc74758530
  evidence_ids:
  - ev-c06b4db9f1b639fe
  - ev-20c921e6ad3f3589
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c06b4db9f1b639fe
    - ev-20c921e6ad3f3589
findings:
- finding_id: rec-f-role-037402dc74758530
  issue_key: mim-reconciliation-role-support-037402dc74758530
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Bromocresol_Purple'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-037402dc74758530
  evidence_ids:
  - ev-c06b4db9f1b639fe
  - ev-20c921e6ad3f3589
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromocresol_Purple.yaml
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
- action_id: rec-act-role-037402dc74758530
  description: 'Reassess prediction-only or empty role support: Bromocresol_Purple'
  finding_ids:
  - rec-f-role-037402dc74758530
  target_ids:
  - record-037402dc74758530
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromocresol_Purple.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
