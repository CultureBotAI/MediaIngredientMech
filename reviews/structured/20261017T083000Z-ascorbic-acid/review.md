# Per-record structured review: Ascorbic_Acid (data/ingredients/mapped/Ascorbic_Acid.yaml)

- Review: 20261017T083000Z-ascorbic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ascorbic_Acid (data/ingredients/mapped/Ascorbic_Acid.yaml, record-dc2f661688317689, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ascorbic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ascorbic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dc2f661688317689 | data/ingredients/mapped/Ascorbic_Acid.yaml | maintained | Ascorbic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dc2f661688317689 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-dc2f661688317689 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dc2f661688317689 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dc2f661688317689.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dc2f661688317689.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:51:40Z; reviewed SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf; current SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf; hash_changed=False. Reports=["reports/yaml_record_review/Ascorbic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The record mixes generic CHEBI ascorbic acid with the L-ascorbic-acid CAS and still carries role/property strings as synonyms.

## Findings

### rec-f-cfb45396aa550413: Historical review coverage and residual narrative: Ascorbic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-dc2f661688317689.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:51:40Z; reviewed SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf; current SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf; hash_changed=False. Reports=["reports/yaml_record_review/Ascorbic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The record mixes generic CHEBI ascorbic acid with the L-ascorbic-acid CAS and still carries role/property strings as synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a1f195d70e655893 | data/ingredients/mapped/Ascorbic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[521],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:22652","line":523,"mapping_status":"MAPPED","ontology_id":"CHEBI:22652","preferred_term":"Ascorbic acid"}],"identifier":"CHEBI:22652","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":65,"edge_count":65,"occurrences":65},"occurrence_statistics":{"media_count":65,"total_occurrences":65},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:22652","ontology_label":"ascorbic acid","ontology_source":"CHEBI"},"preferred_term":"Ascorbic acid","sssom_rows":[{"data_row":438,"object_id":"CHEBI:22652","object_label":"ascorbic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ascorbic_Acid","synonym_count":6} |
| ev-915b969ab0ed25b1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [521] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2732b86e55004519 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ascorbic_Acid; data-row positions=[438] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":438,"object_id":"CHEBI:22652","object_label":"ascorbic acid","other":"Ascorbic acid (Sigma)&#124;CAS:50-81-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ascorbic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-aa1a973812e13876 | docs/data/mapped_ingredients.csv; CSV lines=[523] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:22652","line":523,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"65","ontology_id":"CHEBI:22652","preferred_term":"Ascorbic acid","total_occurrences":"65"}] |
| ev-f55a83a3e2c300d9 | reports/yaml_record_review/Ascorbic_Acid.md; &#96;data/ingredients/mapped/Ascorbic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:28; Evidence:51; Completeness:67; Recommended Edits:77 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c22f04e4494f7953 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[280] | context_only | [{"current_record_sha256":"0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf","finding_id":"SEM:044cd3f18a112afe4253","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ascorbic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ascorbic_Acid (data/ingredients/mapped/Ascorbic_Acid.yaml)'
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
summary: Per-record structured review for Ascorbic_Acid (data/ingredients/mapped/Ascorbic_Acid.yaml,
  record-dc2f661688317689, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ascorbic_Acid.yaml
    sha256: 0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf
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
  - path: reports/yaml_record_review/Ascorbic_Acid.md
    sha256: bef880e362a3215262ef9831cba59973261a99fd662776ef63859b54119ff69d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dc2f661688317689
  path: data/ingredients/mapped/Ascorbic_Acid.yaml
  label: Ascorbic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ascorbic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ascorbic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ascorbic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dc2f661688317689
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dc2f661688317689
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-dc2f661688317689
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dc2f661688317689
evidence:
- evidence_id: ev-a1f195d70e655893
  kind: record_content
  reference: data/ingredients/mapped/Ascorbic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[521],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:22652","line":523,"mapping_status":"MAPPED","ontology_id":"CHEBI:22652","preferred_term":"Ascorbic
    acid"}],"identifier":"CHEBI:22652","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":65,"edge_count":65,"occurrences":65},"occurrence_statistics":{"media_count":65,"total_occurrences":65},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:22652","ontology_label":"ascorbic
    acid","ontology_source":"CHEBI"},"preferred_term":"Ascorbic acid","sssom_rows":[{"data_row":438,"object_id":"CHEBI:22652","object_label":"ascorbic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ascorbic_Acid","synonym_count":6}'
  snapshot_sha256: 0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf
- evidence_id: ev-915b969ab0ed25b1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [521]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2732b86e55004519
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ascorbic_Acid; data-row positions=[438]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":438,"object_id":"CHEBI:22652","object_label":"ascorbic
    acid","other":"Ascorbic acid (Sigma)|CAS:50-81-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ascorbic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-aa1a973812e13876
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[523]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:22652","line":523,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"65","ontology_id":"CHEBI:22652","preferred_term":"Ascorbic
    acid","total_occurrences":"65"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f55a83a3e2c300d9
  kind: prior_review
  reference: reports/yaml_record_review/Ascorbic_Acid.md
  locator: '`data/ingredients/mapped/Ascorbic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:28; Evidence:51; Completeness:67; Recommended Edits:77'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: bef880e362a3215262ef9831cba59973261a99fd662776ef63859b54119ff69d
  quote: "Recommended Edits:\n- Reground `data/ingredients/mapped/Ascorbic_Acid.yaml`\
    \ from `CHEBI:22652` to\n  the form-specific `CHEBI:29073` when the source label\
    \ and CAS `50-81-7`\n  denote ordinary L-ascorbic acid.\n- Decide whether this\
    \ record should merge with `L-ascorbic_Acid.yaml` or retain\n  a separate source-surface\
    \ record; do not leave two exact records for the same\n  CAS-backed chemical unless\
    \ the duplicate-identifier baseline intentionally\n  tracks that family.\n- Remove\
    \ the five `Role: Vitamin; Properties: ...` strings from `synonyms`.\n- Synchronize\
    \ the aggregate and SSSOM rows, then rerun focused strict and term\n  validation,\
    \ SSSOM invariants, flat-export coverage, and the id/label product\n  check."
- evidence_id: ev-c22f04e4494f7953
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[280]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf","finding_id":"SEM:044cd3f18a112afe4253","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c44f5f6ad04fd70b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dc2f661688317689
  evidence_ids:
  - ev-a1f195d70e655893
  - ev-915b969ab0ed25b1
  - ev-2732b86e55004519
  - ev-aa1a973812e13876
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-87219167ebfd239f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dc2f661688317689
  evidence_ids:
  - ev-f55a83a3e2c300d9
  - ev-a1f195d70e655893
  - ev-c22f04e4494f7953
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:51:40Z;
    reviewed SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf;
    current SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf;
    hash_changed=False. Reports=["reports/yaml_record_review/Ascorbic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The record mixes
    generic CHEBI ascorbic acid with the L-ascorbic-acid CAS and still carries role/property
    strings as synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f55a83a3e2c300d9
    - ev-a1f195d70e655893
  - name: legacy-native-ids
    value: '["SEM:044cd3f18a112afe4253"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a1f195d70e655893
    - ev-f55a83a3e2c300d9
    - ev-c22f04e4494f7953
findings:
- finding_id: rec-f-cfb45396aa550413
  issue_key: mim-reconciliation-historical-review-coverage-and-r-dc2f661688317689
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ascorbic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:51:40Z;
    reviewed SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf;
    current SHA-256=0c75838e9b7ce6c20427ec7c433555d8f1a84fd499aec0c4416385b6e41fe7cf;
    hash_changed=False. Reports=["reports/yaml_record_review/Ascorbic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The record mixes
    generic CHEBI ascorbic acid with the L-ascorbic-acid CAS and still carries role/property
    strings as synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dc2f661688317689
  evidence_ids:
  - ev-f55a83a3e2c300d9
  - ev-a1f195d70e655893
  - ev-c22f04e4494f7953
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ascorbic_Acid.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
