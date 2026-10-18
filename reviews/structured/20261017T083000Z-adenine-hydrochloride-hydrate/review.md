# Per-record structured review: Adenine_Hydrochloride_Hydrate (data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml)

- Review: 20261017T083000Z-adenine-hydrochloride-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Adenine_Hydrochloride_Hydrate (data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml, record-0e14d2a010d295b1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0e14d2a010d295b1 | data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml | maintained | Adenine_Hydrochloride_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0e14d2a010d295b1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-0e14d2a010d295b1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0e14d2a010d295b1 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0e14d2a010d295b1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0e14d2a010d295b1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z; reviewed SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1; current SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1; hash_changed=False. Reports=["reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS registry identity and CHEBI:16708 close match pass, but the hydrate state still needs source support because CAS/PubChem structure lacks a water component.

## Findings

### rec-f-9e33036b39a89e31: Historical review coverage and residual narrative: Adenine_Hydrochloride_Hydrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-0e14d2a010d295b1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z; reviewed SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1; current SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1; hash_changed=False. Reports=["reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS registry identity and CHEBI:16708 close match pass, but the hydrate state still needs source support because CAS/PubChem structure lacks a water component.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a6c798f3129428f6 | data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[454],"raw_equal":true},"docs_rows":[{"identifier":"cas:2922-28-3","line":456,"mapping_status":"MAPPED","ontology_id":"CHEBI:16708","preferred_term":"Adenine hydrochloride hydrate"}],"identifier":"cas:2922-28-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":22,"edge_count":22,"occurrences":22},"occurrence_statistics":{"media_count":22,"total_occurrences":22},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16708","ontology_label":"adenine","ontology_source":"CHEBI"},"preferred_term":"Adenine hydrochloride hydrate","sssom_rows":[{"data_row":303,"object_id":"CHEBI:16708","object_label":"adenine","predicate_id":"skos:closeMatch"},{"data_row":304,"object_id":"cas:2922-28-3","object_label":"Adenine hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Adenine_Hydrochloride_Hydrate","synonym_count":0} |
| ev-23e133a1a88ef03e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [454] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f362e4a372977882 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Adenine_Hydrochloride_Hydrate; data-row positions=[303,304] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":303,"object_id":"CHEBI:16708","object_label":"adenine","other":"CAS:2922-28-3","predicate_id":"skos:closeMatch","subject_id":"MIM:Adenine_Hydrochloride_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":304,"object_id":"cas:2922-28-3","object_label":"Adenine hydrochloride hydrate","other":"CAS:2922-28-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Adenine_Hydrochloride_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-94bcc6782ed9253e | docs/data/mapped_ingredients.csv; CSV lines=[456] | supports | Published identity and count rows inspected: [{"identifier":"cas:2922-28-3","line":456,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"22","ontology_id":"CHEBI:16708","preferred_term":"Adenine hydrochloride hydrate","total_occurrences":"22"}] |
| ev-1c3a85e05c1a7dff | reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md; &#96;data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:41; Completeness:59; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f946ba2db49c02d8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[212] | context_only | [{"current_record_sha256":"2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1","finding_id":"SEM:cddedeffc2f33a2b9cad","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-adenine-hydrochloride-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Adenine_Hydrochloride_Hydrate (data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml)'
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
summary: Per-record structured review for Adenine_Hydrochloride_Hydrate (data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml,
  record-0e14d2a010d295b1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
    sha256: 2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1
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
  - path: reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md
    sha256: 49a7c76478997bcde193b481090fb8c61a7b15bd2c848f4b7a9374b25fd5e881
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0e14d2a010d295b1
  path: data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
  label: Adenine_Hydrochloride_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0e14d2a010d295b1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0e14d2a010d295b1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-0e14d2a010d295b1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0e14d2a010d295b1
evidence:
- evidence_id: ev-a6c798f3129428f6
  kind: record_content
  reference: data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[454],"raw_equal":true},"docs_rows":[{"identifier":"cas:2922-28-3","line":456,"mapping_status":"MAPPED","ontology_id":"CHEBI:16708","preferred_term":"Adenine
    hydrochloride hydrate"}],"identifier":"cas:2922-28-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":22,"edge_count":22,"occurrences":22},"occurrence_statistics":{"media_count":22,"total_occurrences":22},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16708","ontology_label":"adenine","ontology_source":"CHEBI"},"preferred_term":"Adenine
    hydrochloride hydrate","sssom_rows":[{"data_row":303,"object_id":"CHEBI:16708","object_label":"adenine","predicate_id":"skos:closeMatch"},{"data_row":304,"object_id":"cas:2922-28-3","object_label":"Adenine
    hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Adenine_Hydrochloride_Hydrate","synonym_count":0}'
  snapshot_sha256: 2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1
- evidence_id: ev-23e133a1a88ef03e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [454]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f362e4a372977882
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Adenine_Hydrochloride_Hydrate; data-row positions=[303,304]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":303,"object_id":"CHEBI:16708","object_label":"adenine","other":"CAS:2922-28-3","predicate_id":"skos:closeMatch","subject_id":"MIM:Adenine_Hydrochloride_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":304,"object_id":"cas:2922-28-3","object_label":"Adenine
    hydrochloride hydrate","other":"CAS:2922-28-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Adenine_Hydrochloride_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-94bcc6782ed9253e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[456]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:2922-28-3","line":456,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"22","ontology_id":"CHEBI:16708","preferred_term":"Adenine
    hydrochloride hydrate","total_occurrences":"22"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1c3a85e05c1a7dff
  kind: prior_review
  reference: reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md
  locator: '`data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml`:2; Verdict:4;
    Identity:11; Validation:25; Evidence:41; Completeness:59; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 49a7c76478997bcde193b481090fb8c61a7b15bd2c848f4b7a9374b25fd5e881
  quote: "Recommended Edits:\n- Inspect the CultureBotHT or source-media records that\
    \ supplied CAS\n  `2922-28-3`; either confirm the hydrated form and update the\
    \ structure\n  evidence accordingly, or relabel the exact CAS identity if it is\
    \ only adenine\n  hydrochloride.\n- Keep `CHEBI:16708` as a close parent/neighbor\
    \ rather than an exact identity\n  unless ChEBI adds a term for the exact supplied\
    \ form."
- evidence_id: ev-f946ba2db49c02d8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[212]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1","finding_id":"SEM:cddedeffc2f33a2b9cad","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8a1231637eed68fa
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0e14d2a010d295b1
  evidence_ids:
  - ev-a6c798f3129428f6
  - ev-23e133a1a88ef03e
  - ev-f362e4a372977882
  - ev-94bcc6782ed9253e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-493ecf7e185b3157
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0e14d2a010d295b1
  evidence_ids:
  - ev-1c3a85e05c1a7dff
  - ev-a6c798f3129428f6
  - ev-f946ba2db49c02d8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z;
    reviewed SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1;
    current SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1;
    hash_changed=False. Reports=["reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    registry identity and CHEBI:16708 close match pass, but the hydrate state still
    needs source support because CAS/PubChem structure lacks a water component.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1c3a85e05c1a7dff
    - ev-a6c798f3129428f6
  - name: legacy-native-ids
    value: '["SEM:cddedeffc2f33a2b9cad"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a6c798f3129428f6
    - ev-1c3a85e05c1a7dff
    - ev-f946ba2db49c02d8
findings:
- finding_id: rec-f-9e33036b39a89e31
  issue_key: mim-reconciliation-historical-review-coverage-and-r-0e14d2a010d295b1
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Adenine_Hydrochloride_Hydrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z;
    reviewed SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1;
    current SHA-256=2467c25545c1818d60b1822acbcc64ab0b25aef09f99722f2fb140d5296722e1;
    hash_changed=False. Reports=["reports/yaml_record_review/Adenine_Hydrochloride_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    registry identity and CHEBI:16708 close match pass, but the hydrate state still
    needs source support because CAS/PubChem structure lacks a water component.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0e14d2a010d295b1
  evidence_ids:
  - ev-1c3a85e05c1a7dff
  - ev-a6c798f3129428f6
  - ev-f946ba2db49c02d8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml
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
