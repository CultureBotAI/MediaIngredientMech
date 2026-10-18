# Per-record structured review: 7-hydroxyflavone (data/ingredients/mapped/7-hydroxyflavone.yaml)

- Review: 20261017T083000Z-7-hydroxyflavone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 7-hydroxyflavone (data/ingredients/mapped/7-hydroxyflavone.yaml, record-d8006d43e0c3174c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/7-hydroxyflavone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/7-hydroxyflavone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d8006d43e0c3174c | data/ingredients/mapped/7-hydroxyflavone.yaml | maintained | 7-hydroxyflavone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d8006d43e0c3174c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d8006d43e0c3174c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d8006d43e0c3174c | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d8006d43e0c3174c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d8006d43e0c3174c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:49:01Z; reviewed SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd; current SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd; hash_changed=False. Reports=["reports/yaml_record_review/7-hydroxyflavone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, synonym, chemistry, SSSOM, and aggregate pass; one historic auto-backfill change string has a truncated InChI.

## Findings

### rec-f-8dafe4e9a618f47a: Historical review coverage and residual narrative: 7-hydroxyflavone

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d8006d43e0c3174c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:49:01Z; reviewed SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd; current SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd; hash_changed=False. Reports=["reports/yaml_record_review/7-hydroxyflavone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, synonym, chemistry, SSSOM, and aggregate pass; one historic auto-backfill change string has a truncated InChI.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7f38aa6a6b20d2f8 | data/ingredients/mapped/7-hydroxyflavone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[422],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2268","line":424,"mapping_status":"MAPPED","ontology_id":"CHEBI:2268","preferred_term":"7-hydroxyflavone"}],"identifier":"CHEBI:2268","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2268","ontology_label":"7-hydroxyflavone","ontology_source":"CHEBI"},"preferred_term":"7-hydroxyflavone","sssom_rows":[{"data_row":253,"object_id":"CHEBI:2268","object_label":"7-hydroxyflavone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:7-hydroxyflavone","synonym_count":1} |
| ev-163fe23b46761b1b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [422] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-abf8e0c8a4b3b2ca | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:7-hydroxyflavone; data-row positions=[253] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":253,"object_id":"CHEBI:2268","object_label":"7-hydroxyflavone","other":"7-hydroxy-2-phenyl-4H-chromen-4-one&#124;CAS:6665-86-7","predicate_id":"skos:exactMatch","subject_id":"MIM:7-hydroxyflavone","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-bd3e026914496a77 | docs/data/mapped_ingredients.csv; CSV lines=[424] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:2268","line":424,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2268","preferred_term":"7-hydroxyflavone","total_occurrences":"0"}] |
| ev-363256b1756dd811 | reports/yaml_record_review/7-hydroxyflavone.md; &#96;data/ingredients/mapped/7-hydroxyflavone.yaml&#96;:2; Verdict:4; Identity:10; Validation:27; Evidence:42; Completeness:58; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5bcfb9cd87b82516 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[178] | context_only | [{"current_record_sha256":"be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd","finding_id":"SEM:531e5541467bf9bed261","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-7-hydroxyflavone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 7-hydroxyflavone (data/ingredients/mapped/7-hydroxyflavone.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for 7-hydroxyflavone (data/ingredients/mapped/7-hydroxyflavone.yaml,
  record-d8006d43e0c3174c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/7-hydroxyflavone.yaml
    sha256: be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd
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
  - path: reports/yaml_record_review/7-hydroxyflavone.md
    sha256: 2a7c47c5f6fa0f3b96eaee7b45c073aeeb03be246a25fbac17dbf053cd99b5f6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d8006d43e0c3174c
  path: data/ingredients/mapped/7-hydroxyflavone.yaml
  label: 7-hydroxyflavone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/7-hydroxyflavone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/7-hydroxyflavone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/7-hydroxyflavone.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d8006d43e0c3174c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d8006d43e0c3174c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d8006d43e0c3174c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d8006d43e0c3174c
evidence:
- evidence_id: ev-7f38aa6a6b20d2f8
  kind: record_content
  reference: data/ingredients/mapped/7-hydroxyflavone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[422],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2268","line":424,"mapping_status":"MAPPED","ontology_id":"CHEBI:2268","preferred_term":"7-hydroxyflavone"}],"identifier":"CHEBI:2268","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2268","ontology_label":"7-hydroxyflavone","ontology_source":"CHEBI"},"preferred_term":"7-hydroxyflavone","sssom_rows":[{"data_row":253,"object_id":"CHEBI:2268","object_label":"7-hydroxyflavone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:7-hydroxyflavone","synonym_count":1}'
  snapshot_sha256: be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd
- evidence_id: ev-163fe23b46761b1b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [422]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-abf8e0c8a4b3b2ca
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:7-hydroxyflavone; data-row positions=[253]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":253,"object_id":"CHEBI:2268","object_label":"7-hydroxyflavone","other":"7-hydroxy-2-phenyl-4H-chromen-4-one|CAS:6665-86-7","predicate_id":"skos:exactMatch","subject_id":"MIM:7-hydroxyflavone","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bd3e026914496a77
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[424]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:2268","line":424,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2268","preferred_term":"7-hydroxyflavone","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-363256b1756dd811
  kind: prior_review
  reference: reports/yaml_record_review/7-hydroxyflavone.md
  locator: '`data/ingredients/mapped/7-hydroxyflavone.yaml`:2; Verdict:4; Identity:10;
    Validation:27; Evidence:42; Completeness:58; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2a7c47c5f6fa0f3b96eaee7b45c073aeeb03be246a25fbac17dbf053cd99b5f6
  quote: "Recommended Edits:\n- Optionally clarify the stale\n  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes`\
    \ string in\n  `data/ingredients/mapped/7-hydroxyflavone.yaml` so it no longer\
    \ shows a\n  truncated InChI. No identity, chemistry, synonym, or SSSOM edit is\
    \ required."
- evidence_id: ev-5bcfb9cd87b82516
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[178]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd","finding_id":"SEM:531e5541467bf9bed261","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-60ab571b3239b09d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d8006d43e0c3174c
  evidence_ids:
  - ev-7f38aa6a6b20d2f8
  - ev-163fe23b46761b1b
  - ev-abf8e0c8a4b3b2ca
  - ev-bd3e026914496a77
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-334fdd67eca53039
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d8006d43e0c3174c
  evidence_ids:
  - ev-363256b1756dd811
  - ev-7f38aa6a6b20d2f8
  - ev-5bcfb9cd87b82516
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:49:01Z;
    reviewed SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd;
    current SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd;
    hash_changed=False. Reports=["reports/yaml_record_review/7-hydroxyflavone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, synonym, chemistry, SSSOM, and aggregate pass; one historic
    auto-backfill change string has a truncated InChI.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-363256b1756dd811
    - ev-7f38aa6a6b20d2f8
  - name: legacy-native-ids
    value: '["SEM:531e5541467bf9bed261"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7f38aa6a6b20d2f8
    - ev-363256b1756dd811
    - ev-5bcfb9cd87b82516
findings:
- finding_id: rec-f-8dafe4e9a618f47a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d8006d43e0c3174c
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 7-hydroxyflavone'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:49:01Z;
    reviewed SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd;
    current SHA-256=be85b69fb988397854e68903b775b0ab68116399d6bb4d590f4f7261e31c07bd;
    hash_changed=False. Reports=["reports/yaml_record_review/7-hydroxyflavone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, synonym, chemistry, SSSOM, and aggregate pass; one historic
    auto-backfill change string has a truncated InChI.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d8006d43e0c3174c
  evidence_ids:
  - ev-363256b1756dd811
  - ev-7f38aa6a6b20d2f8
  - ev-5bcfb9cd87b82516
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/7-hydroxyflavone.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
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
