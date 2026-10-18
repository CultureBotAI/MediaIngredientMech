# Per-record structured review: Levomenthol (data/ingredients/mapped/Levomenthol.yaml)

- Review: 20261017T083000Z-levomenthol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Levomenthol (data/ingredients/mapped/Levomenthol.yaml, record-3ca0f0114503824d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Levomenthol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Levomenthol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3ca0f0114503824d | data/ingredients/mapped/Levomenthol.yaml | maintained | Levomenthol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3ca0f0114503824d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3ca0f0114503824d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3ca0f0114503824d | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3ca0f0114503824d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3ca0f0114503824d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z; reviewed SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50; current SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50; hash_changed=False. Reports=["reports/yaml_record_review/Levomenthol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:15409 identity, CAS value, and PubChem structure pass, but racemic menthol labels are attached to this enantiopure record and exported as final SSSOM synonyms.

## Findings

### rec-f-3f131001eff83c0c: Historical review coverage and residual narrative: Levomenthol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3ca0f0114503824d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z; reviewed SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50; current SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50; hash_changed=False. Reports=["reports/yaml_record_review/Levomenthol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:15409 identity, CAS value, and PubChem structure pass, but racemic menthol labels are attached to this enantiopure record and exported as final SSSOM synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f3e1edcabded5700 | data/ingredients/mapped/Levomenthol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1297],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15409","line":1299,"mapping_status":"MAPPED","ontology_id":"CHEBI:15409","preferred_term":"Levomenthol"}],"identifier":"CHEBI:15409","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15409","ontology_label":"(-)-menthol","ontology_source":"CHEBI"},"preferred_term":"Levomenthol","sssom_rows":[{"data_row":1687,"object_id":"CHEBI:15409","object_label":"(-)-menthol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levomenthol","synonym_count":8} |
| ev-ac4c265cad431a5c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1297] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-42ce3a0c9e50ccf7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Levomenthol; data-row positions=[1687] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1687,"object_id":"CHEBI:15409","object_label":"(-)-menthol","other":"(1R,2S,5R)-5-methyl-2-(propan-2-yl)cyclohexan-1-ol&#124;(+-)-menthol&#124;DL-menthol&#124;rac-(1R,2S,5R)-5-methyl-2-(propan-2-yl)cyclohexan-1-ol&#124;rac-menthol&#124;racementhol&#124;racementholum&#124;racementol&#124;CAS:2216-51-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Levomenthol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-4190408cfdfe32b7 | docs/data/mapped_ingredients.csv; CSV lines=[1299] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15409","line":1299,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15409","preferred_term":"Levomenthol","total_occurrences":"0"}] |
| ev-c06096f60fb29a07 | reports/yaml_record_review/Levomenthol.md; &#96;data/ingredients/mapped/Levomenthol.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5723d49449aa1c4f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[859] | context_only | [{"current_record_sha256":"548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50","finding_id":"SEM:b22c69b5299c297dede2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-levomenthol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Levomenthol (data/ingredients/mapped/Levomenthol.yaml)'
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
summary: Per-record structured review for Levomenthol (data/ingredients/mapped/Levomenthol.yaml,
  record-3ca0f0114503824d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Levomenthol.yaml
    sha256: 548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Levomenthol.md
    sha256: 1fdbe9b2ef31e4ba9190f2c9005527868006e49bbc9630191c6765f4e54b3716
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3ca0f0114503824d
  path: data/ingredients/mapped/Levomenthol.yaml
  label: Levomenthol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levomenthol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Levomenthol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Levomenthol.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3ca0f0114503824d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3ca0f0114503824d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3ca0f0114503824d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3ca0f0114503824d
evidence:
- evidence_id: ev-f3e1edcabded5700
  kind: record_content
  reference: data/ingredients/mapped/Levomenthol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1297],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15409","line":1299,"mapping_status":"MAPPED","ontology_id":"CHEBI:15409","preferred_term":"Levomenthol"}],"identifier":"CHEBI:15409","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15409","ontology_label":"(-)-menthol","ontology_source":"CHEBI"},"preferred_term":"Levomenthol","sssom_rows":[{"data_row":1687,"object_id":"CHEBI:15409","object_label":"(-)-menthol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levomenthol","synonym_count":8}'
  snapshot_sha256: 548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50
- evidence_id: ev-ac4c265cad431a5c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1297]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-42ce3a0c9e50ccf7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Levomenthol; data-row positions=[1687]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1687,"object_id":"CHEBI:15409","object_label":"(-)-menthol","other":"(1R,2S,5R)-5-methyl-2-(propan-2-yl)cyclohexan-1-ol|(+-)-menthol|DL-menthol|rac-(1R,2S,5R)-5-methyl-2-(propan-2-yl)cyclohexan-1-ol|rac-menthol|racementhol|racementholum|racementol|CAS:2216-51-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Levomenthol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4190408cfdfe32b7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1299]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15409","line":1299,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15409","preferred_term":"Levomenthol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c06096f60fb29a07
  kind: prior_review
  reference: reports/yaml_record_review/Levomenthol.md
  locator: '`data/ingredients/mapped/Levomenthol.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1fdbe9b2ef31e4ba9190f2c9005527868006e49bbc9630191c6765f4e54b3716
  quote: "Recommended Edits:\n- Major: remove the racemic `sssom_other_backfill` synonyms\
    \ from\n  `data/ingredients/mapped/Levomenthol.yaml` so only true levomenthol\
    \ synonyms\n  remain on this enantiopure record.\n- If the raw corpus requires\
    \ a racemic menthol subject, create or curate a\n  separate record grounded to\
    \ `CHEBI:76310`; do not preserve racemic labels on\n  `CHEBI:15409`.\n- Sync the\
    \ aggregate copy and regenerate final SSSOM after the YAML changes;\n  rerun strict,\
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-5723d49449aa1c4f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[859]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50","finding_id":"SEM:b22c69b5299c297dede2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2805a72659d30fa0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3ca0f0114503824d
  evidence_ids:
  - ev-f3e1edcabded5700
  - ev-ac4c265cad431a5c
  - ev-42ce3a0c9e50ccf7
  - ev-4190408cfdfe32b7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7cd1edea3f2a7d96
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ca0f0114503824d
  evidence_ids:
  - ev-c06096f60fb29a07
  - ev-f3e1edcabded5700
  - ev-5723d49449aa1c4f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z;
    reviewed SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50;
    current SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50;
    hash_changed=False. Reports=["reports/yaml_record_review/Levomenthol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    CHEBI:15409 identity, CAS value, and PubChem structure pass, but racemic menthol
    labels are attached to this enantiopure record and exported as final SSSOM synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c06096f60fb29a07
    - ev-f3e1edcabded5700
  - name: legacy-native-ids
    value: '["SEM:b22c69b5299c297dede2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f3e1edcabded5700
    - ev-c06096f60fb29a07
    - ev-5723d49449aa1c4f
findings:
- finding_id: rec-f-3f131001eff83c0c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3ca0f0114503824d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Levomenthol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z;
    reviewed SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50;
    current SHA-256=548c7bdc9c9e0363f4d1872d972d918a8f6ff9151555c914b17c258483641d50;
    hash_changed=False. Reports=["reports/yaml_record_review/Levomenthol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    CHEBI:15409 identity, CAS value, and PubChem structure pass, but racemic menthol
    labels are attached to this enantiopure record and exported as final SSSOM synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ca0f0114503824d
  evidence_ids:
  - ev-c06096f60fb29a07
  - ev-f3e1edcabded5700
  - ev-5723d49449aa1c4f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levomenthol.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
