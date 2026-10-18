# Per-record structured review: Trigonelline (data/ingredients/mapped/Trigonelline.yaml)

- Review: 20261017T083000Z-trigonelline
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trigonelline (data/ingredients/mapped/Trigonelline.yaml, record-d1a31b3fb1c99200, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trigonelline.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trigonelline.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d1a31b3fb1c99200 | data/ingredients/mapped/Trigonelline.yaml | maintained | Trigonelline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d1a31b3fb1c99200 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d1a31b3fb1c99200 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d1a31b3fb1c99200 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d1a31b3fb1c99200.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d1a31b3fb1c99200.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:33:45Z; reviewed SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde; current SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde; hash_changed=False. Reports=["reports/yaml_record_review/Trigonelline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MeSH mapping resolves, but CHEBI now has an exact candidate for review while this chemical remains on the MeSH fallback.

## Findings

### rec-f-9e1a290997ac3cc7: Historical review coverage and residual narrative: Trigonelline

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d1a31b3fb1c99200.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:33:45Z; reviewed SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde; current SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde; hash_changed=False. Reports=["reports/yaml_record_review/Trigonelline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MeSH mapping resolves, but CHEBI now has an exact candidate for review while this chemical remains on the MeSH fallback.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dc9ffd5c40730c68 | data/ingredients/mapped/Trigonelline.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1991],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C009560","line":1993,"mapping_status":"MAPPED","ontology_id":"mesh:C009560","preferred_term":"Trigonelline"}],"identifier":"mesh:C009560","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C009560","ontology_label":"trigonelline","ontology_source":"MESH"},"preferred_term":"Trigonelline","sssom_rows":[{"data_row":2823,"object_id":"mesh:C009560","object_label":"trigonelline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trigonelline","synonym_count":1} |
| ev-e5f97ffd8f0bd6bf | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1991] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-aa95ff152042927d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trigonelline; data-row positions=[2823] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2823,"object_id":"mesh:C009560","object_label":"trigonelline","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Trigonelline","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e3d2ce054c35ce0a | docs/data/mapped_ingredients.csv; CSV lines=[1993] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C009560","line":1993,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C009560","preferred_term":"Trigonelline","total_occurrences":"2"}] |
| ev-59535bd5c805b635 | reports/yaml_record_review/Trigonelline.md; &#96;data/ingredients/mapped/Trigonelline.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:28; Issues:40; Major: exact ChEBI grounding is still unresolved:42; Completeness:50; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8a2cb443d2e7c8ae | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1307] | context_only | [{"current_record_sha256":"11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde","finding_id":"SEM:084c464d8e246d327916","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trigonelline
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trigonelline (data/ingredients/mapped/Trigonelline.yaml)'
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
summary: Per-record structured review for Trigonelline (data/ingredients/mapped/Trigonelline.yaml,
  record-d1a31b3fb1c99200, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trigonelline.yaml
    sha256: 11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Trigonelline.md
    sha256: 5e8003762b4eff8f86f741594b67d8710f4a45bb3dc6c8508f6a3c00fe947bbb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d1a31b3fb1c99200
  path: data/ingredients/mapped/Trigonelline.yaml
  label: Trigonelline
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trigonelline.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trigonelline.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trigonelline.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d1a31b3fb1c99200
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d1a31b3fb1c99200
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d1a31b3fb1c99200
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d1a31b3fb1c99200
evidence:
- evidence_id: ev-dc9ffd5c40730c68
  kind: record_content
  reference: data/ingredients/mapped/Trigonelline.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1991],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C009560","line":1993,"mapping_status":"MAPPED","ontology_id":"mesh:C009560","preferred_term":"Trigonelline"}],"identifier":"mesh:C009560","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C009560","ontology_label":"trigonelline","ontology_source":"MESH"},"preferred_term":"Trigonelline","sssom_rows":[{"data_row":2823,"object_id":"mesh:C009560","object_label":"trigonelline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trigonelline","synonym_count":1}'
  snapshot_sha256: 11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde
- evidence_id: ev-e5f97ffd8f0bd6bf
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1991]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-aa95ff152042927d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trigonelline; data-row positions=[2823]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2823,"object_id":"mesh:C009560","object_label":"trigonelline","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Trigonelline","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e3d2ce054c35ce0a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1993]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C009560","line":1993,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C009560","preferred_term":"Trigonelline","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-59535bd5c805b635
  kind: prior_review
  reference: reports/yaml_record_review/Trigonelline.md
  locator: '`data/ingredients/mapped/Trigonelline.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:28; Issues:40; Major: exact ChEBI grounding is still unresolved:42;
    Completeness:50; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5e8003762b4eff8f86f741594b67d8710f4a45bb3dc6c8508f6a3c00fe947bbb
  quote: "Issues:\n\n\nMajor: exact ChEBI grounding is still unresolved:\nThe record\
    \ was promoted to MeSH on 2026-05-02 because no ChEBI mapping was\navailable at\
    \ that point. ChEBI now exposes `CHEBI:18123` with `Trigonelline` as\na synonym\
    \ for the free betaine, so this chemical should be reviewed against\nthat candidate\
    \ instead of being left on a MeSH fallback with no\n`ingredient_type` or `chemical_properties`.\n\
    \nRecommended Edits:\n- Evaluate `CHEBI:18123` for `Trigonelline`; if exact, remap\
    \ this record from\n  `mesh:C009560` to `CHEBI:18123`, populate the normal\n \
    \ `SINGLE_INGREDIENT`/chemical-property fields, regenerate the aggregate copy\n\
    \  and final SSSOM row, and leave the existing `Trigonelline_HCl` salt record\
    \ on\n  `CHEBI:229203`."
- evidence_id: ev-8a2cb443d2e7c8ae
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1307]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde","finding_id":"SEM:084c464d8e246d327916","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9b5fe383d7abd471
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d1a31b3fb1c99200
  evidence_ids:
  - ev-dc9ffd5c40730c68
  - ev-e5f97ffd8f0bd6bf
  - ev-aa95ff152042927d
  - ev-e3d2ce054c35ce0a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-910b0b314cfc0f6f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1a31b3fb1c99200
  evidence_ids:
  - ev-59535bd5c805b635
  - ev-dc9ffd5c40730c68
  - ev-8a2cb443d2e7c8ae
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:33:45Z;
    reviewed SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde;
    current SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde;
    hash_changed=False. Reports=["reports/yaml_record_review/Trigonelline.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The MeSH mapping
    resolves, but CHEBI now has an exact candidate for review while this chemical
    remains on the MeSH fallback.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-59535bd5c805b635
    - ev-dc9ffd5c40730c68
  - name: legacy-native-ids
    value: '["SEM:084c464d8e246d327916"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dc9ffd5c40730c68
    - ev-59535bd5c805b635
    - ev-8a2cb443d2e7c8ae
findings:
- finding_id: rec-f-9e1a290997ac3cc7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d1a31b3fb1c99200
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Trigonelline'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:33:45Z;
    reviewed SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde;
    current SHA-256=11cb600b9ee471da321d3ae8feedf3b3ed057cd934c4a874fadcbc6ff6360cde;
    hash_changed=False. Reports=["reports/yaml_record_review/Trigonelline.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The MeSH mapping
    resolves, but CHEBI now has an exact candidate for review while this chemical
    remains on the MeSH fallback.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1a31b3fb1c99200
  evidence_ids:
  - ev-59535bd5c805b635
  - ev-dc9ffd5c40730c68
  - ev-8a2cb443d2e7c8ae
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trigonelline.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
