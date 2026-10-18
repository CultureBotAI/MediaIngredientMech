# Per-record structured review: L-Homoserine (data/ingredients/mapped/L-Homoserine.yaml)

- Review: 20261017T083000Z-l-homoserine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Homoserine (data/ingredients/mapped/L-Homoserine.yaml, record-81d92bfb869740a1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Homoserine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Homoserine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-81d92bfb869740a1 | data/ingredients/mapped/L-Homoserine.yaml | maintained | L-Homoserine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-81d92bfb869740a1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-81d92bfb869740a1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-81d92bfb869740a1 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-81d92bfb869740a1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-81d92bfb869740a1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z; reviewed SHA-256=33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c; current SHA-256=33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c; hash_changed=False. Reports=["reports/yaml_record_review/L-Homoserine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15699 identity, CAS value, PubChem structure, empty occurrence count, and final SSSOM row pass, but AMINO_ACID_SOURCE is only provisional CHEBI-ancestry evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-81d92bfb869740a1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e3aec684eca72c53: Reassess prediction-only role support: L-Homoserine

major / open / confirmed; issue key: mim-reconciliation-role-support-81d92bfb869740a1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e3aec684eca72c53

Reassess prediction-only role support: L-Homoserine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1b01bc8fd8a2397c | data/ingredients/mapped/L-Homoserine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1226],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15699","line":1228,"mapping_status":"MAPPED","ontology_id":"CHEBI:15699","preferred_term":"L-Homoserine"}],"identifier":"CHEBI:15699","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15699","ontology_label":"L-homoserine","ontology_source":"CHEBI"},"preferred_term":"L-Homoserine","sssom_rows":[{"data_row":1578,"object_id":"CHEBI:15699","object_label":"L-homoserine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Homoserine","synonym_count":0} |
| ev-34b7cf7be61cf027 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1226] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4e4f70d086fbbc30 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Homoserine; data-row positions=[1578] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1578,"object_id":"CHEBI:15699","object_label":"L-homoserine","other":"CAS:672-15-1","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Homoserine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d591b846b0e1097b | docs/data/mapped_ingredients.csv; CSV lines=[1228] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15699","line":1228,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15699","preferred_term":"L-Homoserine","total_occurrences":"0"}] |
| ev-6234ea24dffe4714 | reports/yaml_record_review/L-Homoserine.md; &#96;data/ingredients/mapped/L-Homoserine.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bca105123f7818f4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[793,1547] | context_only | [{"current_record_sha256":"33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c","finding_id":"SEM:28a47cbdd64a4262d4e5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c","finding_id":"SEM:80196160a50232b3b9f9","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0b58a2613ba7831d | data/ingredients/mapped/L-Homoserine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-7794121e761a8aea | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-e3aec684eca72c53] | context_only | Predecessor structured review finding f-e3aec684eca72c53 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-homoserine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Homoserine (data/ingredients/mapped/L-Homoserine.yaml)'
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
summary: Per-record structured review for L-Homoserine (data/ingredients/mapped/L-Homoserine.yaml,
  record-81d92bfb869740a1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Homoserine.yaml
    sha256: 33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-Homoserine.md
    sha256: 771d5d3e2387ee36a0fd8b1ed4b5bd338d97a1054194bb6b20f76003b40979ec
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-81d92bfb869740a1
  path: data/ingredients/mapped/L-Homoserine.yaml
  label: L-Homoserine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Homoserine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Homoserine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Homoserine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-81d92bfb869740a1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-81d92bfb869740a1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-81d92bfb869740a1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-81d92bfb869740a1
evidence:
- evidence_id: ev-1b01bc8fd8a2397c
  kind: record_content
  reference: data/ingredients/mapped/L-Homoserine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1226],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15699","line":1228,"mapping_status":"MAPPED","ontology_id":"CHEBI:15699","preferred_term":"L-Homoserine"}],"identifier":"CHEBI:15699","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15699","ontology_label":"L-homoserine","ontology_source":"CHEBI"},"preferred_term":"L-Homoserine","sssom_rows":[{"data_row":1578,"object_id":"CHEBI:15699","object_label":"L-homoserine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Homoserine","synonym_count":0}'
  snapshot_sha256: 33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c
- evidence_id: ev-34b7cf7be61cf027
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1226]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4e4f70d086fbbc30
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Homoserine; data-row positions=[1578]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1578,"object_id":"CHEBI:15699","object_label":"L-homoserine","other":"CAS:672-15-1","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Homoserine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d591b846b0e1097b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1228]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15699","line":1228,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15699","preferred_term":"L-Homoserine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6234ea24dffe4714
  kind: prior_review
  reference: reports/yaml_record_review/L-Homoserine.md
  locator: '`data/ingredients/mapped/L-Homoserine.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:31; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 771d5d3e2387ee36a0fd8b1ed4b5bd338d97a1054194bb6b20f76003b40979ec
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ unless an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-homoserine as\n  an amino acid source.\n- Rerun strict, term, round-trip,\
    \ role, component, and SSSOM validation after\n  the role change."
- evidence_id: ev-bca105123f7818f4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[793,1547]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c","finding_id":"SEM:28a47cbdd64a4262d4e5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c","finding_id":"SEM:80196160a50232b3b9f9","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0b58a2613ba7831d
  kind: record_content
  reference: data/ingredients/mapped/L-Homoserine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c
- evidence_id: ev-7794121e761a8aea
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-e3aec684eca72c53]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e3aec684eca72c53 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-9743fec34656b978
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-81d92bfb869740a1
  evidence_ids:
  - ev-1b01bc8fd8a2397c
  - ev-34b7cf7be61cf027
  - ev-4e4f70d086fbbc30
  - ev-d591b846b0e1097b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-15056791b8dfd2ea
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-81d92bfb869740a1
  evidence_ids:
  - ev-6234ea24dffe4714
  - ev-1b01bc8fd8a2397c
  - ev-bca105123f7818f4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z;
    reviewed SHA-256=33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c;
    current SHA-256=33e3ecca2d886332e6bfb9449be92384ba33151f959ec45ebb94d53fc06a875c;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Homoserine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15699
    identity, CAS value, PubChem structure, empty occurrence count, and final SSSOM
    row pass, but AMINO_ACID_SOURCE is only provisional CHEBI-ancestry evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6234ea24dffe4714
    - ev-1b01bc8fd8a2397c
  - name: legacy-native-ids
    value: '["SEM:28a47cbdd64a4262d4e5","SEM:80196160a50232b3b9f9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1b01bc8fd8a2397c
    - ev-6234ea24dffe4714
    - ev-bca105123f7818f4
- assessment_id: a-0b58a2613ba7831d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81d92bfb869740a1
  evidence_ids:
  - ev-6234ea24dffe4714
  - ev-0b58a2613ba7831d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6234ea24dffe4714
    - ev-0b58a2613ba7831d
findings:
- finding_id: rec-f-e3aec684eca72c53
  issue_key: mim-reconciliation-role-support-81d92bfb869740a1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Homoserine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81d92bfb869740a1
  evidence_ids:
  - ev-6234ea24dffe4714
  - ev-0b58a2613ba7831d
  - ev-7794121e761a8aea
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Homoserine.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-e3aec684eca72c53
actions:
- action_id: rec-action-e3aec684eca72c53
  description: 'Reassess prediction-only role support: L-Homoserine'
  finding_ids:
  - rec-f-e3aec684eca72c53
  target_ids:
  - record-81d92bfb869740a1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Homoserine.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
