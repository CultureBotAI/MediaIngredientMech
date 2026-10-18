# Per-record structured review: (2)-D-lyxose (data/ingredients/mapped/(2)-D-lyxose.yaml)

- Review: 20261017T083000Z-2-d-lyxose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for (2)-D-lyxose (data/ingredients/mapped/(2)-D-lyxose.yaml, record-5703779de3d5d6d5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/(2)-D-lyxose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/(2)-D-lyxose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5703779de3d5d6d5 | data/ingredients/mapped/(2)-D-lyxose.yaml | maintained | (2)-D-lyxose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | failed | True | record-5703779de3d5d6d5 | Reconcile direct D-lyxose MicrobeDecoder occurrences |
| Role evidence and plausibility check | passed | True | record-5703779de3d5d6d5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5703779de3d5d6d5 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5703779de3d5d6d5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5703779de3d5d6d5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T04:46:10Z; reviewed SHA-256=62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e; current SHA-256=62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e; hash_changed=False. Reports=["reports/yaml_record_review/(2)-D-lyxose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active identity passes, but source_occurrences appears to omit the direct microbedecoder D-lyxose row with count 159.

### Missing direct D-lyxose source occurrence row

quantity: concern. Targets: record-5703779de3d5d6d5.

The local source still contains kgmicrobe.trait:d_lyxose, count 159, while the record retains only the damaged-label count 1. The direct source-count provenance remains unrepresented in this record; media counts must remain separate.

## Findings

### rec-f-444b73747dddc915: Reconcile direct D-lyxose MicrobeDecoder occurrences

major / open / confirmed; issue key: mim-reconciliation-source-count-5703779de3d5d6d5.

The 159 direct D-lyxose source occurrences remain absent from source_occurrences. Verify deduplication against the damaged-label row before preserving both source rows; do not inflate CultureMech media_count.

## Recommended Actions And Acceptance Checks

### rec-action-444b73747dddc915

Reconcile direct D-lyxose MicrobeDecoder occurrences

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c47f5c761d89211f | data/ingredients/mapped/(2)-D-lyxose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[261],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":263,"mapping_status":"MAPPED","ontology_id":"CHEBI:62318","preferred_term":"D-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-lyxose","sssom_rows":[],"sssom_subject":"MIM:(2)-D-lyxose","synonym_count":3} |
| ev-8415d47f688bc31e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [261] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a2a559decb3bad18 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:(2)-D-lyxose; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-5b7e3f2daab7df58 | docs/data/mapped_ingredients.csv; CSV lines=[263] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:62318","line":263,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62318","preferred_term":"D-lyxose","total_occurrences":"0"}] |
| ev-d69679219babeef0 | reports/yaml_record_review/(2)-D-lyxose.md; &#96;data/ingredients/mapped/(2)-D-lyxose.yaml&#96;:2; Verdict:4; Identity:14; Validation:36; Evidence:50; Completeness:85; Recommended Edits:96 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e0e2a024a09f1958 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[4] | context_only | [{"current_record_sha256":"62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e","finding_id":"SEM:cd74f8ddafa04d7e9a9a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-deba3eac5817996f | data/custom/microbedecoder/unmapped_labels.tsv; line 326 | supports | {"category":"biolink:PhenotypicQuality","label":"D-lyxose","occurrences":"159","placeholder_curie":"kgmicrobe.trait:d_lyxose","source_columns":"BacDive_Metabolite_utilization"} |
| ev-e07f5b645ccdb4e7 | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-444b73747dddc915] | context_only | Predecessor structured review finding f-444b73747dddc915 in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-d-lyxose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: (2)-D-lyxose (data/ingredients/mapped/(2)-D-lyxose.yaml)'
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
summary: Per-record structured review for (2)-D-lyxose (data/ingredients/mapped/(2)-D-lyxose.yaml,
  record-5703779de3d5d6d5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/(2)-D-lyxose.yaml
    sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
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
  - path: reports/yaml_record_review/(2)-D-lyxose.md
    sha256: 3a05386e5da75aed7995c2b4abde4f49fae43b92ce0b8c61db514f28afabc1e8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: data/custom/microbedecoder/unmapped_labels.tsv
    sha256: 96975af522c3e55d5bc6f542637e071a30d1191c34a8555eb81f540cb7bfe569
    role: context
targets:
- target_id: record-5703779de3d5d6d5
  path: data/ingredients/mapped/(2)-D-lyxose.yaml
  label: (2)-D-lyxose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(2)-D-lyxose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/(2)-D-lyxose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/(2)-D-lyxose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5703779de3d5d6d5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: failed
  required: true
  summary: Reconcile direct D-lyxose MicrobeDecoder occurrences
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-c47f5c761d89211f
  - ev-8415d47f688bc31e
  - ev-a2a559decb3bad18
  - ev-5b7e3f2daab7df58
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-c47f5c761d89211f
  - ev-e0e2a024a09f1958
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-d69679219babeef0
  - ev-e0e2a024a09f1958
  - ev-e07f5b645ccdb4e7
evidence:
- evidence_id: ev-c47f5c761d89211f
  kind: record_content
  reference: data/ingredients/mapped/(2)-D-lyxose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[261],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":263,"mapping_status":"MAPPED","ontology_id":"CHEBI:62318","preferred_term":"D-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-lyxose","sssom_rows":[],"sssom_subject":"MIM:(2)-D-lyxose","synonym_count":3}'
  snapshot_sha256: 62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e
- evidence_id: ev-8415d47f688bc31e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [261]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a2a559decb3bad18
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:(2)-D-lyxose; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5b7e3f2daab7df58
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[263]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:62318","line":263,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62318","preferred_term":"D-lyxose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d69679219babeef0
  kind: prior_review
  reference: reports/yaml_record_review/(2)-D-lyxose.md
  locator: '`data/ingredients/mapped/(2)-D-lyxose.yaml`:2; Verdict:4; Identity:14;
    Validation:36; Evidence:50; Completeness:85; Recommended Edits:96'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3a05386e5da75aed7995c2b4abde4f49fae43b92ce0b8c61db514f28afabc1e8
  quote: "Recommended Edits:\n1. Update the maintained per-record input\n   `data/ingredients/mapped/(2)-D-lyxose.yaml`\
    \ so\n   `occurrence_statistics.source_occurrences` accounts for both microbedecoder\n\
    \   rows: `kgmicrobe.trait:d_lyxose` with count `159` and\n   `kgmicrobe.trait:2_d_lyxose`\
    \ with count `1`. Append a curation-history event\n   that names the `data/custom/microbedecoder`\
    \ rows as the source, then run\n   `just sync-curated` and regenerate the flat\
    \ docs exports.\n2. Remove or replace the stale top-level `notes` import sentence\
    \ when the\n   occurrence fix is made; the later `curation_history` already records\
    \ why the\n   damaged source string was corrected and the aldehydo record was\
    \ folded in.\n3. Regenerate `mappings/record_research_validation.tsv` from its\
    \ maintained\n   recipe, or mark the stale `(2)-D-lyxose` rows resolved, after\
    \ the\n   occurrence-source fix lands."
- evidence_id: ev-e0e2a024a09f1958
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e","finding_id":"SEM:cd74f8ddafa04d7e9a9a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-deba3eac5817996f
  kind: record_content
  reference: data/custom/microbedecoder/unmapped_labels.tsv
  locator: line 326
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: '{"category":"biolink:PhenotypicQuality","label":"D-lyxose","occurrences":"159","placeholder_curie":"kgmicrobe.trait:d_lyxose","source_columns":"BacDive_Metabolite_utilization"}'
  snapshot_sha256: 96975af522c3e55d5bc6f542637e071a30d1191c34a8555eb81f540cb7bfe569
- evidence_id: ev-e07f5b645ccdb4e7
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-444b73747dddc915]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-444b73747dddc915 in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-d3c0cfc8f7c0328f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-c47f5c761d89211f
  - ev-8415d47f688bc31e
  - ev-a2a559decb3bad18
  - ev-5b7e3f2daab7df58
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-51482c45c61f047d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-d69679219babeef0
  - ev-c47f5c761d89211f
  - ev-e0e2a024a09f1958
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T04:46:10Z;
    reviewed SHA-256=62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e;
    current SHA-256=62258c9bdabaf8728fafb6923345fe4b24b9956069113896acb16e9631c1451e;
    hash_changed=False. Reports=["reports/yaml_record_review/(2)-D-lyxose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active identity
    passes, but source_occurrences appears to omit the direct microbedecoder D-lyxose
    row with count 159.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d69679219babeef0
    - ev-c47f5c761d89211f
  - name: legacy-native-ids
    value: '["SEM:cd74f8ddafa04d7e9a9a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c47f5c761d89211f
    - ev-d69679219babeef0
    - ev-e0e2a024a09f1958
- assessment_id: a-deba3eac5817996f
  area: quantity
  topic: Missing direct D-lyxose source occurrence row
  outcome: concern
  summary: The local source still contains kgmicrobe.trait:d_lyxose, count 159, while
    the record retains only the damaged-label count 1. The direct source-count provenance
    remains unrepresented in this record; media counts must remain separate.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-d69679219babeef0
  - ev-c47f5c761d89211f
  - ev-deba3eac5817996f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d69679219babeef0
    - ev-c47f5c761d89211f
    - ev-deba3eac5817996f
findings:
- finding_id: rec-f-444b73747dddc915
  issue_key: mim-reconciliation-source-count-5703779de3d5d6d5
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile direct D-lyxose MicrobeDecoder occurrences
  description: The 159 direct D-lyxose source occurrences remain absent from source_occurrences.
    Verify deduplication against the damaged-label row before preserving both source
    rows; do not inflate CultureMech media_count.
  target_ids:
  - record-5703779de3d5d6d5
  evidence_ids:
  - ev-d69679219babeef0
  - ev-c47f5c761d89211f
  - ev-deba3eac5817996f
  - ev-e07f5b645ccdb4e7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(2)-D-lyxose.yaml
    role: maintained ingredient
  field_paths:
  - occurrence_statistics.source_occurrences
  tags:
  - reconciliation
  - bundle-by-owner
  - source-count
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024629Z-mim-reconcile-all-batch-01
    finding_id: f-444b73747dddc915
actions:
- action_id: rec-action-444b73747dddc915
  description: Reconcile direct D-lyxose MicrobeDecoder occurrences
  finding_ids:
  - rec-f-444b73747dddc915
  target_ids:
  - record-5703779de3d5d6d5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/(2)-D-lyxose.yaml
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
  with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.
```
