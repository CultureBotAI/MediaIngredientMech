# Per-record structured review: Na2b4o7_X_10_H2o (data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml)

- Review: 20261017T083000Z-na2b4o7-x-10-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2b4o7_X_10_H2o (data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml, record-a42d13dd9f1a63c8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a42d13dd9f1a63c8 | data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml | maintained | Na2b4o7_X_10_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a42d13dd9f1a63c8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a42d13dd9f1a63c8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a42d13dd9f1a63c8 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a42d13dd9f1a63c8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a42d13dd9f1a63c8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:10:17Z; reviewed SHA-256=596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09; current SHA-256=596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09; hash_changed=False. Reports=["reports/yaml_record_review/Na2b4o7_X_10_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131366 disodium tetraborate decahydrate identity and hydrate synonyms pass, but BUFFER is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-a42d13dd9f1a63c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2a129e35c176b987: Reassess prediction-only role support: Na2B4O7 x 10 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-a42d13dd9f1a63c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2a129e35c176b987

Reassess prediction-only role support: Na2B4O7 x 10 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7153779cafc27922 | data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1484],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131366","line":1486,"mapping_status":"MAPPED","ontology_id":"CHEBI:131366","preferred_term":"Na2B4O7 x 10 H2O"}],"identifier":"CHEBI:131366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":263,"edge_count":263,"occurrences":263},"occurrence_statistics":{"media_count":263,"total_occurrences":263},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131366","ontology_label":"disodium tetraborate decahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2B4O7 x 10 H2O","sssom_rows":[{"data_row":1989,"object_id":"CHEBI:131366","object_label":"disodium tetraborate decahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2b4o7_X_10_H2o","synonym_count":12} |
| ev-5c2065449e7dc635 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1484] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-170dabf7874eee11 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2b4o7_X_10_H2o; data-row positions=[1989] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1989,"object_id":"CHEBI:131366","object_label":"disodium tetraborate decahydrate","other":"Na2B4O7\u00b710H2O&#124;Na2B4O7\uff0e10H2O&#124;sodium tetraborate decahydrate&#124;borax&#124;sodium borate decahydrate&#124;Na2B4O7 \u00b7 10 H2O&#124;Na2B4O7 . 10H2O&#124;Na2B4O7\u22c510H2O&#124;Na2B4O7\u30fb10H2O&#124;Na2B4O7 \u00b7  10 H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2b4o7_X_10_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f7a5d42e876030f4 | docs/data/mapped_ingredients.csv; CSV lines=[1486] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131366","line":1486,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"263","ontology_id":"CHEBI:131366","preferred_term":"Na2B4O7 x 10 H2O","total_occurrences":"263"}] |
| ev-0988ba75b454b0c2 | reports/yaml_record_review/Na2b4o7_X_10_H2o.md; &#96;data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0d8fff4f33d22bc0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[990,1534] | context_only | [{"current_record_sha256":"596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09","finding_id":"SEM:3bb6e7f7d045bed077e3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09","finding_id":"SEM:a3c56dddac33149b0afc","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b6a3566145a09392 | data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:35225 (buffer (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}] |
| ev-28b080fdab815397 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-2a129e35c176b987] | context_only | Predecessor structured review finding f-2a129e35c176b987 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2b4o7-x-10-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2b4o7_X_10_H2o (data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml)'
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
summary: Per-record structured review for Na2b4o7_X_10_H2o (data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml,
  record-a42d13dd9f1a63c8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
    sha256: 596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09
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
  - path: reports/yaml_record_review/Na2b4o7_X_10_H2o.md
    sha256: 135804008e2a242750eac322dd4d24bd210e9a6545f66841a8c1130108ab0d74
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a42d13dd9f1a63c8
  path: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
  label: Na2b4o7_X_10_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a42d13dd9f1a63c8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a42d13dd9f1a63c8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a42d13dd9f1a63c8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a42d13dd9f1a63c8
evidence:
- evidence_id: ev-7153779cafc27922
  kind: record_content
  reference: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1484],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131366","line":1486,"mapping_status":"MAPPED","ontology_id":"CHEBI:131366","preferred_term":"Na2B4O7
    x 10 H2O"}],"identifier":"CHEBI:131366","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":263,"edge_count":263,"occurrences":263},"occurrence_statistics":{"media_count":263,"total_occurrences":263},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131366","ontology_label":"disodium
    tetraborate decahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2B4O7
    x 10 H2O","sssom_rows":[{"data_row":1989,"object_id":"CHEBI:131366","object_label":"disodium
    tetraborate decahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2b4o7_X_10_H2o","synonym_count":12}'
  snapshot_sha256: 596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09
- evidence_id: ev-5c2065449e7dc635
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1484]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-170dabf7874eee11
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2b4o7_X_10_H2o; data-row positions=[1989]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1989,"object_id":"CHEBI:131366","object_label":"disodium
    tetraborate decahydrate","other":"Na2B4O7\u00b710H2O|Na2B4O7\uff0e10H2O|sodium
    tetraborate decahydrate|borax|sodium borate decahydrate|Na2B4O7 \u00b7 10 H2O|Na2B4O7
    . 10H2O|Na2B4O7\u22c510H2O|Na2B4O7\u30fb10H2O|Na2B4O7 \u00b7  10 H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2b4o7_X_10_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f7a5d42e876030f4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1486]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131366","line":1486,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"263","ontology_id":"CHEBI:131366","preferred_term":"Na2B4O7
    x 10 H2O","total_occurrences":"263"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0988ba75b454b0c2
  kind: prior_review
  reference: reports/yaml_record_review/Na2b4o7_X_10_H2o.md
  locator: '`data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 135804008e2a242750eac322dd4d24bd210e9a6545f66841a8c1130108ab0d74
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml`,\
    \ either remove\n  `physicochemical_roles.BUFFER` or replace its ChEBI-ancestry\
    \ placeholder with\n  source-backed evidence from maintained role-text or literature\
    \ inputs. Rerun\n  strict validation and the role/output SSSOM checks after the\
    \ role facet\n  change."
- evidence_id: ev-0d8fff4f33d22bc0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[990,1534]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09","finding_id":"SEM:3bb6e7f7d045bed077e3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09","finding_id":"SEM:a3c56dddac33149b0afc","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b6a3566145a09392
  kind: record_content
  reference: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:35225 (buffer (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}]'
  snapshot_sha256: 596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09
- evidence_id: ev-28b080fdab815397
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-2a129e35c176b987]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2a129e35c176b987 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-4d555917076022a8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a42d13dd9f1a63c8
  evidence_ids:
  - ev-7153779cafc27922
  - ev-5c2065449e7dc635
  - ev-170dabf7874eee11
  - ev-f7a5d42e876030f4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ebe50219246c9550
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a42d13dd9f1a63c8
  evidence_ids:
  - ev-0988ba75b454b0c2
  - ev-7153779cafc27922
  - ev-0d8fff4f33d22bc0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:10:17Z;
    reviewed SHA-256=596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09;
    current SHA-256=596380ddafeefb860cebe7e69d4ac6f336b93987ece57a2d005a86a2d6a29d09;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2b4o7_X_10_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:131366 disodium tetraborate decahydrate identity and hydrate synonyms pass,
    but BUFFER is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0988ba75b454b0c2
    - ev-7153779cafc27922
  - name: legacy-native-ids
    value: '["SEM:3bb6e7f7d045bed077e3","SEM:a3c56dddac33149b0afc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7153779cafc27922
    - ev-0988ba75b454b0c2
    - ev-0d8fff4f33d22bc0
- assessment_id: a-b6a3566145a09392
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a42d13dd9f1a63c8
  evidence_ids:
  - ev-0988ba75b454b0c2
  - ev-b6a3566145a09392
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0988ba75b454b0c2
    - ev-b6a3566145a09392
findings:
- finding_id: rec-f-2a129e35c176b987
  issue_key: mim-reconciliation-role-support-a42d13dd9f1a63c8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2B4O7 x 10 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a42d13dd9f1a63c8
  evidence_ids:
  - ev-0988ba75b454b0c2
  - ev-b6a3566145a09392
  - ev-28b080fdab815397
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
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
    finding_id: f-2a129e35c176b987
actions:
- action_id: rec-action-2a129e35c176b987
  description: 'Reassess prediction-only role support: Na2B4O7 x 10 H2O'
  finding_ids:
  - rec-f-2a129e35c176b987
  target_ids:
  - record-a42d13dd9f1a63c8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2b4o7_X_10_H2o.yaml
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
