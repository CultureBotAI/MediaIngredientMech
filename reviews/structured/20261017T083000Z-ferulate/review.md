# Per-record structured review: Ferulate (data/ingredients/mapped/Ferulate.yaml)

- Review: 20261017T083000Z-ferulate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ferulate (data/ingredients/mapped/Ferulate.yaml, record-8add51589a350fc5, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ferulate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ferulate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8add51589a350fc5 | data/ingredients/mapped/Ferulate.yaml | maintained | Ferulate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8add51589a350fc5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8add51589a350fc5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8add51589a350fc5 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8add51589a350fc5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8add51589a350fc5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:19Z; reviewed SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; current SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050219Z-Ferulate.md","reports/yaml_record_review/Ferulate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Ferulate.md&#96; after the record changed from be67995f7cee8605f997dcfa2ce586c657c629145d4ff349dec3c6dc07ed7793 to 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-dc72ccdcf496dea0: Historical review coverage and residual narrative: Ferulate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8add51589a350fc5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:19Z; reviewed SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; current SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050219Z-Ferulate.md","reports/yaml_record_review/Ferulate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Ferulate.md&#96; after the record changed from be67995f7cee8605f997dcfa2ce586c657c629145d4ff349dec3c6dc07ed7793 to 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cd1ef198878af409 | data/ingredients/mapped/Ferulate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2652],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29749","line":2654,"mapping_status":"MAPPED","ontology_id":"CHEBI:29749","preferred_term":"Ferulate"}],"identifier":"CHEBI:29749","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:29749","ontology_label":"trans-ferulate","ontology_source":"CHEBI"},"preferred_term":"Ferulate","sssom_rows":[{"data_row":1196,"object_id":"CHEBI:29749","object_label":"trans-ferulate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferulate","synonym_count":1} |
| ev-9d44905c7084fbcd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2652] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-91e1babb8bded8b8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ferulate; data-row positions=[1196] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1196,"object_id":"CHEBI:29749","object_label":"trans-ferulate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferulate","validation_method":"manual:apply_312_batch2&#124;IDENTITY&#124;2026-09-22"}] |
| ev-a0dde25e6ca1f3ce | docs/data/mapped_ingredients.csv; CSV lines=[2654] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29749","line":2654,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29749","preferred_term":"Ferulate","total_occurrences":"0"}] |
| ev-f4d7406b2fdfea45 | reports/yaml_record_review/20261001T050219Z-Ferulate.md; YAML Record Review: Ferulate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e41e5a7e6894685f | reports/yaml_record_review/Ferulate.md; &#96;data/ingredients/mapped/Ferulate.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:30; Completeness:52; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dfee0324e88ee6b3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[605] | context_only | [{"current_record_sha256":"0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d","finding_id":"SEM:0dbedcfec49132543f07","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ferulate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ferulate (data/ingredients/mapped/Ferulate.yaml)'
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
summary: Per-record structured review for Ferulate (data/ingredients/mapped/Ferulate.yaml,
  record-8add51589a350fc5, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ferulate.yaml
    sha256: 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d
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
  - path: reports/yaml_record_review/20261001T050219Z-Ferulate.md
    sha256: 73cda769d46dbf3a0ac6b99c6a41d15ebc5836808339c670fdff073c03e6539b
    role: context
  - path: reports/yaml_record_review/Ferulate.md
    sha256: c535c5c736a27fa82a13b93503db36c7310dcfd2f18186ac59d52a8765492d75
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8add51589a350fc5
  path: data/ingredients/mapped/Ferulate.yaml
  label: Ferulate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferulate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ferulate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ferulate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8add51589a350fc5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8add51589a350fc5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8add51589a350fc5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8add51589a350fc5
evidence:
- evidence_id: ev-cd1ef198878af409
  kind: record_content
  reference: data/ingredients/mapped/Ferulate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2652],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29749","line":2654,"mapping_status":"MAPPED","ontology_id":"CHEBI:29749","preferred_term":"Ferulate"}],"identifier":"CHEBI:29749","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:29749","ontology_label":"trans-ferulate","ontology_source":"CHEBI"},"preferred_term":"Ferulate","sssom_rows":[{"data_row":1196,"object_id":"CHEBI:29749","object_label":"trans-ferulate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferulate","synonym_count":1}'
  snapshot_sha256: 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d
- evidence_id: ev-9d44905c7084fbcd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2652]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-91e1babb8bded8b8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ferulate; data-row positions=[1196]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1196,"object_id":"CHEBI:29749","object_label":"trans-ferulate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferulate","validation_method":"manual:apply_312_batch2|IDENTITY|2026-09-22"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a0dde25e6ca1f3ce
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2654]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29749","line":2654,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29749","preferred_term":"Ferulate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f4d7406b2fdfea45
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050219Z-Ferulate.md
  locator: 'YAML Record Review: Ferulate:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 73cda769d46dbf3a0ac6b99c6a41d15ebc5836808339c670fdff073c03e6539b
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Ferulate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The record
    maps ferulate to neutral trans-ferulic acid even though CHEBI has a trans-ferulate
    anion term.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Ferulate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Ferulate.yaml`,
    `just validate-terms data/ingredients/mapped/Ferulate.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-e41e5a7e6894685f
  kind: prior_review
  reference: reports/yaml_record_review/Ferulate.md
  locator: '`data/ingredients/mapped/Ferulate.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:30; Completeness:52; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c535c5c736a27fa82a13b93503db36c7310dcfd2f18186ac59d52a8765492d75
  quote: "Recommended Edits:\n- Major: remap `data/ingredients/mapped/Ferulate.yaml`\
    \ from `CHEBI:17620`\n  `trans-ferulic acid` to `CHEBI:29749` `trans-ferulate`,\
    \ update the evidence\n  that currently says no ChEBI anion term exists, sync\n\
    \  `data/curated/mapped_ingredients.yaml`, regenerate\n  `mappings/ingredient_mappings.sssom.tsv`,\
    \ and rerun strict validation plus\n  the final SSSOM invariant gates."
- evidence_id: ev-dfee0324e88ee6b3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[605]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d","finding_id":"SEM:0dbedcfec49132543f07","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1abd3b7c4028f838
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8add51589a350fc5
  evidence_ids:
  - ev-cd1ef198878af409
  - ev-9d44905c7084fbcd
  - ev-91e1babb8bded8b8
  - ev-a0dde25e6ca1f3ce
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6a43f45b356e7ec1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8add51589a350fc5
  evidence_ids:
  - ev-f4d7406b2fdfea45
  - ev-e41e5a7e6894685f
  - ev-cd1ef198878af409
  - ev-dfee0324e88ee6b3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:19Z;
    reviewed SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d;
    current SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050219Z-Ferulate.md","reports/yaml_record_review/Ferulate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Ferulate.md` after the record changed from be67995f7cee8605f997dcfa2ce586c657c629145d4ff349dec3c6dc07ed7793
    to 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f4d7406b2fdfea45
    - ev-e41e5a7e6894685f
    - ev-cd1ef198878af409
  - name: legacy-native-ids
    value: '["SEM:0dbedcfec49132543f07"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cd1ef198878af409
    - ev-f4d7406b2fdfea45
    - ev-e41e5a7e6894685f
    - ev-dfee0324e88ee6b3
findings:
- finding_id: rec-f-dc72ccdcf496dea0
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8add51589a350fc5
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ferulate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:19Z;
    reviewed SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d;
    current SHA-256=0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050219Z-Ferulate.md","reports/yaml_record_review/Ferulate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Ferulate.md` after the record changed from be67995f7cee8605f997dcfa2ce586c657c629145d4ff349dec3c6dc07ed7793
    to 0020d82932826d6ce58c30d0f9aa88e8bb43e646b20f02b13512ca083dd1071d; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8add51589a350fc5
  evidence_ids:
  - ev-f4d7406b2fdfea45
  - ev-e41e5a7e6894685f
  - ev-cd1ef198878af409
  - ev-dfee0324e88ee6b3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferulate.yaml
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
