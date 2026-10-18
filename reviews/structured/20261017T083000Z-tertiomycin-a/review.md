# Per-record structured review: Tertiomycin_A (data/ingredients/mapped/Tertiomycin_A.yaml)

- Review: 20261017T083000Z-tertiomycin-a
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tertiomycin_A (data/ingredients/mapped/Tertiomycin_A.yaml, record-e01d2e715f91943f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tertiomycin_A.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tertiomycin_A.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e01d2e715f91943f | data/ingredients/mapped/Tertiomycin_A.yaml | maintained | Tertiomycin_A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e01d2e715f91943f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e01d2e715f91943f | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e01d2e715f91943f | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e01d2e715f91943f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e01d2e715f91943f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:00:43Z; reviewed SHA-256=78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a; current SHA-256=78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a; hash_changed=False. Reports=["reports/yaml_record_review/Tertiomycin_A.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe placeholder identity passes, but SELECTIVE_AGENT is still only a provisional computational name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-e01d2e715f91943f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b1241f464055e387: Reassess prediction-only role support: Tertiomycin A

major / open / confirmed; issue key: mim-reconciliation-role-support-e01d2e715f91943f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b1241f464055e387

Reassess prediction-only role support: Tertiomycin A

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4369e0fa4c2774cf | data/ingredients/mapped/Tertiomycin_A.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1936],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin A"}],"identifier":"kgmicrobe.compound:tertiomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:tertiomycin_a","ontology_label":"Tertiomycin A","ontology_source":"kgmicrobe.compound"},"preferred_term":"Tertiomycin A","sssom_rows":[{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tertiomycin_A","synonym_count":0} |
| ev-bd3e7d622f975d4b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1936] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-05863dccf3fbdf24 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tertiomycin_A; data-row positions=[2732] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Tertiomycin_A","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-abce849ea0a26035 | docs/data/mapped_ingredients.csv; CSV lines=[1938] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin A","total_occurrences":"0"}] |
| ev-a9025545c2a6394b | reports/yaml_record_review/Tertiomycin_A.md; &#96;data/ingredients/mapped/Tertiomycin_A.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:30; Completeness:47; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a06680dd2ab44daa | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1271,1688] | context_only | [{"current_record_sha256":"78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a","finding_id":"SEM:26c7fd76fd5a5c9a3c77","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a","finding_id":"SEM:4fcb2635451950698fca","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-cd17334a2fcf72c4 | data/ingredients/mapped/Tertiomycin_A.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1936],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin A"}],"identifier":"kgmicrobe.compound:tertiomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:tertiomycin_a","ontology_label":"Tertiomycin A","ontology_source":"kgmicrobe.compound"},"preferred_term":"Tertiomycin A","sssom_rows":[{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tertiomycin_A","synonym_count":0} |
| ev-75145654bd0a40d7 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-b1241f464055e387] | context_only | Predecessor structured review finding f-b1241f464055e387 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tertiomycin-a
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tertiomycin_A (data/ingredients/mapped/Tertiomycin_A.yaml)'
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
summary: Per-record structured review for Tertiomycin_A (data/ingredients/mapped/Tertiomycin_A.yaml,
  record-e01d2e715f91943f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tertiomycin_A.yaml
    sha256: 78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Tertiomycin_A.md
    sha256: 33ce076df1848d721a83c8f62efafafe54aa976f2898751261d3125c97b2f2af
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e01d2e715f91943f
  path: data/ingredients/mapped/Tertiomycin_A.yaml
  label: Tertiomycin_A
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tertiomycin_A.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tertiomycin_A.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tertiomycin_A.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e01d2e715f91943f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-4369e0fa4c2774cf
  - ev-bd3e7d622f975d4b
  - ev-05863dccf3fbdf24
  - ev-abce849ea0a26035
  - ev-cd17334a2fcf72c4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-4369e0fa4c2774cf
  - ev-a06680dd2ab44daa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-a9025545c2a6394b
  - ev-a06680dd2ab44daa
  - ev-75145654bd0a40d7
evidence:
- evidence_id: ev-4369e0fa4c2774cf
  kind: record_content
  reference: data/ingredients/mapped/Tertiomycin_A.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1936],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin
    A"}],"identifier":"kgmicrobe.compound:tertiomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:tertiomycin_a","ontology_label":"Tertiomycin
    A","ontology_source":"kgmicrobe.compound"},"preferred_term":"Tertiomycin A","sssom_rows":[{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tertiomycin_A","synonym_count":0}'
  snapshot_sha256: 78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a
- evidence_id: ev-bd3e7d622f975d4b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1936]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-05863dccf3fbdf24
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tertiomycin_A; data-row positions=[2732]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin
    A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Tertiomycin_A","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-abce849ea0a26035
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1938]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin
    A","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a9025545c2a6394b
  kind: prior_review
  reference: reports/yaml_record_review/Tertiomycin_A.md
  locator: '`data/ingredients/mapped/Tertiomycin_A.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:30; Completeness:47; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 33ce076df1848d721a83c8f62efafafe54aa976f2898751261d3125c97b2f2af
  quote: "Recommended Edits:\n- Major: replace the provisional name-pattern `SELECTIVE_AGENT`\
    \ role in\n  `data/ingredients/mapped/Tertiomycin_A.yaml` with source-backed evidence\
    \ for\n  Tertiomycin A as a selective agent, or remove the role if no maintained\n\
    \  source supports it.\n- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`\n\
    \  and regenerate generated products so the role facets match the per-record\n\
    \  YAML."
- evidence_id: ev-a06680dd2ab44daa
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1271,1688]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a","finding_id":"SEM:26c7fd76fd5a5c9a3c77","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a","finding_id":"SEM:4fcb2635451950698fca","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-cd17334a2fcf72c4
  kind: record_content
  reference: data/ingredients/mapped/Tertiomycin_A.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1936],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:tertiomycin_a","line":1938,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:tertiomycin_a","preferred_term":"Tertiomycin
    A"}],"identifier":"kgmicrobe.compound:tertiomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:tertiomycin_a","ontology_label":"Tertiomycin
    A","ontology_source":"kgmicrobe.compound"},"preferred_term":"Tertiomycin A","sssom_rows":[{"data_row":2732,"object_id":"kgmicrobe.compound:tertiomycin_a","object_label":"Tertiomycin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tertiomycin_A","synonym_count":0}'
  snapshot_sha256: 78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a
- evidence_id: ev-75145654bd0a40d7
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-b1241f464055e387]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b1241f464055e387 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-11ab314fbab5e0b2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-4369e0fa4c2774cf
  - ev-bd3e7d622f975d4b
  - ev-05863dccf3fbdf24
  - ev-abce849ea0a26035
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e2a4cabd5513737b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-a9025545c2a6394b
  - ev-4369e0fa4c2774cf
  - ev-a06680dd2ab44daa
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:00:43Z;
    reviewed SHA-256=78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a;
    current SHA-256=78cc4f58e50f0be6af20f18852d731e266842ed24373ecbf285265349a62d57a;
    hash_changed=False. Reports=["reports/yaml_record_review/Tertiomycin_A.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local kgmicrobe
    placeholder identity passes, but SELECTIVE_AGENT is still only a provisional computational
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9025545c2a6394b
    - ev-4369e0fa4c2774cf
  - name: legacy-native-ids
    value: '["SEM:26c7fd76fd5a5c9a3c77","SEM:4fcb2635451950698fca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4369e0fa4c2774cf
    - ev-a9025545c2a6394b
    - ev-a06680dd2ab44daa
- assessment_id: a-cd17334a2fcf72c4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-a9025545c2a6394b
  - ev-cd17334a2fcf72c4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9025545c2a6394b
    - ev-cd17334a2fcf72c4
findings:
- finding_id: rec-f-b1241f464055e387
  issue_key: mim-reconciliation-role-support-e01d2e715f91943f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tertiomycin A'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e01d2e715f91943f
  evidence_ids:
  - ev-a9025545c2a6394b
  - ev-cd17334a2fcf72c4
  - ev-75145654bd0a40d7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tertiomycin_A.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-b1241f464055e387
actions:
- action_id: rec-action-b1241f464055e387
  description: 'Reassess prediction-only role support: Tertiomycin A'
  finding_ids:
  - rec-f-b1241f464055e387
  target_ids:
  - record-e01d2e715f91943f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tertiomycin_A.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
