# Per-record structured review: Thiamine (data/ingredients/mapped/Thiamine.yaml)

- Review: 20261017T083000Z-thiamine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Thiamine (data/ingredients/mapped/Thiamine.yaml, record-615b0d99b5f72b86, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Thiamine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Thiamine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-615b0d99b5f72b86 | data/ingredients/mapped/Thiamine.yaml | maintained | Thiamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-615b0d99b5f72b86 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-615b0d99b5f72b86 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-615b0d99b5f72b86 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-615b0d99b5f72b86.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-615b0d99b5f72b86.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z; reviewed SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e; current SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e; hash_changed=False. Reports=["reports/yaml_record_review/Thiamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym match to CHEBI:18385 and CAS RN pass, but final SSSOM other exports broader/plural vitamin labels and concentration-qualified recipe text.

## Findings

### rec-f-0c19d5dd5d659a0e: Historical review coverage and residual narrative: Thiamine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-615b0d99b5f72b86.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z; reviewed SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e; current SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e; hash_changed=False. Reports=["reports/yaml_record_review/Thiamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym match to CHEBI:18385 and CAS RN pass, but final SSSOM other exports broader/plural vitamin labels and concentration-qualified recipe text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8054958cc1f7b3f2 | data/ingredients/mapped/Thiamine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1955],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18385","line":1957,"mapping_status":"MAPPED","ontology_id":"CHEBI:18385","preferred_term":"Thiamine"}],"identifier":"CHEBI:18385","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":159,"edge_count":159,"occurrences":159},"occurrence_statistics":{"media_count":159,"total_occurrences":159},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18385","ontology_label":"thiamine(1+)","ontology_source":"CHEBI"},"preferred_term":"Thiamine","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:18385","object_label":"thiamine(1+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine","synonym_count":20} |
| ev-987320bf7adbb063 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1955] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ae2fcf8420c449dd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Thiamine; data-row positions=[2761] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2761,"object_id":"CHEBI:18385","object_label":"thiamine(1+)","other":"thiamines&#124;thiamins&#124;vitamin B1 vitamer&#124;vitamin B1 vitamers&#124;vitamins B1&#124;Thiamin&#124;3-(4-AMINO-2-METHYL-PYRIMIDIN-5-YLMETHYL)-5-(2-HYDROXY-ETHYL)-4-METHYL-THIAZOL-3-IUM&#124;3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium&#124;Aneurin&#124;Antiberiberi factor&#124;Thiamine (B1)&#124;thiamine cation&#124;thiamine ion&#124;thiamine(1+) ion&#124;thiaminium&#124;Thiamine (0.05 \u03bcg/mL)&#124;CAS:70-16-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-169a8579d8943368 | docs/data/mapped_ingredients.csv; CSV lines=[1957] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18385","line":1957,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"159","ontology_id":"CHEBI:18385","preferred_term":"Thiamine","total_occurrences":"159"}] |
| ev-19e389e02344e679 | reports/yaml_record_review/Thiamine.md; &#96;data/ingredients/mapped/Thiamine.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:35; Completeness:49; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-013c30fa15545822 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1282] | context_only | [{"current_record_sha256":"8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e","finding_id":"SEM:167218e009c026b06904","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-thiamine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Thiamine (data/ingredients/mapped/Thiamine.yaml)'
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
summary: Per-record structured review for Thiamine (data/ingredients/mapped/Thiamine.yaml,
  record-615b0d99b5f72b86, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Thiamine.yaml
    sha256: 8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Thiamine.md
    sha256: b02fa2d1fc8704586a7c93e6a84a07ab1791d2605a99c16cad0fdd265312dd53
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-615b0d99b5f72b86
  path: data/ingredients/mapped/Thiamine.yaml
  label: Thiamine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Thiamine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Thiamine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-615b0d99b5f72b86
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-615b0d99b5f72b86
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-615b0d99b5f72b86
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-615b0d99b5f72b86
evidence:
- evidence_id: ev-8054958cc1f7b3f2
  kind: record_content
  reference: data/ingredients/mapped/Thiamine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1955],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18385","line":1957,"mapping_status":"MAPPED","ontology_id":"CHEBI:18385","preferred_term":"Thiamine"}],"identifier":"CHEBI:18385","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":159,"edge_count":159,"occurrences":159},"occurrence_statistics":{"media_count":159,"total_occurrences":159},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18385","ontology_label":"thiamine(1+)","ontology_source":"CHEBI"},"preferred_term":"Thiamine","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:18385","object_label":"thiamine(1+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine","synonym_count":20}'
  snapshot_sha256: 8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e
- evidence_id: ev-987320bf7adbb063
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1955]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ae2fcf8420c449dd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Thiamine; data-row positions=[2761]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2761,"object_id":"CHEBI:18385","object_label":"thiamine(1+)","other":"thiamines|thiamins|vitamin
    B1 vitamer|vitamin B1 vitamers|vitamins B1|Thiamin|3-(4-AMINO-2-METHYL-PYRIMIDIN-5-YLMETHYL)-5-(2-HYDROXY-ETHYL)-4-METHYL-THIAZOL-3-IUM|3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium|Aneurin|Antiberiberi
    factor|Thiamine (B1)|thiamine cation|thiamine ion|thiamine(1+) ion|thiaminium|Thiamine
    (0.05 \u03bcg/mL)|CAS:70-16-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-169a8579d8943368
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1957]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18385","line":1957,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"159","ontology_id":"CHEBI:18385","preferred_term":"Thiamine","total_occurrences":"159"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-19e389e02344e679
  kind: prior_review
  reference: reports/yaml_record_review/Thiamine.md
  locator: '`data/ingredients/mapped/Thiamine.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:35; Completeness:49; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b02fa2d1fc8704586a7c93e6a84a07ab1791d2605a99c16cad0fdd265312dd53
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Thiamine.yaml`,\
    \ remove or retype the\n  broader/plural `vitamin B1 vitamer`, `vitamin B1 vitamers`,\
    \ `thiamines`,\n  `thiamins`, and `vitamins B1` labels so they do not publish\
    \ as exact\n  `other` values for `CHEBI:18385`.\n- Major: in `data/ingredients/mapped/Thiamine.yaml`,\
    \ keep the CultureMech\n  occurrence surface `Thiamine (0.05 ug/mL)` as provenance\
    \ only or filter it\n  from SSSOM export. Then rerun strict validation, SSSOM\
    \ publication,\n  synonym-row review, and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-013c30fa15545822
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1282]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e","finding_id":"SEM:167218e009c026b06904","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d59e3c5fd29e8bf4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-615b0d99b5f72b86
  evidence_ids:
  - ev-8054958cc1f7b3f2
  - ev-987320bf7adbb063
  - ev-ae2fcf8420c449dd
  - ev-169a8579d8943368
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0b1c3a48bd293579
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-615b0d99b5f72b86
  evidence_ids:
  - ev-19e389e02344e679
  - ev-8054958cc1f7b3f2
  - ev-013c30fa15545822
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z;
    reviewed SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e;
    current SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym match to CHEBI:18385
    and CAS RN pass, but final SSSOM other exports broader/plural vitamin labels and
    concentration-qualified recipe text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-19e389e02344e679
    - ev-8054958cc1f7b3f2
  - name: legacy-native-ids
    value: '["SEM:167218e009c026b06904"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8054958cc1f7b3f2
    - ev-19e389e02344e679
    - ev-013c30fa15545822
findings:
- finding_id: rec-f-0c19d5dd5d659a0e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-615b0d99b5f72b86
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Thiamine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z;
    reviewed SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e;
    current SHA-256=8a72b4399b922c430e3a33792b3e8b0c2efb26f647d5f78fa4c7a6c4f42ff52e;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym match to CHEBI:18385
    and CAS RN pass, but final SSSOM other exports broader/plural vitamin labels and
    concentration-qualified recipe text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-615b0d99b5f72b86
  evidence_ids:
  - ev-19e389e02344e679
  - ev-8054958cc1f7b3f2
  - ev-013c30fa15545822
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
