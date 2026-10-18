# Per-record structured review: 2-deoxyadenosine (data/ingredients/mapped/2-deoxyadenosine.yaml)

- Review: 20261017T083000Z-2-deoxyadenosine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-deoxyadenosine (data/ingredients/mapped/2-deoxyadenosine.yaml, record-af95e8b55ba780d1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-deoxyadenosine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-deoxyadenosine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-af95e8b55ba780d1 | data/ingredients/mapped/2-deoxyadenosine.yaml | maintained | 2-deoxyadenosine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | failed | True | record-af95e8b55ba780d1 | Explain curation-history timestamp order: 2-deoxyadenosine |
| Role evidence and plausibility check | passed | True | record-af95e8b55ba780d1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-af95e8b55ba780d1 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-af95e8b55ba780d1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-af95e8b55ba780d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:37:16Z; reviewed SHA-256=992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930; current SHA-256=992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930; hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyadenosine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, anhydrous/monohydrate split, SSSOM, and aggregate pass, but top-level notes still describe the pre-promotion unmapped state.

### Non-monotonic curation-history timestamps

provenance: concern. Targets: record-af95e8b55ba780d1.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported from microbedecoder (source_id=kgmicrobe.trait:2_deoxyadenosine); no CAS-RN or CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted UNMAPPED_0660 -&gt; CHEBI:17256 \"2'-deoxyadenosine\" (EXACT_MATCH); mapping_status UNMAPPED -&gt; MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Findings

### rec-f-0e7210521e16e8f4: Explain curation-history timestamp order: 2-deoxyadenosine

minor / open / confirmed; issue key: mim-reconciliation-history-order-af95e8b55ba780d1.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported from microbedecoder (source_id=kgmicrobe.trait:2_deoxyadenosine); no CAS-RN or CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted UNMAPPED_0660 -&gt; CHEBI:17256 \"2'-deoxyadenosine\" (EXACT_MATCH); mapping_status UNMAPPED -&gt; MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Recommended Actions And Acceptance Checks

### rec-action-0e7210521e16e8f4

Explain curation-history timestamp order: 2-deoxyadenosine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-98be9900c88cd0f9 | data/ingredients/mapped/2-deoxyadenosine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[259],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17256","line":261,"mapping_status":"MAPPED","ontology_id":"CHEBI:17256","preferred_term":"2-deoxyadenosine"}],"identifier":"CHEBI:17256","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17256","ontology_label":"2'-deoxyadenosine","ontology_source":"CHEBI"},"preferred_term":"2-deoxyadenosine","sssom_rows":[{"data_row":80,"object_id":"CHEBI:17256","object_label":"2'-deoxyadenosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-deoxyadenosine","synonym_count":1} |
| ev-89e6932a284ac6c6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [259] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-112b1cfaac9733a6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-deoxyadenosine; data-row positions=[80] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":80,"object_id":"CHEBI:17256","object_label":"2'-deoxyadenosine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:2-deoxyadenosine","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-165d35c260479703 | docs/data/mapped_ingredients.csv; CSV lines=[261] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17256","line":261,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17256","preferred_term":"2-deoxyadenosine","total_occurrences":"0"}] |
| ev-bea0350ef32a6609 | reports/yaml_record_review/2-deoxyadenosine.md; &#96;data/ingredients/mapped/2-deoxyadenosine.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:35; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-737de4e990c2f06a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[62] | context_only | [{"current_record_sha256":"992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930","finding_id":"SEM:346e37bb86ce402c6ca3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9f1b5a554a6bf3a5 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-0e7210521e16e8f4] | context_only | Predecessor structured review finding f-0e7210521e16e8f4 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-deoxyadenosine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-deoxyadenosine (data/ingredients/mapped/2-deoxyadenosine.yaml)'
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
summary: Per-record structured review for 2-deoxyadenosine (data/ingredients/mapped/2-deoxyadenosine.yaml,
  record-af95e8b55ba780d1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-deoxyadenosine.yaml
    sha256: 992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930
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
  - path: reports/yaml_record_review/2-deoxyadenosine.md
    sha256: 2def4398748f18e632f63b68fa5a44246a21fd4102c3a82c3201a3ffb33c68d3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-af95e8b55ba780d1
  path: data/ingredients/mapped/2-deoxyadenosine.yaml
  label: 2-deoxyadenosine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-deoxyadenosine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-deoxyadenosine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-deoxyadenosine.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-af95e8b55ba780d1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: failed
  required: true
  summary: 'Explain curation-history timestamp order: 2-deoxyadenosine'
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-98be9900c88cd0f9
  - ev-89e6932a284ac6c6
  - ev-112b1cfaac9733a6
  - ev-165d35c260479703
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-98be9900c88cd0f9
  - ev-737de4e990c2f06a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-bea0350ef32a6609
  - ev-737de4e990c2f06a
  - ev-9f1b5a554a6bf3a5
evidence:
- evidence_id: ev-98be9900c88cd0f9
  kind: record_content
  reference: data/ingredients/mapped/2-deoxyadenosine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[259],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17256","line":261,"mapping_status":"MAPPED","ontology_id":"CHEBI:17256","preferred_term":"2-deoxyadenosine"}],"identifier":"CHEBI:17256","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17256","ontology_label":"2''-deoxyadenosine","ontology_source":"CHEBI"},"preferred_term":"2-deoxyadenosine","sssom_rows":[{"data_row":80,"object_id":"CHEBI:17256","object_label":"2''-deoxyadenosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-deoxyadenosine","synonym_count":1}'
  snapshot_sha256: 992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930
- evidence_id: ev-89e6932a284ac6c6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [259]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-112b1cfaac9733a6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-deoxyadenosine; data-row positions=[80]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":80,"object_id":"CHEBI:17256","object_label":"2''-deoxyadenosine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:2-deoxyadenosine","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-165d35c260479703
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[261]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17256","line":261,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17256","preferred_term":"2-deoxyadenosine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bea0350ef32a6609
  kind: prior_review
  reference: reports/yaml_record_review/2-deoxyadenosine.md
  locator: '`data/ingredients/mapped/2-deoxyadenosine.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:35; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2def4398748f18e632f63b68fa5a44246a21fd4102c3a82c3201a3ffb33c68d3
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/2-deoxyadenosine.yaml`,\
    \ replace the stale `notes`\n   text with a concise statement that the microbedecoder\
    \ residual was promoted\n   to `CHEBI:17256` through an exact local ChEBI verification.\n\
    2. Run `just sync-curated`, `just validate-strict\n   data/ingredients/mapped/2-deoxyadenosine.yaml`,\
    \ `just validate-terms\n   data/ingredients/mapped/2-deoxyadenosine.yaml`, `just\
    \ qc-sssom`, and\n   `just qc-flat-coverage` after that curation edit."
- evidence_id: ev-737de4e990c2f06a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[62]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930","finding_id":"SEM:346e37bb86ce402c6ca3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9f1b5a554a6bf3a5
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-0e7210521e16e8f4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0e7210521e16e8f4 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-fd3fc490d4e6da6c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-98be9900c88cd0f9
  - ev-89e6932a284ac6c6
  - ev-112b1cfaac9733a6
  - ev-165d35c260479703
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e3bcb123e9638bc2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-bea0350ef32a6609
  - ev-98be9900c88cd0f9
  - ev-737de4e990c2f06a
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:37:16Z;
    reviewed SHA-256=992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930;
    current SHA-256=992a02df42d22c2b42dd432e809d6dcefd0816d270733a044dd0838e77bda930;
    hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyadenosine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, anhydrous/monohydrate split, SSSOM, and aggregate pass, but
    top-level notes still describe the pre-promotion unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bea0350ef32a6609
    - ev-98be9900c88cd0f9
  - name: legacy-native-ids
    value: '["SEM:346e37bb86ce402c6ca3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-98be9900c88cd0f9
    - ev-bea0350ef32a6609
    - ev-737de4e990c2f06a
- assessment_id: a-89ad956964fcf8e6
  area: provenance
  topic: Non-monotonic curation-history timestamps
  outcome: concern
  summary: 'The reported timestamp-order problem is still observable in these adjacent
    append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported
    from microbedecoder (source_id=kgmicrobe.trait:2_deoxyadenosine); no CAS-RN or
    CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted
    UNMAPPED_0660 -> CHEBI:17256 \"2''-deoxyadenosine\" (EXACT_MATCH); mapping_status
    UNMAPPED -> MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-bea0350ef32a6609
  - ev-98be9900c88cd0f9
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bea0350ef32a6609
    - ev-98be9900c88cd0f9
findings:
- finding_id: rec-f-0e7210521e16e8f4
  issue_key: mim-reconciliation-history-order-af95e8b55ba780d1
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: 'Explain curation-history timestamp order: 2-deoxyadenosine'
  description: 'The reported timestamp-order problem is still observable in these
    adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported
    from microbedecoder (source_id=kgmicrobe.trait:2_deoxyadenosine); no CAS-RN or
    CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted
    UNMAPPED_0660 -> CHEBI:17256 \"2''-deoxyadenosine\" (EXACT_MATCH); mapping_status
    UNMAPPED -> MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-af95e8b55ba780d1
  evidence_ids:
  - ev-bea0350ef32a6609
  - ev-98be9900c88cd0f9
  - ev-9f1b5a554a6bf3a5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-deoxyadenosine.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - history-order
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-0e7210521e16e8f4
actions:
- action_id: rec-action-0e7210521e16e8f4
  description: 'Explain curation-history timestamp order: 2-deoxyadenosine'
  finding_ids:
  - rec-f-0e7210521e16e8f4
  target_ids:
  - record-af95e8b55ba780d1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-deoxyadenosine.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
