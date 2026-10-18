# Per-record structured review: L-histidine (data/ingredients/mapped/L-histidine.yaml)

- Review: 20261017T083000Z-l-histidine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-histidine (data/ingredients/mapped/L-histidine.yaml, record-34cf99e23476f59f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-histidine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-histidine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-34cf99e23476f59f | data/ingredients/mapped/L-histidine.yaml | maintained | L-histidine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-34cf99e23476f59f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-34cf99e23476f59f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-34cf99e23476f59f | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-34cf99e23476f59f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-34cf99e23476f59f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z; reviewed SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d; current SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d; hash_changed=False. Reports=["reports/yaml_record_review/L-histidine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15971 identity, CAS value, PubChem structure, nitrogen-source role, occurrence count, and active ChEBI grounding pass, but final SSSOM exports bare Histidine.

## Findings

### rec-f-2d4808230838532f: Historical review coverage and residual narrative: L-histidine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-34cf99e23476f59f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z; reviewed SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d; current SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d; hash_changed=False. Reports=["reports/yaml_record_review/L-histidine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15971 identity, CAS value, PubChem structure, nitrogen-source role, occurrence count, and active ChEBI grounding pass, but final SSSOM exports bare Histidine.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5620fd9d637ba6af | data/ingredients/mapped/L-histidine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1250],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15971","line":1252,"mapping_status":"MAPPED","ontology_id":"CHEBI:15971","preferred_term":"L-Histidine"}],"identifier":"CHEBI:15971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":154,"edge_count":154,"occurrences":154},"occurrence_statistics":{"media_count":154,"total_occurrences":154},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15971","ontology_label":"L-histidine","ontology_source":"CHEBI"},"preferred_term":"L-Histidine","sssom_rows":[{"data_row":1618,"object_id":"CHEBI:15971","object_label":"L-histidine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-histidine","synonym_count":11} |
| ev-bf24bc624817dd63 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1250] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cccefcb9411d0707 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-histidine; data-row positions=[1618] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1618,"object_id":"CHEBI:15971","object_label":"L-histidine","other":"(2S)-2-amino-3-(1H-imidazol-4-yl)propanoic acid&#124;(S)-4-(2-Amino-2-carboxyethyl)imidazole&#124;(S)-alpha-Amino-1H-imidazole-4-propionic acid&#124;(S)-alpha-amino-1H-Imidazole-4-propanoic acid&#124;L-(-)-histidine&#124;L-Histidin&#124;Histidine&#124;CAS:71-00-1","predicate_id":"skos:exactMatch","subject_id":"MIM:L-histidine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6c9a86beea5c79ee | docs/data/mapped_ingredients.csv; CSV lines=[1252] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15971","line":1252,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"154","ontology_id":"CHEBI:15971","preferred_term":"L-Histidine","total_occurrences":"154"}] |
| ev-3b2d8beecd472875 | reports/yaml_record_review/L-histidine.md; &#96;data/ingredients/mapped/L-histidine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:49; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ab5c00704aecee53 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[819] | context_only | [{"current_record_sha256":"e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d","finding_id":"SEM:16185d6e6d94c0c4fa7a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-histidine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-histidine (data/ingredients/mapped/L-histidine.yaml)'
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
summary: Per-record structured review for L-histidine (data/ingredients/mapped/L-histidine.yaml,
  record-34cf99e23476f59f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-histidine.yaml
    sha256: e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d
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
  - path: reports/yaml_record_review/L-histidine.md
    sha256: 902fe5bae765cfa9a2d3c0d6227c71249b5182f7b5f3cc8bf71c542efd837312
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-34cf99e23476f59f
  path: data/ingredients/mapped/L-histidine.yaml
  label: L-histidine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-histidine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-histidine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-histidine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-34cf99e23476f59f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-34cf99e23476f59f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-34cf99e23476f59f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-34cf99e23476f59f
evidence:
- evidence_id: ev-5620fd9d637ba6af
  kind: record_content
  reference: data/ingredients/mapped/L-histidine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1250],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15971","line":1252,"mapping_status":"MAPPED","ontology_id":"CHEBI:15971","preferred_term":"L-Histidine"}],"identifier":"CHEBI:15971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":154,"edge_count":154,"occurrences":154},"occurrence_statistics":{"media_count":154,"total_occurrences":154},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15971","ontology_label":"L-histidine","ontology_source":"CHEBI"},"preferred_term":"L-Histidine","sssom_rows":[{"data_row":1618,"object_id":"CHEBI:15971","object_label":"L-histidine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-histidine","synonym_count":11}'
  snapshot_sha256: e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d
- evidence_id: ev-bf24bc624817dd63
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1250]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cccefcb9411d0707
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-histidine; data-row positions=[1618]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1618,"object_id":"CHEBI:15971","object_label":"L-histidine","other":"(2S)-2-amino-3-(1H-imidazol-4-yl)propanoic
    acid|(S)-4-(2-Amino-2-carboxyethyl)imidazole|(S)-alpha-Amino-1H-imidazole-4-propionic
    acid|(S)-alpha-amino-1H-Imidazole-4-propanoic acid|L-(-)-histidine|L-Histidin|Histidine|CAS:71-00-1","predicate_id":"skos:exactMatch","subject_id":"MIM:L-histidine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6c9a86beea5c79ee
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1252]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15971","line":1252,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"154","ontology_id":"CHEBI:15971","preferred_term":"L-Histidine","total_occurrences":"154"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3b2d8beecd472875
  kind: prior_review
  reference: reports/yaml_record_review/L-histidine.md
  locator: '`data/ingredients/mapped/L-histidine.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:49; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 902fe5bae765cfa9a2d3c0d6227c71249b5182f7b5f3cc8bf71c542efd837312
  quote: "Recommended Edits:\n- Major: remove `Histidine` from\n  `data/ingredients/mapped/L-histidine.yaml`;\
    \ keep the bare label only on the\n  existing generic `data/ingredients/mapped/Dl-histidine.yaml`\
    \ record.\n- Sync the aggregate copy and regenerate the SSSOM/docs products so\
    \ `other`\n  stops publishing the cross-stereochemistry synonym; rerun strict,\
    \ term,\n  round-trip, component, and SSSOM validation."
- evidence_id: ev-ab5c00704aecee53
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[819]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d","finding_id":"SEM:16185d6e6d94c0c4fa7a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e6d98295ecd204c0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-34cf99e23476f59f
  evidence_ids:
  - ev-5620fd9d637ba6af
  - ev-bf24bc624817dd63
  - ev-cccefcb9411d0707
  - ev-6c9a86beea5c79ee
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8eac46d78646f976
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-34cf99e23476f59f
  evidence_ids:
  - ev-3b2d8beecd472875
  - ev-5620fd9d637ba6af
  - ev-ab5c00704aecee53
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z;
    reviewed SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d;
    current SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d;
    hash_changed=False. Reports=["reports/yaml_record_review/L-histidine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15971
    identity, CAS value, PubChem structure, nitrogen-source role, occurrence count,
    and active ChEBI grounding pass, but final SSSOM exports bare Histidine.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3b2d8beecd472875
    - ev-5620fd9d637ba6af
  - name: legacy-native-ids
    value: '["SEM:16185d6e6d94c0c4fa7a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5620fd9d637ba6af
    - ev-3b2d8beecd472875
    - ev-ab5c00704aecee53
findings:
- finding_id: rec-f-2d4808230838532f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-34cf99e23476f59f
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-histidine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:00:44Z;
    reviewed SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d;
    current SHA-256=e610c6f890361baf08dfe64b2399c78c09fc02a486f552d460daf8562e20968d;
    hash_changed=False. Reports=["reports/yaml_record_review/L-histidine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15971
    identity, CAS value, PubChem structure, nitrogen-source role, occurrence count,
    and active ChEBI grounding pass, but final SSSOM exports bare Histidine.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-34cf99e23476f59f
  evidence_ids:
  - ev-3b2d8beecd472875
  - ev-5620fd9d637ba6af
  - ev-ab5c00704aecee53
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-histidine.yaml
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
