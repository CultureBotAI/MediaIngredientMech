# Per-record structured review: Nano3 (data/ingredients/mapped/Nano3.yaml)

- Review: 20261017T083000Z-nano3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nano3 (data/ingredients/mapped/Nano3.yaml, record-a195a7daaa716895, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nano3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nano3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a195a7daaa716895 | data/ingredients/mapped/Nano3.yaml | maintained | Nano3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a195a7daaa716895 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a195a7daaa716895 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a195a7daaa716895 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a195a7daaa716895.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a195a7daaa716895.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:59Z; reviewed SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; current SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050259Z-Nano3.md","reports/yaml_record_review/Nano3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nano3.md&#96; after the record changed from efe9b51b3e6c91c8cf78f6623da8b71dd5731bdf2603cf9a6dbf24bb1a177c0b to 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-15ddd494172e9217: Historical review coverage and residual narrative: Nano3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a195a7daaa716895.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:59Z; reviewed SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; current SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050259Z-Nano3.md","reports/yaml_record_review/Nano3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nano3.md&#96; after the record changed from efe9b51b3e6c91c8cf78f6623da8b71dd5731bdf2603cf9a6dbf24bb1a177c0b to 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-00fa04ad30b67eab | data/ingredients/mapped/Nano3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1530],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63005","line":1532,"mapping_status":"MAPPED","ontology_id":"CHEBI:63005","preferred_term":"NaNO3"}],"identifier":"CHEBI:63005","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":674,"edge_count":674,"occurrences":675},"occurrence_statistics":{"media_count":674,"total_occurrences":675},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium nitrate","ontology_source":"CHEBI"},"preferred_term":"NaNO3","sssom_rows":[{"data_row":2041,"object_id":"CHEBI:63005","object_label":"sodium nitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nano3","synonym_count":21} |
| ev-ae188b575acab53d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1530] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e32a080b27e9915f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nano3; data-row positions=[2041] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2041,"object_id":"CHEBI:63005","object_label":"sodium nitrate","other":"CAS:7631-99-4&#124;Chile saltpeter&#124;Cubic niter&#124;Na NO3&#124;NaNO&#124;NaNO3(autoclave before adding)(Fisher BP360-500)&#124;NaNO3(CAS: 7631-99-4)&#124;NaNO3(Fisher BP360-500)&#124;Nitrate de sodium&#124;Nitrate of soda&#124;Nitric acid monosodium salt&#124;Nitric acid sodium salt (1:1)&#124;Nitric acid, sodium salt&#124;Sodium nitrate (nitrogen source)&#124;Sodium saltpeter&#124;sodium trioxidonitrate(1-)&#124;Sodium(I) nitrate (1:1)","predicate_id":"skos:exactMatch","subject_id":"MIM:Nano3","validation_method":"manual:semantic_identity_review&#124;IDENTITY_REVIEWED&#124;2026-09-21"}] |
| ev-30e6bbd1597b0e43 | docs/data/mapped_ingredients.csv; CSV lines=[1532] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63005","line":1532,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"674","ontology_id":"CHEBI:63005","preferred_term":"NaNO3","total_occurrences":"675"}] |
| ev-e21c119c74391b98 | reports/yaml_record_review/20261001T050259Z-Nano3.md; YAML Record Review: NaNO3:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b58626c8ab29cf5a | reports/yaml_record_review/Nano3.md; &#96;data/ingredients/mapped/Nano3.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:41; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-731fa4996239a268 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1032] | context_only | [{"current_record_sha256":"6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f","finding_id":"SEM:7041ae8b6f8fcc168efc","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nano3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nano3 (data/ingredients/mapped/Nano3.yaml)'
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
summary: Per-record structured review for Nano3 (data/ingredients/mapped/Nano3.yaml,
  record-a195a7daaa716895, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nano3.yaml
    sha256: 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
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
  - path: reports/yaml_record_review/20261001T050259Z-Nano3.md
    sha256: 0ba59b5deccd5137632265523a85192b3d99b14fb22db0fe73bf95e44592e10a
    role: context
  - path: reports/yaml_record_review/Nano3.md
    sha256: 626397b7ef2a087f2dca225315fcefcc174f4709f86b7a356346deb286e06854
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a195a7daaa716895
  path: data/ingredients/mapped/Nano3.yaml
  label: Nano3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nano3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nano3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nano3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a195a7daaa716895
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a195a7daaa716895
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a195a7daaa716895
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a195a7daaa716895
evidence:
- evidence_id: ev-00fa04ad30b67eab
  kind: record_content
  reference: data/ingredients/mapped/Nano3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1530],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63005","line":1532,"mapping_status":"MAPPED","ontology_id":"CHEBI:63005","preferred_term":"NaNO3"}],"identifier":"CHEBI:63005","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":674,"edge_count":674,"occurrences":675},"occurrence_statistics":{"media_count":674,"total_occurrences":675},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium
    nitrate","ontology_source":"CHEBI"},"preferred_term":"NaNO3","sssom_rows":[{"data_row":2041,"object_id":"CHEBI:63005","object_label":"sodium
    nitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nano3","synonym_count":21}'
  snapshot_sha256: 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f
- evidence_id: ev-ae188b575acab53d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1530]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e32a080b27e9915f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nano3; data-row positions=[2041]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2041,"object_id":"CHEBI:63005","object_label":"sodium
    nitrate","other":"CAS:7631-99-4|Chile saltpeter|Cubic niter|Na NO3|NaNO|NaNO3(autoclave
    before adding)(Fisher BP360-500)|NaNO3(CAS: 7631-99-4)|NaNO3(Fisher BP360-500)|Nitrate
    de sodium|Nitrate of soda|Nitric acid monosodium salt|Nitric acid sodium salt
    (1:1)|Nitric acid, sodium salt|Sodium nitrate (nitrogen source)|Sodium saltpeter|sodium
    trioxidonitrate(1-)|Sodium(I) nitrate (1:1)","predicate_id":"skos:exactMatch","subject_id":"MIM:Nano3","validation_method":"manual:semantic_identity_review|IDENTITY_REVIEWED|2026-09-21"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-30e6bbd1597b0e43
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1532]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63005","line":1532,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"674","ontology_id":"CHEBI:63005","preferred_term":"NaNO3","total_occurrences":"675"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e21c119c74391b98
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050259Z-Nano3.md
  locator: 'YAML Record Review: NaNO3:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61;
    Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0ba59b5deccd5137632265523a85192b3d99b14fb22db0fe73bf95e44592e10a
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Nano3.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:63005 sodium nitrate identity passes, but final other has a role-qualified
    synonym.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Nano3.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Nano3.yaml`,
    `just validate-terms data/ingredients/mapped/Nano3.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-b58626c8ab29cf5a
  kind: prior_review
  reference: reports/yaml_record_review/Nano3.md
  locator: '`data/ingredients/mapped/Nano3.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:27; Completeness:41; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 626397b7ef2a087f2dca225315fcefcc174f4709f86b7a356346deb286e06854
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nano3.yaml`, reject\
    \ or delete\n  `Sodium nitrate (nitrogen source)`, then rebuild final SSSOM so\
    \ `other`\n  keeps only true sodium nitrate synonyms plus `CAS:7631-99-4`."
- evidence_id: ev-731fa4996239a268
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1032]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f","finding_id":"SEM:7041ae8b6f8fcc168efc","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bf36dbb24b712d79
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a195a7daaa716895
  evidence_ids:
  - ev-00fa04ad30b67eab
  - ev-ae188b575acab53d
  - ev-e32a080b27e9915f
  - ev-30e6bbd1597b0e43
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-45bed50a15fe7719
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a195a7daaa716895
  evidence_ids:
  - ev-e21c119c74391b98
  - ev-b58626c8ab29cf5a
  - ev-00fa04ad30b67eab
  - ev-731fa4996239a268
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:59Z;
    reviewed SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f;
    current SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050259Z-Nano3.md","reports/yaml_record_review/Nano3.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nano3.md` after the record changed from efe9b51b3e6c91c8cf78f6623da8b71dd5731bdf2603cf9a6dbf24bb1a177c0b
    to 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e21c119c74391b98
    - ev-b58626c8ab29cf5a
    - ev-00fa04ad30b67eab
  - name: legacy-native-ids
    value: '["SEM:7041ae8b6f8fcc168efc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-00fa04ad30b67eab
    - ev-e21c119c74391b98
    - ev-b58626c8ab29cf5a
    - ev-731fa4996239a268
findings:
- finding_id: rec-f-15ddd494172e9217
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a195a7daaa716895
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nano3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:59Z;
    reviewed SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f;
    current SHA-256=6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050259Z-Nano3.md","reports/yaml_record_review/Nano3.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nano3.md` after the record changed from efe9b51b3e6c91c8cf78f6623da8b71dd5731bdf2603cf9a6dbf24bb1a177c0b
    to 6ac10a54805425447c42dc2ff47eb014dd00d71ac84a3701437f070c09ad2d0f; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a195a7daaa716895
  evidence_ids:
  - ev-e21c119c74391b98
  - ev-b58626c8ab29cf5a
  - ev-00fa04ad30b67eab
  - ev-731fa4996239a268
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nano3.yaml
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
  with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.
```
