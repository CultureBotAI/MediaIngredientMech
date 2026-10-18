# Per-record structured review: Casein_Peptone (data/ingredients/mapped/Casein_Peptone.yaml)

- Review: 20261017T083000Z-casein-peptone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Casein_Peptone (data/ingredients/mapped/Casein_Peptone.yaml, record-d53a266c76ee002b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Casein_Peptone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Casein_Peptone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d53a266c76ee002b | data/ingredients/mapped/Casein_Peptone.yaml | maintained | Casein_Peptone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d53a266c76ee002b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d53a266c76ee002b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d53a266c76ee002b | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d53a266c76ee002b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d53a266c76ee002b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:45Z; reviewed SHA-256=6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; current SHA-256=6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050145Z-Casein_Peptone.md","reports/yaml_record_review/Casein_Peptone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Casein_Peptone.md&#96; after the record changed from fb7511438af2b5a01352f441376690282c1f399a40ed5bc9de564dbe3c929724 to 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-d53a266c76ee002b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f7705eadc1b26d43: Reassess prediction-only role support: Casein peptone

major / open / confirmed; issue key: mim-reconciliation-role-support-d53a266c76ee002b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f7705eadc1b26d43

Reassess prediction-only role support: Casein peptone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-71ea74cdd2fb41ce | data/ingredients/mapped/Casein_Peptone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[663],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315719","line":665,"mapping_status":"MAPPED","ontology_id":"FOODON:03315719","preferred_term":"Casein peptone"}],"identifier":"FOODON:03315719","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1247,"edge_count":1247,"occurrences":1313},"occurrence_statistics":{"media_count":1247,"total_occurrences":1313},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315719","ontology_label":"mammalian milk protein (hydrolyzed)","ontology_source":"FOODON"},"preferred_term":"Casein peptone","sssom_rows":[{"data_row":659,"object_id":"FOODON:03315719","object_label":"mammalian milk protein (hydrolyzed)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein_Peptone","synonym_count":15} |
| ev-b01f072bf88ffbd8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [663] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-422f4f53dcf7c298 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Casein_Peptone; data-row positions=[659] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":659,"object_id":"FOODON:03315719","object_label":"mammalian milk protein (hydrolyzed)","other":"Casein peptone, tryptic digest&#124;Peptone from casein&#124;Pancreatic Digest of Casein&#124;Pancreatic Digest of Casein (Hardy C6530)&#124;Caseine peptone&#124;Casein peptone, tryptic digested&#124;Enzymatic digest of casein&#124;Acid-hydrolyzed casein&#124;Casein enzymic hydrolysate&#124;casein hydrolyzate acid&#124;Casein hydrolysate (NZ Case TT, Quest International)","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein_Peptone","validation_method":"manual:apply_669_704_rulings&#124;OTHER&#124;2026-09-24"}] |
| ev-a5909ee349f9e43b | docs/data/mapped_ingredients.csv; CSV lines=[665] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03315719","line":665,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1247","ontology_id":"FOODON:03315719","preferred_term":"Casein peptone","total_occurrences":"1313"}] |
| ev-cb3e163d35ba7e80 | reports/yaml_record_review/20261001T050145Z-Casein_Peptone.md; YAML Record Review: Casein peptone:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0dd9396a3b6b20e7 | reports/yaml_record_review/Casein_Peptone.md; &#96;data/ingredients/mapped/Casein_Peptone.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:45; Completeness:59; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c53e9515722348e2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[367,1570] | context_only | [{"current_record_sha256":"6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64","finding_id":"SEM:ace1e0beee97878de750","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64","finding_id":"SEM:0b51ae3fe55776e57073","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9d7036a698f118ad | data/ingredients/mapped/Casein_Peptone.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-ea31fd31c9525147 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-f7705eadc1b26d43] | context_only | Predecessor structured review finding f-f7705eadc1b26d43 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-casein-peptone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Casein_Peptone (data/ingredients/mapped/Casein_Peptone.yaml)'
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
summary: Per-record structured review for Casein_Peptone (data/ingredients/mapped/Casein_Peptone.yaml,
  record-d53a266c76ee002b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Casein_Peptone.yaml
    sha256: 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/20261001T050145Z-Casein_Peptone.md
    sha256: f00e0545690f31233615613bc40ac6f24c4fe234e6cd607aecc563c3c640fd38
    role: context
  - path: reports/yaml_record_review/Casein_Peptone.md
    sha256: 4e42bfaf71350b0249aae96d5b830de8a5d3c7bf79f021ef3da6e234c8b17cc2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d53a266c76ee002b
  path: data/ingredients/mapped/Casein_Peptone.yaml
  label: Casein_Peptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_Peptone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Casein_Peptone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Casein_Peptone.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d53a266c76ee002b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d53a266c76ee002b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d53a266c76ee002b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d53a266c76ee002b
evidence:
- evidence_id: ev-71ea74cdd2fb41ce
  kind: record_content
  reference: data/ingredients/mapped/Casein_Peptone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[663],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315719","line":665,"mapping_status":"MAPPED","ontology_id":"FOODON:03315719","preferred_term":"Casein
    peptone"}],"identifier":"FOODON:03315719","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1247,"edge_count":1247,"occurrences":1313},"occurrence_statistics":{"media_count":1247,"total_occurrences":1313},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315719","ontology_label":"mammalian
    milk protein (hydrolyzed)","ontology_source":"FOODON"},"preferred_term":"Casein
    peptone","sssom_rows":[{"data_row":659,"object_id":"FOODON:03315719","object_label":"mammalian
    milk protein (hydrolyzed)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein_Peptone","synonym_count":15}'
  snapshot_sha256: 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64
- evidence_id: ev-b01f072bf88ffbd8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [663]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-422f4f53dcf7c298
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Casein_Peptone; data-row positions=[659]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":659,"object_id":"FOODON:03315719","object_label":"mammalian
    milk protein (hydrolyzed)","other":"Casein peptone, tryptic digest|Peptone from
    casein|Pancreatic Digest of Casein|Pancreatic Digest of Casein (Hardy C6530)|Caseine
    peptone|Casein peptone, tryptic digested|Enzymatic digest of casein|Acid-hydrolyzed
    casein|Casein enzymic hydrolysate|casein hydrolyzate acid|Casein hydrolysate (NZ
    Case TT, Quest International)","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein_Peptone","validation_method":"manual:apply_669_704_rulings|OTHER|2026-09-24"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a5909ee349f9e43b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[665]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03315719","line":665,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1247","ontology_id":"FOODON:03315719","preferred_term":"Casein
    peptone","total_occurrences":"1313"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cb3e163d35ba7e80
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050145Z-Casein_Peptone.md
  locator: 'YAML Record Review: Casein peptone:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f00e0545690f31233615613bc40ac6f24c4fe234e6cd607aecc563c3c640fd38
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Casein_Peptone.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The FoodOn
    casein-peptone parent grounding passes, but PROTEIN_SOURCE is only a provisional
    name-pattern prediction.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Casein_Peptone.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Casein_Peptone.yaml`,
    `just validate-terms data/ingredients/mapped/Casein_Peptone.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-0dd9396a3b6b20e7
  kind: prior_review
  reference: reports/yaml_record_review/Casein_Peptone.md
  locator: '`data/ingredients/mapped/Casein_Peptone.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:45; Completeness:59; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4e42bfaf71350b0249aae96d5b830de8a5d3c7bf79f021ef3da6e234c8b17cc2
  quote: "Recommended Edits:\n- Major: either replace the provisional\n  `nutritional_roles.PROTEIN_SOURCE`\
    \ evidence in\n  `data/ingredients/mapped/Casein_Peptone.yaml` with inspected\
    \ evidence for\n  this casein-peptone family scope, or remove the role, then rerun\
    \ strict\n  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-c53e9515722348e2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[367,1570]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64","finding_id":"SEM:ace1e0beee97878de750","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64","finding_id":"SEM:0b51ae3fe55776e57073","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9d7036a698f118ad
  kind: record_content
  reference: data/ingredients/mapped/Casein_Peptone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64
- evidence_id: ev-ea31fd31c9525147
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-f7705eadc1b26d43]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f7705eadc1b26d43 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-4d604be172319076
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d53a266c76ee002b
  evidence_ids:
  - ev-71ea74cdd2fb41ce
  - ev-b01f072bf88ffbd8
  - ev-422f4f53dcf7c298
  - ev-a5909ee349f9e43b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b3ee724361fbb54a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d53a266c76ee002b
  evidence_ids:
  - ev-cb3e163d35ba7e80
  - ev-0dd9396a3b6b20e7
  - ev-71ea74cdd2fb41ce
  - ev-c53e9515722348e2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:45Z;
    reviewed SHA-256=6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64;
    current SHA-256=6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050145Z-Casein_Peptone.md","reports/yaml_record_review/Casein_Peptone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Casein_Peptone.md` after the record changed from fb7511438af2b5a01352f441376690282c1f399a40ed5bc9de564dbe3c929724
    to 6c8f30e9340d2df5b8477791831810db38cdf6a03df96643304e43f1e2157a64; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cb3e163d35ba7e80
    - ev-0dd9396a3b6b20e7
    - ev-71ea74cdd2fb41ce
  - name: legacy-native-ids
    value: '["SEM:ace1e0beee97878de750","SEM:0b51ae3fe55776e57073"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-71ea74cdd2fb41ce
    - ev-cb3e163d35ba7e80
    - ev-0dd9396a3b6b20e7
    - ev-c53e9515722348e2
- assessment_id: a-9d7036a698f118ad
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d53a266c76ee002b
  evidence_ids:
  - ev-cb3e163d35ba7e80
  - ev-0dd9396a3b6b20e7
  - ev-9d7036a698f118ad
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cb3e163d35ba7e80
    - ev-0dd9396a3b6b20e7
    - ev-9d7036a698f118ad
findings:
- finding_id: rec-f-f7705eadc1b26d43
  issue_key: mim-reconciliation-role-support-d53a266c76ee002b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Casein peptone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d53a266c76ee002b
  evidence_ids:
  - ev-cb3e163d35ba7e80
  - ev-0dd9396a3b6b20e7
  - ev-9d7036a698f118ad
  - ev-ea31fd31c9525147
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_Peptone.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-f7705eadc1b26d43
actions:
- action_id: rec-action-f7705eadc1b26d43
  description: 'Reassess prediction-only role support: Casein peptone'
  finding_ids:
  - rec-f-f7705eadc1b26d43
  target_ids:
  - record-d53a266c76ee002b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_Peptone.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
