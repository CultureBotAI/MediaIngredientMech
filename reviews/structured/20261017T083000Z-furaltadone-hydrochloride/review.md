# Per-record structured review: Furaltadone_Hydrochloride (data/ingredients/mapped/Furaltadone_Hydrochloride.yaml)

- Review: 20261017T083000Z-furaltadone-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Furaltadone_Hydrochloride (data/ingredients/mapped/Furaltadone_Hydrochloride.yaml, record-2e4090e1bf27a52d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Furaltadone_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Furaltadone_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2e4090e1bf27a52d | data/ingredients/mapped/Furaltadone_Hydrochloride.yaml | maintained | Furaltadone_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2e4090e1bf27a52d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2e4090e1bf27a52d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2e4090e1bf27a52d | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2e4090e1bf27a52d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2e4090e1bf27a52d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:11:13Z; reviewed SHA-256=87e18c29f00b3dc30303c304ca308b8afee481cda252dc34ba101f19d51ff259; current SHA-256=d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81; hash_changed=True. Reports=["reports/yaml_record_review/Furaltadone_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The NCIT target is exact, but the record still emits it as a narrow match plus local registry rows.

### Furaltadone hydrochloride predicate and registry-row shape

grounding: supported. Targets: record-2e4090e1bf27a52d.

NCIT:C217928 is now both primary and ontology identifier with EXACT_MATCH; the sole SSSOM row is skos:exactMatch to NCIT:C217928. The prior CAS/local-registry and non-exact NCIT rows are gone. This verifies the requested representation change, not fresh NCIT/CAS scientific validation.

### Furaltadone CAS alias verification

identity: unknown. Targets: record-2e4090e1bf27a52d.

CAS 3759-92-1 remains in chemical_properties and final other. The old report explicitly requested registry-source verification; promoting NCIT does not itself establish that alias. A current resolving registry source is still needed.

## Findings

### rec-f-a7e06cacf823b6f9: Verify retained Furaltadone CAS alias

minor / deferred / provisional; issue key: mim-reconciliation-cas-source-2e4090e1bf27a52d.

CAS 3759-92-1 still publishes as a resolving alias, while the original report did not establish an authoritative registry match. Verify exact hydrochloride identity before retaining or rejecting this alias.

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-92f2602ee8f36ebd | data/ingredients/mapped/Furaltadone_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2679],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C217928","line":2681,"mapping_status":"MAPPED","ontology_id":"NCIT:C217928","preferred_term":"Furaltadone hydrochloride"}],"identifier":"NCIT:C217928","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C217928","ontology_label":"Furaltadone Hydrochloride","ontology_source":"NCIT"},"preferred_term":"Furaltadone hydrochloride","sssom_rows":[{"data_row":1256,"object_id":"NCIT:C217928","object_label":"Furaltadone Hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Furaltadone_Hydrochloride","synonym_count":0} |
| ev-6fd4802b6fb4b4d5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2679] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-065ced0d6e60ecd2 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Furaltadone_Hydrochloride; data-row positions=[1256] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1256,"object_id":"NCIT:C217928","object_label":"Furaltadone Hydrochloride","other":"CAS:3759-92-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Furaltadone_Hydrochloride","validation_method":"manual:yaml_record_review&#124;EXACT_NCIT&#124;2026-10-03"}] |
| ev-505c7326f8238146 | docs/data/mapped_ingredients.csv; CSV lines=[2681] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C217928","line":2681,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C217928","preferred_term":"Furaltadone hydrochloride","total_occurrences":"0"}] |
| ev-836307283d84c74a | reports/yaml_record_review/Furaltadone_Hydrochloride.md; &#96;data/ingredients/mapped/Furaltadone_Hydrochloride.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:35; Completeness:59; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3e33246292a1173e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[640] | context_only | [{"current_record_sha256":"d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81","finding_id":"SEM:daa5a3f8cbe30f00018a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ebbea96d3683ce6b | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-a7e06cacf823b6f9] | context_only | Predecessor structured review finding f-a7e06cacf823b6f9 in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-furaltadone-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Furaltadone_Hydrochloride (data/ingredients/mapped/Furaltadone_Hydrochloride.yaml)'
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
summary: Per-record structured review for Furaltadone_Hydrochloride (data/ingredients/mapped/Furaltadone_Hydrochloride.yaml,
  record-2e4090e1bf27a52d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
    sha256: d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81
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
  - path: reports/yaml_record_review/Furaltadone_Hydrochloride.md
    sha256: 4fe409820f79b03a7a779764bc8adf1fd3af60ccd368bf1e5e9f48efd8367241
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2e4090e1bf27a52d
  path: data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
  label: Furaltadone_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2e4090e1bf27a52d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2e4090e1bf27a52d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2e4090e1bf27a52d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2e4090e1bf27a52d
evidence:
- evidence_id: ev-92f2602ee8f36ebd
  kind: record_content
  reference: data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2679],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C217928","line":2681,"mapping_status":"MAPPED","ontology_id":"NCIT:C217928","preferred_term":"Furaltadone
    hydrochloride"}],"identifier":"NCIT:C217928","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C217928","ontology_label":"Furaltadone
    Hydrochloride","ontology_source":"NCIT"},"preferred_term":"Furaltadone hydrochloride","sssom_rows":[{"data_row":1256,"object_id":"NCIT:C217928","object_label":"Furaltadone
    Hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Furaltadone_Hydrochloride","synonym_count":0}'
  snapshot_sha256: d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81
- evidence_id: ev-6fd4802b6fb4b4d5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2679]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-065ced0d6e60ecd2
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Furaltadone_Hydrochloride; data-row positions=[1256]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1256,"object_id":"NCIT:C217928","object_label":"Furaltadone
    Hydrochloride","other":"CAS:3759-92-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Furaltadone_Hydrochloride","validation_method":"manual:yaml_record_review|EXACT_NCIT|2026-10-03"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-505c7326f8238146
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2681]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C217928","line":2681,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C217928","preferred_term":"Furaltadone
    hydrochloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-836307283d84c74a
  kind: prior_review
  reference: reports/yaml_record_review/Furaltadone_Hydrochloride.md
  locator: '`data/ingredients/mapped/Furaltadone_Hydrochloride.yaml`:2; Verdict:4;
    Identity:12; Validation:24; Evidence:35; Completeness:59; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4fe409820f79b03a7a779764bc8adf1fd3af60ccd368bf1e5e9f48efd8367241
  quote: "Recommended Edits:\n- Major: regrade `data/ingredients/mapped/Furaltadone_Hydrochloride.yaml`\
    \ from\n  `NARROW_MATCH` to an exact NCIT mapping or promote `NCIT:C217928` as\
    \ the\n  primary identifier, sync `data/curated/mapped_ingredients.yaml`, regenerate\n\
    \  final SSSOM so it no longer emits `skos:narrowMatch` or unnecessary local\n\
    \  registry rows, and rerun SSSOM invariants.\n- Minor: verify CAS RN `3759-92-1`\
    \ from the original CultureBotHT input or\n  another registry source before keeping\
    \ it as an exact registry identity."
- evidence_id: ev-3e33246292a1173e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[640]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81","finding_id":"SEM:daa5a3f8cbe30f00018a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ebbea96d3683ce6b
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-a7e06cacf823b6f9]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a7e06cacf823b6f9 in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-ce0b12558cf10704
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2e4090e1bf27a52d
  evidence_ids:
  - ev-92f2602ee8f36ebd
  - ev-6fd4802b6fb4b4d5
  - ev-065ced0d6e60ecd2
  - ev-505c7326f8238146
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-67a4b4759d565a7a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2e4090e1bf27a52d
  evidence_ids:
  - ev-836307283d84c74a
  - ev-92f2602ee8f36ebd
  - ev-3e33246292a1173e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:11:13Z;
    reviewed SHA-256=87e18c29f00b3dc30303c304ca308b8afee481cda252dc34ba101f19d51ff259;
    current SHA-256=d266285ec6a66b1ac0bb331c14f42232646f3f1c799bfb4c91b5c1c2f5808f81;
    hash_changed=True. Reports=["reports/yaml_record_review/Furaltadone_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The NCIT
    target is exact, but the record still emits it as a narrow match plus local registry
    rows.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-836307283d84c74a
    - ev-92f2602ee8f36ebd
  - name: legacy-native-ids
    value: '["SEM:daa5a3f8cbe30f00018a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-92f2602ee8f36ebd
    - ev-836307283d84c74a
    - ev-3e33246292a1173e
- assessment_id: a-b4f5a6cdab2de088
  area: grounding
  topic: Furaltadone hydrochloride predicate and registry-row shape
  outcome: supported
  summary: NCIT:C217928 is now both primary and ontology identifier with EXACT_MATCH;
    the sole SSSOM row is skos:exactMatch to NCIT:C217928. The prior CAS/local-registry
    and non-exact NCIT rows are gone. This verifies the requested representation change,
    not fresh NCIT/CAS scientific validation.
  target_ids:
  - record-2e4090e1bf27a52d
  evidence_ids:
  - ev-836307283d84c74a
  - ev-92f2602ee8f36ebd
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-836307283d84c74a
    - ev-92f2602ee8f36ebd
- assessment_id: a-b731be39c8dcc771
  area: identity
  topic: Furaltadone CAS alias verification
  outcome: unknown
  summary: CAS 3759-92-1 remains in chemical_properties and final other. The old report
    explicitly requested registry-source verification; promoting NCIT does not itself
    establish that alias. A current resolving registry source is still needed.
  target_ids:
  - record-2e4090e1bf27a52d
  evidence_ids:
  - ev-836307283d84c74a
  - ev-92f2602ee8f36ebd
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-836307283d84c74a
    - ev-92f2602ee8f36ebd
findings:
- finding_id: rec-f-a7e06cacf823b6f9
  issue_key: mim-reconciliation-cas-source-2e4090e1bf27a52d
  category: identity
  severity: minor
  status: deferred
  certainty: provisional
  title: Verify retained Furaltadone CAS alias
  description: CAS 3759-92-1 still publishes as a resolving alias, while the original
    report did not establish an authoritative registry match. Verify exact hydrochloride
    identity before retaining or rejecting this alias.
  target_ids:
  - record-2e4090e1bf27a52d
  evidence_ids:
  - ev-836307283d84c74a
  - ev-92f2602ee8f36ebd
  - ev-ebbea96d3683ce6b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Furaltadone_Hydrochloride.yaml
    role: maintained ingredient
  field_paths:
  - chemical_properties.cas_rn
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - cas-source
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024629Z-mim-reconcile-all-batch-01
    finding_id: f-a7e06cacf823b6f9
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
