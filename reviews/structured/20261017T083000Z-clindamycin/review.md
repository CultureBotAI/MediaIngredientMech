# Per-record structured review: Clindamycin (data/ingredients/mapped/Clindamycin.yaml)

- Review: 20261017T083000Z-clindamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Clindamycin (data/ingredients/mapped/Clindamycin.yaml, record-9bd2408577703427, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Clindamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Clindamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9bd2408577703427 | data/ingredients/mapped/Clindamycin.yaml | maintained | Clindamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9bd2408577703427 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9bd2408577703427 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9bd2408577703427 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9bd2408577703427.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9bd2408577703427.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:18:47Z; reviewed SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5; current SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5; hash_changed=False. Reports=["reports/yaml_record_review/Clindamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI clindamycin identity passes, but one active RAW_TEXT synonym resolves to a different PubChem CID and still reaches final SSSOM.

## Findings

### rec-f-271379493ad00f21: Historical review coverage and residual narrative: Clindamycin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9bd2408577703427.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:18:47Z; reviewed SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5; current SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5; hash_changed=False. Reports=["reports/yaml_record_review/Clindamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI clindamycin identity passes, but one active RAW_TEXT synonym resolves to a different PubChem CID and still reaches final SSSOM.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ad0cdc34eb3c6c02 | data/ingredients/mapped/Clindamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2219],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3745","line":2221,"mapping_status":"MAPPED","ontology_id":"CHEBI:3745","preferred_term":"Clindamycin"}],"identifier":"CHEBI:3745","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":104,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance&#124;BacDive_Antibiotic_sensitivity"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3745","ontology_label":"clindamycin","ontology_source":"CHEBI"},"preferred_term":"Clindamycin","sssom_rows":[{"data_row":786,"object_id":"CHEBI:3745","object_label":"clindamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Clindamycin","synonym_count":1} |
| ev-1f29e59806905649 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2219] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9104642e24cc87c1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Clindamycin; data-row positions=[786] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":786,"object_id":"CHEBI:3745","object_label":"clindamycin","other":"methyl 7-chloro-6,7,8-trideoxy-6-({[(2S,4R)-1-methyl-4-propylpyrrolidin-2-yl]carbonyl}amino)-1-thio-D-glycero-alpha-D-galacto-octopyranoside","predicate_id":"skos:exactMatch","subject_id":"MIM:Clindamycin","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-32f55b034a3379e8 | docs/data/mapped_ingredients.csv; CSV lines=[2221] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3745","line":2221,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3745","preferred_term":"Clindamycin","total_occurrences":"0"}] |
| ev-af77c6f26cbfd53b | reports/yaml_record_review/Clindamycin.md; &#96;data/ingredients/mapped/Clindamycin.yaml&#96;:2; Verdict:4; Identity:13; Validation:32; Evidence:49; Completeness:67; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-050076249fcef5d3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[426] | context_only | [{"current_record_sha256":"a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5","finding_id":"SEM:309fe6aa08e010bc0692","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-clindamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Clindamycin (data/ingredients/mapped/Clindamycin.yaml)'
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
summary: Per-record structured review for Clindamycin (data/ingredients/mapped/Clindamycin.yaml,
  record-9bd2408577703427, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Clindamycin.yaml
    sha256: a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Clindamycin.md
    sha256: 38b3af1c407e527e8b5c54864639011896d5dac2f991dcdbf3a03b0b3d7d748b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9bd2408577703427
  path: data/ingredients/mapped/Clindamycin.yaml
  label: Clindamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Clindamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Clindamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Clindamycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9bd2408577703427
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9bd2408577703427
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9bd2408577703427
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9bd2408577703427
evidence:
- evidence_id: ev-ad0cdc34eb3c6c02
  kind: record_content
  reference: data/ingredients/mapped/Clindamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2219],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3745","line":2221,"mapping_status":"MAPPED","ontology_id":"CHEBI:3745","preferred_term":"Clindamycin"}],"identifier":"CHEBI:3745","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":104,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3745","ontology_label":"clindamycin","ontology_source":"CHEBI"},"preferred_term":"Clindamycin","sssom_rows":[{"data_row":786,"object_id":"CHEBI:3745","object_label":"clindamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Clindamycin","synonym_count":1}'
  snapshot_sha256: a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5
- evidence_id: ev-1f29e59806905649
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2219]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9104642e24cc87c1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Clindamycin; data-row positions=[786]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":786,"object_id":"CHEBI:3745","object_label":"clindamycin","other":"methyl
    7-chloro-6,7,8-trideoxy-6-({[(2S,4R)-1-methyl-4-propylpyrrolidin-2-yl]carbonyl}amino)-1-thio-D-glycero-alpha-D-galacto-octopyranoside","predicate_id":"skos:exactMatch","subject_id":"MIM:Clindamycin","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-32f55b034a3379e8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2221]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3745","line":2221,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3745","preferred_term":"Clindamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-af77c6f26cbfd53b
  kind: prior_review
  reference: reports/yaml_record_review/Clindamycin.md
  locator: '`data/ingredients/mapped/Clindamycin.yaml`:2; Verdict:4; Identity:13;
    Validation:32; Evidence:49; Completeness:67; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 38b3af1c407e527e8b5c54864639011896d5dac2f991dcdbf3a03b0b3d7d748b
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Clindamycin.yaml`,\
    \ remove the\n  CID-29029-specific `RAW_TEXT` synonym or replace it with an exact\n\
    \  ChEBI/PubChem clindamycin synonym.\n- Regenerate synchronized products and\
    \ rerun strict validation, SSSOM QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-050076249fcef5d3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[426]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5","finding_id":"SEM:309fe6aa08e010bc0692","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0bf6532e23308e7c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9bd2408577703427
  evidence_ids:
  - ev-ad0cdc34eb3c6c02
  - ev-1f29e59806905649
  - ev-9104642e24cc87c1
  - ev-32f55b034a3379e8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2714920a5169a14c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9bd2408577703427
  evidence_ids:
  - ev-af77c6f26cbfd53b
  - ev-ad0cdc34eb3c6c02
  - ev-050076249fcef5d3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:18:47Z;
    reviewed SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5;
    current SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5;
    hash_changed=False. Reports=["reports/yaml_record_review/Clindamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    clindamycin identity passes, but one active RAW_TEXT synonym resolves to a different
    PubChem CID and still reaches final SSSOM.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-af77c6f26cbfd53b
    - ev-ad0cdc34eb3c6c02
  - name: legacy-native-ids
    value: '["SEM:309fe6aa08e010bc0692"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ad0cdc34eb3c6c02
    - ev-af77c6f26cbfd53b
    - ev-050076249fcef5d3
findings:
- finding_id: rec-f-271379493ad00f21
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9bd2408577703427
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Clindamycin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:18:47Z;
    reviewed SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5;
    current SHA-256=a6712f58fe65e83a987f2a0bd6f80c98c64f1ac930cb296c69a3af77964932a5;
    hash_changed=False. Reports=["reports/yaml_record_review/Clindamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    clindamycin identity passes, but one active RAW_TEXT synonym resolves to a different
    PubChem CID and still reaches final SSSOM.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9bd2408577703427
  evidence_ids:
  - ev-af77c6f26cbfd53b
  - ev-ad0cdc34eb3c6c02
  - ev-050076249fcef5d3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Clindamycin.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
