# Per-record structured review: 4-aminobutyrate (data/ingredients/mapped/4-aminobutyrate.yaml)

- Review: 20261017T083000Z-4-aminobutyrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 4-aminobutyrate (data/ingredients/mapped/4-aminobutyrate.yaml, record-736095f9a480287b, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/4-aminobutyrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/4-aminobutyrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-736095f9a480287b | data/ingredients/mapped/4-aminobutyrate.yaml | maintained | 4-aminobutyrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-736095f9a480287b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-736095f9a480287b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-736095f9a480287b | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-736095f9a480287b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-736095f9a480287b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:19:48Z; reviewed SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa; current SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa; hash_changed=False. Reports=["reports/yaml_record_review/4-aminobutyrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The promoted CHEBI GABA anion identity, microbedecoder occurrence count, chemistry, SSSOM, and aggregate pass, but stale pre-promotion import text remains in notes.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-736095f9a480287b.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-87422ccee1cec37b: Historical review coverage and residual narrative: 4-aminobutyrate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-736095f9a480287b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:19:48Z; reviewed SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa; current SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa; hash_changed=False. Reports=["reports/yaml_record_review/4-aminobutyrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The promoted CHEBI GABA anion identity, microbedecoder occurrence count, chemistry, SSSOM, and aggregate pass, but stale pre-promotion import text remains in notes.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

### rec-f-0590ec8944ca2fc4: Legacy field-missing triage rows: 4-aminobutyrate

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-736095f9a480287b.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dfee70134cc857b4 | data/ingredients/mapped/4-aminobutyrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[220],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30566","line":222,"mapping_status":"MAPPED","ontology_id":"CHEBI:30566","preferred_term":"4-aminobutyrate"}],"identifier":"CHEBI:30566","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":7,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30566","ontology_label":"gamma-aminobutyrate","ontology_source":"CHEBI"},"preferred_term":"4-aminobutyrate","sssom_rows":[{"data_row":192,"object_id":"CHEBI:30566","object_label":"gamma-aminobutyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-aminobutyrate","synonym_count":1} |
| ev-87b8a46fc9e7a18c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [220] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8170dca5e69b659d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-aminobutyrate; data-row positions=[192] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":192,"object_id":"CHEBI:30566","object_label":"gamma-aminobutyrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:4-aminobutyrate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-9578d6496c0ef2be | docs/data/mapped_ingredients.csv; CSV lines=[222] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30566","line":222,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30566","preferred_term":"4-aminobutyrate","total_occurrences":"0"}] |
| ev-83293b1dc129d566 | reports/yaml_record_review/4-aminobutyrate.md; &#96;data/ingredients/mapped/4-aminobutyrate.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:34; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c122047434ee4b25 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[151] | context_only | [{"current_record_sha256":"81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa","finding_id":"SEM:e329a52ab4c0b3d55551","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-877842f6098eb3b8 | mappings/record_research_validation.tsv; lines=[813] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"yes","evidence":"formula &#96;C4H8NO2&#96;; charge &#96;-1&#96;; average mass &#96;102.113&#96;; monoisotopic &#96;102.05605&#96;; SMILES &#96;NCCCC(=O)[O-]&#96;; InChIKey &#96;BTCSSZJGUNDROE-UHFFFAOYSA-M&#96;; **no CAS-RN** (see \u00a73)","identifier":"CHEBI:30566","kind":"FIELD_MISSING","lane":"claude","line":813,"mapping_quality":"SYNONYM_MATCH","preferred_term":"4-aminobutyrate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:30566","slug":"4-aminobutyrate","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-4-aminobutyrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 4-aminobutyrate (data/ingredients/mapped/4-aminobutyrate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=2
scientific_review: false
summary: Per-record structured review for 4-aminobutyrate (data/ingredients/mapped/4-aminobutyrate.yaml,
  record-736095f9a480287b, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/4-aminobutyrate.yaml
    sha256: 81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/4-aminobutyrate.md
    sha256: 970f63e0704a8554d0cf98ea36695c09bfcce680148ff88b83f8f43b1e4b65fb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-736095f9a480287b
  path: data/ingredients/mapped/4-aminobutyrate.yaml
  label: 4-aminobutyrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-aminobutyrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/4-aminobutyrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/4-aminobutyrate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-736095f9a480287b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-736095f9a480287b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-736095f9a480287b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-736095f9a480287b
evidence:
- evidence_id: ev-dfee70134cc857b4
  kind: record_content
  reference: data/ingredients/mapped/4-aminobutyrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[220],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30566","line":222,"mapping_status":"MAPPED","ontology_id":"CHEBI:30566","preferred_term":"4-aminobutyrate"}],"identifier":"CHEBI:30566","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":7,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30566","ontology_label":"gamma-aminobutyrate","ontology_source":"CHEBI"},"preferred_term":"4-aminobutyrate","sssom_rows":[{"data_row":192,"object_id":"CHEBI:30566","object_label":"gamma-aminobutyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-aminobutyrate","synonym_count":1}'
  snapshot_sha256: 81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa
- evidence_id: ev-87b8a46fc9e7a18c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [220]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8170dca5e69b659d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-aminobutyrate; data-row positions=[192]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":192,"object_id":"CHEBI:30566","object_label":"gamma-aminobutyrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:4-aminobutyrate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9578d6496c0ef2be
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[222]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30566","line":222,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30566","preferred_term":"4-aminobutyrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-83293b1dc129d566
  kind: prior_review
  reference: reports/yaml_record_review/4-aminobutyrate.md
  locator: '`data/ingredients/mapped/4-aminobutyrate.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:34; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 970f63e0704a8554d0cf98ea36695c09bfcce680148ff88b83f8f43b1e4b65fb
  quote: 'Recommended Edits:

    Optionally replace the stale top-level `notes` with a post-promotion statement

    or remove the note entirely, and drop the duplicate `RAW_TEXT` synonym.'
- evidence_id: ev-c122047434ee4b25
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[151]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa","finding_id":"SEM:e329a52ab4c0b3d55551","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-877842f6098eb3b8
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[813]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"formula
    `C4H8NO2`; charge `-1`; average mass `102.113`; monoisotopic `102.05605`; SMILES
    `NCCCC(=O)[O-]`; InChIKey `BTCSSZJGUNDROE-UHFFFAOYSA-M`; **no CAS-RN** (see \u00a73)","identifier":"CHEBI:30566","kind":"FIELD_MISSING","lane":"claude","line":813,"mapping_quality":"SYNONYM_MATCH","preferred_term":"4-aminobutyrate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:30566","slug":"4-aminobutyrate","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-3fc608eb5dc330a4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-736095f9a480287b
  evidence_ids:
  - ev-dfee70134cc857b4
  - ev-87b8a46fc9e7a18c
  - ev-8170dca5e69b659d
  - ev-9578d6496c0ef2be
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9f4ce6ff5b6f8b6e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-736095f9a480287b
  evidence_ids:
  - ev-83293b1dc129d566
  - ev-dfee70134cc857b4
  - ev-c122047434ee4b25
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:19:48Z;
    reviewed SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa;
    current SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa;
    hash_changed=False. Reports=["reports/yaml_record_review/4-aminobutyrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The promoted
    CHEBI GABA anion identity, microbedecoder occurrence count, chemistry, SSSOM,
    and aggregate pass, but stale pre-promotion import text remains in notes.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83293b1dc129d566
    - ev-dfee70134cc857b4
  - name: legacy-native-ids
    value: '["SEM:e329a52ab4c0b3d55551"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dfee70134cc857b4
    - ev-83293b1dc129d566
    - ev-c122047434ee4b25
- assessment_id: a-877842f6098eb3b8
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-736095f9a480287b
  evidence_ids:
  - ev-83293b1dc129d566
  - ev-dfee70134cc857b4
  - ev-877842f6098eb3b8
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83293b1dc129d566
    - ev-dfee70134cc857b4
    - ev-877842f6098eb3b8
findings:
- finding_id: rec-f-87422ccee1cec37b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-736095f9a480287b
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 4-aminobutyrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:19:48Z;
    reviewed SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa;
    current SHA-256=81cda698c0a83434935448791dfa636fa36996869bd690e426687b8a6783b0fa;
    hash_changed=False. Reports=["reports/yaml_record_review/4-aminobutyrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The promoted
    CHEBI GABA anion identity, microbedecoder occurrence count, chemistry, SSSOM,
    and aggregate pass, but stale pre-promotion import text remains in notes.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-736095f9a480287b
  evidence_ids:
  - ev-83293b1dc129d566
  - ev-dfee70134cc857b4
  - ev-c122047434ee4b25
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-aminobutyrate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-0590ec8944ca2fc4
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-736095f9a480287b
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: 4-aminobutyrate'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-736095f9a480287b
  evidence_ids:
  - ev-83293b1dc129d566
  - ev-dfee70134cc857b4
  - ev-877842f6098eb3b8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-aminobutyrate.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
