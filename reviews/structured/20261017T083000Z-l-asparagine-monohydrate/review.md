# Per-record structured review: L-Asparagine_Monohydrate (data/ingredients/mapped/L-Asparagine_Monohydrate.yaml)

- Review: 20261017T083000Z-l-asparagine-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Asparagine_Monohydrate (data/ingredients/mapped/L-Asparagine_Monohydrate.yaml, record-fa315281a3bf9ea3, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Asparagine_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Asparagine_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fa315281a3bf9ea3 | data/ingredients/mapped/L-Asparagine_Monohydrate.yaml | maintained | L-Asparagine_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fa315281a3bf9ea3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-fa315281a3bf9ea3 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fa315281a3bf9ea3 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fa315281a3bf9ea3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fa315281a3bf9ea3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:55:10Z; reviewed SHA-256=0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a; current SHA-256=0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a; hash_changed=False. Reports=["reports/yaml_record_review/L-Asparagine_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, hydrate-specific PubChem structure, NCIT parent mapping, registry rows, and hydrate review pass, but AMINO_ACID_SOURCE is only provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-fa315281a3bf9ea3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5ddff4c316c75a01: Reassess prediction-only role support: L-Asparagine monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-fa315281a3bf9ea3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5ddff4c316c75a01

Reassess prediction-only role support: L-Asparagine monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-15619c929c40b814 | data/ingredients/mapped/L-Asparagine_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1215],"raw_equal":true},"docs_rows":[{"identifier":"cas:5794-13-8","line":1217,"mapping_status":"MAPPED","ontology_id":"NCIT:C87433","preferred_term":"L-Asparagine monohydrate"}],"identifier":"cas:5794-13-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C87433","ontology_label":"Asparagine Monohydrate","ontology_source":"NCIT"},"preferred_term":"L-Asparagine monohydrate","sssom_rows":[{"data_row":1557,"object_id":"NCIT:C87433","object_label":"Asparagine Monohydrate","predicate_id":"skos:broadMatch"},{"data_row":1558,"object_id":"cas:5794-13-8","object_label":"L-Asparagine monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1559,"object_id":"kgmicrobe.compound:l-asparagine_monohydrate","object_label":"L-Asparagine monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Asparagine_Monohydrate","synonym_count":0} |
| ev-0dea1e2949996e25 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1215] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6e4be19be390d634 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Asparagine_Monohydrate; data-row positions=[1557,1558,1559] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1557,"object_id":"NCIT:C87433","object_label":"Asparagine Monohydrate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1558,"object_id":"cas:5794-13-8","object_label":"L-Asparagine monohydrate","other":"CAS:5794-13-8","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1559,"object_id":"kgmicrobe.compound:l-asparagine_monohydrate","object_label":"L-Asparagine monohydrate","other":"CAS:5794-13-8","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1d031265424c8188 | docs/data/mapped_ingredients.csv; CSV lines=[1217] | supports | Published identity and count rows inspected: [{"identifier":"cas:5794-13-8","line":1217,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C87433","preferred_term":"L-Asparagine monohydrate","total_occurrences":"0"}] |
| ev-218366f9451ca5cb | reports/yaml_record_review/L-Asparagine_Monohydrate.md; &#96;data/ingredients/mapped/L-Asparagine_Monohydrate.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:57; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a86287571134c5db | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[782,1781] | context_only | [{"current_record_sha256":"0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a","finding_id":"SEM:8cc40ab2caedd264d5c6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a","finding_id":"SEM:eb8d5775f500d35ba87e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b839f807e1db131b | data/ingredients/mapped/L-Asparagine_Monohydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-136d938db0504c0a | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-5ddff4c316c75a01] | context_only | Predecessor structured review finding f-5ddff4c316c75a01 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-asparagine-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Asparagine_Monohydrate (data/ingredients/mapped/L-Asparagine_Monohydrate.yaml)'
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
summary: Per-record structured review for L-Asparagine_Monohydrate (data/ingredients/mapped/L-Asparagine_Monohydrate.yaml,
  record-fa315281a3bf9ea3, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
    sha256: 0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a
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
  - path: reports/yaml_record_review/L-Asparagine_Monohydrate.md
    sha256: 80bd86cf125b59abace6703abc05d30937c7e28c523c72fa4585e982b6ae8de8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fa315281a3bf9ea3
  path: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
  label: L-Asparagine_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Asparagine_Monohydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fa315281a3bf9ea3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fa315281a3bf9ea3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-fa315281a3bf9ea3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fa315281a3bf9ea3
evidence:
- evidence_id: ev-15619c929c40b814
  kind: record_content
  reference: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1215],"raw_equal":true},"docs_rows":[{"identifier":"cas:5794-13-8","line":1217,"mapping_status":"MAPPED","ontology_id":"NCIT:C87433","preferred_term":"L-Asparagine
    monohydrate"}],"identifier":"cas:5794-13-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C87433","ontology_label":"Asparagine
    Monohydrate","ontology_source":"NCIT"},"preferred_term":"L-Asparagine monohydrate","sssom_rows":[{"data_row":1557,"object_id":"NCIT:C87433","object_label":"Asparagine
    Monohydrate","predicate_id":"skos:broadMatch"},{"data_row":1558,"object_id":"cas:5794-13-8","object_label":"L-Asparagine
    monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1559,"object_id":"kgmicrobe.compound:l-asparagine_monohydrate","object_label":"L-Asparagine
    monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Asparagine_Monohydrate","synonym_count":0}'
  snapshot_sha256: 0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a
- evidence_id: ev-0dea1e2949996e25
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1215]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6e4be19be390d634
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Asparagine_Monohydrate; data-row positions=[1557,1558,1559]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1557,"object_id":"NCIT:C87433","object_label":"Asparagine
    Monohydrate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1558,"object_id":"cas:5794-13-8","object_label":"L-Asparagine
    monohydrate","other":"CAS:5794-13-8","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1559,"object_id":"kgmicrobe.compound:l-asparagine_monohydrate","object_label":"L-Asparagine
    monohydrate","other":"CAS:5794-13-8","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Asparagine_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1d031265424c8188
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1217]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:5794-13-8","line":1217,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C87433","preferred_term":"L-Asparagine
    monohydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-218366f9451ca5cb
  kind: prior_review
  reference: reports/yaml_record_review/L-Asparagine_Monohydrate.md
  locator: '`data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`:2; Verdict:4;
    Identity:10; Validation:20; Evidence:31; Completeness:57; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 80bd86cf125b59abace6703abc05d30937c7e28c523c72fa4585e982b6ae8de8
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ unless an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-asparagine\n  monohydrate as an amino acid source, then rerun strict, term,\
    \ round-trip,\n  component, and SSSOM validation."
- evidence_id: ev-a86287571134c5db
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[782,1781]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a","finding_id":"SEM:8cc40ab2caedd264d5c6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a","finding_id":"SEM:eb8d5775f500d35ba87e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b839f807e1db131b
  kind: record_content
  reference: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a
- evidence_id: ev-136d938db0504c0a
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-5ddff4c316c75a01]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5ddff4c316c75a01 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-17f1e800ad14de76
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fa315281a3bf9ea3
  evidence_ids:
  - ev-15619c929c40b814
  - ev-0dea1e2949996e25
  - ev-6e4be19be390d634
  - ev-1d031265424c8188
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c382ca8d20452ff0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fa315281a3bf9ea3
  evidence_ids:
  - ev-218366f9451ca5cb
  - ev-15619c929c40b814
  - ev-a86287571134c5db
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:55:10Z;
    reviewed SHA-256=0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a;
    current SHA-256=0f3972bdde44bc5bf922cef4cfa8748d3cd18b5dd7bd9ebea77ae8e6659ed11a;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Asparagine_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, hydrate-specific PubChem structure, NCIT parent mapping, registry
    rows, and hydrate review pass, but AMINO_ACID_SOURCE is only provisional name-pattern
    evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-218366f9451ca5cb
    - ev-15619c929c40b814
  - name: legacy-native-ids
    value: '["SEM:8cc40ab2caedd264d5c6","SEM:eb8d5775f500d35ba87e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-15619c929c40b814
    - ev-218366f9451ca5cb
    - ev-a86287571134c5db
- assessment_id: a-b839f807e1db131b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-fa315281a3bf9ea3
  evidence_ids:
  - ev-218366f9451ca5cb
  - ev-b839f807e1db131b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-218366f9451ca5cb
    - ev-b839f807e1db131b
findings:
- finding_id: rec-f-5ddff4c316c75a01
  issue_key: mim-reconciliation-role-support-fa315281a3bf9ea3
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Asparagine monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-fa315281a3bf9ea3
  evidence_ids:
  - ev-218366f9451ca5cb
  - ev-b839f807e1db131b
  - ev-136d938db0504c0a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
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
    finding_id: f-5ddff4c316c75a01
actions:
- action_id: rec-action-5ddff4c316c75a01
  description: 'Reassess prediction-only role support: L-Asparagine monohydrate'
  finding_ids:
  - rec-f-5ddff4c316c75a01
  target_ids:
  - record-fa315281a3bf9ea3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Asparagine_Monohydrate.yaml
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
