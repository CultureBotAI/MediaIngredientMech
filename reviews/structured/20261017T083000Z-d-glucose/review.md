# Per-record structured review: D-glucose (data/ingredients/mapped/D-glucose.yaml)

- Review: 20261017T083000Z-d-glucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-glucose (data/ingredients/mapped/D-glucose.yaml, record-9642ca4960adff13, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-glucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-glucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9642ca4960adff13 | data/ingredients/mapped/D-glucose.yaml | maintained | D-glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9642ca4960adff13 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9642ca4960adff13 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9642ca4960adff13 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9642ca4960adff13.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9642ca4960adff13.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:43:33Z; reviewed SHA-256=dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914; current SHA-256=dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914; hash_changed=False. Reports=["reports/yaml_record_review/D-glucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, 1211-recipe CultureMech count, carbon role, and final SSSOM payload pass, but PubMed mapping evidence is unsupported and the energy role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-9642ca4960adff13.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e4a2fadb48488dd1: Reassess prediction-only role support: D-Glucose

major / open / confirmed; issue key: mim-reconciliation-role-support-9642ca4960adff13.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e4a2fadb48488dd1

Reassess prediction-only role support: D-Glucose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cbaca8b71ecfa34f | data/ingredients/mapped/D-glucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[835],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":837,"mapping_status":"MAPPED","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":1211,"total_occurrences":1250},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"D-Glucose","sssom_rows":[{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-glucose","synonym_count":11} |
| ev-5a04d050886024b6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [835] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c2ca78f3d1fdc45d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-glucose; data-row positions=[938] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","other":"D-(+)-glucose&#124;Traubenzucker&#124;D(+)-Glucose&#124;D-gluco-hexose&#124;Dextrose&#124;aldehydo-D-glucose&#124;CAS:50-99-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-glucose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-3f4e89a4109beb37 | docs/data/mapped_ingredients.csv; CSV lines=[837] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17634","line":837,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1211","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose","total_occurrences":"1250"}] |
| ev-c1f273204a5dee65 | reports/yaml_record_review/D-glucose.md; &#96;data/ingredients/mapped/D-glucose.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:40; Completeness:64; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d95e59087f8b2373 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[497,1914] | context_only | [{"current_record_sha256":"dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914","finding_id":"SEM:bdc0b484c8ff3683309d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914","finding_id":"SEM:2d09e53cd5bdcc853380","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-361647282f26c9ec | data/ingredients/mapped/D-glucose.yaml; nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[835],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":837,"mapping_status":"MAPPED","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":1211,"total_occurrences":1250},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"D-Glucose","sssom_rows":[{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-glucose","synonym_count":11} |
| ev-5dfdc7db02944c82 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-e4a2fadb48488dd1] | context_only | Predecessor structured review finding f-e4a2fadb48488dd1 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-glucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-glucose (data/ingredients/mapped/D-glucose.yaml)'
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
summary: Per-record structured review for D-glucose (data/ingredients/mapped/D-glucose.yaml,
  record-9642ca4960adff13, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-glucose.yaml
    sha256: dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-glucose.md
    sha256: 1e66f00ddfd9aad1b840260b8fe72a5e5b5ed81c3dec1fdb2f6e5a625638ca31
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9642ca4960adff13
  path: data/ingredients/mapped/D-glucose.yaml
  label: D-glucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-glucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-glucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-glucose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9642ca4960adff13
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-cbaca8b71ecfa34f
  - ev-5a04d050886024b6
  - ev-c2ca78f3d1fdc45d
  - ev-3f4e89a4109beb37
  - ev-361647282f26c9ec
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-cbaca8b71ecfa34f
  - ev-d95e59087f8b2373
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-c1f273204a5dee65
  - ev-d95e59087f8b2373
  - ev-5dfdc7db02944c82
evidence:
- evidence_id: ev-cbaca8b71ecfa34f
  kind: record_content
  reference: data/ingredients/mapped/D-glucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[835],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":837,"mapping_status":"MAPPED","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":1211,"total_occurrences":1250},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"D-Glucose","sssom_rows":[{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-glucose","synonym_count":11}'
  snapshot_sha256: dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914
- evidence_id: ev-5a04d050886024b6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [835]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c2ca78f3d1fdc45d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-glucose; data-row positions=[938]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","other":"D-(+)-glucose|Traubenzucker|D(+)-Glucose|D-gluco-hexose|Dextrose|aldehydo-D-glucose|CAS:50-99-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-glucose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3f4e89a4109beb37
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[837]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17634","line":837,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1211","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose","total_occurrences":"1250"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c1f273204a5dee65
  kind: prior_review
  reference: reports/yaml_record_review/D-glucose.md
  locator: '`data/ingredients/mapped/D-glucose.yaml`:2; Verdict:4; Identity:12; Validation:25;
    Evidence:40; Completeness:64; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1e66f00ddfd9aad1b840260b8fe72a5e5b5ed81c3dec1fdb2f6e5a625638ca31
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-glucose.yaml`, remove\
    \ PMID `33762358` from\n  `ontology_mapping.evidence` or replace it with evidence\
    \ that actually\n  supports the identity mapping to `CHEBI:17634`.\n- Remove the\
    \ provisional `ENERGY_SOURCE` role or replace its\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence with inspected claim-level evidence for\n  D-glucose as an energy source\
    \ in media.\n- Regenerate synchronized curated and SSSOM products, then rerun\n\
    \  `uv run --frozen python scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/D-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-d95e59087f8b2373
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[497,1914]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914","finding_id":"SEM:bdc0b484c8ff3683309d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914","finding_id":"SEM:2d09e53cd5bdcc853380","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-361647282f26c9ec
  kind: record_content
  reference: data/ingredients/mapped/D-glucose.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[835],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":837,"mapping_status":"MAPPED","ontology_id":"CHEBI:17634","preferred_term":"D-Glucose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":1211,"total_occurrences":1250},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"D-Glucose","sssom_rows":[{"data_row":938,"object_id":"CHEBI:17634","object_label":"D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-glucose","synonym_count":11}'
  snapshot_sha256: dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914
- evidence_id: ev-5dfdc7db02944c82
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-e4a2fadb48488dd1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e4a2fadb48488dd1 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-5833360438a1c099
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-cbaca8b71ecfa34f
  - ev-5a04d050886024b6
  - ev-c2ca78f3d1fdc45d
  - ev-3f4e89a4109beb37
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b706c0399ed907c9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-c1f273204a5dee65
  - ev-cbaca8b71ecfa34f
  - ev-d95e59087f8b2373
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:43:33Z;
    reviewed SHA-256=dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914;
    current SHA-256=dd603850555b5735acd54dcc6f4695a23a0d789b120d77000db239427bad0914;
    hash_changed=False. Reports=["reports/yaml_record_review/D-glucose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, 1211-recipe CultureMech count, carbon role, and final SSSOM payload
    pass, but PubMed mapping evidence is unsupported and the energy role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c1f273204a5dee65
    - ev-cbaca8b71ecfa34f
  - name: legacy-native-ids
    value: '["SEM:bdc0b484c8ff3683309d","SEM:2d09e53cd5bdcc853380"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cbaca8b71ecfa34f
    - ev-c1f273204a5dee65
    - ev-d95e59087f8b2373
- assessment_id: a-361647282f26c9ec
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-c1f273204a5dee65
  - ev-361647282f26c9ec
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c1f273204a5dee65
    - ev-361647282f26c9ec
findings:
- finding_id: rec-f-e4a2fadb48488dd1
  issue_key: mim-reconciliation-role-support-9642ca4960adff13
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Glucose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9642ca4960adff13
  evidence_ids:
  - ev-c1f273204a5dee65
  - ev-361647282f26c9ec
  - ev-5dfdc7db02944c82
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-glucose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-e4a2fadb48488dd1
actions:
- action_id: rec-action-e4a2fadb48488dd1
  description: 'Reassess prediction-only role support: D-Glucose'
  finding_ids:
  - rec-f-e4a2fadb48488dd1
  target_ids:
  - record-9642ca4960adff13
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-glucose.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
