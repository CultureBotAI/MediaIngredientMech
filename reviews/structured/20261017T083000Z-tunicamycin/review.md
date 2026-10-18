# Per-record structured review: Tunicamycin (data/ingredients/mapped/Tunicamycin.yaml)

- Review: 20261017T083000Z-tunicamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tunicamycin (data/ingredients/mapped/Tunicamycin.yaml, record-63ff5a477f11ebf9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tunicamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tunicamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-63ff5a477f11ebf9 | data/ingredients/mapped/Tunicamycin.yaml | maintained | Tunicamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-63ff5a477f11ebf9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-63ff5a477f11ebf9 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-63ff5a477f11ebf9 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-63ff5a477f11ebf9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-63ff5a477f11ebf9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:12:39Z; reviewed SHA-256=d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b; current SHA-256=d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b; hash_changed=False. Reports=["reports/yaml_record_review/Tunicamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity and final SSSOM row pass, but SELECTIVE_AGENT is provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-63ff5a477f11ebf9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-21a75cfeea3bb6b7: Reassess prediction-only role support: Tunicamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-63ff5a477f11ebf9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-21a75cfeea3bb6b7

Reassess prediction-only role support: Tunicamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-845be2fe2fe8d793 | data/ingredients/mapped/Tunicamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2014],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29699","line":2016,"mapping_status":"MAPPED","ontology_id":"CHEBI:29699","preferred_term":"Tunicamycin"}],"identifier":"CHEBI:29699","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:29699","ontology_label":"tunicamycin","ontology_source":"CHEBI"},"preferred_term":"Tunicamycin","sssom_rows":[{"data_row":2854,"object_id":"CHEBI:29699","object_label":"tunicamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tunicamycin","synonym_count":0} |
| ev-5e4ada30582d26d9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2014] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-eb1968402b9c8372 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tunicamycin; data-row positions=[2854] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2854,"object_id":"CHEBI:29699","object_label":"tunicamycin","other":"CAS:11089-65-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Tunicamycin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-3f0b104d8bc3ea95 | docs/data/mapped_ingredients.csv; CSV lines=[2016] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29699","line":2016,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29699","preferred_term":"Tunicamycin","total_occurrences":"0"}] |
| ev-409bee4b33bc5174 | reports/yaml_record_review/Tunicamycin.md; &#96;data/ingredients/mapped/Tunicamycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:32; Issues:41; Major: &#96;SELECTIVE_AGENT&#96; is provisional name-pattern evidence:43; Completeness:60; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-20d54bdae6efc4c0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1326,1795] | context_only | [{"current_record_sha256":"d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b","finding_id":"SEM:568e7fa1ebda0e6ba3d0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b","finding_id":"SEM:ccf3614c5f5ad4296830","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-78d7e077ee98ff1f | data/ingredients/mapped/Tunicamycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-5ccd5d2b25a166a1 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-21a75cfeea3bb6b7] | context_only | Predecessor structured review finding f-21a75cfeea3bb6b7 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tunicamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tunicamycin (data/ingredients/mapped/Tunicamycin.yaml)'
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
summary: Per-record structured review for Tunicamycin (data/ingredients/mapped/Tunicamycin.yaml,
  record-63ff5a477f11ebf9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tunicamycin.yaml
    sha256: d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Tunicamycin.md
    sha256: 09fa704535786a59896308047df631d90358877c324a4244dee9bcf030c7c915
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-63ff5a477f11ebf9
  path: data/ingredients/mapped/Tunicamycin.yaml
  label: Tunicamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tunicamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tunicamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tunicamycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-63ff5a477f11ebf9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-63ff5a477f11ebf9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-63ff5a477f11ebf9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-63ff5a477f11ebf9
evidence:
- evidence_id: ev-845be2fe2fe8d793
  kind: record_content
  reference: data/ingredients/mapped/Tunicamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2014],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29699","line":2016,"mapping_status":"MAPPED","ontology_id":"CHEBI:29699","preferred_term":"Tunicamycin"}],"identifier":"CHEBI:29699","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:29699","ontology_label":"tunicamycin","ontology_source":"CHEBI"},"preferred_term":"Tunicamycin","sssom_rows":[{"data_row":2854,"object_id":"CHEBI:29699","object_label":"tunicamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tunicamycin","synonym_count":0}'
  snapshot_sha256: d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b
- evidence_id: ev-5e4ada30582d26d9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2014]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-eb1968402b9c8372
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tunicamycin; data-row positions=[2854]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2854,"object_id":"CHEBI:29699","object_label":"tunicamycin","other":"CAS:11089-65-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Tunicamycin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3f0b104d8bc3ea95
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2016]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29699","line":2016,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29699","preferred_term":"Tunicamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-409bee4b33bc5174
  kind: prior_review
  reference: reports/yaml_record_review/Tunicamycin.md
  locator: '`data/ingredients/mapped/Tunicamycin.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:32; Issues:41; Major: `SELECTIVE_AGENT` is provisional
    name-pattern evidence:43; Completeness:60; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 09fa704535786a59896308047df631d90358877c324a4244dee9bcf030c7c915
  quote: "Issues:\n\n\nMajor: `SELECTIVE_AGENT` is provisional name-pattern evidence:\n\
    The only role assertion is:\n\n```yaml\nphysicochemical_roles:\n- role: SELECTIVE_AGENT\n\
    \  confidence: 0.8\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Inferred from curated media-role name pattern\n    curator_note:\
    \ Provisional role from a curated name-pattern rule; review recommended.\n```\n\
    \nThe exact CHEBI identity does not independently curate the selective-agent\n\
    role.\n\nRecommended Edits:\n- Replace the `SELECTIVE_AGENT` computational prediction\
    \ with curated\n  database/literature evidence, or remove `physicochemical_roles`\
    \ until such\n  support is added."
- evidence_id: ev-20d54bdae6efc4c0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1326,1795]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b","finding_id":"SEM:568e7fa1ebda0e6ba3d0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b","finding_id":"SEM:ccf3614c5f5ad4296830","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-78d7e077ee98ff1f
  kind: record_content
  reference: data/ingredients/mapped/Tunicamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b
- evidence_id: ev-5ccd5d2b25a166a1
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-21a75cfeea3bb6b7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-21a75cfeea3bb6b7 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-5c7710d718a4d4e3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-63ff5a477f11ebf9
  evidence_ids:
  - ev-845be2fe2fe8d793
  - ev-5e4ada30582d26d9
  - ev-eb1968402b9c8372
  - ev-3f0b104d8bc3ea95
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-04d87575da82853c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-63ff5a477f11ebf9
  evidence_ids:
  - ev-409bee4b33bc5174
  - ev-845be2fe2fe8d793
  - ev-20d54bdae6efc4c0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:12:39Z;
    reviewed SHA-256=d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b;
    current SHA-256=d6c1f7324d1f1fb0b60cd89c54e2b81950fdd873f6b32c76d3f2388a9092fe7b;
    hash_changed=False. Reports=["reports/yaml_record_review/Tunicamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity and final SSSOM row pass, but SELECTIVE_AGENT is provisional name-pattern
    evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-409bee4b33bc5174
    - ev-845be2fe2fe8d793
  - name: legacy-native-ids
    value: '["SEM:568e7fa1ebda0e6ba3d0","SEM:ccf3614c5f5ad4296830"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-845be2fe2fe8d793
    - ev-409bee4b33bc5174
    - ev-20d54bdae6efc4c0
- assessment_id: a-78d7e077ee98ff1f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-63ff5a477f11ebf9
  evidence_ids:
  - ev-409bee4b33bc5174
  - ev-78d7e077ee98ff1f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-409bee4b33bc5174
    - ev-78d7e077ee98ff1f
findings:
- finding_id: rec-f-21a75cfeea3bb6b7
  issue_key: mim-reconciliation-role-support-63ff5a477f11ebf9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tunicamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-63ff5a477f11ebf9
  evidence_ids:
  - ev-409bee4b33bc5174
  - ev-78d7e077ee98ff1f
  - ev-5ccd5d2b25a166a1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tunicamycin.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-21a75cfeea3bb6b7
actions:
- action_id: rec-action-21a75cfeea3bb6b7
  description: 'Reassess prediction-only role support: Tunicamycin'
  finding_ids:
  - rec-f-21a75cfeea3bb6b7
  target_ids:
  - record-63ff5a477f11ebf9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tunicamycin.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
````
