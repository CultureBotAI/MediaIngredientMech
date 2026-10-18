# Per-record structured review: Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate (data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml)

- Review: 20261017T083000Z-galactose-1-phosphate-dipotassium-salt-pentahydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate (data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml, record-8976da602de42b0f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8976da602de42b0f | data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml | maintained | Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8976da602de42b0f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8976da602de42b0f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8976da602de42b0f | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8976da602de42b0f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8976da602de42b0f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:23:32Z; reviewed SHA-256=f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53; current SHA-256=f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53; hash_changed=False. Reports=["reports/yaml_record_review/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close parent and CAS row pass, but stored PubChem structure omits the pentahydrate waters and CARBON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-8976da602de42b0f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6cc4d9c789b497c0: Reassess prediction-only role support: Galactose 1-phosphate dipotassium salt pentahydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-8976da602de42b0f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6cc4d9c789b497c0

Reassess prediction-only role support: Galactose 1-phosphate dipotassium salt pentahydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f58c400689fc269c | data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1036],"raw_equal":true},"docs_rows":[{"identifier":"cas:19046-60-7","line":1038,"mapping_status":"MAPPED","ontology_id":"CHEBI:17973","preferred_term":"Galactose 1-phosphate dipotassium salt pentahydrate"}],"identifier":"cas:19046-60-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17973","ontology_label":"alpha-D-galactose 1-phosphate","ontology_source":"CHEBI"},"preferred_term":"Galactose 1-phosphate dipotassium salt pentahydrate","sssom_rows":[{"data_row":1275,"object_id":"CHEBI:17973","object_label":"alpha-D-galactose 1-phosphate","predicate_id":"skos:closeMatch"},{"data_row":1276,"object_id":"cas:19046-60-7","object_label":"Galactose 1-phosphate dipotassium salt pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","synonym_count":0} |
| ev-dda3f86d06b1f5bb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1036] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e0d72971d222856a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate; data-row positions=[1275,1276] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1275,"object_id":"CHEBI:17973","object_label":"alpha-D-galactose 1-phosphate","other":"CAS:19046-60-7","predicate_id":"skos:closeMatch","subject_id":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":1276,"object_id":"cas:19046-60-7","object_label":"Galactose 1-phosphate dipotassium salt pentahydrate","other":"CAS:19046-60-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e6745e8cd258a979 | docs/data/mapped_ingredients.csv; CSV lines=[1038] | supports | Published identity and count rows inspected: [{"identifier":"cas:19046-60-7","line":1038,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17973","preferred_term":"Galactose 1-phosphate dipotassium salt pentahydrate","total_occurrences":"0"}] |
| ev-e07aef352be9b8bd | reports/yaml_record_review/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.md; &#96;data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:39; Completeness:61; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a0c3ca3ccaece149 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[649,1904] | context_only | [{"current_record_sha256":"f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53","finding_id":"SEM:72d5cdfa12b0ac8f42cc","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53","finding_id":"SEM:12b79898c3ba8df8e9ba","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b396b6686aa5c015 | data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-1e6065e48bf7eeeb | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-6cc4d9c789b497c0] | context_only | Predecessor structured review finding f-6cc4d9c789b497c0 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-galactose-1-phosphate-dipotassium-salt-pentahydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate
  (data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml)'
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
summary: Per-record structured review for Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate
  (data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml,
  record-8976da602de42b0f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
    sha256: f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.md
    sha256: a220f524d993cd1bb776b8eb2dc4c41854ab6763489c72b1293a172017fbcad7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8976da602de42b0f
  path: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
  label: Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8976da602de42b0f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8976da602de42b0f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8976da602de42b0f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8976da602de42b0f
evidence:
- evidence_id: ev-f58c400689fc269c
  kind: record_content
  reference: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1036],"raw_equal":true},"docs_rows":[{"identifier":"cas:19046-60-7","line":1038,"mapping_status":"MAPPED","ontology_id":"CHEBI:17973","preferred_term":"Galactose
    1-phosphate dipotassium salt pentahydrate"}],"identifier":"cas:19046-60-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17973","ontology_label":"alpha-D-galactose
    1-phosphate","ontology_source":"CHEBI"},"preferred_term":"Galactose 1-phosphate
    dipotassium salt pentahydrate","sssom_rows":[{"data_row":1275,"object_id":"CHEBI:17973","object_label":"alpha-D-galactose
    1-phosphate","predicate_id":"skos:closeMatch"},{"data_row":1276,"object_id":"cas:19046-60-7","object_label":"Galactose
    1-phosphate dipotassium salt pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","synonym_count":0}'
  snapshot_sha256: f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53
- evidence_id: ev-dda3f86d06b1f5bb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1036]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e0d72971d222856a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate; data-row
    positions=[1275,1276]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1275,"object_id":"CHEBI:17973","object_label":"alpha-D-galactose
    1-phosphate","other":"CAS:19046-60-7","predicate_id":"skos:closeMatch","subject_id":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":1276,"object_id":"cas:19046-60-7","object_label":"Galactose
    1-phosphate dipotassium salt pentahydrate","other":"CAS:19046-60-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e6745e8cd258a979
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1038]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:19046-60-7","line":1038,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17973","preferred_term":"Galactose
    1-phosphate dipotassium salt pentahydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e07aef352be9b8bd
  kind: prior_review
  reference: reports/yaml_record_review/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.md
  locator: '`data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml`:2;
    Verdict:4; Identity:12; Validation:28; Evidence:39; Completeness:61; Recommended
    Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a220f524d993cd1bb776b8eb2dc4c41854ab6763489c72b1293a172017fbcad7
  quote: "Recommended Edits:\n- Major: replace `pubchem_cid: 87916` and the anhydrous\
    \ formula, SMILES, and\n  InChI in\n  `data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml`\n\
    \  with the PubChem pentahydrate identity, then sync\n  `data/curated/mapped_ingredients.yaml`.\n\
    - Major: replace the provisional `CARBON_SOURCE` role with source-backed\n  evidence\
    \ or remove it.\n- Regenerate final SSSOM and rerun strict validation plus SSSOM\
    \ invariants."
- evidence_id: ev-a0c3ca3ccaece149
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[649,1904]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53","finding_id":"SEM:72d5cdfa12b0ac8f42cc","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53","finding_id":"SEM:12b79898c3ba8df8e9ba","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b396b6686aa5c015
  kind: record_content
  reference: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53
- evidence_id: ev-1e6065e48bf7eeeb
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-6cc4d9c789b497c0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6cc4d9c789b497c0 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-b6920e5daddbfabb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8976da602de42b0f
  evidence_ids:
  - ev-f58c400689fc269c
  - ev-dda3f86d06b1f5bb
  - ev-e0d72971d222856a
  - ev-e6745e8cd258a979
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d84dfba5f460fee8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8976da602de42b0f
  evidence_ids:
  - ev-e07aef352be9b8bd
  - ev-f58c400689fc269c
  - ev-a0c3ca3ccaece149
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:23:32Z;
    reviewed SHA-256=f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53;
    current SHA-256=f5e8481e5f4588940e88d389061bdfee2e23838b653928c4bf3f18ca36c26e53;
    hash_changed=False. Reports=["reports/yaml_record_review/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The close
    parent and CAS row pass, but stored PubChem structure omits the pentahydrate waters
    and CARBON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e07aef352be9b8bd
    - ev-f58c400689fc269c
  - name: legacy-native-ids
    value: '["SEM:72d5cdfa12b0ac8f42cc","SEM:12b79898c3ba8df8e9ba"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f58c400689fc269c
    - ev-e07aef352be9b8bd
    - ev-a0c3ca3ccaece149
- assessment_id: a-b396b6686aa5c015
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8976da602de42b0f
  evidence_ids:
  - ev-e07aef352be9b8bd
  - ev-b396b6686aa5c015
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e07aef352be9b8bd
    - ev-b396b6686aa5c015
findings:
- finding_id: rec-f-6cc4d9c789b497c0
  issue_key: mim-reconciliation-role-support-8976da602de42b0f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Galactose 1-phosphate dipotassium
    salt pentahydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8976da602de42b0f
  evidence_ids:
  - ev-e07aef352be9b8bd
  - ev-b396b6686aa5c015
  - ev-1e6065e48bf7eeeb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-6cc4d9c789b497c0
actions:
- action_id: rec-action-6cc4d9c789b497c0
  description: 'Reassess prediction-only role support: Galactose 1-phosphate dipotassium
    salt pentahydrate'
  finding_ids:
  - rec-f-6cc4d9c789b497c0
  target_ids:
  - record-8976da602de42b0f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
