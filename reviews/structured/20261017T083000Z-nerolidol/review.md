# Per-record structured review: Nerolidol (data/ingredients/mapped/Nerolidol.yaml)

- Review: 20261017T083000Z-nerolidol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nerolidol (data/ingredients/mapped/Nerolidol.yaml, record-ab8f9aa35d71f9cd, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nerolidol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nerolidol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ab8f9aa35d71f9cd | data/ingredients/mapped/Nerolidol.yaml | maintained | Nerolidol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ab8f9aa35d71f9cd | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-ab8f9aa35d71f9cd | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ab8f9aa35d71f9cd | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ab8f9aa35d71f9cd.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ab8f9aa35d71f9cd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z; reviewed SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb; current SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb; hash_changed=False. Reports=["reports/yaml_record_review/Nerolidol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI:7524 nerolidol identity passes, but stored CAS 7212-44-4 resolves to a stereospecific PubChem structure.

## Findings

### rec-f-d5fadc572431bc00: Historical review coverage and residual narrative: Nerolidol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-ab8f9aa35d71f9cd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z; reviewed SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb; current SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb; hash_changed=False. Reports=["reports/yaml_record_review/Nerolidol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI:7524 nerolidol identity passes, but stored CAS 7212-44-4 resolves to a stereospecific PubChem structure.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-698448a63c18526c | data/ingredients/mapped/Nerolidol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1542],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7524","line":1544,"mapping_status":"MAPPED","ontology_id":"CHEBI:7524","preferred_term":"Nerolidol"}],"identifier":"CHEBI:7524","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:7524","ontology_label":"nerolidol","ontology_source":"CHEBI"},"preferred_term":"Nerolidol","sssom_rows":[{"data_row":2059,"object_id":"CHEBI:7524","object_label":"nerolidol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nerolidol","synonym_count":1} |
| ev-164a3d83d9b36d15 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1542] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4fa622d1dd59ae95 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nerolidol; data-row positions=[2059] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2059,"object_id":"CHEBI:7524","object_label":"nerolidol","other":"3,7,11-trimethyldodeca-1,6,10-trien-3-ol&#124;CAS:7212-44-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Nerolidol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-ca91ac7aa300eca2 | docs/data/mapped_ingredients.csv; CSV lines=[1544] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:7524","line":1544,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:7524","preferred_term":"Nerolidol","total_occurrences":"0"}] |
| ev-e2287190de64ae13 | reports/yaml_record_review/Nerolidol.md; &#96;data/ingredients/mapped/Nerolidol.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:26; Completeness:41; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-409c46dbd9a05803 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1039] | context_only | [{"current_record_sha256":"d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb","finding_id":"SEM:a04fefe906257f4f1a6d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nerolidol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nerolidol (data/ingredients/mapped/Nerolidol.yaml)'
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
summary: Per-record structured review for Nerolidol (data/ingredients/mapped/Nerolidol.yaml,
  record-ab8f9aa35d71f9cd, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nerolidol.yaml
    sha256: d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb
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
  - path: reports/yaml_record_review/Nerolidol.md
    sha256: 67e204b5eb2d465ea47abc11755dd30b3f9bf96fbe8d0c91a242cc1a0f31994c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ab8f9aa35d71f9cd
  path: data/ingredients/mapped/Nerolidol.yaml
  label: Nerolidol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nerolidol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nerolidol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nerolidol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ab8f9aa35d71f9cd
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ab8f9aa35d71f9cd
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-ab8f9aa35d71f9cd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ab8f9aa35d71f9cd
evidence:
- evidence_id: ev-698448a63c18526c
  kind: record_content
  reference: data/ingredients/mapped/Nerolidol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1542],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:7524","line":1544,"mapping_status":"MAPPED","ontology_id":"CHEBI:7524","preferred_term":"Nerolidol"}],"identifier":"CHEBI:7524","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:7524","ontology_label":"nerolidol","ontology_source":"CHEBI"},"preferred_term":"Nerolidol","sssom_rows":[{"data_row":2059,"object_id":"CHEBI:7524","object_label":"nerolidol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nerolidol","synonym_count":1}'
  snapshot_sha256: d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb
- evidence_id: ev-164a3d83d9b36d15
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1542]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4fa622d1dd59ae95
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nerolidol; data-row positions=[2059]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2059,"object_id":"CHEBI:7524","object_label":"nerolidol","other":"3,7,11-trimethyldodeca-1,6,10-trien-3-ol|CAS:7212-44-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Nerolidol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ca91ac7aa300eca2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1544]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:7524","line":1544,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:7524","preferred_term":"Nerolidol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e2287190de64ae13
  kind: prior_review
  reference: reports/yaml_record_review/Nerolidol.md
  locator: '`data/ingredients/mapped/Nerolidol.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:26; Completeness:41; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 67e204b5eb2d465ea47abc11755dd30b3f9bf96fbe8d0c91a242cc1a0f31994c
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nerolidol.yaml`,\
    \ review CAS\n  `7212-44-4` against the source row and either reject/delete it\
    \ from the\n  generic `CHEBI:7524` record or remap the source to a specific supported\n\
    \  nerolidol isomer before rebuilding final SSSOM."
- evidence_id: ev-409c46dbd9a05803
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1039]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb","finding_id":"SEM:a04fefe906257f4f1a6d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6f0d42fbdc58e006
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ab8f9aa35d71f9cd
  evidence_ids:
  - ev-698448a63c18526c
  - ev-164a3d83d9b36d15
  - ev-4fa622d1dd59ae95
  - ev-ca91ac7aa300eca2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0961c5349224bb2d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ab8f9aa35d71f9cd
  evidence_ids:
  - ev-e2287190de64ae13
  - ev-698448a63c18526c
  - ev-409c46dbd9a05803
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z;
    reviewed SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb;
    current SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb;
    hash_changed=False. Reports=["reports/yaml_record_review/Nerolidol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The generic CHEBI:7524
    nerolidol identity passes, but stored CAS 7212-44-4 resolves to a stereospecific
    PubChem structure.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e2287190de64ae13
    - ev-698448a63c18526c
  - name: legacy-native-ids
    value: '["SEM:a04fefe906257f4f1a6d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-698448a63c18526c
    - ev-e2287190de64ae13
    - ev-409c46dbd9a05803
findings:
- finding_id: rec-f-d5fadc572431bc00
  issue_key: mim-reconciliation-historical-review-coverage-and-r-ab8f9aa35d71f9cd
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nerolidol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:17:19Z;
    reviewed SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb;
    current SHA-256=d452733fc21ad7ff3e8df8092eaaf309bef00934237d761cc4a2b7d8bdf491fb;
    hash_changed=False. Reports=["reports/yaml_record_review/Nerolidol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The generic CHEBI:7524
    nerolidol identity passes, but stored CAS 7212-44-4 resolves to a stereospecific
    PubChem structure.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ab8f9aa35d71f9cd
  evidence_ids:
  - ev-e2287190de64ae13
  - ev-698448a63c18526c
  - ev-409c46dbd9a05803
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nerolidol.yaml
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
