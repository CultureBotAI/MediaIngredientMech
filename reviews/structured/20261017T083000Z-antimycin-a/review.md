# Per-record structured review: Antimycin_A (data/ingredients/mapped/Antimycin_A.yaml)

- Review: 20261017T083000Z-antimycin-a
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Antimycin_A (data/ingredients/mapped/Antimycin_A.yaml, record-e95259f65a0bb6d9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Antimycin_A.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Antimycin_A.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e95259f65a0bb6d9 | data/ingredients/mapped/Antimycin_A.yaml | maintained | Antimycin_A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e95259f65a0bb6d9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e95259f65a0bb6d9 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e95259f65a0bb6d9 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e95259f65a0bb6d9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e95259f65a0bb6d9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:24:40Z; reviewed SHA-256=53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0; current SHA-256=53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0; hash_changed=False. Reports=["reports/yaml_record_review/Antimycin_A.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, formula, exact synonym, SSSOM row, and aggregate copy pass, but the selective-agent role is only a provisional name-pattern inference.

### Historical provisional-role concern

evidence: concern. Targets: record-e95259f65a0bb6d9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-243e667bf81faeb8: Reassess prediction-only role support: Antimycin A

major / open / confirmed; issue key: mim-reconciliation-role-support-e95259f65a0bb6d9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-243e667bf81faeb8

Reassess prediction-only role support: Antimycin A

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3ea54081b1a4504e | data/ingredients/mapped/Antimycin_A.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[501],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2762","line":503,"mapping_status":"MAPPED","ontology_id":"CHEBI:2762","preferred_term":"Antimycin A"}],"identifier":"CHEBI:2762","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2762","ontology_label":"antimycin A","ontology_source":"CHEBI"},"preferred_term":"Antimycin A","sssom_rows":[{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Antimycin_A","synonym_count":1} |
| ev-c5fd2dc8afb8a0c8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [501] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f2f5b7c92f08abbd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Antimycin_A; data-row positions=[394] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin A","other":"(2R,3S,6S,7R,8R)-3-[(3-formamido-2-hydroxybenzoyl)amino]-8-hexyl-2,6-dimethyl-4,9-dioxo-1,5-dioxonan-7-yl 3-methylbutanoate&#124;CAS:1397-94-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Antimycin_A","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-97a49ea20a206ef8 | docs/data/mapped_ingredients.csv; CSV lines=[503] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:2762","line":503,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2762","preferred_term":"Antimycin A","total_occurrences":"0"}] |
| ev-c09b93873498b767 | reports/yaml_record_review/Antimycin_A.md; &#96;data/ingredients/mapped/Antimycin_A.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:40; Completeness:60; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-625298acdd2a6c38 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[266,1988] | context_only | [{"current_record_sha256":"53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0","finding_id":"SEM:5454f9cd0e1889155a93","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0","finding_id":"SEM:bddf69732999c7870e1c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-bf18ff9f3ccd8588 | data/ingredients/mapped/Antimycin_A.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[501],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2762","line":503,"mapping_status":"MAPPED","ontology_id":"CHEBI:2762","preferred_term":"Antimycin A"}],"identifier":"CHEBI:2762","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2762","ontology_label":"antimycin A","ontology_source":"CHEBI"},"preferred_term":"Antimycin A","sssom_rows":[{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Antimycin_A","synonym_count":1} |
| ev-64927cd242906f83 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-243e667bf81faeb8] | context_only | Predecessor structured review finding f-243e667bf81faeb8 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-antimycin-a
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Antimycin_A (data/ingredients/mapped/Antimycin_A.yaml)'
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
summary: Per-record structured review for Antimycin_A (data/ingredients/mapped/Antimycin_A.yaml,
  record-e95259f65a0bb6d9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Antimycin_A.yaml
    sha256: 53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0
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
  - path: reports/yaml_record_review/Antimycin_A.md
    sha256: 44e39a7db2348e3c19d4f50109d69b3ae1da61062bd99112f59237e34ee3e767
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e95259f65a0bb6d9
  path: data/ingredients/mapped/Antimycin_A.yaml
  label: Antimycin_A
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Antimycin_A.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Antimycin_A.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Antimycin_A.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e95259f65a0bb6d9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-3ea54081b1a4504e
  - ev-c5fd2dc8afb8a0c8
  - ev-f2f5b7c92f08abbd
  - ev-97a49ea20a206ef8
  - ev-bf18ff9f3ccd8588
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-3ea54081b1a4504e
  - ev-625298acdd2a6c38
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-c09b93873498b767
  - ev-625298acdd2a6c38
  - ev-64927cd242906f83
evidence:
- evidence_id: ev-3ea54081b1a4504e
  kind: record_content
  reference: data/ingredients/mapped/Antimycin_A.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[501],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2762","line":503,"mapping_status":"MAPPED","ontology_id":"CHEBI:2762","preferred_term":"Antimycin
    A"}],"identifier":"CHEBI:2762","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2762","ontology_label":"antimycin
    A","ontology_source":"CHEBI"},"preferred_term":"Antimycin A","sssom_rows":[{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Antimycin_A","synonym_count":1}'
  snapshot_sha256: 53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0
- evidence_id: ev-c5fd2dc8afb8a0c8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [501]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f2f5b7c92f08abbd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Antimycin_A; data-row positions=[394]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin
    A","other":"(2R,3S,6S,7R,8R)-3-[(3-formamido-2-hydroxybenzoyl)amino]-8-hexyl-2,6-dimethyl-4,9-dioxo-1,5-dioxonan-7-yl
    3-methylbutanoate|CAS:1397-94-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Antimycin_A","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-97a49ea20a206ef8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[503]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:2762","line":503,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2762","preferred_term":"Antimycin
    A","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c09b93873498b767
  kind: prior_review
  reference: reports/yaml_record_review/Antimycin_A.md
  locator: '`data/ingredients/mapped/Antimycin_A.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:40; Completeness:60; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 44e39a7db2348e3c19d4f50109d69b3ae1da61062bd99112f59237e34ee3e767
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Antimycin_A.yaml`, remove\n\
    \  `physicochemical_roles.SELECTIVE_AGENT` unless direct source evidence for\n\
    \  Antimycin A as a selective agent is attached to that role.\n- Regenerate synchronized\
    \ products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimycin_A.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-625298acdd2a6c38
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[266,1988]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0","finding_id":"SEM:5454f9cd0e1889155a93","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0","finding_id":"SEM:bddf69732999c7870e1c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-bf18ff9f3ccd8588
  kind: record_content
  reference: data/ingredients/mapped/Antimycin_A.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[501],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2762","line":503,"mapping_status":"MAPPED","ontology_id":"CHEBI:2762","preferred_term":"Antimycin
    A"}],"identifier":"CHEBI:2762","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2762","ontology_label":"antimycin
    A","ontology_source":"CHEBI"},"preferred_term":"Antimycin A","sssom_rows":[{"data_row":394,"object_id":"CHEBI:2762","object_label":"antimycin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Antimycin_A","synonym_count":1}'
  snapshot_sha256: 53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0
- evidence_id: ev-64927cd242906f83
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-243e667bf81faeb8]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-243e667bf81faeb8 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-5644ab4570369d06
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-3ea54081b1a4504e
  - ev-c5fd2dc8afb8a0c8
  - ev-f2f5b7c92f08abbd
  - ev-97a49ea20a206ef8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-accf47ed10a86a45
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-c09b93873498b767
  - ev-3ea54081b1a4504e
  - ev-625298acdd2a6c38
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:24:40Z;
    reviewed SHA-256=53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0;
    current SHA-256=53b2ae1d271c05dc3c0cbcf7612d367df95a906463fee7eb5dbb91fa5251e1a0;
    hash_changed=False. Reports=["reports/yaml_record_review/Antimycin_A.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, formula, exact synonym, SSSOM row, and aggregate copy pass, but
    the selective-agent role is only a provisional name-pattern inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c09b93873498b767
    - ev-3ea54081b1a4504e
  - name: legacy-native-ids
    value: '["SEM:5454f9cd0e1889155a93","SEM:bddf69732999c7870e1c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3ea54081b1a4504e
    - ev-c09b93873498b767
    - ev-625298acdd2a6c38
- assessment_id: a-bf18ff9f3ccd8588
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-c09b93873498b767
  - ev-bf18ff9f3ccd8588
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c09b93873498b767
    - ev-bf18ff9f3ccd8588
findings:
- finding_id: rec-f-243e667bf81faeb8
  issue_key: mim-reconciliation-role-support-e95259f65a0bb6d9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Antimycin A'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e95259f65a0bb6d9
  evidence_ids:
  - ev-c09b93873498b767
  - ev-bf18ff9f3ccd8588
  - ev-64927cd242906f83
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Antimycin_A.yaml
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
    finding_id: f-243e667bf81faeb8
actions:
- action_id: rec-action-243e667bf81faeb8
  description: 'Reassess prediction-only role support: Antimycin A'
  finding_ids:
  - rec-f-243e667bf81faeb8
  target_ids:
  - record-e95259f65a0bb6d9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Antimycin_A.yaml
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
