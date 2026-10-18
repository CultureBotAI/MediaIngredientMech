# Per-record structured review: Nigericin_Sodium_Salt (data/ingredients/mapped/Nigericin_Sodium_Salt.yaml)

- Review: 20261017T083000Z-nigericin-sodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nigericin_Sodium_Salt (data/ingredients/mapped/Nigericin_Sodium_Salt.yaml, record-1d4f97b2677ce9f5, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nigericin_Sodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nigericin_Sodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1d4f97b2677ce9f5 | data/ingredients/mapped/Nigericin_Sodium_Salt.yaml | maintained | Nigericin_Sodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1d4f97b2677ce9f5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1d4f97b2677ce9f5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1d4f97b2677ce9f5 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1d4f97b2677ce9f5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1d4f97b2677ce9f5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z; reviewed SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b; current SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b; hash_changed=False. Reports=["reports/yaml_record_review/Nigericin_Sodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The sodium salt identity passes, but current CHEBI:201444 now supports promotion off CAS fallback rows.

## Findings

### rec-f-37bf4ac6a8c2a25a: Historical review coverage and residual narrative: Nigericin_Sodium_Salt

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1d4f97b2677ce9f5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z; reviewed SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b; current SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b; hash_changed=False. Reports=["reports/yaml_record_review/Nigericin_Sodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The sodium salt identity passes, but current CHEBI:201444 now supports promotion off CAS fallback rows.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-69bde55443e460f3 | data/ingredients/mapped/Nigericin_Sodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"cas:28643-80-3","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:201444","preferred_term":"Nigericin sodium salt"}],"identifier":"cas:28643-80-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:201444","ontology_label":"Nigericin sodium","ontology_source":"CHEBI"},"preferred_term":"Nigericin sodium salt","sssom_rows":[{"data_row":2090,"object_id":"CHEBI:201444","object_label":"Nigericin sodium","predicate_id":"skos:broadMatch"},{"data_row":2091,"object_id":"cas:28643-80-3","object_label":"Nigericin sodium salt","predicate_id":"skos:exactMatch"},{"data_row":2092,"object_id":"kgmicrobe.compound:nigericin_sodium_salt","object_label":"Nigericin sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nigericin_Sodium_Salt","synonym_count":1} |
| ev-f1646001d6f9001d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1563] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-44c45d1de5c496a3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nigericin_Sodium_Salt; data-row positions=[2090,2091,2092] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2090,"object_id":"CHEBI:201444","object_label":"Nigericin sodium","other":"sodium;(2R)-2-[(2R,3S,6R)-6-[[(2S,4R,5R,6R,7R,9R)-2-[(2R,5S)-5-[(2R,3S,5R)-5-[(2S,3S,5R,6R)-6-hydroxy-6-(hydroxymethyl)-3,5-dimethyloxan-2-yl]-3-methyloxolan-2-yl]-5-methyloxolan-2-yl]-7-methoxy-2,4,6-trimethyl-1,10-dioxaspiro[4.5]decan-9-yl]methyl]-3-methyloxan-2-yl]propanoate","predicate_id":"skos:broadMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2091,"object_id":"cas:28643-80-3","object_label":"Nigericin sodium salt","other":"CAS:28643-80-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2092,"object_id":"kgmicrobe.compound:nigericin_sodium_salt","object_label":"Nigericin sodium salt","other":"CAS:28643-80-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-df63c74919b6dd34 | docs/data/mapped_ingredients.csv; CSV lines=[1565] | supports | Published identity and count rows inspected: [{"identifier":"cas:28643-80-3","line":1565,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:201444","preferred_term":"Nigericin sodium salt","total_occurrences":"0"}] |
| ev-8f9bddf778016ffe | reports/yaml_record_review/Nigericin_Sodium_Salt.md; &#96;data/ingredients/mapped/Nigericin_Sodium_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:26; Completeness:40; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-18c3fea418120b29 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1060] | context_only | [{"current_record_sha256":"cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b","finding_id":"SEM:f6c46248df0d6b71331f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nigericin-sodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nigericin_Sodium_Salt (data/ingredients/mapped/Nigericin_Sodium_Salt.yaml)'
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
summary: Per-record structured review for Nigericin_Sodium_Salt (data/ingredients/mapped/Nigericin_Sodium_Salt.yaml,
  record-1d4f97b2677ce9f5, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
    sha256: cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b
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
  - path: reports/yaml_record_review/Nigericin_Sodium_Salt.md
    sha256: ef4e0065e3c6158fcf030cf1445dfdfdc423d1c5bb019533bb85340c3eca7abe
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1d4f97b2677ce9f5
  path: data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
  label: Nigericin_Sodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nigericin_Sodium_Salt.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1d4f97b2677ce9f5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1d4f97b2677ce9f5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1d4f97b2677ce9f5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1d4f97b2677ce9f5
evidence:
- evidence_id: ev-69bde55443e460f3
  kind: record_content
  reference: data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"cas:28643-80-3","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:201444","preferred_term":"Nigericin
    sodium salt"}],"identifier":"cas:28643-80-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:201444","ontology_label":"Nigericin
    sodium","ontology_source":"CHEBI"},"preferred_term":"Nigericin sodium salt","sssom_rows":[{"data_row":2090,"object_id":"CHEBI:201444","object_label":"Nigericin
    sodium","predicate_id":"skos:broadMatch"},{"data_row":2091,"object_id":"cas:28643-80-3","object_label":"Nigericin
    sodium salt","predicate_id":"skos:exactMatch"},{"data_row":2092,"object_id":"kgmicrobe.compound:nigericin_sodium_salt","object_label":"Nigericin
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nigericin_Sodium_Salt","synonym_count":1}'
  snapshot_sha256: cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b
- evidence_id: ev-f1646001d6f9001d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1563]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-44c45d1de5c496a3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nigericin_Sodium_Salt; data-row positions=[2090,2091,2092]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2090,"object_id":"CHEBI:201444","object_label":"Nigericin
    sodium","other":"sodium;(2R)-2-[(2R,3S,6R)-6-[[(2S,4R,5R,6R,7R,9R)-2-[(2R,5S)-5-[(2R,3S,5R)-5-[(2S,3S,5R,6R)-6-hydroxy-6-(hydroxymethyl)-3,5-dimethyloxan-2-yl]-3-methyloxolan-2-yl]-5-methyloxolan-2-yl]-7-methoxy-2,4,6-trimethyl-1,10-dioxaspiro[4.5]decan-9-yl]methyl]-3-methyloxan-2-yl]propanoate","predicate_id":"skos:broadMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2091,"object_id":"cas:28643-80-3","object_label":"Nigericin
    sodium salt","other":"CAS:28643-80-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2092,"object_id":"kgmicrobe.compound:nigericin_sodium_salt","object_label":"Nigericin
    sodium salt","other":"CAS:28643-80-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Nigericin_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-df63c74919b6dd34
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1565]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:28643-80-3","line":1565,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:201444","preferred_term":"Nigericin
    sodium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8f9bddf778016ffe
  kind: prior_review
  reference: reports/yaml_record_review/Nigericin_Sodium_Salt.md
  locator: '`data/ingredients/mapped/Nigericin_Sodium_Salt.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:26; Completeness:40; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ef4e0065e3c6158fcf030cf1445dfdfdc423d1c5bb019533bb85340c3eca7abe
  quote: "Recommended Edits:\n- Major: promote `data/ingredients/mapped/Nigericin_Sodium_Salt.yaml`\
    \ from\n  `cas:28643-80-3` to `CHEBI:201444`, change\n  `ontology_mapping.mapping_quality`\
    \ to `EXACT_MATCH`, keep\n  `CAS:28643-80-3` as structured chemistry metadata,\
    \ and rebuild final SSSOM so\n  it emits one exact CHEBI row rather than parent\
    \ plus registry fallback rows."
- evidence_id: ev-18c3fea418120b29
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1060]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b","finding_id":"SEM:f6c46248df0d6b71331f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c38ad7a4efa1dd0f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1d4f97b2677ce9f5
  evidence_ids:
  - ev-69bde55443e460f3
  - ev-f1646001d6f9001d
  - ev-44c45d1de5c496a3
  - ev-df63c74919b6dd34
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-60acb70825a8f94c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1d4f97b2677ce9f5
  evidence_ids:
  - ev-8f9bddf778016ffe
  - ev-69bde55443e460f3
  - ev-18c3fea418120b29
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z;
    reviewed SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b;
    current SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b;
    hash_changed=False. Reports=["reports/yaml_record_review/Nigericin_Sodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The sodium
    salt identity passes, but current CHEBI:201444 now supports promotion off CAS
    fallback rows.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8f9bddf778016ffe
    - ev-69bde55443e460f3
  - name: legacy-native-ids
    value: '["SEM:f6c46248df0d6b71331f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-69bde55443e460f3
    - ev-8f9bddf778016ffe
    - ev-18c3fea418120b29
findings:
- finding_id: rec-f-37bf4ac6a8c2a25a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1d4f97b2677ce9f5
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nigericin_Sodium_Salt'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z;
    reviewed SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b;
    current SHA-256=cd885f64faa4ef865150a0a4b928b526868752a6819faf1584b20e3ef1b8bb0b;
    hash_changed=False. Reports=["reports/yaml_record_review/Nigericin_Sodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The sodium
    salt identity passes, but current CHEBI:201444 now supports promotion off CAS
    fallback rows.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1d4f97b2677ce9f5
  evidence_ids:
  - ev-8f9bddf778016ffe
  - ev-69bde55443e460f3
  - ev-18c3fea418120b29
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nigericin_Sodium_Salt.yaml
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
