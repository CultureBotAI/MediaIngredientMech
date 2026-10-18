# Per-record structured review: Azomycin (data/ingredients/mapped/Azomycin.yaml)

- Review: 20261017T083000Z-azomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Azomycin (data/ingredients/mapped/Azomycin.yaml, record-db29b4487fb4fec0, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Azomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Azomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-db29b4487fb4fec0 | data/ingredients/mapped/Azomycin.yaml | maintained | Azomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-db29b4487fb4fec0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-db29b4487fb4fec0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-db29b4487fb4fec0 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-db29b4487fb4fec0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-db29b4487fb4fec0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:10:14Z; reviewed SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b; current SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b; hash_changed=False. Reports=["reports/yaml_record_review/Azomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-grounded CHEBI 2-nitroimidazole identity and chemistry pass, but the top-level notes still describe the stale pre-promotion unmapped state.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-db29b4487fb4fec0.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-2e0974bcbb4ab044: Historical review coverage and residual narrative: Azomycin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-db29b4487fb4fec0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:10:14Z; reviewed SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b; current SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b; hash_changed=False. Reports=["reports/yaml_record_review/Azomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-grounded CHEBI 2-nitroimidazole identity and chemistry pass, but the top-level notes still describe the stale pre-promotion unmapped state.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

### rec-f-09804a8dd6c796fc: Legacy field-missing triage rows: Azomycin

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-db29b4487fb4fec0.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bfddcb6d1d16e4c8 | data/ingredients/mapped/Azomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[216],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:67135","line":218,"mapping_status":"MAPPED","ontology_id":"CHEBI:67135","preferred_term":"Azomycin"}],"identifier":"CHEBI:67135","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:67135","ontology_label":"2-nitroimidazole","ontology_source":"CHEBI"},"preferred_term":"Azomycin","sssom_rows":[{"data_row":466,"object_id":"CHEBI:67135","object_label":"2-nitroimidazole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azomycin","synonym_count":1} |
| ev-49ff773b0cb34454 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [216] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a05ca021e5443533 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Azomycin; data-row positions=[466] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":466,"object_id":"CHEBI:67135","object_label":"2-nitroimidazole","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Azomycin","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-03bf69b11c18b16d | docs/data/mapped_ingredients.csv; CSV lines=[218] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:67135","line":218,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:67135","preferred_term":"Azomycin","total_occurrences":"0"}] |
| ev-a1410464cadb1158 | reports/yaml_record_review/Azomycin.md; &#96;data/ingredients/mapped/Azomycin.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:38; Completeness:54; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b8ba912920824f31 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[287] | context_only | [{"current_record_sha256":"1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b","finding_id":"SEM:53af41b0c513f5b38263","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a32758c67692c13e | mappings/record_research_validation.tsv; lines=[854] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"yes","evidence":"formula &#96;C3H3N3O2&#96;; net charge &#96;0&#96;; average mass &#96;113.076&#96;; monoisotopic mass &#96;113.02253&#96;; SMILES &#96;O=[N+]([O-])c1nccn1&#96;; InChI &#96;InChI=1S/C3H3N3O2/c7-6(8)3-4-1-2-5-3/h1-2H,(H,4,5)&#96;; InChIKey &#96;YZEUHQHUFTYLPH-UHFFFAOYSA-N&#96;; CAS-RN &#96;527-73-1&#96; (\u00a73)","identifier":"CHEBI:67135","kind":"FIELD_MISSING","lane":"claude","line":854,"mapping_quality":"SYNONYM_MATCH","preferred_term":"Azomycin","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:67135","slug":"Azomycin","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-azomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Azomycin (data/ingredients/mapped/Azomycin.yaml)'
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
summary: Per-record structured review for Azomycin (data/ingredients/mapped/Azomycin.yaml,
  record-db29b4487fb4fec0, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Azomycin.yaml
    sha256: 1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b
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
  - path: reports/yaml_record_review/Azomycin.md
    sha256: 1d31b217a18e41d4529a746a6f66770e01727fddf88a54d9ce76dae14c9754c4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-db29b4487fb4fec0
  path: data/ingredients/mapped/Azomycin.yaml
  label: Azomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Azomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Azomycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-db29b4487fb4fec0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-db29b4487fb4fec0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-db29b4487fb4fec0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-db29b4487fb4fec0
evidence:
- evidence_id: ev-bfddcb6d1d16e4c8
  kind: record_content
  reference: data/ingredients/mapped/Azomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[216],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:67135","line":218,"mapping_status":"MAPPED","ontology_id":"CHEBI:67135","preferred_term":"Azomycin"}],"identifier":"CHEBI:67135","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:67135","ontology_label":"2-nitroimidazole","ontology_source":"CHEBI"},"preferred_term":"Azomycin","sssom_rows":[{"data_row":466,"object_id":"CHEBI:67135","object_label":"2-nitroimidazole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azomycin","synonym_count":1}'
  snapshot_sha256: 1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b
- evidence_id: ev-49ff773b0cb34454
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [216]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a05ca021e5443533
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Azomycin; data-row positions=[466]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":466,"object_id":"CHEBI:67135","object_label":"2-nitroimidazole","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Azomycin","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-03bf69b11c18b16d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[218]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:67135","line":218,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:67135","preferred_term":"Azomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a1410464cadb1158
  kind: prior_review
  reference: reports/yaml_record_review/Azomycin.md
  locator: '`data/ingredients/mapped/Azomycin.yaml`:2; Verdict:4; Identity:12; Validation:23;
    Evidence:38; Completeness:54; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1d31b217a18e41d4529a746a6f66770e01727fddf88a54d9ce76dae14c9754c4
  quote: "Recommended Edits:\n- Remove or rewrite the top-level `notes` in\n  `data/ingredients/mapped/Azomycin.yaml`,\
    \ synchronize\n  `data/curated/mapped_ingredients.yaml`, and rerun focused strict\
    \ and term\n  validation plus flat-export coverage."
- evidence_id: ev-b8ba912920824f31
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[287]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b","finding_id":"SEM:53af41b0c513f5b38263","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a32758c67692c13e
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[854]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"formula
    `C3H3N3O2`; net charge `0`; average mass `113.076`; monoisotopic mass `113.02253`;
    SMILES `O=[N+]([O-])c1nccn1`; InChI `InChI=1S/C3H3N3O2/c7-6(8)3-4-1-2-5-3/h1-2H,(H,4,5)`;
    InChIKey `YZEUHQHUFTYLPH-UHFFFAOYSA-N`; CAS-RN `527-73-1` (\u00a73)","identifier":"CHEBI:67135","kind":"FIELD_MISSING","lane":"claude","line":854,"mapping_quality":"SYNONYM_MATCH","preferred_term":"Azomycin","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:67135","slug":"Azomycin","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-a72382674daa4da7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-db29b4487fb4fec0
  evidence_ids:
  - ev-bfddcb6d1d16e4c8
  - ev-49ff773b0cb34454
  - ev-a05ca021e5443533
  - ev-03bf69b11c18b16d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-aee86c56e6bb36e6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-db29b4487fb4fec0
  evidence_ids:
  - ev-a1410464cadb1158
  - ev-bfddcb6d1d16e4c8
  - ev-b8ba912920824f31
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:10:14Z;
    reviewed SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b;
    current SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b;
    hash_changed=False. Reports=["reports/yaml_record_review/Azomycin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym-grounded CHEBI
    2-nitroimidazole identity and chemistry pass, but the top-level notes still describe
    the stale pre-promotion unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a1410464cadb1158
    - ev-bfddcb6d1d16e4c8
  - name: legacy-native-ids
    value: '["SEM:53af41b0c513f5b38263"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bfddcb6d1d16e4c8
    - ev-a1410464cadb1158
    - ev-b8ba912920824f31
- assessment_id: a-a32758c67692c13e
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-db29b4487fb4fec0
  evidence_ids:
  - ev-a1410464cadb1158
  - ev-bfddcb6d1d16e4c8
  - ev-a32758c67692c13e
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a1410464cadb1158
    - ev-bfddcb6d1d16e4c8
    - ev-a32758c67692c13e
findings:
- finding_id: rec-f-2e0974bcbb4ab044
  issue_key: mim-reconciliation-historical-review-coverage-and-r-db29b4487fb4fec0
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Azomycin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:10:14Z;
    reviewed SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b;
    current SHA-256=1312f9ec16210ddff006bf8836ae5260f268e6514c416017de113c489d523b8b;
    hash_changed=False. Reports=["reports/yaml_record_review/Azomycin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym-grounded CHEBI
    2-nitroimidazole identity and chemistry pass, but the top-level notes still describe
    the stale pre-promotion unmapped state.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-db29b4487fb4fec0
  evidence_ids:
  - ev-a1410464cadb1158
  - ev-bfddcb6d1d16e4c8
  - ev-b8ba912920824f31
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azomycin.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-09804a8dd6c796fc
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-db29b4487fb4fec0
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: Azomycin'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-db29b4487fb4fec0
  evidence_ids:
  - ev-a1410464cadb1158
  - ev-bfddcb6d1d16e4c8
  - ev-a32758c67692c13e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azomycin.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
