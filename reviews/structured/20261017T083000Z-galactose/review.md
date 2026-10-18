# Per-record structured review: Galactose (data/ingredients/mapped/Galactose.yaml)

- Review: 20261017T083000Z-galactose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Galactose (data/ingredients/mapped/Galactose.yaml, record-b4b4358f19a4321e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Galactose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Galactose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b4b4358f19a4321e | data/ingredients/mapped/Galactose.yaml | maintained | Galactose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b4b4358f19a4321e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b4b4358f19a4321e | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b4b4358f19a4321e | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b4b4358f19a4321e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b4b4358f19a4321e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:23:32Z; reviewed SHA-256=cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb; current SHA-256=cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb; hash_changed=False. Reports=["reports/yaml_record_review/Galactose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact galactose identity and CultureMech carbon role pass, but ENERGY_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-b4b4358f19a4321e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0711ee52abefd33f: Reassess prediction-only role support: Galactose

major / open / confirmed; issue key: mim-reconciliation-role-support-b4b4358f19a4321e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0711ee52abefd33f

Reassess prediction-only role support: Galactose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-377f3509654666fa | data/ingredients/mapped/Galactose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1035],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28260","line":1037,"mapping_status":"MAPPED","ontology_id":"CHEBI:28260","preferred_term":"Galactose"}],"identifier":"CHEBI:28260","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28260","ontology_label":"galactose","ontology_source":"CHEBI"},"preferred_term":"Galactose","sssom_rows":[{"data_row":1274,"object_id":"CHEBI:28260","object_label":"galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Galactose","synonym_count":6} |
| ev-88fc75f14d468c11 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1035] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8bcceabc780c674a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Galactose; data-row positions=[1274] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1274,"object_id":"CHEBI:28260","object_label":"galactose","other":"Gal&#124;Galaktose&#124;galacto-hexose&#124;CAS:26566-61-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Galactose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d8991bcd6ca84ad0 | docs/data/mapped_ingredients.csv; CSV lines=[1037] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28260","line":1037,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"CHEBI:28260","preferred_term":"Galactose","total_occurrences":"14"}] |
| ev-df122ca71cd9a05b | reports/yaml_record_review/Galactose.md; &#96;data/ingredients/mapped/Galactose.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Completeness:57; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2b9f4b9ad6e4d7c1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[648,1877] | context_only | [{"current_record_sha256":"cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb","finding_id":"SEM:fbb1ecc97d284026ac26","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb","finding_id":"SEM:f8699f6f4e6a7590fb5f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-56e598e2bd33b651 | data/ingredients/mapped/Galactose.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-2a43b508e85c7791 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-0711ee52abefd33f] | context_only | Predecessor structured review finding f-0711ee52abefd33f in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-galactose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Galactose (data/ingredients/mapped/Galactose.yaml)'
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
summary: Per-record structured review for Galactose (data/ingredients/mapped/Galactose.yaml,
  record-b4b4358f19a4321e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Galactose.yaml
    sha256: cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb
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
  - path: reports/yaml_record_review/Galactose.md
    sha256: cfbde96895b3d68ddbdafeb9cbbba3d490f5c355720d9497d8b033beb76abdbe
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b4b4358f19a4321e
  path: data/ingredients/mapped/Galactose.yaml
  label: Galactose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Galactose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Galactose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b4b4358f19a4321e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b4b4358f19a4321e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b4b4358f19a4321e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b4b4358f19a4321e
evidence:
- evidence_id: ev-377f3509654666fa
  kind: record_content
  reference: data/ingredients/mapped/Galactose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1035],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28260","line":1037,"mapping_status":"MAPPED","ontology_id":"CHEBI:28260","preferred_term":"Galactose"}],"identifier":"CHEBI:28260","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28260","ontology_label":"galactose","ontology_source":"CHEBI"},"preferred_term":"Galactose","sssom_rows":[{"data_row":1274,"object_id":"CHEBI:28260","object_label":"galactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Galactose","synonym_count":6}'
  snapshot_sha256: cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb
- evidence_id: ev-88fc75f14d468c11
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1035]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8bcceabc780c674a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Galactose; data-row positions=[1274]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1274,"object_id":"CHEBI:28260","object_label":"galactose","other":"Gal|Galaktose|galacto-hexose|CAS:26566-61-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Galactose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d8991bcd6ca84ad0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1037]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28260","line":1037,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"CHEBI:28260","preferred_term":"Galactose","total_occurrences":"14"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-df122ca71cd9a05b
  kind: prior_review
  reference: reports/yaml_record_review/Galactose.md
  locator: '`data/ingredients/mapped/Galactose.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:34; Completeness:57; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cfbde96895b3d68ddbdafeb9cbbba3d490f5c355720d9497d8b033beb76abdbe
  quote: "Recommended Edits:\n- Major: replace the provisional `ENERGY_SOURCE` facet\
    \ in\n  `data/ingredients/mapped/Galactose.yaml` with source-backed evidence or\n\
    \  remove it; sync `data/curated/mapped_ingredients.yaml` and rerun strict\n \
    \ validation."
- evidence_id: ev-2b9f4b9ad6e4d7c1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[648,1877]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb","finding_id":"SEM:fbb1ecc97d284026ac26","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb","finding_id":"SEM:f8699f6f4e6a7590fb5f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-56e598e2bd33b651
  kind: record_content
  reference: data/ingredients/mapped/Galactose.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb
- evidence_id: ev-2a43b508e85c7791
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-0711ee52abefd33f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0711ee52abefd33f in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-9b24bd1f4a32a8c7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b4b4358f19a4321e
  evidence_ids:
  - ev-377f3509654666fa
  - ev-88fc75f14d468c11
  - ev-8bcceabc780c674a
  - ev-d8991bcd6ca84ad0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d74957646a0a1cbc
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b4b4358f19a4321e
  evidence_ids:
  - ev-df122ca71cd9a05b
  - ev-377f3509654666fa
  - ev-2b9f4b9ad6e4d7c1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:23:32Z;
    reviewed SHA-256=cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb;
    current SHA-256=cf7e73c8c57501c0a5eb44a55908977c3ad4b6c4e296dbd4cd58ed5c7b821ceb;
    hash_changed=False. Reports=["reports/yaml_record_review/Galactose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact galactose
    identity and CultureMech carbon role pass, but ENERGY_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df122ca71cd9a05b
    - ev-377f3509654666fa
  - name: legacy-native-ids
    value: '["SEM:fbb1ecc97d284026ac26","SEM:f8699f6f4e6a7590fb5f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-377f3509654666fa
    - ev-df122ca71cd9a05b
    - ev-2b9f4b9ad6e4d7c1
- assessment_id: a-56e598e2bd33b651
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b4b4358f19a4321e
  evidence_ids:
  - ev-df122ca71cd9a05b
  - ev-56e598e2bd33b651
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df122ca71cd9a05b
    - ev-56e598e2bd33b651
findings:
- finding_id: rec-f-0711ee52abefd33f
  issue_key: mim-reconciliation-role-support-b4b4358f19a4321e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Galactose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b4b4358f19a4321e
  evidence_ids:
  - ev-df122ca71cd9a05b
  - ev-56e598e2bd33b651
  - ev-2a43b508e85c7791
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-0711ee52abefd33f
actions:
- action_id: rec-action-0711ee52abefd33f
  description: 'Reassess prediction-only role support: Galactose'
  finding_ids:
  - rec-f-0711ee52abefd33f
  target_ids:
  - record-b4b4358f19a4321e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose.yaml
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
