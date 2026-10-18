# Per-record structured review: Beef_Heart_Infusion (data/ingredients/mapped/Beef_Heart_Infusion.yaml)

- Review: 20261017T083000Z-beef-heart-infusion
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beef_Heart_Infusion (data/ingredients/mapped/Beef_Heart_Infusion.yaml, record-8f9aff89e3f3cc18, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beef_Heart_Infusion.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beef_Heart_Infusion.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8f9aff89e3f3cc18 | data/ingredients/mapped/Beef_Heart_Infusion.yaml | maintained | Beef_Heart_Infusion |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8f9aff89e3f3cc18 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8f9aff89e3f3cc18 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8f9aff89e3f3cc18 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8f9aff89e3f3cc18.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8f9aff89e3f3cc18.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:26:42Z; reviewed SHA-256=dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815; current SHA-256=dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815; hash_changed=False. Reports=["reports/yaml_record_review/Beef_Heart_Infusion.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient beef heart infusion identity, FOODON parent, protein-source role, occurrence count, SSSOM rows, and aggregate copy pass, but top-level notes still describe the old unmapped state.

### Historical provisional-role concern

evidence: concern. Targets: record-8f9aff89e3f3cc18.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-8f9aff89e3f3cc18: Reassess prediction-only or empty role support: Beef_Heart_Infusion

major / open / confirmed; issue key: mim-reconciliation-role-support-8f9aff89e3f3cc18.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-8f9aff89e3f3cc18

Reassess prediction-only or empty role support: Beef_Heart_Infusion

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6f7e7710c5786385 | data/ingredients/mapped/Beef_Heart_Infusion.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[565],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beef_heart_infusion","line":567,"mapping_status":"MAPPED","ontology_id":"FOODON:00004410","preferred_term":"Beef Heart Infusion"}],"identifier":"kgmicrobe.ingredient:beef_heart_infusion","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"FOODON:00004410","ontology_label":"beef heart","ontology_source":"FOODON"},"preferred_term":"Beef Heart Infusion","sssom_rows":[{"data_row":500,"object_id":"FOODON:00004410","object_label":"beef heart","predicate_id":"skos:broadMatch"},{"data_row":501,"object_id":"kgmicrobe.ingredient:beef_heart_infusion","object_label":"Beef Heart Infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Heart_Infusion","synonym_count":1} |
| ev-f79cff76f0c77efc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [565] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ea379de8c3e84680 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beef_Heart_Infusion; data-row positions=[500, 501] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":500,"object_id":"FOODON:00004410","object_label":"beef heart","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Beef_Heart_Infusion","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":501,"object_id":"kgmicrobe.ingredient:beef_heart_infusion","object_label":"Beef Heart Infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Heart_Infusion","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-678b329977bc0b20 | docs/data/mapped_ingredients.csv; CSV lines=[567] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beef_heart_infusion","line":567,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"FOODON:00004410","preferred_term":"Beef Heart Infusion","total_occurrences":"2"}] |
| ev-069dbade97bbaec7 | reports/yaml_record_review/Beef_Heart_Infusion.md; &#96;data/ingredients/mapped/Beef_Heart_Infusion.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:33; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1f4661edb3217f35 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[300,1515] | context_only | [{"current_record_sha256":"dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815","finding_id":"SEM:772f1eb42d60ea355329","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815","finding_id":"SEM:2bd8ada4f86c29066730","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beef-heart-infusion
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beef_Heart_Infusion (data/ingredients/mapped/Beef_Heart_Infusion.yaml)'
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
summary: Per-record structured review for Beef_Heart_Infusion (data/ingredients/mapped/Beef_Heart_Infusion.yaml,
  record-8f9aff89e3f3cc18, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beef_Heart_Infusion.yaml
    sha256: dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Beef_Heart_Infusion.md
    sha256: d37a2d367657d4b0055f755537dee9e1f6127b206f35fce4a954fe98f0920ae7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8f9aff89e3f3cc18
  path: data/ingredients/mapped/Beef_Heart_Infusion.yaml
  label: Beef_Heart_Infusion
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart_Infusion.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beef_Heart_Infusion.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beef_Heart_Infusion.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8f9aff89e3f3cc18
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-6f7e7710c5786385
  - ev-f79cff76f0c77efc
  - ev-ea379de8c3e84680
  - ev-678b329977bc0b20
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-6f7e7710c5786385
  - ev-1f4661edb3217f35
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-069dbade97bbaec7
  - ev-1f4661edb3217f35
evidence:
- evidence_id: ev-6f7e7710c5786385
  kind: record_content
  reference: data/ingredients/mapped/Beef_Heart_Infusion.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[565],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beef_heart_infusion","line":567,"mapping_status":"MAPPED","ontology_id":"FOODON:00004410","preferred_term":"Beef
    Heart Infusion"}],"identifier":"kgmicrobe.ingredient:beef_heart_infusion","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"FOODON:00004410","ontology_label":"beef
    heart","ontology_source":"FOODON"},"preferred_term":"Beef Heart Infusion","sssom_rows":[{"data_row":500,"object_id":"FOODON:00004410","object_label":"beef
    heart","predicate_id":"skos:broadMatch"},{"data_row":501,"object_id":"kgmicrobe.ingredient:beef_heart_infusion","object_label":"Beef
    Heart Infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Heart_Infusion","synonym_count":1}'
  snapshot_sha256: dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815
- evidence_id: ev-f79cff76f0c77efc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [565]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ea379de8c3e84680
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beef_Heart_Infusion; data-row positions=[500, 501]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":500,"object_id":"FOODON:00004410","object_label":"beef
    heart","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Beef_Heart_Infusion","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":501,"object_id":"kgmicrobe.ingredient:beef_heart_infusion","object_label":"Beef
    Heart Infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Heart_Infusion","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-678b329977bc0b20
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[567]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beef_heart_infusion","line":567,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"FOODON:00004410","preferred_term":"Beef
    Heart Infusion","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-069dbade97bbaec7
  kind: prior_review
  reference: reports/yaml_record_review/Beef_Heart_Infusion.md
  locator: '`data/ingredients/mapped/Beef_Heart_Infusion.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:33; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d37a2d367657d4b0055f755537dee9e1f6127b206f35fce4a954fe98f0920ae7
  quote: "Recommended Edits:\n- Minor: update `notes` in `data/ingredients/mapped/Beef_Heart_Infusion.yaml`\n\
    \  to describe the current kg-microbe identity and FOODON parent mapping, then\n\
    \  run `just sync-curated`."
- evidence_id: ev-1f4661edb3217f35
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[300,1515]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815","finding_id":"SEM:772f1eb42d60ea355329","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815","finding_id":"SEM:2bd8ada4f86c29066730","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2bab14ec9211e96a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-6f7e7710c5786385
  - ev-f79cff76f0c77efc
  - ev-ea379de8c3e84680
  - ev-678b329977bc0b20
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fa6544339f50081b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-069dbade97bbaec7
  - ev-6f7e7710c5786385
  - ev-1f4661edb3217f35
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:26:42Z;
    reviewed SHA-256=dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815;
    current SHA-256=dcd66af5e4938632357716d9b874020373d96f1e79f95a4b79a0c69dd16a9815;
    hash_changed=False. Reports=["reports/yaml_record_review/Beef_Heart_Infusion.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient
    beef heart infusion identity, FOODON parent, protein-source role, occurrence count,
    SSSOM rows, and aggregate copy pass, but top-level notes still describe the old
    unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-069dbade97bbaec7
    - ev-6f7e7710c5786385
  - name: legacy-native-ids
    value: '["SEM:772f1eb42d60ea355329","SEM:2bd8ada4f86c29066730"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6f7e7710c5786385
    - ev-069dbade97bbaec7
    - ev-1f4661edb3217f35
- assessment_id: a-role-8f9aff89e3f3cc18
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-6f7e7710c5786385
  - ev-1f4661edb3217f35
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6f7e7710c5786385
    - ev-1f4661edb3217f35
findings:
- finding_id: rec-f-role-8f9aff89e3f3cc18
  issue_key: mim-reconciliation-role-support-8f9aff89e3f3cc18
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beef_Heart_Infusion'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-8f9aff89e3f3cc18
  evidence_ids:
  - ev-6f7e7710c5786385
  - ev-1f4661edb3217f35
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart_Infusion.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-8f9aff89e3f3cc18
  description: 'Reassess prediction-only or empty role support: Beef_Heart_Infusion'
  finding_ids:
  - rec-f-role-8f9aff89e3f3cc18
  target_ids:
  - record-8f9aff89e3f3cc18
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart_Infusion.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
