# Per-record structured review: 2-Nitrophenol (data/ingredients/mapped/2-Nitrophenol.yaml)

- Review: 20261017T083000Z-2-nitrophenol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-Nitrophenol (data/ingredients/mapped/2-Nitrophenol.yaml, record-1e2245c533d91954, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-Nitrophenol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-Nitrophenol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1e2245c533d91954 | data/ingredients/mapped/2-Nitrophenol.yaml | maintained | 2-Nitrophenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1e2245c533d91954 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1e2245c533d91954 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1e2245c533d91954 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1e2245c533d91954.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1e2245c533d91954.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:30:17Z; reviewed SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62; current SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62; hash_changed=False. Reports=["reports/yaml_record_review/2-Nitrophenol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Residual CultureMech grounding to CHEBI:16260 passes, but ingredient_type and ChEBI-derived chemistry are missing.

## Findings

### rec-f-70fdf1d06d6a330a: Historical review coverage and residual narrative: 2-Nitrophenol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1e2245c533d91954.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:30:17Z; reviewed SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62; current SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62; hash_changed=False. Reports=["reports/yaml_record_review/2-Nitrophenol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Residual CultureMech grounding to CHEBI:16260 passes, but ingredient_type and ChEBI-derived chemistry are missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8bca3ac2d1d770a9 | data/ingredients/mapped/2-Nitrophenol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2521],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16260","line":2523,"mapping_status":"MAPPED","ontology_id":"CHEBI:16260","preferred_term":"2-Nitrophenol"}],"identifier":"CHEBI:16260","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:16260","ontology_label":"2-nitrophenol","ontology_source":"CHEBI"},"preferred_term":"2-Nitrophenol","sssom_rows":[{"data_row":70,"object_id":"CHEBI:16260","object_label":"2-nitrophenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Nitrophenol","synonym_count":0} |
| ev-095ba6f131fb0a3a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2521] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c2af7cfbf33dba3b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-Nitrophenol; data-row positions=[70] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":70,"object_id":"CHEBI:16260","object_label":"2-nitrophenol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Nitrophenol","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-c5864656669fedd7 | docs/data/mapped_ingredients.csv; CSV lines=[2523] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16260","line":2523,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16260","preferred_term":"2-Nitrophenol","total_occurrences":"1"}] |
| ev-2e4736c37f4d61f0 | reports/yaml_record_review/2-Nitrophenol.md; &#96;data/ingredients/mapped/2-Nitrophenol.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:40; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3dfd44f0b72ef15a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[52] | context_only | [{"current_record_sha256":"a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62","finding_id":"SEM:95c215d379a05ae77aa3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-nitrophenol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-Nitrophenol (data/ingredients/mapped/2-Nitrophenol.yaml)'
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
summary: Per-record structured review for 2-Nitrophenol (data/ingredients/mapped/2-Nitrophenol.yaml,
  record-1e2245c533d91954, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-Nitrophenol.yaml
    sha256: a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62
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
  - path: reports/yaml_record_review/2-Nitrophenol.md
    sha256: 074f808be5c762d3d5ca7f11a21dfd821f135286d1967697fc6634b9df309163
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1e2245c533d91954
  path: data/ingredients/mapped/2-Nitrophenol.yaml
  label: 2-Nitrophenol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Nitrophenol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-Nitrophenol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-Nitrophenol.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1e2245c533d91954
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1e2245c533d91954
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1e2245c533d91954
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1e2245c533d91954
evidence:
- evidence_id: ev-8bca3ac2d1d770a9
  kind: record_content
  reference: data/ingredients/mapped/2-Nitrophenol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2521],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16260","line":2523,"mapping_status":"MAPPED","ontology_id":"CHEBI:16260","preferred_term":"2-Nitrophenol"}],"identifier":"CHEBI:16260","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:16260","ontology_label":"2-nitrophenol","ontology_source":"CHEBI"},"preferred_term":"2-Nitrophenol","sssom_rows":[{"data_row":70,"object_id":"CHEBI:16260","object_label":"2-nitrophenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Nitrophenol","synonym_count":0}'
  snapshot_sha256: a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62
- evidence_id: ev-095ba6f131fb0a3a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2521]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c2af7cfbf33dba3b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-Nitrophenol; data-row positions=[70]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":70,"object_id":"CHEBI:16260","object_label":"2-nitrophenol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Nitrophenol","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c5864656669fedd7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2523]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16260","line":2523,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16260","preferred_term":"2-Nitrophenol","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2e4736c37f4d61f0
  kind: prior_review
  reference: reports/yaml_record_review/2-Nitrophenol.md
  locator: '`data/ingredients/mapped/2-Nitrophenol.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:40; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 074f808be5c762d3d5ca7f11a21dfd821f135286d1967697fc6634b9df309163
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/2-Nitrophenol.yaml`,\
    \ add\n   `ingredient_type: SINGLE_INGREDIENT` and ChEBI-derived CAS/formula/InChI/SMILES\n\
    \   for `CHEBI:16260`.\n2. Regenerate `data/curated/mapped_ingredients.yaml` and\
    \ docs from the\n   maintained YAML.\n3. Re-run strict/LinkML validation and SSSOM\
    \ export checks after the backfill."
- evidence_id: ev-3dfd44f0b72ef15a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[52]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62","finding_id":"SEM:95c215d379a05ae77aa3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3df4f3e7212df40c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1e2245c533d91954
  evidence_ids:
  - ev-8bca3ac2d1d770a9
  - ev-095ba6f131fb0a3a
  - ev-c2af7cfbf33dba3b
  - ev-c5864656669fedd7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e6ee850b2c569bbd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1e2245c533d91954
  evidence_ids:
  - ev-2e4736c37f4d61f0
  - ev-8bca3ac2d1d770a9
  - ev-3dfd44f0b72ef15a
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:30:17Z;
    reviewed SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62;
    current SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62;
    hash_changed=False. Reports=["reports/yaml_record_review/2-Nitrophenol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Residual CultureMech
    grounding to CHEBI:16260 passes, but ingredient_type and ChEBI-derived chemistry
    are missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2e4736c37f4d61f0
    - ev-8bca3ac2d1d770a9
  - name: legacy-native-ids
    value: '["SEM:95c215d379a05ae77aa3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8bca3ac2d1d770a9
    - ev-2e4736c37f4d61f0
    - ev-3dfd44f0b72ef15a
findings:
- finding_id: rec-f-70fdf1d06d6a330a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1e2245c533d91954
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 2-Nitrophenol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:30:17Z;
    reviewed SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62;
    current SHA-256=a7129e0ed90f6ab1984acc26027154dec6ae075cb8d17788085c248e9bdbcc62;
    hash_changed=False. Reports=["reports/yaml_record_review/2-Nitrophenol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Residual CultureMech
    grounding to CHEBI:16260 passes, but ingredient_type and ChEBI-derived chemistry
    are missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1e2245c533d91954
  evidence_ids:
  - ev-2e4736c37f4d61f0
  - ev-8bca3ac2d1d770a9
  - ev-3dfd44f0b72ef15a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Nitrophenol.yaml
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
