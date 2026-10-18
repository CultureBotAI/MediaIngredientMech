# Per-record structured review: Danubomycin (data/ingredients/mapped/Danubomycin.yaml)

- Review: 20261017T083000Z-danubomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Danubomycin (data/ingredients/mapped/Danubomycin.yaml, record-61f523d1b9024d6a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Danubomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Danubomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-61f523d1b9024d6a | data/ingredients/mapped/Danubomycin.yaml | maintained | Danubomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-61f523d1b9024d6a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-61f523d1b9024d6a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-61f523d1b9024d6a | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-61f523d1b9024d6a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-61f523d1b9024d6a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:09:27Z; reviewed SHA-256=0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c; current SHA-256=0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c; hash_changed=False. Reports=["reports/yaml_record_review/Danubomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local placeholder still has no live OLS exact replacement, but its selective-agent role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-61f523d1b9024d6a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-dba58fe26c7d5bdd: Reassess prediction-only role support: Danubomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-61f523d1b9024d6a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-dba58fe26c7d5bdd

Reassess prediction-only role support: Danubomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-87810972cf9a7d22 | data/ingredients/mapped/Danubomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[862],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin"}],"identifier":"kgmicrobe.compound:danubomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:danubomycin","ontology_label":"Danubomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Danubomycin","sssom_rows":[{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Danubomycin","synonym_count":0} |
| ev-ffa082a7f4727ef1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [862] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-db79f829c22ca69e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Danubomycin; data-row positions=[999] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Danubomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f8152049f1148da1 | docs/data/mapped_ingredients.csv; CSV lines=[864] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin","total_occurrences":"0"}] |
| ev-d539b00e5b6690e2 | reports/yaml_record_review/Danubomycin.md; &#96;data/ingredients/mapped/Danubomycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:41; Completeness:57; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c0366eb936b1aa01 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[521,1438] | context_only | [{"current_record_sha256":"0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c","finding_id":"SEM:a1a7feed779894aafb2c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c","finding_id":"SEM:215f2857ba29fa4bc054","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5329d229db7b77f3 | data/ingredients/mapped/Danubomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[862],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin"}],"identifier":"kgmicrobe.compound:danubomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:danubomycin","ontology_label":"Danubomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Danubomycin","sssom_rows":[{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Danubomycin","synonym_count":0} |
| ev-6297608436738443 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-dba58fe26c7d5bdd] | context_only | Predecessor structured review finding f-dba58fe26c7d5bdd in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-danubomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Danubomycin (data/ingredients/mapped/Danubomycin.yaml)'
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
summary: Per-record structured review for Danubomycin (data/ingredients/mapped/Danubomycin.yaml,
  record-61f523d1b9024d6a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Danubomycin.yaml
    sha256: 0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c
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
  - path: reports/yaml_record_review/Danubomycin.md
    sha256: 9b319188737cdeeb1746813618a8a3329b92b637074ae3032175624e30e77bd8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-61f523d1b9024d6a
  path: data/ingredients/mapped/Danubomycin.yaml
  label: Danubomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Danubomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Danubomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Danubomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-61f523d1b9024d6a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-87810972cf9a7d22
  - ev-ffa082a7f4727ef1
  - ev-db79f829c22ca69e
  - ev-f8152049f1148da1
  - ev-5329d229db7b77f3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-87810972cf9a7d22
  - ev-c0366eb936b1aa01
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-d539b00e5b6690e2
  - ev-c0366eb936b1aa01
  - ev-6297608436738443
evidence:
- evidence_id: ev-87810972cf9a7d22
  kind: record_content
  reference: data/ingredients/mapped/Danubomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[862],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin"}],"identifier":"kgmicrobe.compound:danubomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:danubomycin","ontology_label":"Danubomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Danubomycin","sssom_rows":[{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Danubomycin","synonym_count":0}'
  snapshot_sha256: 0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c
- evidence_id: ev-ffa082a7f4727ef1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [862]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-db79f829c22ca69e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Danubomycin; data-row positions=[999]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Danubomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f8152049f1148da1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[864]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d539b00e5b6690e2
  kind: prior_review
  reference: reports/yaml_record_review/Danubomycin.md
  locator: '`data/ingredients/mapped/Danubomycin.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:41; Completeness:57; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9b319188737cdeeb1746813618a8a3329b92b637074ae3032175624e30e77bd8
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Danubomycin.yaml`, remove\
    \ the provisional\n  `SELECTIVE_AGENT` role or replace its `COMPUTATIONAL_PREDICTION`\
    \ evidence\n  with inspected claim-level evidence for this compound.\n- Regenerate\
    \ synchronized curated and SSSOM products, then rerun\n  `uv run --frozen python\
    \ scripts/validate_strict.py`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-c0366eb936b1aa01
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[521,1438]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c","finding_id":"SEM:a1a7feed779894aafb2c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c","finding_id":"SEM:215f2857ba29fa4bc054","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5329d229db7b77f3
  kind: record_content
  reference: data/ingredients/mapped/Danubomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[862],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:danubomycin","line":864,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:danubomycin","preferred_term":"Danubomycin"}],"identifier":"kgmicrobe.compound:danubomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:danubomycin","ontology_label":"Danubomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Danubomycin","sssom_rows":[{"data_row":999,"object_id":"kgmicrobe.compound:danubomycin","object_label":"Danubomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Danubomycin","synonym_count":0}'
  snapshot_sha256: 0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c
- evidence_id: ev-6297608436738443
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-dba58fe26c7d5bdd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-dba58fe26c7d5bdd in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-ea18c729d5ee099e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-87810972cf9a7d22
  - ev-ffa082a7f4727ef1
  - ev-db79f829c22ca69e
  - ev-f8152049f1148da1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-085faaca2fdf61a1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-d539b00e5b6690e2
  - ev-87810972cf9a7d22
  - ev-c0366eb936b1aa01
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:09:27Z;
    reviewed SHA-256=0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c;
    current SHA-256=0d90522f7559d33a8c25a8701006ac82bb817e50f2965bf91c584882c8bb8c1c;
    hash_changed=False. Reports=["reports/yaml_record_review/Danubomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local placeholder
    still has no live OLS exact replacement, but its selective-agent role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d539b00e5b6690e2
    - ev-87810972cf9a7d22
  - name: legacy-native-ids
    value: '["SEM:a1a7feed779894aafb2c","SEM:215f2857ba29fa4bc054"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-87810972cf9a7d22
    - ev-d539b00e5b6690e2
    - ev-c0366eb936b1aa01
- assessment_id: a-5329d229db7b77f3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-d539b00e5b6690e2
  - ev-5329d229db7b77f3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d539b00e5b6690e2
    - ev-5329d229db7b77f3
findings:
- finding_id: rec-f-dba58fe26c7d5bdd
  issue_key: mim-reconciliation-role-support-61f523d1b9024d6a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Danubomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-61f523d1b9024d6a
  evidence_ids:
  - ev-d539b00e5b6690e2
  - ev-5329d229db7b77f3
  - ev-6297608436738443
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Danubomycin.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-dba58fe26c7d5bdd
actions:
- action_id: rec-action-dba58fe26c7d5bdd
  description: 'Reassess prediction-only role support: Danubomycin'
  finding_ids:
  - rec-f-dba58fe26c7d5bdd
  target_ids:
  - record-61f523d1b9024d6a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Danubomycin.yaml
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
