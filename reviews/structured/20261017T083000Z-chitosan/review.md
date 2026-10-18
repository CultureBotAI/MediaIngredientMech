# Per-record structured review: Chitosan (data/ingredients/mapped/Chitosan.yaml)

- Review: 20261017T083000Z-chitosan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Chitosan (data/ingredients/mapped/Chitosan.yaml, record-bd5b968443fd15bd, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Chitosan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Chitosan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bd5b968443fd15bd | data/ingredients/mapped/Chitosan.yaml | maintained | Chitosan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bd5b968443fd15bd | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-bd5b968443fd15bd | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bd5b968443fd15bd | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bd5b968443fd15bd.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bd5b968443fd15bd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:51Z; reviewed SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; current SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050151Z-Chitosan.md","reports/yaml_record_review/Chitosan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Chitosan.md&#96; after the record changed from 65e848e860f525ec047bfb123e2852a74d62ac42a68ab2abf2f7b00e8264a0e9 to e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-b5a14b417c9397b7: Historical review coverage and residual narrative: Chitosan

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-bd5b968443fd15bd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:51Z; reviewed SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; current SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050151Z-Chitosan.md","reports/yaml_record_review/Chitosan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Chitosan.md&#96; after the record changed from 65e848e860f525ec047bfb123e2852a74d62ac42a68ab2abf2f7b00e8264a0e9 to e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4c27023d56350852 | data/ingredients/mapped/Chitosan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[707],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16261","line":709,"mapping_status":"MAPPED","ontology_id":"CHEBI:16261","preferred_term":"Chitosan"}],"identifier":"CHEBI:16261","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16261","ontology_label":"chitosan","ontology_source":"CHEBI"},"preferred_term":"Chitosan","sssom_rows":[{"data_row":738,"object_id":"CHEBI:16261","object_label":"chitosan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitosan","synonym_count":7} |
| ev-c08363128fe34811 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [707] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-57677508f3efb153 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Chitosan; data-row positions=[738] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":738,"object_id":"CHEBI:16261","object_label":"chitosan","other":"(1-&gt;4)-2-amino-2-deoxy-beta-D-glucan&#124;Deacetylchitin&#124;[4)-beta-D-GlcpN(1-&gt;]n&#124;beta-1,4-Poly-D-glucosamine&#124;poliglusam&#124;CAS:9012-76-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Chitosan","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-afc51c9707b15eac | docs/data/mapped_ingredients.csv; CSV lines=[709] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16261","line":709,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:16261","preferred_term":"Chitosan","total_occurrences":"3"}] |
| ev-467e6b2403ebb648 | reports/yaml_record_review/20261001T050151Z-Chitosan.md; YAML Record Review: Chitosan:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-49eb096564b1a02b | reports/yaml_record_review/Chitosan.md; &#96;data/ingredients/mapped/Chitosan.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:56; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-daf4bae9f2fb1193 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[404] | context_only | [{"current_record_sha256":"e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2","finding_id":"SEM:dcd6713b97cc00ee9d67","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-chitosan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Chitosan (data/ingredients/mapped/Chitosan.yaml)'
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
summary: Per-record structured review for Chitosan (data/ingredients/mapped/Chitosan.yaml,
  record-bd5b968443fd15bd, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Chitosan.yaml
    sha256: e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/20261001T050151Z-Chitosan.md
    sha256: 865c3f27e54f14c8e2fc68818906bc7d0ca18cd0251d8049de213c7b68e8bca1
    role: context
  - path: reports/yaml_record_review/Chitosan.md
    sha256: 16553291c0fdfaa20a5ade24a3986d6f7ae00ff1dc7ef414cad7bba5b8ce8e1c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bd5b968443fd15bd
  path: data/ingredients/mapped/Chitosan.yaml
  label: Chitosan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Chitosan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Chitosan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Chitosan.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bd5b968443fd15bd
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bd5b968443fd15bd
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-bd5b968443fd15bd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bd5b968443fd15bd
evidence:
- evidence_id: ev-4c27023d56350852
  kind: record_content
  reference: data/ingredients/mapped/Chitosan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[707],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16261","line":709,"mapping_status":"MAPPED","ontology_id":"CHEBI:16261","preferred_term":"Chitosan"}],"identifier":"CHEBI:16261","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16261","ontology_label":"chitosan","ontology_source":"CHEBI"},"preferred_term":"Chitosan","sssom_rows":[{"data_row":738,"object_id":"CHEBI:16261","object_label":"chitosan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitosan","synonym_count":7}'
  snapshot_sha256: e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2
- evidence_id: ev-c08363128fe34811
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [707]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-57677508f3efb153
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Chitosan; data-row positions=[738]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":738,"object_id":"CHEBI:16261","object_label":"chitosan","other":"(1->4)-2-amino-2-deoxy-beta-D-glucan|Deacetylchitin|[4)-beta-D-GlcpN(1->]n|beta-1,4-Poly-D-glucosamine|poliglusam|CAS:9012-76-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Chitosan","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-afc51c9707b15eac
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[709]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16261","line":709,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:16261","preferred_term":"Chitosan","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-467e6b2403ebb648
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050151Z-Chitosan.md
  locator: 'YAML Record Review: Chitosan:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 865c3f27e54f14c8e2fc68818906bc7d0ca18cd0251d8049de213c7b68e8bca1
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Chitosan.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI chitosan identity, structure fields, 3/3 occurrence count, and carbon-source
    role pass, but a hydrolysis source statement is exported as an exact synonym.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Chitosan.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Chitosan.yaml`,
    `just validate-terms data/ingredients/mapped/Chitosan.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-49eb096564b1a02b
  kind: prior_review
  reference: reports/yaml_record_review/Chitosan.md
  locator: '`data/ingredients/mapped/Chitosan.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:39; Completeness:56; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 16553291c0fdfaa20a5ade24a3986d6f7ae00ff1dc7ef414cad7bba5b8ce8e1c
  quote: "Recommended Edits:\n- Major: either remove `hydrolysis: cationic chitosan`\
    \ from\n  `data/ingredients/mapped/Chitosan.yaml` or extend\n  `src/mediaingredientmech/synonym_policy.py`\
    \ so `hydrolysis:` source\n  statements stay in provenance without resolving as\
    \ ingredient synonyms.\n- Regenerate synchronized outputs and rerun strict validation,\
    \ SSSOM QC,\n  aggregate roundtrip, docs generation, and `git diff --check`."
- evidence_id: ev-daf4bae9f2fb1193
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[404]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2","finding_id":"SEM:dcd6713b97cc00ee9d67","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8f718e2eba80d902
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bd5b968443fd15bd
  evidence_ids:
  - ev-4c27023d56350852
  - ev-c08363128fe34811
  - ev-57677508f3efb153
  - ev-afc51c9707b15eac
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fc795cb88915f33c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bd5b968443fd15bd
  evidence_ids:
  - ev-467e6b2403ebb648
  - ev-49eb096564b1a02b
  - ev-4c27023d56350852
  - ev-daf4bae9f2fb1193
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:51Z;
    reviewed SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2;
    current SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050151Z-Chitosan.md","reports/yaml_record_review/Chitosan.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Chitosan.md` after the record changed from 65e848e860f525ec047bfb123e2852a74d62ac42a68ab2abf2f7b00e8264a0e9
    to e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-467e6b2403ebb648
    - ev-49eb096564b1a02b
    - ev-4c27023d56350852
  - name: legacy-native-ids
    value: '["SEM:dcd6713b97cc00ee9d67"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4c27023d56350852
    - ev-467e6b2403ebb648
    - ev-49eb096564b1a02b
    - ev-daf4bae9f2fb1193
findings:
- finding_id: rec-f-b5a14b417c9397b7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-bd5b968443fd15bd
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Chitosan'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:51Z;
    reviewed SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2;
    current SHA-256=e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050151Z-Chitosan.md","reports/yaml_record_review/Chitosan.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Chitosan.md` after the record changed from 65e848e860f525ec047bfb123e2852a74d62ac42a68ab2abf2f7b00e8264a0e9
    to e325ebfd852b192802b470797ab5052107a39a2f5a55a4cf3b1801427d1f1bd2; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bd5b968443fd15bd
  evidence_ids:
  - ev-467e6b2403ebb648
  - ev-49eb096564b1a02b
  - ev-4c27023d56350852
  - ev-daf4bae9f2fb1193
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Chitosan.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
