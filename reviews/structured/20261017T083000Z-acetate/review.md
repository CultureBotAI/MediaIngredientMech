# Per-record structured review: Acetate (data/ingredients/mapped/Acetate.yaml)

- Review: 20261017T083000Z-acetate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Acetate (data/ingredients/mapped/Acetate.yaml, record-edc7652497b859e8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Acetate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Acetate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-edc7652497b859e8 | data/ingredients/mapped/Acetate.yaml | maintained | Acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-edc7652497b859e8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-edc7652497b859e8 | Role assertions on nutritional_roles[1], nutritional_roles[2] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-edc7652497b859e8 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-edc7652497b859e8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-edc7652497b859e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:12Z; reviewed SHA-256=f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4; current SHA-256=f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050112Z-Acetate.md","reports/yaml_record_review/Acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Acetate.md&#96; after the record changed from 903a76864cf76781d05225e3520f3167a1815508bf9fdf8538cf10daf8c78fce to f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-edc7652497b859e8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-053648a807e87728: Reassess prediction-only role support: Acetate

major / open / confirmed; issue key: mim-reconciliation-role-support-edc7652497b859e8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-053648a807e87728

Reassess prediction-only role support: Acetate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ee665e7aebded001 | data/ingredients/mapped/Acetate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[438],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30089","line":440,"mapping_status":"MAPPED","ontology_id":"CHEBI:30089","preferred_term":"Acetate"}],"identifier":"CHEBI:30089","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":48,"total_occurrences":48},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30089","ontology_label":"acetate","ontology_source":"CHEBI"},"preferred_term":"Acetate","sssom_rows":[{"data_row":279,"object_id":"CHEBI:30089","object_label":"acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetate","synonym_count":11} |
| ev-cda360c7f1061ed0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [438] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cea5588a6e37d54d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Acetate; data-row positions=[279] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":279,"object_id":"CHEBI:30089","object_label":"acetate","other":"ACETATE ION&#124;Azetat&#124;Ethanoat&#124;MeCO2 anion&#124;ethanoate&#124;Acetate (carbon source)&#124;CAS:71-50-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Acetate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-5e1821a8c0a9afcb | docs/data/mapped_ingredients.csv; CSV lines=[440] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30089","line":440,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"48","ontology_id":"CHEBI:30089","preferred_term":"Acetate","total_occurrences":"48"}] |
| ev-d8f3a7445b40ac39 | reports/yaml_record_review/20261001T050112Z-Acetate.md; YAML Record Review: Acetate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-31547d9fc9c1c8ca | reports/yaml_record_review/Acetate.md; &#96;data/ingredients/mapped/Acetate.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:45; Completeness:66; Recommended Edits:75 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6297834553ff64ad | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[195,1718,2056] | context_only | [{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:d2f900514771b491f061","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:6d32ba1f8c319600e599","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:f52e2cdff802bc3024c0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ad02f968da174887 | data/ingredients/mapped/Acetate.yaml; nutritional_roles[1], nutritional_roles[2] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}},{"field":"nutritional_roles[2]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-790918cc4cbc3c56 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-053648a807e87728] | context_only | Predecessor structured review finding f-053648a807e87728 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-acetate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Acetate (data/ingredients/mapped/Acetate.yaml)'
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
summary: Per-record structured review for Acetate (data/ingredients/mapped/Acetate.yaml,
  record-edc7652497b859e8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Acetate.yaml
    sha256: f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/20261001T050112Z-Acetate.md
    sha256: c0403cbac72f71aacbf7c677d40f579d3e087718dc2057e7c3dd2d693438999b
    role: context
  - path: reports/yaml_record_review/Acetate.md
    sha256: 3dc23437ef79bfbd7df92c6cdafe7acc5c28e596ed5e9d7a0ddd2b61cf7ba48d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-edc7652497b859e8
  path: data/ingredients/mapped/Acetate.yaml
  label: Acetate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Acetate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Acetate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-edc7652497b859e8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-edc7652497b859e8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1], nutritional_roles[2] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-edc7652497b859e8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-edc7652497b859e8
evidence:
- evidence_id: ev-ee665e7aebded001
  kind: record_content
  reference: data/ingredients/mapped/Acetate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[438],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30089","line":440,"mapping_status":"MAPPED","ontology_id":"CHEBI:30089","preferred_term":"Acetate"}],"identifier":"CHEBI:30089","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":48,"edge_count":48,"occurrences":48},"occurrence_statistics":{"media_count":48,"total_occurrences":48},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30089","ontology_label":"acetate","ontology_source":"CHEBI"},"preferred_term":"Acetate","sssom_rows":[{"data_row":279,"object_id":"CHEBI:30089","object_label":"acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Acetate","synonym_count":11}'
  snapshot_sha256: f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4
- evidence_id: ev-cda360c7f1061ed0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [438]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cea5588a6e37d54d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Acetate; data-row positions=[279]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":279,"object_id":"CHEBI:30089","object_label":"acetate","other":"ACETATE
    ION|Azetat|Ethanoat|MeCO2 anion|ethanoate|Acetate (carbon source)|CAS:71-50-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Acetate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5e1821a8c0a9afcb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[440]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30089","line":440,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"48","ontology_id":"CHEBI:30089","preferred_term":"Acetate","total_occurrences":"48"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d8f3a7445b40ac39
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050112Z-Acetate.md
  locator: 'YAML Record Review: Acetate:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c0403cbac72f71aacbf7c677d40f579d3e087718dc2057e7c3dd2d693438999b
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Acetate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    acetate identity and duplicate merge pass, but duplicate/provisional nutritional
    roles remain and SSSOM other exports contextual catabolization labels as ingredient
    surfaces.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Acetate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Acetate.yaml`,
    `just validate-terms data/ingredients/mapped/Acetate.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-31547d9fc9c1c8ca
  kind: prior_review
  reference: reports/yaml_record_review/Acetate.md
  locator: '`data/ingredients/mapped/Acetate.yaml`:2; Verdict:4; Identity:12; Validation:28;
    Evidence:45; Completeness:66; Recommended Edits:75'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3dc23437ef79bfbd7df92c6cdafe7acc5c28e596ed5e9d7a0ddd2b61cf7ba48d
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Acetate.yaml`, replace\
    \ or remove the provisional\n  `ENERGY_SOURCE` role and the duplicate provisional\
    \ `CARBON_SOURCE` role after\n  inspecting evidence that specifically supports\
    \ those assertions for acetate.\n- Move `aerobic catabolization: acetate` and\n\
    \  `anaerobic catabolization: acetate` out of SSSOM-exported synonym surfaces\n\
    \  while preserving their source traceability in the maintained record input.\n\
    - Rebuild `mappings/ingredient_mappings.sssom.tsv` from the maintained YAML and\n\
    \  re-run `scripts/validate_strict.py` plus\n  `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-6297834553ff64ad
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[195,1718,2056]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:d2f900514771b491f061","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:6d32ba1f8c319600e599","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4","finding_id":"SEM:f52e2cdff802bc3024c0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ad02f968da174887
  kind: record_content
  reference: data/ingredients/mapped/Acetate.yaml
  locator: nutritional_roles[1], nutritional_roles[2]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}},{"field":"nutritional_roles[2]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4
- evidence_id: ev-790918cc4cbc3c56
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-053648a807e87728]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-053648a807e87728 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-58063e257887793d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-edc7652497b859e8
  evidence_ids:
  - ev-ee665e7aebded001
  - ev-cda360c7f1061ed0
  - ev-cea5588a6e37d54d
  - ev-5e1821a8c0a9afcb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-827cb757b16d25f2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-edc7652497b859e8
  evidence_ids:
  - ev-d8f3a7445b40ac39
  - ev-31547d9fc9c1c8ca
  - ev-ee665e7aebded001
  - ev-6297834553ff64ad
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:12Z;
    reviewed SHA-256=f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4;
    current SHA-256=f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050112Z-Acetate.md","reports/yaml_record_review/Acetate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Acetate.md` after the record changed from 903a76864cf76781d05225e3520f3167a1815508bf9fdf8538cf10daf8c78fce
    to f567fa02e6ff94519c772a1025e329e7d14324599c14d13521f62c9f2d5e4cd4; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8f3a7445b40ac39
    - ev-31547d9fc9c1c8ca
    - ev-ee665e7aebded001
  - name: legacy-native-ids
    value: '["SEM:d2f900514771b491f061","SEM:6d32ba1f8c319600e599","SEM:f52e2cdff802bc3024c0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ee665e7aebded001
    - ev-d8f3a7445b40ac39
    - ev-31547d9fc9c1c8ca
    - ev-6297834553ff64ad
- assessment_id: a-ad02f968da174887
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-edc7652497b859e8
  evidence_ids:
  - ev-d8f3a7445b40ac39
  - ev-31547d9fc9c1c8ca
  - ev-ad02f968da174887
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8f3a7445b40ac39
    - ev-31547d9fc9c1c8ca
    - ev-ad02f968da174887
findings:
- finding_id: rec-f-053648a807e87728
  issue_key: mim-reconciliation-role-support-edc7652497b859e8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Acetate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-edc7652497b859e8
  evidence_ids:
  - ev-d8f3a7445b40ac39
  - ev-31547d9fc9c1c8ca
  - ev-ad02f968da174887
  - ev-790918cc4cbc3c56
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  - nutritional_roles[2]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-053648a807e87728
actions:
- action_id: rec-action-053648a807e87728
  description: 'Reassess prediction-only role support: Acetate'
  finding_ids:
  - rec-f-053648a807e87728
  target_ids:
  - record-edc7652497b859e8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Acetate.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
