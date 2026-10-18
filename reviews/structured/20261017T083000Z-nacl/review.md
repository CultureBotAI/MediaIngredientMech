# Per-record structured review: Nacl (data/ingredients/mapped/Nacl.yaml)

- Review: 20261017T083000Z-nacl
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nacl (data/ingredients/mapped/Nacl.yaml, record-1a2a6043fd4ebb5d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nacl.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nacl.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1a2a6043fd4ebb5d | data/ingredients/mapped/Nacl.yaml | maintained | Nacl |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1a2a6043fd4ebb5d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1a2a6043fd4ebb5d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1a2a6043fd4ebb5d | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1a2a6043fd4ebb5d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1a2a6043fd4ebb5d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:51:48Z; reviewed SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68; current SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68; hash_changed=False. Reports=["reports/yaml_record_review/Nacl.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26710 sodium chloride identity passes, but final other has vendor and concentration labels.

## Findings

### rec-f-027f85b086fc2e2a: Historical review coverage and residual narrative: Nacl

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1a2a6043fd4ebb5d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:51:48Z; reviewed SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68; current SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68; hash_changed=False. Reports=["reports/yaml_record_review/Nacl.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26710 sodium chloride identity passes, but final other has vendor and concentration labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e67875a38362b6e5 | data/ingredients/mapped/Nacl.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1519],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26710","line":1521,"mapping_status":"MAPPED","ontology_id":"CHEBI:26710","preferred_term":"NaCl"}],"identifier":"CHEBI:26710","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7695,"edge_count":7695,"occurrences":8191},"occurrence_statistics":{"media_count":7695,"total_occurrences":8191},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26710","ontology_label":"sodium chloride","ontology_source":"CHEBI"},"preferred_term":"NaCl","sssom_rows":[{"data_row":2028,"object_id":"CHEBI:26710","object_label":"sodium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nacl","synonym_count":21} |
| ev-e7feee574572948e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1519] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bdf255aaa718e892 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nacl; data-row positions=[2028] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2028,"object_id":"CHEBI:26710","object_label":"sodium chloride","other":"Kochsalz&#124;Natriumchlorid&#124;chlorure de sodium&#124;cloruro sodico&#124;common salt&#124;natrii chloridum&#124;rock salt&#124;salt&#124;table salt&#124;NaCl (Fisher S271-500)&#124;NaCl(Fisher S271-500)&#124;1% Sodium Chloride&#124;CAS:7647-14-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nacl","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-b9efa2547ff79243 | docs/data/mapped_ingredients.csv; CSV lines=[1521] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26710","line":1521,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7695","ontology_id":"CHEBI:26710","preferred_term":"NaCl","total_occurrences":"8191"}] |
| ev-d9bce6efbbdd23fb | reports/yaml_record_review/Nacl.md; &#96;data/ingredients/mapped/Nacl.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ad02bfea674571d4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1023] | context_only | [{"current_record_sha256":"41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68","finding_id":"SEM:bec9ec1edde6c6cf4530","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nacl
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nacl (data/ingredients/mapped/Nacl.yaml)'
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
summary: Per-record structured review for Nacl (data/ingredients/mapped/Nacl.yaml,
  record-1a2a6043fd4ebb5d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nacl.yaml
    sha256: 41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68
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
  - path: reports/yaml_record_review/Nacl.md
    sha256: 23e6ac950c95a4b5330ade55f5f312dbc9f075a8f42f03a9738a85b81483539e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1a2a6043fd4ebb5d
  path: data/ingredients/mapped/Nacl.yaml
  label: Nacl
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nacl.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nacl.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Nacl.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1a2a6043fd4ebb5d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1a2a6043fd4ebb5d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1a2a6043fd4ebb5d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1a2a6043fd4ebb5d
evidence:
- evidence_id: ev-e67875a38362b6e5
  kind: record_content
  reference: data/ingredients/mapped/Nacl.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1519],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26710","line":1521,"mapping_status":"MAPPED","ontology_id":"CHEBI:26710","preferred_term":"NaCl"}],"identifier":"CHEBI:26710","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7695,"edge_count":7695,"occurrences":8191},"occurrence_statistics":{"media_count":7695,"total_occurrences":8191},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26710","ontology_label":"sodium
    chloride","ontology_source":"CHEBI"},"preferred_term":"NaCl","sssom_rows":[{"data_row":2028,"object_id":"CHEBI:26710","object_label":"sodium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nacl","synonym_count":21}'
  snapshot_sha256: 41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68
- evidence_id: ev-e7feee574572948e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1519]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bdf255aaa718e892
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nacl; data-row positions=[2028]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2028,"object_id":"CHEBI:26710","object_label":"sodium
    chloride","other":"Kochsalz|Natriumchlorid|chlorure de sodium|cloruro sodico|common
    salt|natrii chloridum|rock salt|salt|table salt|NaCl (Fisher S271-500)|NaCl(Fisher
    S271-500)|1% Sodium Chloride|CAS:7647-14-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nacl","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b9efa2547ff79243
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1521]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26710","line":1521,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7695","ontology_id":"CHEBI:26710","preferred_term":"NaCl","total_occurrences":"8191"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d9bce6efbbdd23fb
  kind: prior_review
  reference: reports/yaml_record_review/Nacl.md
  locator: '`data/ingredients/mapped/Nacl.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:27; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 23e6ac950c95a4b5330ade55f5f312dbc9f075a8f42f03a9738a85b81483539e
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nacl.yaml`, reject\
    \ or delete the two\n  Fisher catalog strings and `1% Sodium Chloride`, then rebuild\
    \ final SSSOM so\n  `other` contains only real sodium chloride synonyms and `CAS:7647-14-5`.\n\
    - Minor: remove `pmid: 40820329` from\n  `ontology_mapping.evidence` unless a\
    \ curator finds it materially supports\n  the identity decision better than the\
    \ existing database evidence."
- evidence_id: ev-ad02bfea674571d4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1023]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68","finding_id":"SEM:bec9ec1edde6c6cf4530","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9d8c3a21e103f5ff
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1a2a6043fd4ebb5d
  evidence_ids:
  - ev-e67875a38362b6e5
  - ev-e7feee574572948e
  - ev-bdf255aaa718e892
  - ev-b9efa2547ff79243
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-851fa7913634482e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a2a6043fd4ebb5d
  evidence_ids:
  - ev-d9bce6efbbdd23fb
  - ev-e67875a38362b6e5
  - ev-ad02bfea674571d4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:51:48Z;
    reviewed SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68;
    current SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68;
    hash_changed=False. Reports=["reports/yaml_record_review/Nacl.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:26710 sodium
    chloride identity passes, but final other has vendor and concentration labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d9bce6efbbdd23fb
    - ev-e67875a38362b6e5
  - name: legacy-native-ids
    value: '["SEM:bec9ec1edde6c6cf4530"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e67875a38362b6e5
    - ev-d9bce6efbbdd23fb
    - ev-ad02bfea674571d4
findings:
- finding_id: rec-f-027f85b086fc2e2a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1a2a6043fd4ebb5d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nacl'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:51:48Z;
    reviewed SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68;
    current SHA-256=41c45e2a588da9811c8f20f7bf5c2c80dc15945cf8fdee5673d4143a8af62e68;
    hash_changed=False. Reports=["reports/yaml_record_review/Nacl.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:26710 sodium
    chloride identity passes, but final other has vendor and concentration labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a2a6043fd4ebb5d
  evidence_ids:
  - ev-d9bce6efbbdd23fb
  - ev-e67875a38362b6e5
  - ev-ad02bfea674571d4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nacl.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
