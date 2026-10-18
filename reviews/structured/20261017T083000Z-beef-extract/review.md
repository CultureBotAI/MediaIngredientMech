# Per-record structured review: Beef_Extract (data/ingredients/mapped/Beef_Extract.yaml)

- Review: 20261017T083000Z-beef-extract
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beef_Extract (data/ingredients/mapped/Beef_Extract.yaml, record-da942f09736a0b84, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beef_Extract.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beef_Extract.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-da942f09736a0b84 | data/ingredients/mapped/Beef_Extract.yaml | maintained | Beef_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-da942f09736a0b84 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-da942f09736a0b84 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-da942f09736a0b84 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-da942f09736a0b84.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-da942f09736a0b84.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:24:42Z; reviewed SHA-256=f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23; current SHA-256=f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23; hash_changed=False. Reports=["reports/yaml_record_review/Beef_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact FOODON beef extract mapping, catalog synonyms, removed false-positive CAS, occurrence count, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-da942f09736a0b84.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-da942f09736a0b84: Reassess prediction-only or empty role support: Beef_Extract

major / open / confirmed; issue key: mim-reconciliation-role-support-da942f09736a0b84.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-da942f09736a0b84

Reassess prediction-only or empty role support: Beef_Extract

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-057caea81b39fac7 | data/ingredients/mapped/Beef_Extract.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[563],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03302088","line":565,"mapping_status":"MAPPED","ontology_id":"FOODON:03302088","preferred_term":"Beef extract"}],"identifier":"FOODON:03302088","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":330,"edge_count":330,"occurrences":331},"occurrence_statistics":{"media_count":330,"total_occurrences":331},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03302088","ontology_label":"beef extract","ontology_source":"FOODON"},"preferred_term":"Beef extract","sssom_rows":[{"data_row":498,"object_id":"FOODON:03302088","object_label":"beef extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Extract","synonym_count":8} |
| ev-ae8e849caa968cca | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [563] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cbee03f0fc41a972 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beef_Extract; data-row positions=[498] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":498,"object_id":"FOODON:03302088","object_label":"beef extract","other":"Beef extract(Sigma B-4888)&#124;Beef extract (BD-Difco)&#124;Lab-Lemco beef extract&#124;Bacto beef extract&#124;Bacto Beef Extract (Difco)&#124;Beef extract (BBL)","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Extract","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-66bf92785a5d0b18 | docs/data/mapped_ingredients.csv; CSV lines=[565] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03302088","line":565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"330","ontology_id":"FOODON:03302088","preferred_term":"Beef extract","total_occurrences":"331"}] |
| ev-4117ca46b61d3e26 | reports/yaml_record_review/Beef_Extract.md; &#96;data/ingredients/mapped/Beef_Extract.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:31; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e44635a252f6a387 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1815] | context_only | [{"current_record_sha256":"f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23","finding_id":"SEM:c742dc0d0b18b46f9081","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beef-extract
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beef_Extract (data/ingredients/mapped/Beef_Extract.yaml)'
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
summary: Per-record structured review for Beef_Extract (data/ingredients/mapped/Beef_Extract.yaml,
  record-da942f09736a0b84, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beef_Extract.yaml
    sha256: f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23
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
  - path: reports/yaml_record_review/Beef_Extract.md
    sha256: 82fea110fd294a78e79bb5b43a1f3a6944b376888fb3bf96462565ce447c1666
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-da942f09736a0b84
  path: data/ingredients/mapped/Beef_Extract.yaml
  label: Beef_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Extract.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beef_Extract.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beef_Extract.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-da942f09736a0b84
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-057caea81b39fac7
  - ev-ae8e849caa968cca
  - ev-cbee03f0fc41a972
  - ev-66bf92785a5d0b18
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-057caea81b39fac7
  - ev-e44635a252f6a387
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-4117ca46b61d3e26
  - ev-e44635a252f6a387
evidence:
- evidence_id: ev-057caea81b39fac7
  kind: record_content
  reference: data/ingredients/mapped/Beef_Extract.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[563],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03302088","line":565,"mapping_status":"MAPPED","ontology_id":"FOODON:03302088","preferred_term":"Beef
    extract"}],"identifier":"FOODON:03302088","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":330,"edge_count":330,"occurrences":331},"occurrence_statistics":{"media_count":330,"total_occurrences":331},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03302088","ontology_label":"beef
    extract","ontology_source":"FOODON"},"preferred_term":"Beef extract","sssom_rows":[{"data_row":498,"object_id":"FOODON:03302088","object_label":"beef
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Extract","synonym_count":8}'
  snapshot_sha256: f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23
- evidence_id: ev-ae8e849caa968cca
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [563]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cbee03f0fc41a972
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beef_Extract; data-row positions=[498]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":498,"object_id":"FOODON:03302088","object_label":"beef
    extract","other":"Beef extract(Sigma B-4888)|Beef extract (BD-Difco)|Lab-Lemco
    beef extract|Bacto beef extract|Bacto Beef Extract (Difco)|Beef extract (BBL)","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Extract","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-66bf92785a5d0b18
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[565]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03302088","line":565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"330","ontology_id":"FOODON:03302088","preferred_term":"Beef
    extract","total_occurrences":"331"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4117ca46b61d3e26
  kind: prior_review
  reference: reports/yaml_record_review/Beef_Extract.md
  locator: '`data/ingredients/mapped/Beef_Extract.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:31; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 82fea110fd294a78e79bb5b43a1f3a6944b376888fb3bf96462565ce447c1666
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-e44635a252f6a387
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1815]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23","finding_id":"SEM:c742dc0d0b18b46f9081","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-19916ec393b132f7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-057caea81b39fac7
  - ev-ae8e849caa968cca
  - ev-cbee03f0fc41a972
  - ev-66bf92785a5d0b18
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c212680c4a3e4b02
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-4117ca46b61d3e26
  - ev-057caea81b39fac7
  - ev-e44635a252f6a387
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:24:42Z;
    reviewed SHA-256=f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23;
    current SHA-256=f5d1b31763be5ddf9da97c3bd18075298fee7c2f6dfda2c9ce9b93f128f89d23;
    hash_changed=False. Reports=["reports/yaml_record_review/Beef_Extract.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact FOODON
    beef extract mapping, catalog synonyms, removed false-positive CAS, occurrence
    count, SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:c742dc0d0b18b46f9081"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-057caea81b39fac7
    - ev-4117ca46b61d3e26
    - ev-e44635a252f6a387
- assessment_id: a-role-da942f09736a0b84
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-057caea81b39fac7
  - ev-e44635a252f6a387
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-057caea81b39fac7
    - ev-e44635a252f6a387
findings:
- finding_id: rec-f-role-da942f09736a0b84
  issue_key: mim-reconciliation-role-support-da942f09736a0b84
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beef_Extract'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-da942f09736a0b84
  evidence_ids:
  - ev-057caea81b39fac7
  - ev-e44635a252f6a387
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Extract.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-da942f09736a0b84
  description: 'Reassess prediction-only or empty role support: Beef_Extract'
  finding_ids:
  - rec-f-role-da942f09736a0b84
  target_ids:
  - record-da942f09736a0b84
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Extract.yaml
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
