# Per-record structured review: Thiamine_Hcl (data/ingredients/mapped/Thiamine_Hcl.yaml)

- Review: 20261017T083000Z-thiamine-hcl
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Thiamine_Hcl (data/ingredients/mapped/Thiamine_Hcl.yaml, record-c375e99738c7374d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Thiamine_Hcl.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Thiamine_Hcl.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c375e99738c7374d | data/ingredients/mapped/Thiamine_Hcl.yaml | maintained | Thiamine_Hcl |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c375e99738c7374d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c375e99738c7374d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c375e99738c7374d | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c375e99738c7374d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c375e99738c7374d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z; reviewed SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732; current SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732; hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Hcl.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:49105 identity and CAS RN pass, but final SSSOM other exports truncated and context-qualified thiamine-HCl labels.

## Findings

### rec-f-f6468688539f8f04: Historical review coverage and residual narrative: Thiamine_Hcl

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c375e99738c7374d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z; reviewed SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732; current SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732; hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Hcl.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:49105 identity and CAS RN pass, but final SSSOM other exports truncated and context-qualified thiamine-HCl labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-df590bc89e1fbb18 | data/ingredients/mapped/Thiamine_Hcl.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1956],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:49105","line":1958,"mapping_status":"MAPPED","ontology_id":"CHEBI:49105","preferred_term":"Thiamine HCl"}],"identifier":"CHEBI:49105","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1996,"edge_count":1996,"occurrences":2009},"occurrence_statistics":{"media_count":1996,"total_occurrences":2009},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:49105","ontology_label":"thiamine hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Thiamine HCl","sssom_rows":[{"data_row":2762,"object_id":"CHEBI:49105","object_label":"thiamine hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Hcl","synonym_count":26} |
| ev-ff205f2a86fe8f13 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1956] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bece4faeaef0a9d1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Thiamine_Hcl; data-row positions=[2762] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2762,"object_id":"CHEBI:49105","object_label":"thiamine hydrochloride","other":"Thiamine\u30fbHCl&#124;Thiamine\u00b7HCl&#124;3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium chloride hydrochloride&#124;3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium dichloride&#124;Thiamin HCl&#124;Thiamin-HCl&#124;Thiamine Dihydrochloride&#124;Thiamine HCl (B ) -&#124;Thiamine HCl (Vitamin B )&#124;Thiamine-HCl&#124;thiamin dichloride&#124;thiamin hydrochloride&#124;thiamine chloride hydrochloride&#124;thiamine dichloride&#124;thiamine(2+) dichloride&#124;thiaminium chloride hydrochloride&#124;Thiamine\u00a0HCl&#124;Thiamine HCl (Vitamin B1)&#124;Thiamine . HCl&#124;Thiamine\u30fbHCl (see below)&#124;CAS:67-03-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine_Hcl","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d7ebe443beae731c | docs/data/mapped_ingredients.csv; CSV lines=[1958] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:49105","line":1958,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1996","ontology_id":"CHEBI:49105","preferred_term":"Thiamine HCl","total_occurrences":"2009"}] |
| ev-3c2c42d69e083edf | reports/yaml_record_review/Thiamine_Hcl.md; &#96;data/ingredients/mapped/Thiamine_Hcl.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:35; Completeness:50; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-654def9dd6b2227f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1283] | context_only | [{"current_record_sha256":"8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732","finding_id":"SEM:4873544803845e62e8b4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-thiamine-hcl
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Thiamine_Hcl (data/ingredients/mapped/Thiamine_Hcl.yaml)'
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
summary: Per-record structured review for Thiamine_Hcl (data/ingredients/mapped/Thiamine_Hcl.yaml,
  record-c375e99738c7374d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Thiamine_Hcl.yaml
    sha256: 8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Thiamine_Hcl.md
    sha256: ec5a23ff73b1837e3a886df652c3ec0bae22b1f4d9b1ee5ea5e7d0b09d33859e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c375e99738c7374d
  path: data/ingredients/mapped/Thiamine_Hcl.yaml
  label: Thiamine_Hcl
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine_Hcl.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Thiamine_Hcl.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Thiamine_Hcl.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c375e99738c7374d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c375e99738c7374d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c375e99738c7374d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c375e99738c7374d
evidence:
- evidence_id: ev-df590bc89e1fbb18
  kind: record_content
  reference: data/ingredients/mapped/Thiamine_Hcl.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1956],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:49105","line":1958,"mapping_status":"MAPPED","ontology_id":"CHEBI:49105","preferred_term":"Thiamine
    HCl"}],"identifier":"CHEBI:49105","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1996,"edge_count":1996,"occurrences":2009},"occurrence_statistics":{"media_count":1996,"total_occurrences":2009},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:49105","ontology_label":"thiamine
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Thiamine HCl","sssom_rows":[{"data_row":2762,"object_id":"CHEBI:49105","object_label":"thiamine
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Hcl","synonym_count":26}'
  snapshot_sha256: 8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732
- evidence_id: ev-ff205f2a86fe8f13
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1956]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bece4faeaef0a9d1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Thiamine_Hcl; data-row positions=[2762]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2762,"object_id":"CHEBI:49105","object_label":"thiamine
    hydrochloride","other":"Thiamine\u30fbHCl|Thiamine\u00b7HCl|3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    chloride hydrochloride|3-[(4-azaniumyl-2-methylpyrimidin-5-yl)methyl]-5-(2-hydroxyethyl)-4-methyl-1,3-thiazol-3-ium
    dichloride|Thiamin HCl|Thiamin-HCl|Thiamine Dihydrochloride|Thiamine HCl (B )
    -|Thiamine HCl (Vitamin B )|Thiamine-HCl|thiamin dichloride|thiamin hydrochloride|thiamine
    chloride hydrochloride|thiamine dichloride|thiamine(2+) dichloride|thiaminium
    chloride hydrochloride|Thiamine\u00a0HCl|Thiamine HCl (Vitamin B1)|Thiamine .
    HCl|Thiamine\u30fbHCl (see below)|CAS:67-03-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine_Hcl","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d7ebe443beae731c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1958]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:49105","line":1958,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1996","ontology_id":"CHEBI:49105","preferred_term":"Thiamine
    HCl","total_occurrences":"2009"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3c2c42d69e083edf
  kind: prior_review
  reference: reports/yaml_record_review/Thiamine_Hcl.md
  locator: '`data/ingredients/mapped/Thiamine_Hcl.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:35; Completeness:50; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ec5a23ff73b1837e3a886df652c3ec0bae22b1f4d9b1ee5ea5e7d0b09d33859e
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Thiamine_Hcl.yaml`,\
    \ remove or retype the\n  truncated vitamin parentheticals and CultureMech `see\
    \ below` label so they\n  cannot publish as exact `other` values. Then rerun strict\
    \ validation, SSSOM\n  publication, synonym-row review, and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-654def9dd6b2227f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1283]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732","finding_id":"SEM:4873544803845e62e8b4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-70c6c80eb784fa28
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c375e99738c7374d
  evidence_ids:
  - ev-df590bc89e1fbb18
  - ev-ff205f2a86fe8f13
  - ev-bece4faeaef0a9d1
  - ev-d7ebe443beae731c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b6d4d35ede029447
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c375e99738c7374d
  evidence_ids:
  - ev-3c2c42d69e083edf
  - ev-df590bc89e1fbb18
  - ev-654def9dd6b2227f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z;
    reviewed SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732;
    current SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Hcl.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:49105
    identity and CAS RN pass, but final SSSOM other exports truncated and context-qualified
    thiamine-HCl labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3c2c42d69e083edf
    - ev-df590bc89e1fbb18
  - name: legacy-native-ids
    value: '["SEM:4873544803845e62e8b4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-df590bc89e1fbb18
    - ev-3c2c42d69e083edf
    - ev-654def9dd6b2227f
findings:
- finding_id: rec-f-f6468688539f8f04
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c375e99738c7374d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Thiamine_Hcl'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z;
    reviewed SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732;
    current SHA-256=8e7d3802dc19872e85d753b6c7a0e1fb34c552311e69c450e697d9f1e55b2732;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Hcl.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:49105
    identity and CAS RN pass, but final SSSOM other exports truncated and context-qualified
    thiamine-HCl labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c375e99738c7374d
  evidence_ids:
  - ev-3c2c42d69e083edf
  - ev-df590bc89e1fbb18
  - ev-654def9dd6b2227f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine_Hcl.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
