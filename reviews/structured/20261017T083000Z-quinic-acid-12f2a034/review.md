# Per-record structured review: Quinic_Acid (data/ingredients/mapped/Quinic_Acid.yaml)

- Review: 20261017T083000Z-quinic-acid-12f2a034
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Quinic_Acid (data/ingredients/mapped/Quinic_Acid.yaml, record-12f2a034a9cad9bc, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Quinic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Quinic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-12f2a034a9cad9bc | data/ingredients/mapped/Quinic_Acid.yaml | maintained | Quinic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-12f2a034a9cad9bc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-12f2a034a9cad9bc | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-12f2a034a9cad9bc | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-12f2a034a9cad9bc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-12f2a034a9cad9bc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:27:42Z; reviewed SHA-256=c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a; current SHA-256=c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a; hash_changed=False. Reports=["reports/yaml_record_review/Quinic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The broad CHEBI:26493 quinic acid identity and final CAS token pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-12f2a034a9cad9bc.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-3a9088310ef509cc: Reassess prediction-only role support: Quinic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-12f2a034a9cad9bc.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-3a9088310ef509cc

Reassess prediction-only role support: Quinic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b42463445042f8cd | data/ingredients/mapped/Quinic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1738],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26493","line":1740,"mapping_status":"MAPPED","ontology_id":"CHEBI:26493","preferred_term":"Quinic acid"}],"identifier":"CHEBI:26493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":11,"edge_count":11,"occurrences":11},"occurrence_statistics":{"media_count":11,"total_occurrences":11},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26493","ontology_label":"quinic acid","ontology_source":"CHEBI"},"preferred_term":"Quinic acid","sssom_rows":[{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Quinic_Acid","synonym_count":3} |
| ev-dc60f4c28a28466f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1738] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-60a3572795248aad | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Quinic_Acid; data-row positions=[2402] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic acid","other":"CAS:7729-33-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Quinic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d9d668cb587efc56 | docs/data/mapped_ingredients.csv; CSV lines=[1740] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26493","line":1740,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"11","ontology_id":"CHEBI:26493","preferred_term":"Quinic acid","total_occurrences":"11"}] |
| ev-96c434d396aa1256 | reports/yaml_record_review/Quinic_Acid.md; &#96;data/ingredients/mapped/Quinic_Acid.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3bb267c72df0c342 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1160,2021] | context_only | [{"current_record_sha256":"c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a","finding_id":"SEM:5fad7a4574c94d3620a9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a","finding_id":"SEM:4ab5d190cb80b00c4dad","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7730243072927d43 | data/ingredients/mapped/Quinic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1738],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26493","line":1740,"mapping_status":"MAPPED","ontology_id":"CHEBI:26493","preferred_term":"Quinic acid"}],"identifier":"CHEBI:26493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":11,"edge_count":11,"occurrences":11},"occurrence_statistics":{"media_count":11,"total_occurrences":11},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26493","ontology_label":"quinic acid","ontology_source":"CHEBI"},"preferred_term":"Quinic acid","sssom_rows":[{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Quinic_Acid","synonym_count":3} |
| ev-0d30d03f7672b3ac | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-3a9088310ef509cc] | context_only | Predecessor structured review finding f-3a9088310ef509cc in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-quinic-acid-12f2a034
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Quinic_Acid (data/ingredients/mapped/Quinic_Acid.yaml)'
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
summary: Per-record structured review for Quinic_Acid (data/ingredients/mapped/Quinic_Acid.yaml,
  record-12f2a034a9cad9bc, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Quinic_Acid.yaml
    sha256: c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Quinic_Acid.md
    sha256: cd8613e6c284579f4c425e0384a8e8fce052e5e7e0c33736e9b71d5dadece7df
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-12f2a034a9cad9bc
  path: data/ingredients/mapped/Quinic_Acid.yaml
  label: Quinic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Quinic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Quinic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Quinic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-12f2a034a9cad9bc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-b42463445042f8cd
  - ev-dc60f4c28a28466f
  - ev-60a3572795248aad
  - ev-d9d668cb587efc56
  - ev-7730243072927d43
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-b42463445042f8cd
  - ev-3bb267c72df0c342
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-96c434d396aa1256
  - ev-3bb267c72df0c342
  - ev-0d30d03f7672b3ac
evidence:
- evidence_id: ev-b42463445042f8cd
  kind: record_content
  reference: data/ingredients/mapped/Quinic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1738],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26493","line":1740,"mapping_status":"MAPPED","ontology_id":"CHEBI:26493","preferred_term":"Quinic
    acid"}],"identifier":"CHEBI:26493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":11,"edge_count":11,"occurrences":11},"occurrence_statistics":{"media_count":11,"total_occurrences":11},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26493","ontology_label":"quinic
    acid","ontology_source":"CHEBI"},"preferred_term":"Quinic acid","sssom_rows":[{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Quinic_Acid","synonym_count":3}'
  snapshot_sha256: c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a
- evidence_id: ev-dc60f4c28a28466f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1738]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-60a3572795248aad
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Quinic_Acid; data-row positions=[2402]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic
    acid","other":"CAS:7729-33-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Quinic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d9d668cb587efc56
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1740]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26493","line":1740,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"11","ontology_id":"CHEBI:26493","preferred_term":"Quinic
    acid","total_occurrences":"11"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-96c434d396aa1256
  kind: prior_review
  reference: reports/yaml_record_review/Quinic_Acid.md
  locator: '`data/ingredients/mapped/Quinic_Acid.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cd8613e6c284579f4c425e0384a8e8fce052e5e7e0c33736e9b71d5dadece7df
- evidence_id: ev-3bb267c72df0c342
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1160,2021]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a","finding_id":"SEM:5fad7a4574c94d3620a9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a","finding_id":"SEM:4ab5d190cb80b00c4dad","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7730243072927d43
  kind: record_content
  reference: data/ingredients/mapped/Quinic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1738],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26493","line":1740,"mapping_status":"MAPPED","ontology_id":"CHEBI:26493","preferred_term":"Quinic
    acid"}],"identifier":"CHEBI:26493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":11,"edge_count":11,"occurrences":11},"occurrence_statistics":{"media_count":11,"total_occurrences":11},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26493","ontology_label":"quinic
    acid","ontology_source":"CHEBI"},"preferred_term":"Quinic acid","sssom_rows":[{"data_row":2402,"object_id":"CHEBI:26493","object_label":"quinic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Quinic_Acid","synonym_count":3}'
  snapshot_sha256: c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a
- evidence_id: ev-0d30d03f7672b3ac
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-3a9088310ef509cc]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-3a9088310ef509cc in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-1c5d746117d71af6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-b42463445042f8cd
  - ev-dc60f4c28a28466f
  - ev-60a3572795248aad
  - ev-d9d668cb587efc56
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9eedc0e7a5dcdf57
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-96c434d396aa1256
  - ev-b42463445042f8cd
  - ev-3bb267c72df0c342
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:27:42Z;
    reviewed SHA-256=c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a;
    current SHA-256=c1c2fc353bbf1ef458988b3aad173cde353b976ef805dfdd2bead0878960559a;
    hash_changed=False. Reports=["reports/yaml_record_review/Quinic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The broad CHEBI:26493
    quinic acid identity and final CAS token pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-96c434d396aa1256
    - ev-b42463445042f8cd
  - name: legacy-native-ids
    value: '["SEM:5fad7a4574c94d3620a9","SEM:4ab5d190cb80b00c4dad"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b42463445042f8cd
    - ev-96c434d396aa1256
    - ev-3bb267c72df0c342
- assessment_id: a-7730243072927d43
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-96c434d396aa1256
  - ev-7730243072927d43
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-96c434d396aa1256
    - ev-7730243072927d43
findings:
- finding_id: rec-f-3a9088310ef509cc
  issue_key: mim-reconciliation-role-support-12f2a034a9cad9bc
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Quinic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-12f2a034a9cad9bc
  evidence_ids:
  - ev-96c434d396aa1256
  - ev-7730243072927d43
  - ev-0d30d03f7672b3ac
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Quinic_Acid.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-3a9088310ef509cc
actions:
- action_id: rec-action-3a9088310ef509cc
  description: 'Reassess prediction-only role support: Quinic acid'
  finding_ids:
  - rec-f-3a9088310ef509cc
  target_ids:
  - record-12f2a034a9cad9bc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Quinic_Acid.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
