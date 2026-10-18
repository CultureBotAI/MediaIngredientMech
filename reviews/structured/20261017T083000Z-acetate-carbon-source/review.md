# Per-record structured review: Acetate_Carbon_Source (data/ingredients/mapped/Acetate_Carbon_Source.yaml)

- Review: 20261017T083000Z-acetate-carbon-source
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Acetate_Carbon_Source (data/ingredients/mapped/Acetate_Carbon_Source.yaml, record-2410003b5461b69f, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Acetate_Carbon_Source.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Acetate_Carbon_Source.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2410003b5461b69f | data/ingredients/mapped/Acetate_Carbon_Source.yaml | maintained | Acetate_Carbon_Source |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2410003b5461b69f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2410003b5461b69f | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2410003b5461b69f | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2410003b5461b69f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2410003b5461b69f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:02:19Z; reviewed SHA-256=ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061; current SHA-256=ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061; hash_changed=False. Reports=["reports/yaml_record_review/Acetate_Carbon_Source.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected Acetate (carbon source) tombstone points at the retained Acetate record and no longer exports SSSOM; only stale notes and advisory TSV rows predate the merge.

### Historical provisional-role concern

evidence: unknown. Targets: record-2410003b5461b69f.

Current role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-2410003b5461b69f: Reassess prediction-only or empty role support: Acetate_Carbon_Source

minor / deferred / provisional; issue key: mim-reconciliation-role-support-2410003b5461b69f.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

Disposition: The current local observation is recorded on a REJECTED tombstone, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2ded0937bbcbab9c | data/ingredients/mapped/Acetate_Carbon_Source.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[439],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30089","line":441,"mapping_status":"REJECTED","ontology_id":"CHEBI:30089","preferred_term":"Acetate (carbon source)"}],"identifier":"CHEBI:30089","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30089","ontology_label":"acetate","ontology_source":"CHEBI"},"preferred_term":"Acetate (carbon source)","sssom_rows":[],"sssom_subject":"MIM:Acetate_Carbon_Source","synonym_count":1} |
| ev-510ede3f1a840ca6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [439] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-04d0c7e649f12343 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Acetate_Carbon_Source; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-b117bb3e7c1ec547 | docs/data/mapped_ingredients.csv; CSV lines=[441] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30089","line":441,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:30089","preferred_term":"Acetate (carbon source)","total_occurrences":"0"}] |
| ev-51b97333355626da | reports/yaml_record_review/Acetate_Carbon_Source.md; &#96;data/ingredients/mapped/Acetate_Carbon_Source.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:42; Completeness:62; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5ac3e2b3ff95dcb6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[196] | context_only | [{"current_record_sha256":"ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061","finding_id":"SEM:54d1f802b16ed4120fab","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-acetate-carbon-source
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Acetate_Carbon_Source (data/ingredients/mapped/Acetate_Carbon_Source.yaml)'
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
summary: Per-record structured review for Acetate_Carbon_Source (data/ingredients/mapped/Acetate_Carbon_Source.yaml,
  record-2410003b5461b69f, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Acetate_Carbon_Source.yaml
    sha256: ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/Acetate_Carbon_Source.md
    sha256: 62481e8523c4a1b77c9c154fd11f4c745d843a37c39b963837bf6d203adb04c8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2410003b5461b69f
  path: data/ingredients/mapped/Acetate_Carbon_Source.yaml
  label: Acetate_Carbon_Source
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetate_Carbon_Source.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Acetate_Carbon_Source.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Acetate_Carbon_Source.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2410003b5461b69f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-2ded0937bbcbab9c
  - ev-510ede3f1a840ca6
  - ev-04d0c7e649f12343
  - ev-b117bb3e7c1ec547
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-2ded0937bbcbab9c
  - ev-5ac3e2b3ff95dcb6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-51b97333355626da
  - ev-5ac3e2b3ff95dcb6
evidence:
- evidence_id: ev-2ded0937bbcbab9c
  kind: record_content
  reference: data/ingredients/mapped/Acetate_Carbon_Source.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[439],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30089","line":441,"mapping_status":"REJECTED","ontology_id":"CHEBI:30089","preferred_term":"Acetate
    (carbon source)"}],"identifier":"CHEBI:30089","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30089","ontology_label":"acetate","ontology_source":"CHEBI"},"preferred_term":"Acetate
    (carbon source)","sssom_rows":[],"sssom_subject":"MIM:Acetate_Carbon_Source","synonym_count":1}'
  snapshot_sha256: ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061
- evidence_id: ev-510ede3f1a840ca6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [439]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-04d0c7e649f12343
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Acetate_Carbon_Source; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b117bb3e7c1ec547
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[441]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30089","line":441,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:30089","preferred_term":"Acetate
    (carbon source)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-51b97333355626da
  kind: prior_review
  reference: reports/yaml_record_review/Acetate_Carbon_Source.md
  locator: '`data/ingredients/mapped/Acetate_Carbon_Source.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:42; Completeness:62; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 62481e8523c4a1b77c9c154fd11f4c745d843a37c39b963837bf6d203adb04c8
  quote: "Recommended Edits:\n- Optionally refresh the stale top-level `notes` in\n\
    \  `data/ingredients/mapped/Acetate_Carbon_Source.yaml` and derived\n  row-review/cross-record\
    \ tables so they no longer describe this tombstone as\n  still pending mapping\
    \ review. No tombstone, SSSOM, or ChEBI pointer edit is\n  required."
- evidence_id: ev-5ac3e2b3ff95dcb6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[196]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061","finding_id":"SEM:54d1f802b16ed4120fab","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4033fc10b214a2f0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-2ded0937bbcbab9c
  - ev-510ede3f1a840ca6
  - ev-04d0c7e649f12343
  - ev-b117bb3e7c1ec547
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9c7a5fc1f6594024
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-51b97333355626da
  - ev-2ded0937bbcbab9c
  - ev-5ac3e2b3ff95dcb6
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:02:19Z;
    reviewed SHA-256=ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061;
    current SHA-256=ab66b23c404877bcdb21cead87083ef1f7df4aacaa817ab3dab495c606626061;
    hash_changed=False. Reports=["reports/yaml_record_review/Acetate_Carbon_Source.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The rejected
    Acetate (carbon source) tombstone points at the retained Acetate record and no
    longer exports SSSOM; only stale notes and advisory TSV rows predate the merge.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-51b97333355626da
    - ev-2ded0937bbcbab9c
  - name: legacy-native-ids
    value: '["SEM:54d1f802b16ed4120fab"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2ded0937bbcbab9c
    - ev-51b97333355626da
    - ev-5ac3e2b3ff95dcb6
- assessment_id: a-role-2410003b5461b69f
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Current role assertions on nutritional_roles[0], nutritional_roles[1] rely
    only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed
    curation support.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-2ded0937bbcbab9c
  - ev-5ac3e2b3ff95dcb6
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2ded0937bbcbab9c
    - ev-5ac3e2b3ff95dcb6
findings:
- finding_id: rec-f-role-2410003b5461b69f
  issue_key: mim-reconciliation-role-support-2410003b5461b69f
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only or empty role support: Acetate_Carbon_Source'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the
    local evidence gap, not that the biological role is false.
  target_ids:
  - record-2410003b5461b69f
  evidence_ids:
  - ev-2ded0937bbcbab9c
  - ev-5ac3e2b3ff95dcb6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetate_Carbon_Source.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
