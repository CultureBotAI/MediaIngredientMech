# Per-record structured review: Ca (data/ingredients/unmapped/Ca.yaml)

- Review: 20261017T083000Z-ca
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ca (data/ingredients/unmapped/Ca.yaml, record-93cd2f755a63894b, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/unmapped/Ca.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/unmapped/Ca.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-93cd2f755a63894b | data/ingredients/unmapped/Ca.yaml | maintained | Ca |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-93cd2f755a63894b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-93cd2f755a63894b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-93cd2f755a63894b | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-93cd2f755a63894b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-93cd2f755a63894b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:04Z; reviewed SHA-256=6a03b511c5ec090b792709a429d879c28fef07ef3fda37eccf1cad8606b2320a; current SHA-256=30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af; hash_changed=True. Reports=["reports/yaml_record_review/20261001T044704Z-Ca.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

### CAS-qualified hydrate label and three-occurrence transfer

provenance: supported. Targets: record-93cd2f755a63894b.

The specific stranded-label/3-occurrence defect is already fixed: resolving synonym is on CHEBI:86159 and in its SSSOM row; the active record and pinned membership count are 202/202; Ca is a zero-count REJECTED tombstone without a final row. This says nothing about additional occurrences in a newer sibling snapshot.

## Findings

### rec-f-c188b1832a147499: Historical review coverage and residual narrative: Ca

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-93cd2f755a63894b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:04Z; reviewed SHA-256=6a03b511c5ec090b792709a429d879c28fef07ef3fda37eccf1cad8606b2320a; current SHA-256=30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af; hash_changed=True. Reports=["reports/yaml_record_review/20261001T044704Z-Ca.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-10708f98b4caeee4 | data/ingredients/unmapped/Ca.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[48],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0049","line":50,"mapping_status":"REJECTED","ontology_id":"","preferred_term":"Ca"}],"identifier":"UNMAPPED_0049","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Ca","sssom_rows":[],"sssom_subject":"MIM:Ca","synonym_count":0} |
| ev-5769c2652345d2f4 | data/curated/unmapped_ingredients.yaml; ingredients positions (zero-based): [48] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-19c0af2a56bc5bf5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ca; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-f17fb53120415270 | docs/data/unmapped_ingredients.csv; CSV lines=[50] | supports | Published identity and count rows inspected: [{"identifier":"UNMAPPED_0049","line":50,"mapping_quality":"","mapping_status":"REJECTED","media_count":"0","ontology_id":"","preferred_term":"Ca","total_occurrences":"0"}] |
| ev-ac8cc401220219c7 | reports/yaml_record_review/20261001T044704Z-Ca.md; YAML Record Review: Ca:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ae225a452b755e57 | reports/yaml_record_review/Ca_No32_X_4_H2o.md; &#96;data/ingredients/mapped/Ca_No32_X_4_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:40; Completeness:62; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5f1c4a27fd8956b2 | data/ingredients/mapped/Ca_No32_X_4_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[619],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86159","line":621,"mapping_status":"MAPPED","ontology_id":"CHEBI:86159","preferred_term":"Ca(NO3)2 x 4 H2O"}],"identifier":"CHEBI:86159","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":202,"edge_count":202,"occurrences":202},"occurrence_statistics":{"media_count":202,"total_occurrences":202},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86159","ontology_label":"calcium nitrate tetrahydrate","ontology_source":"CHEBI"},"preferred_term":"Ca(NO3)2 x 4 H2O","sssom_rows":[{"data_row":600,"object_id":"CHEBI:86159","object_label":"calcium nitrate tetrahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ca_No32_X_4_H2o","synonym_count":16} |
| ev-298e818e08d3065c | mappings/culturemech_recipe_membership.tsv; mim_identifier=CHEBI:86159; scoped_identity_corrections=2026-10-03 | supports | 202 distinct recipe edges and 202 occurrences, matching the live YAML/aggregate. The explicit three-recipe correction uses CultureMech:000171, CultureMech:000174, CultureMech:000238. |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ca
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ca (data/ingredients/unmapped/Ca.yaml)'
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
summary: Per-record structured review for Ca (data/ingredients/unmapped/Ca.yaml, record-93cd2f755a63894b,
  mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/unmapped/Ca.yaml
    sha256: 30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
    role: context
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/unmapped_ingredients.csv
    sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
    role: context
  - path: reports/yaml_record_review/20261001T044704Z-Ca.md
    sha256: 744e7c6079668fb0d1afb7c6d8241ff89b2005ef163ebfc715b59fff780624d8
    role: context
  - path: reports/yaml_record_review/Ca_No32_X_4_H2o.md
    sha256: 98df3417ee84630599b14b0a8e6499d16aa8856773ede25a5bf6125a2fa9115d
    role: context
  - path: data/ingredients/mapped/Ca_No32_X_4_H2o.yaml
    sha256: ac99b7e60c6d2f38dfb9299f5ba6ea70e07e6aeddbedf8e8254d19b694f4c907
    role: context
  - path: mappings/culturemech_recipe_membership.tsv
    sha256: ab3f3905303c2b7e78192d1006ba2f157331ef0c27774aa51099e97f140ff929
    role: context
targets:
- target_id: record-93cd2f755a63894b
  path: data/ingredients/unmapped/Ca.yaml
  label: Ca
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Ca.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/unmapped/Ca.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/unmapped/Ca.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-93cd2f755a63894b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-93cd2f755a63894b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-93cd2f755a63894b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-93cd2f755a63894b
evidence:
- evidence_id: ev-10708f98b4caeee4
  kind: record_content
  reference: data/ingredients/unmapped/Ca.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[48],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0049","line":50,"mapping_status":"REJECTED","ontology_id":"","preferred_term":"Ca"}],"identifier":"UNMAPPED_0049","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Ca","sssom_rows":[],"sssom_subject":"MIM:Ca","synonym_count":0}'
  snapshot_sha256: 30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af
- evidence_id: ev-5769c2652345d2f4
  kind: validation
  reference: data/curated/unmapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [48]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
- evidence_id: ev-19c0af2a56bc5bf5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ca; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f17fb53120415270
  kind: record_content
  reference: docs/data/unmapped_ingredients.csv
  locator: CSV lines=[50]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"UNMAPPED_0049","line":50,"mapping_quality":"","mapping_status":"REJECTED","media_count":"0","ontology_id":"","preferred_term":"Ca","total_occurrences":"0"}]'
  snapshot_sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
- evidence_id: ev-ac8cc401220219c7
  kind: prior_review
  reference: reports/yaml_record_review/20261001T044704Z-Ca.md
  locator: 'YAML Record Review: Ca:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60;
    Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 744e7c6079668fb0d1afb7c6d8241ff89b2005ef163ebfc715b59fff780624d8
  quote: 'Findings:

    - **major**: `data/ingredients/unmapped/Ca.yaml` remains `UNMAPPED`; no exact
    ontology term or independently supported registry identity is recorded. Do not
    exact-match it to a broader parent, component, hydrate, salt, or lookalike label.


    Recommended Edits:

    - Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Ca.yaml`
    before mapping it.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Ca.yaml`,
    `just validate-terms data/ingredients/unmapped/Ca.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-ae225a452b755e57
  kind: prior_review
  reference: reports/yaml_record_review/Ca_No32_X_4_H2o.md
  locator: '`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:40; Completeness:62; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 98df3417ee84630599b14b0a8e6499d16aa8856773ede25a5bf6125a2fa9115d
  quote: "Recommended Edits:\n- Major: merge the calcium nitrate tetrahydrate raw\
    \ label and three occurrences\n  from `data/ingredients/unmapped/Ca.yaml` into\n\
    \  `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`, retire or update the stale\n\
    \  `UNMAPPED_0049` placeholder, refresh occurrence statistics, and regenerate\n\
    \  `mappings/ingredient_mappings.sssom.tsv` and `docs/data/label_index.csv`.\n\
    - Minor: refresh the hydrate-review report so the calcium nitrate tetrahydrate\n\
    \  spellings now carried by this record no longer appear as `NOT_IN_MIM`."
- evidence_id: ev-5f1c4a27fd8956b2
  kind: record_content
  reference: data/ingredients/mapped/Ca_No32_X_4_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[619],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86159","line":621,"mapping_status":"MAPPED","ontology_id":"CHEBI:86159","preferred_term":"Ca(NO3)2
    x 4 H2O"}],"identifier":"CHEBI:86159","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":202,"edge_count":202,"occurrences":202},"occurrence_statistics":{"media_count":202,"total_occurrences":202},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86159","ontology_label":"calcium
    nitrate tetrahydrate","ontology_source":"CHEBI"},"preferred_term":"Ca(NO3)2 x
    4 H2O","sssom_rows":[{"data_row":600,"object_id":"CHEBI:86159","object_label":"calcium
    nitrate tetrahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ca_No32_X_4_H2o","synonym_count":16}'
  snapshot_sha256: ac99b7e60c6d2f38dfb9299f5ba6ea70e07e6aeddbedf8e8254d19b694f4c907
- evidence_id: ev-298e818e08d3065c
  kind: record_content
  reference: mappings/culturemech_recipe_membership.tsv
  locator: mim_identifier=CHEBI:86159; scoped_identity_corrections=2026-10-03
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 202 distinct recipe edges and 202 occurrences, matching the live YAML/aggregate.
    The explicit three-recipe correction uses CultureMech:000171, CultureMech:000174,
    CultureMech:000238.
  snapshot_sha256: ab3f3905303c2b7e78192d1006ba2f157331ef0c27774aa51099e97f140ff929
assessments:
- assessment_id: a-39ab88e2f0e52198
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-93cd2f755a63894b
  evidence_ids:
  - ev-10708f98b4caeee4
  - ev-5769c2652345d2f4
  - ev-19c0af2a56bc5bf5
  - ev-f17fb53120415270
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5f86608b5dbbaa4a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-93cd2f755a63894b
  evidence_ids:
  - ev-ac8cc401220219c7
  - ev-10708f98b4caeee4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:04Z;
    reviewed SHA-256=6a03b511c5ec090b792709a429d879c28fef07ef3fda37eccf1cad8606b2320a;
    current SHA-256=30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T044704Z-Ca.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Specific
    single-ingredient residual remains unresolved: current evidence does not support
    an exact ontology or stable-registry identity.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac8cc401220219c7
    - ev-10708f98b4caeee4
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-10708f98b4caeee4
    - ev-ac8cc401220219c7
- assessment_id: a-5a98a9c0c31ba396
  area: provenance
  topic: CAS-qualified hydrate label and three-occurrence transfer
  outcome: supported
  summary: 'The specific stranded-label/3-occurrence defect is already fixed: resolving
    synonym is on CHEBI:86159 and in its SSSOM row; the active record and pinned membership
    count are 202/202; Ca is a zero-count REJECTED tombstone without a final row.
    This says nothing about additional occurrences in a newer sibling snapshot.'
  target_ids:
  - record-93cd2f755a63894b
  evidence_ids:
  - ev-ae225a452b755e57
  - ev-ac8cc401220219c7
  - ev-5f1c4a27fd8956b2
  - ev-10708f98b4caeee4
  - ev-298e818e08d3065c
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ae225a452b755e57
    - ev-ac8cc401220219c7
    - ev-5f1c4a27fd8956b2
    - ev-10708f98b4caeee4
    - ev-298e818e08d3065c
findings:
- finding_id: rec-f-c188b1832a147499
  issue_key: mim-reconciliation-historical-review-coverage-and-r-93cd2f755a63894b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ca'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:04Z;
    reviewed SHA-256=6a03b511c5ec090b792709a429d879c28fef07ef3fda37eccf1cad8606b2320a;
    current SHA-256=30536efdb26bcaaa5729c3e61ca9ea9cd7372cd3ed7106834895ee8da38b14af;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T044704Z-Ca.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Specific
    single-ingredient residual remains unresolved: current evidence does not support
    an exact ontology or stable-registry identity.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-93cd2f755a63894b
  evidence_ids:
  - ev-ac8cc401220219c7
  - ev-10708f98b4caeee4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Ca.yaml
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
