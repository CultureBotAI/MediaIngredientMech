# Per-record structured review: Fibrin (data/ingredients/mapped/Fibrin.yaml)

- Review: 20261017T083000Z-fibrin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fibrin (data/ingredients/mapped/Fibrin.yaml, record-23f59979ef5299db, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fibrin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fibrin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-23f59979ef5299db | data/ingredients/mapped/Fibrin.yaml | maintained | Fibrin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-23f59979ef5299db | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-23f59979ef5299db | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-23f59979ef5299db | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-23f59979ef5299db.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-23f59979ef5299db.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z; reviewed SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1; current SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1; hash_changed=False. Reports=["reports/yaml_record_review/Fibrin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI fibrin identity and final SSSOM row pass, but copied C5H11N3O2 structure fields do not describe fibrin.

## Findings

### rec-f-33d2e89bdcd1754e: Historical review coverage and residual narrative: Fibrin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-23f59979ef5299db.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z; reviewed SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1; current SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1; hash_changed=False. Reports=["reports/yaml_record_review/Fibrin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI fibrin identity and final SSSOM row pass, but copied C5H11N3O2 structure fields do not describe fibrin.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9bd5fe38f6115c41 | data/ingredients/mapped/Fibrin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2269],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5054","line":2271,"mapping_status":"MAPPED","ontology_id":"CHEBI:5054","preferred_term":"Fibrin"}],"identifier":"CHEBI:5054","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:5054","ontology_label":"Fibrin","ontology_source":"CHEBI"},"preferred_term":"Fibrin","sssom_rows":[{"data_row":1206,"object_id":"CHEBI:5054","object_label":"Fibrin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fibrin","synonym_count":0} |
| ev-39f62812b820aee1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2269] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-632ca4f2c08b8c49 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fibrin; data-row positions=[1206] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1206,"object_id":"CHEBI:5054","object_label":"Fibrin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fibrin","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-294a1161aee0599c | docs/data/mapped_ingredients.csv; CSV lines=[2271] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:5054","line":2271,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5054","preferred_term":"Fibrin","total_occurrences":"0"}] |
| ev-41ea86406c0244ef | reports/yaml_record_review/Fibrin.md; &#96;data/ingredients/mapped/Fibrin.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:36; Completeness:56; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-726c4ffc75e5afdf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[613] | context_only | [{"current_record_sha256":"11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1","finding_id":"SEM:93e2a072928dcd8597c4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fibrin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fibrin (data/ingredients/mapped/Fibrin.yaml)'
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
summary: Per-record structured review for Fibrin (data/ingredients/mapped/Fibrin.yaml,
  record-23f59979ef5299db, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fibrin.yaml
    sha256: 11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1
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
  - path: reports/yaml_record_review/Fibrin.md
    sha256: 3b9a617e69f059191e1ba5e3d76f7b001207a465c03abb0ad772c73bdaacf32a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-23f59979ef5299db
  path: data/ingredients/mapped/Fibrin.yaml
  label: Fibrin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fibrin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fibrin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fibrin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-23f59979ef5299db
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-23f59979ef5299db
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-23f59979ef5299db
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-23f59979ef5299db
evidence:
- evidence_id: ev-9bd5fe38f6115c41
  kind: record_content
  reference: data/ingredients/mapped/Fibrin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2269],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5054","line":2271,"mapping_status":"MAPPED","ontology_id":"CHEBI:5054","preferred_term":"Fibrin"}],"identifier":"CHEBI:5054","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:5054","ontology_label":"Fibrin","ontology_source":"CHEBI"},"preferred_term":"Fibrin","sssom_rows":[{"data_row":1206,"object_id":"CHEBI:5054","object_label":"Fibrin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fibrin","synonym_count":0}'
  snapshot_sha256: 11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1
- evidence_id: ev-39f62812b820aee1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2269]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-632ca4f2c08b8c49
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fibrin; data-row positions=[1206]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1206,"object_id":"CHEBI:5054","object_label":"Fibrin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fibrin","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-294a1161aee0599c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2271]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:5054","line":2271,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5054","preferred_term":"Fibrin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-41ea86406c0244ef
  kind: prior_review
  reference: reports/yaml_record_review/Fibrin.md
  locator: '`data/ingredients/mapped/Fibrin.yaml`:2; Verdict:4; Identity:11; Validation:26;
    Evidence:36; Completeness:56; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3b9a617e69f059191e1ba5e3d76f7b001207a465c03abb0ad772c73bdaacf32a
  quote: "Recommended Edits:\n- Major: review `data/ingredients/mapped/Fibrin.yaml`\
    \ as a protein/polymer\n  ingredient and remove the `C5H11N3O2` `chemical_properties`\
    \ fields unless a\n  source can justify them for fibrin; sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ regenerate products if structure\n  fields feed them, and rerun strict validation\
    \ plus the final SSSOM invariant\n  gates."
- evidence_id: ev-726c4ffc75e5afdf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[613]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1","finding_id":"SEM:93e2a072928dcd8597c4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6f4668b800802bdd
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-23f59979ef5299db
  evidence_ids:
  - ev-9bd5fe38f6115c41
  - ev-39f62812b820aee1
  - ev-632ca4f2c08b8c49
  - ev-294a1161aee0599c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5b320340eb3ba8b5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-23f59979ef5299db
  evidence_ids:
  - ev-41ea86406c0244ef
  - ev-9bd5fe38f6115c41
  - ev-726c4ffc75e5afdf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z;
    reviewed SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1;
    current SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1;
    hash_changed=False. Reports=["reports/yaml_record_review/Fibrin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI fibrin
    identity and final SSSOM row pass, but copied C5H11N3O2 structure fields do not
    describe fibrin.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-41ea86406c0244ef
    - ev-9bd5fe38f6115c41
  - name: legacy-native-ids
    value: '["SEM:93e2a072928dcd8597c4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9bd5fe38f6115c41
    - ev-41ea86406c0244ef
    - ev-726c4ffc75e5afdf
findings:
- finding_id: rec-f-33d2e89bdcd1754e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-23f59979ef5299db
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Fibrin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z;
    reviewed SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1;
    current SHA-256=11de03014afdf4b66f034f8aee218db0df6f7e84037c491fcea85c982ef987c1;
    hash_changed=False. Reports=["reports/yaml_record_review/Fibrin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI fibrin
    identity and final SSSOM row pass, but copied C5H11N3O2 structure fields do not
    describe fibrin.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-23f59979ef5299db
  evidence_ids:
  - ev-41ea86406c0244ef
  - ev-9bd5fe38f6115c41
  - ev-726c4ffc75e5afdf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fibrin.yaml
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
