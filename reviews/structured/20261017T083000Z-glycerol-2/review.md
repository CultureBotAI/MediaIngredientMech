# Per-record structured review: Glycerol_2 (data/ingredients/mapped/Glycerol_2.yaml)

- Review: 20261017T083000Z-glycerol-2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycerol_2 (data/ingredients/mapped/Glycerol_2.yaml, record-513db52437603d7f, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycerol_2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycerol_2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-513db52437603d7f | data/ingredients/mapped/Glycerol_2.yaml | maintained | Glycerol_2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-513db52437603d7f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-513db52437603d7f | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-513db52437603d7f | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-513db52437603d7f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-513db52437603d7f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:07:22Z; reviewed SHA-256=b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344; current SHA-256=b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344; hash_changed=False. Reports=["reports/yaml_record_review/Glycerol_2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected lowercase glycerol tombstone no longer publishes final SSSOM, but stale pre-merge fields remain.

### Historical provisional-role concern

evidence: unknown. Targets: record-513db52437603d7f.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-513db52437603d7f: Reassess prediction-only or empty role support: Glycerol_2

minor / deferred / provisional; issue key: mim-reconciliation-role-support-513db52437603d7f.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

Disposition: The current local observation is recorded on a REJECTED tombstone, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-64ca55e66feba58b | data/ingredients/mapped/Glycerol_2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1070],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17754","line":1072,"mapping_status":"REJECTED","ontology_id":"CHEBI:17754","preferred_term":"glycerol"}],"identifier":"CHEBI:17754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":292,"edge_count":292,"occurrences":292},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17754","ontology_label":"glycerol","ontology_source":"CHEBI"},"preferred_term":"glycerol","sssom_rows":[],"sssom_subject":"MIM:Glycerol_2","synonym_count":14} |
| ev-34c618a82a2427ea | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1070] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bb7929fa270a4753 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycerol_2; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-7ad44afd15318b50 | docs/data/mapped_ingredients.csv; CSV lines=[1072] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17754","line":1072,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17754","preferred_term":"glycerol","total_occurrences":"0"}] |
| ev-5c1d8c861044fb62 | reports/yaml_record_review/Glycerol_2.md; &#96;data/ingredients/mapped/Glycerol_2.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:32; Completeness:51; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bd13ca59d0a6ba6f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[687] | context_only | [{"current_record_sha256":"b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344","finding_id":"SEM:549366cb4b505246028d","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-4efde99f0f9d7c57 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Glycerol_2.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycerol-2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycerol_2 (data/ingredients/mapped/Glycerol_2.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Glycerol_2 (data/ingredients/mapped/Glycerol_2.yaml,
  record-513db52437603d7f, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycerol_2.yaml
    sha256: b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344
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
  - path: reports/yaml_record_review/Glycerol_2.md
    sha256: 1210317f5b5bee354a8b663fe2846e540fe27a827c55fffc963d49b5ac9aaf15
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-513db52437603d7f
  path: data/ingredients/mapped/Glycerol_2.yaml
  label: Glycerol_2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol_2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycerol_2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycerol_2.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-513db52437603d7f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-513db52437603d7f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-513db52437603d7f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-513db52437603d7f
evidence:
- evidence_id: ev-64ca55e66feba58b
  kind: record_content
  reference: data/ingredients/mapped/Glycerol_2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1070],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17754","line":1072,"mapping_status":"REJECTED","ontology_id":"CHEBI:17754","preferred_term":"glycerol"}],"identifier":"CHEBI:17754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":292,"edge_count":292,"occurrences":292},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17754","ontology_label":"glycerol","ontology_source":"CHEBI"},"preferred_term":"glycerol","sssom_rows":[],"sssom_subject":"MIM:Glycerol_2","synonym_count":14}'
  snapshot_sha256: b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344
- evidence_id: ev-34c618a82a2427ea
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1070]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bb7929fa270a4753
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycerol_2; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7ad44afd15318b50
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1072]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17754","line":1072,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17754","preferred_term":"glycerol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5c1d8c861044fb62
  kind: prior_review
  reference: reports/yaml_record_review/Glycerol_2.md
  locator: '`data/ingredients/mapped/Glycerol_2.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:32; Completeness:51; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1210317f5b5bee354a8b663fe2846e540fe27a827c55fffc963d49b5ac9aaf15
  quote: "Recommended Edits:\n- Minor: trim stale pre-merge structure, role, and synonym\
    \ fields from\n  `data/ingredients/mapped/Glycerol_2.yaml`, or add a tombstone\
    \ note that these\n  retained fields are historical and not exported."
- evidence_id: ev-bd13ca59d0a6ba6f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[687]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344","finding_id":"SEM:549366cb4b505246028d","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4efde99f0f9d7c57
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Glycerol_2.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-18524544575ddc5b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-513db52437603d7f
  evidence_ids:
  - ev-64ca55e66feba58b
  - ev-34c618a82a2427ea
  - ev-bb7929fa270a4753
  - ev-7ad44afd15318b50
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bb3e2014644a4372
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-513db52437603d7f
  evidence_ids:
  - ev-5c1d8c861044fb62
  - ev-64ca55e66feba58b
  - ev-bd13ca59d0a6ba6f
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:07:22Z;
    reviewed SHA-256=b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344;
    current SHA-256=b3240086071f131249c8e39f438a22be0535cb128c258936f70339f1ae7b7344;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycerol_2.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected lowercase
    glycerol tombstone no longer publishes final SSSOM, but stale pre-merge fields
    remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5c1d8c861044fb62
    - ev-64ca55e66feba58b
  - name: legacy-native-ids
    value: '["SEM:549366cb4b505246028d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-64ca55e66feba58b
    - ev-5c1d8c861044fb62
    - ev-bd13ca59d0a6ba6f
- assessment_id: a-role-513db52437603d7f
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-513db52437603d7f
  evidence_ids:
  - ev-64ca55e66feba58b
  - ev-4efde99f0f9d7c57
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-64ca55e66feba58b
    - ev-4efde99f0f9d7c57
findings:
- finding_id: rec-f-role-513db52437603d7f
  issue_key: mim-reconciliation-role-support-513db52437603d7f
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only or empty role support: Glycerol_2'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-513db52437603d7f
  evidence_ids:
  - ev-64ca55e66feba58b
  - ev-4efde99f0f9d7c57
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol_2.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded on a REJECTED tombstone,
    but the named source/context or policy decision is still required; no correction
    is inferred.
actions: []
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
