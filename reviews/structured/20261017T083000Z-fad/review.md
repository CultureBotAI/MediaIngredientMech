# Per-record structured review: Fad (data/ingredients/mapped/Fad.yaml)

- Review: 20261017T083000Z-fad
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fad (data/ingredients/mapped/Fad.yaml, record-7baa5feffa5690ec, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fad.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fad.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7baa5feffa5690ec | data/ingredients/mapped/Fad.yaml | maintained | Fad |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7baa5feffa5690ec | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7baa5feffa5690ec | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7baa5feffa5690ec | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7baa5feffa5690ec.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7baa5feffa5690ec.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:05:10Z; reviewed SHA-256=604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699; current SHA-256=604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699; hash_changed=False. Reports=["reports/yaml_record_review/Fad.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI FAD identity and final SSSOM synonyms pass, but VITAMIN_SOURCE is computational and an active flavin adenine dinucleotide row overlaps the CAS identity.

### Historical provisional-role concern

evidence: concern. Targets: record-7baa5feffa5690ec.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9365fa81c4b3f88b: Reassess prediction-only role support: FAD

major / open / confirmed; issue key: mim-reconciliation-role-support-7baa5feffa5690ec.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9365fa81c4b3f88b

Reassess prediction-only role support: FAD

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f8360a4ccae1ac12 | data/ingredients/mapped/Fad.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[974],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16238","line":976,"mapping_status":"MAPPED","ontology_id":"CHEBI:16238","preferred_term":"FAD"}],"identifier":"CHEBI:16238","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16238","ontology_label":"FAD","ontology_source":"CHEBI"},"preferred_term":"FAD","sssom_rows":[{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fad","synonym_count":7} |
| ev-b675b56fcd1b9e64 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [974] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5a25ad883c0abc0d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fad; data-row positions=[1162] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","other":"Adenosine 5'-(trihydrogen pyrophosphate), 5'-5'-ester with riboflavine&#124;FLAVIN-ADENINE DINUCLEOTIDE&#124;Riboflavin 5'-(trihydrogen diphosphate), 5'-5'-ester with adenosine&#124;Riboflavin 5'-adenosine diphosphate&#124;adenosine 5'-(3-{D-ribo-5-[7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl]-2,3,4-trihydroxypentyl} dihydrogen diphosphate)&#124;adenosine 5'-[3-(riboflavin-5'-yl) dihydrogen diphosphate]&#124;CAS:146-14-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Fad","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-aebefba6b103adf3 | docs/data/mapped_ingredients.csv; CSV lines=[976] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16238","line":976,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:16238","preferred_term":"FAD","total_occurrences":"8"}] |
| ev-6946255a5952ddde | reports/yaml_record_review/Fad.md; &#96;data/ingredients/mapped/Fad.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:32; Completeness:57; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-424f46f49e3528b5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[580,1744] | context_only | [{"current_record_sha256":"604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699","finding_id":"SEM:9d2d755848cb2cce588c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699","finding_id":"SEM:5cc88c69942af9369f02","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b1ae246d92ffbd20 | data/ingredients/mapped/Fad.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[974],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16238","line":976,"mapping_status":"MAPPED","ontology_id":"CHEBI:16238","preferred_term":"FAD"}],"identifier":"CHEBI:16238","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16238","ontology_label":"FAD","ontology_source":"CHEBI"},"preferred_term":"FAD","sssom_rows":[{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fad","synonym_count":7} |
| ev-93e297c49811f67f | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-9365fa81c4b3f88b] | context_only | Predecessor structured review finding f-9365fa81c4b3f88b in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fad
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fad (data/ingredients/mapped/Fad.yaml)'
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
summary: Per-record structured review for Fad (data/ingredients/mapped/Fad.yaml, record-7baa5feffa5690ec,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fad.yaml
    sha256: 604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699
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
  - path: reports/yaml_record_review/Fad.md
    sha256: 142550c8c98cc56e31fffeff8016fab905cc7e0041aeb52354e407c1a84a38d9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7baa5feffa5690ec
  path: data/ingredients/mapped/Fad.yaml
  label: Fad
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fad.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fad.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Fad.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7baa5feffa5690ec
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-f8360a4ccae1ac12
  - ev-b675b56fcd1b9e64
  - ev-5a25ad883c0abc0d
  - ev-aebefba6b103adf3
  - ev-b1ae246d92ffbd20
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-f8360a4ccae1ac12
  - ev-424f46f49e3528b5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-6946255a5952ddde
  - ev-424f46f49e3528b5
  - ev-93e297c49811f67f
evidence:
- evidence_id: ev-f8360a4ccae1ac12
  kind: record_content
  reference: data/ingredients/mapped/Fad.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[974],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16238","line":976,"mapping_status":"MAPPED","ontology_id":"CHEBI:16238","preferred_term":"FAD"}],"identifier":"CHEBI:16238","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16238","ontology_label":"FAD","ontology_source":"CHEBI"},"preferred_term":"FAD","sssom_rows":[{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fad","synonym_count":7}'
  snapshot_sha256: 604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699
- evidence_id: ev-b675b56fcd1b9e64
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [974]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5a25ad883c0abc0d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fad; data-row positions=[1162]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","other":"Adenosine
    5''-(trihydrogen pyrophosphate), 5''-5''-ester with riboflavine|FLAVIN-ADENINE
    DINUCLEOTIDE|Riboflavin 5''-(trihydrogen diphosphate), 5''-5''-ester with adenosine|Riboflavin
    5''-adenosine diphosphate|adenosine 5''-(3-{D-ribo-5-[7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl]-2,3,4-trihydroxypentyl}
    dihydrogen diphosphate)|adenosine 5''-[3-(riboflavin-5''-yl) dihydrogen diphosphate]|CAS:146-14-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Fad","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-aebefba6b103adf3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[976]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16238","line":976,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:16238","preferred_term":"FAD","total_occurrences":"8"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6946255a5952ddde
  kind: prior_review
  reference: reports/yaml_record_review/Fad.md
  locator: '`data/ingredients/mapped/Fad.yaml`:2; Verdict:4; Identity:12; Validation:25;
    Evidence:32; Completeness:57; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 142550c8c98cc56e31fffeff8016fab905cc7e0041aeb52354e407c1a84a38d9
  quote: "Recommended Edits:\n- Major: either replace the provisional `VITAMIN_SOURCE`\
    \ inference with\n  source-backed evidence or remove the role facet.\n- Major:\
    \ review `data/ingredients/mapped/Fad.yaml` together with\n  `data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml`,\
    \ preserve the\n  CultureMech occurrences and accepted exact synonyms on the chosen\n\
    \  representative, avoid exporting `CAS:146-14-5` on two exact identity rows,\n\
    \  sync `data/curated/mapped_ingredients.yaml`, regenerate\n  `mappings/ingredient_mappings.sssom.tsv`,\
    \ and rerun strict validation plus\n  the final SSSOM invariant gates."
- evidence_id: ev-424f46f49e3528b5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[580,1744]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699","finding_id":"SEM:9d2d755848cb2cce588c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699","finding_id":"SEM:5cc88c69942af9369f02","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b1ae246d92ffbd20
  kind: record_content
  reference: data/ingredients/mapped/Fad.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[974],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16238","line":976,"mapping_status":"MAPPED","ontology_id":"CHEBI:16238","preferred_term":"FAD"}],"identifier":"CHEBI:16238","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16238","ontology_label":"FAD","ontology_source":"CHEBI"},"preferred_term":"FAD","sssom_rows":[{"data_row":1162,"object_id":"CHEBI:16238","object_label":"FAD","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fad","synonym_count":7}'
  snapshot_sha256: 604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699
- evidence_id: ev-93e297c49811f67f
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-9365fa81c4b3f88b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9365fa81c4b3f88b in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-afa592de59b78394
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-f8360a4ccae1ac12
  - ev-b675b56fcd1b9e64
  - ev-5a25ad883c0abc0d
  - ev-aebefba6b103adf3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-261f567fd2225a83
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-6946255a5952ddde
  - ev-f8360a4ccae1ac12
  - ev-424f46f49e3528b5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:05:10Z;
    reviewed SHA-256=604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699;
    current SHA-256=604aa537dff13b0a9b75ca69fb5a144473016a66aaddd5bfb0a271222edfe699;
    hash_changed=False. Reports=["reports/yaml_record_review/Fad.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact ChEBI FAD identity
    and final SSSOM synonyms pass, but VITAMIN_SOURCE is computational and an active
    flavin adenine dinucleotide row overlaps the CAS identity.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6946255a5952ddde
    - ev-f8360a4ccae1ac12
  - name: legacy-native-ids
    value: '["SEM:9d2d755848cb2cce588c","SEM:5cc88c69942af9369f02"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f8360a4ccae1ac12
    - ev-6946255a5952ddde
    - ev-424f46f49e3528b5
- assessment_id: a-b1ae246d92ffbd20
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-6946255a5952ddde
  - ev-b1ae246d92ffbd20
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6946255a5952ddde
    - ev-b1ae246d92ffbd20
findings:
- finding_id: rec-f-9365fa81c4b3f88b
  issue_key: mim-reconciliation-role-support-7baa5feffa5690ec
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: FAD'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7baa5feffa5690ec
  evidence_ids:
  - ev-6946255a5952ddde
  - ev-b1ae246d92ffbd20
  - ev-93e297c49811f67f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fad.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-9365fa81c4b3f88b
actions:
- action_id: rec-action-9365fa81c4b3f88b
  description: 'Reassess prediction-only role support: FAD'
  finding_ids:
  - rec-f-9365fa81c4b3f88b
  target_ids:
  - record-7baa5feffa5690ec
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fad.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
