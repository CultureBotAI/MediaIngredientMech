# Per-record structured review: L-malate (data/ingredients/mapped/L-malate.yaml)

- Review: 20261017T083000Z-l-malate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-malate (data/ingredients/mapped/L-malate.yaml, record-d1d526465ff9c786, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-malate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-malate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d1d526465ff9c786 | data/ingredients/mapped/L-malate.yaml | maintained | L-malate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d1d526465ff9c786 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d1d526465ff9c786 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d1d526465ff9c786 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d1d526465ff9c786.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d1d526465ff9c786.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T23:11:24Z; reviewed SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18; current SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18; hash_changed=False. Reports=["reports/yaml_record_review/L-malate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, dianion structure, source occurrence count, and final SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-d1d526465ff9c786.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-ae1d2dc8bc918acc: Historical review coverage and residual narrative: L-malate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d1d526465ff9c786.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T23:11:24Z; reviewed SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18; current SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18; hash_changed=False. Reports=["reports/yaml_record_review/L-malate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, dianion structure, source occurrence count, and final SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

### rec-f-e42a69ca69118110: Legacy field-missing triage rows: L-malate

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-d1d526465ff9c786.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cf362de77ed967e0 | data/ingredients/mapped/L-malate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[236],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15589","line":238,"mapping_status":"MAPPED","ontology_id":"CHEBI:15589","preferred_term":"L-malate"}],"identifier":"CHEBI:15589","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":48,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:15589","ontology_label":"(S)-malate(2-)","ontology_source":"CHEBI"},"preferred_term":"L-malate","sssom_rows":[{"data_row":1627,"object_id":"CHEBI:15589","object_label":"(S)-malate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-malate","synonym_count":1} |
| ev-48bbd35ba7ac9861 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [236] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f65c0d4a648f84a5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-malate; data-row positions=[1627] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1627,"object_id":"CHEBI:15589","object_label":"(S)-malate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-malate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-05"}] |
| ev-641a35bb321902cc | docs/data/mapped_ingredients.csv; CSV lines=[238] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15589","line":238,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15589","preferred_term":"L-malate","total_occurrences":"0"}] |
| ev-8d9407ba658a9391 | reports/yaml_record_review/L-malate.md; &#96;data/ingredients/mapped/L-malate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:46; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-640cf7258237cb6c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[826] | context_only | [{"current_record_sha256":"f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18","finding_id":"SEM:27d5704368cb5c9e581d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-58c30bb524026726 | mappings/record_research_validation.tsv; lines=[874] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"no","evidence":"formula &#96;C4H4O5&#96;; net charge &#96;-2&#96;; average mass &#96;132.071&#96;; monoisotopic mass &#96;132.00697&#96;; SMILES &#96;O=C([O-])C[C@H](O)C(=O)[O-]&#96;; InChIKey &#96;BJEPYKJPYRNKOW-REOHCLBHSA-L&#96;; PubChem CID 5459792. **No CAS-RN** \u2014 see \u00a73","identifier":"CHEBI:15589","kind":"FIELD_MISSING","lane":"claude","line":874,"mapping_quality":"SYNONYM_MATCH","preferred_term":"L-malate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:15589","slug":"L-malate","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-malate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-malate (data/ingredients/mapped/L-malate.yaml)'
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
summary: Per-record structured review for L-malate (data/ingredients/mapped/L-malate.yaml,
  record-d1d526465ff9c786, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-malate.yaml
    sha256: f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-malate.md
    sha256: ede06d33ab23af2c3b0d1854bb96c8c3fbd21848d623817ed87d66c70de9a92b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-d1d526465ff9c786
  path: data/ingredients/mapped/L-malate.yaml
  label: L-malate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-malate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-malate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-malate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d1d526465ff9c786
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d1d526465ff9c786
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d1d526465ff9c786
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d1d526465ff9c786
evidence:
- evidence_id: ev-cf362de77ed967e0
  kind: record_content
  reference: data/ingredients/mapped/L-malate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[236],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15589","line":238,"mapping_status":"MAPPED","ontology_id":"CHEBI:15589","preferred_term":"L-malate"}],"identifier":"CHEBI:15589","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":48,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:15589","ontology_label":"(S)-malate(2-)","ontology_source":"CHEBI"},"preferred_term":"L-malate","sssom_rows":[{"data_row":1627,"object_id":"CHEBI:15589","object_label":"(S)-malate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-malate","synonym_count":1}'
  snapshot_sha256: f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18
- evidence_id: ev-48bbd35ba7ac9861
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [236]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f65c0d4a648f84a5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-malate; data-row positions=[1627]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1627,"object_id":"CHEBI:15589","object_label":"(S)-malate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-malate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-05"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-641a35bb321902cc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[238]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15589","line":238,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15589","preferred_term":"L-malate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8d9407ba658a9391
  kind: prior_review
  reference: reports/yaml_record_review/L-malate.md
  locator: '`data/ingredients/mapped/L-malate.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:28; Completeness:46; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ede06d33ab23af2c3b0d1854bb96c8c3fbd21848d623817ed87d66c70de9a92b
  quote: "Recommended Edits:\n- Minor: update the stale top-level `notes` in\n  `data/ingredients/mapped/L-malate.yaml`\
    \ and the aggregate copy the next time\n  the record is touched so the current\
    \ review text does not imply that the\n  CHEBI search is still unresolved."
- evidence_id: ev-640cf7258237cb6c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[826]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18","finding_id":"SEM:27d5704368cb5c9e581d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-58c30bb524026726
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[874]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"no","evidence":"formula
    `C4H4O5`; net charge `-2`; average mass `132.071`; monoisotopic mass `132.00697`;
    SMILES `O=C([O-])C[C@H](O)C(=O)[O-]`; InChIKey `BJEPYKJPYRNKOW-REOHCLBHSA-L`;
    PubChem CID 5459792. **No CAS-RN** \u2014 see \u00a73","identifier":"CHEBI:15589","kind":"FIELD_MISSING","lane":"claude","line":874,"mapping_quality":"SYNONYM_MATCH","preferred_term":"L-malate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:15589","slug":"L-malate","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-317b705257e9d810
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d1d526465ff9c786
  evidence_ids:
  - ev-cf362de77ed967e0
  - ev-48bbd35ba7ac9861
  - ev-f65c0d4a648f84a5
  - ev-641a35bb321902cc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a8915ae6d1c4e0c2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1d526465ff9c786
  evidence_ids:
  - ev-8d9407ba658a9391
  - ev-cf362de77ed967e0
  - ev-640cf7258237cb6c
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T23:11:24Z;
    reviewed SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18;
    current SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18;
    hash_changed=False. Reports=["reports/yaml_record_review/L-malate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CHEBI synonym identity,
    dianion structure, source occurrence count, and final SSSOM row pass, but stale
    importer notes still say no CHEBI/NCIT match was found.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8d9407ba658a9391
    - ev-cf362de77ed967e0
  - name: legacy-native-ids
    value: '["SEM:27d5704368cb5c9e581d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cf362de77ed967e0
    - ev-8d9407ba658a9391
    - ev-640cf7258237cb6c
- assessment_id: a-58c30bb524026726
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-d1d526465ff9c786
  evidence_ids:
  - ev-8d9407ba658a9391
  - ev-cf362de77ed967e0
  - ev-58c30bb524026726
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8d9407ba658a9391
    - ev-cf362de77ed967e0
    - ev-58c30bb524026726
findings:
- finding_id: rec-f-ae1d2dc8bc918acc
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d1d526465ff9c786
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-malate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T23:11:24Z;
    reviewed SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18;
    current SHA-256=f13e689afed8266abef67b1eb2fac342c477ffe0089d2d2f24ddb23e39446e18;
    hash_changed=False. Reports=["reports/yaml_record_review/L-malate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CHEBI synonym identity,
    dianion structure, source occurrence count, and final SSSOM row pass, but stale
    importer notes still say no CHEBI/NCIT match was found.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1d526465ff9c786
  evidence_ids:
  - ev-8d9407ba658a9391
  - ev-cf362de77ed967e0
  - ev-640cf7258237cb6c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-malate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-e42a69ca69118110
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-d1d526465ff9c786
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: L-malate'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-d1d526465ff9c786
  evidence_ids:
  - ev-8d9407ba658a9391
  - ev-cf362de77ed967e0
  - ev-58c30bb524026726
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-malate.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
