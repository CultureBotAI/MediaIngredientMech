# Per-record structured review: 1-Pentanol (data/ingredients/mapped/1-Pentanol.yaml)

- Review: 20261017T083000Z-1-pentanol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 1-Pentanol (data/ingredients/mapped/1-Pentanol.yaml, record-1917aa8472892727, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/1-Pentanol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/1-Pentanol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1917aa8472892727 | data/ingredients/mapped/1-Pentanol.yaml | maintained | 1-Pentanol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1917aa8472892727 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1917aa8472892727 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1917aa8472892727 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1917aa8472892727.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1917aa8472892727.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:02:57Z; reviewed SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19; current SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19; hash_changed=False. Reports=["reports/yaml_record_review/1-Pentanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-derived ChEBI identity and exported products pass, but the open kgscan discussion is irrelevant and unattached.

## Findings

### rec-f-085447075e0c16ef: Historical review coverage and residual narrative: 1-Pentanol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1917aa8472892727.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:02:57Z; reviewed SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19; current SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19; hash_changed=False. Reports=["reports/yaml_record_review/1-Pentanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-derived ChEBI identity and exported products pass, but the open kgscan discussion is irrelevant and unattached.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0912785fc1bc14fb | data/ingredients/mapped/1-Pentanol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[284],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:44884","line":286,"mapping_status":"MAPPED","ontology_id":"CHEBI:44884","preferred_term":"1-Pentanol"}],"identifier":"CHEBI:44884","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:44884","ontology_label":"pentan-1-ol","ontology_source":"CHEBI"},"preferred_term":"1-Pentanol","sssom_rows":[{"data_row":12,"object_id":"CHEBI:44884","object_label":"pentan-1-ol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-Pentanol","synonym_count":0} |
| ev-7b98ea59ee754d88 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [284] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False. |
| ev-d9fcfc2ae738206f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:1-Pentanol; data-row positions=[12] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":12,"object_id":"CHEBI:44884","object_label":"pentan-1-ol","other":"CAS:71-41-0","predicate_id":"skos:exactMatch","subject_id":"MIM:1-Pentanol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-ba5d7a43102685e8 | docs/data/mapped_ingredients.csv; CSV lines=[286] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:44884","line":286,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:44884","preferred_term":"1-Pentanol","total_occurrences":"0"}] |
| ev-aa5d1fc09372c430 | reports/yaml_record_review/1-Pentanol.md; &#96;data/ingredients/mapped/1-Pentanol.yaml&#96;:2; Verdict:4; Identity:13; Validation:32; Evidence:55; Completeness:83; Recommended Edits:96 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b46d322351d50c3d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[13] | context_only | [{"current_record_sha256":"d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19","finding_id":"SEM:0e201d7995b5dcc3eb98","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-1-pentanol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 1-Pentanol (data/ingredients/mapped/1-Pentanol.yaml)'
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
summary: Per-record structured review for 1-Pentanol (data/ingredients/mapped/1-Pentanol.yaml,
  record-1917aa8472892727, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/1-Pentanol.yaml
    sha256: d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19
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
  - path: reports/yaml_record_review/1-Pentanol.md
    sha256: fb44af6171bb87a72a0a557e5513f140ec6b74af9d653ea235c470297d58fcac
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1917aa8472892727
  path: data/ingredients/mapped/1-Pentanol.yaml
  label: 1-Pentanol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-Pentanol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/1-Pentanol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/1-Pentanol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1917aa8472892727
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1917aa8472892727
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1917aa8472892727
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1917aa8472892727
evidence:
- evidence_id: ev-0912785fc1bc14fb
  kind: record_content
  reference: data/ingredients/mapped/1-Pentanol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[284],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:44884","line":286,"mapping_status":"MAPPED","ontology_id":"CHEBI:44884","preferred_term":"1-Pentanol"}],"identifier":"CHEBI:44884","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:44884","ontology_label":"pentan-1-ol","ontology_source":"CHEBI"},"preferred_term":"1-Pentanol","sssom_rows":[{"data_row":12,"object_id":"CHEBI:44884","object_label":"pentan-1-ol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-Pentanol","synonym_count":0}'
  snapshot_sha256: d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19
- evidence_id: ev-7b98ea59ee754d88
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [284]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d9fcfc2ae738206f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:1-Pentanol; data-row positions=[12]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":12,"object_id":"CHEBI:44884","object_label":"pentan-1-ol","other":"CAS:71-41-0","predicate_id":"skos:exactMatch","subject_id":"MIM:1-Pentanol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ba5d7a43102685e8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[286]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:44884","line":286,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:44884","preferred_term":"1-Pentanol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aa5d1fc09372c430
  kind: prior_review
  reference: reports/yaml_record_review/1-Pentanol.md
  locator: '`data/ingredients/mapped/1-Pentanol.yaml`:2; Verdict:4; Identity:13; Validation:32;
    Evidence:55; Completeness:83; Recommended Edits:96'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fb44af6171bb87a72a0a557e5513f140ec6b74af9d653ea235c470297d58fcac
  quote: "Recommended Edits:\n1. Remove or replace `kgscan-fedfdc7a75ff` in\n   `data/ingredients/mapped/1-Pentanol.yaml`\
    \ with a 1-pentanol-specific,\n   claim-attached discussion if an actual unresolved\
    \ evidence gap remains.\n2. If `mappings/record_research_validation.tsv` is meant\
    \ to be a live triage\n   queue, regenerate it from its maintained recipe or mark\
    \ the `1-Pentanol`\n   `CURIE_REFUTED` row resolved and downgrade the synonym\
    \ row to optional\n   enrichment.\n3. On a future synonym-enrichment pass, consider\
    \ adding exact ChEBI aliases for\n   `n-pentanol` and `pentan-1-ol`.\n4. No identifier,\
    \ mapping predicate, mapping grade, chemical-property,\n   ingredient-type, component,\
    \ or SSSOM edit is needed for the active\n   `CHEBI:44884` mapping."
- evidence_id: ev-b46d322351d50c3d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[13]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19","finding_id":"SEM:0e201d7995b5dcc3eb98","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-54a950ca0cee868c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1917aa8472892727
  evidence_ids:
  - ev-0912785fc1bc14fb
  - ev-7b98ea59ee754d88
  - ev-d9fcfc2ae738206f
  - ev-ba5d7a43102685e8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-002626f0429de8ac
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1917aa8472892727
  evidence_ids:
  - ev-aa5d1fc09372c430
  - ev-0912785fc1bc14fb
  - ev-b46d322351d50c3d
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:02:57Z;
    reviewed SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19;
    current SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19;
    hash_changed=False. Reports=["reports/yaml_record_review/1-Pentanol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CAS-derived
    ChEBI identity and exported products pass, but the open kgscan discussion is irrelevant
    and unattached.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aa5d1fc09372c430
    - ev-0912785fc1bc14fb
  - name: legacy-native-ids
    value: '["SEM:0e201d7995b5dcc3eb98"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0912785fc1bc14fb
    - ev-aa5d1fc09372c430
    - ev-b46d322351d50c3d
findings:
- finding_id: rec-f-085447075e0c16ef
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1917aa8472892727
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 1-Pentanol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:02:57Z;
    reviewed SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19;
    current SHA-256=d47463e81ebb231c75529caffced6330cdfb1bea8ebc2b517aaaecd12a4e6d19;
    hash_changed=False. Reports=["reports/yaml_record_review/1-Pentanol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CAS-derived
    ChEBI identity and exported products pass, but the open kgscan discussion is irrelevant
    and unattached.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1917aa8472892727
  evidence_ids:
  - ev-aa5d1fc09372c430
  - ev-0912785fc1bc14fb
  - ev-b46d322351d50c3d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-Pentanol.yaml
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
