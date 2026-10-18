# Per-record structured review: Coenzyme_A (data/ingredients/mapped/Coenzyme_A.yaml)

- Review: 20261017T083000Z-coenzyme-a
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Coenzyme_A (data/ingredients/mapped/Coenzyme_A.yaml, record-04b99bf093c23316, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Coenzyme_A.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Coenzyme_A.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-04b99bf093c23316 | data/ingredients/mapped/Coenzyme_A.yaml | maintained | Coenzyme_A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-04b99bf093c23316 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-04b99bf093c23316 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-04b99bf093c23316 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-04b99bf093c23316.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-04b99bf093c23316.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:27:40Z; reviewed SHA-256=38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1; current SHA-256=38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1; hash_changed=False. Reports=["reports/yaml_record_review/Coenzyme_A.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI coenzyme A identity, 10/10 count, and SSSOM row pass, but its cofactor role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-04b99bf093c23316.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-dd2b7d6894c9faef: Reassess prediction-only role support: Coenzyme A

major / open / confirmed; issue key: mim-reconciliation-role-support-04b99bf093c23316.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-dd2b7d6894c9faef

Reassess prediction-only role support: Coenzyme A

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e6134611443b58be | data/ingredients/mapped/Coenzyme_A.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15346","line":749,"mapping_status":"MAPPED","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme A"}],"identifier":"CHEBI:15346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15346","ontology_label":"coenzyme A","ontology_source":"CHEBI"},"preferred_term":"Coenzyme A","sssom_rows":[{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Coenzyme_A","synonym_count":10} |
| ev-37024e64333f174b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [747] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b25401d18a41183a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Coenzyme_A; data-row positions=[801] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme A","other":"3'-phosphoadenosine 5'-{3-[(3R)-3-hydroxy-2,2-dimethyl-4-oxo-4-({3-oxo-3-[(2-sulfanylethyl)amino]propyl}amino)butyl] dihydrogen diphosphate}&#124;3'-phosphoadenosine-(5')diphospho(4')pantatheine&#124;CoA-SH&#124;CoASH&#124;Coenzym A&#124;HSCoA&#124;Koenzym A&#124;[(2R,3S,4R,5R)-5-(6-amino-9H-purin-9-yl)-4-hydroxy-3-(phosphonooxy)tetrahydrofuran-2-yl]methyl (3R)-3-hydroxy-4-({3-oxo-3-[(2-sulfanylethyl)amino]propyl}amino)-2,2-dimethyl-4-oxobutyl dihydrogen diphosphate&#124;CAS:85-61-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Coenzyme_A","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-7d9698d22b3aaff9 | docs/data/mapped_ingredients.csv; CSV lines=[749] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15346","line":749,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme A","total_occurrences":"10"}] |
| ev-97ba8fc0bc98089f | reports/yaml_record_review/Coenzyme_A.md; &#96;data/ingredients/mapped/Coenzyme_A.yaml&#96;:2; Verdict:4; Identity:12; Validation:27; Evidence:47; Completeness:66; Recommended Edits:72 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-be2d0574caea8928 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[435,1814] | context_only | [{"current_record_sha256":"38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1","finding_id":"SEM:e67a1994bfab4acc6703","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1","finding_id":"SEM:78ef4f8ef76af79b8849","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4f8ba62b4bdd6e1b | data/ingredients/mapped/Coenzyme_A.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15346","line":749,"mapping_status":"MAPPED","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme A"}],"identifier":"CHEBI:15346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15346","ontology_label":"coenzyme A","ontology_source":"CHEBI"},"preferred_term":"Coenzyme A","sssom_rows":[{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Coenzyme_A","synonym_count":10} |
| ev-a6039e98aff76d02 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-dd2b7d6894c9faef] | context_only | Predecessor structured review finding f-dd2b7d6894c9faef in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-coenzyme-a
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Coenzyme_A (data/ingredients/mapped/Coenzyme_A.yaml)'
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
summary: Per-record structured review for Coenzyme_A (data/ingredients/mapped/Coenzyme_A.yaml,
  record-04b99bf093c23316, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Coenzyme_A.yaml
    sha256: 38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1
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
  - path: reports/yaml_record_review/Coenzyme_A.md
    sha256: bcf43f452a5e6818396cbdc1a2a2589ac8e889278cfd5654985699a3373da8c3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-04b99bf093c23316
  path: data/ingredients/mapped/Coenzyme_A.yaml
  label: Coenzyme_A
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Coenzyme_A.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Coenzyme_A.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Coenzyme_A.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-04b99bf093c23316
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-e6134611443b58be
  - ev-37024e64333f174b
  - ev-b25401d18a41183a
  - ev-7d9698d22b3aaff9
  - ev-4f8ba62b4bdd6e1b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-e6134611443b58be
  - ev-be2d0574caea8928
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-97ba8fc0bc98089f
  - ev-be2d0574caea8928
  - ev-a6039e98aff76d02
evidence:
- evidence_id: ev-e6134611443b58be
  kind: record_content
  reference: data/ingredients/mapped/Coenzyme_A.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15346","line":749,"mapping_status":"MAPPED","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme
    A"}],"identifier":"CHEBI:15346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15346","ontology_label":"coenzyme
    A","ontology_source":"CHEBI"},"preferred_term":"Coenzyme A","sssom_rows":[{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Coenzyme_A","synonym_count":10}'
  snapshot_sha256: 38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1
- evidence_id: ev-37024e64333f174b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [747]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b25401d18a41183a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Coenzyme_A; data-row positions=[801]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme
    A","other":"3''-phosphoadenosine 5''-{3-[(3R)-3-hydroxy-2,2-dimethyl-4-oxo-4-({3-oxo-3-[(2-sulfanylethyl)amino]propyl}amino)butyl]
    dihydrogen diphosphate}|3''-phosphoadenosine-(5'')diphospho(4'')pantatheine|CoA-SH|CoASH|Coenzym
    A|HSCoA|Koenzym A|[(2R,3S,4R,5R)-5-(6-amino-9H-purin-9-yl)-4-hydroxy-3-(phosphonooxy)tetrahydrofuran-2-yl]methyl
    (3R)-3-hydroxy-4-({3-oxo-3-[(2-sulfanylethyl)amino]propyl}amino)-2,2-dimethyl-4-oxobutyl
    dihydrogen diphosphate|CAS:85-61-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Coenzyme_A","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7d9698d22b3aaff9
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[749]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15346","line":749,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme
    A","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-97ba8fc0bc98089f
  kind: prior_review
  reference: reports/yaml_record_review/Coenzyme_A.md
  locator: '`data/ingredients/mapped/Coenzyme_A.yaml`:2; Verdict:4; Identity:12; Validation:27;
    Evidence:47; Completeness:66; Recommended Edits:72'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: bcf43f452a5e6818396cbdc1a2a2589ac8e889278cfd5654985699a3373da8c3
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Coenzyme_A.yaml`,\
    \ either replace\n  `nutritional_roles.COFACTOR_PROVIDER` with inspected evidence\
    \ for coenzyme A\n  as a cofactor provider in this media scope, or remove the\
    \ role.\n- Regenerate synchronized products and rerun strict validation, SSSOM\
    \ QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-be2d0574caea8928
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[435,1814]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1","finding_id":"SEM:e67a1994bfab4acc6703","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1","finding_id":"SEM:78ef4f8ef76af79b8849","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4f8ba62b4bdd6e1b
  kind: record_content
  reference: data/ingredients/mapped/Coenzyme_A.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15346","line":749,"mapping_status":"MAPPED","ontology_id":"CHEBI:15346","preferred_term":"Coenzyme
    A"}],"identifier":"CHEBI:15346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15346","ontology_label":"coenzyme
    A","ontology_source":"CHEBI"},"preferred_term":"Coenzyme A","sssom_rows":[{"data_row":801,"object_id":"CHEBI:15346","object_label":"coenzyme
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Coenzyme_A","synonym_count":10}'
  snapshot_sha256: 38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1
- evidence_id: ev-a6039e98aff76d02
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-dd2b7d6894c9faef]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-dd2b7d6894c9faef in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-61a846299cf59c24
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-e6134611443b58be
  - ev-37024e64333f174b
  - ev-b25401d18a41183a
  - ev-7d9698d22b3aaff9
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ea32aa6e1a97ef47
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-97ba8fc0bc98089f
  - ev-e6134611443b58be
  - ev-be2d0574caea8928
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:27:40Z;
    reviewed SHA-256=38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1;
    current SHA-256=38a4c9f6bf0743e254be2eb1ae86a28b37e7bda3bc767421fb57fa241be67ce1;
    hash_changed=False. Reports=["reports/yaml_record_review/Coenzyme_A.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    coenzyme A identity, 10/10 count, and SSSOM row pass, but its cofactor role is
    only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-97ba8fc0bc98089f
    - ev-e6134611443b58be
  - name: legacy-native-ids
    value: '["SEM:e67a1994bfab4acc6703","SEM:78ef4f8ef76af79b8849"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e6134611443b58be
    - ev-97ba8fc0bc98089f
    - ev-be2d0574caea8928
- assessment_id: a-4f8ba62b4bdd6e1b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-97ba8fc0bc98089f
  - ev-4f8ba62b4bdd6e1b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-97ba8fc0bc98089f
    - ev-4f8ba62b4bdd6e1b
findings:
- finding_id: rec-f-dd2b7d6894c9faef
  issue_key: mim-reconciliation-role-support-04b99bf093c23316
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Coenzyme A'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-04b99bf093c23316
  evidence_ids:
  - ev-97ba8fc0bc98089f
  - ev-4f8ba62b4bdd6e1b
  - ev-a6039e98aff76d02
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Coenzyme_A.yaml
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
    finding_id: f-dd2b7d6894c9faef
actions:
- action_id: rec-action-dd2b7d6894c9faef
  description: 'Reassess prediction-only role support: Coenzyme A'
  finding_ids:
  - rec-f-dd2b7d6894c9faef
  target_ids:
  - record-04b99bf093c23316
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Coenzyme_A.yaml
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
