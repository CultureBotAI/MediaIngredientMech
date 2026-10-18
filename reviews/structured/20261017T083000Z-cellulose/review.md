# Per-record structured review: Cellulose (data/ingredients/mapped/Cellulose.yaml)

- Review: 20261017T083000Z-cellulose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cellulose (data/ingredients/mapped/Cellulose.yaml, record-19f48952b4ec213b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cellulose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cellulose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-19f48952b4ec213b | data/ingredients/mapped/Cellulose.yaml | maintained | Cellulose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-19f48952b4ec213b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-19f48952b4ec213b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-19f48952b4ec213b | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-19f48952b4ec213b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-19f48952b4ec213b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:48Z; reviewed SHA-256=65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a; current SHA-256=65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050148Z-Cellulose.md","reports/yaml_record_review/Cellulose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Cellulose.md&#96; after the record changed from ef8af16a7cf385843a7d887a779c0e83a44246dc18b5f1bbf4a7955527519e5d to 65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-19f48952b4ec213b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-00af4c973518d5c0: Reassess prediction-only role support: Cellulose

major / open / confirmed; issue key: mim-reconciliation-role-support-19f48952b4ec213b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-00af4c973518d5c0

Reassess prediction-only role support: Cellulose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e60179a25d5327ca | data/ingredients/mapped/Cellulose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[690],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18246","line":692,"mapping_status":"MAPPED","ontology_id":"CHEBI:18246","preferred_term":"Cellulose"}],"identifier":"CHEBI:18246","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":45,"edge_count":45,"occurrences":45},"occurrence_statistics":{"media_count":45,"total_occurrences":45},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18246","ontology_label":"(1-&gt;4)-beta-D-glucan","ontology_source":"CHEBI"},"preferred_term":"Cellulose","sssom_rows":[{"data_row":713,"object_id":"CHEBI:18246","object_label":"(1-&gt;4)-beta-D-glucan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellulose","synonym_count":13} |
| ev-f815bd49f749d9eb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [690] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-71b7da2f99c48b71 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cellulose; data-row positions=[713] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":713,"object_id":"CHEBI:18246","object_label":"(1-&gt;4)-beta-D-glucan","other":"Optional ingredient (Avicel SIGMA)&#124;Optional ingredient (Lens tissue or MN 301)&#124;Optional ingredient (MN 301)&#124;(1,4-beta-D-Glucosyl)n&#124;(1,4-beta-D-Glucosyl)n+1&#124;(1,4-beta-D-Glucosyl)n-1&#124;(1,4-beta-D-glucosyl)(n)&#124;(1-&gt;4)-beta-D-glucopyranan&#124;Filter paper (cellulose substrate)&#124;Cellulose (Avicel or MN 300)&#124;CAS:9004-34-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellulose","validation_method":"manual:retire_wrong_form_names&#124;OTHER&#124;2026-09-23"}] |
| ev-d89a6b4a4e35552f | docs/data/mapped_ingredients.csv; CSV lines=[692] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18246","line":692,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"45","ontology_id":"CHEBI:18246","preferred_term":"Cellulose","total_occurrences":"45"}] |
| ev-79acf807a6d60326 | reports/yaml_record_review/20261001T050148Z-Cellulose.md; YAML Record Review: Cellulose:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-403ba215ef1f97c0 | reports/yaml_record_review/Cellulose.md; &#96;data/ingredients/mapped/Cellulose.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:59; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5981efe47c78053d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[391,1785] | context_only | [{"current_record_sha256":"65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a","finding_id":"SEM:eb3085fe7830f19d5f4f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a","finding_id":"SEM:c01f921127df3b5bd07a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-398ebc56fb4e3675 | data/ingredients/mapped/Cellulose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-93b73eb04977a19b | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-00af4c973518d5c0] | context_only | Predecessor structured review finding f-00af4c973518d5c0 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cellulose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cellulose (data/ingredients/mapped/Cellulose.yaml)'
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
summary: Per-record structured review for Cellulose (data/ingredients/mapped/Cellulose.yaml,
  record-19f48952b4ec213b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cellulose.yaml
    sha256: 65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a
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
  - path: reports/yaml_record_review/20261001T050148Z-Cellulose.md
    sha256: 25117341eb9af22aec9407bdc846313837f3040a0c67a3adfad322f3ad65f626
    role: context
  - path: reports/yaml_record_review/Cellulose.md
    sha256: 69653557b6380efa3d880605c7d0860d7460a944aedbc151a6051701d05f79f5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-19f48952b4ec213b
  path: data/ingredients/mapped/Cellulose.yaml
  label: Cellulose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellulose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cellulose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cellulose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-19f48952b4ec213b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-19f48952b4ec213b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-19f48952b4ec213b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-19f48952b4ec213b
evidence:
- evidence_id: ev-e60179a25d5327ca
  kind: record_content
  reference: data/ingredients/mapped/Cellulose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[690],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18246","line":692,"mapping_status":"MAPPED","ontology_id":"CHEBI:18246","preferred_term":"Cellulose"}],"identifier":"CHEBI:18246","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":45,"edge_count":45,"occurrences":45},"occurrence_statistics":{"media_count":45,"total_occurrences":45},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18246","ontology_label":"(1->4)-beta-D-glucan","ontology_source":"CHEBI"},"preferred_term":"Cellulose","sssom_rows":[{"data_row":713,"object_id":"CHEBI:18246","object_label":"(1->4)-beta-D-glucan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellulose","synonym_count":13}'
  snapshot_sha256: 65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a
- evidence_id: ev-f815bd49f749d9eb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [690]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-71b7da2f99c48b71
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cellulose; data-row positions=[713]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":713,"object_id":"CHEBI:18246","object_label":"(1->4)-beta-D-glucan","other":"Optional
    ingredient (Avicel SIGMA)|Optional ingredient (Lens tissue or MN 301)|Optional
    ingredient (MN 301)|(1,4-beta-D-Glucosyl)n|(1,4-beta-D-Glucosyl)n+1|(1,4-beta-D-Glucosyl)n-1|(1,4-beta-D-glucosyl)(n)|(1->4)-beta-D-glucopyranan|Filter
    paper (cellulose substrate)|Cellulose (Avicel or MN 300)|CAS:9004-34-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellulose","validation_method":"manual:retire_wrong_form_names|OTHER|2026-09-23"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d89a6b4a4e35552f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[692]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18246","line":692,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"45","ontology_id":"CHEBI:18246","preferred_term":"Cellulose","total_occurrences":"45"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-79acf807a6d60326
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050148Z-Cellulose.md
  locator: 'YAML Record Review: Cellulose:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 25117341eb9af22aec9407bdc846313837f3040a0c67a3adfad322f3ad65f626
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Cellulose.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI cellulose identity and 45/45 occurrence count pass, but optional-ingredient
    notes still export as synonyms and CARBON_SOURCE is only provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Cellulose.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Cellulose.yaml`,
    `just validate-terms data/ingredients/mapped/Cellulose.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-403ba215ef1f97c0
  kind: prior_review
  reference: reports/yaml_record_review/Cellulose.md
  locator: '`data/ingredients/mapped/Cellulose.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:39; Completeness:59; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 69653557b6380efa3d880605c7d0860d7460a944aedbc151a6051701d05f79f5
  quote: "Recommended Edits:\n- Major: remove or reject the four `Optional ingredient...`\
    \ `RAW_TEXT` synonym\n  entries so they no longer publish as cellulose labels.\n\
    - Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected\n  evidence\
    \ for cellulose as a carbon source in media, or remove the role, then\n  rerun\
    \ strict validation, SSSOM QC, aggregate roundtrip, synonym export checks,\n \
    \ and `git diff --check`."
- evidence_id: ev-5981efe47c78053d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[391,1785]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a","finding_id":"SEM:eb3085fe7830f19d5f4f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a","finding_id":"SEM:c01f921127df3b5bd07a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-398ebc56fb4e3675
  kind: record_content
  reference: data/ingredients/mapped/Cellulose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a
- evidence_id: ev-93b73eb04977a19b
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-00af4c973518d5c0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-00af4c973518d5c0 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-fdddae3d052b56f7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-19f48952b4ec213b
  evidence_ids:
  - ev-e60179a25d5327ca
  - ev-f815bd49f749d9eb
  - ev-71b7da2f99c48b71
  - ev-d89a6b4a4e35552f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7bb181a590c2b645
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-19f48952b4ec213b
  evidence_ids:
  - ev-79acf807a6d60326
  - ev-403ba215ef1f97c0
  - ev-e60179a25d5327ca
  - ev-5981efe47c78053d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:48Z;
    reviewed SHA-256=65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a;
    current SHA-256=65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050148Z-Cellulose.md","reports/yaml_record_review/Cellulose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Cellulose.md` after the record changed from ef8af16a7cf385843a7d887a779c0e83a44246dc18b5f1bbf4a7955527519e5d
    to 65050b762a448d04092507444502e42bc905761aa2b6aafef7e550298da8980a; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-79acf807a6d60326
    - ev-403ba215ef1f97c0
    - ev-e60179a25d5327ca
  - name: legacy-native-ids
    value: '["SEM:eb3085fe7830f19d5f4f","SEM:c01f921127df3b5bd07a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e60179a25d5327ca
    - ev-79acf807a6d60326
    - ev-403ba215ef1f97c0
    - ev-5981efe47c78053d
- assessment_id: a-398ebc56fb4e3675
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-19f48952b4ec213b
  evidence_ids:
  - ev-79acf807a6d60326
  - ev-403ba215ef1f97c0
  - ev-398ebc56fb4e3675
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-79acf807a6d60326
    - ev-403ba215ef1f97c0
    - ev-398ebc56fb4e3675
findings:
- finding_id: rec-f-00af4c973518d5c0
  issue_key: mim-reconciliation-role-support-19f48952b4ec213b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cellulose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-19f48952b4ec213b
  evidence_ids:
  - ev-79acf807a6d60326
  - ev-403ba215ef1f97c0
  - ev-398ebc56fb4e3675
  - ev-93b73eb04977a19b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellulose.yaml
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
    finding_id: f-00af4c973518d5c0
actions:
- action_id: rec-action-00af4c973518d5c0
  description: 'Reassess prediction-only role support: Cellulose'
  finding_ids:
  - rec-f-00af4c973518d5c0
  target_ids:
  - record-19f48952b4ec213b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellulose.yaml
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
