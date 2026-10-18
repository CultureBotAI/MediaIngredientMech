# Per-record structured review: Vitamin_K1 (data/ingredients/mapped/Vitamin_K1.yaml)

- Review: 20261017T083000Z-vitamin-k1
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vitamin_K1 (data/ingredients/mapped/Vitamin_K1.yaml, record-f9ecdfe63885336a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vitamin_K1.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vitamin_K1.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f9ecdfe63885336a | data/ingredients/mapped/Vitamin_K1.yaml | maintained | Vitamin_K1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f9ecdfe63885336a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f9ecdfe63885336a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f9ecdfe63885336a | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f9ecdfe63885336a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f9ecdfe63885336a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z; reviewed SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a; current SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a; hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_K1.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The phylloquinone identity and source-backed vitamin role pass, but final SSSOM exports concentration-qualified Vitamin K1 as an exact other synonym.

## Findings

### rec-f-1a58d2eedca3aaa5: Historical review coverage and residual narrative: Vitamin_K1

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f9ecdfe63885336a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z; reviewed SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a; current SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a; hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_K1.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The phylloquinone identity and source-backed vitamin role pass, but final SSSOM exports concentration-qualified Vitamin K1 as an exact other synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-054386271cfd7931 | data/ingredients/mapped/Vitamin_K1.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18067","line":2049,"mapping_status":"MAPPED","ontology_id":"CHEBI:18067","preferred_term":"Vitamin K1"}],"identifier":"CHEBI:18067","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":127,"edge_count":127,"occurrences":127},"occurrence_statistics":{"media_count":127,"total_occurrences":127},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18067","ontology_label":"phylloquinone","ontology_source":"CHEBI"},"preferred_term":"Vitamin K1","sssom_rows":[{"data_row":2907,"object_id":"CHEBI:18067","object_label":"phylloquinone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_K1","synonym_count":28} |
| ev-2232dfaaaa945c5f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2047] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4086d9516cb5f669 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vitamin_K1; data-row positions=[2907] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2907,"object_id":"CHEBI:18067","object_label":"phylloquinone","other":"2-Methyl-3-(3,7,11,15-tetramethyl-2-hexadecenyl)-1,4-naphthalenedione&#124;2-Methyl-3-[(2E)-3,7,11,15-tetramethyl-2-hexadecenyl]naphthoquinone&#124;2-Methyl-3-phytyl-1,4-naphthochinon&#124;2-methyl-3-[(2E,7R,11R)-3,7,11,15-tetramethylhexadec-2-en-1-yl]naphthalene-1,4-dione&#124;2-methyl-3-phytyl-1,4-naphthoquinone&#124;3-phytylmenadione&#124;Mephyton&#124;Phyllochinon&#124;Phyllochinonum&#124;Phytonadionum&#124;Phytylmenadione&#124;alpha-phylloquinone&#124;fitomenadiona&#124;fitomenadione&#124;phytomenadione&#124;phytomenadionum&#124;phytonadione&#124;Vitamin K1 (1 mg/ml)&#124;CAS:84-80-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamin_K1","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e446b1acf158e0d1 | docs/data/mapped_ingredients.csv; CSV lines=[2049] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18067","line":2049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"127","ontology_id":"CHEBI:18067","preferred_term":"Vitamin K1","total_occurrences":"127"}] |
| ev-f93cee047aaadbb6 | reports/yaml_record_review/Vitamin_K1.md; &#96;data/ingredients/mapped/Vitamin_K1.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:38; Issues:50; Completeness:57; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7e56ccfd2a7f85c7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1338] | context_only | [{"current_record_sha256":"b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a","finding_id":"SEM:6a09b87994550976db09","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vitamin-k1
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vitamin_K1 (data/ingredients/mapped/Vitamin_K1.yaml)'
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
summary: Per-record structured review for Vitamin_K1 (data/ingredients/mapped/Vitamin_K1.yaml,
  record-f9ecdfe63885336a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vitamin_K1.yaml
    sha256: b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Vitamin_K1.md
    sha256: 97d3955452f785cd673a226e6609b8ee05110012b14646f4d2ac9f7cffae9543
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f9ecdfe63885336a
  path: data/ingredients/mapped/Vitamin_K1.yaml
  label: Vitamin_K1
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamin_K1.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vitamin_K1.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vitamin_K1.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f9ecdfe63885336a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f9ecdfe63885336a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f9ecdfe63885336a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f9ecdfe63885336a
evidence:
- evidence_id: ev-054386271cfd7931
  kind: record_content
  reference: data/ingredients/mapped/Vitamin_K1.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18067","line":2049,"mapping_status":"MAPPED","ontology_id":"CHEBI:18067","preferred_term":"Vitamin
    K1"}],"identifier":"CHEBI:18067","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":127,"edge_count":127,"occurrences":127},"occurrence_statistics":{"media_count":127,"total_occurrences":127},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18067","ontology_label":"phylloquinone","ontology_source":"CHEBI"},"preferred_term":"Vitamin
    K1","sssom_rows":[{"data_row":2907,"object_id":"CHEBI:18067","object_label":"phylloquinone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_K1","synonym_count":28}'
  snapshot_sha256: b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a
- evidence_id: ev-2232dfaaaa945c5f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2047]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4086d9516cb5f669
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vitamin_K1; data-row positions=[2907]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2907,"object_id":"CHEBI:18067","object_label":"phylloquinone","other":"2-Methyl-3-(3,7,11,15-tetramethyl-2-hexadecenyl)-1,4-naphthalenedione|2-Methyl-3-[(2E)-3,7,11,15-tetramethyl-2-hexadecenyl]naphthoquinone|2-Methyl-3-phytyl-1,4-naphthochinon|2-methyl-3-[(2E,7R,11R)-3,7,11,15-tetramethylhexadec-2-en-1-yl]naphthalene-1,4-dione|2-methyl-3-phytyl-1,4-naphthoquinone|3-phytylmenadione|Mephyton|Phyllochinon|Phyllochinonum|Phytonadionum|Phytylmenadione|alpha-phylloquinone|fitomenadiona|fitomenadione|phytomenadione|phytomenadionum|phytonadione|Vitamin
    K1 (1 mg/ml)|CAS:84-80-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamin_K1","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e446b1acf158e0d1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2049]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18067","line":2049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"127","ontology_id":"CHEBI:18067","preferred_term":"Vitamin
    K1","total_occurrences":"127"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f93cee047aaadbb6
  kind: prior_review
  reference: reports/yaml_record_review/Vitamin_K1.md
  locator: '`data/ingredients/mapped/Vitamin_K1.yaml`:2; Verdict:4; Identity:11; Validation:26;
    Evidence:38; Issues:50; Completeness:57; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 97d3955452f785cd673a226e6609b8ee05110012b14646f4d2ac9f7cffae9543
  quote: "Issues:\n- Major: the final exact `CHEBI:18067` row exports the concentration-qualified\n\
    \  recipe surface form `Vitamin K1 (1 mg/ml)` as an `other` synonym. That string\n\
    \  describes a specific stock concentration or recipe annotation, not a\n  synonymous\
    \ label for phylloquinone itself.\n\nRecommended Edits:\n- Remove `Vitamin K1\
    \ (1 mg/ml)` from the record's exported synonym set, either\n  by dropping the\
    \ stale raw alias or by teaching the final SSSOM export to\n  suppress concentration-qualified\
    \ CultureMech surface forms.\n- Rebuild SSSOM and rerun strict validation, LinkML\
    \ term validation, SSSOM\n  invariant validation, and the cross-record `other`\
    \ synonym audit."
- evidence_id: ev-7e56ccfd2a7f85c7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1338]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a","finding_id":"SEM:6a09b87994550976db09","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a629f4f3b1b4614d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f9ecdfe63885336a
  evidence_ids:
  - ev-054386271cfd7931
  - ev-2232dfaaaa945c5f
  - ev-4086d9516cb5f669
  - ev-e446b1acf158e0d1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7bfec9c0906bc51d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f9ecdfe63885336a
  evidence_ids:
  - ev-f93cee047aaadbb6
  - ev-054386271cfd7931
  - ev-7e56ccfd2a7f85c7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z;
    reviewed SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a;
    current SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a;
    hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_K1.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The phylloquinone
    identity and source-backed vitamin role pass, but final SSSOM exports concentration-qualified
    Vitamin K1 as an exact other synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f93cee047aaadbb6
    - ev-054386271cfd7931
  - name: legacy-native-ids
    value: '["SEM:6a09b87994550976db09"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-054386271cfd7931
    - ev-f93cee047aaadbb6
    - ev-7e56ccfd2a7f85c7
findings:
- finding_id: rec-f-1a58d2eedca3aaa5
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f9ecdfe63885336a
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Vitamin_K1'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z;
    reviewed SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a;
    current SHA-256=b1b4d7e83be0bbefa3d6100a34159db0c6806253cad60ee2c121be58357fb94a;
    hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_K1.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The phylloquinone
    identity and source-backed vitamin role pass, but final SSSOM exports concentration-qualified
    Vitamin K1 as an exact other synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f9ecdfe63885336a
  evidence_ids:
  - ev-f93cee047aaadbb6
  - ev-054386271cfd7931
  - ev-7e56ccfd2a7f85c7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamin_K1.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
