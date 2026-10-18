# Per-record structured review: Bleomycin_Sulfate (data/ingredients/mapped/Bleomycin_Sulfate.yaml)

- Review: 20261017T083000Z-bleomycin-sulfate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bleomycin_Sulfate (data/ingredients/mapped/Bleomycin_Sulfate.yaml, record-379a688644aba7ab, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bleomycin_Sulfate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bleomycin_Sulfate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-379a688644aba7ab | data/ingredients/mapped/Bleomycin_Sulfate.yaml | maintained | Bleomycin_Sulfate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-379a688644aba7ab | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-379a688644aba7ab | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-379a688644aba7ab | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-379a688644aba7ab.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-379a688644aba7ab.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:04:45Z; reviewed SHA-256=bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d; current SHA-256=bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d; hash_changed=False. Reports=["reports/yaml_record_review/Bleomycin_Sulfate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bleomycin sulfate identity, CAS, selective-agent role, generalized formula, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-379a688644aba7ab.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-379a688644aba7ab: Reassess prediction-only or empty role support: Bleomycin_Sulfate

major / open / confirmed; issue key: mim-reconciliation-role-support-379a688644aba7ab.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-379a688644aba7ab

Reassess prediction-only or empty role support: Bleomycin_Sulfate

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-baef5967a0172754 | data/ingredients/mapped/Bleomycin_Sulfate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[596],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34582","line":598,"mapping_status":"MAPPED","ontology_id":"CHEBI:34582","preferred_term":"Bleomycin sulfate"}],"identifier":"CHEBI:34582","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34582","ontology_label":"bleomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Bleomycin sulfate","sssom_rows":[{"data_row":564,"object_id":"CHEBI:34582","object_label":"bleomycin sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bleomycin_Sulfate","synonym_count":0} |
| ev-bbf29b55ccef9533 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [596] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-afde0500b8f13216 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bleomycin_Sulfate; data-row positions=[564] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":564,"object_id":"CHEBI:34582","object_label":"bleomycin sulfate","other":"CAS:9041-93-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Bleomycin_Sulfate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-941059af2d6e08a3 | docs/data/mapped_ingredients.csv; CSV lines=[598] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:34582","line":598,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:34582","preferred_term":"Bleomycin sulfate","total_occurrences":"0"}] |
| ev-9fc9cb18e88392fa | reports/yaml_record_review/Bleomycin_Sulfate.md; &#96;data/ingredients/mapped/Bleomycin_Sulfate.yaml&#96;:2; Verdict:4; Identity:9; Validation:23; Evidence:33; Completeness:48; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-353bd38937d508e2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1613] | context_only | [{"current_record_sha256":"bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d","finding_id":"SEM:5f963ac4802eb58ab10e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bleomycin-sulfate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bleomycin_Sulfate (data/ingredients/mapped/Bleomycin_Sulfate.yaml)'
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
summary: Per-record structured review for Bleomycin_Sulfate (data/ingredients/mapped/Bleomycin_Sulfate.yaml,
  record-379a688644aba7ab, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bleomycin_Sulfate.yaml
    sha256: bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Bleomycin_Sulfate.md
    sha256: c5067dc0b4afd2401e1e814ece280c39d3c7770a14b7514c19afbae18b8c35cc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-379a688644aba7ab
  path: data/ingredients/mapped/Bleomycin_Sulfate.yaml
  label: Bleomycin_Sulfate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bleomycin_Sulfate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bleomycin_Sulfate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bleomycin_Sulfate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-379a688644aba7ab
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-baef5967a0172754
  - ev-bbf29b55ccef9533
  - ev-afde0500b8f13216
  - ev-941059af2d6e08a3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-baef5967a0172754
  - ev-353bd38937d508e2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-9fc9cb18e88392fa
  - ev-353bd38937d508e2
evidence:
- evidence_id: ev-baef5967a0172754
  kind: record_content
  reference: data/ingredients/mapped/Bleomycin_Sulfate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[596],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34582","line":598,"mapping_status":"MAPPED","ontology_id":"CHEBI:34582","preferred_term":"Bleomycin
    sulfate"}],"identifier":"CHEBI:34582","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34582","ontology_label":"bleomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Bleomycin sulfate","sssom_rows":[{"data_row":564,"object_id":"CHEBI:34582","object_label":"bleomycin
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bleomycin_Sulfate","synonym_count":0}'
  snapshot_sha256: bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d
- evidence_id: ev-bbf29b55ccef9533
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [596]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-afde0500b8f13216
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bleomycin_Sulfate; data-row positions=[564]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":564,"object_id":"CHEBI:34582","object_label":"bleomycin
    sulfate","other":"CAS:9041-93-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Bleomycin_Sulfate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-941059af2d6e08a3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[598]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:34582","line":598,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:34582","preferred_term":"Bleomycin
    sulfate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9fc9cb18e88392fa
  kind: prior_review
  reference: reports/yaml_record_review/Bleomycin_Sulfate.md
  locator: '`data/ingredients/mapped/Bleomycin_Sulfate.yaml`:2; Verdict:4; Identity:9;
    Validation:23; Evidence:33; Completeness:48; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c5067dc0b4afd2401e1e814ece280c39d3c7770a14b7514c19afbae18b8c35cc
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-353bd38937d508e2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1613]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d","finding_id":"SEM:5f963ac4802eb58ab10e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-56252fbdd1f4fc21
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-baef5967a0172754
  - ev-bbf29b55ccef9533
  - ev-afde0500b8f13216
  - ev-941059af2d6e08a3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0f5b0aad8612bf2c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-9fc9cb18e88392fa
  - ev-baef5967a0172754
  - ev-353bd38937d508e2
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:04:45Z;
    reviewed SHA-256=bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d;
    current SHA-256=bb308066ebebc6f0c09d03fc58f85afb37cd793f8af88982c3be851bcfb25c4d;
    hash_changed=False. Reports=["reports/yaml_record_review/Bleomycin_Sulfate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bleomycin sulfate identity, CAS, selective-agent role, generalized formula,
    SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:5f963ac4802eb58ab10e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-baef5967a0172754
    - ev-9fc9cb18e88392fa
    - ev-353bd38937d508e2
- assessment_id: a-role-379a688644aba7ab
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-baef5967a0172754
  - ev-353bd38937d508e2
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-baef5967a0172754
    - ev-353bd38937d508e2
findings:
- finding_id: rec-f-role-379a688644aba7ab
  issue_key: mim-reconciliation-role-support-379a688644aba7ab
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Bleomycin_Sulfate'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-379a688644aba7ab
  evidence_ids:
  - ev-baef5967a0172754
  - ev-353bd38937d508e2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bleomycin_Sulfate.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-379a688644aba7ab
  description: 'Reassess prediction-only or empty role support: Bleomycin_Sulfate'
  finding_ids:
  - rec-f-role-379a688644aba7ab
  target_ids:
  - record-379a688644aba7ab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bleomycin_Sulfate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
