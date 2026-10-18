# Per-record structured review: L-glutamic_Acid (data/ingredients/mapped/L-glutamic_Acid.yaml)

- Review: 20261017T083000Z-l-glutamic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-glutamic_Acid (data/ingredients/mapped/L-glutamic_Acid.yaml, record-cfd9a89c582f6fdd, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-glutamic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-glutamic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-cfd9a89c582f6fdd | data/ingredients/mapped/L-glutamic_Acid.yaml | maintained | L-glutamic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-cfd9a89c582f6fdd | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-cfd9a89c582f6fdd | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-cfd9a89c582f6fdd | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-cfd9a89c582f6fdd.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-cfd9a89c582f6fdd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z; reviewed SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb; current SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb; hash_changed=False. Reports=["reports/yaml_record_review/L-glutamic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16015 identity, CAS value, PubChem structure, nitrogen-source role, occurrence count, and most final synonyms pass, but final SSSOM exports charged L-Glutamate.

## Findings

### rec-f-40c2a229fa4f401a: Historical review coverage and residual narrative: L-glutamic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-cfd9a89c582f6fdd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z; reviewed SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb; current SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb; hash_changed=False. Reports=["reports/yaml_record_review/L-glutamic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16015 identity, CAS value, PubChem structure, nitrogen-source role, occurrence count, and most final synonyms pass, but final SSSOM exports charged L-Glutamate.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-075b5949153dbf0f | data/ingredients/mapped/L-glutamic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1248],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16015","line":1250,"mapping_status":"MAPPED","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic acid"}],"identifier":"CHEBI:16015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":143,"edge_count":143,"occurrences":143},"occurrence_statistics":{"media_count":143,"total_occurrences":143},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16015","ontology_label":"L-glutamic acid","ontology_source":"CHEBI"},"preferred_term":"L-Glutamic acid","sssom_rows":[{"data_row":1616,"object_id":"CHEBI:16015","object_label":"L-glutamic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-glutamic_Acid","synonym_count":13} |
| ev-ceb2ca3b27a2caae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1248] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a2adfdb527e7df44 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-glutamic_Acid; data-row positions=[1616] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1616,"object_id":"CHEBI:16015","object_label":"L-glutamic acid","other":"L-Glutamate&#124;(2S)-2-aminopentanedioic acid&#124;(S)-2-aminopentanedioic acid&#124;(S)-glutamic acid&#124;L-Glu&#124;L-Glutaminic acid&#124;L-Glutaminsaeure&#124;acide glutamique&#124;acido glutamico&#124;acidum glutamicum&#124;GLUTAMIC ACID&#124;CAS:56-86-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-glutamic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-38d75cb4c4090c25 | docs/data/mapped_ingredients.csv; CSV lines=[1250] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16015","line":1250,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"143","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic acid","total_occurrences":"143"}] |
| ev-aee7ec664ba69d02 | reports/yaml_record_review/L-glutamic_Acid.md; &#96;data/ingredients/mapped/L-glutamic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a430de422c5af50e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[818] | context_only | [{"current_record_sha256":"1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb","finding_id":"SEM:6d0044cde431e1111f94","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-glutamic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-glutamic_Acid (data/ingredients/mapped/L-glutamic_Acid.yaml)'
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
summary: Per-record structured review for L-glutamic_Acid (data/ingredients/mapped/L-glutamic_Acid.yaml,
  record-cfd9a89c582f6fdd, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-glutamic_Acid.yaml
    sha256: 1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-glutamic_Acid.md
    sha256: dff6a1d0658cc21f0df6c4f590715dd0145a1c0cf0b920f8577a63a8822033d8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-cfd9a89c582f6fdd
  path: data/ingredients/mapped/L-glutamic_Acid.yaml
  label: L-glutamic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-glutamic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-glutamic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-glutamic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-cfd9a89c582f6fdd
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-cfd9a89c582f6fdd
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-cfd9a89c582f6fdd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-cfd9a89c582f6fdd
evidence:
- evidence_id: ev-075b5949153dbf0f
  kind: record_content
  reference: data/ingredients/mapped/L-glutamic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1248],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16015","line":1250,"mapping_status":"MAPPED","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic
    acid"}],"identifier":"CHEBI:16015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":143,"edge_count":143,"occurrences":143},"occurrence_statistics":{"media_count":143,"total_occurrences":143},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16015","ontology_label":"L-glutamic
    acid","ontology_source":"CHEBI"},"preferred_term":"L-Glutamic acid","sssom_rows":[{"data_row":1616,"object_id":"CHEBI:16015","object_label":"L-glutamic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-glutamic_Acid","synonym_count":13}'
  snapshot_sha256: 1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb
- evidence_id: ev-ceb2ca3b27a2caae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1248]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a2adfdb527e7df44
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-glutamic_Acid; data-row positions=[1616]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1616,"object_id":"CHEBI:16015","object_label":"L-glutamic
    acid","other":"L-Glutamate|(2S)-2-aminopentanedioic acid|(S)-2-aminopentanedioic
    acid|(S)-glutamic acid|L-Glu|L-Glutaminic acid|L-Glutaminsaeure|acide glutamique|acido
    glutamico|acidum glutamicum|GLUTAMIC ACID|CAS:56-86-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-glutamic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-38d75cb4c4090c25
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1250]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16015","line":1250,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"143","ontology_id":"CHEBI:16015","preferred_term":"L-Glutamic
    acid","total_occurrences":"143"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aee7ec664ba69d02
  kind: prior_review
  reference: reports/yaml_record_review/L-glutamic_Acid.md
  locator: '`data/ingredients/mapped/L-glutamic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dff6a1d0658cc21f0df6c4f590715dd0145a1c0cf0b920f8577a63a8822033d8
  quote: "Recommended Edits:\n- Major: remove or demote `L-Glutamate` in\n  `data/ingredients/mapped/L-glutamic_Acid.yaml`;\
    \ keep that label for the\n  charged L-glutamate identity.\n- Sync the aggregate\
    \ copy and regenerate the SSSOM/docs products so `other`\n  stops publishing the\
    \ cross-charge synonym; rerun strict, term, round-trip,\n  component, and SSSOM\
    \ validation."
- evidence_id: ev-a430de422c5af50e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[818]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb","finding_id":"SEM:6d0044cde431e1111f94","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-13a3768ae055b498
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-cfd9a89c582f6fdd
  evidence_ids:
  - ev-075b5949153dbf0f
  - ev-ceb2ca3b27a2caae
  - ev-a2adfdb527e7df44
  - ev-38d75cb4c4090c25
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-eeb8ea7a781a8502
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cfd9a89c582f6fdd
  evidence_ids:
  - ev-aee7ec664ba69d02
  - ev-075b5949153dbf0f
  - ev-a430de422c5af50e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z;
    reviewed SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb;
    current SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb;
    hash_changed=False. Reports=["reports/yaml_record_review/L-glutamic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:16015 identity, CAS value, PubChem structure, nitrogen-source role, occurrence
    count, and most final synonyms pass, but final SSSOM exports charged L-Glutamate.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aee7ec664ba69d02
    - ev-075b5949153dbf0f
  - name: legacy-native-ids
    value: '["SEM:6d0044cde431e1111f94"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-075b5949153dbf0f
    - ev-aee7ec664ba69d02
    - ev-a430de422c5af50e
findings:
- finding_id: rec-f-40c2a229fa4f401a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-cfd9a89c582f6fdd
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-glutamic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z;
    reviewed SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb;
    current SHA-256=1abbfb5fd04f94d5f684108d4304267a5d8c972a9d9a629d60ba755198c6edbb;
    hash_changed=False. Reports=["reports/yaml_record_review/L-glutamic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:16015 identity, CAS value, PubChem structure, nitrogen-source role, occurrence
    count, and most final synonyms pass, but final SSSOM exports charged L-Glutamate.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cfd9a89c582f6fdd
  evidence_ids:
  - ev-aee7ec664ba69d02
  - ev-075b5949153dbf0f
  - ev-a430de422c5af50e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-glutamic_Acid.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
