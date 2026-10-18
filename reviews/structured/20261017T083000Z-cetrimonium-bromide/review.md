# Per-record structured review: Cetrimonium_Bromide (data/ingredients/mapped/Cetrimonium_Bromide.yaml)

- Review: 20261017T083000Z-cetrimonium-bromide
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cetrimonium_Bromide (data/ingredients/mapped/Cetrimonium_Bromide.yaml, record-9282c12230031b00, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cetrimonium_Bromide.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cetrimonium_Bromide.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9282c12230031b00 | data/ingredients/mapped/Cetrimonium_Bromide.yaml | maintained | Cetrimonium_Bromide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9282c12230031b00 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9282c12230031b00 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9282c12230031b00 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9282c12230031b00.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-9282c12230031b00.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T11:42:54Z; reviewed SHA-256=6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e; current SHA-256=6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e; hash_changed=False. Reports=["reports/yaml_record_review/Cetrimonium_Bromide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CAS-derived CHEBI cetrimonium bromide identity, structure fields, exact synonym, surfactant role, zero occurrence count, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-9282c12230031b00.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-9282c12230031b00: Reassess prediction-only or empty role support: Cetrimonium_Bromide

major / open / confirmed; issue key: mim-reconciliation-role-support-9282c12230031b00.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-9282c12230031b00

Reassess prediction-only or empty role support: Cetrimonium_Bromide

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c73b4d5656718184 | data/ingredients/mapped/Cetrimonium_Bromide.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[699],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3567","line":701,"mapping_status":"MAPPED","ontology_id":"CHEBI:3567","preferred_term":"Cetrimonium bromide"}],"identifier":"CHEBI:3567","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3567","ontology_label":"cetyltrimethylammonium bromide","ontology_source":"CHEBI"},"preferred_term":"Cetrimonium bromide","sssom_rows":[{"data_row":728,"object_id":"CHEBI:3567","object_label":"cetyltrimethylammonium bromide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cetrimonium_Bromide","synonym_count":1} |
| ev-c6a2ca23fbbdb2e0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [699] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cf56db4018dc3a85 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cetrimonium_Bromide; data-row positions=[728] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":728,"object_id":"CHEBI:3567","object_label":"cetyltrimethylammonium bromide","other":"N,N,N-trimethylhexadecan-1-aminium bromide&#124;CAS:57-09-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Cetrimonium_Bromide","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-3b00f1a59ec8b88b | docs/data/mapped_ingredients.csv; CSV lines=[701] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3567","line":701,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3567","preferred_term":"Cetrimonium bromide","total_occurrences":"0"}] |
| ev-c3849f8bda2d75d3 | reports/yaml_record_review/Cetrimonium_Bromide.md; &#96;data/ingredients/mapped/Cetrimonium_Bromide.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:40; Completeness:55; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-887cf80c77f957d1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1830] | context_only | [{"current_record_sha256":"6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e","finding_id":"SEM:3d2050e7de4637cde231","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cetrimonium-bromide
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cetrimonium_Bromide (data/ingredients/mapped/Cetrimonium_Bromide.yaml)'
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
summary: Per-record structured review for Cetrimonium_Bromide (data/ingredients/mapped/Cetrimonium_Bromide.yaml,
  record-9282c12230031b00, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cetrimonium_Bromide.yaml
    sha256: 6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e
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
  - path: reports/yaml_record_review/Cetrimonium_Bromide.md
    sha256: 8d03ab8701c00a055b08b5fd89843fca8e4258af77bd741ade6533ca924be5cb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9282c12230031b00
  path: data/ingredients/mapped/Cetrimonium_Bromide.yaml
  label: Cetrimonium_Bromide
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cetrimonium_Bromide.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cetrimonium_Bromide.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cetrimonium_Bromide.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9282c12230031b00
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c73b4d5656718184
  - ev-c6a2ca23fbbdb2e0
  - ev-cf56db4018dc3a85
  - ev-3b00f1a59ec8b88b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c73b4d5656718184
  - ev-887cf80c77f957d1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c3849f8bda2d75d3
  - ev-887cf80c77f957d1
evidence:
- evidence_id: ev-c73b4d5656718184
  kind: record_content
  reference: data/ingredients/mapped/Cetrimonium_Bromide.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[699],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3567","line":701,"mapping_status":"MAPPED","ontology_id":"CHEBI:3567","preferred_term":"Cetrimonium
    bromide"}],"identifier":"CHEBI:3567","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:3567","ontology_label":"cetyltrimethylammonium
    bromide","ontology_source":"CHEBI"},"preferred_term":"Cetrimonium bromide","sssom_rows":[{"data_row":728,"object_id":"CHEBI:3567","object_label":"cetyltrimethylammonium
    bromide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cetrimonium_Bromide","synonym_count":1}'
  snapshot_sha256: 6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e
- evidence_id: ev-c6a2ca23fbbdb2e0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [699]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cf56db4018dc3a85
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cetrimonium_Bromide; data-row positions=[728]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":728,"object_id":"CHEBI:3567","object_label":"cetyltrimethylammonium
    bromide","other":"N,N,N-trimethylhexadecan-1-aminium bromide|CAS:57-09-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Cetrimonium_Bromide","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3b00f1a59ec8b88b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[701]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3567","line":701,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3567","preferred_term":"Cetrimonium
    bromide","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c3849f8bda2d75d3
  kind: prior_review
  reference: reports/yaml_record_review/Cetrimonium_Bromide.md
  locator: '`data/ingredients/mapped/Cetrimonium_Bromide.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:40; Completeness:55; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8d03ab8701c00a055b08b5fd89843fca8e4258af77bd741ade6533ca924be5cb
  quote: 'Recommended Edits:

    - None for this record.'
- evidence_id: ev-887cf80c77f957d1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1830]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e","finding_id":"SEM:3d2050e7de4637cde231","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9bb26cb455f49e59
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c73b4d5656718184
  - ev-c6a2ca23fbbdb2e0
  - ev-cf56db4018dc3a85
  - ev-3b00f1a59ec8b88b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c2686b9214ce3030
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c3849f8bda2d75d3
  - ev-c73b4d5656718184
  - ev-887cf80c77f957d1
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T11:42:54Z;
    reviewed SHA-256=6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e;
    current SHA-256=6e26768c9eab61f7864a4224811c20d86e7ec1eae8e7e0e634a82ed687fa917e;
    hash_changed=False. Reports=["reports/yaml_record_review/Cetrimonium_Bromide.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CAS-derived CHEBI cetrimonium bromide identity, structure fields, exact synonym,
    surfactant role, zero occurrence count, SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:3d2050e7de4637cde231"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c73b4d5656718184
    - ev-c3849f8bda2d75d3
    - ev-887cf80c77f957d1
- assessment_id: a-role-9282c12230031b00
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c73b4d5656718184
  - ev-887cf80c77f957d1
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c73b4d5656718184
    - ev-887cf80c77f957d1
findings:
- finding_id: rec-f-role-9282c12230031b00
  issue_key: mim-reconciliation-role-support-9282c12230031b00
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Cetrimonium_Bromide'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-9282c12230031b00
  evidence_ids:
  - ev-c73b4d5656718184
  - ev-887cf80c77f957d1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cetrimonium_Bromide.yaml
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
- action_id: rec-act-role-9282c12230031b00
  description: 'Reassess prediction-only or empty role support: Cetrimonium_Bromide'
  finding_ids:
  - rec-f-role-9282c12230031b00
  target_ids:
  - record-9282c12230031b00
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cetrimonium_Bromide.yaml
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
