# Per-record structured review: Bacto_Peptone (data/ingredients/mapped/Bacto_Peptone.yaml)

- Review: 20261017T083000Z-bacto-peptone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bacto_Peptone (data/ingredients/mapped/Bacto_Peptone.yaml, record-41facf2eff261c2d, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bacto_Peptone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bacto_Peptone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-41facf2eff261c2d | data/ingredients/mapped/Bacto_Peptone.yaml | maintained | Bacto_Peptone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-41facf2eff261c2d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-41facf2eff261c2d | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-41facf2eff261c2d | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-41facf2eff261c2d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-41facf2eff261c2d.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-10-01T05:01:35Z; reviewed SHA-256=864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655; current SHA-256=864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050135Z-Bacto_Peptone.md","reports/yaml_record_review/Bacto_Peptone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Bacto_Peptone.md&#96; after the record changed from 48eb2be26c06e8dc23f4d3b67bbd55b559dbc3b3a3600ce1c271f618ec199d69 to 864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655; no prior finding is carried forward.

### Historical provisional-role concern

evidence: concern. Targets: record-41facf2eff261c2d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-87a28cf48ab57697: Reassess prediction-only role support: Bacto peptone

major / open / confirmed; issue key: mim-reconciliation-role-support-41facf2eff261c2d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-87a28cf48ab57697

Reassess prediction-only role support: Bacto peptone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-524d0f8ca6da27fa | data/ingredients/mapped/Bacto_Peptone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[547],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000178","line":549,"mapping_status":"MAPPED","ontology_id":"MICRO:0000178","preferred_term":"Bacto peptone"}],"identifier":"MICRO:0000178","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2251,"edge_count":2251,"occurrences":2255},"occurrence_statistics":{"media_count":2251,"total_occurrences":2255},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000178","ontology_label":"peptone","ontology_source":"MICRO"},"preferred_term":"Bacto peptone","sssom_rows":[{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Peptone","synonym_count":30} |
| ev-ed65b132da976798 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [547] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5374891eedef19e9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bacto_Peptone; data-row positions=[480] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","other":"Bacto peptone (BD-Difco)&#124;Bacto Peptone (Difco)&#124;Bacto-Peptone (BD)&#124;Peptone, Bacto (BD 211677)&#124;Peptone (Oxoid)&#124;Peptone (BD--Difco)&#124;Peptone (BD Bacto)&#124;Peptone (BD-Difco)&#124;Peptone (BBL 11910)&#124;Oxoid peptone&#124;Bacto peptone (BD--Difco)&#124;Peptone from meat&#124;Peptone (meat)&#124;Peptone from meat (pepsin-digested)&#124;Bacteriological peptone&#124;Neopeptone&#124;Neopeptone (BD-Difco)&#124;Neopeptone (Difco Laboratories, Detroit, Ml)&#124;Gelatin peptone&#124;Universal peptone&#124;Universal peptone (Merck)&#124;Peptone mixture&#124;Fish peptone (Fluka)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bacto_Peptone","validation_method":"manual:apply_669_704_rulings&#124;OTHER&#124;2026-09-24"}] |
| ev-360de0a59dc002a8 | docs/data/mapped_ingredients.csv; CSV lines=[549] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000178","line":549,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2251","ontology_id":"MICRO:0000178","preferred_term":"Bacto peptone","total_occurrences":"2255"}] |
| ev-f71a5c61e40ce6b2 | reports/yaml_record_review/20261001T050135Z-Bacto_Peptone.md; YAML Record Review: Bacto peptone:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b4674e752f8ce4b5 | reports/yaml_record_review/Bacto_Peptone.md; &#96;data/ingredients/mapped/Bacto_Peptone.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:34; Completeness:51; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1c60f41fa6fd54d7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[2025] | context_only | [{"current_record_sha256":"864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655","finding_id":"SEM:98bcf3a6c3cc179d25ea","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-cae70c6299116da8 | data/ingredients/mapped/Bacto_Peptone.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[547],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000178","line":549,"mapping_status":"MAPPED","ontology_id":"MICRO:0000178","preferred_term":"Bacto peptone"}],"identifier":"MICRO:0000178","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2251,"edge_count":2251,"occurrences":2255},"occurrence_statistics":{"media_count":2251,"total_occurrences":2255},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000178","ontology_label":"peptone","ontology_source":"MICRO"},"preferred_term":"Bacto peptone","sssom_rows":[{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Peptone","synonym_count":30} |
| ev-e38bd699b422db42 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-87a28cf48ab57697] | context_only | Predecessor structured review finding f-87a28cf48ab57697 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bacto-peptone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bacto_Peptone (data/ingredients/mapped/Bacto_Peptone.yaml)'
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
summary: Per-record structured review for Bacto_Peptone (data/ingredients/mapped/Bacto_Peptone.yaml,
  record-41facf2eff261c2d, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bacto_Peptone.yaml
    sha256: 864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655
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
  - path: reports/yaml_record_review/20261001T050135Z-Bacto_Peptone.md
    sha256: a32a260f4fd205361375586be8ed4d2e8a26a2825bceda44a5fadba8744b7294
    role: context
  - path: reports/yaml_record_review/Bacto_Peptone.md
    sha256: 4e89ebe616720fc9908ef1749d0754a0d1bd01dd3f571eeaf504031f1257e721
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-41facf2eff261c2d
  path: data/ingredients/mapped/Bacto_Peptone.yaml
  label: Bacto_Peptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Peptone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bacto_Peptone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bacto_Peptone.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-41facf2eff261c2d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-524d0f8ca6da27fa
  - ev-ed65b132da976798
  - ev-5374891eedef19e9
  - ev-360de0a59dc002a8
  - ev-cae70c6299116da8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-524d0f8ca6da27fa
  - ev-1c60f41fa6fd54d7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-f71a5c61e40ce6b2
  - ev-b4674e752f8ce4b5
  - ev-1c60f41fa6fd54d7
  - ev-e38bd699b422db42
evidence:
- evidence_id: ev-524d0f8ca6da27fa
  kind: record_content
  reference: data/ingredients/mapped/Bacto_Peptone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[547],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000178","line":549,"mapping_status":"MAPPED","ontology_id":"MICRO:0000178","preferred_term":"Bacto
    peptone"}],"identifier":"MICRO:0000178","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2251,"edge_count":2251,"occurrences":2255},"occurrence_statistics":{"media_count":2251,"total_occurrences":2255},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000178","ontology_label":"peptone","ontology_source":"MICRO"},"preferred_term":"Bacto
    peptone","sssom_rows":[{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Peptone","synonym_count":30}'
  snapshot_sha256: 864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655
- evidence_id: ev-ed65b132da976798
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [547]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5374891eedef19e9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bacto_Peptone; data-row positions=[480]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","other":"Bacto
    peptone (BD-Difco)|Bacto Peptone (Difco)|Bacto-Peptone (BD)|Peptone, Bacto (BD
    211677)|Peptone (Oxoid)|Peptone (BD--Difco)|Peptone (BD Bacto)|Peptone (BD-Difco)|Peptone
    (BBL 11910)|Oxoid peptone|Bacto peptone (BD--Difco)|Peptone from meat|Peptone
    (meat)|Peptone from meat (pepsin-digested)|Bacteriological peptone|Neopeptone|Neopeptone
    (BD-Difco)|Neopeptone (Difco Laboratories, Detroit, Ml)|Gelatin peptone|Universal
    peptone|Universal peptone (Merck)|Peptone mixture|Fish peptone (Fluka)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bacto_Peptone","validation_method":"manual:apply_669_704_rulings|OTHER|2026-09-24"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-360de0a59dc002a8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[549]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000178","line":549,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2251","ontology_id":"MICRO:0000178","preferred_term":"Bacto
    peptone","total_occurrences":"2255"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f71a5c61e40ce6b2
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050135Z-Bacto_Peptone.md
  locator: 'YAML Record Review: Bacto peptone:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a32a260f4fd205361375586be8ed4d2e8a26a2825bceda44a5fadba8744b7294
  quote: 'Findings:

    None found.


    Recommended Edits:

    - None.'
- evidence_id: ev-b4674e752f8ce4b5
  kind: prior_review
  reference: reports/yaml_record_review/Bacto_Peptone.md
  locator: '`data/ingredients/mapped/Bacto_Peptone.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:34; Completeness:51; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4e89ebe616720fc9908ef1749d0754a0d1bd01dd3f571eeaf504031f1257e721
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-1c60f41fa6fd54d7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[2025]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655","finding_id":"SEM:98bcf3a6c3cc179d25ea","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-cae70c6299116da8
  kind: record_content
  reference: data/ingredients/mapped/Bacto_Peptone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[547],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000178","line":549,"mapping_status":"MAPPED","ontology_id":"MICRO:0000178","preferred_term":"Bacto
    peptone"}],"identifier":"MICRO:0000178","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2251,"edge_count":2251,"occurrences":2255},"occurrence_statistics":{"media_count":2251,"total_occurrences":2255},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000178","ontology_label":"peptone","ontology_source":"MICRO"},"preferred_term":"Bacto
    peptone","sssom_rows":[{"data_row":480,"object_id":"MICRO:0000178","object_label":"peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Peptone","synonym_count":30}'
  snapshot_sha256: 864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655
- evidence_id: ev-e38bd699b422db42
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-87a28cf48ab57697]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-87a28cf48ab57697 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-b2c4f0ce0fe5a989
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-524d0f8ca6da27fa
  - ev-ed65b132da976798
  - ev-5374891eedef19e9
  - ev-360de0a59dc002a8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9989083cbbd21db0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-f71a5c61e40ce6b2
  - ev-b4674e752f8ce4b5
  - ev-524d0f8ca6da27fa
  - ev-1c60f41fa6fd54d7
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-10-01T05:01:35Z;
    reviewed SHA-256=864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655;
    current SHA-256=864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050135Z-Bacto_Peptone.md","reports/yaml_record_review/Bacto_Peptone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Bacto_Peptone.md` after the record changed from 48eb2be26c06e8dc23f4d3b67bbd55b559dbc3b3a3600ce1c271f618ec199d69
    to 864e86820c578ff82b2b32e075c6fb428e704907f78a250c2733b06a70d8e655; no prior
    finding is carried forward.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:98bcf3a6c3cc179d25ea"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-524d0f8ca6da27fa
    - ev-f71a5c61e40ce6b2
    - ev-b4674e752f8ce4b5
    - ev-1c60f41fa6fd54d7
- assessment_id: a-cae70c6299116da8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-f71a5c61e40ce6b2
  - ev-b4674e752f8ce4b5
  - ev-cae70c6299116da8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f71a5c61e40ce6b2
    - ev-b4674e752f8ce4b5
    - ev-cae70c6299116da8
findings:
- finding_id: rec-f-87a28cf48ab57697
  issue_key: mim-reconciliation-role-support-41facf2eff261c2d
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Bacto peptone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-41facf2eff261c2d
  evidence_ids:
  - ev-f71a5c61e40ce6b2
  - ev-b4674e752f8ce4b5
  - ev-cae70c6299116da8
  - ev-e38bd699b422db42
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Peptone.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-87a28cf48ab57697
actions:
- action_id: rec-action-87a28cf48ab57697
  description: 'Reassess prediction-only role support: Bacto peptone'
  finding_ids:
  - rec-f-87a28cf48ab57697
  target_ids:
  - record-41facf2eff261c2d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Peptone.yaml
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
