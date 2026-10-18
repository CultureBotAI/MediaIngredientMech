# Per-record structured review: Ampicillin (data/ingredients/mapped/Ampicillin.yaml)

- Review: 20261017T083000Z-ampicillin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ampicillin (data/ingredients/mapped/Ampicillin.yaml, record-a56205b401586960, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ampicillin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ampicillin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a56205b401586960 | data/ingredients/mapped/Ampicillin.yaml | maintained | Ampicillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a56205b401586960 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a56205b401586960 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a56205b401586960 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a56205b401586960.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a56205b401586960.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z; reviewed SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4; current SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4; hash_changed=False. Reports=["reports/yaml_record_review/Ampicillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, chemistry, memberships, source-backed selective-agent role, row-review confirmation, and SSSOM row pass, but CultureMech role/property metadata remains in synonyms.

## Findings

### rec-f-4d9d958d9d3a01ff: Historical review coverage and residual narrative: Ampicillin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a56205b401586960.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z; reviewed SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4; current SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4; hash_changed=False. Reports=["reports/yaml_record_review/Ampicillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, chemistry, memberships, source-backed selective-agent role, row-review confirmation, and SSSOM row pass, but CultureMech role/property metadata remains in synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b15fc5b4c89b8af0 | data/ingredients/mapped/Ampicillin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[489],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28971","line":491,"mapping_status":"MAPPED","ontology_id":"CHEBI:28971","preferred_term":"Ampicillin"}],"identifier":"CHEBI:28971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28971","ontology_label":"ampicillin","ontology_source":"CHEBI"},"preferred_term":"Ampicillin","sssom_rows":[{"data_row":373,"object_id":"CHEBI:28971","object_label":"ampicillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ampicillin","synonym_count":18} |
| ev-8f212a941fee2878 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [489] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-234b127c0c9ad20f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ampicillin; data-row positions=[373] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":373,"object_id":"CHEBI:28971","object_label":"ampicillin","other":"(2S,5R,6R)-6-{[(2R)-2-AMINO-2-PHENYLETHANOYL]AMINO}-3,3-DIMETHYL-7-OXO-4-THIA-1-AZABICYCLO[3.2.0]HEPTANE-2-CARBOXYLIC ACID&#124;(2S,5R,6R)-6-{[(2R)-2-amino-2-phenylacetyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic acid&#124;(2S,6R)-6-{[(2R)-2-amino-2-phenylethanoyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic acid&#124;6-(D-(2-amino-2-phenylacetamido))-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo(3.2.0)heptane-2-carboxylic acid&#124;6beta-[(2R)-2-amino-2-phenylacetamido]-2,2-dimethylpenam-3alpha-carboxylic acid&#124;ABPC&#124;D-(-)-6-(alpha-aminophenylacetamido)penicillanic acid&#124;D-(-)-ampicillin&#124;aminobenzylpenicillin&#124;ampicilina&#124;ampicillin acid&#124;ampicilline&#124;ampicillinum&#124;Ampicillin (50 mg/ml)&#124;CAS:69-53-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Ampicillin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-98f6b61795ef10b2 | docs/data/mapped_ingredients.csv; CSV lines=[491] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28971","line":491,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"23","ontology_id":"CHEBI:28971","preferred_term":"Ampicillin","total_occurrences":"23"}] |
| ev-80f9950dfb655d71 | reports/yaml_record_review/Ampicillin.md; &#96;data/ingredients/mapped/Ampicillin.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:44; Completeness:66; Recommended Edits:77 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cfe27b584329556f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[255] | context_only | [{"current_record_sha256":"41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4","finding_id":"SEM:501b8a8dc43d634e8964","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ampicillin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ampicillin (data/ingredients/mapped/Ampicillin.yaml)'
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
summary: Per-record structured review for Ampicillin (data/ingredients/mapped/Ampicillin.yaml,
  record-a56205b401586960, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ampicillin.yaml
    sha256: 41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4
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
  - path: reports/yaml_record_review/Ampicillin.md
    sha256: 93c2bac6ad4246a49c10deeb9f0c146f7cd700c361b5748499ea7c6f1d81e8da
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a56205b401586960
  path: data/ingredients/mapped/Ampicillin.yaml
  label: Ampicillin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ampicillin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ampicillin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ampicillin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a56205b401586960
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a56205b401586960
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a56205b401586960
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a56205b401586960
evidence:
- evidence_id: ev-b15fc5b4c89b8af0
  kind: record_content
  reference: data/ingredients/mapped/Ampicillin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[489],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28971","line":491,"mapping_status":"MAPPED","ontology_id":"CHEBI:28971","preferred_term":"Ampicillin"}],"identifier":"CHEBI:28971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28971","ontology_label":"ampicillin","ontology_source":"CHEBI"},"preferred_term":"Ampicillin","sssom_rows":[{"data_row":373,"object_id":"CHEBI:28971","object_label":"ampicillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ampicillin","synonym_count":18}'
  snapshot_sha256: 41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4
- evidence_id: ev-8f212a941fee2878
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [489]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-234b127c0c9ad20f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ampicillin; data-row positions=[373]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":373,"object_id":"CHEBI:28971","object_label":"ampicillin","other":"(2S,5R,6R)-6-{[(2R)-2-AMINO-2-PHENYLETHANOYL]AMINO}-3,3-DIMETHYL-7-OXO-4-THIA-1-AZABICYCLO[3.2.0]HEPTANE-2-CARBOXYLIC
    ACID|(2S,5R,6R)-6-{[(2R)-2-amino-2-phenylacetyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic
    acid|(2S,6R)-6-{[(2R)-2-amino-2-phenylethanoyl]amino}-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic
    acid|6-(D-(2-amino-2-phenylacetamido))-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo(3.2.0)heptane-2-carboxylic
    acid|6beta-[(2R)-2-amino-2-phenylacetamido]-2,2-dimethylpenam-3alpha-carboxylic
    acid|ABPC|D-(-)-6-(alpha-aminophenylacetamido)penicillanic acid|D-(-)-ampicillin|aminobenzylpenicillin|ampicilina|ampicillin
    acid|ampicilline|ampicillinum|Ampicillin (50 mg/ml)|CAS:69-53-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Ampicillin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-98f6b61795ef10b2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[491]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28971","line":491,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"23","ontology_id":"CHEBI:28971","preferred_term":"Ampicillin","total_occurrences":"23"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-80f9950dfb655d71
  kind: prior_review
  reference: reports/yaml_record_review/Ampicillin.md
  locator: '`data/ingredients/mapped/Ampicillin.yaml`:2; Verdict:4; Identity:11; Validation:26;
    Evidence:44; Completeness:66; Recommended Edits:77'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 93c2bac6ad4246a49c10deeb9f0c146f7cd700c361b5748499ea7c6f1d81e8da
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Ampicillin.yaml`, remove\
    \ the four\n  `Role: Antimicrobial agent; Properties: ...` strings from `synonyms`.\n\
    - Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ampicillin.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-cfe27b584329556f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[255]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4","finding_id":"SEM:501b8a8dc43d634e8964","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b23c892741ecfc1a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a56205b401586960
  evidence_ids:
  - ev-b15fc5b4c89b8af0
  - ev-8f212a941fee2878
  - ev-234b127c0c9ad20f
  - ev-98f6b61795ef10b2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0e2a38b230b28297
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a56205b401586960
  evidence_ids:
  - ev-80f9950dfb655d71
  - ev-b15fc5b4c89b8af0
  - ev-cfe27b584329556f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z;
    reviewed SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4;
    current SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4;
    hash_changed=False. Reports=["reports/yaml_record_review/Ampicillin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, chemistry, memberships, source-backed selective-agent role, row-review
    confirmation, and SSSOM row pass, but CultureMech role/property metadata remains
    in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-80f9950dfb655d71
    - ev-b15fc5b4c89b8af0
  - name: legacy-native-ids
    value: '["SEM:501b8a8dc43d634e8964"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b15fc5b4c89b8af0
    - ev-80f9950dfb655d71
    - ev-cfe27b584329556f
findings:
- finding_id: rec-f-4d9d958d9d3a01ff
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a56205b401586960
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ampicillin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z;
    reviewed SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4;
    current SHA-256=41b4b2f941c10fd8123b15831f9f9522507f3a7a4305b42b4207e6f308cd50d4;
    hash_changed=False. Reports=["reports/yaml_record_review/Ampicillin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, chemistry, memberships, source-backed selective-agent role, row-review
    confirmation, and SSSOM row pass, but CultureMech role/property metadata remains
    in synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a56205b401586960
  evidence_ids:
  - ev-80f9950dfb655d71
  - ev-b15fc5b4c89b8af0
  - ev-cfe27b584329556f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ampicillin.yaml
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
