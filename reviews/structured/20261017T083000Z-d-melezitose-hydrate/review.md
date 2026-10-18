# Per-record structured review: D-_-melezitose_Hydrate (data/ingredients/mapped/D-_-melezitose_Hydrate.yaml)

- Review: 20261017T083000Z-d-melezitose-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-_-melezitose_Hydrate (data/ingredients/mapped/D-_-melezitose_Hydrate.yaml, record-6a7c992230ad3a68, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-_-melezitose_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-_-melezitose_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6a7c992230ad3a68 | data/ingredients/mapped/D-_-melezitose_Hydrate.yaml | maintained | D-_-melezitose_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6a7c992230ad3a68 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6a7c992230ad3a68 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6a7c992230ad3a68 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6a7c992230ad3a68.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6a7c992230ad3a68.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:23:22Z; reviewed SHA-256=e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59; current SHA-256=e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59; hash_changed=False. Reports=["reports/yaml_record_review/D-_-melezitose_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS hydrate identity, close melezitose parent, and registry row pass, but final SSSOM exports an anhydrous parent label and the carbon role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-6a7c992230ad3a68.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ad30e391822c91c2: Reassess prediction-only role support: D-(+)-Melezitose hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-6a7c992230ad3a68.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ad30e391822c91c2

Reassess prediction-only role support: D-(+)-Melezitose hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bed0c463c3f7df1b | data/ingredients/mapped/D-_-melezitose_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[798],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-10-2","line":800,"mapping_status":"MAPPED","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose hydrate"}],"identifier":"cas:207511-10-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6731","ontology_label":"melezitose","ontology_source":"CHEBI"},"preferred_term":"D-(+)-Melezitose hydrate","sssom_rows":[{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","predicate_id":"skos:closeMatch"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-melezitose_Hydrate","synonym_count":1} |
| ev-3fdde644013845a8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [798] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2420490e9ac2abab | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-_-melezitose_Hydrate; data-row positions=[916, 917] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","other":"D-melezitose (melezitose)&#124;CAS:207511-10-2","predicate_id":"skos:closeMatch","subject_id":"MIM:D-_-melezitose_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose hydrate","other":"CAS:207511-10-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-_-melezitose_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-70d851140b6ab6d2 | docs/data/mapped_ingredients.csv; CSV lines=[800] | supports | Published identity and count rows inspected: [{"identifier":"cas:207511-10-2","line":800,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose hydrate","total_occurrences":"0"}] |
| ev-34088d9e7365c328 | reports/yaml_record_review/D-_-melezitose_Hydrate.md; &#96;data/ingredients/mapped/D-_-melezitose_Hydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:30; Evidence:49; Completeness:68; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-282787ba2118a38b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[483,1945] | context_only | [{"current_record_sha256":"e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59","finding_id":"SEM:2b48b35ca471592f4f25","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59","finding_id":"SEM:99467502d0ca0d43ba93","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-55f2ddefe05b7a10 | data/ingredients/mapped/D-_-melezitose_Hydrate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[798],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-10-2","line":800,"mapping_status":"MAPPED","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose hydrate"}],"identifier":"cas:207511-10-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6731","ontology_label":"melezitose","ontology_source":"CHEBI"},"preferred_term":"D-(+)-Melezitose hydrate","sssom_rows":[{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","predicate_id":"skos:closeMatch"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-melezitose_Hydrate","synonym_count":1} |
| ev-3eb8940df7ded7a4 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-ad30e391822c91c2] | context_only | Predecessor structured review finding f-ad30e391822c91c2 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-melezitose-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-_-melezitose_Hydrate (data/ingredients/mapped/D-_-melezitose_Hydrate.yaml)'
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
summary: Per-record structured review for D-_-melezitose_Hydrate (data/ingredients/mapped/D-_-melezitose_Hydrate.yaml,
  record-6a7c992230ad3a68, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
    sha256: e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59
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
  - path: reports/yaml_record_review/D-_-melezitose_Hydrate.md
    sha256: e162005154ab575975e6c08eae79507d50ea6c84c00e9f9374529f7cbfca1bef
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6a7c992230ad3a68
  path: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
  label: D-_-melezitose_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-_-melezitose_Hydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6a7c992230ad3a68
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-bed0c463c3f7df1b
  - ev-3fdde644013845a8
  - ev-2420490e9ac2abab
  - ev-70d851140b6ab6d2
  - ev-55f2ddefe05b7a10
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-bed0c463c3f7df1b
  - ev-282787ba2118a38b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-34088d9e7365c328
  - ev-282787ba2118a38b
  - ev-3eb8940df7ded7a4
evidence:
- evidence_id: ev-bed0c463c3f7df1b
  kind: record_content
  reference: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[798],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-10-2","line":800,"mapping_status":"MAPPED","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose
    hydrate"}],"identifier":"cas:207511-10-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6731","ontology_label":"melezitose","ontology_source":"CHEBI"},"preferred_term":"D-(+)-Melezitose
    hydrate","sssom_rows":[{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","predicate_id":"skos:closeMatch"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-melezitose_Hydrate","synonym_count":1}'
  snapshot_sha256: e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59
- evidence_id: ev-3fdde644013845a8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [798]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2420490e9ac2abab
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-_-melezitose_Hydrate; data-row positions=[916, 917]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","other":"D-melezitose
    (melezitose)|CAS:207511-10-2","predicate_id":"skos:closeMatch","subject_id":"MIM:D-_-melezitose_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose
    hydrate","other":"CAS:207511-10-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-_-melezitose_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-70d851140b6ab6d2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[800]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:207511-10-2","line":800,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose
    hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-34088d9e7365c328
  kind: prior_review
  reference: reports/yaml_record_review/D-_-melezitose_Hydrate.md
  locator: '`data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`:2; Verdict:4; Identity:12;
    Validation:30; Evidence:49; Completeness:68; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e162005154ab575975e6c08eae79507d50ea6c84c00e9f9374529f7cbfca1bef
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`,\
    \ remove\n  `D-melezitose (melezitose)` from active synonyms or retag it as\n\
    \  provenance-only so it no longer reaches final SSSOM `other`; then\n  synchronize\
    \ `data/curated/mapped_ingredients.yaml` and regenerate final\n  SSSOM.\n- Either\
    \ replace the computational `CARBON_SOURCE` evidence with direct\n  CultureBotHT\
    \ or source-backed media-role evidence for this ingredient, or\n  remove the role\
    \ facet; then rerun strict validation and the final SSSOM\n  build."
- evidence_id: ev-282787ba2118a38b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[483,1945]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59","finding_id":"SEM:2b48b35ca471592f4f25","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59","finding_id":"SEM:99467502d0ca0d43ba93","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-55f2ddefe05b7a10
  kind: record_content
  reference: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[798],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-10-2","line":800,"mapping_status":"MAPPED","ontology_id":"CHEBI:6731","preferred_term":"D-(+)-Melezitose
    hydrate"}],"identifier":"cas:207511-10-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6731","ontology_label":"melezitose","ontology_source":"CHEBI"},"preferred_term":"D-(+)-Melezitose
    hydrate","sssom_rows":[{"data_row":916,"object_id":"CHEBI:6731","object_label":"melezitose","predicate_id":"skos:closeMatch"},{"data_row":917,"object_id":"cas:207511-10-2","object_label":"D-(+)-Melezitose
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-melezitose_Hydrate","synonym_count":1}'
  snapshot_sha256: e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59
- evidence_id: ev-3eb8940df7ded7a4
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-ad30e391822c91c2]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ad30e391822c91c2 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-3f6669bba52336c1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-bed0c463c3f7df1b
  - ev-3fdde644013845a8
  - ev-2420490e9ac2abab
  - ev-70d851140b6ab6d2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7cc9d6abc9107384
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-34088d9e7365c328
  - ev-bed0c463c3f7df1b
  - ev-282787ba2118a38b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:23:22Z;
    reviewed SHA-256=e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59;
    current SHA-256=e1b61c883ad813d73b3b508054774699b577fbaa90c8dd6fd4748abfa20bcc59;
    hash_changed=False. Reports=["reports/yaml_record_review/D-_-melezitose_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    hydrate identity, close melezitose parent, and registry row pass, but final SSSOM
    exports an anhydrous parent label and the carbon role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-34088d9e7365c328
    - ev-bed0c463c3f7df1b
  - name: legacy-native-ids
    value: '["SEM:2b48b35ca471592f4f25","SEM:99467502d0ca0d43ba93"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bed0c463c3f7df1b
    - ev-34088d9e7365c328
    - ev-282787ba2118a38b
- assessment_id: a-55f2ddefe05b7a10
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-34088d9e7365c328
  - ev-55f2ddefe05b7a10
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-34088d9e7365c328
    - ev-55f2ddefe05b7a10
findings:
- finding_id: rec-f-ad30e391822c91c2
  issue_key: mim-reconciliation-role-support-6a7c992230ad3a68
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-(+)-Melezitose hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6a7c992230ad3a68
  evidence_ids:
  - ev-34088d9e7365c328
  - ev-55f2ddefe05b7a10
  - ev-3eb8940df7ded7a4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-ad30e391822c91c2
actions:
- action_id: rec-action-ad30e391822c91c2
  description: 'Reassess prediction-only role support: D-(+)-Melezitose hydrate'
  finding_ids:
  - rec-f-ad30e391822c91c2
  target_ids:
  - record-6a7c992230ad3a68
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-melezitose_Hydrate.yaml
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
