# Per-record structured review: Catalase (data/ingredients/mapped/Catalase.yaml)

- Review: 20261017T083000Z-catalase
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Catalase (data/ingredients/mapped/Catalase.yaml, record-c1be0e1fe71a2a9b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Catalase.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Catalase.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c1be0e1fe71a2a9b | data/ingredients/mapped/Catalase.yaml | maintained | Catalase |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c1be0e1fe71a2a9b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c1be0e1fe71a2a9b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c1be0e1fe71a2a9b | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c1be0e1fe71a2a9b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c1be0e1fe71a2a9b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:01:46Z; reviewed SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; current SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050146Z-Catalase.md","reports/yaml_record_review/Catalase.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Catalase.md&#96; after the record changed from eddaf0e7818aee7212b45b508f533c48f18c87285003d01bfc135daf64b1cc02 to acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; preserved the previous minor finding floor pending targeted retirement.

## Findings

### rec-f-dd6a2c7971c8f0ea: Historical review coverage and residual narrative: Catalase

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c1be0e1fe71a2a9b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:01:46Z; reviewed SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; current SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050146Z-Catalase.md","reports/yaml_record_review/Catalase.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Catalase.md&#96; after the record changed from eddaf0e7818aee7212b45b508f533c48f18c87285003d01bfc135daf64b1cc02 to acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; preserved the previous minor finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-46626682f6ef9d6e | data/ingredients/mapped/Catalase.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2651],"raw_equal":true},"docs_rows":[{"identifier":"cas:9001-05-2","line":2653,"mapping_status":"MAPPED","ontology_id":"mesh:D002374","preferred_term":"Catalase"}],"identifier":"cas:9001-05-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":34,"edge_count":34,"occurrences":34},"occurrence_statistics":{"media_count":34,"total_occurrences":34},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:D002374","ontology_label":"Catalase","ontology_source":"MESH"},"preferred_term":"Catalase","sssom_rows":[{"data_row":668,"object_id":"mesh:D002374","object_label":"Catalase","predicate_id":"skos:broadMatch"},{"data_row":2976,"object_id":"cas:9001-05-2","object_label":"Catalase","predicate_id":"skos:exactMatch"},{"data_row":2977,"object_id":"kgmicrobe.ingredient:catalase","object_label":"Catalase","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Catalase","synonym_count":3} |
| ev-e4c69a031b5ee0ca | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2651] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a943a65f6677facd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Catalase; data-row positions=[668,2976,2977] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":668,"object_id":"mesh:D002374","object_label":"Catalase","other":"Catalase (Sigma C--10)","predicate_id":"skos:broadMatch","subject_id":"MIM:Catalase","validation_method":"manual:reconcile_sssom&#124;REMAPPED&#124;2026-09-22"},{"data_row":2976,"object_id":"cas:9001-05-2","object_label":"Catalase","other":"CAS:9001-05-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Catalase","validation_method":"manual:apply_312_batch2&#124;IDENTITY&#124;2026-09-22"},{"data_row":2977,"object_id":"kgmicrobe.ingredient:catalase","object_label":"Catalase","other":"CAS:9001-05-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Catalase","validation_method":"manual:apply_312_batch2&#124;REGISTRY&#124;2026-09-22"}] |
| ev-0c614866ec17c836 | docs/data/mapped_ingredients.csv; CSV lines=[2653] | supports | Published identity and count rows inspected: [{"identifier":"cas:9001-05-2","line":2653,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"34","ontology_id":"mesh:D002374","preferred_term":"Catalase","total_occurrences":"34"}] |
| ev-67fbf45043290591 | reports/yaml_record_review/20261001T050146Z-Catalase.md; YAML Record Review: Catalase:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d9a668fac9d0f009 | reports/yaml_record_review/Catalase.md; &#96;data/ingredients/mapped/Catalase.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:41; Completeness:53; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-66b34c9c361287f7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[374] | context_only | [{"current_record_sha256":"acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd","finding_id":"SEM:582b7c291a19a2b5369c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-catalase
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Catalase (data/ingredients/mapped/Catalase.yaml)'
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
summary: Per-record structured review for Catalase (data/ingredients/mapped/Catalase.yaml,
  record-c1be0e1fe71a2a9b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Catalase.yaml
    sha256: acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd
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
  - path: reports/yaml_record_review/20261001T050146Z-Catalase.md
    sha256: 1893ffc4261e566eae09428af9a8b51594b43800219d19304d2f410c04cd65ca
    role: context
  - path: reports/yaml_record_review/Catalase.md
    sha256: a1756b02e5ddc70b95260927e8c50bf9666790cea06e3d39ee9fb2314474a40f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c1be0e1fe71a2a9b
  path: data/ingredients/mapped/Catalase.yaml
  label: Catalase
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Catalase.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Catalase.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Catalase.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c1be0e1fe71a2a9b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c1be0e1fe71a2a9b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c1be0e1fe71a2a9b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c1be0e1fe71a2a9b
evidence:
- evidence_id: ev-46626682f6ef9d6e
  kind: record_content
  reference: data/ingredients/mapped/Catalase.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2651],"raw_equal":true},"docs_rows":[{"identifier":"cas:9001-05-2","line":2653,"mapping_status":"MAPPED","ontology_id":"mesh:D002374","preferred_term":"Catalase"}],"identifier":"cas:9001-05-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":34,"edge_count":34,"occurrences":34},"occurrence_statistics":{"media_count":34,"total_occurrences":34},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:D002374","ontology_label":"Catalase","ontology_source":"MESH"},"preferred_term":"Catalase","sssom_rows":[{"data_row":668,"object_id":"mesh:D002374","object_label":"Catalase","predicate_id":"skos:broadMatch"},{"data_row":2976,"object_id":"cas:9001-05-2","object_label":"Catalase","predicate_id":"skos:exactMatch"},{"data_row":2977,"object_id":"kgmicrobe.ingredient:catalase","object_label":"Catalase","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Catalase","synonym_count":3}'
  snapshot_sha256: acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd
- evidence_id: ev-e4c69a031b5ee0ca
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2651]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a943a65f6677facd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Catalase; data-row positions=[668,2976,2977]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":668,"object_id":"mesh:D002374","object_label":"Catalase","other":"Catalase
    (Sigma C--10)","predicate_id":"skos:broadMatch","subject_id":"MIM:Catalase","validation_method":"manual:reconcile_sssom|REMAPPED|2026-09-22"},{"data_row":2976,"object_id":"cas:9001-05-2","object_label":"Catalase","other":"CAS:9001-05-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Catalase","validation_method":"manual:apply_312_batch2|IDENTITY|2026-09-22"},{"data_row":2977,"object_id":"kgmicrobe.ingredient:catalase","object_label":"Catalase","other":"CAS:9001-05-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Catalase","validation_method":"manual:apply_312_batch2|REGISTRY|2026-09-22"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0c614866ec17c836
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2653]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:9001-05-2","line":2653,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"34","ontology_id":"mesh:D002374","preferred_term":"Catalase","total_occurrences":"34"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-67fbf45043290591
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050146Z-Catalase.md
  locator: 'YAML Record Review: Catalase:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1893ffc4261e566eae09428af9a8b51594b43800219d19304d2f410c04cd65ca
  quote: 'Findings:

    - **minor**: The previous finding set in `reports/yaml_record_review/Catalase.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    active NCIT catalase identity passes, but the SSSOM validation_method still reports
    the pre-migration UNKNOWN_TERM state.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Catalase.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Catalase.yaml`,
    `just validate-terms data/ingredients/mapped/Catalase.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-d9a668fac9d0f009
  kind: prior_review
  reference: reports/yaml_record_review/Catalase.md
  locator: '`data/ingredients/mapped/Catalase.yaml`:2; Verdict:4; Identity:11; Validation:26;
    Evidence:41; Completeness:53; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a1756b02e5ddc70b95260927e8c50bf9666790cea06e3d39ee9fb2314474a40f
  quote: "Recommended Edits:\n- Minor: refresh the synonym/unknown-term review metadata\
    \ for the\n  `MIM:Catalase` SSSOM row so `validation_method` no longer reports\
    \ the\n  pre-migration `UNKNOWN_TERM` state."
- evidence_id: ev-66b34c9c361287f7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[374]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd","finding_id":"SEM:582b7c291a19a2b5369c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b0ac7068160e33f1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c1be0e1fe71a2a9b
  evidence_ids:
  - ev-46626682f6ef9d6e
  - ev-e4c69a031b5ee0ca
  - ev-a943a65f6677facd
  - ev-0c614866ec17c836
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7bd9fecd8fe8285f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c1be0e1fe71a2a9b
  evidence_ids:
  - ev-67fbf45043290591
  - ev-d9a668fac9d0f009
  - ev-46626682f6ef9d6e
  - ev-66b34c9c361287f7
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:01:46Z;
    reviewed SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd;
    current SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050146Z-Catalase.md","reports/yaml_record_review/Catalase.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Catalase.md` after the record changed from eddaf0e7818aee7212b45b508f533c48f18c87285003d01bfc135daf64b1cc02
    to acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; preserved
    the previous minor finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-67fbf45043290591
    - ev-d9a668fac9d0f009
    - ev-46626682f6ef9d6e
  - name: legacy-native-ids
    value: '["SEM:582b7c291a19a2b5369c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-46626682f6ef9d6e
    - ev-67fbf45043290591
    - ev-d9a668fac9d0f009
    - ev-66b34c9c361287f7
findings:
- finding_id: rec-f-dd6a2c7971c8f0ea
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c1be0e1fe71a2a9b
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Catalase'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:01:46Z;
    reviewed SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd;
    current SHA-256=acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050146Z-Catalase.md","reports/yaml_record_review/Catalase.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Catalase.md` after the record changed from eddaf0e7818aee7212b45b508f533c48f18c87285003d01bfc135daf64b1cc02
    to acf35ca83d195941071bd756beaea8560d59b0ab5e9cc5761d36889969590efd; preserved
    the previous minor finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c1be0e1fe71a2a9b
  evidence_ids:
  - ev-67fbf45043290591
  - ev-d9a668fac9d0f009
  - ev-46626682f6ef9d6e
  - ev-66b34c9c361287f7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Catalase.yaml
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
