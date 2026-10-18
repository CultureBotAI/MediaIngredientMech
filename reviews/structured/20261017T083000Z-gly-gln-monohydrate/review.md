# Per-record structured review: Gly-Gln_Monohydrate (data/ingredients/mapped/Gly-Gln_Monohydrate.yaml)

- Review: 20261017T083000Z-gly-gln-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Gly-Gln_Monohydrate (data/ingredients/mapped/Gly-Gln_Monohydrate.yaml, record-2ae40dd704186a80, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Gly-Gln_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Gly-Gln_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2ae40dd704186a80 | data/ingredients/mapped/Gly-Gln_Monohydrate.yaml | maintained | Gly-Gln_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2ae40dd704186a80 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2ae40dd704186a80 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2ae40dd704186a80 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2ae40dd704186a80.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2ae40dd704186a80.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z; reviewed SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37; current SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37; hash_changed=False. Reports=["reports/yaml_record_review/Gly-Gln_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The hydrate close match and CAS registry row pass, but final SSSOM exports an anhydrous parent synonym in other.

## Findings

### rec-f-dd208d65941cc9bf: Historical review coverage and residual narrative: Gly-Gln_Monohydrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2ae40dd704186a80.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z; reviewed SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37; current SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37; hash_changed=False. Reports=["reports/yaml_record_review/Gly-Gln_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The hydrate close match and CAS registry row pass, but final SSSOM exports an anhydrous parent synonym in other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cba3bb9c142381be | data/ingredients/mapped/Gly-Gln_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1067],"raw_equal":true},"docs_rows":[{"identifier":"cas:172669-64-6","line":1069,"mapping_status":"MAPPED","ontology_id":"CHEBI:73898","preferred_term":"Gly-Gln monohydrate"}],"identifier":"cas:172669-64-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:73898","ontology_label":"Gly-Gln","ontology_source":"CHEBI"},"preferred_term":"Gly-Gln monohydrate","sssom_rows":[{"data_row":1330,"object_id":"CHEBI:73898","object_label":"Gly-Gln","predicate_id":"skos:closeMatch"},{"data_row":1331,"object_id":"cas:172669-64-6","object_label":"Gly-Gln monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gly-Gln_Monohydrate","synonym_count":1} |
| ev-8f5fe82cb436c6f2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1067] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b53933ee4e1891c7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Gly-Gln_Monohydrate; data-row positions=[1330,1331] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1330,"object_id":"CHEBI:73898","object_label":"Gly-Gln","other":"glycyl-L-glutamine&#124;CAS:172669-64-6","predicate_id":"skos:closeMatch","subject_id":"MIM:Gly-Gln_Monohydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":1331,"object_id":"cas:172669-64-6","object_label":"Gly-Gln monohydrate","other":"CAS:172669-64-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Gly-Gln_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-7c5f02aa6237dc6a | docs/data/mapped_ingredients.csv; CSV lines=[1069] | supports | Published identity and count rows inspected: [{"identifier":"cas:172669-64-6","line":1069,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73898","preferred_term":"Gly-Gln monohydrate","total_occurrences":"0"}] |
| ev-8f8e246c9ab3b38d | reports/yaml_record_review/Gly-Gln_Monohydrate.md; &#96;data/ingredients/mapped/Gly-Gln_Monohydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:34; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5a7130cda2d0ec26 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[685] | context_only | [{"current_record_sha256":"96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37","finding_id":"SEM:d64365761a05794cee17","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-gly-gln-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Gly-Gln_Monohydrate (data/ingredients/mapped/Gly-Gln_Monohydrate.yaml)'
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
summary: Per-record structured review for Gly-Gln_Monohydrate (data/ingredients/mapped/Gly-Gln_Monohydrate.yaml,
  record-2ae40dd704186a80, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
    sha256: 96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37
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
  - path: reports/yaml_record_review/Gly-Gln_Monohydrate.md
    sha256: e4fcc42ab1cb3024d6c7cd6adc7be5c11597ede7aa3d90ed07697a9309461354
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2ae40dd704186a80
  path: data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
  label: Gly-Gln_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Gly-Gln_Monohydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2ae40dd704186a80
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2ae40dd704186a80
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2ae40dd704186a80
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2ae40dd704186a80
evidence:
- evidence_id: ev-cba3bb9c142381be
  kind: record_content
  reference: data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1067],"raw_equal":true},"docs_rows":[{"identifier":"cas:172669-64-6","line":1069,"mapping_status":"MAPPED","ontology_id":"CHEBI:73898","preferred_term":"Gly-Gln
    monohydrate"}],"identifier":"cas:172669-64-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:73898","ontology_label":"Gly-Gln","ontology_source":"CHEBI"},"preferred_term":"Gly-Gln
    monohydrate","sssom_rows":[{"data_row":1330,"object_id":"CHEBI:73898","object_label":"Gly-Gln","predicate_id":"skos:closeMatch"},{"data_row":1331,"object_id":"cas:172669-64-6","object_label":"Gly-Gln
    monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gly-Gln_Monohydrate","synonym_count":1}'
  snapshot_sha256: 96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37
- evidence_id: ev-8f5fe82cb436c6f2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1067]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b53933ee4e1891c7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Gly-Gln_Monohydrate; data-row positions=[1330,1331]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1330,"object_id":"CHEBI:73898","object_label":"Gly-Gln","other":"glycyl-L-glutamine|CAS:172669-64-6","predicate_id":"skos:closeMatch","subject_id":"MIM:Gly-Gln_Monohydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":1331,"object_id":"cas:172669-64-6","object_label":"Gly-Gln
    monohydrate","other":"CAS:172669-64-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Gly-Gln_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7c5f02aa6237dc6a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1069]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:172669-64-6","line":1069,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73898","preferred_term":"Gly-Gln
    monohydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8f8e246c9ab3b38d
  kind: prior_review
  reference: reports/yaml_record_review/Gly-Gln_Monohydrate.md
  locator: '`data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:34; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e4fcc42ab1cb3024d6c7cd6adc7be5c11597ede7aa3d90ed07697a9309461354
  quote: "Recommended Edits:\n- Major: remove `glycyl-L-glutamine` from the active\
    \ exact-synonym set in\n  `data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`;\
    \ keep it only as parent\n  evidence if needed.\n- Major: rebuild the final SSSOM\
    \ so the close-match row to `CHEBI:73898` no\n  longer publishes the anhydrous\
    \ parent synonym in `other`."
- evidence_id: ev-5a7130cda2d0ec26
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[685]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37","finding_id":"SEM:d64365761a05794cee17","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a6feeecfec47bff9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2ae40dd704186a80
  evidence_ids:
  - ev-cba3bb9c142381be
  - ev-8f5fe82cb436c6f2
  - ev-b53933ee4e1891c7
  - ev-7c5f02aa6237dc6a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9820d3949568bf4f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2ae40dd704186a80
  evidence_ids:
  - ev-8f8e246c9ab3b38d
  - ev-cba3bb9c142381be
  - ev-5a7130cda2d0ec26
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z;
    reviewed SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37;
    current SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37;
    hash_changed=False. Reports=["reports/yaml_record_review/Gly-Gln_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The hydrate
    close match and CAS registry row pass, but final SSSOM exports an anhydrous parent
    synonym in other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8f8e246c9ab3b38d
    - ev-cba3bb9c142381be
  - name: legacy-native-ids
    value: '["SEM:d64365761a05794cee17"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cba3bb9c142381be
    - ev-8f8e246c9ab3b38d
    - ev-5a7130cda2d0ec26
findings:
- finding_id: rec-f-dd208d65941cc9bf
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2ae40dd704186a80
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Gly-Gln_Monohydrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z;
    reviewed SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37;
    current SHA-256=96cc72b44792c1cf088d54e37e12da512b40f2ab82291068362a91c4e1572c37;
    hash_changed=False. Reports=["reports/yaml_record_review/Gly-Gln_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The hydrate
    close match and CAS registry row pass, but final SSSOM exports an anhydrous parent
    synonym in other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2ae40dd704186a80
  evidence_ids:
  - ev-8f8e246c9ab3b38d
  - ev-cba3bb9c142381be
  - ev-5a7130cda2d0ec26
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gly-Gln_Monohydrate.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
