# Per-record structured review: Lactitol (data/ingredients/mapped/Lactitol.yaml)

- Review: 20261017T083000Z-lactitol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lactitol (data/ingredients/mapped/Lactitol.yaml, record-4e32f7f9b75f2879, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lactitol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lactitol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4e32f7f9b75f2879 | data/ingredients/mapped/Lactitol.yaml | maintained | Lactitol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4e32f7f9b75f2879 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4e32f7f9b75f2879 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4e32f7f9b75f2879 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4e32f7f9b75f2879.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4e32f7f9b75f2879.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:42:25Z; reviewed SHA-256=c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a; current SHA-256=c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a; hash_changed=False. Reports=["reports/yaml_record_review/Lactitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75323 identity, CAS value, PubChem structure, synonym, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-4e32f7f9b75f2879.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-125a8b43f6152cd4: Reassess prediction-only role support: Lactitol

major / open / confirmed; issue key: mim-reconciliation-role-support-4e32f7f9b75f2879.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-125a8b43f6152cd4

Reassess prediction-only role support: Lactitol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8a719b7a98a6b9ca | data/ingredients/mapped/Lactitol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1275],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75323","line":1277,"mapping_status":"MAPPED","ontology_id":"CHEBI:75323","preferred_term":"Lactitol"}],"identifier":"CHEBI:75323","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75323","ontology_label":"lactitol","ontology_source":"CHEBI"},"preferred_term":"Lactitol","sssom_rows":[{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactitol","synonym_count":1} |
| ev-e835e6e7d653f387 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1275] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c856bc5e5f482537 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lactitol; data-row positions=[1654] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","other":"4-O-beta-D-galactopyranosyl-D-glucitol&#124;CAS:585-86-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactitol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-59cb86d32d2258fc | docs/data/mapped_ingredients.csv; CSV lines=[1277] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75323","line":1277,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:75323","preferred_term":"Lactitol","total_occurrences":"0"}] |
| ev-4bd7049a47340c7b | reports/yaml_record_review/Lactitol.md; &#96;data/ingredients/mapped/Lactitol.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:28; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-81d0641fa09c9cc3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[844,1716] | context_only | [{"current_record_sha256":"c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a","finding_id":"SEM:f879a151f2141d66b224","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a","finding_id":"SEM:1e536df4c318181d37c5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-753d8639c9cdbaea | data/ingredients/mapped/Lactitol.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1275],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75323","line":1277,"mapping_status":"MAPPED","ontology_id":"CHEBI:75323","preferred_term":"Lactitol"}],"identifier":"CHEBI:75323","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75323","ontology_label":"lactitol","ontology_source":"CHEBI"},"preferred_term":"Lactitol","sssom_rows":[{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactitol","synonym_count":1} |
| ev-2294c7a07473b67b | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-125a8b43f6152cd4] | context_only | Predecessor structured review finding f-125a8b43f6152cd4 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lactitol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lactitol (data/ingredients/mapped/Lactitol.yaml)'
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
summary: Per-record structured review for Lactitol (data/ingredients/mapped/Lactitol.yaml,
  record-4e32f7f9b75f2879, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lactitol.yaml
    sha256: c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Lactitol.md
    sha256: 23c4dc8369828108bc2cb5918ee0196e125813ec490a0e597aa42bf9030dc950
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4e32f7f9b75f2879
  path: data/ingredients/mapped/Lactitol.yaml
  label: Lactitol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactitol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lactitol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lactitol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4e32f7f9b75f2879
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-8a719b7a98a6b9ca
  - ev-e835e6e7d653f387
  - ev-c856bc5e5f482537
  - ev-59cb86d32d2258fc
  - ev-753d8639c9cdbaea
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-8a719b7a98a6b9ca
  - ev-81d0641fa09c9cc3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-4bd7049a47340c7b
  - ev-81d0641fa09c9cc3
  - ev-2294c7a07473b67b
evidence:
- evidence_id: ev-8a719b7a98a6b9ca
  kind: record_content
  reference: data/ingredients/mapped/Lactitol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1275],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75323","line":1277,"mapping_status":"MAPPED","ontology_id":"CHEBI:75323","preferred_term":"Lactitol"}],"identifier":"CHEBI:75323","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75323","ontology_label":"lactitol","ontology_source":"CHEBI"},"preferred_term":"Lactitol","sssom_rows":[{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactitol","synonym_count":1}'
  snapshot_sha256: c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a
- evidence_id: ev-e835e6e7d653f387
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1275]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c856bc5e5f482537
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lactitol; data-row positions=[1654]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","other":"4-O-beta-D-galactopyranosyl-D-glucitol|CAS:585-86-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactitol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-59cb86d32d2258fc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1277]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75323","line":1277,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:75323","preferred_term":"Lactitol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4bd7049a47340c7b
  kind: prior_review
  reference: reports/yaml_record_review/Lactitol.md
  locator: '`data/ingredients/mapped/Lactitol.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:28; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 23c4dc8369828108bc2cb5918ee0196e125813ec490a0e597aa42bf9030dc950
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Lactitol.yaml` with inspected source evidence\
    \ for\n  exact lactitol use, or remove the provisional role.\n- Sync the aggregate\
    \ copy and regenerate derived products after the YAML\n  changes; rerun strict,\
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-81d0641fa09c9cc3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[844,1716]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a","finding_id":"SEM:f879a151f2141d66b224","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a","finding_id":"SEM:1e536df4c318181d37c5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-753d8639c9cdbaea
  kind: record_content
  reference: data/ingredients/mapped/Lactitol.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1275],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75323","line":1277,"mapping_status":"MAPPED","ontology_id":"CHEBI:75323","preferred_term":"Lactitol"}],"identifier":"CHEBI:75323","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75323","ontology_label":"lactitol","ontology_source":"CHEBI"},"preferred_term":"Lactitol","sssom_rows":[{"data_row":1654,"object_id":"CHEBI:75323","object_label":"lactitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactitol","synonym_count":1}'
  snapshot_sha256: c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a
- evidence_id: ev-2294c7a07473b67b
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-125a8b43f6152cd4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-125a8b43f6152cd4 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-d5b3e0085b87b0ee
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-8a719b7a98a6b9ca
  - ev-e835e6e7d653f387
  - ev-c856bc5e5f482537
  - ev-59cb86d32d2258fc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5fa7e9b38e78f12b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-4bd7049a47340c7b
  - ev-8a719b7a98a6b9ca
  - ev-81d0641fa09c9cc3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:42:25Z;
    reviewed SHA-256=c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a;
    current SHA-256=c623b2bb321dbe1f1995986a5a69f454cb23825f67d71bbfdbdf2ae9f98efc8a;
    hash_changed=False. Reports=["reports/yaml_record_review/Lactitol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:75323 identity,
    CAS value, PubChem structure, synonym, and final SSSOM row pass, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4bd7049a47340c7b
    - ev-8a719b7a98a6b9ca
  - name: legacy-native-ids
    value: '["SEM:f879a151f2141d66b224","SEM:1e536df4c318181d37c5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8a719b7a98a6b9ca
    - ev-4bd7049a47340c7b
    - ev-81d0641fa09c9cc3
- assessment_id: a-753d8639c9cdbaea
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-4bd7049a47340c7b
  - ev-753d8639c9cdbaea
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4bd7049a47340c7b
    - ev-753d8639c9cdbaea
findings:
- finding_id: rec-f-125a8b43f6152cd4
  issue_key: mim-reconciliation-role-support-4e32f7f9b75f2879
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lactitol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4e32f7f9b75f2879
  evidence_ids:
  - ev-4bd7049a47340c7b
  - ev-753d8639c9cdbaea
  - ev-2294c7a07473b67b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactitol.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-125a8b43f6152cd4
actions:
- action_id: rec-action-125a8b43f6152cd4
  description: 'Reassess prediction-only role support: Lactitol'
  finding_ids:
  - rec-f-125a8b43f6152cd4
  target_ids:
  - record-4e32f7f9b75f2879
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactitol.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
