# Per-record structured review: D-tryptophan (data/ingredients/mapped/D-tryptophan.yaml)

- Review: 20261017T083000Z-d-tryptophan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-tryptophan (data/ingredients/mapped/D-tryptophan.yaml, record-a29ed39e5e26bc6c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-tryptophan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-tryptophan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a29ed39e5e26bc6c | data/ingredients/mapped/D-tryptophan.yaml | maintained | D-tryptophan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a29ed39e5e26bc6c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a29ed39e5e26bc6c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a29ed39e5e26bc6c | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a29ed39e5e26bc6c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a29ed39e5e26bc6c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:53:27Z; reviewed SHA-256=96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54; current SHA-256=96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54; hash_changed=False. Reports=["reports/yaml_record_review/D-tryptophan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI/CAS identity and final SSSOM CAS payload pass, but the amino-acid-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-a29ed39e5e26bc6c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9fb8807431f40221: Reassess prediction-only role support: D-tryptophan

major / open / confirmed; issue key: mim-reconciliation-role-support-a29ed39e5e26bc6c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9fb8807431f40221

Reassess prediction-only role support: D-tryptophan

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-03465f0f6440fd77 | data/ingredients/mapped/D-tryptophan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[842],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16296","line":844,"mapping_status":"MAPPED","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan"}],"identifier":"CHEBI:16296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16296","ontology_label":"D-tryptophan","ontology_source":"CHEBI"},"preferred_term":"D-tryptophan","sssom_rows":[{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-tryptophan","synonym_count":0} |
| ev-07cd01f8f7ec88c1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [842] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-92581a97599a2cab | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-tryptophan; data-row positions=[957] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","other":"CAS:153-94-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-tryptophan","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e83ba2ca0c4bf752 | docs/data/mapped_ingredients.csv; CSV lines=[844] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16296","line":844,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan","total_occurrences":"0"}] |
| ev-b19830f1dacb0cd6 | reports/yaml_record_review/D-tryptophan.md; &#96;data/ingredients/mapped/D-tryptophan.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:36; Completeness:50; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b342f276e419e5db | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[508,1540] | context_only | [{"current_record_sha256":"96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54","finding_id":"SEM:bbec3bc94023a7f7af8c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54","finding_id":"SEM:3eec2edaab4c701cfb4d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-278afae12143167c | data/ingredients/mapped/D-tryptophan.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[842],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16296","line":844,"mapping_status":"MAPPED","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan"}],"identifier":"CHEBI:16296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16296","ontology_label":"D-tryptophan","ontology_source":"CHEBI"},"preferred_term":"D-tryptophan","sssom_rows":[{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-tryptophan","synonym_count":0} |
| ev-e6e90b4a7fd4968d | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-9fb8807431f40221] | context_only | Predecessor structured review finding f-9fb8807431f40221 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-tryptophan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-tryptophan (data/ingredients/mapped/D-tryptophan.yaml)'
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
summary: Per-record structured review for D-tryptophan (data/ingredients/mapped/D-tryptophan.yaml,
  record-a29ed39e5e26bc6c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-tryptophan.yaml
    sha256: 96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-tryptophan.md
    sha256: 8e1b78647e599e1ec351b1e5e2f77c438b8d8983f641cc07df4bae8b82083150
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a29ed39e5e26bc6c
  path: data/ingredients/mapped/D-tryptophan.yaml
  label: D-tryptophan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-tryptophan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-tryptophan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-tryptophan.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a29ed39e5e26bc6c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-03465f0f6440fd77
  - ev-07cd01f8f7ec88c1
  - ev-92581a97599a2cab
  - ev-e83ba2ca0c4bf752
  - ev-278afae12143167c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-03465f0f6440fd77
  - ev-b342f276e419e5db
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-b19830f1dacb0cd6
  - ev-b342f276e419e5db
  - ev-e6e90b4a7fd4968d
evidence:
- evidence_id: ev-03465f0f6440fd77
  kind: record_content
  reference: data/ingredients/mapped/D-tryptophan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[842],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16296","line":844,"mapping_status":"MAPPED","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan"}],"identifier":"CHEBI:16296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16296","ontology_label":"D-tryptophan","ontology_source":"CHEBI"},"preferred_term":"D-tryptophan","sssom_rows":[{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-tryptophan","synonym_count":0}'
  snapshot_sha256: 96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54
- evidence_id: ev-07cd01f8f7ec88c1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [842]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-92581a97599a2cab
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-tryptophan; data-row positions=[957]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","other":"CAS:153-94-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-tryptophan","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e83ba2ca0c4bf752
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[844]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16296","line":844,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b19830f1dacb0cd6
  kind: prior_review
  reference: reports/yaml_record_review/D-tryptophan.md
  locator: '`data/ingredients/mapped/D-tryptophan.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:36; Completeness:50; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8e1b78647e599e1ec351b1e5e2f77c438b8d8983f641cc07df4bae8b82083150
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-tryptophan.yaml`, remove\
    \ the provisional\n  `AMINO_ACID_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION`\
    \ evidence\n  with inspected claim-level evidence.\n- Regenerate synchronized\
    \ curated and SSSOM products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-tryptophan.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-b342f276e419e5db
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[508,1540]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54","finding_id":"SEM:bbec3bc94023a7f7af8c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54","finding_id":"SEM:3eec2edaab4c701cfb4d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-278afae12143167c
  kind: record_content
  reference: data/ingredients/mapped/D-tryptophan.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[842],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16296","line":844,"mapping_status":"MAPPED","ontology_id":"CHEBI:16296","preferred_term":"D-tryptophan"}],"identifier":"CHEBI:16296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16296","ontology_label":"D-tryptophan","ontology_source":"CHEBI"},"preferred_term":"D-tryptophan","sssom_rows":[{"data_row":957,"object_id":"CHEBI:16296","object_label":"D-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-tryptophan","synonym_count":0}'
  snapshot_sha256: 96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54
- evidence_id: ev-e6e90b4a7fd4968d
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-9fb8807431f40221]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9fb8807431f40221 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-620dbbdeb7f6a02c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-03465f0f6440fd77
  - ev-07cd01f8f7ec88c1
  - ev-92581a97599a2cab
  - ev-e83ba2ca0c4bf752
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a84f9700de3d802c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-b19830f1dacb0cd6
  - ev-03465f0f6440fd77
  - ev-b342f276e419e5db
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:53:27Z;
    reviewed SHA-256=96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54;
    current SHA-256=96a0312bee253b2d7e871bcc110c086f329044017860606ff3c1d0e3dec09b54;
    hash_changed=False. Reports=["reports/yaml_record_review/D-tryptophan.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI/CAS
    identity and final SSSOM CAS payload pass, but the amino-acid-source role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b19830f1dacb0cd6
    - ev-03465f0f6440fd77
  - name: legacy-native-ids
    value: '["SEM:bbec3bc94023a7f7af8c","SEM:3eec2edaab4c701cfb4d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-03465f0f6440fd77
    - ev-b19830f1dacb0cd6
    - ev-b342f276e419e5db
- assessment_id: a-278afae12143167c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-b19830f1dacb0cd6
  - ev-278afae12143167c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b19830f1dacb0cd6
    - ev-278afae12143167c
findings:
- finding_id: rec-f-9fb8807431f40221
  issue_key: mim-reconciliation-role-support-a29ed39e5e26bc6c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-tryptophan'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a29ed39e5e26bc6c
  evidence_ids:
  - ev-b19830f1dacb0cd6
  - ev-278afae12143167c
  - ev-e6e90b4a7fd4968d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-tryptophan.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-9fb8807431f40221
actions:
- action_id: rec-action-9fb8807431f40221
  description: 'Reassess prediction-only role support: D-tryptophan'
  finding_ids:
  - rec-f-9fb8807431f40221
  target_ids:
  - record-a29ed39e5e26bc6c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-tryptophan.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
