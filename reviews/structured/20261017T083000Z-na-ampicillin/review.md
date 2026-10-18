# Per-record structured review: Na-ampicillin (data/ingredients/mapped/Na-ampicillin.yaml)

- Review: 20261017T083000Z-na-ampicillin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-ampicillin (data/ingredients/mapped/Na-ampicillin.yaml, record-09fcfa2b32327521, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-ampicillin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-ampicillin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-09fcfa2b32327521 | data/ingredients/mapped/Na-ampicillin.yaml | maintained | Na-ampicillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-09fcfa2b32327521 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-09fcfa2b32327521 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-09fcfa2b32327521 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-09fcfa2b32327521.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-09fcfa2b32327521.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:44:27Z; reviewed SHA-256=def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2; current SHA-256=def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2; hash_changed=False. Reports=["reports/yaml_record_review/Na-ampicillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:34535 ampicillin sodium identity, CAS provenance, synonyms, duplicate merge, and final exact row pass, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-09fcfa2b32327521.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-51bcfdceec1a7afb: Reassess prediction-only role support: Na-ampicillin

major / open / confirmed; issue key: mim-reconciliation-role-support-09fcfa2b32327521.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-51bcfdceec1a7afb

Reassess prediction-only role support: Na-ampicillin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7c2dd2f3119f9335 | data/ingredients/mapped/Na-ampicillin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1458],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34535","line":1460,"mapping_status":"MAPPED","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin"}],"identifier":"CHEBI:34535","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34535","ontology_label":"ampicillin sodium","ontology_source":"CHEBI"},"preferred_term":"Na-ampicillin","sssom_rows":[{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-ampicillin","synonym_count":10} |
| ev-2ff365ec412bd34d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1458] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-545b3f29881a9dc3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-ampicillin; data-row positions=[1963] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin sodium","other":"Austrapen&#124;D(-)-alpha-aminobenzylpenicillin sodium salt&#124;ampicillin natrium&#124;monosodium D-(-)-6-(2-amino-2-phenylacetamido)-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo(3.2.0)heptane-2-carboxylate&#124;sodium (2S,5R,6R)-6-{[(2R)-2-amino-2-phenylacetyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylate&#124;sodium 6beta-[(2R)-2-amino-2-phenylacetamido]-2,2-dimethylpenam-3alpha-carboxylate&#124;sodium D-(-)-alpha-aminobenzylpenicillin&#124;sodium ampicillin&#124;Ampicillin sodium salt&#124;CAS:69-52-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-ampicillin","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-92e3b46108e806c5 | docs/data/mapped_ingredients.csv; CSV lines=[1460] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:34535","line":1460,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin","total_occurrences":"12"}] |
| ev-ca60272c84e70ca6 | reports/yaml_record_review/Na-ampicillin.md; &#96;data/ingredients/mapped/Na-ampicillin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:27; Completeness:41; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a1ede6e44e80a8a8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[968,2007] | context_only | [{"current_record_sha256":"def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2","finding_id":"SEM:9375061634834d76114b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2","finding_id":"SEM:6586f0fa5465c2ab1ea6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d767672b401a68c0 | data/ingredients/mapped/Na-ampicillin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1458],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34535","line":1460,"mapping_status":"MAPPED","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin"}],"identifier":"CHEBI:34535","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34535","ontology_label":"ampicillin sodium","ontology_source":"CHEBI"},"preferred_term":"Na-ampicillin","sssom_rows":[{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-ampicillin","synonym_count":10} |
| ev-7545499aecafa9da | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-51bcfdceec1a7afb] | context_only | Predecessor structured review finding f-51bcfdceec1a7afb in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-ampicillin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-ampicillin (data/ingredients/mapped/Na-ampicillin.yaml)'
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
summary: Per-record structured review for Na-ampicillin (data/ingredients/mapped/Na-ampicillin.yaml,
  record-09fcfa2b32327521, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-ampicillin.yaml
    sha256: def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Na-ampicillin.md
    sha256: 5d99140353468f93aa9a3fb8e3147aa3ebbf411e48a0db40012b506cd3d443ac
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-09fcfa2b32327521
  path: data/ingredients/mapped/Na-ampicillin.yaml
  label: Na-ampicillin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-ampicillin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-ampicillin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-ampicillin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-09fcfa2b32327521
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-7c2dd2f3119f9335
  - ev-2ff365ec412bd34d
  - ev-545b3f29881a9dc3
  - ev-92e3b46108e806c5
  - ev-d767672b401a68c0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-7c2dd2f3119f9335
  - ev-a1ede6e44e80a8a8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-ca60272c84e70ca6
  - ev-a1ede6e44e80a8a8
  - ev-7545499aecafa9da
evidence:
- evidence_id: ev-7c2dd2f3119f9335
  kind: record_content
  reference: data/ingredients/mapped/Na-ampicillin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1458],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34535","line":1460,"mapping_status":"MAPPED","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin"}],"identifier":"CHEBI:34535","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34535","ontology_label":"ampicillin
    sodium","ontology_source":"CHEBI"},"preferred_term":"Na-ampicillin","sssom_rows":[{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin
    sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-ampicillin","synonym_count":10}'
  snapshot_sha256: def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2
- evidence_id: ev-2ff365ec412bd34d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1458]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-545b3f29881a9dc3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-ampicillin; data-row positions=[1963]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin
    sodium","other":"Austrapen|D(-)-alpha-aminobenzylpenicillin sodium salt|ampicillin
    natrium|monosodium D-(-)-6-(2-amino-2-phenylacetamido)-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo(3.2.0)heptane-2-carboxylate|sodium
    (2S,5R,6R)-6-{[(2R)-2-amino-2-phenylacetyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylate|sodium
    6beta-[(2R)-2-amino-2-phenylacetamido]-2,2-dimethylpenam-3alpha-carboxylate|sodium
    D-(-)-alpha-aminobenzylpenicillin|sodium ampicillin|Ampicillin sodium salt|CAS:69-52-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-ampicillin","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-92e3b46108e806c5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1460]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:34535","line":1460,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin","total_occurrences":"12"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ca60272c84e70ca6
  kind: prior_review
  reference: reports/yaml_record_review/Na-ampicillin.md
  locator: '`data/ingredients/mapped/Na-ampicillin.yaml`:2; Verdict:4; Identity:10;
    Validation:19; Evidence:27; Completeness:41; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5d99140353468f93aa9a3fb8e3147aa3ebbf411e48a0db40012b506cd3d443ac
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-ampicillin.yaml`,\
    \ replace the\n  provisional `SELECTIVE_AGENT` inference with source-backed role\
    \ evidence or\n  remove the role. Re-run strict validation and final SSSOM validation\
    \ after\n  the repair."
- evidence_id: ev-a1ede6e44e80a8a8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[968,2007]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2","finding_id":"SEM:9375061634834d76114b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2","finding_id":"SEM:6586f0fa5465c2ab1ea6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d767672b401a68c0
  kind: record_content
  reference: data/ingredients/mapped/Na-ampicillin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1458],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34535","line":1460,"mapping_status":"MAPPED","ontology_id":"CHEBI:34535","preferred_term":"Na-ampicillin"}],"identifier":"CHEBI:34535","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34535","ontology_label":"ampicillin
    sodium","ontology_source":"CHEBI"},"preferred_term":"Na-ampicillin","sssom_rows":[{"data_row":1963,"object_id":"CHEBI:34535","object_label":"ampicillin
    sodium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-ampicillin","synonym_count":10}'
  snapshot_sha256: def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2
- evidence_id: ev-7545499aecafa9da
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-51bcfdceec1a7afb]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-51bcfdceec1a7afb in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-5b7e193a71a4471b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-7c2dd2f3119f9335
  - ev-2ff365ec412bd34d
  - ev-545b3f29881a9dc3
  - ev-92e3b46108e806c5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fa8892493419ae75
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-ca60272c84e70ca6
  - ev-7c2dd2f3119f9335
  - ev-a1ede6e44e80a8a8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:44:27Z;
    reviewed SHA-256=def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2;
    current SHA-256=def2647ee221c1256dbdd1cc95b2cfc5f05fb13f4fdd4250d471dfe94edc4ec2;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-ampicillin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:34535
    ampicillin sodium identity, CAS provenance, synonyms, duplicate merge, and final
    exact row pass, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ca60272c84e70ca6
    - ev-7c2dd2f3119f9335
  - name: legacy-native-ids
    value: '["SEM:9375061634834d76114b","SEM:6586f0fa5465c2ab1ea6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7c2dd2f3119f9335
    - ev-ca60272c84e70ca6
    - ev-a1ede6e44e80a8a8
- assessment_id: a-d767672b401a68c0
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-ca60272c84e70ca6
  - ev-d767672b401a68c0
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ca60272c84e70ca6
    - ev-d767672b401a68c0
findings:
- finding_id: rec-f-51bcfdceec1a7afb
  issue_key: mim-reconciliation-role-support-09fcfa2b32327521
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-ampicillin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-09fcfa2b32327521
  evidence_ids:
  - ev-ca60272c84e70ca6
  - ev-d767672b401a68c0
  - ev-7545499aecafa9da
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-ampicillin.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-51bcfdceec1a7afb
actions:
- action_id: rec-action-51bcfdceec1a7afb
  description: 'Reassess prediction-only role support: Na-ampicillin'
  finding_ids:
  - rec-f-51bcfdceec1a7afb
  target_ids:
  - record-09fcfa2b32327521
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-ampicillin.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
