# Per-record structured review: Nickel_II_chloride_hexahydrate (data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml)

- Review: 20261017T083000Z-nickel-ii-chloride-hexahydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nickel_II_chloride_hexahydrate (data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml, record-77687c39e6747459, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-77687c39e6747459 | data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml | maintained | Nickel_II_chloride_hexahydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-77687c39e6747459 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-77687c39e6747459 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-77687c39e6747459 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-77687c39e6747459.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-77687c39e6747459.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:35:34Z; reviewed SHA-256=3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724; current SHA-256=3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724; hash_changed=False. Reports=["reports/yaml_record_review/Nickel_II_chloride_hexahydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:53542 hydrate identity passes, but TRACE_ELEMENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-77687c39e6747459.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-21c2f22008ac704a: Reassess prediction-only role support: Nickel (II) chloride hexahydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-77687c39e6747459.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-21c2f22008ac704a

Reassess prediction-only role support: Nickel (II) chloride hexahydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1ec23ab89fe0d73b | data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53542","line":1556,"mapping_status":"MAPPED","ontology_id":"CHEBI:53542","preferred_term":"Nickel (II) chloride hexahydrate"}],"identifier":"CHEBI:53542","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2991,"edge_count":2991,"occurrences":2992},"occurrence_statistics":{"media_count":2991,"total_occurrences":2992},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:53542","ontology_label":"nickel chloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"Nickel (II) chloride hexahydrate","sssom_rows":[{"data_row":2077,"object_id":"CHEBI:53542","object_label":"nickel chloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nickel_II_chloride_hexahydrate","synonym_count":6} |
| ev-692281a67c397849 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1554] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-712b90066788e776 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nickel_II_chloride_hexahydrate; data-row positions=[2077] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2077,"object_id":"CHEBI:53542","object_label":"nickel chloride hexahydrate","other":"Nickel dichloride hexahydrate&#124;Nickel(II) chloride, hexahydrate&#124;nickel(II) chloride hexahydrate&#124;nickel chloride--water (1/6)&#124;NiCl2 x 6 H2O&#124;CAS:7791-20-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Nickel_II_chloride_hexahydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-13e70cf0ae446a22 | docs/data/mapped_ingredients.csv; CSV lines=[1556] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:53542","line":1556,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2991","ontology_id":"CHEBI:53542","preferred_term":"Nickel (II) chloride hexahydrate","total_occurrences":"2992"}] |
| ev-56dad6fef4f687c1 | reports/yaml_record_review/Nickel_II_chloride_hexahydrate.md; &#96;data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:29; Completeness:43; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9940b56bc5b1b2a0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1051,1960] | context_only | [{"current_record_sha256":"3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724","finding_id":"SEM:2088f1f36a9e09fb3923","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724","finding_id":"SEM:81e7587b611822fb1611","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-abeaf053fb950d22 | data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-fdb8dadf0094d383 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-21c2f22008ac704a] | context_only | Predecessor structured review finding f-21c2f22008ac704a in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nickel-ii-chloride-hexahydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nickel_II_chloride_hexahydrate (data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml)'
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
summary: Per-record structured review for Nickel_II_chloride_hexahydrate (data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml,
  record-77687c39e6747459, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
    sha256: 3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724
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
  - path: reports/yaml_record_review/Nickel_II_chloride_hexahydrate.md
    sha256: 6b153a1560f3e0a4791ec6377e6280d599210ee0bcb7fcfb640f5fdcb47572e9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-77687c39e6747459
  path: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
  label: Nickel_II_chloride_hexahydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-77687c39e6747459
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-77687c39e6747459
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-77687c39e6747459
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-77687c39e6747459
evidence:
- evidence_id: ev-1ec23ab89fe0d73b
  kind: record_content
  reference: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1554],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53542","line":1556,"mapping_status":"MAPPED","ontology_id":"CHEBI:53542","preferred_term":"Nickel
    (II) chloride hexahydrate"}],"identifier":"CHEBI:53542","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2991,"edge_count":2991,"occurrences":2992},"occurrence_statistics":{"media_count":2991,"total_occurrences":2992},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:53542","ontology_label":"nickel
    chloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"Nickel (II)
    chloride hexahydrate","sssom_rows":[{"data_row":2077,"object_id":"CHEBI:53542","object_label":"nickel
    chloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nickel_II_chloride_hexahydrate","synonym_count":6}'
  snapshot_sha256: 3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724
- evidence_id: ev-692281a67c397849
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1554]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-712b90066788e776
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nickel_II_chloride_hexahydrate; data-row positions=[2077]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2077,"object_id":"CHEBI:53542","object_label":"nickel
    chloride hexahydrate","other":"Nickel dichloride hexahydrate|Nickel(II) chloride,
    hexahydrate|nickel(II) chloride hexahydrate|nickel chloride--water (1/6)|NiCl2
    x 6 H2O|CAS:7791-20-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Nickel_II_chloride_hexahydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-13e70cf0ae446a22
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1556]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:53542","line":1556,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2991","ontology_id":"CHEBI:53542","preferred_term":"Nickel
    (II) chloride hexahydrate","total_occurrences":"2992"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-56dad6fef4f687c1
  kind: prior_review
  reference: reports/yaml_record_review/Nickel_II_chloride_hexahydrate.md
  locator: '`data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml`:2; Verdict:4;
    Identity:11; Validation:22; Evidence:29; Completeness:43; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6b153a1560f3e0a4791ec6377e6280d599210ee0bcb7fcfb640f5fdcb47572e9
  quote: "Recommended Edits:\n- Major: in\n  `data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml`,\
    \ either replace\n  `nutritional_roles.TRACE_ELEMENT` with inspected source evidence\
    \ for nickel\n  chloride hexahydrate as a trace-element source in media, or remove\
    \ the\n  provisional role."
- evidence_id: ev-9940b56bc5b1b2a0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1051,1960]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724","finding_id":"SEM:2088f1f36a9e09fb3923","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724","finding_id":"SEM:81e7587b611822fb1611","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-abeaf053fb950d22
  kind: record_content
  reference: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724
- evidence_id: ev-fdb8dadf0094d383
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-21c2f22008ac704a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-21c2f22008ac704a in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-f12d56de6a30c68c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-77687c39e6747459
  evidence_ids:
  - ev-1ec23ab89fe0d73b
  - ev-692281a67c397849
  - ev-712b90066788e776
  - ev-13e70cf0ae446a22
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-09ac5bdaa0b18dd6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-77687c39e6747459
  evidence_ids:
  - ev-56dad6fef4f687c1
  - ev-1ec23ab89fe0d73b
  - ev-9940b56bc5b1b2a0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:35:34Z;
    reviewed SHA-256=3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724;
    current SHA-256=3cb45355a45ad8622e58fc69f4b84253866042170493ed0eb4dc7597116a4724;
    hash_changed=False. Reports=["reports/yaml_record_review/Nickel_II_chloride_hexahydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:53542 hydrate identity passes, but TRACE_ELEMENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-56dad6fef4f687c1
    - ev-1ec23ab89fe0d73b
  - name: legacy-native-ids
    value: '["SEM:2088f1f36a9e09fb3923","SEM:81e7587b611822fb1611"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1ec23ab89fe0d73b
    - ev-56dad6fef4f687c1
    - ev-9940b56bc5b1b2a0
- assessment_id: a-abeaf053fb950d22
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-77687c39e6747459
  evidence_ids:
  - ev-56dad6fef4f687c1
  - ev-abeaf053fb950d22
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-56dad6fef4f687c1
    - ev-abeaf053fb950d22
findings:
- finding_id: rec-f-21c2f22008ac704a
  issue_key: mim-reconciliation-role-support-77687c39e6747459
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Nickel (II) chloride hexahydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-77687c39e6747459
  evidence_ids:
  - ev-56dad6fef4f687c1
  - ev-abeaf053fb950d22
  - ev-fdb8dadf0094d383
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-21c2f22008ac704a
actions:
- action_id: rec-action-21c2f22008ac704a
  description: 'Reassess prediction-only role support: Nickel (II) chloride hexahydrate'
  finding_ids:
  - rec-f-21c2f22008ac704a
  target_ids:
  - record-77687c39e6747459
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nickel_II_chloride_hexahydrate.yaml
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
