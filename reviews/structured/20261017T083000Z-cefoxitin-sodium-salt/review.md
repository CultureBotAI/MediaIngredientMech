# Per-record structured review: Cefoxitin_Sodium_Salt (data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml)

- Review: 20261017T083000Z-cefoxitin-sodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cefoxitin_Sodium_Salt (data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml, record-32b6898e40544f12, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-32b6898e40544f12 | data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml | maintained | Cefoxitin_Sodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-32b6898e40544f12 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-32b6898e40544f12 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-32b6898e40544f12 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-32b6898e40544f12.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-32b6898e40544f12.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:26:24Z; reviewed SHA-256=c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd; current SHA-256=c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd; hash_changed=False. Reports=["reports/yaml_record_review/Cefoxitin_Sodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CAS-derived CHEBI cefoxitin sodium salt identity passes, but SELECTIVE_AGENT is only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-32b6898e40544f12.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0e8cff303dea6cdc: Reassess prediction-only role support: Cefoxitin sodium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-32b6898e40544f12.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0e8cff303dea6cdc

Reassess prediction-only role support: Cefoxitin sodium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4e69fbec5cad60f0 | data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[679],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3501","line":681,"mapping_status":"MAPPED","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin sodium salt"}],"identifier":"CHEBI:3501","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3501","ontology_label":"Cefoxitin sodium","ontology_source":"CHEBI"},"preferred_term":"Cefoxitin sodium salt","sssom_rows":[{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefoxitin_Sodium_Salt","synonym_count":0} |
| ev-aa5988713d8ed7eb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [679] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-40b2b13daec76634 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cefoxitin_Sodium_Salt; data-row positions=[693] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin sodium","other":"CAS:33564-30-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Cefoxitin_Sodium_Salt","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-00f2f68f55cd92ca | docs/data/mapped_ingredients.csv; CSV lines=[681] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3501","line":681,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin sodium salt","total_occurrences":"0"}] |
| ev-aadd2d2f878427b5 | reports/yaml_record_review/Cefoxitin_Sodium_Salt.md; &#96;data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:54; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-65767513c3a7d4af | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[381,1473] | context_only | [{"current_record_sha256":"c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd","finding_id":"SEM:46773517097ad211849f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd","finding_id":"SEM:b2a707715250bbf07ae1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-512495c1fe232f0c | data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[679],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3501","line":681,"mapping_status":"MAPPED","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin sodium salt"}],"identifier":"CHEBI:3501","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3501","ontology_label":"Cefoxitin sodium","ontology_source":"CHEBI"},"preferred_term":"Cefoxitin sodium salt","sssom_rows":[{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefoxitin_Sodium_Salt","synonym_count":0} |
| ev-69272b0e1f5b72f2 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-0e8cff303dea6cdc] | context_only | Predecessor structured review finding f-0e8cff303dea6cdc in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cefoxitin-sodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cefoxitin_Sodium_Salt (data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml)'
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
summary: Per-record structured review for Cefoxitin_Sodium_Salt (data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml,
  record-32b6898e40544f12, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
    sha256: c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd
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
  - path: reports/yaml_record_review/Cefoxitin_Sodium_Salt.md
    sha256: b6ec0b4634464d8c7bf0eb50b408598704371476e098e9eda59cb5e0ca6efd44
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-32b6898e40544f12
  path: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
  label: Cefoxitin_Sodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-32b6898e40544f12
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-4e69fbec5cad60f0
  - ev-aa5988713d8ed7eb
  - ev-40b2b13daec76634
  - ev-00f2f68f55cd92ca
  - ev-512495c1fe232f0c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-4e69fbec5cad60f0
  - ev-65767513c3a7d4af
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-aadd2d2f878427b5
  - ev-65767513c3a7d4af
  - ev-69272b0e1f5b72f2
evidence:
- evidence_id: ev-4e69fbec5cad60f0
  kind: record_content
  reference: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[679],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3501","line":681,"mapping_status":"MAPPED","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin
    sodium salt"}],"identifier":"CHEBI:3501","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3501","ontology_label":"Cefoxitin
    sodium","ontology_source":"CHEBI"},"preferred_term":"Cefoxitin sodium salt","sssom_rows":[{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin
    sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefoxitin_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd
- evidence_id: ev-aa5988713d8ed7eb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [679]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-40b2b13daec76634
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cefoxitin_Sodium_Salt; data-row positions=[693]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin
    sodium","other":"CAS:33564-30-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Cefoxitin_Sodium_Salt","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-00f2f68f55cd92ca
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[681]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3501","line":681,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin
    sodium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aadd2d2f878427b5
  kind: prior_review
  reference: reports/yaml_record_review/Cefoxitin_Sodium_Salt.md
  locator: '`data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:39; Completeness:54; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b6ec0b4634464d8c7bf0eb50b408598704371476e098e9eda59cb5e0ca6efd44
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ with inspected\n  evidence for cefoxitin sodium as a selective agent in this\
    \ media scope, or\n  remove the role, then rerun strict validation, SSSOM QC,\
    \ aggregate roundtrip,\n  and `git diff --check`."
- evidence_id: ev-65767513c3a7d4af
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[381,1473]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd","finding_id":"SEM:46773517097ad211849f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd","finding_id":"SEM:b2a707715250bbf07ae1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-512495c1fe232f0c
  kind: record_content
  reference: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[679],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3501","line":681,"mapping_status":"MAPPED","ontology_id":"CHEBI:3501","preferred_term":"Cefoxitin
    sodium salt"}],"identifier":"CHEBI:3501","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3501","ontology_label":"Cefoxitin
    sodium","ontology_source":"CHEBI"},"preferred_term":"Cefoxitin sodium salt","sssom_rows":[{"data_row":693,"object_id":"CHEBI:3501","object_label":"Cefoxitin
    sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefoxitin_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd
- evidence_id: ev-69272b0e1f5b72f2
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-0e8cff303dea6cdc]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0e8cff303dea6cdc in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-c89953104bd1a8a0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-4e69fbec5cad60f0
  - ev-aa5988713d8ed7eb
  - ev-40b2b13daec76634
  - ev-00f2f68f55cd92ca
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6a4e0858ef460573
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-aadd2d2f878427b5
  - ev-4e69fbec5cad60f0
  - ev-65767513c3a7d4af
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:26:24Z;
    reviewed SHA-256=c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd;
    current SHA-256=c42368a68a9bb96a8ca994ac1ce506257bbb72d03f79c08bad794b72b92d9cdd;
    hash_changed=False. Reports=["reports/yaml_record_review/Cefoxitin_Sodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CAS-derived CHEBI cefoxitin sodium salt identity passes, but SELECTIVE_AGENT is
    only a provisional name-pattern prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aadd2d2f878427b5
    - ev-4e69fbec5cad60f0
  - name: legacy-native-ids
    value: '["SEM:46773517097ad211849f","SEM:b2a707715250bbf07ae1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4e69fbec5cad60f0
    - ev-aadd2d2f878427b5
    - ev-65767513c3a7d4af
- assessment_id: a-512495c1fe232f0c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-aadd2d2f878427b5
  - ev-512495c1fe232f0c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aadd2d2f878427b5
    - ev-512495c1fe232f0c
findings:
- finding_id: rec-f-0e8cff303dea6cdc
  issue_key: mim-reconciliation-role-support-32b6898e40544f12
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cefoxitin sodium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-32b6898e40544f12
  evidence_ids:
  - ev-aadd2d2f878427b5
  - ev-512495c1fe232f0c
  - ev-69272b0e1f5b72f2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
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
    finding_id: f-0e8cff303dea6cdc
actions:
- action_id: rec-action-0e8cff303dea6cdc
  description: 'Reassess prediction-only role support: Cefoxitin sodium salt'
  finding_ids:
  - rec-f-0e8cff303dea6cdc
  target_ids:
  - record-32b6898e40544f12
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefoxitin_Sodium_Salt.yaml
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
