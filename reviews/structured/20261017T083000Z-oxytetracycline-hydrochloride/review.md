# Per-record structured review: Oxytetracycline_Hydrochloride (data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml)

- Review: 20261017T083000Z-oxytetracycline-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Oxytetracycline_Hydrochloride (data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml, record-5ca2da8788f78c39, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5ca2da8788f78c39 | data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml | maintained | Oxytetracycline_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5ca2da8788f78c39 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5ca2da8788f78c39 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5ca2da8788f78c39 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5ca2da8788f78c39.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5ca2da8788f78c39.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z; reviewed SHA-256=75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef; current SHA-256=75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef; hash_changed=False. Reports=["reports/yaml_record_review/Oxytetracycline_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:31953 hydrochloride identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-5ca2da8788f78c39.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fb50d98dfbd68af3: Reassess prediction-only role support: Oxytetracycline hydrochloride

major / open / confirmed; issue key: mim-reconciliation-role-support-5ca2da8788f78c39.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fb50d98dfbd68af3

Reassess prediction-only role support: Oxytetracycline hydrochloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0694352f1153d43b | data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1599],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31953","line":1601,"mapping_status":"MAPPED","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline hydrochloride"}],"identifier":"CHEBI:31953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31953","ontology_label":"Oxytetracycline hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Oxytetracycline hydrochloride","sssom_rows":[{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oxytetracycline_Hydrochloride","synonym_count":0} |
| ev-ac758f32f3d4acdb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1599] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-08471b24ba844eca | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Oxytetracycline_Hydrochloride; data-row positions=[2163] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline hydrochloride","other":"CAS:2058-46-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Oxytetracycline_Hydrochloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-efa55a1b43b6ed48 | docs/data/mapped_ingredients.csv; CSV lines=[1601] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31953","line":1601,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline hydrochloride","total_occurrences":"0"}] |
| ev-0d4d9a57a7d45069 | reports/yaml_record_review/Oxytetracycline_Hydrochloride.md; &#96;data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:31; Completeness:45; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8de274fd4b27a878 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1083,1588] | context_only | [{"current_record_sha256":"75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef","finding_id":"SEM:dce69818b1965b0bf15d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef","finding_id":"SEM:c33ce76b679b083cd97a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4df2cdd2618d8e47 | data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1599],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31953","line":1601,"mapping_status":"MAPPED","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline hydrochloride"}],"identifier":"CHEBI:31953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31953","ontology_label":"Oxytetracycline hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Oxytetracycline hydrochloride","sssom_rows":[{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oxytetracycline_Hydrochloride","synonym_count":0} |
| ev-33dd64116d87f579 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-fb50d98dfbd68af3] | context_only | Predecessor structured review finding f-fb50d98dfbd68af3 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-oxytetracycline-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Oxytetracycline_Hydrochloride (data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml)'
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
summary: Per-record structured review for Oxytetracycline_Hydrochloride (data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml,
  record-5ca2da8788f78c39, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
    sha256: 75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Oxytetracycline_Hydrochloride.md
    sha256: c20866ec51cd4b6a1299fe2c169fd32d9750363e5e3edd098129d30d20d6e03c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5ca2da8788f78c39
  path: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
  label: Oxytetracycline_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5ca2da8788f78c39
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0694352f1153d43b
  - ev-ac758f32f3d4acdb
  - ev-08471b24ba844eca
  - ev-efa55a1b43b6ed48
  - ev-4df2cdd2618d8e47
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0694352f1153d43b
  - ev-8de274fd4b27a878
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0d4d9a57a7d45069
  - ev-8de274fd4b27a878
  - ev-33dd64116d87f579
evidence:
- evidence_id: ev-0694352f1153d43b
  kind: record_content
  reference: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1599],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31953","line":1601,"mapping_status":"MAPPED","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline
    hydrochloride"}],"identifier":"CHEBI:31953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31953","ontology_label":"Oxytetracycline
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Oxytetracycline hydrochloride","sssom_rows":[{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oxytetracycline_Hydrochloride","synonym_count":0}'
  snapshot_sha256: 75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef
- evidence_id: ev-ac758f32f3d4acdb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1599]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-08471b24ba844eca
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Oxytetracycline_Hydrochloride; data-row positions=[2163]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline
    hydrochloride","other":"CAS:2058-46-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Oxytetracycline_Hydrochloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-efa55a1b43b6ed48
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1601]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31953","line":1601,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline
    hydrochloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0d4d9a57a7d45069
  kind: prior_review
  reference: reports/yaml_record_review/Oxytetracycline_Hydrochloride.md
  locator: '`data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml`:2; Verdict:4;
    Identity:10; Validation:22; Evidence:31; Completeness:45; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c20866ec51cd4b6a1299fe2c169fd32d9750363e5e3edd098129d30d20d6e03c
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml`,\n\
    \  either replace `physicochemical_roles.SELECTIVE_AGENT` with cited\n  experimental\
    \ or recipe evidence, or remove the provisional role facet until\n  source-backed\
    \ role evidence is curated. Then rebuild the final SSSOM and\n  rerun `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-8de274fd4b27a878
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1083,1588]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef","finding_id":"SEM:dce69818b1965b0bf15d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef","finding_id":"SEM:c33ce76b679b083cd97a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4df2cdd2618d8e47
  kind: record_content
  reference: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1599],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31953","line":1601,"mapping_status":"MAPPED","ontology_id":"CHEBI:31953","preferred_term":"Oxytetracycline
    hydrochloride"}],"identifier":"CHEBI:31953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31953","ontology_label":"Oxytetracycline
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Oxytetracycline hydrochloride","sssom_rows":[{"data_row":2163,"object_id":"CHEBI:31953","object_label":"Oxytetracycline
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oxytetracycline_Hydrochloride","synonym_count":0}'
  snapshot_sha256: 75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef
- evidence_id: ev-33dd64116d87f579
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-fb50d98dfbd68af3]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fb50d98dfbd68af3 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-cdf5eee24c745922
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0694352f1153d43b
  - ev-ac758f32f3d4acdb
  - ev-08471b24ba844eca
  - ev-efa55a1b43b6ed48
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cc8190d499247c55
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0d4d9a57a7d45069
  - ev-0694352f1153d43b
  - ev-8de274fd4b27a878
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z;
    reviewed SHA-256=75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef;
    current SHA-256=75d4ab0025ee010f7c687a4ecfeea14c12afc583a51a9b7919e3b7d6c58b20ef;
    hash_changed=False. Reports=["reports/yaml_record_review/Oxytetracycline_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:31953 hydrochloride identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0d4d9a57a7d45069
    - ev-0694352f1153d43b
  - name: legacy-native-ids
    value: '["SEM:dce69818b1965b0bf15d","SEM:c33ce76b679b083cd97a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0694352f1153d43b
    - ev-0d4d9a57a7d45069
    - ev-8de274fd4b27a878
- assessment_id: a-4df2cdd2618d8e47
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0d4d9a57a7d45069
  - ev-4df2cdd2618d8e47
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0d4d9a57a7d45069
    - ev-4df2cdd2618d8e47
findings:
- finding_id: rec-f-fb50d98dfbd68af3
  issue_key: mim-reconciliation-role-support-5ca2da8788f78c39
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Oxytetracycline hydrochloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5ca2da8788f78c39
  evidence_ids:
  - ev-0d4d9a57a7d45069
  - ev-4df2cdd2618d8e47
  - ev-33dd64116d87f579
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-fb50d98dfbd68af3
actions:
- action_id: rec-action-fb50d98dfbd68af3
  description: 'Reassess prediction-only role support: Oxytetracycline hydrochloride'
  finding_ids:
  - rec-f-fb50d98dfbd68af3
  target_ids:
  - record-5ca2da8788f78c39
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oxytetracycline_Hydrochloride.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
