# Per-record structured review: Ferulic_Acid (data/ingredients/mapped/Ferulic_Acid.yaml)

- Review: 20261017T083000Z-ferulic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ferulic_Acid (data/ingredients/mapped/Ferulic_Acid.yaml, record-b2b3d07da1007150, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ferulic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ferulic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b2b3d07da1007150 | data/ingredients/mapped/Ferulic_Acid.yaml | maintained | Ferulic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b2b3d07da1007150 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b2b3d07da1007150 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b2b3d07da1007150 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b2b3d07da1007150.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b2b3d07da1007150.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:27:09Z; reviewed SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751; current SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751; hash_changed=False. Reports=["reports/yaml_record_review/Ferulic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed trans ferulic-acid record maps to generic ferulic acid while a trans-ferulic acid term exists.

## Findings

### rec-f-d35e477d45407f44: Historical review coverage and residual narrative: Ferulic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b2b3d07da1007150.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:27:09Z; reviewed SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751; current SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751; hash_changed=False. Reports=["reports/yaml_record_review/Ferulic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed trans ferulic-acid record maps to generic ferulic acid while a trans-ferulic acid term exists.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-526fbb2c82ab66d8 | data/ingredients/mapped/Ferulic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[996],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:193350","line":998,"mapping_status":"MAPPED","ontology_id":"CHEBI:193350","preferred_term":"Ferulic Acid"}],"identifier":"CHEBI:193350","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:193350","ontology_label":"ferulic acid","ontology_source":"CHEBI"},"preferred_term":"Ferulic Acid","sssom_rows":[{"data_row":1197,"object_id":"CHEBI:193350","object_label":"ferulic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferulic_Acid","synonym_count":2} |
| ev-52e9df5604341de6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [996] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-36d3737cfe70d196 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ferulic_Acid; data-row positions=[1197] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1197,"object_id":"CHEBI:193350","object_label":"ferulic acid","other":"trans-4-Hydroxy-3-methoxycinnamic acid&#124;3-(4-hydroxy-3-methoxyphenyl)prop-2-enoic acid&#124;CAS:537-98-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferulic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-8a5a7a78caa095ef | docs/data/mapped_ingredients.csv; CSV lines=[998] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:193350","line":998,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:193350","preferred_term":"Ferulic Acid","total_occurrences":"0"}] |
| ev-c03ac6718667af8a | reports/yaml_record_review/Ferulic_Acid.md; &#96;data/ingredients/mapped/Ferulic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:32; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-29cceef85802e8fc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[606] | context_only | [{"current_record_sha256":"3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751","finding_id":"SEM:8b039c466d6f7a1f71c8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ferulic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ferulic_Acid (data/ingredients/mapped/Ferulic_Acid.yaml)'
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
summary: Per-record structured review for Ferulic_Acid (data/ingredients/mapped/Ferulic_Acid.yaml,
  record-b2b3d07da1007150, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ferulic_Acid.yaml
    sha256: 3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Ferulic_Acid.md
    sha256: 47eaeec59c885f90abff5657402c0d39cae0549ceafa238be40b6d5082d0b935
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b2b3d07da1007150
  path: data/ingredients/mapped/Ferulic_Acid.yaml
  label: Ferulic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferulic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ferulic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ferulic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b2b3d07da1007150
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b2b3d07da1007150
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b2b3d07da1007150
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b2b3d07da1007150
evidence:
- evidence_id: ev-526fbb2c82ab66d8
  kind: record_content
  reference: data/ingredients/mapped/Ferulic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[996],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:193350","line":998,"mapping_status":"MAPPED","ontology_id":"CHEBI:193350","preferred_term":"Ferulic
    Acid"}],"identifier":"CHEBI:193350","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:193350","ontology_label":"ferulic
    acid","ontology_source":"CHEBI"},"preferred_term":"Ferulic Acid","sssom_rows":[{"data_row":1197,"object_id":"CHEBI:193350","object_label":"ferulic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferulic_Acid","synonym_count":2}'
  snapshot_sha256: 3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751
- evidence_id: ev-52e9df5604341de6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [996]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-36d3737cfe70d196
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ferulic_Acid; data-row positions=[1197]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1197,"object_id":"CHEBI:193350","object_label":"ferulic
    acid","other":"trans-4-Hydroxy-3-methoxycinnamic acid|3-(4-hydroxy-3-methoxyphenyl)prop-2-enoic
    acid|CAS:537-98-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferulic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8a5a7a78caa095ef
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[998]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:193350","line":998,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:193350","preferred_term":"Ferulic
    Acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c03ac6718667af8a
  kind: prior_review
  reference: reports/yaml_record_review/Ferulic_Acid.md
  locator: '`data/ingredients/mapped/Ferulic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:32; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 47eaeec59c885f90abff5657402c0d39cae0549ceafa238be40b6d5082d0b935
  quote: "Recommended Edits:\n- Major: after remapping `Ferulate` to `CHEBI:29749`,\
    \ remap\n  `data/ingredients/mapped/Ferulic_Acid.yaml` to `CHEBI:17620`\n  `trans-ferulic\
    \ acid`, refresh the trans InChI/SMILES from PubChem or ChEBI,\n  sync `data/curated/mapped_ingredients.yaml`,\
    \ regenerate\n  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation\
    \ plus\n  the final SSSOM invariant gates."
- evidence_id: ev-29cceef85802e8fc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[606]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751","finding_id":"SEM:8b039c466d6f7a1f71c8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-05ec0a457d9383c2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b2b3d07da1007150
  evidence_ids:
  - ev-526fbb2c82ab66d8
  - ev-52e9df5604341de6
  - ev-36d3737cfe70d196
  - ev-8a5a7a78caa095ef
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-880ad3d56e5d4a0b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b2b3d07da1007150
  evidence_ids:
  - ev-c03ac6718667af8a
  - ev-526fbb2c82ab66d8
  - ev-29cceef85802e8fc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:27:09Z;
    reviewed SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751;
    current SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751;
    hash_changed=False. Reports=["reports/yaml_record_review/Ferulic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    trans ferulic-acid record maps to generic ferulic acid while a trans-ferulic acid
    term exists.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c03ac6718667af8a
    - ev-526fbb2c82ab66d8
  - name: legacy-native-ids
    value: '["SEM:8b039c466d6f7a1f71c8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-526fbb2c82ab66d8
    - ev-c03ac6718667af8a
    - ev-29cceef85802e8fc
findings:
- finding_id: rec-f-d35e477d45407f44
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b2b3d07da1007150
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ferulic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:27:09Z;
    reviewed SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751;
    current SHA-256=3a18f99f38fa777c999e2261c52782ddf9aab37fafb29e6fa968593aa3668751;
    hash_changed=False. Reports=["reports/yaml_record_review/Ferulic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    trans ferulic-acid record maps to generic ferulic acid while a trans-ferulic acid
    term exists.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b2b3d07da1007150
  evidence_ids:
  - ev-c03ac6718667af8a
  - ev-526fbb2c82ab66d8
  - ev-29cceef85802e8fc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferulic_Acid.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
