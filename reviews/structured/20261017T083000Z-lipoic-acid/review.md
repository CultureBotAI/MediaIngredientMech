# Per-record structured review: Α-lipoic_Acid (data/ingredients/mapped/Α-lipoic_Acid.yaml)

- Review: 20261017T083000Z-lipoic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Α-lipoic_Acid (data/ingredients/mapped/Α-lipoic_Acid.yaml, record-b21faf34879b78a3, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Α-lipoic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Α-lipoic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b21faf34879b78a3 | data/ingredients/mapped/Α-lipoic_Acid.yaml | maintained | Α-lipoic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b21faf34879b78a3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b21faf34879b78a3 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b21faf34879b78a3 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b21faf34879b78a3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b21faf34879b78a3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T21:50:39Z; reviewed SHA-256=f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6; current SHA-256=f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6; hash_changed=False. Reports=["reports/yaml_record_review/\u0391-lipoic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected S-lipoic tombstone emits no final SSSOM row and points at the active representative, but stale live-record fields remain.

### Historical provisional-role concern

evidence: unknown. Targets: record-b21faf34879b78a3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-eea7ae64ba6c1a34: Reassess prediction-only role support: α-lipoic acid

minor / deferred / provisional; issue key: mim-reconciliation-role-support-b21faf34879b78a3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2ab3793d23ccd43f | data/ingredients/mapped/Α-lipoic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2088],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16494","line":2090,"mapping_status":"REJECTED","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic acid"}],"identifier":"CHEBI:16494","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1747,"edge_count":1747,"occurrences":1748},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16494","ontology_label":"lipoic acid","ontology_source":"CHEBI"},"preferred_term":"\u03b1-lipoic acid","sssom_rows":[],"sssom_subject":"MIM:\u0391-lipoic_Acid","synonym_count":12} |
| ev-6efd606d1e45196d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2088] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-76be0abda8fe0be7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Α-lipoic_Acid; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-97012c1bdc306d51 | docs/data/mapped_ingredients.csv; CSV lines=[2090] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16494","line":2090,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic acid","total_occurrences":"0"}] |
| ev-3161f554b0ca4473 | reports/yaml_record_review/Α-lipoic_Acid.md; &#96;data/ingredients/mapped/Α-lipoic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:32; Issues:41; Completeness:47; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4d78d317dbb260bb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1366] | context_only | [{"current_record_sha256":"f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6","finding_id":"SEM:7d4a2c88e6a95c3f22ca","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-31128c19b9759007 | data/ingredients/mapped/Α-lipoic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2088],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16494","line":2090,"mapping_status":"REJECTED","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic acid"}],"identifier":"CHEBI:16494","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1747,"edge_count":1747,"occurrences":1748},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16494","ontology_label":"lipoic acid","ontology_source":"CHEBI"},"preferred_term":"\u03b1-lipoic acid","sssom_rows":[],"sssom_subject":"MIM:\u0391-lipoic_Acid","synonym_count":12} |
| ev-ce8aa7f6234f55a6 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-eea7ae64ba6c1a34] | context_only | Predecessor structured review finding f-eea7ae64ba6c1a34 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lipoic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Α-lipoic_Acid (data/ingredients/mapped/Α-lipoic_Acid.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Α-lipoic_Acid (data/ingredients/mapped/Α-lipoic_Acid.yaml,
  record-b21faf34879b78a3, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Α-lipoic_Acid.yaml
    sha256: f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6
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
  - path: reports/yaml_record_review/Α-lipoic_Acid.md
    sha256: 97a5c36463d2f2904bff42075a1c29f4a974080f838b63aa79a5a7fba4516b51
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b21faf34879b78a3
  path: data/ingredients/mapped/Α-lipoic_Acid.yaml
  label: Α-lipoic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Α-lipoic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Α-lipoic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Α-lipoic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b21faf34879b78a3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-2ab3793d23ccd43f
  - ev-6efd606d1e45196d
  - ev-76be0abda8fe0be7
  - ev-97012c1bdc306d51
  - ev-31128c19b9759007
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-2ab3793d23ccd43f
  - ev-4d78d317dbb260bb
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-3161f554b0ca4473
  - ev-4d78d317dbb260bb
  - ev-ce8aa7f6234f55a6
evidence:
- evidence_id: ev-2ab3793d23ccd43f
  kind: record_content
  reference: data/ingredients/mapped/Α-lipoic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2088],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16494","line":2090,"mapping_status":"REJECTED","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic
    acid"}],"identifier":"CHEBI:16494","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1747,"edge_count":1747,"occurrences":1748},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16494","ontology_label":"lipoic
    acid","ontology_source":"CHEBI"},"preferred_term":"\u03b1-lipoic acid","sssom_rows":[],"sssom_subject":"MIM:\u0391-lipoic_Acid","synonym_count":12}'
  snapshot_sha256: f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6
- evidence_id: ev-6efd606d1e45196d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2088]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-76be0abda8fe0be7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Α-lipoic_Acid; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-97012c1bdc306d51
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2090]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16494","line":2090,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3161f554b0ca4473
  kind: prior_review
  reference: reports/yaml_record_review/Α-lipoic_Acid.md
  locator: '`data/ingredients/mapped/Α-lipoic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:32; Issues:41; Completeness:47; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 97a5c36463d2f2904bff42075a1c29f4a974080f838b63aa79a5a7fba4516b51
  quote: "Issues:\n- Minor: the rejected record still carries stale `ingredient_type`,\n\
    \  `chemical_properties`, and provisional `VITAMIN_SOURCE` fields that do not\n\
    \  affect final SSSOM exports.\n\nRecommended Edits:\n- Clear stale live-record\
    \ fields from the rejected tombstone when tombstone\n  cleanup is next run, then\
    \ rerun strict validation and SSSOM publication."
- evidence_id: ev-4d78d317dbb260bb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1366]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6","finding_id":"SEM:7d4a2c88e6a95c3f22ca","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-31128c19b9759007
  kind: record_content
  reference: data/ingredients/mapped/Α-lipoic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2088],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16494","line":2090,"mapping_status":"REJECTED","ontology_id":"CHEBI:16494","preferred_term":"\u03b1-lipoic
    acid"}],"identifier":"CHEBI:16494","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1747,"edge_count":1747,"occurrences":1748},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16494","ontology_label":"lipoic
    acid","ontology_source":"CHEBI"},"preferred_term":"\u03b1-lipoic acid","sssom_rows":[],"sssom_subject":"MIM:\u0391-lipoic_Acid","synonym_count":12}'
  snapshot_sha256: f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6
- evidence_id: ev-ce8aa7f6234f55a6
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-eea7ae64ba6c1a34]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-eea7ae64ba6c1a34 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-08c9fcf04ee95715
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-2ab3793d23ccd43f
  - ev-6efd606d1e45196d
  - ev-76be0abda8fe0be7
  - ev-97012c1bdc306d51
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-00c89bdf3fe8009e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-3161f554b0ca4473
  - ev-2ab3793d23ccd43f
  - ev-4d78d317dbb260bb
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T21:50:39Z;
    reviewed SHA-256=f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6;
    current SHA-256=f7326359f69a4022a6d6399f272109180611423bcd3debc2defccae8fc1ae7b6;
    hash_changed=False. Reports=["reports/yaml_record_review/\u0391-lipoic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The rejected
    S-lipoic tombstone emits no final SSSOM row and points at the active representative,
    but stale live-record fields remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3161f554b0ca4473
    - ev-2ab3793d23ccd43f
  - name: legacy-native-ids
    value: '["SEM:7d4a2c88e6a95c3f22ca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2ab3793d23ccd43f
    - ev-3161f554b0ca4473
    - ev-4d78d317dbb260bb
- assessment_id: a-31128c19b9759007
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-3161f554b0ca4473
  - ev-31128c19b9759007
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3161f554b0ca4473
    - ev-31128c19b9759007
findings:
- finding_id: rec-f-eea7ae64ba6c1a34
  issue_key: mim-reconciliation-role-support-b21faf34879b78a3
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: α-lipoic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b21faf34879b78a3
  evidence_ids:
  - ev-3161f554b0ca4473
  - ev-31128c19b9759007
  - ev-ce8aa7f6234f55a6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Α-lipoic_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-eea7ae64ba6c1a34
actions: []
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
```
