# Per-record structured review: D-Fructose_6-phosphate_Disodium_Salt_Hydrate (data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml)

- Review: 20261017T083000Z-d-fructose-6-phosphate-disodium-salt-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Fructose_6-phosphate_Disodium_Salt_Hydrate (data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml, record-17c23f81cba8deb8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-17c23f81cba8deb8 | data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml | maintained | D-Fructose_6-phosphate_Disodium_Salt_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-17c23f81cba8deb8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-17c23f81cba8deb8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-17c23f81cba8deb8 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-17c23f81cba8deb8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-17c23f81cba8deb8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:09:03Z; reviewed SHA-256=2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565; current SHA-256=2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565; hash_changed=False. Reports=["reports/yaml_record_review/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary and close CHEBI parent pass, but final SSSOM exports an anhydrous synonym and the carbon role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-17c23f81cba8deb8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4f532c5c8515e98b: Reassess prediction-only role support: D-Fructose 6-phosphate disodium salt hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-17c23f81cba8deb8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4f532c5c8515e98b

Reassess prediction-only role support: D-Fructose 6-phosphate disodium salt hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5faa642fbc4acdeb | data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[808],"raw_equal":true},"docs_rows":[{"identifier":"cas:26177-86-6","line":810,"mapping_status":"MAPPED","ontology_id":"CHEBI:190546","preferred_term":"D-Fructose 6-phosphate disodium salt hydrate"}],"identifier":"cas:26177-86-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:190546","ontology_label":"D-Fructose 6-Phosphate-Disodium Salt","ontology_source":"CHEBI"},"preferred_term":"D-Fructose 6-phosphate disodium salt hydrate","sssom_rows":[{"data_row":879,"object_id":"CHEBI:190546","object_label":"D-Fructose 6-Phosphate-Disodium Salt","predicate_id":"skos:closeMatch"},{"data_row":880,"object_id":"cas:26177-86-6","object_label":"D-Fructose 6-phosphate disodium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","synonym_count":1} |
| ev-2eadcb431ca22fc5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [808] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ec53cc64ef973838 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate; data-row positions=[879,880] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":879,"object_id":"CHEBI:190546","object_label":"D-Fructose 6-Phosphate-Disodium Salt","other":"disodium;[(2R,3R,4S)-2,3,4,6-tetrahydroxy-5-oxohexyl] phosphate&#124;CAS:26177-86-6","predicate_id":"skos:closeMatch","subject_id":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":880,"object_id":"cas:26177-86-6","object_label":"D-Fructose 6-phosphate disodium salt hydrate","other":"CAS:26177-86-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-d9f7b1b8d8f8b1b2 | docs/data/mapped_ingredients.csv; CSV lines=[810] | supports | Published identity and count rows inspected: [{"identifier":"cas:26177-86-6","line":810,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:190546","preferred_term":"D-Fructose 6-phosphate disodium salt hydrate","total_occurrences":"0"}] |
| ev-3b6f51f88b98efa8 | reports/yaml_record_review/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.md; &#96;data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:29; Evidence:48; Completeness:70; Recommended Edits:78 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ef5934593709409a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[464,1402] | context_only | [{"current_record_sha256":"2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565","finding_id":"SEM:64755858d701807bb86e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565","finding_id":"SEM:6e34ae0ed0d8378189ed","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c8886643c5a0207d | data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-20347d34f2766b97 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-4f532c5c8515e98b] | context_only | Predecessor structured review finding f-4f532c5c8515e98b in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-fructose-6-phosphate-disodium-salt-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Fructose_6-phosphate_Disodium_Salt_Hydrate
  (data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml)'
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
summary: Per-record structured review for D-Fructose_6-phosphate_Disodium_Salt_Hydrate
  (data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml, record-17c23f81cba8deb8,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
    sha256: 2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.md
    sha256: b68a6440e1faf0b3f2f3e24173b44976653022b68c89dbb696da481973126c96
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-17c23f81cba8deb8
  path: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
  label: D-Fructose_6-phosphate_Disodium_Salt_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-17c23f81cba8deb8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-17c23f81cba8deb8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-17c23f81cba8deb8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-17c23f81cba8deb8
evidence:
- evidence_id: ev-5faa642fbc4acdeb
  kind: record_content
  reference: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[808],"raw_equal":true},"docs_rows":[{"identifier":"cas:26177-86-6","line":810,"mapping_status":"MAPPED","ontology_id":"CHEBI:190546","preferred_term":"D-Fructose
    6-phosphate disodium salt hydrate"}],"identifier":"cas:26177-86-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:190546","ontology_label":"D-Fructose
    6-Phosphate-Disodium Salt","ontology_source":"CHEBI"},"preferred_term":"D-Fructose
    6-phosphate disodium salt hydrate","sssom_rows":[{"data_row":879,"object_id":"CHEBI:190546","object_label":"D-Fructose
    6-Phosphate-Disodium Salt","predicate_id":"skos:closeMatch"},{"data_row":880,"object_id":"cas:26177-86-6","object_label":"D-Fructose
    6-phosphate disodium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","synonym_count":1}'
  snapshot_sha256: 2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565
- evidence_id: ev-2eadcb431ca22fc5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [808]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ec53cc64ef973838
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate; data-row positions=[879,880]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":879,"object_id":"CHEBI:190546","object_label":"D-Fructose
    6-Phosphate-Disodium Salt","other":"disodium;[(2R,3R,4S)-2,3,4,6-tetrahydroxy-5-oxohexyl]
    phosphate|CAS:26177-86-6","predicate_id":"skos:closeMatch","subject_id":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":880,"object_id":"cas:26177-86-6","object_label":"D-Fructose
    6-phosphate disodium salt hydrate","other":"CAS:26177-86-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Fructose_6-phosphate_Disodium_Salt_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d9f7b1b8d8f8b1b2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[810]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:26177-86-6","line":810,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:190546","preferred_term":"D-Fructose
    6-phosphate disodium salt hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3b6f51f88b98efa8
  kind: prior_review
  reference: reports/yaml_record_review/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.md
  locator: '`data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`:2;
    Verdict:4; Identity:12; Validation:29; Evidence:48; Completeness:70; Recommended
    Edits:78'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b68a6440e1faf0b3f2f3e24173b44976653022b68c89dbb696da481973126c96
  quote: "Recommended Edits:\n- In\n  `data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml`,\n\
    \  remove or demote the anhydrous `disodium;[...] phosphate` exact synonym so\n\
    \  the final SSSOM no longer publishes it in `other`, then regenerate the final\n\
    \  SSSOM.\n- In the same record, either replace the computational `CARBON_SOURCE`\n\
    \  evidence with direct source-backed media-role evidence for this hydrated\n\
    \  salt, or remove the role facet; then rerun strict validation and the final\n\
    \  SSSOM build."
- evidence_id: ev-ef5934593709409a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[464,1402]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565","finding_id":"SEM:64755858d701807bb86e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565","finding_id":"SEM:6e34ae0ed0d8378189ed","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c8886643c5a0207d
  kind: record_content
  reference: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565
- evidence_id: ev-20347d34f2766b97
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-4f532c5c8515e98b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4f532c5c8515e98b in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-afba02fcdce0e552
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-17c23f81cba8deb8
  evidence_ids:
  - ev-5faa642fbc4acdeb
  - ev-2eadcb431ca22fc5
  - ev-ec53cc64ef973838
  - ev-d9f7b1b8d8f8b1b2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5390d3158c09a369
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-17c23f81cba8deb8
  evidence_ids:
  - ev-3b6f51f88b98efa8
  - ev-5faa642fbc4acdeb
  - ev-ef5934593709409a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:09:03Z;
    reviewed SHA-256=2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565;
    current SHA-256=2244062bcf003bedc31752d4b5b370a062b488c426fd025f86ce7cecc154a565;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary and close CHEBI parent pass, but final SSSOM exports an anhydrous synonym
    and the carbon role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3b6f51f88b98efa8
    - ev-5faa642fbc4acdeb
  - name: legacy-native-ids
    value: '["SEM:64755858d701807bb86e","SEM:6e34ae0ed0d8378189ed"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5faa642fbc4acdeb
    - ev-3b6f51f88b98efa8
    - ev-ef5934593709409a
- assessment_id: a-c8886643c5a0207d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-17c23f81cba8deb8
  evidence_ids:
  - ev-3b6f51f88b98efa8
  - ev-c8886643c5a0207d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3b6f51f88b98efa8
    - ev-c8886643c5a0207d
findings:
- finding_id: rec-f-4f532c5c8515e98b
  issue_key: mim-reconciliation-role-support-17c23f81cba8deb8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Fructose 6-phosphate disodium salt
    hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-17c23f81cba8deb8
  evidence_ids:
  - ev-3b6f51f88b98efa8
  - ev-c8886643c5a0207d
  - ev-20347d34f2766b97
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-4f532c5c8515e98b
actions:
- action_id: rec-action-4f532c5c8515e98b
  description: 'Reassess prediction-only role support: D-Fructose 6-phosphate disodium
    salt hydrate'
  finding_ids:
  - rec-f-4f532c5c8515e98b
  target_ids:
  - record-17c23f81cba8deb8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
