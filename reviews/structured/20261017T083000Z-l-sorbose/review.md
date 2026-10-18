# Per-record structured review: L-_-sorbose (data/ingredients/mapped/L-_-sorbose.yaml)

- Review: 20261017T083000Z-l-sorbose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-_-sorbose (data/ingredients/mapped/L-_-sorbose.yaml, record-5c82fd440e0bfc66, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-_-sorbose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-_-sorbose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5c82fd440e0bfc66 | data/ingredients/mapped/L-_-sorbose.yaml | maintained | L-_-sorbose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5c82fd440e0bfc66 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5c82fd440e0bfc66 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5c82fd440e0bfc66 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5c82fd440e0bfc66.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5c82fd440e0bfc66.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:29:09Z; reviewed SHA-256=6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801; current SHA-256=6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801; hash_changed=False. Reports=["reports/yaml_record_review/L-_-sorbose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI lookup identity, active CHEBI:17266 grounding, ChEBI synonyms, PubChem identity, occurrence count, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-5c82fd440e0bfc66.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0fa88446526890f5: Reassess prediction-only role support: L-(-)-sorbose

major / open / confirmed; issue key: mim-reconciliation-role-support-5c82fd440e0bfc66.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0fa88446526890f5

Reassess prediction-only role support: L-(-)-sorbose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-529626fc88ea1f48 | data/ingredients/mapped/L-_-sorbose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1212],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17266","line":1214,"mapping_status":"MAPPED","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose"}],"identifier":"CHEBI:17266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17266","ontology_label":"L-sorbose","ontology_source":"CHEBI"},"preferred_term":"L-(-)-sorbose","sssom_rows":[{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-sorbose","synonym_count":2} |
| ev-11ac83bd31fbd8ab | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1212] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c8cb47266244e6d6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-_-sorbose; data-row positions=[1592] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","other":"(3S,4R,5S)-1,3,4,5,6-pentahydroxyhexan-2-one&#124;L-xylo-hex-2-ulose&#124;CAS:87-79-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-_-sorbose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-32fd401d4f01adff | docs/data/mapped_ingredients.csv; CSV lines=[1214] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17266","line":1214,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose","total_occurrences":"1"}] |
| ev-63482c52addd2929 | reports/yaml_record_review/L-_-sorbose.md; &#96;data/ingredients/mapped/L-_-sorbose.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:31; Completeness:48; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a8bfe616945df541 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[802,1706] | context_only | [{"current_record_sha256":"6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801","finding_id":"SEM:72e99bc2d874473301f7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801","finding_id":"SEM:0db69d35f3ea9dff459d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-533f3d4cf07676f6 | data/ingredients/mapped/L-_-sorbose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1212],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17266","line":1214,"mapping_status":"MAPPED","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose"}],"identifier":"CHEBI:17266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17266","ontology_label":"L-sorbose","ontology_source":"CHEBI"},"preferred_term":"L-(-)-sorbose","sssom_rows":[{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-sorbose","synonym_count":2} |
| ev-d4e63c511b35d4f9 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-0fa88446526890f5] | context_only | Predecessor structured review finding f-0fa88446526890f5 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-sorbose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-_-sorbose (data/ingredients/mapped/L-_-sorbose.yaml)'
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
summary: Per-record structured review for L-_-sorbose (data/ingredients/mapped/L-_-sorbose.yaml,
  record-5c82fd440e0bfc66, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-_-sorbose.yaml
    sha256: 6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801
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
  - path: reports/yaml_record_review/L-_-sorbose.md
    sha256: 18cd4bc3af73cb90b388fef609a89d3e6375cc82a9ae75e7b4db2cf0bc4bb264
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5c82fd440e0bfc66
  path: data/ingredients/mapped/L-_-sorbose.yaml
  label: L-_-sorbose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-sorbose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-_-sorbose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-_-sorbose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5c82fd440e0bfc66
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-529626fc88ea1f48
  - ev-11ac83bd31fbd8ab
  - ev-c8cb47266244e6d6
  - ev-32fd401d4f01adff
  - ev-533f3d4cf07676f6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-529626fc88ea1f48
  - ev-a8bfe616945df541
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-63482c52addd2929
  - ev-a8bfe616945df541
  - ev-d4e63c511b35d4f9
evidence:
- evidence_id: ev-529626fc88ea1f48
  kind: record_content
  reference: data/ingredients/mapped/L-_-sorbose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1212],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17266","line":1214,"mapping_status":"MAPPED","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose"}],"identifier":"CHEBI:17266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17266","ontology_label":"L-sorbose","ontology_source":"CHEBI"},"preferred_term":"L-(-)-sorbose","sssom_rows":[{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-sorbose","synonym_count":2}'
  snapshot_sha256: 6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801
- evidence_id: ev-11ac83bd31fbd8ab
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1212]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c8cb47266244e6d6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-_-sorbose; data-row positions=[1592]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","other":"(3S,4R,5S)-1,3,4,5,6-pentahydroxyhexan-2-one|L-xylo-hex-2-ulose|CAS:87-79-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-_-sorbose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-32fd401d4f01adff
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1214]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17266","line":1214,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-63482c52addd2929
  kind: prior_review
  reference: reports/yaml_record_review/L-_-sorbose.md
  locator: '`data/ingredients/mapped/L-_-sorbose.yaml`:2; Verdict:4; Identity:10;
    Validation:19; Evidence:31; Completeness:48; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 18cd4bc3af73cb90b388fef609a89d3e6375cc82a9ae75e7b4db2cf0bc4bb264
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-(-)-sorbose as\n  a carbon source.\n- Rerun strict, term, round-trip, role,\
    \ component, and SSSOM validation after\n  the role change."
- evidence_id: ev-a8bfe616945df541
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[802,1706]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801","finding_id":"SEM:72e99bc2d874473301f7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801","finding_id":"SEM:0db69d35f3ea9dff459d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-533f3d4cf07676f6
  kind: record_content
  reference: data/ingredients/mapped/L-_-sorbose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1212],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17266","line":1214,"mapping_status":"MAPPED","ontology_id":"CHEBI:17266","preferred_term":"L-(-)-sorbose"}],"identifier":"CHEBI:17266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17266","ontology_label":"L-sorbose","ontology_source":"CHEBI"},"preferred_term":"L-(-)-sorbose","sssom_rows":[{"data_row":1592,"object_id":"CHEBI:17266","object_label":"L-sorbose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-sorbose","synonym_count":2}'
  snapshot_sha256: 6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801
- evidence_id: ev-d4e63c511b35d4f9
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-0fa88446526890f5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0fa88446526890f5 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-1eb156bc36d2f1c6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-529626fc88ea1f48
  - ev-11ac83bd31fbd8ab
  - ev-c8cb47266244e6d6
  - ev-32fd401d4f01adff
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ebdba3361f6cad57
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-63482c52addd2929
  - ev-529626fc88ea1f48
  - ev-a8bfe616945df541
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:29:09Z;
    reviewed SHA-256=6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801;
    current SHA-256=6c8d96558f5a743d2f583ce0c3b7f916f807520c627777a032da90bc3c9ac801;
    hash_changed=False. Reports=["reports/yaml_record_review/L-_-sorbose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI
    lookup identity, active CHEBI:17266 grounding, ChEBI synonyms, PubChem identity,
    occurrence count, and final SSSOM row pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-63482c52addd2929
    - ev-529626fc88ea1f48
  - name: legacy-native-ids
    value: '["SEM:72e99bc2d874473301f7","SEM:0db69d35f3ea9dff459d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-529626fc88ea1f48
    - ev-63482c52addd2929
    - ev-a8bfe616945df541
- assessment_id: a-533f3d4cf07676f6
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-63482c52addd2929
  - ev-533f3d4cf07676f6
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-63482c52addd2929
    - ev-533f3d4cf07676f6
findings:
- finding_id: rec-f-0fa88446526890f5
  issue_key: mim-reconciliation-role-support-5c82fd440e0bfc66
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-(-)-sorbose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5c82fd440e0bfc66
  evidence_ids:
  - ev-63482c52addd2929
  - ev-533f3d4cf07676f6
  - ev-d4e63c511b35d4f9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-sorbose.yaml
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
    finding_id: f-0fa88446526890f5
actions:
- action_id: rec-action-0fa88446526890f5
  description: 'Reassess prediction-only role support: L-(-)-sorbose'
  finding_ids:
  - rec-f-0fa88446526890f5
  target_ids:
  - record-5c82fd440e0bfc66
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-sorbose.yaml
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
