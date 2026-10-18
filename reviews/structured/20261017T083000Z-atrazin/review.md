# Per-record structured review: Atrazin (data/ingredients/mapped/Atrazin.yaml)

- Review: 20261017T083000Z-atrazin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Atrazin (data/ingredients/mapped/Atrazin.yaml, record-67b4f4f91e7cf018, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Atrazin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Atrazin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-67b4f4f91e7cf018 | data/ingredients/mapped/Atrazin.yaml | maintained | Atrazin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-67b4f4f91e7cf018 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-67b4f4f91e7cf018 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-67b4f4f91e7cf018 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-67b4f4f91e7cf018.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-67b4f4f91e7cf018.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:01:31Z; reviewed SHA-256=02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; current SHA-256=d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050131Z-Atrazin.md","reports/yaml_record_review/Atrazin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Atrazin.md&#96; after the record changed from 3c049fdb6761ed282d77035db21d57de5e1e2ff04fa405d5a09d5fe1009d6eed to 02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; preserved the previous blocker finding floor pending targeted retirement.

### Retired wrong mapping / stale tombstone ontology pointer

identity: supported. Targets: record-67b4f4f91e7cf018.

The narrow exported-mapping/pointer defect is already fixed: REJECTED tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a live merge target. This does not retire source-count, inert chemistry, role, or synonym questions.

## Findings

### rec-f-3d513346684a739e: Historical review coverage and residual narrative: Atrazin

blocker / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-67b4f4f91e7cf018.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:01:31Z; reviewed SHA-256=02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; current SHA-256=d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050131Z-Atrazin.md","reports/yaml_record_review/Atrazin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Atrazin.md&#96; after the record changed from 3c049fdb6761ed282d77035db21d57de5e1e2ff04fa405d5a09d5fe1009d6eed to 02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; preserved the previous blocker finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6653c2dc8279ffa3 | data/ingredients/mapped/Atrazin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[527],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15930","line":529,"mapping_status":"REJECTED","ontology_id":"CHEBI:15930","preferred_term":"Atrazin"}],"identifier":"CHEBI:15930","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"CHEBI:15930","ontology_label":"atrazine","ontology_source":"CHEBI"},"preferred_term":"Atrazin","sssom_rows":[],"sssom_subject":"MIM:Atrazin","synonym_count":0} |
| ev-9c085361f3dfbd0e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [527] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1ea5a98a2bab3f3b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Atrazin; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-60a4c27f7c084320 | docs/data/mapped_ingredients.csv; CSV lines=[529] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15930","line":529,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:15930","preferred_term":"Atrazin","total_occurrences":"0"}] |
| ev-8205aa1ec37d7bf2 | reports/yaml_record_review/20261001T050131Z-Atrazin.md; YAML Record Review: Atrazin:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-463b4a48e533b7cd | reports/yaml_record_review/Atrazin.md; &#96;data/ingredients/mapped/Atrazin.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:42; Completeness:60; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ee2c4fba604f54fd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[282] | context_only | [{"current_record_sha256":"d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b","finding_id":"SEM:f7b51d23ab90bda7153b","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-a55f2fad24029129 | data/ingredients/mapped/Atrazin.yaml; identifier; ontology_mapping.ontology_id; mapping_status; curation_history | supports | Current loser points to CHEBI:15930; old pointer cas:1924-24-9 survives only as historical/inert payload where retained. Live survivors=["data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml"]; explicit events=[{"action":"MERGED_INTO","changes":"Merged into CHEBI:15930 (2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine). Atrazin is the atrazine name variant. Correct CAS is 1912-24-9; imported 1924-24-9 was erroneous. Survivor already has the exact atrazine ontology identity. Original fields remain only on this excluded tombstone. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:15930","curator":"mim_semantic_review_20260921","llm_assisted":true,"llm_model":"gpt-6","new_status":"REJECTED","previous_status":"MAPPED","timestamp":"2026-09-21T21:33:25.379198+00:00"},{"action":"REPOINTED_TOMBSTONE_IDENTIFIER","changes":"identifier cas:1924-24-9 -&gt; CHEBI:15930 (#799). This record was merged into '2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine' but kept its own old identifier, so a downstream lookup on this label resolved to nothing live. The target is the one named in this record's own MERGED_INTO entry; the chain was followed to the first live record. A tombstone exists to keep the loser resolvable.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"},{"action":"REFRESHED_TOMBSTONE_ONTOLOGY_ID","changes":"ontology_id cas:1924-24-9 -&gt; CHEBI:15930 (#799). The merge set identifier and status but left ontology_mapping untouched, so this tombstone kept advertising a term it no longer asserts \u2014 anything indexing by ontology_id routed through it. Now agrees with the merge target '2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine'. Provenance is unaffected: what the record used to assert is in this history.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-atrazin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Atrazin (data/ingredients/mapped/Atrazin.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Atrazin (data/ingredients/mapped/Atrazin.yaml,
  record-67b4f4f91e7cf018, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Atrazin.yaml
    sha256: d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b
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
  - path: reports/yaml_record_review/20261001T050131Z-Atrazin.md
    sha256: 0b11a2482c6e22bb482a0f10c569e54eb767bd3e381db6ad25cc9bfe3d393cf7
    role: context
  - path: reports/yaml_record_review/Atrazin.md
    sha256: 32884e57ba9a036cd7079ffdf37c71dd1c31cf5ff25401756229b244265b14b0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-67b4f4f91e7cf018
  path: data/ingredients/mapped/Atrazin.yaml
  label: Atrazin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Atrazin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Atrazin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Atrazin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-67b4f4f91e7cf018
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-67b4f4f91e7cf018
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-67b4f4f91e7cf018
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-67b4f4f91e7cf018
evidence:
- evidence_id: ev-6653c2dc8279ffa3
  kind: record_content
  reference: data/ingredients/mapped/Atrazin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[527],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15930","line":529,"mapping_status":"REJECTED","ontology_id":"CHEBI:15930","preferred_term":"Atrazin"}],"identifier":"CHEBI:15930","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"CHEBI:15930","ontology_label":"atrazine","ontology_source":"CHEBI"},"preferred_term":"Atrazin","sssom_rows":[],"sssom_subject":"MIM:Atrazin","synonym_count":0}'
  snapshot_sha256: d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b
- evidence_id: ev-9c085361f3dfbd0e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [527]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1ea5a98a2bab3f3b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Atrazin; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-60a4c27f7c084320
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[529]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15930","line":529,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:15930","preferred_term":"Atrazin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8205aa1ec37d7bf2
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050131Z-Atrazin.md
  locator: 'YAML Record Review: Atrazin:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0b11a2482c6e22bb482a0f10c569e54eb767bd3e381db6ad25cc9bfe3d393cf7
  quote: 'Findings:

    - **blocker**: The previous finding set in `reports/yaml_record_review/Atrazin.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The record
    exact-maps Atrazin to non-resolving CAS 1924-24-9 despite an existing CHEBI atrazine
    record.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Atrazin.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Atrazin.yaml`,
    `just validate-terms data/ingredients/mapped/Atrazin.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-463b4a48e533b7cd
  kind: prior_review
  reference: reports/yaml_record_review/Atrazin.md
  locator: '`data/ingredients/mapped/Atrazin.yaml`:2; Verdict:4; Identity:12; Validation:26;
    Evidence:42; Completeness:60; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 32884e57ba9a036cd7079ffdf37c71dd1c31cf5ff25401756229b244265b14b0
  quote: "Recommended Edits:\n- Verify the upstream CultureBotHT entry for `Atrazin`;\
    \ if it intended\n  atrazine, retire or merge `data/ingredients/mapped/Atrazin.yaml`\
    \ into\n  `data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml`\n\
    \  and preserve `Atrazin` only as a reviewed alias of `CHEBI:15930`.\n- Remove\
    \ or correct `cas:1924-24-9` from the individual YAML, aggregate\n  collection,\
    \ and SSSOM row; regenerate the flat exports and rerun focused\n  strict validation,\
    \ product id/label correspondence, SSSOM invariants, and\n  flat-export coverage."
- evidence_id: ev-ee2c4fba604f54fd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[282]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b","finding_id":"SEM:f7b51d23ab90bda7153b","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a55f2fad24029129
  kind: record_content
  reference: data/ingredients/mapped/Atrazin.yaml
  locator: identifier; ontology_mapping.ontology_id; mapping_status; curation_history
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Current loser points to CHEBI:15930; old pointer cas:1924-24-9 survives
    only as historical/inert payload where retained. Live survivors=["data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml"];
    explicit events=[{"action":"MERGED_INTO","changes":"Merged into CHEBI:15930 (2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine).
    Atrazin is the atrazine name variant. Correct CAS is 1912-24-9; imported 1924-24-9
    was erroneous. Survivor already has the exact atrazine ontology identity. Original
    fields remain only on this excluded tombstone. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:15930","curator":"mim_semantic_review_20260921","llm_assisted":true,"llm_model":"gpt-6","new_status":"REJECTED","previous_status":"MAPPED","timestamp":"2026-09-21T21:33:25.379198+00:00"},{"action":"REPOINTED_TOMBSTONE_IDENTIFIER","changes":"identifier
    cas:1924-24-9 -> CHEBI:15930 (#799). This record was merged into ''2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine''
    but kept its own old identifier, so a downstream lookup on this label resolved
    to nothing live. The target is the one named in this record''s own MERGED_INTO
    entry; the chain was followed to the first live record. A tombstone exists to
    keep the loser resolvable.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"},{"action":"REFRESHED_TOMBSTONE_ONTOLOGY_ID","changes":"ontology_id
    cas:1924-24-9 -> CHEBI:15930 (#799). The merge set identifier and status but left
    ontology_mapping untouched, so this tombstone kept advertising a term it no longer
    asserts \u2014 anything indexing by ontology_id routed through it. Now agrees
    with the merge target ''2-chloro-4ethylamino-6-isopropylamino-1,3,5-triazine''.
    Provenance is unaffected: what the record used to assert is in this history.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"}]'
  snapshot_sha256: d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b
assessments:
- assessment_id: a-1f61b642eb9fbdf7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-67b4f4f91e7cf018
  evidence_ids:
  - ev-6653c2dc8279ffa3
  - ev-9c085361f3dfbd0e
  - ev-1ea5a98a2bab3f3b
  - ev-60a4c27f7c084320
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-724cf6dd06963046
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-67b4f4f91e7cf018
  evidence_ids:
  - ev-8205aa1ec37d7bf2
  - ev-463b4a48e533b7cd
  - ev-6653c2dc8279ffa3
  - ev-ee2c4fba604f54fd
  details: 'Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:01:31Z;
    reviewed SHA-256=02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2;
    current SHA-256=d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050131Z-Atrazin.md","reports/yaml_record_review/Atrazin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Atrazin.md` after the record changed from 3c049fdb6761ed282d77035db21d57de5e1e2ff04fa405d5a09d5fe1009d6eed
    to 02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; preserved
    the previous blocker finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8205aa1ec37d7bf2
    - ev-463b4a48e533b7cd
    - ev-6653c2dc8279ffa3
  - name: legacy-native-ids
    value: '["SEM:f7b51d23ab90bda7153b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6653c2dc8279ffa3
    - ev-8205aa1ec37d7bf2
    - ev-463b4a48e533b7cd
    - ev-ee2c4fba604f54fd
- assessment_id: a-541c6c709a47a663
  area: identity
  topic: Retired wrong mapping / stale tombstone ontology pointer
  outcome: supported
  summary: 'The narrow exported-mapping/pointer defect is already fixed: REJECTED
    tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a
    live merge target. This does not retire source-count, inert chemistry, role, or
    synonym questions.'
  target_ids:
  - record-67b4f4f91e7cf018
  evidence_ids:
  - ev-8205aa1ec37d7bf2
  - ev-463b4a48e533b7cd
  - ev-a55f2fad24029129
  - ev-6653c2dc8279ffa3
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8205aa1ec37d7bf2
    - ev-463b4a48e533b7cd
    - ev-a55f2fad24029129
    - ev-6653c2dc8279ffa3
findings:
- finding_id: rec-f-3d513346684a739e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-67b4f4f91e7cf018
  category: provenance
  severity: blocker
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Atrazin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:01:31Z;
    reviewed SHA-256=02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2;
    current SHA-256=d61bbfeda6dfd9326d9c39111ec579b8eaeabbe7e37c3ed2dd407e35fadca71b;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050131Z-Atrazin.md","reports/yaml_record_review/Atrazin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Atrazin.md` after the record changed from 3c049fdb6761ed282d77035db21d57de5e1e2ff04fa405d5a09d5fe1009d6eed
    to 02c2c72bf9ee60b2e83c99962397049678f1404f74a2fb8593592890d01a8cd2; preserved
    the previous blocker finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-67b4f4f91e7cf018
  evidence_ids:
  - ev-8205aa1ec37d7bf2
  - ev-463b4a48e533b7cd
  - ev-6653c2dc8279ffa3
  - ev-ee2c4fba604f54fd
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Atrazin.yaml
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
