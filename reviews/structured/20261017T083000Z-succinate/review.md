# Per-record structured review: Succinate (data/ingredients/mapped/Succinate.yaml)

- Review: 20261017T083000Z-succinate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Succinate (data/ingredients/mapped/Succinate.yaml, record-a21243d59bace146, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Succinate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Succinate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a21243d59bace146 | data/ingredients/mapped/Succinate.yaml | maintained | Succinate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a21243d59bace146 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a21243d59bace146 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a21243d59bace146 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a21243d59bace146.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a21243d59bace146.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z; reviewed SHA-256=346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e; current SHA-256=346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e; hash_changed=False. Reports=["reports/yaml_record_review/Succinate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The broad CHEBI:26806 identity passes, but salt-specific Na Succinate synonyms and provisional roles need curation.

### Historical provisional-role concern

evidence: concern. Targets: record-a21243d59bace146.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e3e251c7ec571381: Reassess prediction-only role support: Succinate

major / open / confirmed; issue key: mim-reconciliation-role-support-a21243d59bace146.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e3e251c7ec571381

Reassess prediction-only role support: Succinate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1b6c64739f021ea7 | data/ingredients/mapped/Succinate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26806","line":1907,"mapping_status":"MAPPED","ontology_id":"CHEBI:26806","preferred_term":"Succinate"}],"identifier":"CHEBI:26806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26806","ontology_label":"succinate","ontology_source":"CHEBI"},"preferred_term":"Succinate","sssom_rows":[{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinate","synonym_count":7} |
| ev-0b9e4c55d4996e3c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1905] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-26c0a9bb3dbd0095 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Succinate; data-row positions=[2662] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","other":"Na Succinate&#124;Na-succinate&#124;succinate anion&#124;succinates&#124;succinic acid anion&#124;CAS:56-14-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Succinate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f7be35d4fc307016 | docs/data/mapped_ingredients.csv; CSV lines=[1907] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26806","line":1907,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"CHEBI:26806","preferred_term":"Succinate","total_occurrences":"20"}] |
| ev-2fe0bd1554ed0497 | reports/yaml_record_review/Succinate.md; &#96;data/ingredients/mapped/Succinate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:29; Completeness:46; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-99768b5ac138ce3c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1254,1974,2074] | context_only | [{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:cb3cbcf83e9ae1862c41","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:c597f35bf5d1178fbf47","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:543221423de77c9ed268","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1b694cef0914ee02 | data/ingredients/mapped/Succinate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26806","line":1907,"mapping_status":"MAPPED","ontology_id":"CHEBI:26806","preferred_term":"Succinate"}],"identifier":"CHEBI:26806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26806","ontology_label":"succinate","ontology_source":"CHEBI"},"preferred_term":"Succinate","sssom_rows":[{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinate","synonym_count":7} |
| ev-c899852b887bc89b | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-e3e251c7ec571381] | context_only | Predecessor structured review finding f-e3e251c7ec571381 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-succinate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Succinate (data/ingredients/mapped/Succinate.yaml)'
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
summary: Per-record structured review for Succinate (data/ingredients/mapped/Succinate.yaml,
  record-a21243d59bace146, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Succinate.yaml
    sha256: 346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e
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
  - path: reports/yaml_record_review/Succinate.md
    sha256: 6601cc064bdfd7c2cae1279dacfde465dd34d30a4c4c9a11e9126af58737d626
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a21243d59bace146
  path: data/ingredients/mapped/Succinate.yaml
  label: Succinate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Succinate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Succinate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a21243d59bace146
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-1b6c64739f021ea7
  - ev-0b9e4c55d4996e3c
  - ev-26c0a9bb3dbd0095
  - ev-f7be35d4fc307016
  - ev-1b694cef0914ee02
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-1b6c64739f021ea7
  - ev-99768b5ac138ce3c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-2fe0bd1554ed0497
  - ev-99768b5ac138ce3c
  - ev-c899852b887bc89b
evidence:
- evidence_id: ev-1b6c64739f021ea7
  kind: record_content
  reference: data/ingredients/mapped/Succinate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26806","line":1907,"mapping_status":"MAPPED","ontology_id":"CHEBI:26806","preferred_term":"Succinate"}],"identifier":"CHEBI:26806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26806","ontology_label":"succinate","ontology_source":"CHEBI"},"preferred_term":"Succinate","sssom_rows":[{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinate","synonym_count":7}'
  snapshot_sha256: 346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e
- evidence_id: ev-0b9e4c55d4996e3c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1905]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-26c0a9bb3dbd0095
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Succinate; data-row positions=[2662]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","other":"Na
    Succinate|Na-succinate|succinate anion|succinates|succinic acid anion|CAS:56-14-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Succinate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f7be35d4fc307016
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1907]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26806","line":1907,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"CHEBI:26806","preferred_term":"Succinate","total_occurrences":"20"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2fe0bd1554ed0497
  kind: prior_review
  reference: reports/yaml_record_review/Succinate.md
  locator: '`data/ingredients/mapped/Succinate.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:29; Completeness:46; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6601cc064bdfd7c2cae1279dacfde465dd34d30a4c4c9a11e9126af58737d626
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Succinate.yaml`,\
    \ retype or remove the\n  `Na Succinate` and `Na-succinate` synonyms so the final\
    \ SSSOM `other` column\n  only exports names for the `CHEBI:26806` subject.\n\
    - Major: either replace the provisional `CARBON_SOURCE` and `ENERGY_SOURCE`\n\
    \  assertions with inspected CultureMech or literature evidence, or remove\n \
    \ those role facets."
- evidence_id: ev-99768b5ac138ce3c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1254,1974,2074]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:cb3cbcf83e9ae1862c41","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:c597f35bf5d1178fbf47","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e","finding_id":"SEM:543221423de77c9ed268","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1b694cef0914ee02
  kind: record_content
  reference: data/ingredients/mapped/Succinate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26806","line":1907,"mapping_status":"MAPPED","ontology_id":"CHEBI:26806","preferred_term":"Succinate"}],"identifier":"CHEBI:26806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26806","ontology_label":"succinate","ontology_source":"CHEBI"},"preferred_term":"Succinate","sssom_rows":[{"data_row":2662,"object_id":"CHEBI:26806","object_label":"succinate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Succinate","synonym_count":7}'
  snapshot_sha256: 346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e
- evidence_id: ev-c899852b887bc89b
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-e3e251c7ec571381]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e3e251c7ec571381 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-140ba52d6bef555a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-1b6c64739f021ea7
  - ev-0b9e4c55d4996e3c
  - ev-26c0a9bb3dbd0095
  - ev-f7be35d4fc307016
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c80cd38ef0726e68
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-2fe0bd1554ed0497
  - ev-1b6c64739f021ea7
  - ev-99768b5ac138ce3c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z;
    reviewed SHA-256=346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e;
    current SHA-256=346f46e1a132bfa853f83b0742412721982ec60b5d53107c818e21a61d10341e;
    hash_changed=False. Reports=["reports/yaml_record_review/Succinate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The broad CHEBI:26806
    identity passes, but salt-specific Na Succinate synonyms and provisional roles
    need curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2fe0bd1554ed0497
    - ev-1b6c64739f021ea7
  - name: legacy-native-ids
    value: '["SEM:cb3cbcf83e9ae1862c41","SEM:c597f35bf5d1178fbf47","SEM:543221423de77c9ed268"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1b6c64739f021ea7
    - ev-2fe0bd1554ed0497
    - ev-99768b5ac138ce3c
- assessment_id: a-1b694cef0914ee02
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-2fe0bd1554ed0497
  - ev-1b694cef0914ee02
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2fe0bd1554ed0497
    - ev-1b694cef0914ee02
findings:
- finding_id: rec-f-e3e251c7ec571381
  issue_key: mim-reconciliation-role-support-a21243d59bace146
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Succinate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a21243d59bace146
  evidence_ids:
  - ev-2fe0bd1554ed0497
  - ev-1b694cef0914ee02
  - ev-c899852b887bc89b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-e3e251c7ec571381
actions:
- action_id: rec-action-e3e251c7ec571381
  description: 'Reassess prediction-only role support: Succinate'
  finding_ids:
  - rec-f-e3e251c7ec571381
  target_ids:
  - record-a21243d59bace146
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Succinate.yaml
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
