# Per-record structured review: Dicloxacillin_Sodium_Salt_Monohydrate (data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml)

- Review: 20261017T083000Z-dicloxacillin-sodium-salt-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dicloxacillin_Sodium_Salt_Monohydrate (data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml, record-a2f105bcec59d864, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a2f105bcec59d864 | data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml | maintained | Dicloxacillin_Sodium_Salt_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a2f105bcec59d864 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a2f105bcec59d864 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a2f105bcec59d864 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a2f105bcec59d864.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a2f105bcec59d864.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:46:00Z; reviewed SHA-256=638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914; current SHA-256=638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914; hash_changed=False. Reports=["reports/yaml_record_review/Dicloxacillin_Sodium_Salt_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI identity passes, but the selective-agent role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-a2f105bcec59d864.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e986768a5bf4a5b5: Reassess prediction-only role support: Dicloxacillin sodium salt monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-a2f105bcec59d864.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e986768a5bf4a5b5

Reassess prediction-only role support: Dicloxacillin sodium salt monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a4080acae53f5c95 | data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[887],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:52019","line":889,"mapping_status":"MAPPED","ontology_id":"CHEBI:52019","preferred_term":"Dicloxacillin sodium salt monohydrate"}],"identifier":"CHEBI:52019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:52019","ontology_label":"dicloxacillin sodium monohydrate","ontology_source":"CHEBI"},"preferred_term":"Dicloxacillin sodium salt monohydrate","sssom_rows":[{"data_row":1036,"object_id":"CHEBI:52019","object_label":"dicloxacillin sodium monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dicloxacillin_Sodium_Salt_Monohydrate","synonym_count":1} |
| ev-ee784a889acc23ee | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [887] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd1618a05967a079 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dicloxacillin_Sodium_Salt_Monohydrate; data-row positions=[1036] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1036,"object_id":"CHEBI:52019","object_label":"dicloxacillin sodium monohydrate","other":"sodium 6beta-{[3-(2,6-dichlorophenyl)-5-methyl-1,2-oxazol-4-yl]carboxamido}-2,2-dimethylpenam-3alpha-carboxylate--water (1/1)&#124;CAS:13412-64-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Dicloxacillin_Sodium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-80377322877d9542 | docs/data/mapped_ingredients.csv; CSV lines=[889] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:52019","line":889,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:52019","preferred_term":"Dicloxacillin sodium salt monohydrate","total_occurrences":"0"}] |
| ev-478ef2200b0e82d0 | reports/yaml_record_review/Dicloxacillin_Sodium_Salt_Monohydrate.md; &#96;data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:44; Completeness:71; Recommended Edits:79 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ad9bab5d5892d44a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[537,2092] | context_only | [{"current_record_sha256":"638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914","finding_id":"SEM:9751308138908a84fe40","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914","finding_id":"SEM:a1b6d089885d08ac1aaa","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-403f7c413a492dd3 | data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-ed22e79d87e4a9eb | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-e986768a5bf4a5b5] | context_only | Predecessor structured review finding f-e986768a5bf4a5b5 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dicloxacillin-sodium-salt-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dicloxacillin_Sodium_Salt_Monohydrate (data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml)'
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
summary: Per-record structured review for Dicloxacillin_Sodium_Salt_Monohydrate (data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml,
  record-a2f105bcec59d864, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
    sha256: 638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/Dicloxacillin_Sodium_Salt_Monohydrate.md
    sha256: 4c1cd9bd97d60b4d5c6e3c86471e5a9192d053657e0e41a2c4621889e6f2e02e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a2f105bcec59d864
  path: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
  label: Dicloxacillin_Sodium_Salt_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a2f105bcec59d864
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a2f105bcec59d864
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a2f105bcec59d864
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a2f105bcec59d864
evidence:
- evidence_id: ev-a4080acae53f5c95
  kind: record_content
  reference: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[887],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:52019","line":889,"mapping_status":"MAPPED","ontology_id":"CHEBI:52019","preferred_term":"Dicloxacillin
    sodium salt monohydrate"}],"identifier":"CHEBI:52019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:52019","ontology_label":"dicloxacillin
    sodium monohydrate","ontology_source":"CHEBI"},"preferred_term":"Dicloxacillin
    sodium salt monohydrate","sssom_rows":[{"data_row":1036,"object_id":"CHEBI:52019","object_label":"dicloxacillin
    sodium monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dicloxacillin_Sodium_Salt_Monohydrate","synonym_count":1}'
  snapshot_sha256: 638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914
- evidence_id: ev-ee784a889acc23ee
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [887]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd1618a05967a079
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dicloxacillin_Sodium_Salt_Monohydrate; data-row positions=[1036]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1036,"object_id":"CHEBI:52019","object_label":"dicloxacillin
    sodium monohydrate","other":"sodium 6beta-{[3-(2,6-dichlorophenyl)-5-methyl-1,2-oxazol-4-yl]carboxamido}-2,2-dimethylpenam-3alpha-carboxylate--water
    (1/1)|CAS:13412-64-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Dicloxacillin_Sodium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-80377322877d9542
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[889]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:52019","line":889,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:52019","preferred_term":"Dicloxacillin
    sodium salt monohydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-478ef2200b0e82d0
  kind: prior_review
  reference: reports/yaml_record_review/Dicloxacillin_Sodium_Salt_Monohydrate.md
  locator: '`data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml`:2;
    Verdict:4; Identity:11; Validation:25; Evidence:44; Completeness:71; Recommended
    Edits:79'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4c1cd9bd97d60b4d5c6e3c86471e5a9192d053657e0e41a2c4621889e6f2e02e
  quote: "Recommended Edits:\n- Major: replace the `SELECTIVE_AGENT` computational\
    \ role in\n  `data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml`\
    \ with\n  source-backed role evidence scoped to dicloxacillin sodium monohydrate,\
    \ or\n  remove the role if no support is available; then synchronize\n  `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-ad9bab5d5892d44a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[537,2092]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914","finding_id":"SEM:9751308138908a84fe40","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914","finding_id":"SEM:a1b6d089885d08ac1aaa","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-403f7c413a492dd3
  kind: record_content
  reference: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914
- evidence_id: ev-ed22e79d87e4a9eb
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-e986768a5bf4a5b5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e986768a5bf4a5b5 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-70d22be8f380c229
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a2f105bcec59d864
  evidence_ids:
  - ev-a4080acae53f5c95
  - ev-ee784a889acc23ee
  - ev-dd1618a05967a079
  - ev-80377322877d9542
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bc70372965fa1cf6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a2f105bcec59d864
  evidence_ids:
  - ev-478ef2200b0e82d0
  - ev-a4080acae53f5c95
  - ev-ad9bab5d5892d44a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:46:00Z;
    reviewed SHA-256=638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914;
    current SHA-256=638bde6709ddcebdd6c37e01e8c02dd4ae64429bc44f6c53015d8c5f1f802914;
    hash_changed=False. Reports=["reports/yaml_record_review/Dicloxacillin_Sodium_Salt_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI
    identity passes, but the selective-agent role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-478ef2200b0e82d0
    - ev-a4080acae53f5c95
  - name: legacy-native-ids
    value: '["SEM:9751308138908a84fe40","SEM:a1b6d089885d08ac1aaa"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a4080acae53f5c95
    - ev-478ef2200b0e82d0
    - ev-ad9bab5d5892d44a
- assessment_id: a-403f7c413a492dd3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a2f105bcec59d864
  evidence_ids:
  - ev-478ef2200b0e82d0
  - ev-403f7c413a492dd3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-478ef2200b0e82d0
    - ev-403f7c413a492dd3
findings:
- finding_id: rec-f-e986768a5bf4a5b5
  issue_key: mim-reconciliation-role-support-a2f105bcec59d864
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Dicloxacillin sodium salt monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a2f105bcec59d864
  evidence_ids:
  - ev-478ef2200b0e82d0
  - ev-403f7c413a492dd3
  - ev-ed22e79d87e4a9eb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-e986768a5bf4a5b5
actions:
- action_id: rec-action-e986768a5bf4a5b5
  description: 'Reassess prediction-only role support: Dicloxacillin sodium salt monohydrate'
  finding_ids:
  - rec-f-e986768a5bf4a5b5
  target_ids:
  - record-a2f105bcec59d864
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
