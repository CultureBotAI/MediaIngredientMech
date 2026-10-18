# Per-record structured review: Potassium_5-ketogluconate (data/ingredients/mapped/Potassium_5-ketogluconate.yaml)

- Review: 20261017T083000Z-potassium-5-ketogluconate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Potassium_5-ketogluconate (data/ingredients/mapped/Potassium_5-ketogluconate.yaml, record-d118b657fbdb27dc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Potassium_5-ketogluconate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Potassium_5-ketogluconate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d118b657fbdb27dc | data/ingredients/mapped/Potassium_5-ketogluconate.yaml | maintained | Potassium_5-ketogluconate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d118b657fbdb27dc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d118b657fbdb27dc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d118b657fbdb27dc | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d118b657fbdb27dc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d118b657fbdb27dc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z; reviewed SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c; current SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_5-ketogluconate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local salt row shape passes, but the 5-keto and 5-dehydro records duplicate the same active salt identity.

## Findings

### rec-f-43ad2185763132e7: Historical review coverage and residual narrative: Potassium_5-ketogluconate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d118b657fbdb27dc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z; reviewed SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c; current SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_5-ketogluconate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local salt row shape passes, but the 5-keto and 5-dehydro records duplicate the same active salt identity.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ee8ae35e56705039 | data/ingredients/mapped/Potassium_5-ketogluconate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[199],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","line":201,"mapping_status":"MAPPED","ontology_id":"CHEBI:58143","preferred_term":"Potassium 5-ketogluconate"}],"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":47,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:58143","ontology_label":"5-dehydro-D-gluconate","ontology_source":"CHEBI"},"preferred_term":"Potassium 5-ketogluconate","sssom_rows":[{"data_row":2312,"object_id":"CHEBI:58143","object_label":"5-dehydro-D-gluconate","predicate_id":"skos:broadMatch"},{"data_row":2313,"object_id":"kgmicrobe.compound:potassium_5-ketogluconate","object_label":"Potassium 5-ketogluconate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_5-ketogluconate","synonym_count":1} |
| ev-abcd3308d16d3727 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [199] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-536e32e67a348086 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_5-ketogluconate; data-row positions=[2312,2313] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2312,"object_id":"CHEBI:58143","object_label":"5-dehydro-D-gluconate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_5-ketogluconate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2313,"object_id":"kgmicrobe.compound:potassium_5-ketogluconate","object_label":"Potassium 5-ketogluconate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_5-ketogluconate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-72c8fb2f8fe497a3 | docs/data/mapped_ingredients.csv; CSV lines=[201] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","line":201,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:58143","preferred_term":"Potassium 5-ketogluconate","total_occurrences":"0"}] |
| ev-e79c343aca7e1cff | reports/yaml_record_review/Potassium_5-ketogluconate.md; &#96;data/ingredients/mapped/Potassium_5-ketogluconate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-03d7c7c494362721 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1134] | context_only | [{"current_record_sha256":"1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c","finding_id":"SEM:a7859f069cd6fc349d50","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-potassium-5-ketogluconate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Potassium_5-ketogluconate (data/ingredients/mapped/Potassium_5-ketogluconate.yaml)'
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
summary: Per-record structured review for Potassium_5-ketogluconate (data/ingredients/mapped/Potassium_5-ketogluconate.yaml,
  record-d118b657fbdb27dc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Potassium_5-ketogluconate.yaml
    sha256: 1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Potassium_5-ketogluconate.md
    sha256: ff04be649e41a6fb466a15ad6fd6fab87802c1871e7dff43e662d5cd653065ea
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d118b657fbdb27dc
  path: data/ingredients/mapped/Potassium_5-ketogluconate.yaml
  label: Potassium_5-ketogluconate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_5-ketogluconate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Potassium_5-ketogluconate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Potassium_5-ketogluconate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d118b657fbdb27dc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d118b657fbdb27dc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d118b657fbdb27dc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d118b657fbdb27dc
evidence:
- evidence_id: ev-ee8ae35e56705039
  kind: record_content
  reference: data/ingredients/mapped/Potassium_5-ketogluconate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[199],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","line":201,"mapping_status":"MAPPED","ontology_id":"CHEBI:58143","preferred_term":"Potassium
    5-ketogluconate"}],"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":47,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:58143","ontology_label":"5-dehydro-D-gluconate","ontology_source":"CHEBI"},"preferred_term":"Potassium
    5-ketogluconate","sssom_rows":[{"data_row":2312,"object_id":"CHEBI:58143","object_label":"5-dehydro-D-gluconate","predicate_id":"skos:broadMatch"},{"data_row":2313,"object_id":"kgmicrobe.compound:potassium_5-ketogluconate","object_label":"Potassium
    5-ketogluconate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_5-ketogluconate","synonym_count":1}'
  snapshot_sha256: 1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c
- evidence_id: ev-abcd3308d16d3727
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [199]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-536e32e67a348086
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_5-ketogluconate; data-row positions=[2312,2313]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2312,"object_id":"CHEBI:58143","object_label":"5-dehydro-D-gluconate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_5-ketogluconate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2313,"object_id":"kgmicrobe.compound:potassium_5-ketogluconate","object_label":"Potassium
    5-ketogluconate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_5-ketogluconate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-72c8fb2f8fe497a3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[201]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:potassium_5-ketogluconate","line":201,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:58143","preferred_term":"Potassium
    5-ketogluconate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e79c343aca7e1cff
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_5-ketogluconate.md
  locator: '`data/ingredients/mapped/Potassium_5-ketogluconate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ff04be649e41a6fb466a15ad6fd6fab87802c1871e7dff43e662d5cd653065ea
- evidence_id: ev-03d7c7c494362721
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1134]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c","finding_id":"SEM:a7859f069cd6fc349d50","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-06582af6153572f2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d118b657fbdb27dc
  evidence_ids:
  - ev-ee8ae35e56705039
  - ev-abcd3308d16d3727
  - ev-536e32e67a348086
  - ev-72c8fb2f8fe497a3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-40f05cb1c86e5951
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d118b657fbdb27dc
  evidence_ids:
  - ev-e79c343aca7e1cff
  - ev-ee8ae35e56705039
  - ev-03d7c7c494362721
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z;
    reviewed SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c;
    current SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_5-ketogluconate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    salt row shape passes, but the 5-keto and 5-dehydro records duplicate the same
    active salt identity.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e79c343aca7e1cff
    - ev-ee8ae35e56705039
  - name: legacy-native-ids
    value: '["SEM:a7859f069cd6fc349d50"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ee8ae35e56705039
    - ev-e79c343aca7e1cff
    - ev-03d7c7c494362721
findings:
- finding_id: rec-f-43ad2185763132e7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d118b657fbdb27dc
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Potassium_5-ketogluconate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z;
    reviewed SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c;
    current SHA-256=1245f80cfb84e59c6a973a2af632e1833763ba446e6627089ee51e8ecd4f429c;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_5-ketogluconate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    salt row shape passes, but the 5-keto and 5-dehydro records duplicate the same
    active salt identity.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d118b657fbdb27dc
  evidence_ids:
  - ev-e79c343aca7e1cff
  - ev-ee8ae35e56705039
  - ev-03d7c7c494362721
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_5-ketogluconate.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
