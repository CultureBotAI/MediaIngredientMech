# Per-record structured review: Nahso3 (data/ingredients/mapped/Nahso3.yaml)

- Review: 20261017T083000Z-nahso3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nahso3 (data/ingredients/mapped/Nahso3.yaml, record-7d9e96652f6156c7, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nahso3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nahso3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7d9e96652f6156c7 | data/ingredients/mapped/Nahso3.yaml | maintained | Nahso3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7d9e96652f6156c7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7d9e96652f6156c7 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7d9e96652f6156c7 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7d9e96652f6156c7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7d9e96652f6156c7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z; reviewed SHA-256=6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c; current SHA-256=6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c; hash_changed=False. Reports=["reports/yaml_record_review/Nahso3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26709 sodium hydrogensulfite identity passes, but REDUCING_AGENT is only a provisional LLM role.

### Historical provisional-role concern

evidence: concern. Targets: record-7d9e96652f6156c7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ba047b4cc2010549: Reassess prediction-only role support: NaHSO3

major / open / confirmed; issue key: mim-reconciliation-role-support-7d9e96652f6156c7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ba047b4cc2010549

Reassess prediction-only role support: NaHSO3

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2961e63029618cbe | data/ingredients/mapped/Nahso3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26709","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3"}],"identifier":"CHEBI:26709","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26709","ontology_label":"sodium hydrogensulfite","ontology_source":"CHEBI"},"preferred_term":"NaHSO3","sssom_rows":[{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium hydrogensulfite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahso3","synonym_count":16} |
| ev-b63b2ea970e1df2d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1525] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-87c7514aea605712 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nahso3; data-row positions=[2038] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium hydrogensulfite","other":"E 222&#124;E222&#124;Natriumbisulfit&#124;Natriumhydrogensulfit&#124;Sodium Bisulfite&#124;hydrogen sulfite sodium&#124;primaeres Natriumsulfit&#124;saures Natriumsulfit&#124;sodium bisulphite&#124;sodium hydrogen sulfite&#124;sulfurous acid monosodium salt&#124;sulfurous acid sodium salt&#124;sulfurous acid, monosodium salt&#124;sulfurous acid, sodium salt (1:1)&#124;CAS:7631-90-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nahso3","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-edc0534f9dfe4bae | docs/data/mapped_ingredients.csv; CSV lines=[1527] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26709","line":1527,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3","total_occurrences":"5"}] |
| ev-768e888be61023de | reports/yaml_record_review/Nahso3.md; &#96;data/ingredients/mapped/Nahso3.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-80eb18589b95b37e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1029,1940] | context_only | [{"current_record_sha256":"6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c","finding_id":"SEM:0072f46add50ee09ce78","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c","finding_id":"SEM:59a4ff4481faee4c6b4e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9e7ce58d39008a0c | data/ingredients/mapped/Nahso3.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26709","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3"}],"identifier":"CHEBI:26709","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26709","ontology_label":"sodium hydrogensulfite","ontology_source":"CHEBI"},"preferred_term":"NaHSO3","sssom_rows":[{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium hydrogensulfite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahso3","synonym_count":16} |
| ev-51b67f5fab2c942a | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-ba047b4cc2010549] | context_only | Predecessor structured review finding f-ba047b4cc2010549 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nahso3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nahso3 (data/ingredients/mapped/Nahso3.yaml)'
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
summary: Per-record structured review for Nahso3 (data/ingredients/mapped/Nahso3.yaml,
  record-7d9e96652f6156c7, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nahso3.yaml
    sha256: 6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Nahso3.md
    sha256: 44df6a47f5db355bde2b4bb49d533e593dc6550bc80ac9feae804a98ec90e9ec
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7d9e96652f6156c7
  path: data/ingredients/mapped/Nahso3.yaml
  label: Nahso3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nahso3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nahso3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nahso3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7d9e96652f6156c7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-2961e63029618cbe
  - ev-b63b2ea970e1df2d
  - ev-87c7514aea605712
  - ev-edc0534f9dfe4bae
  - ev-9e7ce58d39008a0c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-2961e63029618cbe
  - ev-80eb18589b95b37e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-768e888be61023de
  - ev-80eb18589b95b37e
  - ev-51b67f5fab2c942a
evidence:
- evidence_id: ev-2961e63029618cbe
  kind: record_content
  reference: data/ingredients/mapped/Nahso3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26709","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3"}],"identifier":"CHEBI:26709","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26709","ontology_label":"sodium
    hydrogensulfite","ontology_source":"CHEBI"},"preferred_term":"NaHSO3","sssom_rows":[{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium
    hydrogensulfite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahso3","synonym_count":16}'
  snapshot_sha256: 6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c
- evidence_id: ev-b63b2ea970e1df2d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1525]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-87c7514aea605712
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nahso3; data-row positions=[2038]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium
    hydrogensulfite","other":"E 222|E222|Natriumbisulfit|Natriumhydrogensulfit|Sodium
    Bisulfite|hydrogen sulfite sodium|primaeres Natriumsulfit|saures Natriumsulfit|sodium
    bisulphite|sodium hydrogen sulfite|sulfurous acid monosodium salt|sulfurous acid
    sodium salt|sulfurous acid, monosodium salt|sulfurous acid, sodium salt (1:1)|CAS:7631-90-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nahso3","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-edc0534f9dfe4bae
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1527]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26709","line":1527,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-768e888be61023de
  kind: prior_review
  reference: reports/yaml_record_review/Nahso3.md
  locator: '`data/ingredients/mapped/Nahso3.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:29; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 44df6a47f5db355bde2b4bb49d533e593dc6550bc80ac9feae804a98ec90e9ec
  quote: "Recommended Edits:\n- Major: either remove `physicochemical_roles.REDUCING_AGENT`\
    \ from\n  `data/ingredients/mapped/Nahso3.yaml` or replace its LLM-only placeholder\n\
    \  with source-backed evidence from maintained role-text or literature inputs.\n\
    \  Rerun strict validation and final SSSOM validation after the role facet\n \
    \ change."
- evidence_id: ev-80eb18589b95b37e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1029,1940]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c","finding_id":"SEM:0072f46add50ee09ce78","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c","finding_id":"SEM:59a4ff4481faee4c6b4e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9e7ce58d39008a0c
  kind: record_content
  reference: data/ingredients/mapped/Nahso3.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26709","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:26709","preferred_term":"NaHSO3"}],"identifier":"CHEBI:26709","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26709","ontology_label":"sodium
    hydrogensulfite","ontology_source":"CHEBI"},"preferred_term":"NaHSO3","sssom_rows":[{"data_row":2038,"object_id":"CHEBI:26709","object_label":"sodium
    hydrogensulfite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahso3","synonym_count":16}'
  snapshot_sha256: 6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c
- evidence_id: ev-51b67f5fab2c942a
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-ba047b4cc2010549]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ba047b4cc2010549 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-5ecdf95a92d47fb4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-2961e63029618cbe
  - ev-b63b2ea970e1df2d
  - ev-87c7514aea605712
  - ev-edc0534f9dfe4bae
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ad6f240d6d1d5f3c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-768e888be61023de
  - ev-2961e63029618cbe
  - ev-80eb18589b95b37e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z;
    reviewed SHA-256=6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c;
    current SHA-256=6ba7bec792543bd48b08a5f1f132d0ffda156b637b2662e659a7805552eafb7c;
    hash_changed=False. Reports=["reports/yaml_record_review/Nahso3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:26709 sodium
    hydrogensulfite identity passes, but REDUCING_AGENT is only a provisional LLM
    role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-768e888be61023de
    - ev-2961e63029618cbe
  - name: legacy-native-ids
    value: '["SEM:0072f46add50ee09ce78","SEM:59a4ff4481faee4c6b4e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2961e63029618cbe
    - ev-768e888be61023de
    - ev-80eb18589b95b37e
- assessment_id: a-9e7ce58d39008a0c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-768e888be61023de
  - ev-9e7ce58d39008a0c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-768e888be61023de
    - ev-9e7ce58d39008a0c
findings:
- finding_id: rec-f-ba047b4cc2010549
  issue_key: mim-reconciliation-role-support-7d9e96652f6156c7
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: NaHSO3'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7d9e96652f6156c7
  evidence_ids:
  - ev-768e888be61023de
  - ev-9e7ce58d39008a0c
  - ev-51b67f5fab2c942a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nahso3.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-ba047b4cc2010549
actions:
- action_id: rec-action-ba047b4cc2010549
  description: 'Reassess prediction-only role support: NaHSO3'
  finding_ids:
  - rec-f-ba047b4cc2010549
  target_ids:
  - record-7d9e96652f6156c7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nahso3.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
