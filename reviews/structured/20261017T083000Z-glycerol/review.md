# Per-record structured review: Glycerol (data/ingredients/mapped/Glycerol.yaml)

- Review: 20261017T083000Z-glycerol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycerol (data/ingredients/mapped/Glycerol.yaml, record-153e5251be4c577f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycerol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycerol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-153e5251be4c577f | data/ingredients/mapped/Glycerol.yaml | maintained | Glycerol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-153e5251be4c577f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-153e5251be4c577f | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-153e5251be4c577f | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-153e5251be4c577f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-153e5251be4c577f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:07:22Z; reviewed SHA-256=c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a; current SHA-256=c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a; hash_changed=False. Reports=["reports/yaml_record_review/Glycerol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glycerol identity and source-backed carbon role pass, but ENERGY_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-153e5251be4c577f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6a2b8bd0b450e4f3: Reassess prediction-only role support: Glycerol

major / open / confirmed; issue key: mim-reconciliation-role-support-153e5251be4c577f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6a2b8bd0b450e4f3

Reassess prediction-only role support: Glycerol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5b9d3f35a53105ea | data/ingredients/mapped/Glycerol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1069],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17754","line":1071,"mapping_status":"MAPPED","ontology_id":"CHEBI:17754","preferred_term":"Glycerol"}],"identifier":"CHEBI:17754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":292,"edge_count":292,"occurrences":292},"occurrence_statistics":{"media_count":292,"total_occurrences":292},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17754","ontology_label":"glycerol","ontology_source":"CHEBI"},"preferred_term":"Glycerol","sssom_rows":[{"data_row":1334,"object_id":"CHEBI:17754","object_label":"glycerol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycerol","synonym_count":19} |
| ev-a18ef90896b57b02 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1069] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-af6503e83bf5a758 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycerol; data-row positions=[1334] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1334,"object_id":"CHEBI:17754","object_label":"glycerol","other":"glycerin&#124;Glycerol anhydrous&#124;propane-1,2,3-triol&#124;1,2,3-Propanetriol&#124;1,2,3-Trihydroxypropane&#124;G Glycerol&#124;Glyceritol&#124;Glyzerin&#124;Oelsuess&#124;Propanetriol&#124;Trihydroxypropane&#124;glycerine&#124;CAS:56-81-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycerol","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d08d783e2626048e | docs/data/mapped_ingredients.csv; CSV lines=[1071] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17754","line":1071,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"292","ontology_id":"CHEBI:17754","preferred_term":"Glycerol","total_occurrences":"292"}] |
| ev-0e7aafcdcc5efc22 | reports/yaml_record_review/Glycerol.md; &#96;data/ingredients/mapped/Glycerol.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fae41734b8948e0b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[686,1714] | context_only | [{"current_record_sha256":"c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a","finding_id":"SEM:5ba4f19face3b1bb3c56","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a","finding_id":"SEM:b9c0728e29bd4837e262","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0e20e5ea17fa7682 | data/ingredients/mapped/Glycerol.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-4254cc6fb7a2869d | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-6a2b8bd0b450e4f3] | context_only | Predecessor structured review finding f-6a2b8bd0b450e4f3 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycerol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycerol (data/ingredients/mapped/Glycerol.yaml)'
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
summary: Per-record structured review for Glycerol (data/ingredients/mapped/Glycerol.yaml,
  record-153e5251be4c577f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycerol.yaml
    sha256: c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Glycerol.md
    sha256: 525f8ee6dc329500d1d6a99a4c2297a9185734d403f42b28e4ed09b2d02a0a50
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-153e5251be4c577f
  path: data/ingredients/mapped/Glycerol.yaml
  label: Glycerol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycerol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycerol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-153e5251be4c577f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-153e5251be4c577f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-153e5251be4c577f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-153e5251be4c577f
evidence:
- evidence_id: ev-5b9d3f35a53105ea
  kind: record_content
  reference: data/ingredients/mapped/Glycerol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1069],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17754","line":1071,"mapping_status":"MAPPED","ontology_id":"CHEBI:17754","preferred_term":"Glycerol"}],"identifier":"CHEBI:17754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":292,"edge_count":292,"occurrences":292},"occurrence_statistics":{"media_count":292,"total_occurrences":292},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17754","ontology_label":"glycerol","ontology_source":"CHEBI"},"preferred_term":"Glycerol","sssom_rows":[{"data_row":1334,"object_id":"CHEBI:17754","object_label":"glycerol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycerol","synonym_count":19}'
  snapshot_sha256: c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a
- evidence_id: ev-a18ef90896b57b02
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1069]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-af6503e83bf5a758
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycerol; data-row positions=[1334]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1334,"object_id":"CHEBI:17754","object_label":"glycerol","other":"glycerin|Glycerol
    anhydrous|propane-1,2,3-triol|1,2,3-Propanetriol|1,2,3-Trihydroxypropane|G Glycerol|Glyceritol|Glyzerin|Oelsuess|Propanetriol|Trihydroxypropane|glycerine|CAS:56-81-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycerol","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d08d783e2626048e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1071]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17754","line":1071,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"292","ontology_id":"CHEBI:17754","preferred_term":"Glycerol","total_occurrences":"292"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0e7aafcdcc5efc22
  kind: prior_review
  reference: reports/yaml_record_review/Glycerol.md
  locator: '`data/ingredients/mapped/Glycerol.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:33; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 525f8ee6dc329500d1d6a99a4c2297a9185734d403f42b28e4ed09b2d02a0a50
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.ENERGY_SOURCE` from\n\
    \  `data/ingredients/mapped/Glycerol.yaml`, or replace the provisional\n  computational\
    \ evidence with inspected source evidence that specifically\n  supports glycerol\
    \ as an energy source."
- evidence_id: ev-fae41734b8948e0b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[686,1714]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a","finding_id":"SEM:5ba4f19face3b1bb3c56","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a","finding_id":"SEM:b9c0728e29bd4837e262","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0e20e5ea17fa7682
  kind: record_content
  reference: data/ingredients/mapped/Glycerol.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a
- evidence_id: ev-4254cc6fb7a2869d
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-6a2b8bd0b450e4f3]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6a2b8bd0b450e4f3 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-bd18b72337180487
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-153e5251be4c577f
  evidence_ids:
  - ev-5b9d3f35a53105ea
  - ev-a18ef90896b57b02
  - ev-af6503e83bf5a758
  - ev-d08d783e2626048e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-166378ecb482f9f6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-153e5251be4c577f
  evidence_ids:
  - ev-0e7aafcdcc5efc22
  - ev-5b9d3f35a53105ea
  - ev-fae41734b8948e0b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:07:22Z;
    reviewed SHA-256=c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a;
    current SHA-256=c70babb47ba9f6da0b803dd52ae1ba9a094e7ed19c66f30b5568ff6a57e5809a;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycerol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact glycerol identity
    and source-backed carbon role pass, but ENERGY_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e7aafcdcc5efc22
    - ev-5b9d3f35a53105ea
  - name: legacy-native-ids
    value: '["SEM:5ba4f19face3b1bb3c56","SEM:b9c0728e29bd4837e262"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5b9d3f35a53105ea
    - ev-0e7aafcdcc5efc22
    - ev-fae41734b8948e0b
- assessment_id: a-0e20e5ea17fa7682
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-153e5251be4c577f
  evidence_ids:
  - ev-0e7aafcdcc5efc22
  - ev-0e20e5ea17fa7682
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e7aafcdcc5efc22
    - ev-0e20e5ea17fa7682
findings:
- finding_id: rec-f-6a2b8bd0b450e4f3
  issue_key: mim-reconciliation-role-support-153e5251be4c577f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glycerol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-153e5251be4c577f
  evidence_ids:
  - ev-0e7aafcdcc5efc22
  - ev-0e20e5ea17fa7682
  - ev-4254cc6fb7a2869d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-6a2b8bd0b450e4f3
actions:
- action_id: rec-action-6a2b8bd0b450e4f3
  description: 'Reassess prediction-only role support: Glycerol'
  finding_ids:
  - rec-f-6a2b8bd0b450e4f3
  target_ids:
  - record-153e5251be4c577f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
