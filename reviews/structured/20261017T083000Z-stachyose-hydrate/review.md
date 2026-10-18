# Per-record structured review: Stachyose_Hydrate (data/ingredients/mapped/Stachyose_Hydrate.yaml)

- Review: 20261017T083000Z-stachyose-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Stachyose_Hydrate (data/ingredients/mapped/Stachyose_Hydrate.yaml, record-0ff453440710770a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Stachyose_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Stachyose_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0ff453440710770a | data/ingredients/mapped/Stachyose_Hydrate.yaml | maintained | Stachyose_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0ff453440710770a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0ff453440710770a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0ff453440710770a | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0ff453440710770a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0ff453440710770a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z; reviewed SHA-256=c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682; current SHA-256=c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682; hash_changed=False. Reports=["reports/yaml_record_review/Stachyose_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close hydrate row is missing its local kgmicrobe.compound sibling and has a provisional CARBON_SOURCE role.

### Historical provisional-role concern

evidence: concern. Targets: record-0ff453440710770a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-512714805e6476c5: Reassess prediction-only role support: Stachyose hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-0ff453440710770a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-512714805e6476c5

Reassess prediction-only role support: Stachyose hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9170f89dc4cdf0da | data/ingredients/mapped/Stachyose_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1895],"raw_equal":true},"docs_rows":[{"identifier":"cas:54261-98-2","line":1897,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose hydrate"}],"identifier":"cas:54261-98-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose hydrate","sssom_rows":[{"data_row":2641,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:closeMatch"},{"data_row":2642,"object_id":"cas:54261-98-2","object_label":"Stachyose hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_Hydrate","synonym_count":0} |
| ev-b37c43d45eba1cca | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1895] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-78bd190d319f3102 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Stachyose_Hydrate; data-row positions=[2641,2642] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2641,"object_id":"CHEBI:17164","object_label":"stachyose","other":"CAS:54261-98-2","predicate_id":"skos:closeMatch","subject_id":"MIM:Stachyose_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":2642,"object_id":"cas:54261-98-2","object_label":"Stachyose hydrate","other":"CAS:54261-98-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Stachyose_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e1996954b30aa66e | docs/data/mapped_ingredients.csv; CSV lines=[1897] | supports | Published identity and count rows inspected: [{"identifier":"cas:54261-98-2","line":1897,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17164","preferred_term":"Stachyose hydrate","total_occurrences":"0"}] |
| ev-095a6fa7c8e7040c | reports/yaml_record_review/Stachyose_Hydrate.md; &#96;data/ingredients/mapped/Stachyose_Hydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:32; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3b3cc4908c685cbb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1247,2102] | context_only | [{"current_record_sha256":"c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682","finding_id":"SEM:c1a3ca7f81aed3d5c33d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682","finding_id":"SEM:3342da359901c5a7d5e8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-50631c9455ac1266 | data/ingredients/mapped/Stachyose_Hydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-88fad6150ae03398 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-512714805e6476c5] | context_only | Predecessor structured review finding f-512714805e6476c5 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-stachyose-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Stachyose_Hydrate (data/ingredients/mapped/Stachyose_Hydrate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Stachyose_Hydrate (data/ingredients/mapped/Stachyose_Hydrate.yaml,
  record-0ff453440710770a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Stachyose_Hydrate.yaml
    sha256: c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682
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
  - path: reports/yaml_record_review/Stachyose_Hydrate.md
    sha256: 388c693f0e201b7f581b4144f551ac3bab94b3674bba1d5ef30d91240175f148
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0ff453440710770a
  path: data/ingredients/mapped/Stachyose_Hydrate.yaml
  label: Stachyose_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Stachyose_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Stachyose_Hydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0ff453440710770a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0ff453440710770a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0ff453440710770a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0ff453440710770a
evidence:
- evidence_id: ev-9170f89dc4cdf0da
  kind: record_content
  reference: data/ingredients/mapped/Stachyose_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1895],"raw_equal":true},"docs_rows":[{"identifier":"cas:54261-98-2","line":1897,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose
    hydrate"}],"identifier":"cas:54261-98-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose
    hydrate","sssom_rows":[{"data_row":2641,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:closeMatch"},{"data_row":2642,"object_id":"cas:54261-98-2","object_label":"Stachyose
    hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_Hydrate","synonym_count":0}'
  snapshot_sha256: c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682
- evidence_id: ev-b37c43d45eba1cca
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1895]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-78bd190d319f3102
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Stachyose_Hydrate; data-row positions=[2641,2642]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2641,"object_id":"CHEBI:17164","object_label":"stachyose","other":"CAS:54261-98-2","predicate_id":"skos:closeMatch","subject_id":"MIM:Stachyose_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":2642,"object_id":"cas:54261-98-2","object_label":"Stachyose
    hydrate","other":"CAS:54261-98-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Stachyose_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e1996954b30aa66e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1897]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:54261-98-2","line":1897,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17164","preferred_term":"Stachyose
    hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-095a6fa7c8e7040c
  kind: prior_review
  reference: reports/yaml_record_review/Stachyose_Hydrate.md
  locator: '`data/ingredients/mapped/Stachyose_Hydrate.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:32; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 388c693f0e201b7f581b4144f551ac3bab94b3674bba1d5ef30d91240175f148
  quote: "Recommended Edits:\n- Major: add the missing local `kgmicrobe.compound:stachyose_hydrate`\
    \ identity\n  row through the maintained YAML/SSSOM generation path so the final\
    \ SSSOM\n  records both the close CHEBI parent and the local hydrate identity.\n\
    - Major: remove `nutritional_roles.CARBON_SOURCE` or replace the provisional\n\
    \  name-list assertion with source evidence that uses stachyose hydrate as a\n\
    \  carbon source."
- evidence_id: ev-3b3cc4908c685cbb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1247,2102]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682","finding_id":"SEM:c1a3ca7f81aed3d5c33d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682","finding_id":"SEM:3342da359901c5a7d5e8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-50631c9455ac1266
  kind: record_content
  reference: data/ingredients/mapped/Stachyose_Hydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682
- evidence_id: ev-88fad6150ae03398
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-512714805e6476c5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-512714805e6476c5 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-cd56958cf63f2143
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0ff453440710770a
  evidence_ids:
  - ev-9170f89dc4cdf0da
  - ev-b37c43d45eba1cca
  - ev-78bd190d319f3102
  - ev-e1996954b30aa66e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c318b8392cae371c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0ff453440710770a
  evidence_ids:
  - ev-095a6fa7c8e7040c
  - ev-9170f89dc4cdf0da
  - ev-3b3cc4908c685cbb
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z;
    reviewed SHA-256=c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682;
    current SHA-256=c8bd702022c2f571b9bbcb446d2abe1cda6b69568d2b0bea257be86540305682;
    hash_changed=False. Reports=["reports/yaml_record_review/Stachyose_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The close
    hydrate row is missing its local kgmicrobe.compound sibling and has a provisional
    CARBON_SOURCE role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-095a6fa7c8e7040c
    - ev-9170f89dc4cdf0da
  - name: legacy-native-ids
    value: '["SEM:c1a3ca7f81aed3d5c33d","SEM:3342da359901c5a7d5e8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9170f89dc4cdf0da
    - ev-095a6fa7c8e7040c
    - ev-3b3cc4908c685cbb
- assessment_id: a-50631c9455ac1266
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0ff453440710770a
  evidence_ids:
  - ev-095a6fa7c8e7040c
  - ev-50631c9455ac1266
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-095a6fa7c8e7040c
    - ev-50631c9455ac1266
findings:
- finding_id: rec-f-512714805e6476c5
  issue_key: mim-reconciliation-role-support-0ff453440710770a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Stachyose hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0ff453440710770a
  evidence_ids:
  - ev-095a6fa7c8e7040c
  - ev-50631c9455ac1266
  - ev-88fad6150ae03398
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_Hydrate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-512714805e6476c5
actions:
- action_id: rec-action-512714805e6476c5
  description: 'Reassess prediction-only role support: Stachyose hydrate'
  finding_ids:
  - rec-f-512714805e6476c5
  target_ids:
  - record-0ff453440710770a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_Hydrate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
