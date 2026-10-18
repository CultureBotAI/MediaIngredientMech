# Per-record structured review: Bromothymol_Blue (data/ingredients/mapped/Bromothymol_Blue.yaml)

- Review: 20261017T083000Z-bromothymol-blue
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bromothymol_Blue (data/ingredients/mapped/Bromothymol_Blue.yaml, record-0277ed0c768d7437, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bromothymol_Blue.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bromothymol_Blue.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0277ed0c768d7437 | data/ingredients/mapped/Bromothymol_Blue.yaml | maintained | Bromothymol_Blue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0277ed0c768d7437 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0277ed0c768d7437 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0277ed0c768d7437 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0277ed0c768d7437.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-0277ed0c768d7437.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:17:57Z; reviewed SHA-256=f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab; current SHA-256=f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab; hash_changed=False. Reports=["reports/yaml_record_review/Bromothymol_Blue.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bromothymol blue identity, CAS, synonyms, pH-indicator role, occurrence count, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-0277ed0c768d7437.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-0277ed0c768d7437: Reassess prediction-only or empty role support: Bromothymol_Blue

major / open / confirmed; issue key: mim-reconciliation-role-support-0277ed0c768d7437.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-0277ed0c768d7437

Reassess prediction-only or empty role support: Bromothymol_Blue

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5591a3cb703c2d20 | data/ingredients/mapped/Bromothymol_Blue.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[605],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86155","line":607,"mapping_status":"MAPPED","ontology_id":"CHEBI:86155","preferred_term":"Bromothymol blue"}],"identifier":"CHEBI:86155","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":174,"edge_count":174,"occurrences":174},"occurrence_statistics":{"media_count":174,"total_occurrences":174},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86155","ontology_label":"bromothymol blue","ontology_source":"CHEBI"},"preferred_term":"Bromothymol blue","sssom_rows":[{"data_row":584,"object_id":"CHEBI:86155","object_label":"bromothymol blue","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromothymol_Blue","synonym_count":5} |
| ev-89f27f8e0c513ebf | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [605] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-81fefa7ef8426866 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bromothymol_Blue; data-row positions=[584] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":584,"object_id":"CHEBI:86155","object_label":"bromothymol blue","other":"3,3-bis[3-bromo-4-hydroxy-2-methyl-5-(propan-2-yl)phenyl]-2,1lambda(6)-benzoxathiole-1,1(3H)-dione&#124;4,4'-(3H-2,1-Benzoxathiol-3-ylidene)bis(2-bromo-3-methyl-6-(1-methylethyl)phenol) S,S-dioxide&#124;Bromthymol blue&#124;bromothymol sulfone phthalein&#124;CAS:76-59-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromothymol_Blue","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-34145a31e103a031 | docs/data/mapped_ingredients.csv; CSV lines=[607] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86155","line":607,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"174","ontology_id":"CHEBI:86155","preferred_term":"Bromothymol blue","total_occurrences":"174"}] |
| ev-cc8b5ba72018473b | reports/yaml_record_review/Bromothymol_Blue.md; &#96;data/ingredients/mapped/Bromothymol_Blue.yaml&#96;:2; Verdict:4; Identity:9; Validation:24; Evidence:34; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a0dc25d8a4ff49a3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1810] | context_only | [{"current_record_sha256":"f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab","finding_id":"SEM:b76de50128728130ea77","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b5348b36424fb4e1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Bromothymol_Blue.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bromothymol-blue
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bromothymol_Blue (data/ingredients/mapped/Bromothymol_Blue.yaml)'
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
summary: Per-record structured review for Bromothymol_Blue (data/ingredients/mapped/Bromothymol_Blue.yaml,
  record-0277ed0c768d7437, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bromothymol_Blue.yaml
    sha256: f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab
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
  - path: reports/yaml_record_review/Bromothymol_Blue.md
    sha256: 5bdac526140b950270ce05e7edbbd559cdfcea5ad294f40ce4f45827ae3475a0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0277ed0c768d7437
  path: data/ingredients/mapped/Bromothymol_Blue.yaml
  label: Bromothymol_Blue
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromothymol_Blue.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bromothymol_Blue.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bromothymol_Blue.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0277ed0c768d7437
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0277ed0c768d7437
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0277ed0c768d7437
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0277ed0c768d7437
evidence:
- evidence_id: ev-5591a3cb703c2d20
  kind: record_content
  reference: data/ingredients/mapped/Bromothymol_Blue.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[605],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86155","line":607,"mapping_status":"MAPPED","ontology_id":"CHEBI:86155","preferred_term":"Bromothymol
    blue"}],"identifier":"CHEBI:86155","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":174,"edge_count":174,"occurrences":174},"occurrence_statistics":{"media_count":174,"total_occurrences":174},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86155","ontology_label":"bromothymol
    blue","ontology_source":"CHEBI"},"preferred_term":"Bromothymol blue","sssom_rows":[{"data_row":584,"object_id":"CHEBI:86155","object_label":"bromothymol
    blue","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromothymol_Blue","synonym_count":5}'
  snapshot_sha256: f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab
- evidence_id: ev-89f27f8e0c513ebf
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [605]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-81fefa7ef8426866
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bromothymol_Blue; data-row positions=[584]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":584,"object_id":"CHEBI:86155","object_label":"bromothymol
    blue","other":"3,3-bis[3-bromo-4-hydroxy-2-methyl-5-(propan-2-yl)phenyl]-2,1lambda(6)-benzoxathiole-1,1(3H)-dione|4,4''-(3H-2,1-Benzoxathiol-3-ylidene)bis(2-bromo-3-methyl-6-(1-methylethyl)phenol)
    S,S-dioxide|Bromthymol blue|bromothymol sulfone phthalein|CAS:76-59-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromothymol_Blue","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-34145a31e103a031
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[607]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86155","line":607,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"174","ontology_id":"CHEBI:86155","preferred_term":"Bromothymol
    blue","total_occurrences":"174"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cc8b5ba72018473b
  kind: prior_review
  reference: reports/yaml_record_review/Bromothymol_Blue.md
  locator: '`data/ingredients/mapped/Bromothymol_Blue.yaml`:2; Verdict:4; Identity:9;
    Validation:24; Evidence:34; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5bdac526140b950270ce05e7edbbd559cdfcea5ad294f40ce4f45827ae3475a0
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-a0dc25d8a4ff49a3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1810]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab","finding_id":"SEM:b76de50128728130ea77","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b5348b36424fb4e1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Bromothymol_Blue.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-be95fb49cb086b1b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0277ed0c768d7437
  evidence_ids:
  - ev-5591a3cb703c2d20
  - ev-89f27f8e0c513ebf
  - ev-81fefa7ef8426866
  - ev-34145a31e103a031
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5b7f4e3f4b1d127a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-0277ed0c768d7437
  evidence_ids:
  - ev-cc8b5ba72018473b
  - ev-5591a3cb703c2d20
  - ev-a0dc25d8a4ff49a3
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T10:17:57Z;
    reviewed SHA-256=f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab;
    current SHA-256=f564008408b0b163148d3ca0b924e31c3602fdad07a349085a4a712d06c64bab;
    hash_changed=False. Reports=["reports/yaml_record_review/Bromothymol_Blue.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bromothymol blue identity, CAS, synonyms, pH-indicator role, occurrence
    count, SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:b76de50128728130ea77"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5591a3cb703c2d20
    - ev-cc8b5ba72018473b
    - ev-a0dc25d8a4ff49a3
- assessment_id: a-role-0277ed0c768d7437
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-0277ed0c768d7437
  evidence_ids:
  - ev-5591a3cb703c2d20
  - ev-b5348b36424fb4e1
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5591a3cb703c2d20
    - ev-b5348b36424fb4e1
findings:
- finding_id: rec-f-role-0277ed0c768d7437
  issue_key: mim-reconciliation-role-support-0277ed0c768d7437
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Bromothymol_Blue'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-0277ed0c768d7437
  evidence_ids:
  - ev-5591a3cb703c2d20
  - ev-b5348b36424fb4e1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromothymol_Blue.yaml
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
- action_id: rec-act-role-0277ed0c768d7437
  description: 'Reassess prediction-only or empty role support: Bromothymol_Blue'
  finding_ids:
  - rec-f-role-0277ed0c768d7437
  target_ids:
  - record-0277ed0c768d7437
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromothymol_Blue.yaml
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
