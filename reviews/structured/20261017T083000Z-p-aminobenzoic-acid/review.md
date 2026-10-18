# Per-record structured review: P-aminobenzoic_Acid (data/ingredients/mapped/P-aminobenzoic_Acid.yaml)

- Review: 20261017T083000Z-p-aminobenzoic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for P-aminobenzoic_Acid (data/ingredients/mapped/P-aminobenzoic_Acid.yaml, record-f0957b4f878bad9c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/P-aminobenzoic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/P-aminobenzoic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f0957b4f878bad9c | data/ingredients/mapped/P-aminobenzoic_Acid.yaml | maintained | P-aminobenzoic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f0957b4f878bad9c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f0957b4f878bad9c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f0957b4f878bad9c | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f0957b4f878bad9c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f0957b4f878bad9c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z; reviewed SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f; current SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f; hash_changed=False. Reports=["reports/yaml_record_review/P-aminobenzoic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:30753 neutral-acid identity and VITAMIN_SOURCE pass, but final other exports concentration and zwitterion labels.

## Findings

### rec-f-d9f2f9b5611d9d4c: Historical review coverage and residual narrative: P-aminobenzoic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f0957b4f878bad9c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z; reviewed SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f; current SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f; hash_changed=False. Reports=["reports/yaml_record_review/P-aminobenzoic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:30753 neutral-acid identity and VITAMIN_SOURCE pass, but final other exports concentration and zwitterion labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-49cb61aaf7c3aab0 | data/ingredients/mapped/P-aminobenzoic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1602],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30753","line":1604,"mapping_status":"MAPPED","ontology_id":"CHEBI:30753","preferred_term":"p-Aminobenzoic acid"}],"identifier":"CHEBI:30753","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2269,"edge_count":2269,"occurrences":2270},"occurrence_statistics":{"media_count":2269,"total_occurrences":2270},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30753","ontology_label":"4-aminobenzoic acid","ontology_source":"CHEBI"},"preferred_term":"p-Aminobenzoic acid","sssom_rows":[{"data_row":2164,"object_id":"CHEBI:30753","object_label":"4-aminobenzoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-aminobenzoic_Acid","synonym_count":23} |
| ev-29b4f7d5388a02e9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1602] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3ff8cd1f3c2a7485 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:P-aminobenzoic_Acid; data-row positions=[2164] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2164,"object_id":"CHEBI:30753","object_label":"4-aminobenzoic acid","other":"1-Amino-4-carboxybenzene&#124;4-Amino-benzoic acid&#124;4-Aminobenzoesaeure&#124;4-Carboxyaniline&#124;4-Carboxyphenylamine&#124;ABEE&#124;PABA&#124;Para-aminobenzoic acid&#124;gamma-Aminobenzoic acid&#124;p--Aminobenzoic acid&#124;p-Aminobenzoesaeure&#124;p-carboxyaniline&#124;p-carboxyphenylamine&#124;p-Amino Benzoic Acid&#124;p-aminobenzoic acid (0.3 \u03bcg/\u03bcL)&#124;4-aminobenzoic acid zwitterion&#124;4-ammoniobenzoate&#124;4-azaniumylbenzoate&#124;CAS:150-13-0","predicate_id":"skos:exactMatch","subject_id":"MIM:P-aminobenzoic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bf0b6548a2726adf | docs/data/mapped_ingredients.csv; CSV lines=[1604] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30753","line":1604,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2269","ontology_id":"CHEBI:30753","preferred_term":"p-Aminobenzoic acid","total_occurrences":"2270"}] |
| ev-f2877c03bb0d1ee0 | reports/yaml_record_review/P-aminobenzoic_Acid.md; &#96;data/ingredients/mapped/P-aminobenzoic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Completeness:53; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0e0fcee7d8eb74d4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1084] | context_only | [{"current_record_sha256":"088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f","finding_id":"SEM:1bd99d7ecd27b4b8c88f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-p-aminobenzoic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: P-aminobenzoic_Acid (data/ingredients/mapped/P-aminobenzoic_Acid.yaml)'
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
summary: Per-record structured review for P-aminobenzoic_Acid (data/ingredients/mapped/P-aminobenzoic_Acid.yaml,
  record-f0957b4f878bad9c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/P-aminobenzoic_Acid.yaml
    sha256: 088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f
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
  - path: reports/yaml_record_review/P-aminobenzoic_Acid.md
    sha256: c81eee1c3e081eed5b5c9909fc4ad39d0039dab69f9ef24e3df0de65fc480864
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f0957b4f878bad9c
  path: data/ingredients/mapped/P-aminobenzoic_Acid.yaml
  label: P-aminobenzoic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-aminobenzoic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/P-aminobenzoic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/P-aminobenzoic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f0957b4f878bad9c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f0957b4f878bad9c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f0957b4f878bad9c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f0957b4f878bad9c
evidence:
- evidence_id: ev-49cb61aaf7c3aab0
  kind: record_content
  reference: data/ingredients/mapped/P-aminobenzoic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1602],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30753","line":1604,"mapping_status":"MAPPED","ontology_id":"CHEBI:30753","preferred_term":"p-Aminobenzoic
    acid"}],"identifier":"CHEBI:30753","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2269,"edge_count":2269,"occurrences":2270},"occurrence_statistics":{"media_count":2269,"total_occurrences":2270},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30753","ontology_label":"4-aminobenzoic
    acid","ontology_source":"CHEBI"},"preferred_term":"p-Aminobenzoic acid","sssom_rows":[{"data_row":2164,"object_id":"CHEBI:30753","object_label":"4-aminobenzoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-aminobenzoic_Acid","synonym_count":23}'
  snapshot_sha256: 088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f
- evidence_id: ev-29b4f7d5388a02e9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1602]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3ff8cd1f3c2a7485
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:P-aminobenzoic_Acid; data-row positions=[2164]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2164,"object_id":"CHEBI:30753","object_label":"4-aminobenzoic
    acid","other":"1-Amino-4-carboxybenzene|4-Amino-benzoic acid|4-Aminobenzoesaeure|4-Carboxyaniline|4-Carboxyphenylamine|ABEE|PABA|Para-aminobenzoic
    acid|gamma-Aminobenzoic acid|p--Aminobenzoic acid|p-Aminobenzoesaeure|p-carboxyaniline|p-carboxyphenylamine|p-Amino
    Benzoic Acid|p-aminobenzoic acid (0.3 \u03bcg/\u03bcL)|4-aminobenzoic acid zwitterion|4-ammoniobenzoate|4-azaniumylbenzoate|CAS:150-13-0","predicate_id":"skos:exactMatch","subject_id":"MIM:P-aminobenzoic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bf0b6548a2726adf
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1604]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30753","line":1604,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2269","ontology_id":"CHEBI:30753","preferred_term":"p-Aminobenzoic
    acid","total_occurrences":"2270"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f2877c03bb0d1ee0
  kind: prior_review
  reference: reports/yaml_record_review/P-aminobenzoic_Acid.md
  locator: '`data/ingredients/mapped/P-aminobenzoic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:30; Completeness:53; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c81eee1c3e081eed5b5c9909fc4ad39d0039dab69f9ef24e3df0de65fc480864
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/P-aminobenzoic_Acid.yaml`,\
    \ remove the\n  microgram-per-microliter concentration surface from active `synonyms`,\
    \ or\n  preserve it only as non-exported occurrence provenance, then rebuild the\n\
    \  final SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the\n  id-label\
    \ product check to prove it no longer appears in `other`.\n- Major: move `4-ammoniobenzoate`,\
    \ `4-azaniumylbenzoate`, and\n  `4-aminobenzoic acid zwitterion` out of active\
    \ `synonyms`, preserve them\n  only as rejected or historical provenance if useful,\
    \ and rebuild the final\n  SSSOM so `MIM:P-aminobenzoic_Acid` no longer publishes\
    \ zwitterion labels as\n  neutral-acid synonyms.\n- Minor: remove or rephrase\
    \ the auto-proposed PMID `31986050` ontology\n  evidence so a p-aminobenzoic-acid\
    \ cocrystal paper is not presented as\n  support for the CultureMech mapping decision."
- evidence_id: ev-0e0fcee7d8eb74d4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1084]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f","finding_id":"SEM:1bd99d7ecd27b4b8c88f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2bfd1a44083597f2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f0957b4f878bad9c
  evidence_ids:
  - ev-49cb61aaf7c3aab0
  - ev-29b4f7d5388a02e9
  - ev-3ff8cd1f3c2a7485
  - ev-bf0b6548a2726adf
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-51e4a08d619fba81
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f0957b4f878bad9c
  evidence_ids:
  - ev-f2877c03bb0d1ee0
  - ev-49cb61aaf7c3aab0
  - ev-0e0fcee7d8eb74d4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z;
    reviewed SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f;
    current SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f;
    hash_changed=False. Reports=["reports/yaml_record_review/P-aminobenzoic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:30753
    neutral-acid identity and VITAMIN_SOURCE pass, but final other exports concentration
    and zwitterion labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f2877c03bb0d1ee0
    - ev-49cb61aaf7c3aab0
  - name: legacy-native-ids
    value: '["SEM:1bd99d7ecd27b4b8c88f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-49cb61aaf7c3aab0
    - ev-f2877c03bb0d1ee0
    - ev-0e0fcee7d8eb74d4
findings:
- finding_id: rec-f-d9f2f9b5611d9d4c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f0957b4f878bad9c
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: P-aminobenzoic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:00:49Z;
    reviewed SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f;
    current SHA-256=088498308b47b9a01c45baa4bfbb3a7a367949a08bb85b11cdfbc89f1a8ca91f;
    hash_changed=False. Reports=["reports/yaml_record_review/P-aminobenzoic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:30753
    neutral-acid identity and VITAMIN_SOURCE pass, but final other exports concentration
    and zwitterion labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f0957b4f878bad9c
  evidence_ids:
  - ev-f2877c03bb0d1ee0
  - ev-49cb61aaf7c3aab0
  - ev-0e0fcee7d8eb74d4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-aminobenzoic_Acid.yaml
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
