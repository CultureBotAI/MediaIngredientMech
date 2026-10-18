# Per-record structured review: Nano (data/ingredients/mapped/Nano.yaml)

- Review: 20261017T083000Z-nano
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nano (data/ingredients/mapped/Nano.yaml, record-a3513ba2c7afb1a7, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nano.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nano.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a3513ba2c7afb1a7 | data/ingredients/mapped/Nano.yaml | maintained | Nano |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a3513ba2c7afb1a7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a3513ba2c7afb1a7 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a3513ba2c7afb1a7 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a3513ba2c7afb1a7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a3513ba2c7afb1a7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:58Z; reviewed SHA-256=1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; current SHA-256=4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050258Z-Nano.md","reports/yaml_record_review/Nano.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nano.md&#96; after the record changed from 3a61b91e11ba7e6fd28eee09dceb979b0c991486d871208c7e29bb6b25a56972 to 1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; preserved the previous blocker finding floor pending targeted retirement.

### Retired wrong mapping / stale tombstone ontology pointer

identity: supported. Targets: record-a3513ba2c7afb1a7.

The narrow exported-mapping/pointer defect is already fixed: REJECTED tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a live merge target. This does not retire source-count, inert chemistry, role, or synonym questions.

## Findings

### rec-f-acab2e0138dba1c4: Historical review coverage and residual narrative: Nano

blocker / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a3513ba2c7afb1a7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:58Z; reviewed SHA-256=1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; current SHA-256=4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050258Z-Nano.md","reports/yaml_record_review/Nano.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nano.md&#96; after the record changed from 3a61b91e11ba7e6fd28eee09dceb979b0c991486d871208c7e29bb6b25a56972 to 1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; preserved the previous blocker finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0397c9698a371d0e | data/ingredients/mapped/Nano.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1528],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63005","line":1530,"mapping_status":"REJECTED","ontology_id":"CHEBI:63005","preferred_term":"NaNO"}],"identifier":"CHEBI:63005","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":674,"edge_count":674,"occurrences":675},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium nitrate","ontology_source":"CHEBI"},"preferred_term":"NaNO","sssom_rows":[],"sssom_subject":"MIM:Nano","synonym_count":3} |
| ev-578824bd7f0aefc8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1528] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ca377d51d8c56609 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nano; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-ba31445c10bbc35f | docs/data/mapped_ingredients.csv; CSV lines=[1530] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63005","line":1530,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:63005","preferred_term":"NaNO","total_occurrences":"0"}] |
| ev-626e8164a1842e65 | reports/yaml_record_review/20261001T050258Z-Nano.md; YAML Record Review: NaNO:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1df3a1ed69398e05 | reports/yaml_record_review/Nano.md; &#96;data/ingredients/mapped/Nano.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:40; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b16b07b0286f75fd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1031] | context_only | [{"current_record_sha256":"4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631","finding_id":"SEM:1fb7eb2be19cbc32d5ee","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-0c22dbffe6523338 | data/ingredients/mapped/Nano.yaml; identifier; ontology_mapping.ontology_id; mapping_status; curation_history | supports | Current loser points to CHEBI:63005; old pointer NCIT:C54713 survives only as historical/inert payload where retained. Live survivors=["data/ingredients/mapped/Nano3.yaml"]; explicit events=[{"action":"MERGED_INTO","changes":"Merged into CHEBI:63005 (NaNO3). The source synonyms explicitly identify NaNO3, CAS 7631-99-4 and Fisher BP360-500; NCIT:C54713 denotes the nano unit prefix. NaNO retained solely as the documented truncated source label. Original fields remain only on this excluded tombstone. Evidence: https://www.ebi.ac.uk/chebi/CHEBI:63005","curator":"mim_semantic_review_20260921","llm_assisted":true,"llm_model":"gpt-6","new_status":"REJECTED","previous_status":"MAPPED","timestamp":"2026-09-21T21:33:25.379198+00:00"},{"action":"REPOINTED_TOMBSTONE_IDENTIFIER","changes":"identifier NCIT:C54713 -&gt; CHEBI:63005 (#799). This record was merged into 'NaNO3' but kept its own old identifier, so a downstream lookup on this label resolved to nothing live. The target is the one named in this record's own MERGED_INTO entry; the chain was followed to the first live record. A tombstone exists to keep the loser resolvable.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"},{"action":"REFRESHED_TOMBSTONE_ONTOLOGY_ID","changes":"ontology_id NCIT:C54713 -&gt; CHEBI:63005 (#799). The merge set identifier and status but left ontology_mapping untouched, so this tombstone kept advertising a term it no longer asserts \u2014 anything indexing by ontology_id routed through it. Now agrees with the merge target 'NaNO3'. Provenance is unaffected: what the record used to assert is in this history.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nano
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nano (data/ingredients/mapped/Nano.yaml)'
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
summary: Per-record structured review for Nano (data/ingredients/mapped/Nano.yaml,
  record-a3513ba2c7afb1a7, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nano.yaml
    sha256: 4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631
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
  - path: reports/yaml_record_review/20261001T050258Z-Nano.md
    sha256: 5921f0b234a9f914297195ecad13354ff866111be2458d74f448fd8b8ccff2bd
    role: context
  - path: reports/yaml_record_review/Nano.md
    sha256: 75ce90f7f377ac0b4791090f61008db9e7e6df4cd7e6ab5a31d5d3d094fea9d5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a3513ba2c7afb1a7
  path: data/ingredients/mapped/Nano.yaml
  label: Nano
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nano.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nano.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Nano.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a3513ba2c7afb1a7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a3513ba2c7afb1a7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a3513ba2c7afb1a7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a3513ba2c7afb1a7
evidence:
- evidence_id: ev-0397c9698a371d0e
  kind: record_content
  reference: data/ingredients/mapped/Nano.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1528],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63005","line":1530,"mapping_status":"REJECTED","ontology_id":"CHEBI:63005","preferred_term":"NaNO"}],"identifier":"CHEBI:63005","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":674,"edge_count":674,"occurrences":675},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium
    nitrate","ontology_source":"CHEBI"},"preferred_term":"NaNO","sssom_rows":[],"sssom_subject":"MIM:Nano","synonym_count":3}'
  snapshot_sha256: 4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631
- evidence_id: ev-578824bd7f0aefc8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1528]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ca377d51d8c56609
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nano; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ba31445c10bbc35f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1530]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63005","line":1530,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:63005","preferred_term":"NaNO","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-626e8164a1842e65
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050258Z-Nano.md
  locator: 'YAML Record Review: NaNO:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61;
    Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5921f0b234a9f914297195ecad13354ff866111be2458d74f448fd8b8ccff2bd
  quote: 'Findings:

    - **blocker**: The previous finding set in `reports/yaml_record_review/Nano.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: Sodium nitrate
    source labels are exact-mapped to NCIT:C54713 Nano, the NCIT one-billionth prefix.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Nano.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Nano.yaml`,
    `just validate-terms data/ingredients/mapped/Nano.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-1df3a1ed69398e05
  kind: prior_review
  reference: reports/yaml_record_review/Nano.md
  locator: '`data/ingredients/mapped/Nano.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:27; Completeness:40; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 75ce90f7f377ac0b4791090f61008db9e7e6df4cd7e6ab5a31d5d3d094fea9d5
  quote: "Recommended Edits:\n- Blocker: merge the eight `NaNO3` occurrences and any\
    \ useful provenance from\n  `data/ingredients/mapped/Nano.yaml` into\n  `data/ingredients/mapped/Nano3.yaml`,\
    \ then retire this erroneous\n  `NCIT:C54713` exact mapping so final SSSOM no\
    \ longer maps sodium nitrate\n  forms to the NCIT nano-prefix term."
- evidence_id: ev-b16b07b0286f75fd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1031]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631","finding_id":"SEM:1fb7eb2be19cbc32d5ee","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0c22dbffe6523338
  kind: record_content
  reference: data/ingredients/mapped/Nano.yaml
  locator: identifier; ontology_mapping.ontology_id; mapping_status; curation_history
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Current loser points to CHEBI:63005; old pointer NCIT:C54713 survives
    only as historical/inert payload where retained. Live survivors=["data/ingredients/mapped/Nano3.yaml"];
    explicit events=[{"action":"MERGED_INTO","changes":"Merged into CHEBI:63005 (NaNO3).
    The source synonyms explicitly identify NaNO3, CAS 7631-99-4 and Fisher BP360-500;
    NCIT:C54713 denotes the nano unit prefix. NaNO retained solely as the documented
    truncated source label. Original fields remain only on this excluded tombstone.
    Evidence: https://www.ebi.ac.uk/chebi/CHEBI:63005","curator":"mim_semantic_review_20260921","llm_assisted":true,"llm_model":"gpt-6","new_status":"REJECTED","previous_status":"MAPPED","timestamp":"2026-09-21T21:33:25.379198+00:00"},{"action":"REPOINTED_TOMBSTONE_IDENTIFIER","changes":"identifier
    NCIT:C54713 -> CHEBI:63005 (#799). This record was merged into ''NaNO3'' but kept
    its own old identifier, so a downstream lookup on this label resolved to nothing
    live. The target is the one named in this record''s own MERGED_INTO entry; the
    chain was followed to the first live record. A tombstone exists to keep the loser
    resolvable.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"},{"action":"REFRESHED_TOMBSTONE_ONTOLOGY_ID","changes":"ontology_id
    NCIT:C54713 -> CHEBI:63005 (#799). The merge set identifier and status but left
    ontology_mapping untouched, so this tombstone kept advertising a term it no longer
    asserts \u2014 anything indexing by ontology_id routed through it. Now agrees
    with the merge target ''NaNO3''. Provenance is unaffected: what the record used
    to assert is in this history.","curator":"fix_tombstone_pointers","llm_assisted":false,"timestamp":"2026-10-05T04:09:33.941715+00:00"}]'
  snapshot_sha256: 4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631
assessments:
- assessment_id: a-6eaf7ac6a6eb337b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a3513ba2c7afb1a7
  evidence_ids:
  - ev-0397c9698a371d0e
  - ev-578824bd7f0aefc8
  - ev-ca377d51d8c56609
  - ev-ba31445c10bbc35f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-63dd5639f9577ee5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a3513ba2c7afb1a7
  evidence_ids:
  - ev-626e8164a1842e65
  - ev-1df3a1ed69398e05
  - ev-0397c9698a371d0e
  - ev-b16b07b0286f75fd
  details: 'Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:58Z;
    reviewed SHA-256=1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef;
    current SHA-256=4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050258Z-Nano.md","reports/yaml_record_review/Nano.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nano.md` after the record changed from 3a61b91e11ba7e6fd28eee09dceb979b0c991486d871208c7e29bb6b25a56972
    to 1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; preserved
    the previous blocker finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-626e8164a1842e65
    - ev-1df3a1ed69398e05
    - ev-0397c9698a371d0e
  - name: legacy-native-ids
    value: '["SEM:1fb7eb2be19cbc32d5ee"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0397c9698a371d0e
    - ev-626e8164a1842e65
    - ev-1df3a1ed69398e05
    - ev-b16b07b0286f75fd
- assessment_id: a-69d5d721fb07fcef
  area: identity
  topic: Retired wrong mapping / stale tombstone ontology pointer
  outcome: supported
  summary: 'The narrow exported-mapping/pointer defect is already fixed: REJECTED
    tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a
    live merge target. This does not retire source-count, inert chemistry, role, or
    synonym questions.'
  target_ids:
  - record-a3513ba2c7afb1a7
  evidence_ids:
  - ev-626e8164a1842e65
  - ev-1df3a1ed69398e05
  - ev-0c22dbffe6523338
  - ev-0397c9698a371d0e
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-626e8164a1842e65
    - ev-1df3a1ed69398e05
    - ev-0c22dbffe6523338
    - ev-0397c9698a371d0e
findings:
- finding_id: rec-f-acab2e0138dba1c4
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a3513ba2c7afb1a7
  category: provenance
  severity: blocker
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nano'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:58Z;
    reviewed SHA-256=1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef;
    current SHA-256=4dd4a5ae67fec187d44f23d68fafffe2e533a1d4d85c481b6dd55fa8dfa29631;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050258Z-Nano.md","reports/yaml_record_review/Nano.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nano.md` after the record changed from 3a61b91e11ba7e6fd28eee09dceb979b0c991486d871208c7e29bb6b25a56972
    to 1158fe527bfd42ccb90a580f2c33e015550ff5e6d33bf57e96d778e04a7223ef; preserved
    the previous blocker finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a3513ba2c7afb1a7
  evidence_ids:
  - ev-626e8164a1842e65
  - ev-1df3a1ed69398e05
  - ev-0397c9698a371d0e
  - ev-b16b07b0286f75fd
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nano.yaml
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
