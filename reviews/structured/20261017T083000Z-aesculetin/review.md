# Per-record structured review: Aesculetin (data/ingredients/mapped/Aesculetin.yaml)

- Review: 20261017T083000Z-aesculetin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Aesculetin (data/ingredients/mapped/Aesculetin.yaml, record-76aa3d994aec402b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Aesculetin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Aesculetin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-76aa3d994aec402b | data/ingredients/mapped/Aesculetin.yaml | maintained | Aesculetin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-76aa3d994aec402b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-76aa3d994aec402b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-76aa3d994aec402b | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-76aa3d994aec402b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-76aa3d994aec402b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:25:24Z; reviewed SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46; current SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46; hash_changed=False. Reports=["reports/yaml_record_review/Aesculetin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: CAS 305-01-1 is valid, but ChEBI now has exact esculetin term CHEBI:490095, so the FALLBACK_REGISTRY mapping and no-CHEBI evidence are stale.

## Findings

### rec-f-f8fbc4a6eee936ff: Historical review coverage and residual narrative: Aesculetin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-76aa3d994aec402b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:25:24Z; reviewed SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46; current SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46; hash_changed=False. Reports=["reports/yaml_record_review/Aesculetin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: CAS 305-01-1 is valid, but ChEBI now has exact esculetin term CHEBI:490095, so the FALLBACK_REGISTRY mapping and no-CHEBI evidence are stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6cbbda5a5fea5c1d | data/ingredients/mapped/Aesculetin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[459],"raw_equal":true},"docs_rows":[{"identifier":"cas:305-01-1","line":461,"mapping_status":"MAPPED","ontology_id":"cas:305-01-1","preferred_term":"Aesculetin"}],"identifier":"cas:305-01-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:305-01-1","ontology_label":"Aesculetin","ontology_source":"CAS"},"preferred_term":"Aesculetin","sssom_rows":[{"data_row":311,"object_id":"cas:305-01-1","object_label":"Aesculetin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aesculetin","synonym_count":0} |
| ev-89f845fa0851d19d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [459] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-be75c9969ce99a85 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Aesculetin; data-row positions=[311] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":311,"object_id":"cas:305-01-1","object_label":"Aesculetin","other":"CAS:305-01-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Aesculetin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-ad668272534dd072 | docs/data/mapped_ingredients.csv; CSV lines=[461] | supports | Published identity and count rows inspected: [{"identifier":"cas:305-01-1","line":461,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:305-01-1","preferred_term":"Aesculetin","total_occurrences":"0"}] |
| ev-f57f6edacd40cece | reports/yaml_record_review/Aesculetin.md; &#96;data/ingredients/mapped/Aesculetin.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:44; Completeness:60; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6f5598cd84ee2af2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[218] | context_only | [{"current_record_sha256":"4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46","finding_id":"SEM:54ddc80262db0959a222","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-aesculetin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Aesculetin (data/ingredients/mapped/Aesculetin.yaml)'
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
summary: Per-record structured review for Aesculetin (data/ingredients/mapped/Aesculetin.yaml,
  record-76aa3d994aec402b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Aesculetin.yaml
    sha256: 4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46
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
  - path: reports/yaml_record_review/Aesculetin.md
    sha256: 2e6fcbe68e7d2419adf1e4674a0106eaac8d8af3b1ebd2a61f576fcc93c65bf7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-76aa3d994aec402b
  path: data/ingredients/mapped/Aesculetin.yaml
  label: Aesculetin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aesculetin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Aesculetin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Aesculetin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-76aa3d994aec402b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-76aa3d994aec402b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-76aa3d994aec402b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-76aa3d994aec402b
evidence:
- evidence_id: ev-6cbbda5a5fea5c1d
  kind: record_content
  reference: data/ingredients/mapped/Aesculetin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[459],"raw_equal":true},"docs_rows":[{"identifier":"cas:305-01-1","line":461,"mapping_status":"MAPPED","ontology_id":"cas:305-01-1","preferred_term":"Aesculetin"}],"identifier":"cas:305-01-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:305-01-1","ontology_label":"Aesculetin","ontology_source":"CAS"},"preferred_term":"Aesculetin","sssom_rows":[{"data_row":311,"object_id":"cas:305-01-1","object_label":"Aesculetin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aesculetin","synonym_count":0}'
  snapshot_sha256: 4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46
- evidence_id: ev-89f845fa0851d19d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [459]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-be75c9969ce99a85
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Aesculetin; data-row positions=[311]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":311,"object_id":"cas:305-01-1","object_label":"Aesculetin","other":"CAS:305-01-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Aesculetin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ad668272534dd072
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[461]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:305-01-1","line":461,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:305-01-1","preferred_term":"Aesculetin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f57f6edacd40cece
  kind: prior_review
  reference: reports/yaml_record_review/Aesculetin.md
  locator: '`data/ingredients/mapped/Aesculetin.yaml`:2; Verdict:4; Identity:10; Validation:24;
    Evidence:44; Completeness:60; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2e6fcbe68e7d2419adf1e4674a0106eaac8d8af3b1ebd2a61f576fcc93c65bf7
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Aesculetin.yaml`, promote\
    \ the CAS fallback to\n  `CHEBI:490095`, canonical `ontology_label: esculetin`,\
    \ and a CAS-backed ChEBI\n  mapping quality.\n- Update the stale `ontology_mapping.evidence`\
    \ note that says no ChEBI entry\n  exists, add `chemical_properties` for `CHEBI:490095`/PubChem\
    \ CID `5281416`,\n  and keep `305-01-1` as a CAS xref rather than the primary\
    \ mapping.\n- Regenerate synchronized products, then rerun\n  `uv run --frozen\
    \ python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data\
    \ data/ingredients/mapped/Aesculetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-6f5598cd84ee2af2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[218]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46","finding_id":"SEM:54ddc80262db0959a222","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d2a9d0145158a5bc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-76aa3d994aec402b
  evidence_ids:
  - ev-6cbbda5a5fea5c1d
  - ev-89f845fa0851d19d
  - ev-be75c9969ce99a85
  - ev-ad668272534dd072
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f7d7df3014efd793
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-76aa3d994aec402b
  evidence_ids:
  - ev-f57f6edacd40cece
  - ev-6cbbda5a5fea5c1d
  - ev-6f5598cd84ee2af2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:25:24Z;
    reviewed SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46;
    current SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46;
    hash_changed=False. Reports=["reports/yaml_record_review/Aesculetin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: CAS 305-01-1 is
    valid, but ChEBI now has exact esculetin term CHEBI:490095, so the FALLBACK_REGISTRY
    mapping and no-CHEBI evidence are stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f57f6edacd40cece
    - ev-6cbbda5a5fea5c1d
  - name: legacy-native-ids
    value: '["SEM:54ddc80262db0959a222"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6cbbda5a5fea5c1d
    - ev-f57f6edacd40cece
    - ev-6f5598cd84ee2af2
findings:
- finding_id: rec-f-f8fbc4a6eee936ff
  issue_key: mim-reconciliation-historical-review-coverage-and-r-76aa3d994aec402b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Aesculetin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:25:24Z;
    reviewed SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46;
    current SHA-256=4a66fca05baa72ce5cc6204fe12905038ae7f7a017378e3435d4fc7794e2ce46;
    hash_changed=False. Reports=["reports/yaml_record_review/Aesculetin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: CAS 305-01-1 is
    valid, but ChEBI now has exact esculetin term CHEBI:490095, so the FALLBACK_REGISTRY
    mapping and no-CHEBI evidence are stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-76aa3d994aec402b
  evidence_ids:
  - ev-f57f6edacd40cece
  - ev-6cbbda5a5fea5c1d
  - ev-6f5598cd84ee2af2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aesculetin.yaml
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
