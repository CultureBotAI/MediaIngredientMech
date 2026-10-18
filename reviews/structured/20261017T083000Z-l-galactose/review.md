# Per-record structured review: L-Galactose (data/ingredients/mapped/L-Galactose.yaml)

- Review: 20261017T083000Z-l-galactose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Galactose (data/ingredients/mapped/L-Galactose.yaml, record-3ab76711f22a16ac, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Galactose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Galactose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3ab76711f22a16ac | data/ingredients/mapped/L-Galactose.yaml | maintained | L-Galactose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3ab76711f22a16ac | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3ab76711f22a16ac | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3ab76711f22a16ac | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3ab76711f22a16ac.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3ab76711f22a16ac.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:10:32Z; reviewed SHA-256=cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a; current SHA-256=cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a; hash_changed=False. Reports=["reports/yaml_record_review/L-Galactose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:37618 identity, CAS value, formula, ChEBI synonym, and final SSSOM row pass, but CARBON_SOURCE and ENERGY_SOURCE are only provisional computational roles.

### Historical provisional-role concern

evidence: concern. Targets: record-3ab76711f22a16ac.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f9e6c1cc26ce540a: Reassess prediction-only role support: L-Galactose

major / open / confirmed; issue key: mim-reconciliation-role-support-3ab76711f22a16ac.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f9e6c1cc26ce540a

Reassess prediction-only role support: L-Galactose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9367b4b09f013b4c | data/ingredients/mapped/L-Galactose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1222],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37618","line":1224,"mapping_status":"MAPPED","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose"}],"identifier":"CHEBI:37618","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37618","ontology_label":"L-galactose","ontology_source":"CHEBI"},"preferred_term":"L-Galactose","sssom_rows":[{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Galactose","synonym_count":1} |
| ev-8be2e34fa5bacbf8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1222] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a555d17557b25fd9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Galactose; data-row positions=[1572] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","other":"L-galacto-hexose&#124;CAS:15572-79-9","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Galactose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-f1ee5c78a1d4f3a1 | docs/data/mapped_ingredients.csv; CSV lines=[1224] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:37618","line":1224,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose","total_occurrences":"0"}] |
| ev-bf20b2eaa4fb8b2d | reports/yaml_record_review/L-Galactose.md; &#96;data/ingredients/mapped/L-Galactose.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:31; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-26289eeecfccd9aa | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[789,1827,1928] | context_only | [{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:efea5cb86dd9ae186189","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:4ee1c0e67e44ccb98697","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:4716929324ed84558a24","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8a78428d6cf7fea5 | data/ingredients/mapped/L-Galactose.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1222],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37618","line":1224,"mapping_status":"MAPPED","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose"}],"identifier":"CHEBI:37618","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37618","ontology_label":"L-galactose","ontology_source":"CHEBI"},"preferred_term":"L-Galactose","sssom_rows":[{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Galactose","synonym_count":1} |
| ev-c6c0245cff778869 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-f9e6c1cc26ce540a] | context_only | Predecessor structured review finding f-f9e6c1cc26ce540a in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-galactose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Galactose (data/ingredients/mapped/L-Galactose.yaml)'
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
summary: Per-record structured review for L-Galactose (data/ingredients/mapped/L-Galactose.yaml,
  record-3ab76711f22a16ac, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Galactose.yaml
    sha256: cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a
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
  - path: reports/yaml_record_review/L-Galactose.md
    sha256: 973b3b58ac5537cc6a83d4aa444ce3eb5189947fb7dc7640e9129b863d36015a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3ab76711f22a16ac
  path: data/ingredients/mapped/L-Galactose.yaml
  label: L-Galactose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Galactose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Galactose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Galactose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3ab76711f22a16ac
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-9367b4b09f013b4c
  - ev-8be2e34fa5bacbf8
  - ev-a555d17557b25fd9
  - ev-f1ee5c78a1d4f3a1
  - ev-8a78428d6cf7fea5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-9367b4b09f013b4c
  - ev-26289eeecfccd9aa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-bf20b2eaa4fb8b2d
  - ev-26289eeecfccd9aa
  - ev-c6c0245cff778869
evidence:
- evidence_id: ev-9367b4b09f013b4c
  kind: record_content
  reference: data/ingredients/mapped/L-Galactose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1222],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37618","line":1224,"mapping_status":"MAPPED","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose"}],"identifier":"CHEBI:37618","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37618","ontology_label":"L-galactose","ontology_source":"CHEBI"},"preferred_term":"L-Galactose","sssom_rows":[{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Galactose","synonym_count":1}'
  snapshot_sha256: cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a
- evidence_id: ev-8be2e34fa5bacbf8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1222]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a555d17557b25fd9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Galactose; data-row positions=[1572]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","other":"L-galacto-hexose|CAS:15572-79-9","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Galactose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f1ee5c78a1d4f3a1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1224]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:37618","line":1224,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bf20b2eaa4fb8b2d
  kind: prior_review
  reference: reports/yaml_record_review/L-Galactose.md
  locator: '`data/ingredients/mapped/L-Galactose.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:31; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 973b3b58ac5537cc6a83d4aa444ce3eb5189947fb7dc7640e9129b863d36015a
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` and\n\
    \  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,\n\
    \  or literature sources can support L-galactose as a carbon and energy source.\n\
    - Rerun strict, term, round-trip, role, component, and SSSOM validation after\n\
    \  the role changes."
- evidence_id: ev-26289eeecfccd9aa
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[789,1827,1928]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:efea5cb86dd9ae186189","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:4ee1c0e67e44ccb98697","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a","finding_id":"SEM:4716929324ed84558a24","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8a78428d6cf7fea5
  kind: record_content
  reference: data/ingredients/mapped/L-Galactose.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1222],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37618","line":1224,"mapping_status":"MAPPED","ontology_id":"CHEBI:37618","preferred_term":"L-Galactose"}],"identifier":"CHEBI:37618","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37618","ontology_label":"L-galactose","ontology_source":"CHEBI"},"preferred_term":"L-Galactose","sssom_rows":[{"data_row":1572,"object_id":"CHEBI:37618","object_label":"L-galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Galactose","synonym_count":1}'
  snapshot_sha256: cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a
- evidence_id: ev-c6c0245cff778869
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-f9e6c1cc26ce540a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f9e6c1cc26ce540a in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-e976064cbf7caafe
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-9367b4b09f013b4c
  - ev-8be2e34fa5bacbf8
  - ev-a555d17557b25fd9
  - ev-f1ee5c78a1d4f3a1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-64f051a76ac77e4f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-bf20b2eaa4fb8b2d
  - ev-9367b4b09f013b4c
  - ev-26289eeecfccd9aa
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:10:32Z;
    reviewed SHA-256=cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a;
    current SHA-256=cc736209403f41a4737eadc4bbe530f129fbe57c148505c9413746a61cf83b6a;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Galactose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:37618
    identity, CAS value, formula, ChEBI synonym, and final SSSOM row pass, but CARBON_SOURCE
    and ENERGY_SOURCE are only provisional computational roles.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bf20b2eaa4fb8b2d
    - ev-9367b4b09f013b4c
  - name: legacy-native-ids
    value: '["SEM:efea5cb86dd9ae186189","SEM:4ee1c0e67e44ccb98697","SEM:4716929324ed84558a24"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9367b4b09f013b4c
    - ev-bf20b2eaa4fb8b2d
    - ev-26289eeecfccd9aa
- assessment_id: a-8a78428d6cf7fea5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-bf20b2eaa4fb8b2d
  - ev-8a78428d6cf7fea5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bf20b2eaa4fb8b2d
    - ev-8a78428d6cf7fea5
findings:
- finding_id: rec-f-f9e6c1cc26ce540a
  issue_key: mim-reconciliation-role-support-3ab76711f22a16ac
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Galactose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ab76711f22a16ac
  evidence_ids:
  - ev-bf20b2eaa4fb8b2d
  - ev-8a78428d6cf7fea5
  - ev-c6c0245cff778869
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Galactose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-f9e6c1cc26ce540a
actions:
- action_id: rec-action-f9e6c1cc26ce540a
  description: 'Reassess prediction-only role support: L-Galactose'
  finding_ids:
  - rec-f-f9e6c1cc26ce540a
  target_ids:
  - record-3ab76711f22a16ac
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Galactose.yaml
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
