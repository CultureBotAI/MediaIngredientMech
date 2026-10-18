# Per-record structured review: L-cysteine_Hcl_X_H2o (data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml)

- Review: 20261017T083000Z-l-cysteine-hcl-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-cysteine_Hcl_X_H2o (data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml, record-2b5203a714a51b55, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2b5203a714a51b55 | data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml | maintained | L-cysteine_Hcl_X_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2b5203a714a51b55 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2b5203a714a51b55 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2b5203a714a51b55 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2b5203a714a51b55.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2b5203a714a51b55.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:48:09Z; reviewed SHA-256=1b13fecbe7cba7143af066aebb2322f97fc880d1a3668abcc7bbdd3df6c581a9; current SHA-256=62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8; hash_changed=True. Reports=["reports/yaml_record_review/L-cysteine_Hcl_X_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91248 monohydrate identity, CAS value, PubChem structure, and duplicate merge pass, but final SSSOM exports concentration/no-water tokens and AMINO_ACID_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-2b5203a714a51b55.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2a0aea956c784821: Reassess prediction-only role support: L-Cysteine HCl x H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-2b5203a714a51b55.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2a0aea956c784821

Reassess prediction-only role support: L-Cysteine HCl x H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6e973572b90b9940 | data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1244],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91248","line":1246,"mapping_status":"MAPPED","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine HCl x H2O"}],"identifier":"CHEBI:91248","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1767,"edge_count":1767,"occurrences":1768},"occurrence_statistics":{"media_count":1767,"total_occurrences":1768},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91248","ontology_label":"L-cysteine hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine HCl x H2O","sssom_rows":[{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine_Hcl_X_H2o","synonym_count":27} |
| ev-4730c340dae4b226 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1244] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-189209ee5e19cce5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-cysteine_Hcl_X_H2o; data-row positions=[1608] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine hydrochloride hydrate","other":"L--Cysteine\u30fbHCl\u30fbH2O&#124;L-Cysteine\u30fbHCl\u30fbH2O&#124;L--Cysteine HCl H2O&#124;L-Cysteine HCl monohydrate&#124;(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride monohydrate&#124;L-Cysteine hydrochloride monohydrate&#124;L-Cysteine monohydrate monochloride&#124;L-cysteine HCl.H2O&#124;L-Cysteine-HCl x H2O&#124;Cysteine hydrochloride&#124;Cysteine-HCl x H2O&#124;Cysteine-HCl\u00b7H2O&#124;Cysteine-HCl\u2219H2O&#124;Cysteine-HCl\u22c5H2O&#124;L-Cysteine-HCl\u00b7H2O&#124;(1R)-1-carboxy-2-sulfanylethan-1-aminium chloride--water (1/1)&#124;L-cysteine hydrochloride--water (1/1)&#124;Cystein-HCl&#124;CAS:7048-04-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-cysteine_Hcl_X_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ccfc0de4a0778832 | docs/data/mapped_ingredients.csv; CSV lines=[1246] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:91248","line":1246,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1767","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine HCl x H2O","total_occurrences":"1768"}] |
| ev-0644f174fb2a2dec | reports/yaml_record_review/L-cysteine_Hcl_X_H2o.md; &#96;data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:28; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4a81c501b28a0103 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[812,1396] | context_only | [{"current_record_sha256":"62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8","finding_id":"SEM:2ad96181d4300621b85a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8","finding_id":"SEM:4d83bd1c63412ae89bb9","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1a73f18554b42d87 | data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1244],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91248","line":1246,"mapping_status":"MAPPED","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine HCl x H2O"}],"identifier":"CHEBI:91248","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1767,"edge_count":1767,"occurrences":1768},"occurrence_statistics":{"media_count":1767,"total_occurrences":1768},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91248","ontology_label":"L-cysteine hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine HCl x H2O","sssom_rows":[{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine_Hcl_X_H2o","synonym_count":27} |
| ev-f74f36989b928308 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-2a0aea956c784821] | context_only | Predecessor structured review finding f-2a0aea956c784821 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-cysteine-hcl-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-cysteine_Hcl_X_H2o (data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml)'
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
summary: Per-record structured review for L-cysteine_Hcl_X_H2o (data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml,
  record-2b5203a714a51b55, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
    sha256: 62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-cysteine_Hcl_X_H2o.md
    sha256: da7a3782402c25c0aca6db5398055484796c5334e284f03cefe0e0e728216734
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2b5203a714a51b55
  path: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
  label: L-cysteine_Hcl_X_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2b5203a714a51b55
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-6e973572b90b9940
  - ev-4730c340dae4b226
  - ev-189209ee5e19cce5
  - ev-ccfc0de4a0778832
  - ev-1a73f18554b42d87
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-6e973572b90b9940
  - ev-4a81c501b28a0103
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-0644f174fb2a2dec
  - ev-4a81c501b28a0103
  - ev-f74f36989b928308
evidence:
- evidence_id: ev-6e973572b90b9940
  kind: record_content
  reference: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1244],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91248","line":1246,"mapping_status":"MAPPED","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine
    HCl x H2O"}],"identifier":"CHEBI:91248","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1767,"edge_count":1767,"occurrences":1768},"occurrence_statistics":{"media_count":1767,"total_occurrences":1768},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91248","ontology_label":"L-cysteine
    hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine
    HCl x H2O","sssom_rows":[{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine
    hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine_Hcl_X_H2o","synonym_count":27}'
  snapshot_sha256: 62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8
- evidence_id: ev-4730c340dae4b226
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1244]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-189209ee5e19cce5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-cysteine_Hcl_X_H2o; data-row positions=[1608]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine
    hydrochloride hydrate","other":"L--Cysteine\u30fbHCl\u30fbH2O|L-Cysteine\u30fbHCl\u30fbH2O|L--Cysteine
    HCl H2O|L-Cysteine HCl monohydrate|(2R)-2-Amino-3-sulfanyl-propanoic acid hydrochloride
    monohydrate|L-Cysteine hydrochloride monohydrate|L-Cysteine monohydrate monochloride|L-cysteine
    HCl.H2O|L-Cysteine-HCl x H2O|Cysteine hydrochloride|Cysteine-HCl x H2O|Cysteine-HCl\u00b7H2O|Cysteine-HCl\u2219H2O|Cysteine-HCl\u22c5H2O|L-Cysteine-HCl\u00b7H2O|(1R)-1-carboxy-2-sulfanylethan-1-aminium
    chloride--water (1/1)|L-cysteine hydrochloride--water (1/1)|Cystein-HCl|CAS:7048-04-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-cysteine_Hcl_X_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ccfc0de4a0778832
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1246]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:91248","line":1246,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1767","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine
    HCl x H2O","total_occurrences":"1768"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0644f174fb2a2dec
  kind: prior_review
  reference: reports/yaml_record_review/L-cysteine_Hcl_X_H2o.md
  locator: '`data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:28; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: da7a3782402c25c0aca6db5398055484796c5334e284f03cefe0e0e728216734
  quote: "Recommended Edits:\n- Major: remove concentration-qualified `Cystein-HCl\
    \ x 2 H2O (5% (w/v))` and\n  anhydrous `Cystein-HCl` from\n  `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml`.\n\
    - Major: either replace\n  `nutritional_roles.AMINO_ACID_SOURCE` with source-backed\
    \ evidence for this\n  exact monohydrate, or remove the provisional role.\n- Sync\
    \ the aggregate copy and regenerate the SSSOM/docs products; rerun strict,\n \
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-4a81c501b28a0103
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[812,1396]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8","finding_id":"SEM:2ad96181d4300621b85a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8","finding_id":"SEM:4d83bd1c63412ae89bb9","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1a73f18554b42d87
  kind: record_content
  reference: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1244],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91248","line":1246,"mapping_status":"MAPPED","ontology_id":"CHEBI:91248","preferred_term":"L-Cysteine
    HCl x H2O"}],"identifier":"CHEBI:91248","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1767,"edge_count":1767,"occurrences":1768},"occurrence_statistics":{"media_count":1767,"total_occurrences":1768},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91248","ontology_label":"L-cysteine
    hydrochloride hydrate","ontology_source":"CHEBI"},"preferred_term":"L-Cysteine
    HCl x H2O","sssom_rows":[{"data_row":1608,"object_id":"CHEBI:91248","object_label":"L-cysteine
    hydrochloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-cysteine_Hcl_X_H2o","synonym_count":27}'
  snapshot_sha256: 62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8
- evidence_id: ev-f74f36989b928308
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-2a0aea956c784821]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2a0aea956c784821 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-9a1e45b4e393d668
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-6e973572b90b9940
  - ev-4730c340dae4b226
  - ev-189209ee5e19cce5
  - ev-ccfc0de4a0778832
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6e292b98cebcd5ec
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-0644f174fb2a2dec
  - ev-6e973572b90b9940
  - ev-4a81c501b28a0103
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:48:09Z;
    reviewed SHA-256=1b13fecbe7cba7143af066aebb2322f97fc880d1a3668abcc7bbdd3df6c581a9;
    current SHA-256=62f2fc203583507010c6ceed694f1f9622973699d3387f1d6b66b0b61107bca8;
    hash_changed=True. Reports=["reports/yaml_record_review/L-cysteine_Hcl_X_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91248 monohydrate identity, CAS value, PubChem structure, and duplicate
    merge pass, but final SSSOM exports concentration/no-water tokens and AMINO_ACID_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0644f174fb2a2dec
    - ev-6e973572b90b9940
  - name: legacy-native-ids
    value: '["SEM:2ad96181d4300621b85a","SEM:4d83bd1c63412ae89bb9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6e973572b90b9940
    - ev-0644f174fb2a2dec
    - ev-4a81c501b28a0103
- assessment_id: a-1a73f18554b42d87
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-0644f174fb2a2dec
  - ev-1a73f18554b42d87
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0644f174fb2a2dec
    - ev-1a73f18554b42d87
findings:
- finding_id: rec-f-2a0aea956c784821
  issue_key: mim-reconciliation-role-support-2b5203a714a51b55
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Cysteine HCl x H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2b5203a714a51b55
  evidence_ids:
  - ev-0644f174fb2a2dec
  - ev-1a73f18554b42d87
  - ev-f74f36989b928308
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-2a0aea956c784821
actions:
- action_id: rec-action-2a0aea956c784821
  description: 'Reassess prediction-only role support: L-Cysteine HCl x H2O'
  finding_ids:
  - rec-f-2a0aea956c784821
  target_ids:
  - record-2b5203a714a51b55
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
