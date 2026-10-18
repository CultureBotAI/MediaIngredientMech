# Per-record structured review: Aluminum_Chloride_Hydrate (data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml)

- Review: 20261017T083000Z-aluminum-chloride-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Aluminum_Chloride_Hydrate (data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml, record-d6cbcbac1e7b0e07, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d6cbcbac1e7b0e07 | data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml | maintained | Aluminum_Chloride_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d6cbcbac1e7b0e07 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d6cbcbac1e7b0e07 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d6cbcbac1e7b0e07 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d6cbcbac1e7b0e07.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d6cbcbac1e7b0e07.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:56:22Z; reviewed SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd; current SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd; hash_changed=False. Reports=["reports/yaml_record_review/Aluminum_Chloride_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, NCIT parent, exact CAS/local SSSOM rows, CultureMech count, and aggregate pass, but the hydrate stoichiometry remains unverified while PubChem monohydrate-like chemistry is stored.

## Findings

### rec-f-ffabdfbc30a7e360: Historical review coverage and residual narrative: Aluminum_Chloride_Hydrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d6cbcbac1e7b0e07.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:56:22Z; reviewed SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd; current SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd; hash_changed=False. Reports=["reports/yaml_record_review/Aluminum_Chloride_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, NCIT parent, exact CAS/local SSSOM rows, CultureMech count, and aggregate pass, but the hydrate stoichiometry remains unverified while PubChem monohydrate-like chemistry is stored.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b99c130ba2d51187 | data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[478],"raw_equal":true},"docs_rows":[{"identifier":"cas:10124-27-3","line":480,"mapping_status":"MAPPED","ontology_id":"NCIT:C83530","preferred_term":"Aluminum chloride hydrate"}],"identifier":"cas:10124-27-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":28,"edge_count":28,"occurrences":28},"occurrence_statistics":{"media_count":28,"total_occurrences":28},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C83530","ontology_label":"Aluminum Chloride","ontology_source":"NCIT"},"preferred_term":"Aluminum chloride hydrate","sssom_rows":[{"data_row":345,"object_id":"NCIT:C83530","object_label":"Aluminum Chloride","predicate_id":"skos:broadMatch"},{"data_row":346,"object_id":"cas:10124-27-3","object_label":"Aluminum chloride hydrate","predicate_id":"skos:exactMatch"},{"data_row":347,"object_id":"kgmicrobe.compound:aluminum_chloride_hydrate","object_label":"Aluminum chloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aluminum_Chloride_Hydrate","synonym_count":0} |
| ev-5302b20d0d4ac923 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [478] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c1b7d84680bb6e11 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Aluminum_Chloride_Hydrate; data-row positions=[345,346,347] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":345,"object_id":"NCIT:C83530","object_label":"Aluminum Chloride","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":346,"object_id":"cas:10124-27-3","object_label":"Aluminum chloride hydrate","other":"CAS:10124-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":347,"object_id":"kgmicrobe.compound:aluminum_chloride_hydrate","object_label":"Aluminum chloride hydrate","other":"CAS:10124-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-866ec367e1569033 | docs/data/mapped_ingredients.csv; CSV lines=[480] | supports | Published identity and count rows inspected: [{"identifier":"cas:10124-27-3","line":480,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"28","ontology_id":"NCIT:C83530","preferred_term":"Aluminum chloride hydrate","total_occurrences":"28"}] |
| ev-9ada88d2b77343df | reports/yaml_record_review/Aluminum_Chloride_Hydrate.md; &#96;data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:40; Completeness:61; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-996ee1c8b6258c1f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[245] | context_only | [{"current_record_sha256":"fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd","finding_id":"SEM:f2a848c67af968e4d994","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-aluminum-chloride-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Aluminum_Chloride_Hydrate (data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml)'
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
summary: Per-record structured review for Aluminum_Chloride_Hydrate (data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml,
  record-d6cbcbac1e7b0e07, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
    sha256: fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd
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
  - path: reports/yaml_record_review/Aluminum_Chloride_Hydrate.md
    sha256: 8addd9196ada057a85e02bf0376f368be3330613f372d9935c2992d1257dd0a9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d6cbcbac1e7b0e07
  path: data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
  label: Aluminum_Chloride_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d6cbcbac1e7b0e07
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d6cbcbac1e7b0e07
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d6cbcbac1e7b0e07
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d6cbcbac1e7b0e07
evidence:
- evidence_id: ev-b99c130ba2d51187
  kind: record_content
  reference: data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[478],"raw_equal":true},"docs_rows":[{"identifier":"cas:10124-27-3","line":480,"mapping_status":"MAPPED","ontology_id":"NCIT:C83530","preferred_term":"Aluminum
    chloride hydrate"}],"identifier":"cas:10124-27-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":28,"edge_count":28,"occurrences":28},"occurrence_statistics":{"media_count":28,"total_occurrences":28},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C83530","ontology_label":"Aluminum
    Chloride","ontology_source":"NCIT"},"preferred_term":"Aluminum chloride hydrate","sssom_rows":[{"data_row":345,"object_id":"NCIT:C83530","object_label":"Aluminum
    Chloride","predicate_id":"skos:broadMatch"},{"data_row":346,"object_id":"cas:10124-27-3","object_label":"Aluminum
    chloride hydrate","predicate_id":"skos:exactMatch"},{"data_row":347,"object_id":"kgmicrobe.compound:aluminum_chloride_hydrate","object_label":"Aluminum
    chloride hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aluminum_Chloride_Hydrate","synonym_count":0}'
  snapshot_sha256: fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd
- evidence_id: ev-5302b20d0d4ac923
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [478]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c1b7d84680bb6e11
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Aluminum_Chloride_Hydrate; data-row positions=[345,346,347]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":345,"object_id":"NCIT:C83530","object_label":"Aluminum
    Chloride","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":346,"object_id":"cas:10124-27-3","object_label":"Aluminum
    chloride hydrate","other":"CAS:10124-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":347,"object_id":"kgmicrobe.compound:aluminum_chloride_hydrate","object_label":"Aluminum
    chloride hydrate","other":"CAS:10124-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Aluminum_Chloride_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-866ec367e1569033
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[480]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:10124-27-3","line":480,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"28","ontology_id":"NCIT:C83530","preferred_term":"Aluminum
    chloride hydrate","total_occurrences":"28"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9ada88d2b77343df
  kind: prior_review
  reference: reports/yaml_record_review/Aluminum_Chloride_Hydrate.md
  locator: '`data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml`:2; Verdict:4;
    Identity:12; Validation:25; Evidence:40; Completeness:61; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8addd9196ada057a85e02bf0376f368be3330613f372d9935c2992d1257dd0a9
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml`,\
    \ either confirm\n  the exact hydrate stoichiometry from the CultureBotHT/supplier\
    \ source and\n  update the preferred term plus chemistry accordingly, or qualify/clear\
    \ the\n  formula so the CAS hydrate record does not overstate a verified monohydrate.\n\
    - Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\
    \ `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-996ee1c8b6258c1f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[245]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd","finding_id":"SEM:f2a848c67af968e4d994","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-44c9dcf23837413d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d6cbcbac1e7b0e07
  evidence_ids:
  - ev-b99c130ba2d51187
  - ev-5302b20d0d4ac923
  - ev-c1b7d84680bb6e11
  - ev-866ec367e1569033
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5cb9c9e89ca11ae6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d6cbcbac1e7b0e07
  evidence_ids:
  - ev-9ada88d2b77343df
  - ev-b99c130ba2d51187
  - ev-996ee1c8b6258c1f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:56:22Z;
    reviewed SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd;
    current SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd;
    hash_changed=False. Reports=["reports/yaml_record_review/Aluminum_Chloride_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, NCIT parent, exact CAS/local SSSOM rows, CultureMech count,
    and aggregate pass, but the hydrate stoichiometry remains unverified while PubChem
    monohydrate-like chemistry is stored.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9ada88d2b77343df
    - ev-b99c130ba2d51187
  - name: legacy-native-ids
    value: '["SEM:f2a848c67af968e4d994"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b99c130ba2d51187
    - ev-9ada88d2b77343df
    - ev-996ee1c8b6258c1f
findings:
- finding_id: rec-f-ffabdfbc30a7e360
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d6cbcbac1e7b0e07
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Aluminum_Chloride_Hydrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:56:22Z;
    reviewed SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd;
    current SHA-256=fe6deba3a77e252c461982061ff75ded9b47f5be3a90632981ecdbd745dc16bd;
    hash_changed=False. Reports=["reports/yaml_record_review/Aluminum_Chloride_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, NCIT parent, exact CAS/local SSSOM rows, CultureMech count,
    and aggregate pass, but the hydrate stoichiometry remains unverified while PubChem
    monohydrate-like chemistry is stored.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d6cbcbac1e7b0e07
  evidence_ids:
  - ev-9ada88d2b77343df
  - ev-b99c130ba2d51187
  - ev-996ee1c8b6258c1f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml
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
