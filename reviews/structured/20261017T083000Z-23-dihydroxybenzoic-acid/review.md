# Per-record structured review: 23-dihydroxybenzoic_Acid (data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml)

- Review: 20261017T083000Z-23-dihydroxybenzoic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 23-dihydroxybenzoic_Acid (data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml, record-0820d4473912e17e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0820d4473912e17e | data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml | maintained | 23-dihydroxybenzoic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0820d4473912e17e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0820d4473912e17e | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0820d4473912e17e | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0820d4473912e17e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0820d4473912e17e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:45Z; reviewed SHA-256=a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401; current SHA-256=a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401; hash_changed=False. Reports=["reports/yaml_record_review/23-dihydroxybenzoic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, occurrence count, SSSOM, and aggregate pass, but CARBON_SOURCE is only supported by in-session LLM evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-0820d4473912e17e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-52b001b8f5082104: Reassess prediction-only role support: 2,3-dihydroxybenzoic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-0820d4473912e17e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-52b001b8f5082104

Reassess prediction-only role support: 2,3-dihydroxybenzoic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e0ecd34d2534ff72 | data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18026","line":342,"mapping_status":"MAPPED","ontology_id":"CHEBI:18026","preferred_term":"2,3-dihydroxybenzoic acid"}],"identifier":"CHEBI:18026","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18026","ontology_label":"2,3-dihydroxybenzoic acid","ontology_source":"CHEBI"},"preferred_term":"2,3-dihydroxybenzoic acid","sssom_rows":[{"data_row":108,"object_id":"CHEBI:18026","object_label":"2,3-dihydroxybenzoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:23-dihydroxybenzoic_Acid","synonym_count":8} |
| ev-ab8c558ad1914abd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [340] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a0b47d66b652d95f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:23-dihydroxybenzoic_Acid; data-row positions=[108] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":108,"object_id":"CHEBI:18026","object_label":"2,3-dihydroxybenzoic acid","other":"2,3 DHB&#124;2,3-DIHYDROXY-BENZOIC ACID&#124;2-pyrocatechuic acid&#124;3-hydroxysalicylic acid&#124;DOBK&#124;catechol-3-carboxylic acid&#124;o-pyrocatechuic acid&#124;pyrocatechuic acid&#124;CAS:303-38-8","predicate_id":"skos:exactMatch","subject_id":"MIM:23-dihydroxybenzoic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-54fc9ff11a98ce46 | docs/data/mapped_ingredients.csv; CSV lines=[342] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18026","line":342,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:18026","preferred_term":"2,3-dihydroxybenzoic acid","total_occurrences":"2"}] |
| ev-fdb2e96b3289d3b7 | reports/yaml_record_review/23-dihydroxybenzoic_Acid.md; &#96;data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:39; Completeness:55; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8e0b711bf51ad9f3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[89,1372] | context_only | [{"current_record_sha256":"a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401","finding_id":"SEM:c98fafed88f67be64bf8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401","finding_id":"SEM:9c811b172767eb656df5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-446bf9ebcce7ca47 | data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-389850a3fdbf7c45 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-52b001b8f5082104] | context_only | Predecessor structured review finding f-52b001b8f5082104 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-23-dihydroxybenzoic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 23-dihydroxybenzoic_Acid (data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml)'
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
summary: Per-record structured review for 23-dihydroxybenzoic_Acid (data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml,
  record-0820d4473912e17e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
    sha256: a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/23-dihydroxybenzoic_Acid.md
    sha256: fe5e82d63d20c4c0f403a0e2b107bc759faac538e651c209787f5e5509d600e4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0820d4473912e17e
  path: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
  label: 23-dihydroxybenzoic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0820d4473912e17e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0820d4473912e17e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0820d4473912e17e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0820d4473912e17e
evidence:
- evidence_id: ev-e0ecd34d2534ff72
  kind: record_content
  reference: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18026","line":342,"mapping_status":"MAPPED","ontology_id":"CHEBI:18026","preferred_term":"2,3-dihydroxybenzoic
    acid"}],"identifier":"CHEBI:18026","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18026","ontology_label":"2,3-dihydroxybenzoic
    acid","ontology_source":"CHEBI"},"preferred_term":"2,3-dihydroxybenzoic acid","sssom_rows":[{"data_row":108,"object_id":"CHEBI:18026","object_label":"2,3-dihydroxybenzoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:23-dihydroxybenzoic_Acid","synonym_count":8}'
  snapshot_sha256: a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401
- evidence_id: ev-ab8c558ad1914abd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [340]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a0b47d66b652d95f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:23-dihydroxybenzoic_Acid; data-row positions=[108]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":108,"object_id":"CHEBI:18026","object_label":"2,3-dihydroxybenzoic
    acid","other":"2,3 DHB|2,3-DIHYDROXY-BENZOIC ACID|2-pyrocatechuic acid|3-hydroxysalicylic
    acid|DOBK|catechol-3-carboxylic acid|o-pyrocatechuic acid|pyrocatechuic acid|CAS:303-38-8","predicate_id":"skos:exactMatch","subject_id":"MIM:23-dihydroxybenzoic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-54fc9ff11a98ce46
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[342]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18026","line":342,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:18026","preferred_term":"2,3-dihydroxybenzoic
    acid","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-fdb2e96b3289d3b7
  kind: prior_review
  reference: reports/yaml_record_review/23-dihydroxybenzoic_Acid.md
  locator: '`data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml`:2; Verdict:4;
    Identity:11; Validation:25; Evidence:39; Completeness:55; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fe5e82d63d20c4c0f403a0e2b107bc759faac538e651c209787f5e5509d600e4
  quote: "Recommended Edits:\n1. Either remove `CARBON_SOURCE` or replace it with\
    \ inspected\n   formulation-specific evidence that directly supports this exact\
    \ ingredient\n   as a carbon source.\n2. Regenerate `data/curated/mapped_ingredients.yaml`,\n\
    \   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.\n\
    3. Re-run the focused strict/LinkML validators, role/evidence checks,\n   `just\
    \ qc-sssom`, and `just qc-flat-coverage` after those edits."
- evidence_id: ev-8e0b711bf51ad9f3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[89,1372]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401","finding_id":"SEM:c98fafed88f67be64bf8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401","finding_id":"SEM:9c811b172767eb656df5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-446bf9ebcce7ca47
  kind: record_content
  reference: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401
- evidence_id: ev-389850a3fdbf7c45
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-52b001b8f5082104]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-52b001b8f5082104 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-eeefa03ace71549b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0820d4473912e17e
  evidence_ids:
  - ev-e0ecd34d2534ff72
  - ev-ab8c558ad1914abd
  - ev-a0b47d66b652d95f
  - ev-54fc9ff11a98ce46
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c87f87551eddd88f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0820d4473912e17e
  evidence_ids:
  - ev-fdb2e96b3289d3b7
  - ev-e0ecd34d2534ff72
  - ev-8e0b711bf51ad9f3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:45Z;
    reviewed SHA-256=a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401;
    current SHA-256=a9833424856648828345709109550cf6be56264e00acd352a19ad620dc29a401;
    hash_changed=False. Reports=["reports/yaml_record_review/23-dihydroxybenzoic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, occurrence count, SSSOM, and aggregate pass, but CARBON_SOURCE
    is only supported by in-session LLM evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fdb2e96b3289d3b7
    - ev-e0ecd34d2534ff72
  - name: legacy-native-ids
    value: '["SEM:c98fafed88f67be64bf8","SEM:9c811b172767eb656df5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e0ecd34d2534ff72
    - ev-fdb2e96b3289d3b7
    - ev-8e0b711bf51ad9f3
- assessment_id: a-446bf9ebcce7ca47
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0820d4473912e17e
  evidence_ids:
  - ev-fdb2e96b3289d3b7
  - ev-446bf9ebcce7ca47
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fdb2e96b3289d3b7
    - ev-446bf9ebcce7ca47
findings:
- finding_id: rec-f-52b001b8f5082104
  issue_key: mim-reconciliation-role-support-0820d4473912e17e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 2,3-dihydroxybenzoic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0820d4473912e17e
  evidence_ids:
  - ev-fdb2e96b3289d3b7
  - ev-446bf9ebcce7ca47
  - ev-389850a3fdbf7c45
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-52b001b8f5082104
actions:
- action_id: rec-action-52b001b8f5082104
  description: 'Reassess prediction-only role support: 2,3-dihydroxybenzoic acid'
  finding_ids:
  - rec-f-52b001b8f5082104
  target_ids:
  - record-0820d4473912e17e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
