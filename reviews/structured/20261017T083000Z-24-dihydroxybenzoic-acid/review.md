# Per-record structured review: 24-Dihydroxybenzoic_acid (data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml)

- Review: 20261017T083000Z-24-dihydroxybenzoic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 24-Dihydroxybenzoic_acid (data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml, record-8a4965c52c0bf677, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8a4965c52c0bf677 | data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml | maintained | 24-Dihydroxybenzoic_acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8a4965c52c0bf677 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8a4965c52c0bf677 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8a4965c52c0bf677 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8a4965c52c0bf677.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8a4965c52c0bf677.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:50:48Z; reviewed SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a; current SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a; hash_changed=False. Reports=["reports/yaml_record_review/24-Dihydroxybenzoic_acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active residual grounding to CHEBI:42094, occurrence count, SSSOM, and aggregate pass, but ingredient_type and ChEBI chemistry are missing.

## Findings

### rec-f-f52135a338616e1f: Historical review coverage and residual narrative: 24-Dihydroxybenzoic_acid

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8a4965c52c0bf677.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:50:48Z; reviewed SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a; current SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a; hash_changed=False. Reports=["reports/yaml_record_review/24-Dihydroxybenzoic_acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active residual grounding to CHEBI:42094, occurrence count, SSSOM, and aggregate pass, but ingredient_type and ChEBI chemistry are missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d94f35ff4278365b | data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2523],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42094","line":2525,"mapping_status":"MAPPED","ontology_id":"CHEBI:42094","preferred_term":"2,4-Dihydroxybenzoic acid"}],"identifier":"CHEBI:42094","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:42094","ontology_label":"2,4-dihydroxybenzoic acid","ontology_source":"CHEBI"},"preferred_term":"2,4-Dihydroxybenzoic acid","sssom_rows":[{"data_row":111,"object_id":"CHEBI:42094","object_label":"2,4-dihydroxybenzoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:24-Dihydroxybenzoic_acid","synonym_count":0} |
| ev-85c97eca1fabb0fe | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2523] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-efdd6c9c350b6294 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:24-Dihydroxybenzoic_acid; data-row positions=[111] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":111,"object_id":"CHEBI:42094","object_label":"2,4-dihydroxybenzoic acid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:24-Dihydroxybenzoic_acid","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-798eecc545c8a30f | docs/data/mapped_ingredients.csv; CSV lines=[2525] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:42094","line":2525,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:42094","preferred_term":"2,4-Dihydroxybenzoic acid","total_occurrences":"1"}] |
| ev-6a803502a2da56ef | reports/yaml_record_review/24-Dihydroxybenzoic_acid.md; &#96;data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:37; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0d3d018dd6a44b9f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[92] | context_only | [{"current_record_sha256":"ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a","finding_id":"SEM:d8fbd39caa83c8307db7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-24-dihydroxybenzoic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 24-Dihydroxybenzoic_acid (data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml)'
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
summary: Per-record structured review for 24-Dihydroxybenzoic_acid (data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml,
  record-8a4965c52c0bf677, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
    sha256: ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/24-Dihydroxybenzoic_acid.md
    sha256: 7a2b3d1533cbeff89e072f372b38a4638e3cdc567310beb2c2e2a3e8a680b9fb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8a4965c52c0bf677
  path: data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
  label: 24-Dihydroxybenzoic_acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8a4965c52c0bf677
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8a4965c52c0bf677
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8a4965c52c0bf677
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8a4965c52c0bf677
evidence:
- evidence_id: ev-d94f35ff4278365b
  kind: record_content
  reference: data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2523],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42094","line":2525,"mapping_status":"MAPPED","ontology_id":"CHEBI:42094","preferred_term":"2,4-Dihydroxybenzoic
    acid"}],"identifier":"CHEBI:42094","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:42094","ontology_label":"2,4-dihydroxybenzoic
    acid","ontology_source":"CHEBI"},"preferred_term":"2,4-Dihydroxybenzoic acid","sssom_rows":[{"data_row":111,"object_id":"CHEBI:42094","object_label":"2,4-dihydroxybenzoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:24-Dihydroxybenzoic_acid","synonym_count":0}'
  snapshot_sha256: ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a
- evidence_id: ev-85c97eca1fabb0fe
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2523]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-efdd6c9c350b6294
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:24-Dihydroxybenzoic_acid; data-row positions=[111]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":111,"object_id":"CHEBI:42094","object_label":"2,4-dihydroxybenzoic
    acid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:24-Dihydroxybenzoic_acid","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-798eecc545c8a30f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2525]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:42094","line":2525,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:42094","preferred_term":"2,4-Dihydroxybenzoic
    acid","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6a803502a2da56ef
  kind: prior_review
  reference: reports/yaml_record_review/24-Dihydroxybenzoic_acid.md
  locator: '`data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml`:2; Verdict:4;
    Identity:10; Validation:24; Evidence:37; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7a2b3d1533cbeff89e072f372b38a4638e3cdc567310beb2c2e2a3e8a680b9fb
  quote: "Recommended Edits:\n1. Set `ingredient_type: SINGLE_INGREDIENT`.\n2. Backfill\
    \ CAS RN `89-86-1`, formula `C7H6O4`, InChI, and SMILES from ChEBI.\n3. Regenerate\
    \ `data/curated/mapped_ingredients.yaml`,\n   `mappings/ingredient_mappings.sssom.tsv`,\
    \ and docs from the maintained YAML.\n4. Re-run the focused strict/LinkML validators,\
    \ `just qc-sssom`, and\n   `just qc-flat-coverage` after those edits."
- evidence_id: ev-0d3d018dd6a44b9f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[92]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a","finding_id":"SEM:d8fbd39caa83c8307db7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b8a3ee28cf1bd651
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8a4965c52c0bf677
  evidence_ids:
  - ev-d94f35ff4278365b
  - ev-85c97eca1fabb0fe
  - ev-efdd6c9c350b6294
  - ev-798eecc545c8a30f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8356692bc6668346
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8a4965c52c0bf677
  evidence_ids:
  - ev-6a803502a2da56ef
  - ev-d94f35ff4278365b
  - ev-0d3d018dd6a44b9f
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:50:48Z;
    reviewed SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a;
    current SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a;
    hash_changed=False. Reports=["reports/yaml_record_review/24-Dihydroxybenzoic_acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active residual
    grounding to CHEBI:42094, occurrence count, SSSOM, and aggregate pass, but ingredient_type
    and ChEBI chemistry are missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6a803502a2da56ef
    - ev-d94f35ff4278365b
  - name: legacy-native-ids
    value: '["SEM:d8fbd39caa83c8307db7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d94f35ff4278365b
    - ev-6a803502a2da56ef
    - ev-0d3d018dd6a44b9f
findings:
- finding_id: rec-f-f52135a338616e1f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8a4965c52c0bf677
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 24-Dihydroxybenzoic_acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:50:48Z;
    reviewed SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a;
    current SHA-256=ebe160a8769dbcd699deba9ac4c6d2d13c3b0ec16cadc9959c9d26aba0a3807a;
    hash_changed=False. Reports=["reports/yaml_record_review/24-Dihydroxybenzoic_acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active residual
    grounding to CHEBI:42094, occurrence count, SSSOM, and aggregate pass, but ingredient_type
    and ChEBI chemistry are missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8a4965c52c0bf677
  evidence_ids:
  - ev-6a803502a2da56ef
  - ev-d94f35ff4278365b
  - ev-0d3d018dd6a44b9f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
