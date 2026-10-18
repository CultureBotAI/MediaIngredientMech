# Per-record structured review: 1-octen-3-ol (data/ingredients/mapped/1-octen-3-ol.yaml)

- Review: 20261017T083000Z-1-octen-3-ol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 1-octen-3-ol (data/ingredients/mapped/1-octen-3-ol.yaml, record-86418cebca163e89, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/1-octen-3-ol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/1-octen-3-ol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-86418cebca163e89 | data/ingredients/mapped/1-octen-3-ol.yaml | maintained | 1-octen-3-ol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-86418cebca163e89 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-86418cebca163e89 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-86418cebca163e89 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-86418cebca163e89.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-86418cebca163e89.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:15:41Z; reviewed SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff; current SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff; hash_changed=False. Reports=["reports/yaml_record_review/1-octen-3-ol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded CHEBI identity passes, but the open kgscan discussion is irrelevant and unattached.

## Findings

### rec-f-2f7a117f017a61a3: Historical review coverage and residual narrative: 1-octen-3-ol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-86418cebca163e89.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:15:41Z; reviewed SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff; current SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff; hash_changed=False. Reports=["reports/yaml_record_review/1-octen-3-ol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded CHEBI identity passes, but the open kgscan discussion is irrelevant and unattached.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-52fe4a2e31c71b04 | data/ingredients/mapped/1-octen-3-ol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[289],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:34118","line":291,"mapping_status":"MAPPED","ontology_id":"CHEBI:34118","preferred_term":"1-octen-3-ol"}],"identifier":"CHEBI:34118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:34118","ontology_label":"oct-1-en-3-ol","ontology_source":"CHEBI"},"preferred_term":"1-octen-3-ol","sssom_rows":[{"data_row":26,"object_id":"CHEBI:34118","object_label":"oct-1-en-3-ol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-octen-3-ol","synonym_count":0} |
| ev-93922ed2417602e1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [289] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False. |
| ev-1e58fcdf2ca69b60 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:1-octen-3-ol; data-row positions=[26] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":26,"object_id":"CHEBI:34118","object_label":"oct-1-en-3-ol","other":"CAS:3391-86-4","predicate_id":"skos:exactMatch","subject_id":"MIM:1-octen-3-ol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-260d2a507186fe11 | docs/data/mapped_ingredients.csv; CSV lines=[291] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:34118","line":291,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:34118","preferred_term":"1-octen-3-ol","total_occurrences":"0"}] |
| ev-c31c954de57e5eb9 | reports/yaml_record_review/1-octen-3-ol.md; &#96;data/ingredients/mapped/1-octen-3-ol.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:52; Completeness:70; Recommended Edits:78 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f433b4163c46371c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[23] | context_only | [{"current_record_sha256":"0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff","finding_id":"SEM:a2737f674626659ffe76","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-1-octen-3-ol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 1-octen-3-ol (data/ingredients/mapped/1-octen-3-ol.yaml)'
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
summary: Per-record structured review for 1-octen-3-ol (data/ingredients/mapped/1-octen-3-ol.yaml,
  record-86418cebca163e89, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/1-octen-3-ol.yaml
    sha256: 0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff
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
  - path: reports/yaml_record_review/1-octen-3-ol.md
    sha256: 5d4dab898996ba5e01c128f7d2949dc16a6969bf7f42a240ad10c71ffeedd760
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-86418cebca163e89
  path: data/ingredients/mapped/1-octen-3-ol.yaml
  label: 1-octen-3-ol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-octen-3-ol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/1-octen-3-ol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/1-octen-3-ol.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-86418cebca163e89
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-86418cebca163e89
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-86418cebca163e89
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-86418cebca163e89
evidence:
- evidence_id: ev-52fe4a2e31c71b04
  kind: record_content
  reference: data/ingredients/mapped/1-octen-3-ol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[289],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:34118","line":291,"mapping_status":"MAPPED","ontology_id":"CHEBI:34118","preferred_term":"1-octen-3-ol"}],"identifier":"CHEBI:34118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:34118","ontology_label":"oct-1-en-3-ol","ontology_source":"CHEBI"},"preferred_term":"1-octen-3-ol","sssom_rows":[{"data_row":26,"object_id":"CHEBI:34118","object_label":"oct-1-en-3-ol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-octen-3-ol","synonym_count":0}'
  snapshot_sha256: 0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff
- evidence_id: ev-93922ed2417602e1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [289]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1e58fcdf2ca69b60
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:1-octen-3-ol; data-row positions=[26]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":26,"object_id":"CHEBI:34118","object_label":"oct-1-en-3-ol","other":"CAS:3391-86-4","predicate_id":"skos:exactMatch","subject_id":"MIM:1-octen-3-ol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-260d2a507186fe11
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[291]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:34118","line":291,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:34118","preferred_term":"1-octen-3-ol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c31c954de57e5eb9
  kind: prior_review
  reference: reports/yaml_record_review/1-octen-3-ol.md
  locator: '`data/ingredients/mapped/1-octen-3-ol.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:52; Completeness:70; Recommended Edits:78'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5d4dab898996ba5e01c128f7d2949dc16a6969bf7f42a240ad10c71ffeedd760
  quote: "Recommended Edits:\n1. Remove or replace `kgscan-ca9d598a165f` with a claim-attached,\n\
    \   1-octen-3-ol-specific discussion if an actual unresolved gap remains.\n2.\
    \ If `mappings/record_research_validation.tsv` is meant to be live, regenerate\n\
    \   it or mark the optional/stale 1-octen-3-ol row resolved.\n3. No ChEBI, CAS\
    \ RN, formula, SMILES, InChI, SSSOM, aggregate, or docs edit is\n   needed for\
    \ the active identity."
- evidence_id: ev-f433b4163c46371c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[23]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff","finding_id":"SEM:a2737f674626659ffe76","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9705514d3415b177
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-86418cebca163e89
  evidence_ids:
  - ev-52fe4a2e31c71b04
  - ev-93922ed2417602e1
  - ev-1e58fcdf2ca69b60
  - ev-260d2a507186fe11
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-aa37eafc148cfa5e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-86418cebca163e89
  evidence_ids:
  - ev-c31c954de57e5eb9
  - ev-52fe4a2e31c71b04
  - ev-f433b4163c46371c
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:15:41Z;
    reviewed SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff;
    current SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff;
    hash_changed=False. Reports=["reports/yaml_record_review/1-octen-3-ol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CAS-grounded
    CHEBI identity passes, but the open kgscan discussion is irrelevant and unattached.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c31c954de57e5eb9
    - ev-52fe4a2e31c71b04
  - name: legacy-native-ids
    value: '["SEM:a2737f674626659ffe76"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-52fe4a2e31c71b04
    - ev-c31c954de57e5eb9
    - ev-f433b4163c46371c
findings:
- finding_id: rec-f-2f7a117f017a61a3
  issue_key: mim-reconciliation-historical-review-coverage-and-r-86418cebca163e89
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 1-octen-3-ol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:15:41Z;
    reviewed SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff;
    current SHA-256=0b48ef0d1a3762aaff60b09ab6b7719bef6279fe0fd60e87688189daad4395ff;
    hash_changed=False. Reports=["reports/yaml_record_review/1-octen-3-ol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CAS-grounded
    CHEBI identity passes, but the open kgscan discussion is irrelevant and unattached.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-86418cebca163e89
  evidence_ids:
  - ev-c31c954de57e5eb9
  - ev-52fe4a2e31c71b04
  - ev-f433b4163c46371c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-octen-3-ol.yaml
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
