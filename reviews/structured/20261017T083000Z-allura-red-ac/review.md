# Per-record structured review: Allura_Red_AC (data/ingredients/mapped/Allura_Red_AC.yaml)

- Review: 20261017T083000Z-allura-red-ac
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Allura_Red_AC (data/ingredients/mapped/Allura_Red_AC.yaml, record-b4829307500697de, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Allura_Red_AC.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Allura_Red_AC.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b4829307500697de | data/ingredients/mapped/Allura_Red_AC.yaml | maintained | Allura_Red_AC |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b4829307500697de | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b4829307500697de | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b4829307500697de | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b4829307500697de.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b4829307500697de.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z; reviewed SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985; current SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985; hash_changed=False. Reports=["reports/yaml_record_review/Allura_Red_AC.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass; one historical auto-backfill event has truncated structure prose.

## Findings

### rec-f-43b6b73a0cb418c7: Historical review coverage and residual narrative: Allura_Red_AC

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b4829307500697de.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z; reviewed SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985; current SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985; hash_changed=False. Reports=["reports/yaml_record_review/Allura_Red_AC.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass; one historical auto-backfill event has truncated structure prose.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e8cc2ad054cf8db8 | data/ingredients/mapped/Allura_Red_AC.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[472],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:172687","line":474,"mapping_status":"MAPPED","ontology_id":"CHEBI:172687","preferred_term":"Allura Red AC"}],"identifier":"CHEBI:172687","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:172687","ontology_label":"Allura red AC","ontology_source":"CHEBI"},"preferred_term":"Allura Red AC","sssom_rows":[{"data_row":330,"object_id":"CHEBI:172687","object_label":"Allura red AC","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Allura_Red_AC","synonym_count":1} |
| ev-dbab6efa3bb7a8c1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [472] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-473cebb5481e5ce7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Allura_Red_AC; data-row positions=[330] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":330,"object_id":"CHEBI:172687","object_label":"Allura red AC","other":"disodium;6-hydroxy-5-[(2-methoxy-5-methyl-4-sulonatophenyl)diazenyl]naphthalene-2-sulonate&#124;CAS:25956-17-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Allura_Red_AC","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-c7a58e06e9bdf0c0 | docs/data/mapped_ingredients.csv; CSV lines=[474] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:172687","line":474,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:172687","preferred_term":"Allura Red AC","total_occurrences":"0"}] |
| ev-579522eaa89a536d | reports/yaml_record_review/Allura_Red_AC.md; &#96;data/ingredients/mapped/Allura_Red_AC.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:43; Completeness:57; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d167fa8d4e86dbe8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[235] | context_only | [{"current_record_sha256":"7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985","finding_id":"SEM:36b073d01758f6370bcf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-allura-red-ac
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Allura_Red_AC (data/ingredients/mapped/Allura_Red_AC.yaml)'
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
summary: Per-record structured review for Allura_Red_AC (data/ingredients/mapped/Allura_Red_AC.yaml,
  record-b4829307500697de, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Allura_Red_AC.yaml
    sha256: 7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Allura_Red_AC.md
    sha256: 516c20b3e44d6d29d4c553e6b3a546a85525f5e0a0177fb72d3e4f59ca1be19f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b4829307500697de
  path: data/ingredients/mapped/Allura_Red_AC.yaml
  label: Allura_Red_AC
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Allura_Red_AC.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Allura_Red_AC.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Allura_Red_AC.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b4829307500697de
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b4829307500697de
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b4829307500697de
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b4829307500697de
evidence:
- evidence_id: ev-e8cc2ad054cf8db8
  kind: record_content
  reference: data/ingredients/mapped/Allura_Red_AC.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[472],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:172687","line":474,"mapping_status":"MAPPED","ontology_id":"CHEBI:172687","preferred_term":"Allura
    Red AC"}],"identifier":"CHEBI:172687","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:172687","ontology_label":"Allura
    red AC","ontology_source":"CHEBI"},"preferred_term":"Allura Red AC","sssom_rows":[{"data_row":330,"object_id":"CHEBI:172687","object_label":"Allura
    red AC","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Allura_Red_AC","synonym_count":1}'
  snapshot_sha256: 7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985
- evidence_id: ev-dbab6efa3bb7a8c1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [472]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-473cebb5481e5ce7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Allura_Red_AC; data-row positions=[330]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":330,"object_id":"CHEBI:172687","object_label":"Allura
    red AC","other":"disodium;6-hydroxy-5-[(2-methoxy-5-methyl-4-sulonatophenyl)diazenyl]naphthalene-2-sulonate|CAS:25956-17-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Allura_Red_AC","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c7a58e06e9bdf0c0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[474]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:172687","line":474,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:172687","preferred_term":"Allura
    Red AC","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-579522eaa89a536d
  kind: prior_review
  reference: reports/yaml_record_review/Allura_Red_AC.md
  locator: '`data/ingredients/mapped/Allura_Red_AC.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:43; Completeness:57; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 516c20b3e44d6d29d4c553e6b3a546a85525f5e0a0177fb72d3e4f59ca1be19f
  quote: "Recommended Edits:\n- Optionally replace the truncated auto-backfill `changes`\
    \ prose in\n  `data/ingredients/mapped/Allura_Red_AC.yaml` with a complete structure\n\
    \  summary or a concise non-structural note. No identity, mapping, or exported\n\
    \  SSSOM change is needed."
- evidence_id: ev-d167fa8d4e86dbe8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[235]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985","finding_id":"SEM:36b073d01758f6370bcf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e852387324ad187c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b4829307500697de
  evidence_ids:
  - ev-e8cc2ad054cf8db8
  - ev-dbab6efa3bb7a8c1
  - ev-473cebb5481e5ce7
  - ev-c7a58e06e9bdf0c0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-27385db327c89af6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b4829307500697de
  evidence_ids:
  - ev-579522eaa89a536d
  - ev-e8cc2ad054cf8db8
  - ev-d167fa8d4e86dbe8
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z;
    reviewed SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985;
    current SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985;
    hash_changed=False. Reports=["reports/yaml_record_review/Allura_Red_AC.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate
    pass; one historical auto-backfill event has truncated structure prose.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-579522eaa89a536d
    - ev-e8cc2ad054cf8db8
  - name: legacy-native-ids
    value: '["SEM:36b073d01758f6370bcf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e8cc2ad054cf8db8
    - ev-579522eaa89a536d
    - ev-d167fa8d4e86dbe8
findings:
- finding_id: rec-f-43b6b73a0cb418c7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b4829307500697de
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Allura_Red_AC'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z;
    reviewed SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985;
    current SHA-256=7b0c454b3048412a46cbf06b8a8cdb7bc0a968092abb8897746ea1733df33985;
    hash_changed=False. Reports=["reports/yaml_record_review/Allura_Red_AC.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate
    pass; one historical auto-backfill event has truncated structure prose.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b4829307500697de
  evidence_ids:
  - ev-579522eaa89a536d
  - ev-e8cc2ad054cf8db8
  - ev-d167fa8d4e86dbe8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Allura_Red_AC.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
