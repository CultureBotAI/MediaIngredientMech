# Per-record structured review: L-_-ergothioneine (data/ingredients/mapped/L-_-ergothioneine.yaml)

- Review: 20261017T083000Z-l-ergothioneine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-_-ergothioneine (data/ingredients/mapped/L-_-ergothioneine.yaml, record-6e9897c247f1e30c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-_-ergothioneine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-_-ergothioneine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6e9897c247f1e30c | data/ingredients/mapped/L-_-ergothioneine.yaml | maintained | L-_-ergothioneine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6e9897c247f1e30c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6e9897c247f1e30c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6e9897c247f1e30c | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6e9897c247f1e30c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6e9897c247f1e30c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:23:47Z; reviewed SHA-256=c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073; current SHA-256=c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073; hash_changed=False. Reports=["reports/yaml_record_review/L-_-ergothioneine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI lookup identity, active CHEBI:4828 grounding, ChEBI synonym, PubChem structure, and final SSSOM row pass, but AMINO_ACID_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-6e9897c247f1e30c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-31a5aa175b01aaaf: Reassess prediction-only role support: L-(+)-Ergothioneine

major / open / confirmed; issue key: mim-reconciliation-role-support-6e9897c247f1e30c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-31a5aa175b01aaaf

Reassess prediction-only role support: L-(+)-Ergothioneine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4fbfe88ad134440e | data/ingredients/mapped/L-_-ergothioneine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1210],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4828","line":1212,"mapping_status":"MAPPED","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine"}],"identifier":"CHEBI:4828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:4828","ontology_label":"ergothioneine","ontology_source":"CHEBI"},"preferred_term":"L-(+)-Ergothioneine","sssom_rows":[{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-ergothioneine","synonym_count":1} |
| ev-3288519aa4ace6b7 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1210] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f7ccdbfdd72f21fb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-_-ergothioneine; data-row positions=[1590] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","other":"(2S)-3-(2-mercapto-1H-imidazol-5-yl)-2-(trimethylazaniumyl)propanoate&#124;CAS:497-30-3","predicate_id":"skos:exactMatch","subject_id":"MIM:L-_-ergothioneine","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ef1b332b4af0fb38 | docs/data/mapped_ingredients.csv; CSV lines=[1212] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:4828","line":1212,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine","total_occurrences":"0"}] |
| ev-6c1bb04eb42b4608 | reports/yaml_record_review/L-_-ergothioneine.md; &#96;data/ingredients/mapped/L-_-ergothioneine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-770ec0d905c30cea | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[800,1772] | context_only | [{"current_record_sha256":"c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073","finding_id":"SEM:923161e21d459decd9b8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073","finding_id":"SEM:5e6b182a8dddce7c7b41","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-208117da8af687ac | data/ingredients/mapped/L-_-ergothioneine.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1210],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4828","line":1212,"mapping_status":"MAPPED","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine"}],"identifier":"CHEBI:4828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:4828","ontology_label":"ergothioneine","ontology_source":"CHEBI"},"preferred_term":"L-(+)-Ergothioneine","sssom_rows":[{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-ergothioneine","synonym_count":1} |
| ev-af580e46203611c0 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-31a5aa175b01aaaf] | context_only | Predecessor structured review finding f-31a5aa175b01aaaf in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-ergothioneine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-_-ergothioneine (data/ingredients/mapped/L-_-ergothioneine.yaml)'
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
summary: Per-record structured review for L-_-ergothioneine (data/ingredients/mapped/L-_-ergothioneine.yaml,
  record-6e9897c247f1e30c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-_-ergothioneine.yaml
    sha256: c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073
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
  - path: reports/yaml_record_review/L-_-ergothioneine.md
    sha256: 2386fa97497eccb19d97b95e21b78230d03e1d419f2afceb0d148250945babdb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6e9897c247f1e30c
  path: data/ingredients/mapped/L-_-ergothioneine.yaml
  label: L-_-ergothioneine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-ergothioneine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-_-ergothioneine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-_-ergothioneine.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6e9897c247f1e30c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-4fbfe88ad134440e
  - ev-3288519aa4ace6b7
  - ev-f7ccdbfdd72f21fb
  - ev-ef1b332b4af0fb38
  - ev-208117da8af687ac
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-4fbfe88ad134440e
  - ev-770ec0d905c30cea
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-6c1bb04eb42b4608
  - ev-770ec0d905c30cea
  - ev-af580e46203611c0
evidence:
- evidence_id: ev-4fbfe88ad134440e
  kind: record_content
  reference: data/ingredients/mapped/L-_-ergothioneine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1210],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4828","line":1212,"mapping_status":"MAPPED","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine"}],"identifier":"CHEBI:4828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:4828","ontology_label":"ergothioneine","ontology_source":"CHEBI"},"preferred_term":"L-(+)-Ergothioneine","sssom_rows":[{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-ergothioneine","synonym_count":1}'
  snapshot_sha256: c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073
- evidence_id: ev-3288519aa4ace6b7
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1210]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f7ccdbfdd72f21fb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-_-ergothioneine; data-row positions=[1590]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","other":"(2S)-3-(2-mercapto-1H-imidazol-5-yl)-2-(trimethylazaniumyl)propanoate|CAS:497-30-3","predicate_id":"skos:exactMatch","subject_id":"MIM:L-_-ergothioneine","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ef1b332b4af0fb38
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1212]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:4828","line":1212,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6c1bb04eb42b4608
  kind: prior_review
  reference: reports/yaml_record_review/L-_-ergothioneine.md
  locator: '`data/ingredients/mapped/L-_-ergothioneine.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:32; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2386fa97497eccb19d97b95e21b78230d03e1d419f2afceb0d148250945babdb
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ unless an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-(+)-\n  ergothioneine as an amino acid source.\n- Rerun strict, term, round-trip,\
    \ role, component, and SSSOM validation after\n  the role change."
- evidence_id: ev-770ec0d905c30cea
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[800,1772]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073","finding_id":"SEM:923161e21d459decd9b8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073","finding_id":"SEM:5e6b182a8dddce7c7b41","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-208117da8af687ac
  kind: record_content
  reference: data/ingredients/mapped/L-_-ergothioneine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1210],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4828","line":1212,"mapping_status":"MAPPED","ontology_id":"CHEBI:4828","preferred_term":"L-(+)-Ergothioneine"}],"identifier":"CHEBI:4828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:4828","ontology_label":"ergothioneine","ontology_source":"CHEBI"},"preferred_term":"L-(+)-Ergothioneine","sssom_rows":[{"data_row":1590,"object_id":"CHEBI:4828","object_label":"ergothioneine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-_-ergothioneine","synonym_count":1}'
  snapshot_sha256: c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073
- evidence_id: ev-af580e46203611c0
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-31a5aa175b01aaaf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-31a5aa175b01aaaf in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-180838454c8a60a4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-4fbfe88ad134440e
  - ev-3288519aa4ace6b7
  - ev-f7ccdbfdd72f21fb
  - ev-ef1b332b4af0fb38
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-56a260cce70104d4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-6c1bb04eb42b4608
  - ev-4fbfe88ad134440e
  - ev-770ec0d905c30cea
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:23:47Z;
    reviewed SHA-256=c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073;
    current SHA-256=c2ee1e304fd23914828e03ff33ba609878fefe03cdf94570b670c4ecd1fb0073;
    hash_changed=False. Reports=["reports/yaml_record_review/L-_-ergothioneine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI
    lookup identity, active CHEBI:4828 grounding, ChEBI synonym, PubChem structure,
    and final SSSOM row pass, but AMINO_ACID_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c1bb04eb42b4608
    - ev-4fbfe88ad134440e
  - name: legacy-native-ids
    value: '["SEM:923161e21d459decd9b8","SEM:5e6b182a8dddce7c7b41"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4fbfe88ad134440e
    - ev-6c1bb04eb42b4608
    - ev-770ec0d905c30cea
- assessment_id: a-208117da8af687ac
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-6c1bb04eb42b4608
  - ev-208117da8af687ac
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c1bb04eb42b4608
    - ev-208117da8af687ac
findings:
- finding_id: rec-f-31a5aa175b01aaaf
  issue_key: mim-reconciliation-role-support-6e9897c247f1e30c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-(+)-Ergothioneine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6e9897c247f1e30c
  evidence_ids:
  - ev-6c1bb04eb42b4608
  - ev-208117da8af687ac
  - ev-af580e46203611c0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-ergothioneine.yaml
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
    finding_id: f-31a5aa175b01aaaf
actions:
- action_id: rec-action-31a5aa175b01aaaf
  description: 'Reassess prediction-only role support: L-(+)-Ergothioneine'
  finding_ids:
  - rec-f-31a5aa175b01aaaf
  target_ids:
  - record-6e9897c247f1e30c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-_-ergothioneine.yaml
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
