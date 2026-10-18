# Per-record structured review: O-nitrophenyl-beta-D-galactopyranosid (data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml)

- Review: 20261017T083000Z-o-nitrophenyl-beta-d-galactopyranosid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for O-nitrophenyl-beta-D-galactopyranosid (data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml, record-05defdd1a6e248db, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-05defdd1a6e248db | data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml | maintained | O-nitrophenyl-beta-D-galactopyranosid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-05defdd1a6e248db | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-05defdd1a6e248db | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-05defdd1a6e248db | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-05defdd1a6e248db.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-05defdd1a6e248db.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T07:26:28Z; reviewed SHA-256=aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069; current SHA-256=aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069; hash_changed=False. Reports=["reports/yaml_record_review/O-nitrophenyl-beta-D-galactopyranosid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-backed exact CHEBI:90144 ONPG identity and final row pass.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-05defdd1a6e248db.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-f557f5e3adbf238a: Legacy field-missing triage rows: O-nitrophenyl-beta-D-galactopyranosid

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-05defdd1a6e248db.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1cff5f98d7cafded | data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[209],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:90144","line":211,"mapping_status":"MAPPED","ontology_id":"CHEBI:90144","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid"}],"identifier":"CHEBI:90144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":8,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production&#124;BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:90144","ontology_label":"2-nitrophenyl beta-D-galactoside","ontology_source":"CHEBI"},"preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","sssom_rows":[{"data_row":2130,"object_id":"CHEBI:90144","object_label":"2-nitrophenyl beta-D-galactoside","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:O-nitrophenyl-beta-D-galactopyranosid","synonym_count":2} |
| ev-125e769ed2b623cb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [209] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3969640b2a281d22 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:O-nitrophenyl-beta-D-galactopyranosid; data-row positions=[2130] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2130,"object_id":"CHEBI:90144","object_label":"2-nitrophenyl beta-D-galactoside","other":"O-nitrophenyl-beta-D-galactopyranoside","predicate_id":"skos:exactMatch","subject_id":"MIM:O-nitrophenyl-beta-D-galactopyranosid","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-cf29735c95bbbb3e | docs/data/mapped_ingredients.csv; CSV lines=[211] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:90144","line":211,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:90144","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","total_occurrences":"0"}] |
| ev-18ca514ccfadc18d | reports/yaml_record_review/O-nitrophenyl-beta-D-galactopyranosid.md; &#96;data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml&#96;:2; Verdict:4; Identity:9; Validation:24; Evidence:31; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e7a43eae407a88e7 | mappings/record_research_validation.tsv; lines=[879,880] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"yes","evidence":"Available and unpopulated: &#96;C12H15NO8&#96;, charge 0, avg mass 301.251, monoisotopic 301.07977, InChIKey &#96;KUWPCJHYPSUOFW-YBXAARCKSA-N&#96; (\u00a73)","identifier":"CHEBI:90144","kind":"FIELD_MISSING","lane":"claude","line":879,"mapping_quality":"SYNONYM_MATCH","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:90144","slug":"O-nitrophenyl-beta-D-galactopyranosid","status_dir":"mapped"}},{"field":"chemical_properties","row":{"detail":"'chemical_properties.cas_rn' is unset; report supplies a value","documented_rationale":"yes","evidence":"369-07-3** \u2014 verified to this exact structure by three independent routes and check-digit-valid (\u00a73)","identifier":"CHEBI:90144","kind":"FIELD_MISSING","lane":"claude","line":880,"mapping_quality":"SYNONYM_MATCH","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:90144","slug":"O-nitrophenyl-beta-D-galactopyranosid","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-o-nitrophenyl-beta-d-galactopyranosid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: O-nitrophenyl-beta-D-galactopyranosid (data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml)'
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
summary: Per-record structured review for O-nitrophenyl-beta-D-galactopyranosid (data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml,
  record-05defdd1a6e248db, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
    sha256: aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/O-nitrophenyl-beta-D-galactopyranosid.md
    sha256: ac8ae542c7a179338d86f7098a34df9918ac477d5447491f1e3984701d3bef24
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-05defdd1a6e248db
  path: data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
  label: O-nitrophenyl-beta-D-galactopyranosid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-05defdd1a6e248db
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-05defdd1a6e248db
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-05defdd1a6e248db
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-05defdd1a6e248db
evidence:
- evidence_id: ev-1cff5f98d7cafded
  kind: record_content
  reference: data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[209],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:90144","line":211,"mapping_status":"MAPPED","ontology_id":"CHEBI:90144","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid"}],"identifier":"CHEBI:90144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":8,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production|BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:90144","ontology_label":"2-nitrophenyl
    beta-D-galactoside","ontology_source":"CHEBI"},"preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","sssom_rows":[{"data_row":2130,"object_id":"CHEBI:90144","object_label":"2-nitrophenyl
    beta-D-galactoside","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:O-nitrophenyl-beta-D-galactopyranosid","synonym_count":2}'
  snapshot_sha256: aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069
- evidence_id: ev-125e769ed2b623cb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [209]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3969640b2a281d22
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:O-nitrophenyl-beta-D-galactopyranosid; data-row positions=[2130]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2130,"object_id":"CHEBI:90144","object_label":"2-nitrophenyl
    beta-D-galactoside","other":"O-nitrophenyl-beta-D-galactopyranoside","predicate_id":"skos:exactMatch","subject_id":"MIM:O-nitrophenyl-beta-D-galactopyranosid","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cf29735c95bbbb3e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[211]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:90144","line":211,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:90144","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-18ca514ccfadc18d
  kind: prior_review
  reference: reports/yaml_record_review/O-nitrophenyl-beta-D-galactopyranosid.md
  locator: '`data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml`:2;
    Verdict:4; Identity:9; Validation:24; Evidence:31; Completeness:48; Recommended
    Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ac8ae542c7a179338d86f7098a34df9918ac477d5447491f1e3984701d3bef24
  quote: 'Recommended Edits:

    - None for this record.'
- evidence_id: ev-e7a43eae407a88e7
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[879,880]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"Available
    and unpopulated: `C12H15NO8`, charge 0, avg mass 301.251, monoisotopic 301.07977,
    InChIKey `KUWPCJHYPSUOFW-YBXAARCKSA-N` (\u00a73)","identifier":"CHEBI:90144","kind":"FIELD_MISSING","lane":"claude","line":879,"mapping_quality":"SYNONYM_MATCH","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:90144","slug":"O-nitrophenyl-beta-D-galactopyranosid","status_dir":"mapped"}},{"field":"chemical_properties","row":{"detail":"''chemical_properties.cas_rn''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"369-07-3**
    \u2014 verified to this exact structure by three independent routes and check-digit-valid
    (\u00a73)","identifier":"CHEBI:90144","kind":"FIELD_MISSING","lane":"claude","line":880,"mapping_quality":"SYNONYM_MATCH","preferred_term":"O-nitrophenyl-beta-D-galactopyranosid","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:90144","slug":"O-nitrophenyl-beta-D-galactopyranosid","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-e14da344c1c72e1b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-05defdd1a6e248db
  evidence_ids:
  - ev-1cff5f98d7cafded
  - ev-125e769ed2b623cb
  - ev-3969640b2a281d22
  - ev-cf29735c95bbbb3e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1bd35a8e54f45b97
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-05defdd1a6e248db
  evidence_ids:
  - ev-18ca514ccfadc18d
  - ev-1cff5f98d7cafded
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T07:26:28Z;
    reviewed SHA-256=aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069;
    current SHA-256=aff77b6eb75121f3f86a4a6010aae190d8eaf59ad27c12782b66d27b0471b069;
    hash_changed=False. Reports=["reports/yaml_record_review/O-nitrophenyl-beta-D-galactopyranosid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The synonym-backed
    exact CHEBI:90144 ONPG identity and final row pass.'
  dimensions:
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1cff5f98d7cafded
    - ev-18ca514ccfadc18d
- assessment_id: a-e7a43eae407a88e7
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-05defdd1a6e248db
  evidence_ids:
  - ev-18ca514ccfadc18d
  - ev-1cff5f98d7cafded
  - ev-e7a43eae407a88e7
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-18ca514ccfadc18d
    - ev-1cff5f98d7cafded
    - ev-e7a43eae407a88e7
findings:
- finding_id: rec-f-f557f5e3adbf238a
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-05defdd1a6e248db
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: O-nitrophenyl-beta-D-galactopyranosid'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-05defdd1a6e248db
  evidence_ids:
  - ev-18ca514ccfadc18d
  - ev-1cff5f98d7cafded
  - ev-e7a43eae407a88e7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/O-nitrophenyl-beta-D-galactopyranosid.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - legacy-field-missing-triage-rows
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
