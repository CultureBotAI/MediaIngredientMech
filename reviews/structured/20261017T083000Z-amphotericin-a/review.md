# Per-record structured review: Amphotericin_A (data/ingredients/mapped/Amphotericin_A.yaml)

- Review: 20261017T083000Z-amphotericin-a
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Amphotericin_A (data/ingredients/mapped/Amphotericin_A.yaml, record-2796a59d4ac29870, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Amphotericin_A.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Amphotericin_A.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2796a59d4ac29870 | data/ingredients/mapped/Amphotericin_A.yaml | maintained | Amphotericin_A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2796a59d4ac29870 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2796a59d4ac29870 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2796a59d4ac29870 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2796a59d4ac29870.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2796a59d4ac29870.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z; reviewed SHA-256=5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3; current SHA-256=5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3; hash_changed=False. Reports=["reports/yaml_record_review/Amphotericin_A.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH identity, SSSOM row, and row-review disposition pass, but the selective-agent role is only a computational name-pattern inference.

### Historical provisional-role concern

evidence: concern. Targets: record-2796a59d4ac29870.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4736f4094c6571e7: Reassess prediction-only role support: Amphotericin A

major / open / confirmed; issue key: mim-reconciliation-role-support-2796a59d4ac29870.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4736f4094c6571e7

Reassess prediction-only role support: Amphotericin A

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-88b41c24bc71c296 | data/ingredients/mapped/Amphotericin_A.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[487],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041989","line":489,"mapping_status":"MAPPED","ontology_id":"mesh:C041989","preferred_term":"Amphotericin A"}],"identifier":"mesh:C041989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041989","ontology_label":"amphotericin A","ontology_source":"MESH"},"preferred_term":"Amphotericin A","sssom_rows":[{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_A","synonym_count":0} |
| ev-4effd16c4d0bd765 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [487] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1817c35af5d2697f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Amphotericin_A; data-row positions=[371] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Amphotericin_A","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-efe54dc9b1853b87 | docs/data/mapped_ingredients.csv; CSV lines=[489] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C041989","line":489,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C041989","preferred_term":"Amphotericin A","total_occurrences":"0"}] |
| ev-0500ef4ef65b36d1 | reports/yaml_record_review/Amphotericin_A.md; &#96;data/ingredients/mapped/Amphotericin_A.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:34; Completeness:51; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b6ab4859e9072ba5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[253,1665] | context_only | [{"current_record_sha256":"5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3","finding_id":"SEM:fa494a9e272b394a4be3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3","finding_id":"SEM:6ce738645d7f5c982a89","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c230f80c0d5a48e6 | data/ingredients/mapped/Amphotericin_A.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[487],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041989","line":489,"mapping_status":"MAPPED","ontology_id":"mesh:C041989","preferred_term":"Amphotericin A"}],"identifier":"mesh:C041989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041989","ontology_label":"amphotericin A","ontology_source":"MESH"},"preferred_term":"Amphotericin A","sssom_rows":[{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_A","synonym_count":0} |
| ev-659ba91349792e8b | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-4736f4094c6571e7] | context_only | Predecessor structured review finding f-4736f4094c6571e7 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-amphotericin-a
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Amphotericin_A (data/ingredients/mapped/Amphotericin_A.yaml)'
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
summary: Per-record structured review for Amphotericin_A (data/ingredients/mapped/Amphotericin_A.yaml,
  record-2796a59d4ac29870, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Amphotericin_A.yaml
    sha256: 5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3
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
  - path: reports/yaml_record_review/Amphotericin_A.md
    sha256: 4998eaf3f3212c7948cfe0a1ad665d8ac2560b0e6d144a70203aee03cdcf82aa
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2796a59d4ac29870
  path: data/ingredients/mapped/Amphotericin_A.yaml
  label: Amphotericin_A
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_A.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Amphotericin_A.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Amphotericin_A.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2796a59d4ac29870
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-88b41c24bc71c296
  - ev-4effd16c4d0bd765
  - ev-1817c35af5d2697f
  - ev-efe54dc9b1853b87
  - ev-c230f80c0d5a48e6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-88b41c24bc71c296
  - ev-b6ab4859e9072ba5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-0500ef4ef65b36d1
  - ev-b6ab4859e9072ba5
  - ev-659ba91349792e8b
evidence:
- evidence_id: ev-88b41c24bc71c296
  kind: record_content
  reference: data/ingredients/mapped/Amphotericin_A.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[487],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041989","line":489,"mapping_status":"MAPPED","ontology_id":"mesh:C041989","preferred_term":"Amphotericin
    A"}],"identifier":"mesh:C041989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041989","ontology_label":"amphotericin
    A","ontology_source":"MESH"},"preferred_term":"Amphotericin A","sssom_rows":[{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_A","synonym_count":0}'
  snapshot_sha256: 5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3
- evidence_id: ev-4effd16c4d0bd765
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [487]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1817c35af5d2697f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Amphotericin_A; data-row positions=[371]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin
    A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Amphotericin_A","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-efe54dc9b1853b87
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[489]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C041989","line":489,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C041989","preferred_term":"Amphotericin
    A","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0500ef4ef65b36d1
  kind: prior_review
  reference: reports/yaml_record_review/Amphotericin_A.md
  locator: '`data/ingredients/mapped/Amphotericin_A.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:34; Completeness:51; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4998eaf3f3212c7948cfe0a1ad665d8ac2560b0e6d144a70203aee03cdcf82aa
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Amphotericin_A.yaml`,\
    \ replace the\n  `SELECTIVE_AGENT` computational prediction with source-backed\
    \ evidence, or\n  remove it.\n- Regenerate synchronized products, then rerun\n\
    \  `uv run --frozen python scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Amphotericin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-b6ab4859e9072ba5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[253,1665]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3","finding_id":"SEM:fa494a9e272b394a4be3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3","finding_id":"SEM:6ce738645d7f5c982a89","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c230f80c0d5a48e6
  kind: record_content
  reference: data/ingredients/mapped/Amphotericin_A.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[487],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041989","line":489,"mapping_status":"MAPPED","ontology_id":"mesh:C041989","preferred_term":"Amphotericin
    A"}],"identifier":"mesh:C041989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041989","ontology_label":"amphotericin
    A","ontology_source":"MESH"},"preferred_term":"Amphotericin A","sssom_rows":[{"data_row":371,"object_id":"mesh:C041989","object_label":"amphotericin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_A","synonym_count":0}'
  snapshot_sha256: 5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3
- evidence_id: ev-659ba91349792e8b
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-4736f4094c6571e7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4736f4094c6571e7 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-3d7d376e37836101
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-88b41c24bc71c296
  - ev-4effd16c4d0bd765
  - ev-1817c35af5d2697f
  - ev-efe54dc9b1853b87
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a4eb942c44dff5f5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-0500ef4ef65b36d1
  - ev-88b41c24bc71c296
  - ev-b6ab4859e9072ba5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z;
    reviewed SHA-256=5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3;
    current SHA-256=5fd05b51b1510c00941559c7632b178dd057ccce0d35b5dd8aad2c8ca3e297e3;
    hash_changed=False. Reports=["reports/yaml_record_review/Amphotericin_A.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MeSH identity, SSSOM row, and row-review disposition pass, but the selective-agent
    role is only a computational name-pattern inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0500ef4ef65b36d1
    - ev-88b41c24bc71c296
  - name: legacy-native-ids
    value: '["SEM:fa494a9e272b394a4be3","SEM:6ce738645d7f5c982a89"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-88b41c24bc71c296
    - ev-0500ef4ef65b36d1
    - ev-b6ab4859e9072ba5
- assessment_id: a-c230f80c0d5a48e6
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-0500ef4ef65b36d1
  - ev-c230f80c0d5a48e6
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0500ef4ef65b36d1
    - ev-c230f80c0d5a48e6
findings:
- finding_id: rec-f-4736f4094c6571e7
  issue_key: mim-reconciliation-role-support-2796a59d4ac29870
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Amphotericin A'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2796a59d4ac29870
  evidence_ids:
  - ev-0500ef4ef65b36d1
  - ev-c230f80c0d5a48e6
  - ev-659ba91349792e8b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_A.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-4736f4094c6571e7
actions:
- action_id: rec-action-4736f4094c6571e7
  description: 'Reassess prediction-only role support: Amphotericin A'
  finding_ids:
  - rec-f-4736f4094c6571e7
  target_ids:
  - record-2796a59d4ac29870
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_A.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
