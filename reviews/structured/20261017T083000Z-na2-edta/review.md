# Per-record structured review: Na2-edta (data/ingredients/mapped/Na2-edta.yaml)

- Review: 20261017T083000Z-na2-edta
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2-edta (data/ingredients/mapped/Na2-edta.yaml, record-8df9c38904b5495c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2-edta.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2-edta.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8df9c38904b5495c | data/ingredients/mapped/Na2-edta.yaml | maintained | Na2-edta |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8df9c38904b5495c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8df9c38904b5495c | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8df9c38904b5495c | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8df9c38904b5495c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8df9c38904b5495c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z; reviewed SHA-256=7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4; current SHA-256=7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4; hash_changed=False. Reports=["reports/yaml_record_review/Na2-edta.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:64734 anhydrous EDTA disodium salt identity, CAS-backed structure, duplicate merge, occurrence count, and final row pass, but CHELATOR and one final token need cleanup.

### Historical provisional-role concern

evidence: concern. Targets: record-8df9c38904b5495c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f64f43c62a99ab39: Reassess prediction-only role support: Na2-EDTA

major / open / confirmed; issue key: mim-reconciliation-role-support-8df9c38904b5495c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f64f43c62a99ab39

Reassess prediction-only role support: Na2-EDTA

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f85ae908d01e70c8 | data/ingredients/mapped/Na2-edta.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64734","line":1480,"mapping_status":"MAPPED","ontology_id":"CHEBI:64734","preferred_term":"Na2-EDTA"}],"identifier":"CHEBI:64734","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":612,"edge_count":612,"occurrences":614},"occurrence_statistics":{"media_count":612,"total_occurrences":614},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64734","ontology_label":"EDTA disodium salt (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA","sssom_rows":[{"data_row":1981,"object_id":"CHEBI:64734","object_label":"EDTA disodium salt (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2-edta","synonym_count":25} |
| ev-02ce4606307148e9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1478] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b658e5a678731731 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2-edta; data-row positions=[1981] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1981,"object_id":"CHEBI:64734","object_label":"EDTA disodium salt (anhydrous)","other":"EDTA-2Na&#124;EDTA\u00b72Na&#124;EDTA\u30fb2Na&#124;EDTA 2Na&#124;2Na-EDTA&#124;EDTA (disodium salt)&#124;EDTA disodium&#124;EDTA disodium (anh.)&#124;EDTA disodium salt (anh.)&#124;EDTA.Na .2H O&#124;EDTANa&#124;N,N'-1,2-ethanediylbis[N-(carboxymethyl)glycine], disodium salt&#124;NA EDTA&#124;NA2 EDTA&#124;Na-EDTA&#124;Na2H2EDTA&#124;Na2EDTA&#124;disodium 2,2',2'',2'''-(ethane-1,2-diyldiammonio)tetraacetate&#124;EDTA(Disodium salt)&#124;EDTA\u20222Na&#124;NaEDTA&#124;CAS:139-33-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2-edta","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-6411b0ae21a83620 | docs/data/mapped_ingredients.csv; CSV lines=[1480] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:64734","line":1480,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"612","ontology_id":"CHEBI:64734","preferred_term":"Na2-EDTA","total_occurrences":"614"}] |
| ev-b008c9979cb6b407 | reports/yaml_record_review/Na2-edta.md; &#96;data/ingredients/mapped/Na2-edta.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fc7772316fd353e5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[985,1875] | context_only | [{"current_record_sha256":"7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4","finding_id":"SEM:33a8277f0a7d440dca7d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4","finding_id":"SEM:edaf63868af7f226ad0f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-07d6a169c1ac1d43 | data/ingredients/mapped/Na2-edta.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CHELATOR"}}] |
| ev-4110534942fb2ac8 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-f64f43c62a99ab39] | context_only | Predecessor structured review finding f-f64f43c62a99ab39 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2-edta
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2-edta (data/ingredients/mapped/Na2-edta.yaml)'
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
summary: Per-record structured review for Na2-edta (data/ingredients/mapped/Na2-edta.yaml,
  record-8df9c38904b5495c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2-edta.yaml
    sha256: 7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4
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
  - path: reports/yaml_record_review/Na2-edta.md
    sha256: d562a2edff5d13d3d1034e8ac1ce465cb135ad9ba7151bee5d4259f7ad00987a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8df9c38904b5495c
  path: data/ingredients/mapped/Na2-edta.yaml
  label: Na2-edta
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2-edta.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2-edta.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2-edta.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8df9c38904b5495c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8df9c38904b5495c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8df9c38904b5495c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8df9c38904b5495c
evidence:
- evidence_id: ev-f85ae908d01e70c8
  kind: record_content
  reference: data/ingredients/mapped/Na2-edta.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64734","line":1480,"mapping_status":"MAPPED","ontology_id":"CHEBI:64734","preferred_term":"Na2-EDTA"}],"identifier":"CHEBI:64734","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":612,"edge_count":612,"occurrences":614},"occurrence_statistics":{"media_count":612,"total_occurrences":614},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:64734","ontology_label":"EDTA
    disodium salt (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA","sssom_rows":[{"data_row":1981,"object_id":"CHEBI:64734","object_label":"EDTA
    disodium salt (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2-edta","synonym_count":25}'
  snapshot_sha256: 7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4
- evidence_id: ev-02ce4606307148e9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1478]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b658e5a678731731
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2-edta; data-row positions=[1981]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1981,"object_id":"CHEBI:64734","object_label":"EDTA
    disodium salt (anhydrous)","other":"EDTA-2Na|EDTA\u00b72Na|EDTA\u30fb2Na|EDTA
    2Na|2Na-EDTA|EDTA (disodium salt)|EDTA disodium|EDTA disodium (anh.)|EDTA disodium
    salt (anh.)|EDTA.Na .2H O|EDTANa|N,N''-1,2-ethanediylbis[N-(carboxymethyl)glycine],
    disodium salt|NA EDTA|NA2 EDTA|Na-EDTA|Na2H2EDTA|Na2EDTA|disodium 2,2'',2'''',2''''''-(ethane-1,2-diyldiammonio)tetraacetate|EDTA(Disodium
    salt)|EDTA\u20222Na|NaEDTA|CAS:139-33-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2-edta","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6411b0ae21a83620
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1480]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:64734","line":1480,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"612","ontology_id":"CHEBI:64734","preferred_term":"Na2-EDTA","total_occurrences":"614"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b008c9979cb6b407
  kind: prior_review
  reference: reports/yaml_record_review/Na2-edta.md
  locator: '`data/ingredients/mapped/Na2-edta.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:28; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d562a2edff5d13d3d1034e8ac1ce465cb135ad9ba7151bee5d4259f7ad00987a
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2-edta.yaml`,\
    \ either remove\n  `physicochemical_roles.CHELATOR` or replace its name-pattern\
    \ placeholder with\n  source-backed evidence from a maintained role-text or literature\
    \ input. Rerun\n  strict validation after the role facet change.\n- Major: demote\
    \ `EDTA.Na .2H O` so it is no longer published as an exact\n  anhydrous disodium\
    \ EDTA synonym, then rebuild final SSSOM and re-run final\n  SSSOM validation\
    \ plus product label validation."
- evidence_id: ev-fc7772316fd353e5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[985,1875]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4","finding_id":"SEM:33a8277f0a7d440dca7d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4","finding_id":"SEM:edaf63868af7f226ad0f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-07d6a169c1ac1d43
  kind: record_content
  reference: data/ingredients/mapped/Na2-edta.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CHELATOR"}}]'
  snapshot_sha256: 7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4
- evidence_id: ev-4110534942fb2ac8
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-f64f43c62a99ab39]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f64f43c62a99ab39 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-d68d579354006038
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8df9c38904b5495c
  evidence_ids:
  - ev-f85ae908d01e70c8
  - ev-02ce4606307148e9
  - ev-b658e5a678731731
  - ev-6411b0ae21a83620
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bc7d15d0e76a95c8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8df9c38904b5495c
  evidence_ids:
  - ev-b008c9979cb6b407
  - ev-f85ae908d01e70c8
  - ev-fc7772316fd353e5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z;
    reviewed SHA-256=7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4;
    current SHA-256=7ac669135e2443456cf3256bb963d53935e7ce48f9d8878a65778162bf02d4c4;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2-edta.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:64734 anhydrous
    EDTA disodium salt identity, CAS-backed structure, duplicate merge, occurrence
    count, and final row pass, but CHELATOR and one final token need cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b008c9979cb6b407
    - ev-f85ae908d01e70c8
  - name: legacy-native-ids
    value: '["SEM:33a8277f0a7d440dca7d","SEM:edaf63868af7f226ad0f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f85ae908d01e70c8
    - ev-b008c9979cb6b407
    - ev-fc7772316fd353e5
- assessment_id: a-07d6a169c1ac1d43
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8df9c38904b5495c
  evidence_ids:
  - ev-b008c9979cb6b407
  - ev-07d6a169c1ac1d43
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b008c9979cb6b407
    - ev-07d6a169c1ac1d43
findings:
- finding_id: rec-f-f64f43c62a99ab39
  issue_key: mim-reconciliation-role-support-8df9c38904b5495c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2-EDTA'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8df9c38904b5495c
  evidence_ids:
  - ev-b008c9979cb6b407
  - ev-07d6a169c1ac1d43
  - ev-4110534942fb2ac8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2-edta.yaml
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
    finding_id: f-f64f43c62a99ab39
actions:
- action_id: rec-action-f64f43c62a99ab39
  description: 'Reassess prediction-only role support: Na2-EDTA'
  finding_ids:
  - rec-f-f64f43c62a99ab39
  target_ids:
  - record-8df9c38904b5495c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2-edta.yaml
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
