# Per-record structured review: Lactulose (data/ingredients/mapped/Lactulose.yaml)

- Review: 20261017T083000Z-lactulose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lactulose (data/ingredients/mapped/Lactulose.yaml, record-03cc2a9d2afa7f75, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lactulose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lactulose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-03cc2a9d2afa7f75 | data/ingredients/mapped/Lactulose.yaml | maintained | Lactulose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-03cc2a9d2afa7f75 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-03cc2a9d2afa7f75 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-03cc2a9d2afa7f75 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-03cc2a9d2afa7f75.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-03cc2a9d2afa7f75.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:54:51Z; reviewed SHA-256=eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296; current SHA-256=eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296; hash_changed=False. Reports=["reports/yaml_record_review/Lactulose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:6359 identity, CAS value, PubChem structure, synonym, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-03cc2a9d2afa7f75.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f36a3d828261a9d0: Reassess prediction-only role support: Lactulose

major / open / confirmed; issue key: mim-reconciliation-role-support-03cc2a9d2afa7f75.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f36a3d828261a9d0

Reassess prediction-only role support: Lactulose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-902a0e9905b1cb2b | data/ingredients/mapped/Lactulose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1282],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6359","line":1284,"mapping_status":"MAPPED","ontology_id":"CHEBI:6359","preferred_term":"Lactulose"}],"identifier":"CHEBI:6359","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6359","ontology_label":"lactulose","ontology_source":"CHEBI"},"preferred_term":"Lactulose","sssom_rows":[{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactulose","synonym_count":1} |
| ev-63e505f3ff52fa7b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1282] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-50b3947e371d045f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lactulose; data-row positions=[1667] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","other":"4-O-beta-D-galactopyranosyl-beta-D-fructofuranose&#124;CAS:4618-18-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactulose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-29afabdb9e6b0c14 | docs/data/mapped_ingredients.csv; CSV lines=[1284] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:6359","line":1284,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6359","preferred_term":"Lactulose","total_occurrences":"0"}] |
| ev-0a1d9a0d200234c5 | reports/yaml_record_review/Lactulose.md; &#96;data/ingredients/mapped/Lactulose.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:28; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d410b8b7c041b0c8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[851,1422] | context_only | [{"current_record_sha256":"eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296","finding_id":"SEM:db51cedb24ce4481cf20","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296","finding_id":"SEM:4880e77be3e60ec84e54","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-19b7ad2684fe11b3 | data/ingredients/mapped/Lactulose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1282],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6359","line":1284,"mapping_status":"MAPPED","ontology_id":"CHEBI:6359","preferred_term":"Lactulose"}],"identifier":"CHEBI:6359","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6359","ontology_label":"lactulose","ontology_source":"CHEBI"},"preferred_term":"Lactulose","sssom_rows":[{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactulose","synonym_count":1} |
| ev-048b769ae0b79dff | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-f36a3d828261a9d0] | context_only | Predecessor structured review finding f-f36a3d828261a9d0 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lactulose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lactulose (data/ingredients/mapped/Lactulose.yaml)'
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
summary: Per-record structured review for Lactulose (data/ingredients/mapped/Lactulose.yaml,
  record-03cc2a9d2afa7f75, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lactulose.yaml
    sha256: eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Lactulose.md
    sha256: c804a17d1027aee2992a782a414a0bc2fa1883467dfda95b3d58453a48f57c94
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-03cc2a9d2afa7f75
  path: data/ingredients/mapped/Lactulose.yaml
  label: Lactulose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactulose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lactulose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lactulose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-03cc2a9d2afa7f75
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-902a0e9905b1cb2b
  - ev-63e505f3ff52fa7b
  - ev-50b3947e371d045f
  - ev-29afabdb9e6b0c14
  - ev-19b7ad2684fe11b3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-902a0e9905b1cb2b
  - ev-d410b8b7c041b0c8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-0a1d9a0d200234c5
  - ev-d410b8b7c041b0c8
  - ev-048b769ae0b79dff
evidence:
- evidence_id: ev-902a0e9905b1cb2b
  kind: record_content
  reference: data/ingredients/mapped/Lactulose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1282],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6359","line":1284,"mapping_status":"MAPPED","ontology_id":"CHEBI:6359","preferred_term":"Lactulose"}],"identifier":"CHEBI:6359","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6359","ontology_label":"lactulose","ontology_source":"CHEBI"},"preferred_term":"Lactulose","sssom_rows":[{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactulose","synonym_count":1}'
  snapshot_sha256: eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296
- evidence_id: ev-63e505f3ff52fa7b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1282]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-50b3947e371d045f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lactulose; data-row positions=[1667]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","other":"4-O-beta-D-galactopyranosyl-beta-D-fructofuranose|CAS:4618-18-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactulose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-29afabdb9e6b0c14
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1284]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:6359","line":1284,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6359","preferred_term":"Lactulose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0a1d9a0d200234c5
  kind: prior_review
  reference: reports/yaml_record_review/Lactulose.md
  locator: '`data/ingredients/mapped/Lactulose.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:28; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c804a17d1027aee2992a782a414a0bc2fa1883467dfda95b3d58453a48f57c94
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Lactulose.yaml` with inspected source evidence\
    \ for\n  exact lactulose use, or remove the provisional role.\n- Sync the aggregate\
    \ copy and regenerate derived products after the YAML\n  changes; rerun strict,\
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-d410b8b7c041b0c8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[851,1422]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296","finding_id":"SEM:db51cedb24ce4481cf20","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296","finding_id":"SEM:4880e77be3e60ec84e54","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-19b7ad2684fe11b3
  kind: record_content
  reference: data/ingredients/mapped/Lactulose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1282],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6359","line":1284,"mapping_status":"MAPPED","ontology_id":"CHEBI:6359","preferred_term":"Lactulose"}],"identifier":"CHEBI:6359","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6359","ontology_label":"lactulose","ontology_source":"CHEBI"},"preferred_term":"Lactulose","sssom_rows":[{"data_row":1667,"object_id":"CHEBI:6359","object_label":"lactulose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactulose","synonym_count":1}'
  snapshot_sha256: eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296
- evidence_id: ev-048b769ae0b79dff
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-f36a3d828261a9d0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f36a3d828261a9d0 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-888a8701269f977d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-902a0e9905b1cb2b
  - ev-63e505f3ff52fa7b
  - ev-50b3947e371d045f
  - ev-29afabdb9e6b0c14
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-44f68074a8a872a4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-0a1d9a0d200234c5
  - ev-902a0e9905b1cb2b
  - ev-d410b8b7c041b0c8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:54:51Z;
    reviewed SHA-256=eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296;
    current SHA-256=eb970b4c4d681b1a0a4e0069c29d39a5338a9915d87cbd8e5ec2f55ef85af296;
    hash_changed=False. Reports=["reports/yaml_record_review/Lactulose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:6359
    identity, CAS value, PubChem structure, synonym, and final SSSOM row pass, but
    CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0a1d9a0d200234c5
    - ev-902a0e9905b1cb2b
  - name: legacy-native-ids
    value: '["SEM:db51cedb24ce4481cf20","SEM:4880e77be3e60ec84e54"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-902a0e9905b1cb2b
    - ev-0a1d9a0d200234c5
    - ev-d410b8b7c041b0c8
- assessment_id: a-19b7ad2684fe11b3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-0a1d9a0d200234c5
  - ev-19b7ad2684fe11b3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0a1d9a0d200234c5
    - ev-19b7ad2684fe11b3
findings:
- finding_id: rec-f-f36a3d828261a9d0
  issue_key: mim-reconciliation-role-support-03cc2a9d2afa7f75
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lactulose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-03cc2a9d2afa7f75
  evidence_ids:
  - ev-0a1d9a0d200234c5
  - ev-19b7ad2684fe11b3
  - ev-048b769ae0b79dff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactulose.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-f36a3d828261a9d0
actions:
- action_id: rec-action-f36a3d828261a9d0
  description: 'Reassess prediction-only role support: Lactulose'
  finding_ids:
  - rec-f-f36a3d828261a9d0
  target_ids:
  - record-03cc2a9d2afa7f75
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactulose.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
