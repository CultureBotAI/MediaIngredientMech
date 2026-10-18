# Per-record structured review: Mgso4h2o (data/ingredients/mapped/Mgso4h2o.yaml)

- Review: 20261017T083000Z-mgso4h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mgso4h2o (data/ingredients/mapped/Mgso4h2o.yaml, record-fecf59a2a4be510b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mgso4h2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mgso4h2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fecf59a2a4be510b | data/ingredients/mapped/Mgso4h2o.yaml | maintained | Mgso4h2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fecf59a2a4be510b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-fecf59a2a4be510b | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fecf59a2a4be510b | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fecf59a2a4be510b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fecf59a2a4be510b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:20:48Z; reviewed SHA-256=7c5c152a51c5769d7acbeacf97f2f3ac23bf9217dd12787b658039ea38207585; current SHA-256=d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75; hash_changed=True. Reports=["reports/yaml_record_review/Mgso4h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The 1-water magnesium sulfate label is still mapped exactly to CHEBI:31795 magnesium sulfate heptahydrate and exports 7-water final SSSOM aliases.

### Historical provisional-role concern

evidence: concern. Targets: record-fecf59a2a4be510b.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-fecf59a2a4be510b: Reassess prediction-only or empty role support: Mgso4h2o

major / open / confirmed; issue key: mim-reconciliation-role-support-fecf59a2a4be510b.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-fecf59a2a4be510b

Reassess prediction-only or empty role support: Mgso4h2o

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b97be1f47ac05cd3 | data/ingredients/mapped/Mgso4h2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2679],"raw_equal":true},"docs_rows":[{"identifier":"cas:14168-73-1","line":2681,"mapping_status":"MAPPED","ontology_id":"CHEBI:32599","preferred_term":"MgSO4\u00b7H2O"}],"identifier":"cas:14168-73-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:32599","ontology_label":"magnesium sulfate","ontology_source":"CHEBI"},"preferred_term":"MgSO4\u00b7H2O","sssom_rows":[{"data_row":1870,"object_id":"CHEBI:32599","object_label":"magnesium sulfate","predicate_id":"skos:broadMatch"},{"data_row":1871,"object_id":"cas:14168-73-1","object_label":"MgSO4\u00b7H2O","predicate_id":"skos:exactMatch"},{"data_row":1872,"object_id":"kgmicrobe.compound:mgso4h2o","object_label":"MgSO4\u00b7H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgso4h2o","synonym_count":19} |
| ev-50e0991f392e5195 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2679] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d188dd0c8ab2723b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mgso4h2o; data-row positions=[1870, 1871, 1872] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1870,"object_id":"CHEBI:32599","object_label":"magnesium sulfate","other":"magnesium sulfate monohydrate&#124;MgSO4 x H2O&#124;MgSO4 . H2O&#124;MgSO4\u30fbH2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions&#124;REGISTRY&#124;2026-10-15"},{"data_row":1871,"object_id":"cas:14168-73-1","object_label":"MgSO4\u00b7H2O","other":"CAS:14168-73-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions&#124;REGISTRY&#124;2026-10-15"},{"data_row":1872,"object_id":"kgmicrobe.compound:mgso4h2o","object_label":"MgSO4\u00b7H2O","other":"CAS:14168-73-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions&#124;REGISTRY&#124;2026-10-15"}] |
| ev-4eb8b9524818b49f | docs/data/mapped_ingredients.csv; CSV lines=[2681] | supports | Published identity and count rows inspected: [{"identifier":"cas:14168-73-1","line":2681,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"CHEBI:32599","preferred_term":"MgSO4\u00b7H2O","total_occurrences":"19"}] |
| ev-5d35a74d990decda | reports/yaml_record_review/Mgso4h2o.md; &#96;data/ingredients/mapped/Mgso4h2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:32; Completeness:44; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-562be01b9d6d1400 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[940,1446] | context_only | [{"current_record_sha256":"d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75","finding_id":"SEM:ae352c84b5456ae95a4a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75","finding_id":"SEM:3c772872262945f27bb5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mgso4h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mgso4h2o (data/ingredients/mapped/Mgso4h2o.yaml)'
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
summary: Per-record structured review for Mgso4h2o (data/ingredients/mapped/Mgso4h2o.yaml,
  record-fecf59a2a4be510b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mgso4h2o.yaml
    sha256: d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Mgso4h2o.md
    sha256: bd249879d7bb608cb384db069ae76d423dedc2722ccc05375308e185bf8b9a6d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fecf59a2a4be510b
  path: data/ingredients/mapped/Mgso4h2o.yaml
  label: Mgso4h2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgso4h2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mgso4h2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mgso4h2o.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fecf59a2a4be510b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-b97be1f47ac05cd3
  - ev-50e0991f392e5195
  - ev-d188dd0c8ab2723b
  - ev-4eb8b9524818b49f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-b97be1f47ac05cd3
  - ev-562be01b9d6d1400
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-5d35a74d990decda
  - ev-562be01b9d6d1400
evidence:
- evidence_id: ev-b97be1f47ac05cd3
  kind: record_content
  reference: data/ingredients/mapped/Mgso4h2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2679],"raw_equal":true},"docs_rows":[{"identifier":"cas:14168-73-1","line":2681,"mapping_status":"MAPPED","ontology_id":"CHEBI:32599","preferred_term":"MgSO4\u00b7H2O"}],"identifier":"cas:14168-73-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:32599","ontology_label":"magnesium
    sulfate","ontology_source":"CHEBI"},"preferred_term":"MgSO4\u00b7H2O","sssom_rows":[{"data_row":1870,"object_id":"CHEBI:32599","object_label":"magnesium
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":1871,"object_id":"cas:14168-73-1","object_label":"MgSO4\u00b7H2O","predicate_id":"skos:exactMatch"},{"data_row":1872,"object_id":"kgmicrobe.compound:mgso4h2o","object_label":"MgSO4\u00b7H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgso4h2o","synonym_count":19}'
  snapshot_sha256: d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75
- evidence_id: ev-50e0991f392e5195
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2679]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d188dd0c8ab2723b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mgso4h2o; data-row positions=[1870, 1871, 1872]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1870,"object_id":"CHEBI:32599","object_label":"magnesium
    sulfate","other":"magnesium sulfate monohydrate|MgSO4 x H2O|MgSO4 . H2O|MgSO4\u30fbH2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions|REGISTRY|2026-10-15"},{"data_row":1871,"object_id":"cas:14168-73-1","object_label":"MgSO4\u00b7H2O","other":"CAS:14168-73-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions|REGISTRY|2026-10-15"},{"data_row":1872,"object_id":"kgmicrobe.compound:mgso4h2o","object_label":"MgSO4\u00b7H2O","other":"CAS:14168-73-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgso4h2o","validation_method":"manual:issue878_hydrate_contradictions|REGISTRY|2026-10-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4eb8b9524818b49f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2681]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:14168-73-1","line":2681,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"CHEBI:32599","preferred_term":"MgSO4\u00b7H2O","total_occurrences":"19"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5d35a74d990decda
  kind: prior_review
  reference: reports/yaml_record_review/Mgso4h2o.md
  locator: '`data/ingredients/mapped/Mgso4h2o.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:32; Completeness:44; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: bd249879d7bb608cb384db069ae76d423dedc2722ccc05375308e185bf8b9a6d
  quote: "Recommended Edits:\n- Major: localize the 1-water source identity or reject\
    \ it into the correct\n  magnesium sulfate hydrate representative so it no longer\
    \ publishes an exact\n  `CHEBI:31795` heptahydrate row.\n- Major: clear the heptahydrate\
    \ CAS and structure from\n  `data/ingredients/mapped/Mgso4h2o.yaml` unless the\
    \ source label is corrected\n  to the heptahydrate.\n- Major: remove the non-1-water\
    \ final SSSOM `other` labels and repair the\n  mineral-source role evidence."
- evidence_id: ev-562be01b9d6d1400
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[940,1446]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75","finding_id":"SEM:ae352c84b5456ae95a4a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75","finding_id":"SEM:3c772872262945f27bb5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4c09dd9a81e9dc44
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-b97be1f47ac05cd3
  - ev-50e0991f392e5195
  - ev-d188dd0c8ab2723b
  - ev-4eb8b9524818b49f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-03f012b3e36626c1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-5d35a74d990decda
  - ev-b97be1f47ac05cd3
  - ev-562be01b9d6d1400
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:20:48Z;
    reviewed SHA-256=7c5c152a51c5769d7acbeacf97f2f3ac23bf9217dd12787b658039ea38207585;
    current SHA-256=d91d36df2bec21cd4738f888c55ab1bbe0d0a50b453ca0589123c323a9d70c75;
    hash_changed=True. Reports=["reports/yaml_record_review/Mgso4h2o.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The 1-water magnesium sulfate
    label is still mapped exactly to CHEBI:31795 magnesium sulfate heptahydrate and
    exports 7-water final SSSOM aliases.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5d35a74d990decda
    - ev-b97be1f47ac05cd3
  - name: legacy-native-ids
    value: '["SEM:ae352c84b5456ae95a4a","SEM:3c772872262945f27bb5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b97be1f47ac05cd3
    - ev-5d35a74d990decda
    - ev-562be01b9d6d1400
- assessment_id: a-role-fecf59a2a4be510b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-b97be1f47ac05cd3
  - ev-562be01b9d6d1400
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b97be1f47ac05cd3
    - ev-562be01b9d6d1400
findings:
- finding_id: rec-f-role-fecf59a2a4be510b
  issue_key: mim-reconciliation-role-support-fecf59a2a4be510b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Mgso4h2o'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-fecf59a2a4be510b
  evidence_ids:
  - ev-b97be1f47ac05cd3
  - ev-562be01b9d6d1400
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgso4h2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-fecf59a2a4be510b
  description: 'Reassess prediction-only or empty role support: Mgso4h2o'
  finding_ids:
  - rec-f-role-fecf59a2a4be510b
  target_ids:
  - record-fecf59a2a4be510b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgso4h2o.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
