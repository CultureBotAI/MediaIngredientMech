# Per-record structured review: Tyloxapol (data/ingredients/mapped/Tyloxapol.yaml)

- Review: 20261017T083000Z-tyloxapol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tyloxapol (data/ingredients/mapped/Tyloxapol.yaml, record-dbef879267b82021, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tyloxapol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tyloxapol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dbef879267b82021 | data/ingredients/mapped/Tyloxapol.yaml | maintained | Tyloxapol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dbef879267b82021 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-dbef879267b82021 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dbef879267b82021 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dbef879267b82021.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dbef879267b82021.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:17:19Z; reviewed SHA-256=50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8; current SHA-256=50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8; hash_changed=False. Reports=["reports/yaml_record_review/Tyloxapol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity and final SSSOM row pass, but SURFACTANT is provisional in-session LLM evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-dbef879267b82021.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c29d24361a8d2de6: Reassess prediction-only role support: Tyloxapol

major / open / confirmed; issue key: mim-reconciliation-role-support-dbef879267b82021.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c29d24361a8d2de6

Reassess prediction-only role support: Tyloxapol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a46b6e46a5ac07fd | data/ingredients/mapped/Tyloxapol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2019],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:141517","line":2021,"mapping_status":"MAPPED","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol"}],"identifier":"CHEBI:141517","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:141517","ontology_label":"tyloxapol","ontology_source":"CHEBI"},"preferred_term":"Tyloxapol","sssom_rows":[{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tyloxapol","synonym_count":0} |
| ev-0df57ed8c7e51ba6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2019] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-79b545b43d3ce30a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tyloxapol; data-row positions=[2862] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","other":"CAS:25301-02-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Tyloxapol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-a4d876861719188b | docs/data/mapped_ingredients.csv; CSV lines=[2021] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:141517","line":2021,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol","total_occurrences":"2"}] |
| ev-24866f7c4e6a6d06 | reports/yaml_record_review/Tyloxapol.md; &#96;data/ingredients/mapped/Tyloxapol.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:31; Issues:40; Major: &#96;SURFACTANT&#96; is provisional in-session LLM evidence:42; Completeness:59; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-17b423b4181923c6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1330,1963] | context_only | [{"current_record_sha256":"50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8","finding_id":"SEM:bc51e52713904ab30143","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8","finding_id":"SEM:2028d8e9b541635f4a57","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-08b1c8d03d9308fc | data/ingredients/mapped/Tyloxapol.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2019],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:141517","line":2021,"mapping_status":"MAPPED","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol"}],"identifier":"CHEBI:141517","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:141517","ontology_label":"tyloxapol","ontology_source":"CHEBI"},"preferred_term":"Tyloxapol","sssom_rows":[{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tyloxapol","synonym_count":0} |
| ev-854b9f9b4e79618e | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-c29d24361a8d2de6] | context_only | Predecessor structured review finding f-c29d24361a8d2de6 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tyloxapol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tyloxapol (data/ingredients/mapped/Tyloxapol.yaml)'
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
summary: Per-record structured review for Tyloxapol (data/ingredients/mapped/Tyloxapol.yaml,
  record-dbef879267b82021, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tyloxapol.yaml
    sha256: 50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Tyloxapol.md
    sha256: 674e65b7e5446aa14f56352e72514941c3bf5e8428c617522270c0a3b04da364
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dbef879267b82021
  path: data/ingredients/mapped/Tyloxapol.yaml
  label: Tyloxapol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tyloxapol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tyloxapol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tyloxapol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dbef879267b82021
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-a46b6e46a5ac07fd
  - ev-0df57ed8c7e51ba6
  - ev-79b545b43d3ce30a
  - ev-a4d876861719188b
  - ev-08b1c8d03d9308fc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-a46b6e46a5ac07fd
  - ev-17b423b4181923c6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-24866f7c4e6a6d06
  - ev-17b423b4181923c6
  - ev-854b9f9b4e79618e
evidence:
- evidence_id: ev-a46b6e46a5ac07fd
  kind: record_content
  reference: data/ingredients/mapped/Tyloxapol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2019],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:141517","line":2021,"mapping_status":"MAPPED","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol"}],"identifier":"CHEBI:141517","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:141517","ontology_label":"tyloxapol","ontology_source":"CHEBI"},"preferred_term":"Tyloxapol","sssom_rows":[{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tyloxapol","synonym_count":0}'
  snapshot_sha256: 50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8
- evidence_id: ev-0df57ed8c7e51ba6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2019]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-79b545b43d3ce30a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tyloxapol; data-row positions=[2862]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","other":"CAS:25301-02-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Tyloxapol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a4d876861719188b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2021]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:141517","line":2021,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-24866f7c4e6a6d06
  kind: prior_review
  reference: reports/yaml_record_review/Tyloxapol.md
  locator: '`data/ingredients/mapped/Tyloxapol.yaml`:2; Verdict:4; Identity:10; Validation:22;
    Evidence:31; Issues:40; Major: `SURFACTANT` is provisional in-session LLM evidence:42;
    Completeness:59; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 674e65b7e5446aa14f56352e72514941c3bf5e8428c617522270c0a3b04da364
  quote: "Issues:\n\n\nMajor: `SURFACTANT` is provisional in-session LLM evidence:\n\
    The only role assertion is:\n\n```yaml\nphysicochemical_roles:\n- role: SURFACTANT\n\
    \  confidence: 0.6\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Assigned by in-session Claude reasoning (no external API)\n\
    \    curator_note: Provisional in-session LLM role assignment; review recommended.\n\
    ```\n\nThe exact CHEBI identity does not independently curate the surfactant role\
    \ or\nput evidence on that facet.\n\nRecommended Edits:\n- Replace the `SURFACTANT`\
    \ computational prediction with curated\n  database/literature evidence, or remove\
    \ `physicochemical_roles` until such\n  support is added."
- evidence_id: ev-17b423b4181923c6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1330,1963]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8","finding_id":"SEM:bc51e52713904ab30143","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8","finding_id":"SEM:2028d8e9b541635f4a57","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-08b1c8d03d9308fc
  kind: record_content
  reference: data/ingredients/mapped/Tyloxapol.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2019],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:141517","line":2021,"mapping_status":"MAPPED","ontology_id":"CHEBI:141517","preferred_term":"Tyloxapol"}],"identifier":"CHEBI:141517","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:141517","ontology_label":"tyloxapol","ontology_source":"CHEBI"},"preferred_term":"Tyloxapol","sssom_rows":[{"data_row":2862,"object_id":"CHEBI:141517","object_label":"tyloxapol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tyloxapol","synonym_count":0}'
  snapshot_sha256: 50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8
- evidence_id: ev-854b9f9b4e79618e
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-c29d24361a8d2de6]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c29d24361a8d2de6 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-ed20f6621a922e5d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-a46b6e46a5ac07fd
  - ev-0df57ed8c7e51ba6
  - ev-79b545b43d3ce30a
  - ev-a4d876861719188b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7729cbc874fc0beb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-24866f7c4e6a6d06
  - ev-a46b6e46a5ac07fd
  - ev-17b423b4181923c6
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:17:19Z;
    reviewed SHA-256=50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8;
    current SHA-256=50a3e3c7569c8497308a61b1014826b8a0ae728667020d8534218b6b1e6f96a8;
    hash_changed=False. Reports=["reports/yaml_record_review/Tyloxapol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity and final SSSOM row pass, but SURFACTANT is provisional in-session LLM
    evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-24866f7c4e6a6d06
    - ev-a46b6e46a5ac07fd
  - name: legacy-native-ids
    value: '["SEM:bc51e52713904ab30143","SEM:2028d8e9b541635f4a57"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a46b6e46a5ac07fd
    - ev-24866f7c4e6a6d06
    - ev-17b423b4181923c6
- assessment_id: a-08b1c8d03d9308fc
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-24866f7c4e6a6d06
  - ev-08b1c8d03d9308fc
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-24866f7c4e6a6d06
    - ev-08b1c8d03d9308fc
findings:
- finding_id: rec-f-c29d24361a8d2de6
  issue_key: mim-reconciliation-role-support-dbef879267b82021
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tyloxapol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dbef879267b82021
  evidence_ids:
  - ev-24866f7c4e6a6d06
  - ev-08b1c8d03d9308fc
  - ev-854b9f9b4e79618e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tyloxapol.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-c29d24361a8d2de6
actions:
- action_id: rec-action-c29d24361a8d2de6
  description: 'Reassess prediction-only role support: Tyloxapol'
  finding_ids:
  - rec-f-c29d24361a8d2de6
  target_ids:
  - record-dbef879267b82021
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tyloxapol.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
````
