# Per-record structured review: Octanol (data/ingredients/mapped/Octanol.yaml)

- Review: 20261017T083000Z-octanol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Octanol (data/ingredients/mapped/Octanol.yaml, record-13b93fbb72b71ab4, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Octanol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Octanol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-13b93fbb72b71ab4 | data/ingredients/mapped/Octanol.yaml | maintained | Octanol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-13b93fbb72b71ab4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-13b93fbb72b71ab4 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-13b93fbb72b71ab4 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-13b93fbb72b71ab4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-13b93fbb72b71ab4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:31:15Z; reviewed SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d; current SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d; hash_changed=False. Reports=["reports/yaml_record_review/Octanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-specific 1-octanol record exact-maps to generic CHEBI:37868 octanol.

## Findings

### rec-f-2f2c81d055292f0e: Historical review coverage and residual narrative: Octanol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-13b93fbb72b71ab4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:31:15Z; reviewed SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d; current SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d; hash_changed=False. Reports=["reports/yaml_record_review/Octanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-specific 1-octanol record exact-maps to generic CHEBI:37868 octanol.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dabd5f33600510c9 | data/ingredients/mapped/Octanol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1590],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37868","line":1592,"mapping_status":"MAPPED","ontology_id":"CHEBI:37868","preferred_term":"octanol"}],"identifier":"CHEBI:37868","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37868","ontology_label":"octanol","ontology_source":"CHEBI"},"preferred_term":"octanol","sssom_rows":[{"data_row":2138,"object_id":"CHEBI:37868","object_label":"octanol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Octanol","synonym_count":0} |
| ev-7ea9c171ca8c111f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1590] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-93268aa6ae3c75f4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Octanol; data-row positions=[2138] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2138,"object_id":"CHEBI:37868","object_label":"octanol","other":"CAS:111-87-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Octanol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-c8e0ab1a161582eb | docs/data/mapped_ingredients.csv; CSV lines=[1592] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:37868","line":1592,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37868","preferred_term":"octanol","total_occurrences":"0"}] |
| ev-b5dda580396eb8e3 | reports/yaml_record_review/Octanol.md; &#96;data/ingredients/mapped/Octanol.yaml&#96;:2; Verdict:4; Identity:10; Validation:18; Evidence:25; Completeness:39; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-379cca64946e6c9e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1078] | context_only | [{"current_record_sha256":"1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d","finding_id":"SEM:c7cdeee80c86c47a33b7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-octanol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Octanol (data/ingredients/mapped/Octanol.yaml)'
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
summary: Per-record structured review for Octanol (data/ingredients/mapped/Octanol.yaml,
  record-13b93fbb72b71ab4, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Octanol.yaml
    sha256: 1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Octanol.md
    sha256: 5f947be3b7ba7c027c79818d838faf98b38627ea068f49cd756c5cb8da4954dc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-13b93fbb72b71ab4
  path: data/ingredients/mapped/Octanol.yaml
  label: Octanol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Octanol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Octanol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Octanol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-13b93fbb72b71ab4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-13b93fbb72b71ab4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-13b93fbb72b71ab4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-13b93fbb72b71ab4
evidence:
- evidence_id: ev-dabd5f33600510c9
  kind: record_content
  reference: data/ingredients/mapped/Octanol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1590],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37868","line":1592,"mapping_status":"MAPPED","ontology_id":"CHEBI:37868","preferred_term":"octanol"}],"identifier":"CHEBI:37868","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37868","ontology_label":"octanol","ontology_source":"CHEBI"},"preferred_term":"octanol","sssom_rows":[{"data_row":2138,"object_id":"CHEBI:37868","object_label":"octanol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Octanol","synonym_count":0}'
  snapshot_sha256: 1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d
- evidence_id: ev-7ea9c171ca8c111f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1590]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-93268aa6ae3c75f4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Octanol; data-row positions=[2138]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2138,"object_id":"CHEBI:37868","object_label":"octanol","other":"CAS:111-87-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Octanol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c8e0ab1a161582eb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1592]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:37868","line":1592,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37868","preferred_term":"octanol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b5dda580396eb8e3
  kind: prior_review
  reference: reports/yaml_record_review/Octanol.md
  locator: '`data/ingredients/mapped/Octanol.yaml`:2; Verdict:4; Identity:10; Validation:18;
    Evidence:25; Completeness:39; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5f947be3b7ba7c027c79818d838faf98b38627ea068f49cd756c5cb8da4954dc
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Octanol.yaml`, verify\
    \ the source CAS\n  `111-87-5` and re-ground the record to the form-specific `CHEBI:16188`\n\
    \  `octan-1-ol` if the CultureBotHT source row was CAS-specific.\n- Populate InChI\
    \ and SMILES from the selected form-specific ChEBI term.\n- Sync the aggregate\
    \ record, regenerate the final SSSOM, and rerun strict\n  validation, `validate_sssom_invariants.py`,\
    \ and\n  `validate_id_label_correspondence.py`."
- evidence_id: ev-379cca64946e6c9e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1078]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d","finding_id":"SEM:c7cdeee80c86c47a33b7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-71eea13c9c3d865a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-13b93fbb72b71ab4
  evidence_ids:
  - ev-dabd5f33600510c9
  - ev-7ea9c171ca8c111f
  - ev-93268aa6ae3c75f4
  - ev-c8e0ab1a161582eb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-609b178a776b0388
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-13b93fbb72b71ab4
  evidence_ids:
  - ev-b5dda580396eb8e3
  - ev-dabd5f33600510c9
  - ev-379cca64946e6c9e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:31:15Z;
    reviewed SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d;
    current SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d;
    hash_changed=False. Reports=["reports/yaml_record_review/Octanol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-specific 1-octanol
    record exact-maps to generic CHEBI:37868 octanol.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b5dda580396eb8e3
    - ev-dabd5f33600510c9
  - name: legacy-native-ids
    value: '["SEM:c7cdeee80c86c47a33b7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dabd5f33600510c9
    - ev-b5dda580396eb8e3
    - ev-379cca64946e6c9e
findings:
- finding_id: rec-f-2f2c81d055292f0e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-13b93fbb72b71ab4
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Octanol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:31:15Z;
    reviewed SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d;
    current SHA-256=1ffe039938831e874b499d7c62101b0fef5e35313b6e9cebc06723f3d4c1ad4d;
    hash_changed=False. Reports=["reports/yaml_record_review/Octanol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-specific 1-octanol
    record exact-maps to generic CHEBI:37868 octanol.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-13b93fbb72b71ab4
  evidence_ids:
  - ev-b5dda580396eb8e3
  - ev-dabd5f33600510c9
  - ev-379cca64946e6c9e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Octanol.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
