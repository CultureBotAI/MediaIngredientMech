# Per-record structured review: Geneticin_G418 (data/ingredients/mapped/Geneticin_G418.yaml)

- Review: 20261017T083000Z-geneticin-g418
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Geneticin_G418 (data/ingredients/mapped/Geneticin_G418.yaml, record-e06492d933196bbf, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Geneticin_G418.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Geneticin_G418.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e06492d933196bbf | data/ingredients/mapped/Geneticin_G418.yaml | maintained | Geneticin_G418 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e06492d933196bbf | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e06492d933196bbf | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e06492d933196bbf | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e06492d933196bbf.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e06492d933196bbf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z; reviewed SHA-256=94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b; current SHA-256=94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b; hash_changed=False. Reports=["reports/yaml_record_review/Geneticin_G418.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed geneticin identity passes, but SELECTIVE_AGENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-e06492d933196bbf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-76a3cdeb2981c8bc: Reassess prediction-only role support: Geneticin G418

major / open / confirmed; issue key: mim-reconciliation-role-support-e06492d933196bbf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-76a3cdeb2981c8bc

Reassess prediction-only role support: Geneticin G418

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-775367679dcb9e75 | data/ingredients/mapped/Geneticin_G418.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1045],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42768","line":1047,"mapping_status":"MAPPED","ontology_id":"CHEBI:42768","preferred_term":"Geneticin G418"}],"identifier":"CHEBI:42768","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:42768","ontology_label":"geneticin","ontology_source":"CHEBI"},"preferred_term":"Geneticin G418","sssom_rows":[{"data_row":1288,"object_id":"CHEBI:42768","object_label":"geneticin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geneticin_G418","synonym_count":1} |
| ev-8688f11c2c3acfc1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1045] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-227a7e08e2233834 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Geneticin_G418; data-row positions=[1288] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1288,"object_id":"CHEBI:42768","object_label":"geneticin","other":"(1R,2S,3S,4R,6S)-4,6-diamino-3-[3-deoxy-4-C-methyl-3-(methylamino)-beta-L-arabinopyranosyloxy]-2-hydroxycyclohexyl 2-amino-2,7-dideoxy-D-glycero-alpha-D-gluco-heptopyranoside&#124;CAS:49863-47-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Geneticin_G418","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-1abdb41de7a3f50d | docs/data/mapped_ingredients.csv; CSV lines=[1047] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:42768","line":1047,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:42768","preferred_term":"Geneticin G418","total_occurrences":"0"}] |
| ev-29c416cd6e5f100b | reports/yaml_record_review/Geneticin_G418.md; &#96;data/ingredients/mapped/Geneticin_G418.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-54ce0d026a60385c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[655,1421] | context_only | [{"current_record_sha256":"94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b","finding_id":"SEM:e7274aec7248d0237dd4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b","finding_id":"SEM:ef4ff6558048bb387f0d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-006fd79cf1448613 | data/ingredients/mapped/Geneticin_G418.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-b1d4b12404573188 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-76a3cdeb2981c8bc] | context_only | Predecessor structured review finding f-76a3cdeb2981c8bc in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-geneticin-g418
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Geneticin_G418 (data/ingredients/mapped/Geneticin_G418.yaml)'
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
summary: Per-record structured review for Geneticin_G418 (data/ingredients/mapped/Geneticin_G418.yaml,
  record-e06492d933196bbf, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Geneticin_G418.yaml
    sha256: 94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Geneticin_G418.md
    sha256: 9dcaa5c7a471e34bfee98e12c8bda0001a6f205ea464cb12628b04d960f6cb04
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e06492d933196bbf
  path: data/ingredients/mapped/Geneticin_G418.yaml
  label: Geneticin_G418
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geneticin_G418.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Geneticin_G418.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Geneticin_G418.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e06492d933196bbf
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e06492d933196bbf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e06492d933196bbf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e06492d933196bbf
evidence:
- evidence_id: ev-775367679dcb9e75
  kind: record_content
  reference: data/ingredients/mapped/Geneticin_G418.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1045],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42768","line":1047,"mapping_status":"MAPPED","ontology_id":"CHEBI:42768","preferred_term":"Geneticin
    G418"}],"identifier":"CHEBI:42768","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:42768","ontology_label":"geneticin","ontology_source":"CHEBI"},"preferred_term":"Geneticin
    G418","sssom_rows":[{"data_row":1288,"object_id":"CHEBI:42768","object_label":"geneticin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geneticin_G418","synonym_count":1}'
  snapshot_sha256: 94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b
- evidence_id: ev-8688f11c2c3acfc1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1045]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-227a7e08e2233834
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Geneticin_G418; data-row positions=[1288]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1288,"object_id":"CHEBI:42768","object_label":"geneticin","other":"(1R,2S,3S,4R,6S)-4,6-diamino-3-[3-deoxy-4-C-methyl-3-(methylamino)-beta-L-arabinopyranosyloxy]-2-hydroxycyclohexyl
    2-amino-2,7-dideoxy-D-glycero-alpha-D-gluco-heptopyranoside|CAS:49863-47-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Geneticin_G418","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1abdb41de7a3f50d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1047]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:42768","line":1047,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:42768","preferred_term":"Geneticin
    G418","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-29c416cd6e5f100b
  kind: prior_review
  reference: reports/yaml_record_review/Geneticin_G418.md
  locator: '`data/ingredients/mapped/Geneticin_G418.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:33; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9dcaa5c7a471e34bfee98e12c8bda0001a6f205ea464cb12628b04d960f6cb04
  quote: "Recommended Edits:\n- Major: replace `SELECTIVE_AGENT` with source-backed\
    \ evidence or remove the\n  role, then rerun strict validation."
- evidence_id: ev-54ce0d026a60385c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[655,1421]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b","finding_id":"SEM:e7274aec7248d0237dd4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b","finding_id":"SEM:ef4ff6558048bb387f0d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-006fd79cf1448613
  kind: record_content
  reference: data/ingredients/mapped/Geneticin_G418.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b
- evidence_id: ev-b1d4b12404573188
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-76a3cdeb2981c8bc]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-76a3cdeb2981c8bc in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-7cf2bc3710859fe9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e06492d933196bbf
  evidence_ids:
  - ev-775367679dcb9e75
  - ev-8688f11c2c3acfc1
  - ev-227a7e08e2233834
  - ev-1abdb41de7a3f50d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e88ff1f19e3f482c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e06492d933196bbf
  evidence_ids:
  - ev-29c416cd6e5f100b
  - ev-775367679dcb9e75
  - ev-54ce0d026a60385c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z;
    reviewed SHA-256=94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b;
    current SHA-256=94d2a28ec4de8a7ab984c0b2b830580651cf0c43d5a2a382c2ceeda9f886bf8b;
    hash_changed=False. Reports=["reports/yaml_record_review/Geneticin_G418.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-backed
    geneticin identity passes, but SELECTIVE_AGENT is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-29c416cd6e5f100b
    - ev-775367679dcb9e75
  - name: legacy-native-ids
    value: '["SEM:e7274aec7248d0237dd4","SEM:ef4ff6558048bb387f0d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-775367679dcb9e75
    - ev-29c416cd6e5f100b
    - ev-54ce0d026a60385c
- assessment_id: a-006fd79cf1448613
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e06492d933196bbf
  evidence_ids:
  - ev-29c416cd6e5f100b
  - ev-006fd79cf1448613
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-29c416cd6e5f100b
    - ev-006fd79cf1448613
findings:
- finding_id: rec-f-76a3cdeb2981c8bc
  issue_key: mim-reconciliation-role-support-e06492d933196bbf
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Geneticin G418'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e06492d933196bbf
  evidence_ids:
  - ev-29c416cd6e5f100b
  - ev-006fd79cf1448613
  - ev-b1d4b12404573188
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geneticin_G418.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-76a3cdeb2981c8bc
actions:
- action_id: rec-action-76a3cdeb2981c8bc
  description: 'Reassess prediction-only role support: Geneticin G418'
  finding_ids:
  - rec-f-76a3cdeb2981c8bc
  target_ids:
  - record-e06492d933196bbf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geneticin_G418.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
