# Per-record structured review: Alpha-ketoglutaric_Acid (data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml)

- Review: 20261017T083000Z-alpha-ketoglutaric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alpha-ketoglutaric_Acid (data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml, record-091bb42f89d9e39a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-091bb42f89d9e39a | data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml | maintained | Alpha-ketoglutaric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-091bb42f89d9e39a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-091bb42f89d9e39a | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-091bb42f89d9e39a | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-091bb42f89d9e39a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-091bb42f89d9e39a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z; reviewed SHA-256=cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d; current SHA-256=cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d; hash_changed=False. Reports=["reports/yaml_record_review/Alpha-ketoglutaric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but the carbon and energy source roles are still provisional computational predictions.

### Historical provisional-role concern

evidence: concern. Targets: record-091bb42f89d9e39a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1fe668de9a8d82fb: Reassess prediction-only role support: alpha-ketoglutaric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-091bb42f89d9e39a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1fe668de9a8d82fb

Reassess prediction-only role support: alpha-ketoglutaric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-98f898c9d099ce67 | data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[477],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30915","line":479,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"alpha-ketoglutaric acid"}],"identifier":"CHEBI:30915","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric acid","ontology_source":"CHEBI"},"preferred_term":"alpha-ketoglutaric acid","sssom_rows":[{"data_row":340,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alpha-ketoglutaric_Acid","synonym_count":7} |
| ev-39db102cefe73fa4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [477] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-401d7986dd4fff04 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alpha-ketoglutaric_Acid; data-row positions=[340] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":340,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric acid","other":"2-Ketoglutaric acid&#124;2-oxopentanedioic acid&#124;Oxoglutaric acid&#124;a-Ketoglutaric acid&#124;alpha-ketoglutamate&#124;alpha-ketoglutaric acid (100 mM).&#124;CAS:328-50-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Alpha-ketoglutaric_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-59ee7bbda564c951 | docs/data/mapped_ingredients.csv; CSV lines=[479] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30915","line":479,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:30915","preferred_term":"alpha-ketoglutaric acid","total_occurrences":"7"}] |
| ev-6c3eda9c9ae49e87 | reports/yaml_record_review/Alpha-ketoglutaric_Acid.md; &#96;data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:43; Completeness:65; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e0b3af6a208da1bf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[243,1510,1757] | context_only | [{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:80f9ca33e0c5c4d98474","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:d182ed57a817e7f0cd6d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:c1bf7bfcebc65b53333e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b4bad696f1674ae3 | data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-8556252f24fb53a0 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-1fe668de9a8d82fb] | context_only | Predecessor structured review finding f-1fe668de9a8d82fb in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alpha-ketoglutaric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alpha-ketoglutaric_Acid (data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml)'
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
summary: Per-record structured review for Alpha-ketoglutaric_Acid (data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml,
  record-091bb42f89d9e39a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
    sha256: cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d
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
  - path: reports/yaml_record_review/Alpha-ketoglutaric_Acid.md
    sha256: cff4d6b3496c1f8eab2ace8c8fb264708913fb31cad0f3327d10646439bd1c29
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-091bb42f89d9e39a
  path: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
  label: Alpha-ketoglutaric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-091bb42f89d9e39a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-091bb42f89d9e39a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-091bb42f89d9e39a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-091bb42f89d9e39a
evidence:
- evidence_id: ev-98f898c9d099ce67
  kind: record_content
  reference: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[477],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30915","line":479,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"alpha-ketoglutaric
    acid"}],"identifier":"CHEBI:30915","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric
    acid","ontology_source":"CHEBI"},"preferred_term":"alpha-ketoglutaric acid","sssom_rows":[{"data_row":340,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alpha-ketoglutaric_Acid","synonym_count":7}'
  snapshot_sha256: cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d
- evidence_id: ev-39db102cefe73fa4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [477]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-401d7986dd4fff04
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alpha-ketoglutaric_Acid; data-row positions=[340]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":340,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric
    acid","other":"2-Ketoglutaric acid|2-oxopentanedioic acid|Oxoglutaric acid|a-Ketoglutaric
    acid|alpha-ketoglutamate|alpha-ketoglutaric acid (100 mM).|CAS:328-50-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Alpha-ketoglutaric_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-59ee7bbda564c951
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[479]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30915","line":479,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:30915","preferred_term":"alpha-ketoglutaric
    acid","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6c3eda9c9ae49e87
  kind: prior_review
  reference: reports/yaml_record_review/Alpha-ketoglutaric_Acid.md
  locator: '`data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:43; Completeness:65; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cff4d6b3496c1f8eab2ace8c8fb264708913fb31cad0f3327d10646439bd1c29
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml`,\
    \ either replace the\n  `CARBON_SOURCE` and `ENERGY_SOURCE` computational predictions\
    \ with\n  source-specific evidence, or remove the unsupported role facets.\n-\
    \ Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\
    \ `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-e0b3af6a208da1bf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[243,1510,1757]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:80f9ca33e0c5c4d98474","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:d182ed57a817e7f0cd6d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d","finding_id":"SEM:c1bf7bfcebc65b53333e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b4bad696f1674ae3
  kind: record_content
  reference: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d
- evidence_id: ev-8556252f24fb53a0
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-1fe668de9a8d82fb]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1fe668de9a8d82fb in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-213634dd3b5b7daa
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-091bb42f89d9e39a
  evidence_ids:
  - ev-98f898c9d099ce67
  - ev-39db102cefe73fa4
  - ev-401d7986dd4fff04
  - ev-59ee7bbda564c951
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9bd53c5c4ec7c1f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-091bb42f89d9e39a
  evidence_ids:
  - ev-6c3eda9c9ae49e87
  - ev-98f898c9d099ce67
  - ev-e0b3af6a208da1bf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z;
    reviewed SHA-256=cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d;
    current SHA-256=cc852c586e35a3ffa025ce9446da05dc235a6df8a7c0e7c2fa4c4d6ee18d371d;
    hash_changed=False. Reports=["reports/yaml_record_review/Alpha-ketoglutaric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass,
    but the carbon and energy source roles are still provisional computational predictions.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c3eda9c9ae49e87
    - ev-98f898c9d099ce67
  - name: legacy-native-ids
    value: '["SEM:80f9ca33e0c5c4d98474","SEM:d182ed57a817e7f0cd6d","SEM:c1bf7bfcebc65b53333e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-98f898c9d099ce67
    - ev-6c3eda9c9ae49e87
    - ev-e0b3af6a208da1bf
- assessment_id: a-b4bad696f1674ae3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-091bb42f89d9e39a
  evidence_ids:
  - ev-6c3eda9c9ae49e87
  - ev-b4bad696f1674ae3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c3eda9c9ae49e87
    - ev-b4bad696f1674ae3
findings:
- finding_id: rec-f-1fe668de9a8d82fb
  issue_key: mim-reconciliation-role-support-091bb42f89d9e39a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: alpha-ketoglutaric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-091bb42f89d9e39a
  evidence_ids:
  - ev-6c3eda9c9ae49e87
  - ev-b4bad696f1674ae3
  - ev-8556252f24fb53a0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-1fe668de9a8d82fb
actions:
- action_id: rec-action-1fe668de9a8d82fb
  description: 'Reassess prediction-only role support: alpha-ketoglutaric acid'
  finding_ids:
  - rec-f-1fe668de9a8d82fb
  target_ids:
  - record-091bb42f89d9e39a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml
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
