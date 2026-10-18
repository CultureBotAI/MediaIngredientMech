# Per-record structured review: Biotin (data/ingredients/mapped/Biotin.yaml)

- Review: 20261017T083000Z-biotin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Biotin (data/ingredients/mapped/Biotin.yaml, record-7d94fef282a9db36, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Biotin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Biotin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7d94fef282a9db36 | data/ingredients/mapped/Biotin.yaml | maintained | Biotin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7d94fef282a9db36 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-7d94fef282a9db36 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7d94fef282a9db36 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7d94fef282a9db36.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7d94fef282a9db36.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:52:09Z; reviewed SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30; current SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30; hash_changed=False. Reports=["reports/yaml_record_review/Biotin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI biotin identity, aliases, CAS, vitamin role, structure fields, SSSOM row, and aggregate copy pass, but one ontology_mapping PubMed evidence entry is irrelevant.

## Findings

### rec-f-987ebaff43837463: Historical review coverage and residual narrative: Biotin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-7d94fef282a9db36.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:52:09Z; reviewed SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30; current SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30; hash_changed=False. Reports=["reports/yaml_record_review/Biotin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI biotin identity, aliases, CAS, vitamin role, structure fields, SSSOM row, and aggregate copy pass, but one ontology_mapping PubMed evidence entry is irrelevant.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2dfa849450fa89ad | data/ingredients/mapped/Biotin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[591],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15956","line":593,"mapping_status":"MAPPED","ontology_id":"CHEBI:15956","preferred_term":"Biotin"}],"identifier":"CHEBI:15956","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2792,"edge_count":2792,"occurrences":2829},"occurrence_statistics":{"media_count":2792,"total_occurrences":2829},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15956","ontology_label":"biotin","ontology_source":"CHEBI"},"preferred_term":"Biotin","sssom_rows":[{"data_row":549,"object_id":"CHEBI:15956","object_label":"biotin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Biotin","synonym_count":23} |
| ev-9ee317a4ee3df558 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [591] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4fd94ac90d0a1413 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Biotin; data-row positions=[549] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":549,"object_id":"CHEBI:15956","object_label":"biotin","other":"(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric acid&#124;(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid&#124;5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic acid&#124;5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid&#124;Biotine&#124;Coenzyme R&#124;D(+)-Biotin&#124;D-(+)-biotin&#124;D-Biotin&#124;Vitamin H&#124;biotina&#124;biotinum&#124;cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric acid&#124;cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid&#124;cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric acid&#124;vitamin B7&#124;Biotin (Vitamin B7)&#124;Biotin (1 \u03bcg/\u03bcL)&#124;CAS:58-85-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Biotin","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-1688c7d3412eaf16 | docs/data/mapped_ingredients.csv; CSV lines=[593] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15956","line":593,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2792","ontology_id":"CHEBI:15956","preferred_term":"Biotin","total_occurrences":"2829"}] |
| ev-68695971b7f264a8 | reports/yaml_record_review/Biotin.md; &#96;data/ingredients/mapped/Biotin.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:47; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e7f7ae742f670553 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[317] | context_only | [{"current_record_sha256":"26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30","finding_id":"SEM:75020e16f10f869c6aa6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-biotin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Biotin (data/ingredients/mapped/Biotin.yaml)'
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
summary: Per-record structured review for Biotin (data/ingredients/mapped/Biotin.yaml,
  record-7d94fef282a9db36, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Biotin.yaml
    sha256: 26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30
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
  - path: reports/yaml_record_review/Biotin.md
    sha256: 4ba0b75ed89648e876b8d74ff7e62f81a840708e657e05fb5439f2c826c6207f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7d94fef282a9db36
  path: data/ingredients/mapped/Biotin.yaml
  label: Biotin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Biotin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Biotin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Biotin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7d94fef282a9db36
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7d94fef282a9db36
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-7d94fef282a9db36
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7d94fef282a9db36
evidence:
- evidence_id: ev-2dfa849450fa89ad
  kind: record_content
  reference: data/ingredients/mapped/Biotin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[591],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15956","line":593,"mapping_status":"MAPPED","ontology_id":"CHEBI:15956","preferred_term":"Biotin"}],"identifier":"CHEBI:15956","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2792,"edge_count":2792,"occurrences":2829},"occurrence_statistics":{"media_count":2792,"total_occurrences":2829},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15956","ontology_label":"biotin","ontology_source":"CHEBI"},"preferred_term":"Biotin","sssom_rows":[{"data_row":549,"object_id":"CHEBI:15956","object_label":"biotin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Biotin","synonym_count":23}'
  snapshot_sha256: 26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30
- evidence_id: ev-9ee317a4ee3df558
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [591]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4fd94ac90d0a1413
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Biotin; data-row positions=[549]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":549,"object_id":"CHEBI:15956","object_label":"biotin","other":"(+)-cis-Hexahydro-2-oxo-1H-thieno[3,4]imidazole-4-valeric
    acid|(3aS,4S,6aR)-Hexahydro-2-oxo-1H-thieno[3,4-d]imidazole-4-valeric acid|5-(2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl)pentanoic
    acid|5-[(3aS,4S,6aR)-2-oxohexahydro-1H-thieno[3,4-d]imidazol-4-yl]pentanoic acid|Biotine|Coenzyme
    R|D(+)-Biotin|D-(+)-biotin|D-Biotin|Vitamin H|biotina|biotinum|cis-(+)-Tetrahydro-2-oxothieno[3,4]imidazoline-4-valeric
    acid|cis-Hexahydro-2-oxo-1H-thieno(3,4)imidazole-4-valeric acid|cis-Tetrahydro-2-oxothieno(3,4-d)imidazoline-4-valeric
    acid|vitamin B7|Biotin (Vitamin B7)|Biotin (1 \u03bcg/\u03bcL)|CAS:58-85-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Biotin","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1688c7d3412eaf16
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[593]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15956","line":593,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2792","ontology_id":"CHEBI:15956","preferred_term":"Biotin","total_occurrences":"2829"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-68695971b7f264a8
  kind: prior_review
  reference: reports/yaml_record_review/Biotin.md
  locator: '`data/ingredients/mapped/Biotin.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:32; Completeness:47; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4ba0b75ed89648e876b8d74ff7e62f81a840708e657e05fb5439f2c826c6207f
  quote: "Recommended Edits:\n- Minor: remove the `pmid: 39201737` PubMed search entry\
    \ from\n  `data/ingredients/mapped/Biotin.yaml`, or move it to a claim it actually\n\
    \  supports if a curator finds one; then run `just sync-curated` and focused\n\
    \  strict/term validation."
- evidence_id: ev-e7f7ae742f670553
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[317]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30","finding_id":"SEM:75020e16f10f869c6aa6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-02ed5fe65a699c0a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7d94fef282a9db36
  evidence_ids:
  - ev-2dfa849450fa89ad
  - ev-9ee317a4ee3df558
  - ev-4fd94ac90d0a1413
  - ev-1688c7d3412eaf16
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f6019005191bb9de
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7d94fef282a9db36
  evidence_ids:
  - ev-68695971b7f264a8
  - ev-2dfa849450fa89ad
  - ev-e7f7ae742f670553
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:52:09Z;
    reviewed SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30;
    current SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30;
    hash_changed=False. Reports=["reports/yaml_record_review/Biotin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI biotin
    identity, aliases, CAS, vitamin role, structure fields, SSSOM row, and aggregate
    copy pass, but one ontology_mapping PubMed evidence entry is irrelevant.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-68695971b7f264a8
    - ev-2dfa849450fa89ad
  - name: legacy-native-ids
    value: '["SEM:75020e16f10f869c6aa6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2dfa849450fa89ad
    - ev-68695971b7f264a8
    - ev-e7f7ae742f670553
findings:
- finding_id: rec-f-987ebaff43837463
  issue_key: mim-reconciliation-historical-review-coverage-and-r-7d94fef282a9db36
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Biotin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:52:09Z;
    reviewed SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30;
    current SHA-256=26056efadc5e57f081cde6e4ce0c2e25c03530c6d564ef0df25da3bcacb59c30;
    hash_changed=False. Reports=["reports/yaml_record_review/Biotin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI biotin
    identity, aliases, CAS, vitamin role, structure fields, SSSOM row, and aggregate
    copy pass, but one ontology_mapping PubMed evidence entry is irrelevant.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7d94fef282a9db36
  evidence_ids:
  - ev-68695971b7f264a8
  - ev-2dfa849450fa89ad
  - ev-e7f7ae742f670553
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Biotin.yaml
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
