# Per-record structured review: Air (data/ingredients/mapped/Air.yaml)

- Review: 20261017T083000Z-air
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Air (data/ingredients/mapped/Air.yaml, record-e3808829e445ee2c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Air.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Air.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e3808829e445ee2c | data/ingredients/mapped/Air.yaml | maintained | Air |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e3808829e445ee2c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e3808829e445ee2c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e3808829e445ee2c | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e3808829e445ee2c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e3808829e445ee2c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:28:27Z; reviewed SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d; current SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d; hash_changed=False. Reports=["reports/yaml_record_review/Air.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO air grounding passes, but only 12 uppercase Air residual mentions are represented while a second lowercase air residual row with 5 mentions remains unreconciled.

## Findings

### rec-f-9bead948dc3721d8: Historical review coverage and residual narrative: Air

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e3808829e445ee2c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:28:27Z; reviewed SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d; current SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d; hash_changed=False. Reports=["reports/yaml_record_review/Air.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO air grounding passes, but only 12 uppercase Air residual mentions are represented while a second lowercase air residual row with 5 mentions remains unreconciled.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-87037bb195305b62 | data/ingredients/mapped/Air.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2533],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00002005","line":2535,"mapping_status":"MAPPED","ontology_id":"ENVO:00002005","preferred_term":"Air"}],"identifier":"ENVO:00002005","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"ENVO:00002005","ontology_label":"air","ontology_source":"ENVO"},"preferred_term":"Air","sssom_rows":[{"data_row":317,"object_id":"ENVO:00002005","object_label":"air","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Air","synonym_count":0} |
| ev-11a55d007aecbfa1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2533] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-93b60f1f98742803 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Air; data-row positions=[317] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":317,"object_id":"ENVO:00002005","object_label":"air","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Air","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-d585bf6545236f7c | docs/data/mapped_ingredients.csv; CSV lines=[2535] | supports | Published identity and count rows inspected: [{"identifier":"ENVO:00002005","line":2535,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"ENVO:00002005","preferred_term":"Air","total_occurrences":"12"}] |
| ev-315b174411ff74a7 | reports/yaml_record_review/Air.md; &#96;data/ingredients/mapped/Air.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:34; Completeness:51; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-01baa24b25b49468 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[223] | context_only | [{"current_record_sha256":"9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d","finding_id":"SEM:80f2fad09335c24a0439","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-air
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Air (data/ingredients/mapped/Air.yaml)'
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
summary: Per-record structured review for Air (data/ingredients/mapped/Air.yaml, record-e3808829e445ee2c,
  mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Air.yaml
    sha256: 9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d
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
  - path: reports/yaml_record_review/Air.md
    sha256: fe34079b226447dc76f5b995748ebe10aa977be900574bc783d8fe28ca6af4a3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e3808829e445ee2c
  path: data/ingredients/mapped/Air.yaml
  label: Air
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Air.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Air.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Air.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e3808829e445ee2c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e3808829e445ee2c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e3808829e445ee2c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e3808829e445ee2c
evidence:
- evidence_id: ev-87037bb195305b62
  kind: record_content
  reference: data/ingredients/mapped/Air.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2533],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00002005","line":2535,"mapping_status":"MAPPED","ontology_id":"ENVO:00002005","preferred_term":"Air"}],"identifier":"ENVO:00002005","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"ENVO:00002005","ontology_label":"air","ontology_source":"ENVO"},"preferred_term":"Air","sssom_rows":[{"data_row":317,"object_id":"ENVO:00002005","object_label":"air","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Air","synonym_count":0}'
  snapshot_sha256: 9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d
- evidence_id: ev-11a55d007aecbfa1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2533]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-93b60f1f98742803
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Air; data-row positions=[317]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":317,"object_id":"ENVO:00002005","object_label":"air","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Air","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d585bf6545236f7c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2535]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"ENVO:00002005","line":2535,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"ENVO:00002005","preferred_term":"Air","total_occurrences":"12"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-315b174411ff74a7
  kind: prior_review
  reference: reports/yaml_record_review/Air.md
  locator: '`data/ingredients/mapped/Air.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:34; Completeness:51; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fe34079b226447dc76f5b995748ebe10aa977be900574bc783d8fe28ca6af4a3
  quote: "Recommended Edits:\n- Fold the lowercase `air` CultureMech residual row\
    \ into\n  `data/ingredients/mapped/Air.yaml` and refresh membership/occurrence\
    \ products\n  so all 17 mentions are represented, or document why those 5 mentions\
    \ are\n  intentionally excluded.\n- Regenerate synchronized products, then rerun\n\
    \  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Air.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-01baa24b25b49468
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[223]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d","finding_id":"SEM:80f2fad09335c24a0439","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a156f3d2dd579c54
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e3808829e445ee2c
  evidence_ids:
  - ev-87037bb195305b62
  - ev-11a55d007aecbfa1
  - ev-93b60f1f98742803
  - ev-d585bf6545236f7c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2051d3744387d5bd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e3808829e445ee2c
  evidence_ids:
  - ev-315b174411ff74a7
  - ev-87037bb195305b62
  - ev-01baa24b25b49468
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:28:27Z;
    reviewed SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d;
    current SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d;
    hash_changed=False. Reports=["reports/yaml_record_review/Air.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact ENVO air grounding
    passes, but only 12 uppercase Air residual mentions are represented while a second
    lowercase air residual row with 5 mentions remains unreconciled.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-315b174411ff74a7
    - ev-87037bb195305b62
  - name: legacy-native-ids
    value: '["SEM:80f2fad09335c24a0439"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-87037bb195305b62
    - ev-315b174411ff74a7
    - ev-01baa24b25b49468
findings:
- finding_id: rec-f-9bead948dc3721d8
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e3808829e445ee2c
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Air'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:28:27Z;
    reviewed SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d;
    current SHA-256=9fe7572616315e41774ebd74d8600b9d71f80c49c203ff862506322c631c3b7d;
    hash_changed=False. Reports=["reports/yaml_record_review/Air.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact ENVO air grounding
    passes, but only 12 uppercase Air residual mentions are represented while a second
    lowercase air residual row with 5 mentions remains unreconciled.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e3808829e445ee2c
  evidence_ids:
  - ev-315b174411ff74a7
  - ev-87037bb195305b62
  - ev-01baa24b25b49468
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Air.yaml
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
