# Per-record structured review: Calcium_Pantothenate (data/ingredients/mapped/Calcium_Pantothenate.yaml)

- Review: 20261017T083000Z-calcium-pantothenate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Calcium_Pantothenate (data/ingredients/mapped/Calcium_Pantothenate.yaml, record-3a3d3166b2faac3e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Calcium_Pantothenate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Calcium_Pantothenate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3a3d3166b2faac3e | data/ingredients/mapped/Calcium_Pantothenate.yaml | maintained | Calcium_Pantothenate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3a3d3166b2faac3e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3a3d3166b2faac3e | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3a3d3166b2faac3e | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3a3d3166b2faac3e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3a3d3166b2faac3e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:42:55Z; reviewed SHA-256=b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121; current SHA-256=b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121; hash_changed=False. Reports=["reports/yaml_record_review/Calcium_Pantothenate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact calcium pantothenate identity passes, but four capsaicin/Zostrix aliases remain published as calcium pantothenate synonyms.

### Historical provisional-role concern

evidence: concern. Targets: record-3a3d3166b2faac3e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-738d3bc5b68a247c: Reassess prediction-only role support: Calcium pantothenate

major / open / confirmed; issue key: mim-reconciliation-role-support-3a3d3166b2faac3e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-738d3bc5b68a247c

Reassess prediction-only role support: Calcium pantothenate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2031934e6103ac89 | data/ingredients/mapped/Calcium_Pantothenate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[636],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31345","line":638,"mapping_status":"MAPPED","ontology_id":"CHEBI:31345","preferred_term":"Calcium pantothenate"}],"identifier":"CHEBI:31345","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2348,"edge_count":2348,"occurrences":2375},"occurrence_statistics":{"media_count":2348,"total_occurrences":2375},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31345","ontology_label":"Calcium pantothenate","ontology_source":"CHEBI"},"preferred_term":"Calcium pantothenate","sssom_rows":[{"data_row":617,"object_id":"CHEBI:31345","object_label":"Calcium pantothenate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Calcium_Pantothenate","synonym_count":19} |
| ev-3e857d7d5b90de58 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [636] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d294c577ddb09e03 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Calcium_Pantothenate; data-row positions=[617] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":617,"object_id":"CHEBI:31345","object_label":"Calcium pantothenate","other":"Calcium D-(+)-pantothenate&#124;D-Ca-pantothenate&#124;D Calcium Panthothenate&#124;D-Calcium pantothenate&#124;DL-Calcium pantothenate&#124;Hemicalcium D-(+)- pantothenate&#124;calcium D,L-pantothenate&#124;Calcium\u00a0pantothenate&#124;Hemicalcium D-+-pantothenate&#124;Calcium panthothenate&#124;Calcium D-Pantothenate&#124;Ca-pantothenate&#124;(E)-8-Methyl-N-vanillyl-6-nonenamide&#124;Isodecenoic acid vanillylamide&#124;Zostrix&#124;trans-8-Methyl-N-vanillyl-6-nonenamide&#124;CAS:137-08-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Calcium_Pantothenate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-e17b3bee6daeeb30 | docs/data/mapped_ingredients.csv; CSV lines=[638] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31345","line":638,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2348","ontology_id":"CHEBI:31345","preferred_term":"Calcium pantothenate","total_occurrences":"2375"}] |
| ev-3e8696b83799797c | reports/yaml_record_review/Calcium_Pantothenate.md; &#96;data/ingredients/mapped/Calcium_Pantothenate.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:41; Completeness:58; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e2f6aa5493c75c4f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[349,1801] | context_only | [{"current_record_sha256":"b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121","finding_id":"SEM:829062594b65f0a11861","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121","finding_id":"SEM:6db6f9f9537ce057d55b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2fe3f5e45c843392 | data/ingredients/mapped/Calcium_Pantothenate.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"VITAMIN_SOURCE"}}] |
| ev-dfd776d67622aca9 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-738d3bc5b68a247c] | context_only | Predecessor structured review finding f-738d3bc5b68a247c in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-calcium-pantothenate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Calcium_Pantothenate (data/ingredients/mapped/Calcium_Pantothenate.yaml)'
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
summary: Per-record structured review for Calcium_Pantothenate (data/ingredients/mapped/Calcium_Pantothenate.yaml,
  record-3a3d3166b2faac3e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Calcium_Pantothenate.yaml
    sha256: b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121
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
  - path: reports/yaml_record_review/Calcium_Pantothenate.md
    sha256: 0567d0dbf3e12b79aa0da07faf5e055432fb18ff57e541d42f900ab926562ec8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3a3d3166b2faac3e
  path: data/ingredients/mapped/Calcium_Pantothenate.yaml
  label: Calcium_Pantothenate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calcium_Pantothenate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Calcium_Pantothenate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Calcium_Pantothenate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3a3d3166b2faac3e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3a3d3166b2faac3e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3a3d3166b2faac3e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3a3d3166b2faac3e
evidence:
- evidence_id: ev-2031934e6103ac89
  kind: record_content
  reference: data/ingredients/mapped/Calcium_Pantothenate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[636],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31345","line":638,"mapping_status":"MAPPED","ontology_id":"CHEBI:31345","preferred_term":"Calcium
    pantothenate"}],"identifier":"CHEBI:31345","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2348,"edge_count":2348,"occurrences":2375},"occurrence_statistics":{"media_count":2348,"total_occurrences":2375},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31345","ontology_label":"Calcium
    pantothenate","ontology_source":"CHEBI"},"preferred_term":"Calcium pantothenate","sssom_rows":[{"data_row":617,"object_id":"CHEBI:31345","object_label":"Calcium
    pantothenate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Calcium_Pantothenate","synonym_count":19}'
  snapshot_sha256: b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121
- evidence_id: ev-3e857d7d5b90de58
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [636]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d294c577ddb09e03
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Calcium_Pantothenate; data-row positions=[617]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":617,"object_id":"CHEBI:31345","object_label":"Calcium
    pantothenate","other":"Calcium D-(+)-pantothenate|D-Ca-pantothenate|D Calcium
    Panthothenate|D-Calcium pantothenate|DL-Calcium pantothenate|Hemicalcium D-(+)-
    pantothenate|calcium D,L-pantothenate|Calcium\u00a0pantothenate|Hemicalcium D-+-pantothenate|Calcium
    panthothenate|Calcium D-Pantothenate|Ca-pantothenate|(E)-8-Methyl-N-vanillyl-6-nonenamide|Isodecenoic
    acid vanillylamide|Zostrix|trans-8-Methyl-N-vanillyl-6-nonenamide|CAS:137-08-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Calcium_Pantothenate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e17b3bee6daeeb30
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[638]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31345","line":638,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2348","ontology_id":"CHEBI:31345","preferred_term":"Calcium
    pantothenate","total_occurrences":"2375"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3e8696b83799797c
  kind: prior_review
  reference: reports/yaml_record_review/Calcium_Pantothenate.md
  locator: '`data/ingredients/mapped/Calcium_Pantothenate.yaml`:2; Verdict:4; Identity:11;
    Validation:26; Evidence:41; Completeness:58; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0567d0dbf3e12b79aa0da07faf5e055432fb18ff57e541d42f900ab926562ec8
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Calcium_Pantothenate.yaml`,\
    \ remove the four\n  `sssom_other_backfill` aliases that denote capsaicin/Zostrix,\
    \ then trace the\n  #520 backfill source to decide whether those labels belong\
    \ on the capsaicin\n  record or should simply disappear.\n- Remove the redundant\
    \ 0.8 `VITAMIN_SOURCE` role inherited from\n  `Calcium_D-Pantothenate`; the 1.0\
    \ CultureMech-supported role is sufficient.\n- Regenerate `data/curated/mapped_ingredients.yaml`,\n\
    \  `mappings/ingredient_mappings.sssom.tsv`, docs data, and label indexes; prove\n\
    \  the cleanup with strict validation, round-trip verification, and\n  `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-e2f6aa5493c75c4f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[349,1801]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121","finding_id":"SEM:829062594b65f0a11861","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121","finding_id":"SEM:6db6f9f9537ce057d55b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2fe3f5e45c843392
  kind: record_content
  reference: data/ingredients/mapped/Calcium_Pantothenate.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"VITAMIN_SOURCE"}}]'
  snapshot_sha256: b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121
- evidence_id: ev-dfd776d67622aca9
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-738d3bc5b68a247c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-738d3bc5b68a247c in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-29a997a7057e2ce7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3a3d3166b2faac3e
  evidence_ids:
  - ev-2031934e6103ac89
  - ev-3e857d7d5b90de58
  - ev-d294c577ddb09e03
  - ev-e17b3bee6daeeb30
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-17bc0e0540c325a5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3a3d3166b2faac3e
  evidence_ids:
  - ev-3e8696b83799797c
  - ev-2031934e6103ac89
  - ev-e2f6aa5493c75c4f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:42:55Z;
    reviewed SHA-256=b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121;
    current SHA-256=b5a2eb0063046ecb71d2e9a97285aaebbf5780075f0fb0b7b069b4362bf57121;
    hash_changed=False. Reports=["reports/yaml_record_review/Calcium_Pantothenate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    calcium pantothenate identity passes, but four capsaicin/Zostrix aliases remain
    published as calcium pantothenate synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3e8696b83799797c
    - ev-2031934e6103ac89
  - name: legacy-native-ids
    value: '["SEM:829062594b65f0a11861","SEM:6db6f9f9537ce057d55b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2031934e6103ac89
    - ev-3e8696b83799797c
    - ev-e2f6aa5493c75c4f
- assessment_id: a-2fe3f5e45c843392
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3a3d3166b2faac3e
  evidence_ids:
  - ev-3e8696b83799797c
  - ev-2fe3f5e45c843392
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3e8696b83799797c
    - ev-2fe3f5e45c843392
findings:
- finding_id: rec-f-738d3bc5b68a247c
  issue_key: mim-reconciliation-role-support-3a3d3166b2faac3e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Calcium pantothenate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3a3d3166b2faac3e
  evidence_ids:
  - ev-3e8696b83799797c
  - ev-2fe3f5e45c843392
  - ev-dfd776d67622aca9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calcium_Pantothenate.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-738d3bc5b68a247c
actions:
- action_id: rec-action-738d3bc5b68a247c
  description: 'Reassess prediction-only role support: Calcium pantothenate'
  finding_ids:
  - rec-f-738d3bc5b68a247c
  target_ids:
  - record-3a3d3166b2faac3e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calcium_Pantothenate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
