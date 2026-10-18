# Per-record structured review: Arginine (data/ingredients/mapped/Arginine.yaml)

- Review: 20261017T083000Z-arginine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Arginine (data/ingredients/mapped/Arginine.yaml, record-fadca324071cd86a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Arginine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Arginine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fadca324071cd86a | data/ingredients/mapped/Arginine.yaml | maintained | Arginine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fadca324071cd86a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fadca324071cd86a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fadca324071cd86a | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fadca324071cd86a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fadca324071cd86a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:40:20Z; reviewed SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73; current SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73; hash_changed=False. Reports=["reports/yaml_record_review/Arginine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI identity, formula, structure, CultureMech occurrences, nitrogen-source role, and SSSOM row pass, but role/property strings remain in synonyms.

## Findings

### rec-f-e817a2eb6d0e44ff: Historical review coverage and residual narrative: Arginine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fadca324071cd86a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:40:20Z; reviewed SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73; current SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73; hash_changed=False. Reports=["reports/yaml_record_review/Arginine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI identity, formula, structure, CultureMech occurrences, nitrogen-source role, and SSSOM row pass, but role/property strings remain in synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0a9da57ac5380c34 | data/ingredients/mapped/Arginine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[515],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29016","line":517,"mapping_status":"MAPPED","ontology_id":"CHEBI:29016","preferred_term":"Arginine"}],"identifier":"CHEBI:29016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:29016","ontology_label":"arginine","ontology_source":"CHEBI"},"preferred_term":"Arginine","sssom_rows":[{"data_row":428,"object_id":"CHEBI:29016","object_label":"arginine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arginine","synonym_count":9} |
| ev-6e5ec6f7fab8e39f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [515] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a820ce24443752a7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Arginine; data-row positions=[428] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":428,"object_id":"CHEBI:29016","object_label":"arginine","other":"2-Amino-5-guanidinovaleric acid&#124;2-amino-5-(carbamimidamido)pentanoic acid&#124;2-amino-5-guanidinopentanoic acid&#124;Arginin&#124;Harg&#124;CAS:74-79-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Arginine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-ce67407da3651639 | docs/data/mapped_ingredients.csv; CSV lines=[517] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29016","line":517,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"43","ontology_id":"CHEBI:29016","preferred_term":"Arginine","total_occurrences":"43"}] |
| ev-ec065bea5464f883 | reports/yaml_record_review/Arginine.md; &#96;data/ingredients/mapped/Arginine.yaml&#96;:2; Verdict:4; Identity:10; Validation:26; Evidence:43; Completeness:62; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-00b39e03c96fc5ae | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[276] | context_only | [{"current_record_sha256":"a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73","finding_id":"SEM:2c25f265978f0f90872c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-arginine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Arginine (data/ingredients/mapped/Arginine.yaml)'
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
summary: Per-record structured review for Arginine (data/ingredients/mapped/Arginine.yaml,
  record-fadca324071cd86a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Arginine.yaml
    sha256: a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Arginine.md
    sha256: ac3fabc5e2928466fbdb90ebd1135e0f04e8ea1b09672f21e07bfc9763e51f65
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fadca324071cd86a
  path: data/ingredients/mapped/Arginine.yaml
  label: Arginine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Arginine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Arginine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Arginine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fadca324071cd86a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fadca324071cd86a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fadca324071cd86a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fadca324071cd86a
evidence:
- evidence_id: ev-0a9da57ac5380c34
  kind: record_content
  reference: data/ingredients/mapped/Arginine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[515],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29016","line":517,"mapping_status":"MAPPED","ontology_id":"CHEBI:29016","preferred_term":"Arginine"}],"identifier":"CHEBI:29016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:29016","ontology_label":"arginine","ontology_source":"CHEBI"},"preferred_term":"Arginine","sssom_rows":[{"data_row":428,"object_id":"CHEBI:29016","object_label":"arginine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arginine","synonym_count":9}'
  snapshot_sha256: a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73
- evidence_id: ev-6e5ec6f7fab8e39f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [515]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a820ce24443752a7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Arginine; data-row positions=[428]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":428,"object_id":"CHEBI:29016","object_label":"arginine","other":"2-Amino-5-guanidinovaleric
    acid|2-amino-5-(carbamimidamido)pentanoic acid|2-amino-5-guanidinopentanoic acid|Arginin|Harg|CAS:74-79-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Arginine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ce67407da3651639
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[517]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29016","line":517,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"43","ontology_id":"CHEBI:29016","preferred_term":"Arginine","total_occurrences":"43"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ec065bea5464f883
  kind: prior_review
  reference: reports/yaml_record_review/Arginine.md
  locator: '`data/ingredients/mapped/Arginine.yaml`:2; Verdict:4; Identity:10; Validation:26;
    Evidence:43; Completeness:62; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ac3fabc5e2928466fbdb90ebd1135e0f04e8ea1b09672f21e07bfc9763e51f65
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Arginine.yaml`, remove\
    \ the four `RAW_TEXT`\n  CultureMech role/property strings from `synonyms`; keep\
    \ their nitrogen-source\n  content on `nutritional_roles.NITROGEN_SOURCE`.\n-\
    \ Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arginine.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-00b39e03c96fc5ae
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[276]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73","finding_id":"SEM:2c25f265978f0f90872c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bd87abb11e9b4d22
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fadca324071cd86a
  evidence_ids:
  - ev-0a9da57ac5380c34
  - ev-6e5ec6f7fab8e39f
  - ev-a820ce24443752a7
  - ev-ce67407da3651639
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c95ff7c613e89608
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fadca324071cd86a
  evidence_ids:
  - ev-ec065bea5464f883
  - ev-0a9da57ac5380c34
  - ev-00b39e03c96fc5ae
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:40:20Z;
    reviewed SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73;
    current SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73;
    hash_changed=False. Reports=["reports/yaml_record_review/Arginine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The generic CHEBI identity,
    formula, structure, CultureMech occurrences, nitrogen-source role, and SSSOM row
    pass, but role/property strings remain in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ec065bea5464f883
    - ev-0a9da57ac5380c34
  - name: legacy-native-ids
    value: '["SEM:2c25f265978f0f90872c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0a9da57ac5380c34
    - ev-ec065bea5464f883
    - ev-00b39e03c96fc5ae
findings:
- finding_id: rec-f-e817a2eb6d0e44ff
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fadca324071cd86a
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Arginine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:40:20Z;
    reviewed SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73;
    current SHA-256=a076877ed9ec5c56ef3c89d70f704d3e24856e3a722817f6f002392a5b65ff73;
    hash_changed=False. Reports=["reports/yaml_record_review/Arginine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The generic CHEBI identity,
    formula, structure, CultureMech occurrences, nitrogen-source role, and SSSOM row
    pass, but role/property strings remain in synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fadca324071cd86a
  evidence_ids:
  - ev-ec065bea5464f883
  - ev-0a9da57ac5380c34
  - ev-00b39e03c96fc5ae
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Arginine.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
