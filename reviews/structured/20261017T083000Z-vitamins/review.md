# Per-record structured review: Vitamins (data/ingredients/mapped/Vitamins.yaml)

- Review: 20261017T083000Z-vitamins
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vitamins (data/ingredients/mapped/Vitamins.yaml, record-185ce702c969fd47, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vitamins.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vitamins.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-185ce702c969fd47 | data/ingredients/mapped/Vitamins.yaml | maintained | Vitamins |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-185ce702c969fd47 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-185ce702c969fd47 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-185ce702c969fd47 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-185ce702c969fd47.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-185ce702c969fd47.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:08:16Z; reviewed SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177; current SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177; hash_changed=False. Reports=["reports/yaml_record_review/Vitamins.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The restored CultureMech residual grounding points at a ChEBI role class, and final SSSOM exports the ATCC-qualified surface form.

## Findings

### rec-f-a16323ed7d49747b: Historical review coverage and residual narrative: Vitamins

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-185ce702c969fd47.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:08:16Z; reviewed SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177; current SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177; hash_changed=False. Reports=["reports/yaml_record_review/Vitamins.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The restored CultureMech residual grounding points at a ChEBI role class, and final SSSOM exports the ATCC-qualified surface form.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7d5ced64013e1d55 | data/ingredients/mapped/Vitamins.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2618],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33229","line":2620,"mapping_status":"MAPPED","ontology_id":"CHEBI:33229","preferred_term":"Vitamins"}],"identifier":"CHEBI:33229","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:33229","ontology_label":"vitamin (role)","ontology_source":"CHEBI"},"preferred_term":"Vitamins","sssom_rows":[{"data_row":2913,"object_id":"CHEBI:33229","object_label":"vitamin (role)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamins","synonym_count":1} |
| ev-ce6aafcd2950f737 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2618] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6f3974369574860f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vitamins; data-row positions=[2913] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2913,"object_id":"CHEBI:33229","object_label":"vitamin (role)","other":"Vitamins (ATCC)","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamins","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-9a335af970cf03af | docs/data/mapped_ingredients.csv; CSV lines=[2620] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:33229","line":2620,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:33229","preferred_term":"Vitamins","total_occurrences":"3"}] |
| ev-94ea34bb90da87e7 | reports/yaml_record_review/Vitamins.md; &#96;data/ingredients/mapped/Vitamins.yaml&#96;:2; Verdict:4; Identity:12; Validation:22; Evidence:31; Issues:41; Completeness:50; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b6708879ed8ed485 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1342] | context_only | [{"current_record_sha256":"8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177","finding_id":"SEM:2bd7f38648add739a3c9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vitamins
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vitamins (data/ingredients/mapped/Vitamins.yaml)'
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
summary: Per-record structured review for Vitamins (data/ingredients/mapped/Vitamins.yaml,
  record-185ce702c969fd47, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vitamins.yaml
    sha256: 8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177
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
  - path: reports/yaml_record_review/Vitamins.md
    sha256: f1233144054039167825f916d96032250a98d3504e597540a7bb762eebd2213a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-185ce702c969fd47
  path: data/ingredients/mapped/Vitamins.yaml
  label: Vitamins
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamins.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vitamins.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vitamins.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-185ce702c969fd47
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-185ce702c969fd47
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-185ce702c969fd47
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-185ce702c969fd47
evidence:
- evidence_id: ev-7d5ced64013e1d55
  kind: record_content
  reference: data/ingredients/mapped/Vitamins.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2618],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33229","line":2620,"mapping_status":"MAPPED","ontology_id":"CHEBI:33229","preferred_term":"Vitamins"}],"identifier":"CHEBI:33229","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:33229","ontology_label":"vitamin
    (role)","ontology_source":"CHEBI"},"preferred_term":"Vitamins","sssom_rows":[{"data_row":2913,"object_id":"CHEBI:33229","object_label":"vitamin
    (role)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamins","synonym_count":1}'
  snapshot_sha256: 8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177
- evidence_id: ev-ce6aafcd2950f737
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2618]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6f3974369574860f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vitamins; data-row positions=[2913]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2913,"object_id":"CHEBI:33229","object_label":"vitamin
    (role)","other":"Vitamins (ATCC)","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamins","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9a335af970cf03af
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2620]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:33229","line":2620,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:33229","preferred_term":"Vitamins","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-94ea34bb90da87e7
  kind: prior_review
  reference: reports/yaml_record_review/Vitamins.md
  locator: '`data/ingredients/mapped/Vitamins.yaml`:2; Verdict:4; Identity:12; Validation:22;
    Evidence:31; Issues:41; Completeness:50; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f1233144054039167825f916d96032250a98d3504e597540a7bb762eebd2213a
  quote: "Issues:\n- Major: the media ingredient surface `Vitamins` is asserted as\
    \ an exact match\n  to an abstract role class. A vitamin mixture or unspecified\
    \ vitamin additive\n  should not be identical to the biochemical role played by\
    \ vitamin compounds.\n- Major: the final SSSOM row exports `Vitamins (ATCC)` as\
    \ an exact `other`\n  synonym. That parenthetical names a source or formulation\
    \ context and is not\n  a clean synonym for the ChEBI role.\n\nRecommended Edits:\n\
    - Remap `Vitamins` away from `CHEBI:33229`; preserve any relation to\n  `vitamin\
    \ (role)` as role semantics instead of an exact ingredient identity if\n  that\
    \ relation is still useful.\n- Remove or suppress `Vitamins (ATCC)` from final\
    \ SSSOM `other`.\n- Rebuild SSSOM and rerun strict validation, LinkML term validation,\
    \ SSSOM\n  invariant validation, and the cross-record `other` synonym audit."
- evidence_id: ev-b6708879ed8ed485
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1342]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177","finding_id":"SEM:2bd7f38648add739a3c9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-73fc4060577bb553
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-185ce702c969fd47
  evidence_ids:
  - ev-7d5ced64013e1d55
  - ev-ce6aafcd2950f737
  - ev-6f3974369574860f
  - ev-9a335af970cf03af
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9009461981b492cd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-185ce702c969fd47
  evidence_ids:
  - ev-94ea34bb90da87e7
  - ev-7d5ced64013e1d55
  - ev-b6708879ed8ed485
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:08:16Z;
    reviewed SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177;
    current SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177;
    hash_changed=False. Reports=["reports/yaml_record_review/Vitamins.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The restored CultureMech
    residual grounding points at a ChEBI role class, and final SSSOM exports the ATCC-qualified
    surface form.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-94ea34bb90da87e7
    - ev-7d5ced64013e1d55
  - name: legacy-native-ids
    value: '["SEM:2bd7f38648add739a3c9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7d5ced64013e1d55
    - ev-94ea34bb90da87e7
    - ev-b6708879ed8ed485
findings:
- finding_id: rec-f-a16323ed7d49747b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-185ce702c969fd47
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Vitamins'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:08:16Z;
    reviewed SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177;
    current SHA-256=8876f5e34a6bbc4b074dce44333aaf814593a36eb8fc8b88caf2c049a4c2e177;
    hash_changed=False. Reports=["reports/yaml_record_review/Vitamins.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The restored CultureMech
    residual grounding points at a ChEBI role class, and final SSSOM exports the ATCC-qualified
    surface form.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-185ce702c969fd47
  evidence_ids:
  - ev-94ea34bb90da87e7
  - ev-7d5ced64013e1d55
  - ev-b6708879ed8ed485
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamins.yaml
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
