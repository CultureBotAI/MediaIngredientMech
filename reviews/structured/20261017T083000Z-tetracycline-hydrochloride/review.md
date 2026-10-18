# Per-record structured review: Tetracycline_Hydrochloride (data/ingredients/mapped/Tetracycline_Hydrochloride.yaml)

- Review: 20261017T083000Z-tetracycline-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tetracycline_Hydrochloride (data/ingredients/mapped/Tetracycline_Hydrochloride.yaml, record-a2372de43f4e93d8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tetracycline_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tetracycline_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a2372de43f4e93d8 | data/ingredients/mapped/Tetracycline_Hydrochloride.yaml | maintained | Tetracycline_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a2372de43f4e93d8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a2372de43f4e93d8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a2372de43f4e93d8 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a2372de43f4e93d8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a2372de43f4e93d8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:11:59Z; reviewed SHA-256=1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409; current SHA-256=1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409; hash_changed=False. Reports=["reports/yaml_record_review/Tetracycline_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:35006 identity passes, but SELECTIVE_AGENT is still only a provisional computational name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-a2372de43f4e93d8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-38c3ba3d30fc1cdf: Reassess prediction-only role support: Tetracycline hydrochloride

major / open / confirmed; issue key: mim-reconciliation-role-support-a2372de43f4e93d8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-38c3ba3d30fc1cdf

Reassess prediction-only role support: Tetracycline hydrochloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0e1e6186cad39fb2 | data/ingredients/mapped/Tetracycline_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35006","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline hydrochloride"}],"identifier":"CHEBI:35006","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35006","ontology_label":"Tetracycline hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Tetracycline hydrochloride","sssom_rows":[{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline_Hydrochloride","synonym_count":0} |
| ev-b5ac2694e5b8a201 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1941] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-024bbaae02bbda8d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tetracycline_Hydrochloride; data-row positions=[2739] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline hydrochloride","other":"CAS:64-75-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tetracycline_Hydrochloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-f4657fa1420f84d7 | docs/data/mapped_ingredients.csv; CSV lines=[1943] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:35006","line":1943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline hydrochloride","total_occurrences":"0"}] |
| ev-5420c6780aaad434 | reports/yaml_record_review/Tetracycline_Hydrochloride.md; &#96;data/ingredients/mapped/Tetracycline_Hydrochloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:31; Completeness:45; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a085581ca12bae5f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1277,1741] | context_only | [{"current_record_sha256":"1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409","finding_id":"SEM:5eee8d7241f679b1e750","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409","finding_id":"SEM:1ebe0559d39f24ad8978","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-77a47a584c7d088a | data/ingredients/mapped/Tetracycline_Hydrochloride.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35006","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline hydrochloride"}],"identifier":"CHEBI:35006","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35006","ontology_label":"Tetracycline hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Tetracycline hydrochloride","sssom_rows":[{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline_Hydrochloride","synonym_count":0} |
| ev-b344633db54df23a | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-38c3ba3d30fc1cdf] | context_only | Predecessor structured review finding f-38c3ba3d30fc1cdf in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tetracycline-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tetracycline_Hydrochloride (data/ingredients/mapped/Tetracycline_Hydrochloride.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Tetracycline_Hydrochloride (data/ingredients/mapped/Tetracycline_Hydrochloride.yaml,
  record-a2372de43f4e93d8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    sha256: 1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409
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
  - path: reports/yaml_record_review/Tetracycline_Hydrochloride.md
    sha256: 2d98cc563536f8435e556d915d2e6f1868b423895330d9b70ffd692908186977
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a2372de43f4e93d8
  path: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
  label: Tetracycline_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a2372de43f4e93d8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-0e1e6186cad39fb2
  - ev-b5ac2694e5b8a201
  - ev-024bbaae02bbda8d
  - ev-f4657fa1420f84d7
  - ev-77a47a584c7d088a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-0e1e6186cad39fb2
  - ev-a085581ca12bae5f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-5420c6780aaad434
  - ev-a085581ca12bae5f
  - ev-b344633db54df23a
evidence:
- evidence_id: ev-0e1e6186cad39fb2
  kind: record_content
  reference: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35006","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline
    hydrochloride"}],"identifier":"CHEBI:35006","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35006","ontology_label":"Tetracycline
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Tetracycline hydrochloride","sssom_rows":[{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline_Hydrochloride","synonym_count":0}'
  snapshot_sha256: 1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409
- evidence_id: ev-b5ac2694e5b8a201
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1941]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-024bbaae02bbda8d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tetracycline_Hydrochloride; data-row positions=[2739]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline
    hydrochloride","other":"CAS:64-75-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Tetracycline_Hydrochloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f4657fa1420f84d7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1943]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:35006","line":1943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline
    hydrochloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5420c6780aaad434
  kind: prior_review
  reference: reports/yaml_record_review/Tetracycline_Hydrochloride.md
  locator: '`data/ingredients/mapped/Tetracycline_Hydrochloride.yaml`:2; Verdict:4;
    Identity:10; Validation:22; Evidence:31; Completeness:45; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2d98cc563536f8435e556d915d2e6f1868b423895330d9b70ffd692908186977
  quote: "Recommended Edits:\n- Major: replace the provisional name-pattern `SELECTIVE_AGENT`\
    \ role in\n  `data/ingredients/mapped/Tetracycline_Hydrochloride.yaml` with source-backed\n\
    \  evidence for tetracycline hydrochloride as a selective agent, or remove the\n\
    \  role if no maintained source supports it.\n- Major: after any role edit, synchronize\
    \ `data/curated/mapped_ingredients.yaml`\n  and regenerate generated products\
    \ so the role facets match the per-record\n  YAML."
- evidence_id: ev-a085581ca12bae5f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1277,1741]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409","finding_id":"SEM:5eee8d7241f679b1e750","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409","finding_id":"SEM:1ebe0559d39f24ad8978","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-77a47a584c7d088a
  kind: record_content
  reference: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35006","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:35006","preferred_term":"Tetracycline
    hydrochloride"}],"identifier":"CHEBI:35006","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:35006","ontology_label":"Tetracycline
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Tetracycline hydrochloride","sssom_rows":[{"data_row":2739,"object_id":"CHEBI:35006","object_label":"Tetracycline
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline_Hydrochloride","synonym_count":0}'
  snapshot_sha256: 1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409
- evidence_id: ev-b344633db54df23a
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-38c3ba3d30fc1cdf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-38c3ba3d30fc1cdf in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-b8554530aac02802
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-0e1e6186cad39fb2
  - ev-b5ac2694e5b8a201
  - ev-024bbaae02bbda8d
  - ev-f4657fa1420f84d7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e98bac30371122cc
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-5420c6780aaad434
  - ev-0e1e6186cad39fb2
  - ev-a085581ca12bae5f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:11:59Z;
    reviewed SHA-256=1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409;
    current SHA-256=1c65b35e3fe29bf2211a458a339c7cade9e4f6de2d3ad02066d2abef6753f409;
    hash_changed=False. Reports=["reports/yaml_record_review/Tetracycline_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:35006 identity passes, but SELECTIVE_AGENT is still only a provisional computational
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5420c6780aaad434
    - ev-0e1e6186cad39fb2
  - name: legacy-native-ids
    value: '["SEM:5eee8d7241f679b1e750","SEM:1ebe0559d39f24ad8978"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0e1e6186cad39fb2
    - ev-5420c6780aaad434
    - ev-a085581ca12bae5f
- assessment_id: a-77a47a584c7d088a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-5420c6780aaad434
  - ev-77a47a584c7d088a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5420c6780aaad434
    - ev-77a47a584c7d088a
findings:
- finding_id: rec-f-38c3ba3d30fc1cdf
  issue_key: mim-reconciliation-role-support-a2372de43f4e93d8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tetracycline hydrochloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a2372de43f4e93d8
  evidence_ids:
  - ev-5420c6780aaad434
  - ev-77a47a584c7d088a
  - ev-b344633db54df23a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-38c3ba3d30fc1cdf
actions:
- action_id: rec-action-38c3ba3d30fc1cdf
  description: 'Reassess prediction-only role support: Tetracycline hydrochloride'
  finding_ids:
  - rec-f-38c3ba3d30fc1cdf
  target_ids:
  - record-a2372de43f4e93d8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline_Hydrochloride.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
