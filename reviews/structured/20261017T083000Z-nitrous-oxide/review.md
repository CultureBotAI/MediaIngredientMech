# Per-record structured review: Nitrous_Oxide (data/ingredients/mapped/Nitrous_Oxide.yaml)

- Review: 20261017T083000Z-nitrous-oxide
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nitrous_Oxide (data/ingredients/mapped/Nitrous_Oxide.yaml, record-de13dbf9e28ba243, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nitrous_Oxide.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nitrous_Oxide.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-de13dbf9e28ba243 | data/ingredients/mapped/Nitrous_Oxide.yaml | maintained | Nitrous_Oxide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-de13dbf9e28ba243 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-de13dbf9e28ba243 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-de13dbf9e28ba243 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-de13dbf9e28ba243.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-de13dbf9e28ba243.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:06Z; reviewed SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; current SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md","reports/yaml_record_review/Nitrous_Oxide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nitrous_Oxide.md&#96; after the record changed from 1d7b0c658dd8c1fc20d80f2620be3bc7c3d690a50912aa1191a2c345b76c41c9 to 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-d4f70f2e79cd02b6: Historical review coverage and residual narrative: Nitrous_Oxide

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-de13dbf9e28ba243.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:06Z; reviewed SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; current SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md","reports/yaml_record_review/Nitrous_Oxide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nitrous_Oxide.md&#96; after the record changed from 1d7b0c658dd8c1fc20d80f2620be3bc7c3d690a50912aa1191a2c345b76c41c9 to 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e393140d4b4d625d | data/ingredients/mapped/Nitrous_Oxide.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1573],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17045","line":1575,"mapping_status":"MAPPED","ontology_id":"CHEBI:17045","preferred_term":"nitrous oxide"}],"identifier":"CHEBI:17045","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17045","ontology_label":"dinitrogen oxide","ontology_source":"CHEBI"},"preferred_term":"nitrous oxide","sssom_rows":[{"data_row":2105,"object_id":"CHEBI:17045","object_label":"dinitrogen oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nitrous_Oxide","synonym_count":3} |
| ev-711e8168da945a08 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1573] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8097563fa69f95d1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nitrous_Oxide; data-row positions=[2105] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2105,"object_id":"CHEBI:17045","object_label":"dinitrogen oxide","other":"N2O&#124;#N2O&#124;oxidodinitrogen(N--N)&#124;CAS:10024-97-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Nitrous_Oxide","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-6ed50aae342795cd | docs/data/mapped_ingredients.csv; CSV lines=[1575] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17045","line":1575,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:17045","preferred_term":"nitrous oxide","total_occurrences":"3"}] |
| ev-8b8fd4d9b8217426 | reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md; YAML Record Review: nitrous oxide:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f9e03bebf29c60c0 | reports/yaml_record_review/Nitrous_Oxide.md; &#96;data/ingredients/mapped/Nitrous_Oxide.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:42; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9435cd1021c785f6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1068,1670] | context_only | [{"current_record_sha256":"1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932","finding_id":"SEM:ae1734ed896fc48df064","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932","finding_id":"SEM:ec34f295bf948a3abbff","kind":"role_evidence","resolution_reason":"Growth and N2O consumption were measured together in the named isolates with acetate supplying electrons. The role is confined to these tested nitrous-oxide-respiring cultures.","resolution_status":"RESOLVED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nitrous-oxide
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nitrous_Oxide (data/ingredients/mapped/Nitrous_Oxide.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Nitrous_Oxide (data/ingredients/mapped/Nitrous_Oxide.yaml,
  record-de13dbf9e28ba243, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nitrous_Oxide.yaml
    sha256: 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md
    sha256: fe5138a476ee42ea4e3118c73625571da6ca207a36d17879678f593cf12c75ac
    role: context
  - path: reports/yaml_record_review/Nitrous_Oxide.md
    sha256: c0c81410590fa921a3fc58af98b746d705834e04cd7ea9defb616654777b1bf4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-de13dbf9e28ba243
  path: data/ingredients/mapped/Nitrous_Oxide.yaml
  label: Nitrous_Oxide
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nitrous_Oxide.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nitrous_Oxide.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nitrous_Oxide.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-de13dbf9e28ba243
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-de13dbf9e28ba243
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-de13dbf9e28ba243
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-de13dbf9e28ba243
evidence:
- evidence_id: ev-e393140d4b4d625d
  kind: record_content
  reference: data/ingredients/mapped/Nitrous_Oxide.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1573],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17045","line":1575,"mapping_status":"MAPPED","ontology_id":"CHEBI:17045","preferred_term":"nitrous
    oxide"}],"identifier":"CHEBI:17045","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:17045","ontology_label":"dinitrogen
    oxide","ontology_source":"CHEBI"},"preferred_term":"nitrous oxide","sssom_rows":[{"data_row":2105,"object_id":"CHEBI:17045","object_label":"dinitrogen
    oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nitrous_Oxide","synonym_count":3}'
  snapshot_sha256: 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932
- evidence_id: ev-711e8168da945a08
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1573]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8097563fa69f95d1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nitrous_Oxide; data-row positions=[2105]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2105,"object_id":"CHEBI:17045","object_label":"dinitrogen
    oxide","other":"N2O|#N2O|oxidodinitrogen(N--N)|CAS:10024-97-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Nitrous_Oxide","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6ed50aae342795cd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1575]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17045","line":1575,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:17045","preferred_term":"nitrous
    oxide","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8b8fd4d9b8217426
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md
  locator: 'YAML Record Review: nitrous oxide:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fe5138a476ee42ea4e3118c73625571da6ca207a36d17879678f593cf12c75ac
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Nitrous_Oxide.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:17045 nitrous oxide identity passes, but ELECTRON_ACCEPTOR is only provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Nitrous_Oxide.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Nitrous_Oxide.yaml`,
    `just validate-terms data/ingredients/mapped/Nitrous_Oxide.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-f9e03bebf29c60c0
  kind: prior_review
  reference: reports/yaml_record_review/Nitrous_Oxide.md
  locator: '`data/ingredients/mapped/Nitrous_Oxide.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:42; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c0c81410590fa921a3fc58af98b746d705834e04cd7ea9defb616654777b1bf4
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nitrous_Oxide.yaml`,\
    \ replace the\n  `ELECTRON_ACCEPTOR` role evidence with inspected source-backed\
    \ evidence for\n  nitrous oxide acting as a media electron acceptor, or remove\
    \ the role until\n  that evidence exists."
- evidence_id: ev-9435cd1021c785f6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1068,1670]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932","finding_id":"SEM:ae1734ed896fc48df064","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932","finding_id":"SEM:ec34f295bf948a3abbff","kind":"role_evidence","resolution_reason":"Growth
    and N2O consumption were measured together in the named isolates with acetate
    supplying electrons. The role is confined to these tested nitrous-oxide-respiring
    cultures.","resolution_status":"RESOLVED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3dc34607aa2b93f5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-de13dbf9e28ba243
  evidence_ids:
  - ev-e393140d4b4d625d
  - ev-711e8168da945a08
  - ev-8097563fa69f95d1
  - ev-6ed50aae342795cd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ffe28bfcb4518a2e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-de13dbf9e28ba243
  evidence_ids:
  - ev-8b8fd4d9b8217426
  - ev-f9e03bebf29c60c0
  - ev-e393140d4b4d625d
  - ev-9435cd1021c785f6
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:06Z;
    reviewed SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932;
    current SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md","reports/yaml_record_review/Nitrous_Oxide.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nitrous_Oxide.md` after the record changed from 1d7b0c658dd8c1fc20d80f2620be3bc7c3d690a50912aa1191a2c345b76c41c9
    to 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8b8fd4d9b8217426
    - ev-f9e03bebf29c60c0
    - ev-e393140d4b4d625d
  - name: legacy-native-ids
    value: '["SEM:ae1734ed896fc48df064","SEM:ec34f295bf948a3abbff"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e393140d4b4d625d
    - ev-8b8fd4d9b8217426
    - ev-f9e03bebf29c60c0
    - ev-9435cd1021c785f6
findings:
- finding_id: rec-f-d4f70f2e79cd02b6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-de13dbf9e28ba243
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nitrous_Oxide'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:06Z;
    reviewed SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932;
    current SHA-256=1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050306Z-Nitrous_Oxide.md","reports/yaml_record_review/Nitrous_Oxide.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nitrous_Oxide.md` after the record changed from 1d7b0c658dd8c1fc20d80f2620be3bc7c3d690a50912aa1191a2c345b76c41c9
    to 1d11386343ebe50b5f2504359b14ae0818b092f532d99768e1a897143b513932; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-de13dbf9e28ba243
  evidence_ids:
  - ev-8b8fd4d9b8217426
  - ev-f9e03bebf29c60c0
  - ev-e393140d4b4d625d
  - ev-9435cd1021c785f6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nitrous_Oxide.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
