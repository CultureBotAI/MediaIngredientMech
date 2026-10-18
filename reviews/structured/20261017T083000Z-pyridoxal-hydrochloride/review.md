# Per-record structured review: Pyridoxal_Hydrochloride (data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml)

- Review: 20261017T083000Z-pyridoxal-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pyridoxal_Hydrochloride (data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml, record-1bbf30e5cbec5335, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1bbf30e5cbec5335 | data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml | maintained | Pyridoxal_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1bbf30e5cbec5335 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1bbf30e5cbec5335 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1bbf30e5cbec5335 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1bbf30e5cbec5335.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1bbf30e5cbec5335.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:05:29Z; reviewed SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27; current SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27; hash_changed=False. Reports=["reports/yaml_record_review/Pyridoxal_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131529 identity and vitamin role pass, but final SSSOM exports a Sigma Aldrich occurrence string.

## Findings

### rec-f-540d5ea68314b830: Historical review coverage and residual narrative: Pyridoxal_Hydrochloride

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1bbf30e5cbec5335.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:05:29Z; reviewed SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27; current SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27; hash_changed=False. Reports=["reports/yaml_record_review/Pyridoxal_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131529 identity and vitamin role pass, but final SSSOM exports a Sigma Aldrich occurrence string.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8897c3b9ba10245f | data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1722],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131529","line":1724,"mapping_status":"MAPPED","ontology_id":"CHEBI:131529","preferred_term":"Pyridoxal hydrochloride"}],"identifier":"CHEBI:131529","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131529","ontology_label":"pyridoxal hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Pyridoxal hydrochloride","sssom_rows":[{"data_row":2378,"object_id":"CHEBI:131529","object_label":"pyridoxal hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyridoxal_Hydrochloride","synonym_count":9} |
| ev-4e5ef6dce4c2edc1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1722] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1789d0687054eb2b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pyridoxal_Hydrochloride; data-row positions=[2378] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2378,"object_id":"CHEBI:131529","object_label":"pyridoxal hydrochloride","other":"2-Methyl-3-hydroxy-4-formyl-5-hydroxymethylpyridine hydrochloride&#124;3-Hydroxy-5-(hydroxymethyl)-2-methylisonicotinaldehyde, hydrochloride&#124;3-hydroxy-5-(hydroxymethyl)-2-methylpyridine-4-carbaldehyde hydrochloride&#124;4-formyl-3-hydroxy-5-(hydroxymethyl)-2-methylpyridin-1-ium chloride&#124;Pyridoxal HCl&#124;Pyridoxal\u00b7HCl&#124;Pyridoxal\u30fbHCl&#124;pyridoxal-HCl (Sigma Aldrich)&#124;CAS:65-22-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyridoxal_Hydrochloride","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-2e43adf04971898e | docs/data/mapped_ingredients.csv; CSV lines=[1724] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131529","line":1724,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:131529","preferred_term":"Pyridoxal hydrochloride","total_occurrences":"36"}] |
| ev-b4c7ce30b69145e3 | reports/yaml_record_review/Pyridoxal_Hydrochloride.md; &#96;data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-06d9b88efcb35b46 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1149] | context_only | [{"current_record_sha256":"c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27","finding_id":"SEM:e00d885455f9967fae92","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyridoxal-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pyridoxal_Hydrochloride (data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Pyridoxal_Hydrochloride (data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml,
  record-1bbf30e5cbec5335, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
    sha256: c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27
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
  - path: reports/yaml_record_review/Pyridoxal_Hydrochloride.md
    sha256: 97e6679b01bdfa055f263982ec7faffe13f2a0332b4fbba7171e1ac7bdc849a1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1bbf30e5cbec5335
  path: data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
  label: Pyridoxal_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1bbf30e5cbec5335
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1bbf30e5cbec5335
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1bbf30e5cbec5335
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1bbf30e5cbec5335
evidence:
- evidence_id: ev-8897c3b9ba10245f
  kind: record_content
  reference: data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1722],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131529","line":1724,"mapping_status":"MAPPED","ontology_id":"CHEBI:131529","preferred_term":"Pyridoxal
    hydrochloride"}],"identifier":"CHEBI:131529","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131529","ontology_label":"pyridoxal
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Pyridoxal hydrochloride","sssom_rows":[{"data_row":2378,"object_id":"CHEBI:131529","object_label":"pyridoxal
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyridoxal_Hydrochloride","synonym_count":9}'
  snapshot_sha256: c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27
- evidence_id: ev-4e5ef6dce4c2edc1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1722]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1789d0687054eb2b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pyridoxal_Hydrochloride; data-row positions=[2378]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2378,"object_id":"CHEBI:131529","object_label":"pyridoxal
    hydrochloride","other":"2-Methyl-3-hydroxy-4-formyl-5-hydroxymethylpyridine hydrochloride|3-Hydroxy-5-(hydroxymethyl)-2-methylisonicotinaldehyde,
    hydrochloride|3-hydroxy-5-(hydroxymethyl)-2-methylpyridine-4-carbaldehyde hydrochloride|4-formyl-3-hydroxy-5-(hydroxymethyl)-2-methylpyridin-1-ium
    chloride|Pyridoxal HCl|Pyridoxal\u00b7HCl|Pyridoxal\u30fbHCl|pyridoxal-HCl (Sigma
    Aldrich)|CAS:65-22-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyridoxal_Hydrochloride","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2e43adf04971898e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1724]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131529","line":1724,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:131529","preferred_term":"Pyridoxal
    hydrochloride","total_occurrences":"36"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b4c7ce30b69145e3
  kind: prior_review
  reference: reports/yaml_record_review/Pyridoxal_Hydrochloride.md
  locator: '`data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 97e6679b01bdfa055f263982ec7faffe13f2a0332b4fbba7171e1ac7bdc849a1
- evidence_id: ev-06d9b88efcb35b46
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1149]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27","finding_id":"SEM:e00d885455f9967fae92","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4e052545197c612a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1bbf30e5cbec5335
  evidence_ids:
  - ev-8897c3b9ba10245f
  - ev-4e5ef6dce4c2edc1
  - ev-1789d0687054eb2b
  - ev-2e43adf04971898e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7f7f38e83a9e53c2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1bbf30e5cbec5335
  evidence_ids:
  - ev-b4c7ce30b69145e3
  - ev-8897c3b9ba10245f
  - ev-06d9b88efcb35b46
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:05:29Z;
    reviewed SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27;
    current SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27;
    hash_changed=False. Reports=["reports/yaml_record_review/Pyridoxal_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:131529 identity and vitamin role pass, but final SSSOM exports a Sigma Aldrich
    occurrence string.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b4c7ce30b69145e3
    - ev-8897c3b9ba10245f
  - name: legacy-native-ids
    value: '["SEM:e00d885455f9967fae92"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8897c3b9ba10245f
    - ev-b4c7ce30b69145e3
    - ev-06d9b88efcb35b46
findings:
- finding_id: rec-f-540d5ea68314b830
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1bbf30e5cbec5335
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Pyridoxal_Hydrochloride'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:05:29Z;
    reviewed SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27;
    current SHA-256=c1650476ac9b84e061cc836ecc99b7e380625b95afd2c70b643bfb575512df27;
    hash_changed=False. Reports=["reports/yaml_record_review/Pyridoxal_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:131529 identity and vitamin role pass, but final SSSOM exports a Sigma Aldrich
    occurrence string.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1bbf30e5cbec5335
  evidence_ids:
  - ev-b4c7ce30b69145e3
  - ev-8897c3b9ba10245f
  - ev-06d9b88efcb35b46
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
