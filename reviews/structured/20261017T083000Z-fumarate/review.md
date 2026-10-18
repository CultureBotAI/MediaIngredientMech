# Per-record structured review: Fumarate (data/ingredients/mapped/Fumarate.yaml)

- Review: 20261017T083000Z-fumarate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fumarate (data/ingredients/mapped/Fumarate.yaml, record-9664a64a4ac934e4, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fumarate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fumarate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9664a64a4ac934e4 | data/ingredients/mapped/Fumarate.yaml | maintained | Fumarate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9664a64a4ac934e4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9664a64a4ac934e4 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9664a64a4ac934e4 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9664a64a4ac934e4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9664a64a4ac934e4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:08:07Z; reviewed SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005; current SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005; hash_changed=False. Reports=["reports/yaml_record_review/Fumarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The promoted fumarate anion identity, chemistry, and final SSSOM row pass, but top-level notes remain stale.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-9664a64a4ac934e4.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-15b35f58ba2ee1c6: Historical review coverage and residual narrative: Fumarate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9664a64a4ac934e4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:08:07Z; reviewed SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005; current SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005; hash_changed=False. Reports=["reports/yaml_record_review/Fumarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The promoted fumarate anion identity, chemistry, and final SSSOM row pass, but top-level notes remain stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

### rec-f-1200cec8219018d7: Legacy field-missing triage rows: Fumarate

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-9664a64a4ac934e4.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4969b6b6824cd899 | data/ingredients/mapped/Fumarate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[232],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29806","line":234,"mapping_status":"MAPPED","ontology_id":"CHEBI:29806","preferred_term":"Fumarate"}],"identifier":"CHEBI:29806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"source_occurrences":[{"count":103,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production&#124;BacDive_Metabolite_utilization"}],"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29806","ontology_label":"fumarate(2-)","ontology_source":"CHEBI"},"preferred_term":"Fumarate","sssom_rows":[{"data_row":1252,"object_id":"CHEBI:29806","object_label":"fumarate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumarate","synonym_count":1} |
| ev-aaa7b9e0f6a3c96d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [232] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9bb00382480b4bfd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fumarate; data-row positions=[1252] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1252,"object_id":"CHEBI:29806","object_label":"fumarate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fumarate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-27eae5c30beb85d6 | docs/data/mapped_ingredients.csv; CSV lines=[234] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29806","line":234,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:29806","preferred_term":"Fumarate","total_occurrences":"2"}] |
| ev-c0a1d895dff2091d | reports/yaml_record_review/Fumarate.md; &#96;data/ingredients/mapped/Fumarate.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:33; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d607b42d2dd01733 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[638] | context_only | [{"current_record_sha256":"7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005","finding_id":"SEM:3fed827ca60bd926d7b3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a7e0e6f408ed29db | mappings/record_research_validation.tsv; lines=[863] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"yes","evidence":"formula &#96;C4H2O4&#96;; net charge &#96;-2&#96;; average mass &#96;114.056&#96;; monoisotopic mass &#96;113.99641&#96;; SMILES &#96;O=C([O-])/C=C/C(=O)[O-]&#96;; InChIKey &#96;VZCYOOQTPOCHFL-OWOJBTEDSA-L&#96;; CAS-RN &#96;142-42-7","identifier":"CHEBI:29806","kind":"FIELD_MISSING","lane":"claude","line":863,"mapping_quality":"SYNONYM_MATCH","preferred_term":"Fumarate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:29806","slug":"Fumarate","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fumarate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fumarate (data/ingredients/mapped/Fumarate.yaml)'
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
summary: Per-record structured review for Fumarate (data/ingredients/mapped/Fumarate.yaml,
  record-9664a64a4ac934e4, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fumarate.yaml
    sha256: 7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005
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
  - path: reports/yaml_record_review/Fumarate.md
    sha256: e721d6e32b9d0c125d55c2858498596e993140dd37dcdf93bbeb92430739c115
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-9664a64a4ac934e4
  path: data/ingredients/mapped/Fumarate.yaml
  label: Fumarate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumarate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fumarate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fumarate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9664a64a4ac934e4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9664a64a4ac934e4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9664a64a4ac934e4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9664a64a4ac934e4
evidence:
- evidence_id: ev-4969b6b6824cd899
  kind: record_content
  reference: data/ingredients/mapped/Fumarate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[232],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29806","line":234,"mapping_status":"MAPPED","ontology_id":"CHEBI:29806","preferred_term":"Fumarate"}],"identifier":"CHEBI:29806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"source_occurrences":[{"count":103,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production|BacDive_Metabolite_utilization"}],"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29806","ontology_label":"fumarate(2-)","ontology_source":"CHEBI"},"preferred_term":"Fumarate","sssom_rows":[{"data_row":1252,"object_id":"CHEBI:29806","object_label":"fumarate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumarate","synonym_count":1}'
  snapshot_sha256: 7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005
- evidence_id: ev-aaa7b9e0f6a3c96d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [232]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9bb00382480b4bfd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fumarate; data-row positions=[1252]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1252,"object_id":"CHEBI:29806","object_label":"fumarate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fumarate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-27eae5c30beb85d6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[234]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29806","line":234,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:29806","preferred_term":"Fumarate","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c0a1d895dff2091d
  kind: prior_review
  reference: reports/yaml_record_review/Fumarate.md
  locator: '`data/ingredients/mapped/Fumarate.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:33; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e721d6e32b9d0c125d55c2858498596e993140dd37dcdf93bbeb92430739c115
  quote: "Recommended Edits:\n- Minor: replace the stale top-level `notes` in\n  `data/ingredients/mapped/Fumarate.yaml`\
    \ with a short post-promotion statement\n  that the bare anion label was reviewed\
    \ and grounded to `fumarate(2-)`."
- evidence_id: ev-d607b42d2dd01733
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[638]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005","finding_id":"SEM:3fed827ca60bd926d7b3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a7e0e6f408ed29db
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[863]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"formula
    `C4H2O4`; net charge `-2`; average mass `114.056`; monoisotopic mass `113.99641`;
    SMILES `O=C([O-])/C=C/C(=O)[O-]`; InChIKey `VZCYOOQTPOCHFL-OWOJBTEDSA-L`; CAS-RN
    `142-42-7","identifier":"CHEBI:29806","kind":"FIELD_MISSING","lane":"claude","line":863,"mapping_quality":"SYNONYM_MATCH","preferred_term":"Fumarate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:29806","slug":"Fumarate","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-3504d7fe93aae087
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9664a64a4ac934e4
  evidence_ids:
  - ev-4969b6b6824cd899
  - ev-aaa7b9e0f6a3c96d
  - ev-9bb00382480b4bfd
  - ev-27eae5c30beb85d6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-da76a1516760020e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9664a64a4ac934e4
  evidence_ids:
  - ev-c0a1d895dff2091d
  - ev-4969b6b6824cd899
  - ev-d607b42d2dd01733
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:08:07Z;
    reviewed SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005;
    current SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005;
    hash_changed=False. Reports=["reports/yaml_record_review/Fumarate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The promoted fumarate anion
    identity, chemistry, and final SSSOM row pass, but top-level notes remain stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c0a1d895dff2091d
    - ev-4969b6b6824cd899
  - name: legacy-native-ids
    value: '["SEM:3fed827ca60bd926d7b3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4969b6b6824cd899
    - ev-c0a1d895dff2091d
    - ev-d607b42d2dd01733
- assessment_id: a-a7e0e6f408ed29db
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-9664a64a4ac934e4
  evidence_ids:
  - ev-c0a1d895dff2091d
  - ev-4969b6b6824cd899
  - ev-a7e0e6f408ed29db
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c0a1d895dff2091d
    - ev-4969b6b6824cd899
    - ev-a7e0e6f408ed29db
findings:
- finding_id: rec-f-15b35f58ba2ee1c6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9664a64a4ac934e4
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Fumarate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:08:07Z;
    reviewed SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005;
    current SHA-256=7a3ec4ebe3036b8077753432978a5cd3dc40fedd88a55582aaf72a2293fab005;
    hash_changed=False. Reports=["reports/yaml_record_review/Fumarate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The promoted fumarate anion
    identity, chemistry, and final SSSOM row pass, but top-level notes remain stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9664a64a4ac934e4
  evidence_ids:
  - ev-c0a1d895dff2091d
  - ev-4969b6b6824cd899
  - ev-d607b42d2dd01733
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumarate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-1200cec8219018d7
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-9664a64a4ac934e4
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: Fumarate'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-9664a64a4ac934e4
  evidence_ids:
  - ev-c0a1d895dff2091d
  - ev-4969b6b6824cd899
  - ev-a7e0e6f408ed29db
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumarate.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
