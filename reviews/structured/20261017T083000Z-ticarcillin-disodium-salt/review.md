# Per-record structured review: Ticarcillin_Disodium_Salt (data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml)

- Review: 20261017T083000Z-ticarcillin-disodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ticarcillin_Disodium_Salt (data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml, record-a893d1f31f2b9145, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a893d1f31f2b9145 | data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml | maintained | Ticarcillin_Disodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a893d1f31f2b9145 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a893d1f31f2b9145 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a893d1f31f2b9145 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a893d1f31f2b9145.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a893d1f31f2b9145.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:58:51Z; reviewed SHA-256=5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1; current SHA-256=5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1; hash_changed=False. Reports=["reports/yaml_record_review/Ticarcillin_Disodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-to-CHEBI identity and final SSSOM row pass, but SELECTIVE_AGENT is still provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-a893d1f31f2b9145.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2ea4124f2641a358: Reassess prediction-only role support: Ticarcillin disodium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-a893d1f31f2b9145.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2ea4124f2641a358

Reassess prediction-only role support: Ticarcillin disodium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-05f775eb4f9e461a | data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1968],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35017","line":1970,"mapping_status":"MAPPED","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin disodium salt"}],"identifier":"CHEBI:35017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:35017","ontology_label":"ticarcillin disodium","ontology_source":"CHEBI"},"preferred_term":"Ticarcillin disodium salt","sssom_rows":[{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin disodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ticarcillin_Disodium_Salt","synonym_count":1} |
| ev-71bcb6d1ffdc98a5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1968] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-352a37dc465d571c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ticarcillin_Disodium_Salt; data-row positions=[2783] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin disodium","other":"disodium 6beta-{[(2R)-2-carboxylato-2-thiophen-3-ylacetyl]amino}-2,2-dimethylpenam-3alpha-carboxylate&#124;CAS:4697-14-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ticarcillin_Disodium_Salt","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-82d542781ecac686 | docs/data/mapped_ingredients.csv; CSV lines=[1970] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:35017","line":1970,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin disodium salt","total_occurrences":"0"}] |
| ev-83f9d8b62f9746c6 | reports/yaml_record_review/Ticarcillin_Disodium_Salt.md; &#96;data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:32; Issues:44; Major: &#96;SELECTIVE_AGENT&#96; is provisional name-pattern evidence:46; Completeness:64; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-153598f0934bf005 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1290,1403] | context_only | [{"current_record_sha256":"5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1","finding_id":"SEM:f1d24f1f08dcb65aad51","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1","finding_id":"SEM:fbceed116189bbd8320b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-58cc2be47bdb571c | data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1968],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35017","line":1970,"mapping_status":"MAPPED","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin disodium salt"}],"identifier":"CHEBI:35017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:35017","ontology_label":"ticarcillin disodium","ontology_source":"CHEBI"},"preferred_term":"Ticarcillin disodium salt","sssom_rows":[{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin disodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ticarcillin_Disodium_Salt","synonym_count":1} |
| ev-e2003d6fb5dcd1c7 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-2ea4124f2641a358] | context_only | Predecessor structured review finding f-2ea4124f2641a358 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ticarcillin-disodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ticarcillin_Disodium_Salt (data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml)'
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
summary: Per-record structured review for Ticarcillin_Disodium_Salt (data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml,
  record-a893d1f31f2b9145, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
    sha256: 5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1
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
  - path: reports/yaml_record_review/Ticarcillin_Disodium_Salt.md
    sha256: 9599c51f125ea9b89d88b7edb963b03c8a5e96918f9f68df8e1ea85e6dfa6978
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a893d1f31f2b9145
  path: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
  label: Ticarcillin_Disodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a893d1f31f2b9145
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-05f775eb4f9e461a
  - ev-71bcb6d1ffdc98a5
  - ev-352a37dc465d571c
  - ev-82d542781ecac686
  - ev-58cc2be47bdb571c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-05f775eb4f9e461a
  - ev-153598f0934bf005
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-83f9d8b62f9746c6
  - ev-153598f0934bf005
  - ev-e2003d6fb5dcd1c7
evidence:
- evidence_id: ev-05f775eb4f9e461a
  kind: record_content
  reference: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1968],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35017","line":1970,"mapping_status":"MAPPED","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin
    disodium salt"}],"identifier":"CHEBI:35017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:35017","ontology_label":"ticarcillin
    disodium","ontology_source":"CHEBI"},"preferred_term":"Ticarcillin disodium salt","sssom_rows":[{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin
    disodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ticarcillin_Disodium_Salt","synonym_count":1}'
  snapshot_sha256: 5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1
- evidence_id: ev-71bcb6d1ffdc98a5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1968]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-352a37dc465d571c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ticarcillin_Disodium_Salt; data-row positions=[2783]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin
    disodium","other":"disodium 6beta-{[(2R)-2-carboxylato-2-thiophen-3-ylacetyl]amino}-2,2-dimethylpenam-3alpha-carboxylate|CAS:4697-14-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Ticarcillin_Disodium_Salt","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-82d542781ecac686
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1970]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:35017","line":1970,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin
    disodium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-83f9d8b62f9746c6
  kind: prior_review
  reference: reports/yaml_record_review/Ticarcillin_Disodium_Salt.md
  locator: '`data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml`:2; Verdict:4;
    Identity:10; Validation:24; Evidence:32; Issues:44; Major: `SELECTIVE_AGENT` is
    provisional name-pattern evidence:46; Completeness:64; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9599c51f125ea9b89d88b7edb963b03c8a5e96918f9f68df8e1ea85e6dfa6978
  quote: "Issues:\n\n\nMajor: `SELECTIVE_AGENT` is provisional name-pattern evidence:\n\
    The only role assertion is:\n\n```yaml\nphysicochemical_roles:\n- role: SELECTIVE_AGENT\n\
    \  confidence: 0.8\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Inferred from curated media-role name pattern\n    curator_note:\
    \ Provisional role from a curated name-pattern rule; review recommended.\n```\n\
    \nThat is the same provisional `infer_roles_from_name_lists` path flagged for\n\
    other antibiotic salts. The CAS-RN lookup establishes the molecule, but it does\n\
    not independently curate the media role.\n\nRecommended Edits:\n- Replace the\
    \ `COMPUTATIONAL_PREDICTION` role evidence with curated\n  database/literature\
    \ evidence for the CultureBotHT use, or remove\n  `physicochemical_roles` until\
    \ such support is added."
- evidence_id: ev-153598f0934bf005
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1290,1403]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1","finding_id":"SEM:f1d24f1f08dcb65aad51","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1","finding_id":"SEM:fbceed116189bbd8320b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-58cc2be47bdb571c
  kind: record_content
  reference: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1968],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:35017","line":1970,"mapping_status":"MAPPED","ontology_id":"CHEBI:35017","preferred_term":"Ticarcillin
    disodium salt"}],"identifier":"CHEBI:35017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:35017","ontology_label":"ticarcillin
    disodium","ontology_source":"CHEBI"},"preferred_term":"Ticarcillin disodium salt","sssom_rows":[{"data_row":2783,"object_id":"CHEBI:35017","object_label":"ticarcillin
    disodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ticarcillin_Disodium_Salt","synonym_count":1}'
  snapshot_sha256: 5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1
- evidence_id: ev-e2003d6fb5dcd1c7
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-2ea4124f2641a358]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2ea4124f2641a358 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-63f7c027fd06b96e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-05f775eb4f9e461a
  - ev-71bcb6d1ffdc98a5
  - ev-352a37dc465d571c
  - ev-82d542781ecac686
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0b6fe20ba9c072d4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-83f9d8b62f9746c6
  - ev-05f775eb4f9e461a
  - ev-153598f0934bf005
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:58:51Z;
    reviewed SHA-256=5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1;
    current SHA-256=5f9c695108a6ccc66fed42d5463bd5eb850bded263056467ae5f61c583d07ce1;
    hash_changed=False. Reports=["reports/yaml_record_review/Ticarcillin_Disodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-to-CHEBI
    identity and final SSSOM row pass, but SELECTIVE_AGENT is still provisional name-pattern
    evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83f9d8b62f9746c6
    - ev-05f775eb4f9e461a
  - name: legacy-native-ids
    value: '["SEM:f1d24f1f08dcb65aad51","SEM:fbceed116189bbd8320b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-05f775eb4f9e461a
    - ev-83f9d8b62f9746c6
    - ev-153598f0934bf005
- assessment_id: a-58cc2be47bdb571c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-83f9d8b62f9746c6
  - ev-58cc2be47bdb571c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83f9d8b62f9746c6
    - ev-58cc2be47bdb571c
findings:
- finding_id: rec-f-2ea4124f2641a358
  issue_key: mim-reconciliation-role-support-a893d1f31f2b9145
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Ticarcillin disodium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a893d1f31f2b9145
  evidence_ids:
  - ev-83f9d8b62f9746c6
  - ev-58cc2be47bdb571c
  - ev-e2003d6fb5dcd1c7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
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
    finding_id: f-2ea4124f2641a358
actions:
- action_id: rec-action-2ea4124f2641a358
  description: 'Reassess prediction-only role support: Ticarcillin disodium salt'
  finding_ids:
  - rec-f-2ea4124f2641a358
  target_ids:
  - record-a893d1f31f2b9145
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml
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
````
