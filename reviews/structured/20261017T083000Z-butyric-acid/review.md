# Per-record structured review: Butyric_Acid (data/ingredients/mapped/Butyric_Acid.yaml)

- Review: 20261017T083000Z-butyric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Butyric_Acid (data/ingredients/mapped/Butyric_Acid.yaml, record-ba3ccf9cc32e64fb, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Butyric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Butyric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ba3ccf9cc32e64fb | data/ingredients/mapped/Butyric_Acid.yaml | maintained | Butyric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ba3ccf9cc32e64fb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ba3ccf9cc32e64fb | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ba3ccf9cc32e64fb | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ba3ccf9cc32e64fb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-ba3ccf9cc32e64fb.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:24:41Z; reviewed SHA-256=421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86; current SHA-256=421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86; hash_changed=False. Reports=["reports/yaml_record_review/Butyric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI butyric acid identity, CAS, synonyms, nutritional roles, occurrence count, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-ba3ccf9cc32e64fb.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-ba3ccf9cc32e64fb: Reassess prediction-only or empty role support: Butyric_Acid

major / open / confirmed; issue key: mim-reconciliation-role-support-ba3ccf9cc32e64fb.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-ba3ccf9cc32e64fb

Reassess prediction-only or empty role support: Butyric_Acid

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7c2913ecffd02ca9 | data/ingredients/mapped/Butyric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[611],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30772","line":613,"mapping_status":"MAPPED","ontology_id":"CHEBI:30772","preferred_term":"Butyric acid"}],"identifier":"CHEBI:30772","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":48,"total_occurrences":48},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30772","ontology_label":"butyric acid","ontology_source":"CHEBI"},"preferred_term":"Butyric acid","sssom_rows":[{"data_row":593,"object_id":"CHEBI:30772","object_label":"butyric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Butyric_Acid","synonym_count":17} |
| ev-aee8ef17c287032e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [611] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0c95dbefcd9b4edb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Butyric_Acid; data-row positions=[593] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":593,"object_id":"CHEBI:30772","object_label":"butyric acid","other":"1-butanoic acid&#124;1-butyric acid&#124;1-propanecarboxylic acid&#124;4:0&#124;BUTANOIC ACID&#124;Buttersaeure&#124;CH3-[CH2]2-COOH&#124;acide butanoique&#124;acide butyrique&#124;butanic acid&#124;butoic acid&#124;ethylacetic acid&#124;n-Butyric acid&#124;n-butanoic acid&#124;propanecarboxylic acid&#124;propylformic acid&#124;CAS:107-92-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Butyric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6ddcf2bb0d69e41c | docs/data/mapped_ingredients.csv; CSV lines=[613] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30772","line":613,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"48","ontology_id":"CHEBI:30772","preferred_term":"Butyric acid","total_occurrences":"48"}] |
| ev-ac08f11bc8b24f44 | reports/yaml_record_review/Butyric_Acid.md; &#96;data/ingredients/mapped/Butyric_Acid.yaml&#96;:2; Verdict:4; Identity:9; Validation:23; Evidence:33; Completeness:51; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9568793ce8a1ce16 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1782] | context_only | [{"current_record_sha256":"421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86","finding_id":"SEM:a6e57c23901d00fcf17e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-butyric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Butyric_Acid (data/ingredients/mapped/Butyric_Acid.yaml)'
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
summary: Per-record structured review for Butyric_Acid (data/ingredients/mapped/Butyric_Acid.yaml,
  record-ba3ccf9cc32e64fb, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Butyric_Acid.yaml
    sha256: 421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Butyric_Acid.md
    sha256: 18a3c30f3048a4a840d5ebdff78ae628416ca7c2f73930bea92008ba595ec03a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ba3ccf9cc32e64fb
  path: data/ingredients/mapped/Butyric_Acid.yaml
  label: Butyric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Butyric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Butyric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Butyric_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ba3ccf9cc32e64fb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-7c2913ecffd02ca9
  - ev-aee8ef17c287032e
  - ev-0c95dbefcd9b4edb
  - ev-6ddcf2bb0d69e41c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-7c2913ecffd02ca9
  - ev-9568793ce8a1ce16
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-ac08f11bc8b24f44
  - ev-9568793ce8a1ce16
evidence:
- evidence_id: ev-7c2913ecffd02ca9
  kind: record_content
  reference: data/ingredients/mapped/Butyric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[611],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30772","line":613,"mapping_status":"MAPPED","ontology_id":"CHEBI:30772","preferred_term":"Butyric
    acid"}],"identifier":"CHEBI:30772","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":48,"total_occurrences":48},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30772","ontology_label":"butyric
    acid","ontology_source":"CHEBI"},"preferred_term":"Butyric acid","sssom_rows":[{"data_row":593,"object_id":"CHEBI:30772","object_label":"butyric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Butyric_Acid","synonym_count":17}'
  snapshot_sha256: 421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86
- evidence_id: ev-aee8ef17c287032e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [611]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0c95dbefcd9b4edb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Butyric_Acid; data-row positions=[593]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":593,"object_id":"CHEBI:30772","object_label":"butyric
    acid","other":"1-butanoic acid|1-butyric acid|1-propanecarboxylic acid|4:0|BUTANOIC
    ACID|Buttersaeure|CH3-[CH2]2-COOH|acide butanoique|acide butyrique|butanic acid|butoic
    acid|ethylacetic acid|n-Butyric acid|n-butanoic acid|propanecarboxylic acid|propylformic
    acid|CAS:107-92-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Butyric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6ddcf2bb0d69e41c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[613]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30772","line":613,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"48","ontology_id":"CHEBI:30772","preferred_term":"Butyric
    acid","total_occurrences":"48"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ac08f11bc8b24f44
  kind: prior_review
  reference: reports/yaml_record_review/Butyric_Acid.md
  locator: '`data/ingredients/mapped/Butyric_Acid.yaml`:2; Verdict:4; Identity:9;
    Validation:23; Evidence:33; Completeness:51; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 18a3c30f3048a4a840d5ebdff78ae628416ca7c2f73930bea92008ba595ec03a
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-9568793ce8a1ce16
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1782]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86","finding_id":"SEM:a6e57c23901d00fcf17e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d7263fb0e9e626f4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-7c2913ecffd02ca9
  - ev-aee8ef17c287032e
  - ev-0c95dbefcd9b4edb
  - ev-6ddcf2bb0d69e41c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-18b3c8218cd1e14c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-ac08f11bc8b24f44
  - ev-7c2913ecffd02ca9
  - ev-9568793ce8a1ce16
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:24:41Z;
    reviewed SHA-256=421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86;
    current SHA-256=421a741e65598a494cbb8c693e06befa025c59bd49fecc32a0d37869192c7c86;
    hash_changed=False. Reports=["reports/yaml_record_review/Butyric_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    butyric acid identity, CAS, synonyms, nutritional roles, occurrence count, SSSOM
    row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:a6e57c23901d00fcf17e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7c2913ecffd02ca9
    - ev-ac08f11bc8b24f44
    - ev-9568793ce8a1ce16
- assessment_id: a-role-ba3ccf9cc32e64fb
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-7c2913ecffd02ca9
  - ev-9568793ce8a1ce16
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7c2913ecffd02ca9
    - ev-9568793ce8a1ce16
findings:
- finding_id: rec-f-role-ba3ccf9cc32e64fb
  issue_key: mim-reconciliation-role-support-ba3ccf9cc32e64fb
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Butyric_Acid'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-ba3ccf9cc32e64fb
  evidence_ids:
  - ev-7c2913ecffd02ca9
  - ev-9568793ce8a1ce16
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Butyric_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-ba3ccf9cc32e64fb
  description: 'Reassess prediction-only or empty role support: Butyric_Acid'
  finding_ids:
  - rec-f-role-ba3ccf9cc32e64fb
  target_ids:
  - record-ba3ccf9cc32e64fb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Butyric_Acid.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
