# Per-record structured review: Substrate (data/ingredients/mapped/Substrate.yaml)

- Review: 20261017T083000Z-substrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Substrate (data/ingredients/mapped/Substrate.yaml, record-19bb337b34939ab2, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Substrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Substrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-19bb337b34939ab2 | data/ingredients/mapped/Substrate.yaml | maintained | Substrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-19bb337b34939ab2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-19bb337b34939ab2 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-19bb337b34939ab2 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-19bb337b34939ab2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-19bb337b34939ab2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z; reviewed SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70; current SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70; hash_changed=False. Reports=["reports/yaml_record_review/Substrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The NCIT:C120264 label resolves, but a role-like substrate placeholder is modeled as a SINGLE_INGREDIENT.

## Findings

### rec-f-e549752647110900: Historical review coverage and residual narrative: Substrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-19bb337b34939ab2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z; reviewed SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70; current SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70; hash_changed=False. Reports=["reports/yaml_record_review/Substrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The NCIT:C120264 label resolves, but a role-like substrate placeholder is modeled as a SINGLE_INGREDIENT.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1101ede8e5eeeb29 | data/ingredients/mapped/Substrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C120264","line":1907,"mapping_status":"MAPPED","ontology_id":"NCIT:C120264","preferred_term":"Substrate"}],"identifier":"NCIT:C120264","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C120264","ontology_label":"Substrate","ontology_source":"NCIT"},"preferred_term":"Substrate","sssom_rows":[{"data_row":2658,"object_id":"NCIT:C120264","object_label":"Substrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Substrate","synonym_count":0} |
| ev-d0b199c2f6947fd8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1905] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0457726e196cb1d6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Substrate; data-row positions=[2658] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2658,"object_id":"NCIT:C120264","object_label":"Substrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Substrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f3fd2820803880a5 | docs/data/mapped_ingredients.csv; CSV lines=[1907] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C120264","line":1907,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"NCIT:C120264","preferred_term":"Substrate","total_occurrences":"5"}] |
| ev-6724a53b5e75fe7c | reports/yaml_record_review/Substrate.md; &#96;data/ingredients/mapped/Substrate.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:28; Completeness:38; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c248bcf2544fb8fc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1253] | context_only | [{"current_record_sha256":"4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70","finding_id":"SEM:1885d0f3aae52595506d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-substrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Substrate (data/ingredients/mapped/Substrate.yaml)'
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
summary: Per-record structured review for Substrate (data/ingredients/mapped/Substrate.yaml,
  record-19bb337b34939ab2, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Substrate.yaml
    sha256: 4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Substrate.md
    sha256: 518b6d669475685a8d05a6217b7eab4e09f8acc72a5aac4734973500c77713a1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-19bb337b34939ab2
  path: data/ingredients/mapped/Substrate.yaml
  label: Substrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Substrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Substrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Substrate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-19bb337b34939ab2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-19bb337b34939ab2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-19bb337b34939ab2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-19bb337b34939ab2
evidence:
- evidence_id: ev-1101ede8e5eeeb29
  kind: record_content
  reference: data/ingredients/mapped/Substrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1905],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C120264","line":1907,"mapping_status":"MAPPED","ontology_id":"NCIT:C120264","preferred_term":"Substrate"}],"identifier":"NCIT:C120264","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C120264","ontology_label":"Substrate","ontology_source":"NCIT"},"preferred_term":"Substrate","sssom_rows":[{"data_row":2658,"object_id":"NCIT:C120264","object_label":"Substrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Substrate","synonym_count":0}'
  snapshot_sha256: 4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70
- evidence_id: ev-d0b199c2f6947fd8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1905]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0457726e196cb1d6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Substrate; data-row positions=[2658]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2658,"object_id":"NCIT:C120264","object_label":"Substrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Substrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f3fd2820803880a5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1907]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C120264","line":1907,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"NCIT:C120264","preferred_term":"Substrate","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6724a53b5e75fe7c
  kind: prior_review
  reference: reports/yaml_record_review/Substrate.md
  locator: '`data/ingredients/mapped/Substrate.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:28; Completeness:38; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 518b6d669475685a8d05a6217b7eab4e09f8acc72a5aac4734973500c77713a1
  quote: "Recommended Edits:\n- Major: inspect the five CultureMech `Substrate` occurrences\
    \ behind\n  `NCIT:C120264` and either split them to concrete ingredients, reject\
    \ the\n  placeholder if it is not a supplied ingredient, or remodel it as a deliberate\n\
    \  generic class instead of `ingredient_type: SINGLE_INGREDIENT`."
- evidence_id: ev-c248bcf2544fb8fc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1253]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70","finding_id":"SEM:1885d0f3aae52595506d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3054c5ae4533ef8c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-19bb337b34939ab2
  evidence_ids:
  - ev-1101ede8e5eeeb29
  - ev-d0b199c2f6947fd8
  - ev-0457726e196cb1d6
  - ev-f3fd2820803880a5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6629ddc79bad7519
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-19bb337b34939ab2
  evidence_ids:
  - ev-6724a53b5e75fe7c
  - ev-1101ede8e5eeeb29
  - ev-c248bcf2544fb8fc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z;
    reviewed SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70;
    current SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70;
    hash_changed=False. Reports=["reports/yaml_record_review/Substrate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The NCIT:C120264
    label resolves, but a role-like substrate placeholder is modeled as a SINGLE_INGREDIENT.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6724a53b5e75fe7c
    - ev-1101ede8e5eeeb29
  - name: legacy-native-ids
    value: '["SEM:1885d0f3aae52595506d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1101ede8e5eeeb29
    - ev-6724a53b5e75fe7c
    - ev-c248bcf2544fb8fc
findings:
- finding_id: rec-f-e549752647110900
  issue_key: mim-reconciliation-historical-review-coverage-and-r-19bb337b34939ab2
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Substrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:48:23Z;
    reviewed SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70;
    current SHA-256=4b0134fa9b74a3528e74af03437654fe792727760d4c695930b46dccca9f5f70;
    hash_changed=False. Reports=["reports/yaml_record_review/Substrate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The NCIT:C120264
    label resolves, but a role-like substrate placeholder is modeled as a SINGLE_INGREDIENT.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-19bb337b34939ab2
  evidence_ids:
  - ev-6724a53b5e75fe7c
  - ev-1101ede8e5eeeb29
  - ev-c248bcf2544fb8fc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Substrate.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
