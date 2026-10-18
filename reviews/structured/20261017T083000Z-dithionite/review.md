# Per-record structured review: Dithionite (data/ingredients/mapped/Dithionite.yaml)

- Review: 20261017T083000Z-dithionite
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dithionite (data/ingredients/mapped/Dithionite.yaml, record-694992ca37b2f0da, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dithionite.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dithionite.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-694992ca37b2f0da | data/ingredients/mapped/Dithionite.yaml | maintained | Dithionite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-694992ca37b2f0da | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-694992ca37b2f0da | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-694992ca37b2f0da | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-694992ca37b2f0da.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-694992ca37b2f0da.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:06:45Z; reviewed SHA-256=223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5; current SHA-256=223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5; hash_changed=False. Reports=["reports/yaml_record_review/Dithionite.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI identity passes, but the reducing-agent role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-694992ca37b2f0da.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d6c3db291eeeb06e: Reassess prediction-only role support: Dithionite

major / open / confirmed; issue key: mim-reconciliation-role-support-694992ca37b2f0da.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d6c3db291eeeb06e

Reassess prediction-only role support: Dithionite

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5dd82ce950054d1a | data/ingredients/mapped/Dithionite.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[908],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42160","line":910,"mapping_status":"MAPPED","ontology_id":"CHEBI:42160","preferred_term":"Dithionite"}],"identifier":"CHEBI:42160","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:42160","ontology_label":"dithionite(2-)","ontology_source":"CHEBI"},"preferred_term":"Dithionite","sssom_rows":[{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dithionite","synonym_count":4} |
| ev-2af72a6b7a3f4090 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [908] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7e51904654942cbe | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dithionite; data-row positions=[1070] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","other":"Dithionit&#124;2,3-dioxido-1,4-dioxy-2,3-disulfy-[4]catenate(2-)&#124;bis(dioxidosulfate)(S--S)(2-)&#124;CAS:14844-07-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Dithionite","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-9df1dd08049d305a | docs/data/mapped_ingredients.csv; CSV lines=[910] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:42160","line":910,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:42160","preferred_term":"Dithionite","total_occurrences":"2"}] |
| ev-98e6a7f8b035ec98 | reports/yaml_record_review/Dithionite.md; &#96;data/ingredients/mapped/Dithionite.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:38; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0b0deca360983b4e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[547,1593] | context_only | [{"current_record_sha256":"223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5","finding_id":"SEM:a59560c272178568a085","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5","finding_id":"SEM:aa0a0d4b641e42005edf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a28d2993b84ed8b4 | data/ingredients/mapped/Dithionite.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[908],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42160","line":910,"mapping_status":"MAPPED","ontology_id":"CHEBI:42160","preferred_term":"Dithionite"}],"identifier":"CHEBI:42160","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:42160","ontology_label":"dithionite(2-)","ontology_source":"CHEBI"},"preferred_term":"Dithionite","sssom_rows":[{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dithionite","synonym_count":4} |
| ev-f42242f6da190885 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-d6c3db291eeeb06e] | context_only | Predecessor structured review finding f-d6c3db291eeeb06e in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dithionite
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dithionite (data/ingredients/mapped/Dithionite.yaml)'
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
summary: Per-record structured review for Dithionite (data/ingredients/mapped/Dithionite.yaml,
  record-694992ca37b2f0da, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dithionite.yaml
    sha256: 223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5
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
  - path: reports/yaml_record_review/Dithionite.md
    sha256: d7c00c4148d4e8a545a1c15743ee422f7ed5d8ddc4fc923d8e63abaf80790f91
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-694992ca37b2f0da
  path: data/ingredients/mapped/Dithionite.yaml
  label: Dithionite
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dithionite.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dithionite.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dithionite.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-694992ca37b2f0da
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-5dd82ce950054d1a
  - ev-2af72a6b7a3f4090
  - ev-7e51904654942cbe
  - ev-9df1dd08049d305a
  - ev-a28d2993b84ed8b4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-5dd82ce950054d1a
  - ev-0b0deca360983b4e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-98e6a7f8b035ec98
  - ev-0b0deca360983b4e
  - ev-f42242f6da190885
evidence:
- evidence_id: ev-5dd82ce950054d1a
  kind: record_content
  reference: data/ingredients/mapped/Dithionite.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[908],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42160","line":910,"mapping_status":"MAPPED","ontology_id":"CHEBI:42160","preferred_term":"Dithionite"}],"identifier":"CHEBI:42160","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:42160","ontology_label":"dithionite(2-)","ontology_source":"CHEBI"},"preferred_term":"Dithionite","sssom_rows":[{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dithionite","synonym_count":4}'
  snapshot_sha256: 223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5
- evidence_id: ev-2af72a6b7a3f4090
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [908]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7e51904654942cbe
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dithionite; data-row positions=[1070]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","other":"Dithionit|2,3-dioxido-1,4-dioxy-2,3-disulfy-[4]catenate(2-)|bis(dioxidosulfate)(S--S)(2-)|CAS:14844-07-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Dithionite","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9df1dd08049d305a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[910]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:42160","line":910,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:42160","preferred_term":"Dithionite","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-98e6a7f8b035ec98
  kind: prior_review
  reference: reports/yaml_record_review/Dithionite.md
  locator: '`data/ingredients/mapped/Dithionite.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:38; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d7c00c4148d4e8a545a1c15743ee422f7ed5d8ddc4fc923d8e63abaf80790f91
  quote: "Recommended Edits:\n- Major: replace the `REDUCING_AGENT` computational\
    \ role in\n  `data/ingredients/mapped/Dithionite.yaml` with source-backed role\
    \ evidence\n  scoped to dithionite, or remove the role if no support is available;\
    \ then\n  synchronize `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-0b0deca360983b4e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[547,1593]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5","finding_id":"SEM:a59560c272178568a085","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5","finding_id":"SEM:aa0a0d4b641e42005edf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a28d2993b84ed8b4
  kind: record_content
  reference: data/ingredients/mapped/Dithionite.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[908],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42160","line":910,"mapping_status":"MAPPED","ontology_id":"CHEBI:42160","preferred_term":"Dithionite"}],"identifier":"CHEBI:42160","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:42160","ontology_label":"dithionite(2-)","ontology_source":"CHEBI"},"preferred_term":"Dithionite","sssom_rows":[{"data_row":1070,"object_id":"CHEBI:42160","object_label":"dithionite(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dithionite","synonym_count":4}'
  snapshot_sha256: 223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5
- evidence_id: ev-f42242f6da190885
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-d6c3db291eeeb06e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d6c3db291eeeb06e in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-8154f95baadc7782
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-5dd82ce950054d1a
  - ev-2af72a6b7a3f4090
  - ev-7e51904654942cbe
  - ev-9df1dd08049d305a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3316af2ec9a04128
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-98e6a7f8b035ec98
  - ev-5dd82ce950054d1a
  - ev-0b0deca360983b4e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:06:45Z;
    reviewed SHA-256=223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5;
    current SHA-256=223989fc29bf0ff1986c59a2d0abc929cd5751c8a9c43a50307b813e2a554ba5;
    hash_changed=False. Reports=["reports/yaml_record_review/Dithionite.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    identity passes, but the reducing-agent role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-98e6a7f8b035ec98
    - ev-5dd82ce950054d1a
  - name: legacy-native-ids
    value: '["SEM:a59560c272178568a085","SEM:aa0a0d4b641e42005edf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5dd82ce950054d1a
    - ev-98e6a7f8b035ec98
    - ev-0b0deca360983b4e
- assessment_id: a-a28d2993b84ed8b4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-98e6a7f8b035ec98
  - ev-a28d2993b84ed8b4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-98e6a7f8b035ec98
    - ev-a28d2993b84ed8b4
findings:
- finding_id: rec-f-d6c3db291eeeb06e
  issue_key: mim-reconciliation-role-support-694992ca37b2f0da
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Dithionite'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-694992ca37b2f0da
  evidence_ids:
  - ev-98e6a7f8b035ec98
  - ev-a28d2993b84ed8b4
  - ev-f42242f6da190885
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dithionite.yaml
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
    finding_id: f-d6c3db291eeeb06e
actions:
- action_id: rec-action-d6c3db291eeeb06e
  description: 'Reassess prediction-only role support: Dithionite'
  finding_ids:
  - rec-f-d6c3db291eeeb06e
  target_ids:
  - record-694992ca37b2f0da
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dithionite.yaml
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
