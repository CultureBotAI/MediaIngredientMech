# Per-record structured review: Kanamycin_Sulfate (data/ingredients/mapped/Kanamycin_Sulfate.yaml)

- Review: 20261017T083000Z-kanamycin-sulfate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Kanamycin_Sulfate (data/ingredients/mapped/Kanamycin_Sulfate.yaml, record-5025158d79c4edf2, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Kanamycin_Sulfate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Kanamycin_Sulfate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5025158d79c4edf2 | data/ingredients/mapped/Kanamycin_Sulfate.yaml | maintained | Kanamycin_Sulfate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5025158d79c4edf2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5025158d79c4edf2 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5025158d79c4edf2 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5025158d79c4edf2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5025158d79c4edf2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z; reviewed SHA-256=cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9; current SHA-256=cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9; hash_changed=False. Reports=["reports/yaml_record_review/Kanamycin_Sulfate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact kanamycin A sulfate identity, structure fields, specific synonyms, and occurrence count pass, but the stored/exported CAS RN is transposed and SELECTIVE_AGENT is only provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-5025158d79c4edf2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-995e19f27734a72a: Reassess prediction-only role support: Kanamycin sulfate

major / open / confirmed; issue key: mim-reconciliation-role-support-5025158d79c4edf2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-995e19f27734a72a

Reassess prediction-only role support: Kanamycin sulfate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-aec2e820a58514e8 | data/ingredients/mapped/Kanamycin_Sulfate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1194],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6109","line":1196,"mapping_status":"MAPPED","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin sulfate"}],"identifier":"CHEBI:6109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6109","ontology_label":"kanamycin A sulfate","ontology_source":"CHEBI"},"preferred_term":"Kanamycin sulfate","sssom_rows":[{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin A sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanamycin_Sulfate","synonym_count":3} |
| ev-9ab35439c926283b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1194] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ad884d9a8ee0ce7a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Kanamycin_Sulfate; data-row positions=[1536] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin A sulfate","other":"Kanamycin acid sulfate&#124;Kanamycin monosulfate&#124;CAS:25839-94-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Kanamycin_Sulfate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-46180dd83b1e7099 | docs/data/mapped_ingredients.csv; CSV lines=[1196] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:6109","line":1196,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin sulfate","total_occurrences":"5"}] |
| ev-2cce1985a14d5952 | reports/yaml_record_review/Kanamycin_Sulfate.md; &#96;data/ingredients/mapped/Kanamycin_Sulfate.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:34; Completeness:56; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-53928600275cfca8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[766,1498] | context_only | [{"current_record_sha256":"cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9","finding_id":"SEM:b92b5ae994d585b63443","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9","finding_id":"SEM:51d17cb238ada5117c7c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9e14794ac5eacae7 | data/ingredients/mapped/Kanamycin_Sulfate.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1194],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6109","line":1196,"mapping_status":"MAPPED","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin sulfate"}],"identifier":"CHEBI:6109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6109","ontology_label":"kanamycin A sulfate","ontology_source":"CHEBI"},"preferred_term":"Kanamycin sulfate","sssom_rows":[{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin A sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanamycin_Sulfate","synonym_count":3} |
| ev-47d685373c4acf65 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-995e19f27734a72a] | context_only | Predecessor structured review finding f-995e19f27734a72a in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-kanamycin-sulfate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Kanamycin_Sulfate (data/ingredients/mapped/Kanamycin_Sulfate.yaml)'
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
summary: Per-record structured review for Kanamycin_Sulfate (data/ingredients/mapped/Kanamycin_Sulfate.yaml,
  record-5025158d79c4edf2, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Kanamycin_Sulfate.yaml
    sha256: cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9
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
  - path: reports/yaml_record_review/Kanamycin_Sulfate.md
    sha256: 6ccd007af05634cdb0484f80410162e4043176dc9fd7996aba3b610d4348afd7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5025158d79c4edf2
  path: data/ingredients/mapped/Kanamycin_Sulfate.yaml
  label: Kanamycin_Sulfate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanamycin_Sulfate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Kanamycin_Sulfate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Kanamycin_Sulfate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5025158d79c4edf2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-aec2e820a58514e8
  - ev-9ab35439c926283b
  - ev-ad884d9a8ee0ce7a
  - ev-46180dd83b1e7099
  - ev-9e14794ac5eacae7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-aec2e820a58514e8
  - ev-53928600275cfca8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-2cce1985a14d5952
  - ev-53928600275cfca8
  - ev-47d685373c4acf65
evidence:
- evidence_id: ev-aec2e820a58514e8
  kind: record_content
  reference: data/ingredients/mapped/Kanamycin_Sulfate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1194],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6109","line":1196,"mapping_status":"MAPPED","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin
    sulfate"}],"identifier":"CHEBI:6109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6109","ontology_label":"kanamycin
    A sulfate","ontology_source":"CHEBI"},"preferred_term":"Kanamycin sulfate","sssom_rows":[{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin
    A sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanamycin_Sulfate","synonym_count":3}'
  snapshot_sha256: cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9
- evidence_id: ev-9ab35439c926283b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1194]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ad884d9a8ee0ce7a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Kanamycin_Sulfate; data-row positions=[1536]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin
    A sulfate","other":"Kanamycin acid sulfate|Kanamycin monosulfate|CAS:25839-94-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Kanamycin_Sulfate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-46180dd83b1e7099
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1196]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:6109","line":1196,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin
    sulfate","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2cce1985a14d5952
  kind: prior_review
  reference: reports/yaml_record_review/Kanamycin_Sulfate.md
  locator: '`data/ingredients/mapped/Kanamycin_Sulfate.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:34; Completeness:56; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6ccd007af05634cdb0484f80410162e4043176dc9fd7996aba3b610d4348afd7
  quote: "Recommended Edits:\n- Major: replace `chemical_properties.cas_rn: 25839-94-0`\
    \ with\n  `25389-94-0` in `data/ingredients/mapped/Kanamycin_Sulfate.yaml` and\
    \ rebuild\n  final SSSOM/docs surfaces so `CAS:25839-94-0` is no longer published.\n\
    - Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected\n\
    \  CultureMech, FEBA, Hans80, or literature source can support kanamycin sulfate\n\
    \  as a selective agent, then rerun strict, term, round-trip, id-label,\n  component,\
    \ and SSSOM validation."
- evidence_id: ev-53928600275cfca8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[766,1498]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9","finding_id":"SEM:b92b5ae994d585b63443","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9","finding_id":"SEM:51d17cb238ada5117c7c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9e14794ac5eacae7
  kind: record_content
  reference: data/ingredients/mapped/Kanamycin_Sulfate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1194],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6109","line":1196,"mapping_status":"MAPPED","ontology_id":"CHEBI:6109","preferred_term":"Kanamycin
    sulfate"}],"identifier":"CHEBI:6109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6109","ontology_label":"kanamycin
    A sulfate","ontology_source":"CHEBI"},"preferred_term":"Kanamycin sulfate","sssom_rows":[{"data_row":1536,"object_id":"CHEBI:6109","object_label":"kanamycin
    A sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanamycin_Sulfate","synonym_count":3}'
  snapshot_sha256: cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9
- evidence_id: ev-47d685373c4acf65
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-995e19f27734a72a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-995e19f27734a72a in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-fc0929887c4e4136
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-aec2e820a58514e8
  - ev-9ab35439c926283b
  - ev-ad884d9a8ee0ce7a
  - ev-46180dd83b1e7099
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-114e854a87eb7888
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-2cce1985a14d5952
  - ev-aec2e820a58514e8
  - ev-53928600275cfca8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z;
    reviewed SHA-256=cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9;
    current SHA-256=cd1bbebd8e516d860b4b8823a9a8920643443f4d86b5e92b68f90337415dc5a9;
    hash_changed=False. Reports=["reports/yaml_record_review/Kanamycin_Sulfate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    kanamycin A sulfate identity, structure fields, specific synonyms, and occurrence
    count pass, but the stored/exported CAS RN is transposed and SELECTIVE_AGENT is
    only provisional name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2cce1985a14d5952
    - ev-aec2e820a58514e8
  - name: legacy-native-ids
    value: '["SEM:b92b5ae994d585b63443","SEM:51d17cb238ada5117c7c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-aec2e820a58514e8
    - ev-2cce1985a14d5952
    - ev-53928600275cfca8
- assessment_id: a-9e14794ac5eacae7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-2cce1985a14d5952
  - ev-9e14794ac5eacae7
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2cce1985a14d5952
    - ev-9e14794ac5eacae7
findings:
- finding_id: rec-f-995e19f27734a72a
  issue_key: mim-reconciliation-role-support-5025158d79c4edf2
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Kanamycin sulfate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5025158d79c4edf2
  evidence_ids:
  - ev-2cce1985a14d5952
  - ev-9e14794ac5eacae7
  - ev-47d685373c4acf65
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanamycin_Sulfate.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-995e19f27734a72a
actions:
- action_id: rec-action-995e19f27734a72a
  description: 'Reassess prediction-only role support: Kanamycin sulfate'
  finding_ids:
  - rec-f-995e19f27734a72a
  target_ids:
  - record-5025158d79c4edf2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanamycin_Sulfate.yaml
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
