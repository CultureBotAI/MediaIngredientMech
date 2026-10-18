# Per-record structured review: Hydrogen_gas (data/ingredients/mapped/Hydrogen_gas.yaml)

- Review: 20261017T083000Z-hydrogen-gas
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hydrogen_gas (data/ingredients/mapped/Hydrogen_gas.yaml, record-9c32238bdffe4863, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hydrogen_gas.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hydrogen_gas.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9c32238bdffe4863 | data/ingredients/mapped/Hydrogen_gas.yaml | maintained | Hydrogen_gas |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9c32238bdffe4863 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9c32238bdffe4863 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9c32238bdffe4863 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9c32238bdffe4863.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9c32238bdffe4863.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:28Z; reviewed SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; current SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md","reports/yaml_record_review/Hydrogen_gas.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Hydrogen_gas.md&#96; after the record changed from 2152fc1281bf7cbe5b0ab09a4703e87e24c4e417eca704fb1e6d3c5a150d1ad8 to 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-cbd1d763580b3cf2: Historical review coverage and residual narrative: Hydrogen_gas

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9c32238bdffe4863.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:28Z; reviewed SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; current SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md","reports/yaml_record_review/Hydrogen_gas.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Hydrogen_gas.md&#96; after the record changed from 2152fc1281bf7cbe5b0ab09a4703e87e24c4e417eca704fb1e6d3c5a150d1ad8 to 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2a905a5f460f34e6 | data/ingredients/mapped/Hydrogen_gas.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1143],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18276","line":1145,"mapping_status":"MAPPED","ontology_id":"CHEBI:18276","preferred_term":"Hydrogen gas"}],"identifier":"CHEBI:18276","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":243,"edge_count":243,"occurrences":243},"occurrence_statistics":{"media_count":243,"total_occurrences":243},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18276","ontology_label":"dihydrogen","ontology_source":"CHEBI"},"preferred_term":"Hydrogen gas","sssom_rows":[{"data_row":1452,"object_id":"CHEBI:18276","object_label":"dihydrogen","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydrogen_gas","synonym_count":13} |
| ev-faee66d20e3dd84f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1143] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-105d53b9deeefb56 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hydrogen_gas; data-row positions=[1452] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1452,"object_id":"CHEBI:18276","object_label":"dihydrogen","other":"H2&#124;Hydrogen&#124;Hydrogen (gas)&#124;E 949&#124;E-949&#124;E949&#124;H(2)&#124;H2_CO2&#124;H2_methanol&#124;molecular hydrogen&#124;Diydrogen","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydrogen_gas","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-297bc41ba17d5ee6 | docs/data/mapped_ingredients.csv; CSV lines=[1145] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18276","line":1145,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"243","ontology_id":"CHEBI:18276","preferred_term":"Hydrogen gas","total_occurrences":"243"}] |
| ev-9fe8c7d1b3c33e83 | reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md; YAML Record Review: Hydrogen gas:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d033696005bbbd99 | reports/yaml_record_review/Hydrogen_gas.md; &#96;data/ingredients/mapped/Hydrogen_gas.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:33; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dbd73af9e8489a2c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[739] | context_only | [{"current_record_sha256":"16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f","finding_id":"SEM:f81aeb7bfb948dfde38c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hydrogen-gas
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hydrogen_gas (data/ingredients/mapped/Hydrogen_gas.yaml)'
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
summary: Per-record structured review for Hydrogen_gas (data/ingredients/mapped/Hydrogen_gas.yaml,
  record-9c32238bdffe4863, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hydrogen_gas.yaml
    sha256: 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f
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
  - path: reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md
    sha256: f14b2a4ae2be8f41e19bd80d9ec22d89555b6a2e55a92f61a77142040ab37940
    role: context
  - path: reports/yaml_record_review/Hydrogen_gas.md
    sha256: ce9304c4044d24950ad00340ccafc069299a156d155e3bb8ceef5e1976e2a1b1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9c32238bdffe4863
  path: data/ingredients/mapped/Hydrogen_gas.yaml
  label: Hydrogen_gas
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydrogen_gas.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hydrogen_gas.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hydrogen_gas.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9c32238bdffe4863
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9c32238bdffe4863
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9c32238bdffe4863
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9c32238bdffe4863
evidence:
- evidence_id: ev-2a905a5f460f34e6
  kind: record_content
  reference: data/ingredients/mapped/Hydrogen_gas.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1143],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18276","line":1145,"mapping_status":"MAPPED","ontology_id":"CHEBI:18276","preferred_term":"Hydrogen
    gas"}],"identifier":"CHEBI:18276","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":243,"edge_count":243,"occurrences":243},"occurrence_statistics":{"media_count":243,"total_occurrences":243},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18276","ontology_label":"dihydrogen","ontology_source":"CHEBI"},"preferred_term":"Hydrogen
    gas","sssom_rows":[{"data_row":1452,"object_id":"CHEBI:18276","object_label":"dihydrogen","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydrogen_gas","synonym_count":13}'
  snapshot_sha256: 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f
- evidence_id: ev-faee66d20e3dd84f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1143]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-105d53b9deeefb56
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hydrogen_gas; data-row positions=[1452]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1452,"object_id":"CHEBI:18276","object_label":"dihydrogen","other":"H2|Hydrogen|Hydrogen
    (gas)|E 949|E-949|E949|H(2)|H2_CO2|H2_methanol|molecular hydrogen|Diydrogen","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydrogen_gas","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-297bc41ba17d5ee6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1145]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18276","line":1145,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"243","ontology_id":"CHEBI:18276","preferred_term":"Hydrogen
    gas","total_occurrences":"243"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9fe8c7d1b3c33e83
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md
  locator: 'YAML Record Review: Hydrogen gas:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f14b2a4ae2be8f41e19bd80d9ec22d89555b6a2e55a92f61a77142040ab37940
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Hydrogen_gas.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    dihydrogen identity passes, but mixture labels, a typo, and process-qualified
    text are exported as SSSOM synonyms.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Hydrogen_gas.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Hydrogen_gas.yaml`,
    `just validate-terms data/ingredients/mapped/Hydrogen_gas.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-d033696005bbbd99
  kind: prior_review
  reference: reports/yaml_record_review/Hydrogen_gas.md
  locator: '`data/ingredients/mapped/Hydrogen_gas.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:33; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ce9304c4044d24950ad00340ccafc069299a156d155e3bb8ceef5e1976e2a1b1
  quote: "Recommended Edits:\n- Major: remove `H2_CO2`, `H2_methanol`, `Diydrogen`,\
    \ and\n  `aerobic catabolization: dihydrogen` from active exported synonyms or\
    \ keep\n  them only as non-exported provenance, regenerate the SSSOM, and rerun\
    \ strict,\n  term, round-trip, id-label, component, and SSSOM validation."
- evidence_id: ev-dbd73af9e8489a2c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[739]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f","finding_id":"SEM:f81aeb7bfb948dfde38c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cfc58a4488b7af8c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9c32238bdffe4863
  evidence_ids:
  - ev-2a905a5f460f34e6
  - ev-faee66d20e3dd84f
  - ev-105d53b9deeefb56
  - ev-297bc41ba17d5ee6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c45ebb74ed63b758
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9c32238bdffe4863
  evidence_ids:
  - ev-9fe8c7d1b3c33e83
  - ev-d033696005bbbd99
  - ev-2a905a5f460f34e6
  - ev-dbd73af9e8489a2c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:28Z;
    reviewed SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f;
    current SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md","reports/yaml_record_review/Hydrogen_gas.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Hydrogen_gas.md` after the record changed from 2152fc1281bf7cbe5b0ab09a4703e87e24c4e417eca704fb1e6d3c5a150d1ad8
    to 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9fe8c7d1b3c33e83
    - ev-d033696005bbbd99
    - ev-2a905a5f460f34e6
  - name: legacy-native-ids
    value: '["SEM:f81aeb7bfb948dfde38c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2a905a5f460f34e6
    - ev-9fe8c7d1b3c33e83
    - ev-d033696005bbbd99
    - ev-dbd73af9e8489a2c
findings:
- finding_id: rec-f-cbd1d763580b3cf2
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9c32238bdffe4863
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hydrogen_gas'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:28Z;
    reviewed SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f;
    current SHA-256=16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050228Z-Hydrogen_gas.md","reports/yaml_record_review/Hydrogen_gas.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Hydrogen_gas.md` after the record changed from 2152fc1281bf7cbe5b0ab09a4703e87e24c4e417eca704fb1e6d3c5a150d1ad8
    to 16228278ff97e5b39800c957294c01e7cd5a2e2fafdb733189b2b4123504c88f; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9c32238bdffe4863
  evidence_ids:
  - ev-9fe8c7d1b3c33e83
  - ev-d033696005bbbd99
  - ev-2a905a5f460f34e6
  - ev-dbd73af9e8489a2c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydrogen_gas.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
