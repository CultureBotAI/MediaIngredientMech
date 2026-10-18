# Per-record structured review: DL-2-Aminoadipic_Acid (data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml)

- Review: 20261017T083000Z-dl-2-aminoadipic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for DL-2-Aminoadipic_Acid (data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml, record-3685075c8b5b5eb7, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3685075c8b5b5eb7 | data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml | maintained | DL-2-Aminoadipic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3685075c8b5b5eb7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3685075c8b5b5eb7 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3685075c8b5b5eb7 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3685075c8b5b5eb7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3685075c8b5b5eb7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:08Z; reviewed SHA-256=fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e; current SHA-256=fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050208Z-DL-2-Aminoadipic_Acid.md","reports/yaml_record_review/DL-2-Aminoadipic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/DL-2-Aminoadipic_Acid.md&#96; after the record changed from 35142da6bf1867b5b00847f2334a6fa7380af1f43a215bfe701f4e1118f30dc4 to fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e; preserved the previous blocker finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-3685075c8b5b5eb7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-46759fd5ad29eca5: Reassess prediction-only role support: DL-2-Aminoadipic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-3685075c8b5b5eb7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-46759fd5ad29eca5

Reassess prediction-only role support: DL-2-Aminoadipic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0d52ce66bb1acd92 | data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2636],"raw_equal":true},"docs_rows":[{"identifier":"cas:542-32-5","line":2638,"mapping_status":"MAPPED","ontology_id":"cas:542-32-5","preferred_term":"DL-2-Aminoadipic acid"}],"identifier":"cas:542-32-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:542-32-5","ontology_label":"DL-2-Aminoadipic acid","ontology_source":"CAS"},"preferred_term":"DL-2-Aminoadipic acid","sssom_rows":[{"data_row":969,"object_id":"cas:542-32-5","object_label":"DL-2-Aminoadipic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminoadipic_Acid","synonym_count":1} |
| ev-7015ceb7e8a7bb90 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2636] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-18c4a68dac0ff81a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:DL-2-Aminoadipic_Acid; data-row positions=[969] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":969,"object_id":"cas:542-32-5","object_label":"DL-2-Aminoadipic acid","other":"CAS:542-32-5","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminoadipic_Acid","validation_method":"manual:semantic_identity_review&#124;IDENTITY_REVIEWED&#124;2026-09-21"}] |
| ev-58621783e546c3a8 | docs/data/mapped_ingredients.csv; CSV lines=[2638] | supports | Published identity and count rows inspected: [{"identifier":"cas:542-32-5","line":2638,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:542-32-5","preferred_term":"DL-2-Aminoadipic acid","total_occurrences":"0"}] |
| ev-952208d407f91746 | reports/yaml_record_review/20261001T050208Z-DL-2-Aminoadipic_Acid.md; YAML Record Review: DL-2-Aminoadipic acid:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e88a3c9355bc03d1 | reports/yaml_record_review/DL-2-Aminoadipic_Acid.md; &#96;data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml&#96;:2; Verdict:4; Identity:12; Validation:29; Evidence:53; Completeness:68; Recommended Edits:80 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a6621c60116a567c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[512,1606] | context_only | [{"current_record_sha256":"fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e","finding_id":"SEM:1d4b0b2e54c753cb4311","kind":"existing_record_review","resolution_reason":"Retain the explicitly DL source substance as CAS 542-32-5. Withdraw L-enantiomer CHEBI:37023 and its stereospecific synonym/structure; a racemate is not one enantiomer. CAS registry identity does not imply that a new exact ChEBI search was exhaustive.","resolution_status":"RESOLVED"},{"current_record_sha256":"fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e","finding_id":"SEM:f1e57873a6b7e0aa18ee","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d4db048d962e13a6 | data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-f590e179cf5c9096 | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-46759fd5ad29eca5] | context_only | Predecessor structured review finding f-46759fd5ad29eca5 in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dl-2-aminoadipic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: DL-2-Aminoadipic_Acid (data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml)'
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
summary: Per-record structured review for DL-2-Aminoadipic_Acid (data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml,
  record-3685075c8b5b5eb7, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
    sha256: fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
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
  - path: reports/yaml_record_review/20261001T050208Z-DL-2-Aminoadipic_Acid.md
    sha256: 1f578758e86367a15c24c3ff5cbc7b15145ea88be2c2309981202bdba89ed2b0
    role: context
  - path: reports/yaml_record_review/DL-2-Aminoadipic_Acid.md
    sha256: 08c0f58042e21a0a8d13a8c66666fbdb90d13406422431707bdd58d793ead516
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3685075c8b5b5eb7
  path: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
  label: DL-2-Aminoadipic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3685075c8b5b5eb7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3685075c8b5b5eb7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3685075c8b5b5eb7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3685075c8b5b5eb7
evidence:
- evidence_id: ev-0d52ce66bb1acd92
  kind: record_content
  reference: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2636],"raw_equal":true},"docs_rows":[{"identifier":"cas:542-32-5","line":2638,"mapping_status":"MAPPED","ontology_id":"cas:542-32-5","preferred_term":"DL-2-Aminoadipic
    acid"}],"identifier":"cas:542-32-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:542-32-5","ontology_label":"DL-2-Aminoadipic
    acid","ontology_source":"CAS"},"preferred_term":"DL-2-Aminoadipic acid","sssom_rows":[{"data_row":969,"object_id":"cas:542-32-5","object_label":"DL-2-Aminoadipic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminoadipic_Acid","synonym_count":1}'
  snapshot_sha256: fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e
- evidence_id: ev-7015ceb7e8a7bb90
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2636]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-18c4a68dac0ff81a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:DL-2-Aminoadipic_Acid; data-row positions=[969]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":969,"object_id":"cas:542-32-5","object_label":"DL-2-Aminoadipic
    acid","other":"CAS:542-32-5","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminoadipic_Acid","validation_method":"manual:semantic_identity_review|IDENTITY_REVIEWED|2026-09-21"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-58621783e546c3a8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2638]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:542-32-5","line":2638,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:542-32-5","preferred_term":"DL-2-Aminoadipic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-952208d407f91746
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050208Z-DL-2-Aminoadipic_Acid.md
  locator: 'YAML Record Review: DL-2-Aminoadipic acid:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1f578758e86367a15c24c3ff5cbc7b15145ea88be2c2309981202bdba89ed2b0
  quote: 'Findings:

    - **blocker**: The previous finding set in `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The DL record
    is still exact-mapped to the L-enantiomer and exports an L-specific SSSOM synonym.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`,
    `just validate-terms data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml` where
    applicable, and `just qc-sssom`.'
- evidence_id: ev-e88a3c9355bc03d1
  kind: prior_review
  reference: reports/yaml_record_review/DL-2-Aminoadipic_Acid.md
  locator: '`data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`:2; Verdict:4; Identity:12;
    Validation:29; Evidence:53; Completeness:68; Recommended Edits:80'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 08c0f58042e21a0a8d13a8c66666fbdb90d13406422431707bdd58d793ead516
  quote: "Recommended Edits:\n- Extend `scripts/fix_cas_stereochemical_identity_conflicts.py`\
    \ to repair\n  `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`: preserve\n\
    \  `cas:542-32-5` as the exact local identity, map to `CHEBI:37024` by\n  `NARROW_MATCH`,\
    \ replace L-specific chemistry and synonyms, and emit the\n  required CAS and\
    \ kg-microbe identity rows in final SSSOM.\n- Remove the provisional `AMINO_ACID_SOURCE`\
    \ role or replace its\n  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level\
    \ evidence for\n  this supplied form.\n- Regenerate synchronized curated and SSSOM\
    \ products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-a6621c60116a567c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[512,1606]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e","finding_id":"SEM:1d4b0b2e54c753cb4311","kind":"existing_record_review","resolution_reason":"Retain
    the explicitly DL source substance as CAS 542-32-5. Withdraw L-enantiomer CHEBI:37023
    and its stereospecific synonym/structure; a racemate is not one enantiomer. CAS
    registry identity does not imply that a new exact ChEBI search was exhaustive.","resolution_status":"RESOLVED"},{"current_record_sha256":"fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e","finding_id":"SEM:f1e57873a6b7e0aa18ee","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d4db048d962e13a6
  kind: record_content
  reference: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e
- evidence_id: ev-f590e179cf5c9096
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-46759fd5ad29eca5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-46759fd5ad29eca5 in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-e69c54682c8c2097
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3685075c8b5b5eb7
  evidence_ids:
  - ev-0d52ce66bb1acd92
  - ev-7015ceb7e8a7bb90
  - ev-18c4a68dac0ff81a
  - ev-58621783e546c3a8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bb0ccc28d581ec9a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3685075c8b5b5eb7
  evidence_ids:
  - ev-952208d407f91746
  - ev-e88a3c9355bc03d1
  - ev-0d52ce66bb1acd92
  - ev-a6621c60116a567c
  details: 'Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:08Z;
    reviewed SHA-256=fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e;
    current SHA-256=fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050208Z-DL-2-Aminoadipic_Acid.md","reports/yaml_record_review/DL-2-Aminoadipic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/DL-2-Aminoadipic_Acid.md` after the record changed
    from 35142da6bf1867b5b00847f2334a6fa7380af1f43a215bfe701f4e1118f30dc4 to fa26e653b29c8d1aeeaea8a1feee468acaa737cb322b9b525eb454c8e5604d7e;
    preserved the previous blocker finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-952208d407f91746
    - ev-e88a3c9355bc03d1
    - ev-0d52ce66bb1acd92
  - name: legacy-native-ids
    value: '["SEM:1d4b0b2e54c753cb4311","SEM:f1e57873a6b7e0aa18ee"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0d52ce66bb1acd92
    - ev-952208d407f91746
    - ev-e88a3c9355bc03d1
    - ev-a6621c60116a567c
- assessment_id: a-d4db048d962e13a6
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3685075c8b5b5eb7
  evidence_ids:
  - ev-952208d407f91746
  - ev-e88a3c9355bc03d1
  - ev-d4db048d962e13a6
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-952208d407f91746
    - ev-e88a3c9355bc03d1
    - ev-d4db048d962e13a6
findings:
- finding_id: rec-f-46759fd5ad29eca5
  issue_key: mim-reconciliation-role-support-3685075c8b5b5eb7
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: DL-2-Aminoadipic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3685075c8b5b5eb7
  evidence_ids:
  - ev-952208d407f91746
  - ev-e88a3c9355bc03d1
  - ev-d4db048d962e13a6
  - ev-f590e179cf5c9096
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
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
    review_id: 20261011T024629Z-mim-reconcile-all-batch-01
    finding_id: f-46759fd5ad29eca5
actions:
- action_id: rec-action-46759fd5ad29eca5
  description: 'Reassess prediction-only role support: DL-2-Aminoadipic acid'
  finding_ids:
  - rec-f-46759fd5ad29eca5
  target_ids:
  - record-3685075c8b5b5eb7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml
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
  with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.
```
