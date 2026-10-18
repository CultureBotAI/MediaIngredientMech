# Per-record structured review: Alcl3 (data/ingredients/mapped/Alcl3.yaml)

- Review: 20261017T083000Z-alcl3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alcl3 (data/ingredients/mapped/Alcl3.yaml, record-e9b3648170ca8260, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alcl3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alcl3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e9b3648170ca8260 | data/ingredients/mapped/Alcl3.yaml | maintained | Alcl3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e9b3648170ca8260 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e9b3648170ca8260 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e9b3648170ca8260 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e9b3648170ca8260.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e9b3648170ca8260.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z; reviewed SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b; current SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b; hash_changed=False. Reports=["reports/yaml_record_review/Alcl3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous CHEBI identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but a CultureMech role/property string remains in synonyms.

## Findings

### rec-f-eaffc55f63a2b15b: Historical review coverage and residual narrative: Alcl3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e9b3648170ca8260.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z; reviewed SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b; current SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b; hash_changed=False. Reports=["reports/yaml_record_review/Alcl3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous CHEBI identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but a CultureMech role/property string remains in synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-249329df2a039b66 | data/ingredients/mapped/Alcl3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[466],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30114","line":468,"mapping_status":"MAPPED","ontology_id":"CHEBI:30114","preferred_term":"AlCl3"}],"identifier":"CHEBI:30114","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":77,"edge_count":77,"occurrences":77},"occurrence_statistics":{"media_count":77,"total_occurrences":77},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30114","ontology_label":"aluminium trichloride","ontology_source":"CHEBI"},"preferred_term":"AlCl3","sssom_rows":[{"data_row":322,"object_id":"CHEBI:30114","object_label":"aluminium trichloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alcl3","synonym_count":8} |
| ev-78e0a944236da011 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [466] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bea002655bdf171c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alcl3; data-row positions=[322] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":322,"object_id":"CHEBI:30114","object_label":"aluminium trichloride","other":"Aluminum trichloride&#124;[AlCl3]&#124;aluminium(3+) chloride&#124;aluminium(III) chloride&#124;trichloridoaluminium&#124;trichloroalumane&#124;CAS:7446-70-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Alcl3","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-1d3ebf4bf2076b50 | docs/data/mapped_ingredients.csv; CSV lines=[468] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30114","line":468,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"77","ontology_id":"CHEBI:30114","preferred_term":"AlCl3","total_occurrences":"77"}] |
| ev-b44a3eac1025970f | reports/yaml_record_review/Alcl3.md; &#96;data/ingredients/mapped/Alcl3.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:41; Completeness:62; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-49a7fe266e70023e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[227] | context_only | [{"current_record_sha256":"05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b","finding_id":"SEM:929ac49fc93b852dc02c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alcl3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alcl3 (data/ingredients/mapped/Alcl3.yaml)'
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
summary: Per-record structured review for Alcl3 (data/ingredients/mapped/Alcl3.yaml,
  record-e9b3648170ca8260, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alcl3.yaml
    sha256: 05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b
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
  - path: reports/yaml_record_review/Alcl3.md
    sha256: 037e3da08ee66cae03a3b6b2cc62e2a39210102c12e511b1200ac3a6194567e4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e9b3648170ca8260
  path: data/ingredients/mapped/Alcl3.yaml
  label: Alcl3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alcl3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alcl3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alcl3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e9b3648170ca8260
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e9b3648170ca8260
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e9b3648170ca8260
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e9b3648170ca8260
evidence:
- evidence_id: ev-249329df2a039b66
  kind: record_content
  reference: data/ingredients/mapped/Alcl3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[466],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30114","line":468,"mapping_status":"MAPPED","ontology_id":"CHEBI:30114","preferred_term":"AlCl3"}],"identifier":"CHEBI:30114","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":77,"edge_count":77,"occurrences":77},"occurrence_statistics":{"media_count":77,"total_occurrences":77},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30114","ontology_label":"aluminium
    trichloride","ontology_source":"CHEBI"},"preferred_term":"AlCl3","sssom_rows":[{"data_row":322,"object_id":"CHEBI:30114","object_label":"aluminium
    trichloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alcl3","synonym_count":8}'
  snapshot_sha256: 05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b
- evidence_id: ev-78e0a944236da011
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [466]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bea002655bdf171c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alcl3; data-row positions=[322]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":322,"object_id":"CHEBI:30114","object_label":"aluminium
    trichloride","other":"Aluminum trichloride|[AlCl3]|aluminium(3+) chloride|aluminium(III)
    chloride|trichloridoaluminium|trichloroalumane|CAS:7446-70-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Alcl3","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1d3ebf4bf2076b50
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[468]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30114","line":468,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"77","ontology_id":"CHEBI:30114","preferred_term":"AlCl3","total_occurrences":"77"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b44a3eac1025970f
  kind: prior_review
  reference: reports/yaml_record_review/Alcl3.md
  locator: '`data/ingredients/mapped/Alcl3.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:41; Completeness:62; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 037e3da08ee66cae03a3b6b2cc62e2a39210102c12e511b1200ac3a6194567e4
  quote: "Recommended Edits:\n- Remove or move the CultureMech role/property raw synonym\
    \ from\n  `data/ingredients/mapped/Alcl3.yaml`; the curated\n  `nutritional_roles.TRACE_ELEMENT`\
    \ entry already captures the role.\n- Regenerate synchronized products, then rerun\n\
    \  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Alcl3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-49a7fe266e70023e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[227]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b","finding_id":"SEM:929ac49fc93b852dc02c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3f1d167477d23bdf
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e9b3648170ca8260
  evidence_ids:
  - ev-249329df2a039b66
  - ev-78e0a944236da011
  - ev-bea002655bdf171c
  - ev-1d3ebf4bf2076b50
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8ce5be8af5b39ec4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e9b3648170ca8260
  evidence_ids:
  - ev-b44a3eac1025970f
  - ev-249329df2a039b66
  - ev-49a7fe266e70023e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z;
    reviewed SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b;
    current SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b;
    hash_changed=False. Reports=["reports/yaml_record_review/Alcl3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous CHEBI
    identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but
    a CultureMech role/property string remains in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b44a3eac1025970f
    - ev-249329df2a039b66
  - name: legacy-native-ids
    value: '["SEM:929ac49fc93b852dc02c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-249329df2a039b66
    - ev-b44a3eac1025970f
    - ev-49a7fe266e70023e
findings:
- finding_id: rec-f-eaffc55f63a2b15b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e9b3648170ca8260
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Alcl3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z;
    reviewed SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b;
    current SHA-256=05519748d1eb8db4bdb7f716fa00d259d5b03a986fd4452b14cf52f6be0ca03b;
    hash_changed=False. Reports=["reports/yaml_record_review/Alcl3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous CHEBI
    identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but
    a CultureMech role/property string remains in synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e9b3648170ca8260
  evidence_ids:
  - ev-b44a3eac1025970f
  - ev-249329df2a039b66
  - ev-49a7fe266e70023e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alcl3.yaml
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
