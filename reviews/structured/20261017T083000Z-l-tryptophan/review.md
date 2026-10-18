# Per-record structured review: L-tryptophan (data/ingredients/mapped/L-tryptophan.yaml)

- Review: 20261017T083000Z-l-tryptophan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-tryptophan (data/ingredients/mapped/L-tryptophan.yaml, record-e2111085524d8bda, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-tryptophan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-tryptophan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e2111085524d8bda | data/ingredients/mapped/L-tryptophan.yaml | maintained | L-tryptophan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e2111085524d8bda | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e2111085524d8bda | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e2111085524d8bda | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e2111085524d8bda.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e2111085524d8bda.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:30:17Z; reviewed SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0; current SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0; hash_changed=False. Reports=["reports/yaml_record_review/L-tryptophan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16828 identity, CAS value, PubChem structure, CultureMech nitrogen-source role, and occurrence count pass, but final SSSOM exports generic Tryptophan.

## Findings

### rec-f-a0a66bbbeec5a92c: Historical review coverage and residual narrative: L-tryptophan

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e2111085524d8bda.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:30:17Z; reviewed SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0; current SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0; hash_changed=False. Reports=["reports/yaml_record_review/L-tryptophan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16828 identity, CAS value, PubChem structure, CultureMech nitrogen-source role, and occurrence count pass, but final SSSOM exports generic Tryptophan.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b7bbc1b48a86d91d | data/ingredients/mapped/L-tryptophan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1261],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16828","line":1263,"mapping_status":"MAPPED","ontology_id":"CHEBI:16828","preferred_term":"L-Tryptophan"}],"identifier":"CHEBI:16828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":100,"edge_count":100,"occurrences":100},"occurrence_statistics":{"media_count":100,"total_occurrences":100},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16828","ontology_label":"L-tryptophan","ontology_source":"CHEBI"},"preferred_term":"L-Tryptophan","sssom_rows":[{"data_row":1641,"object_id":"CHEBI:16828","object_label":"L-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-tryptophan","synonym_count":9} |
| ev-caf3eb18e3f672ff | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1261] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-511875cf66dd1c71 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-tryptophan; data-row positions=[1641] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1641,"object_id":"CHEBI:16828","object_label":"L-tryptophan","other":"(2S)-2-amino-3-(1H-indol-3-yl)propanoic acid&#124;(S)-alpha-Amino-beta-(3-indolyl)-propionic acid&#124;(S)-alpha-amino-1H-indole-3-propanoic acid&#124;(S)-tryptophan&#124;L-(-)-tryptophan&#124;L-beta-3-indolylalanine&#124;Tryptophan&#124;CAS:73-22-3","predicate_id":"skos:exactMatch","subject_id":"MIM:L-tryptophan","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-74b978902421705f | docs/data/mapped_ingredients.csv; CSV lines=[1263] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16828","line":1263,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"100","ontology_id":"CHEBI:16828","preferred_term":"L-Tryptophan","total_occurrences":"100"}] |
| ev-7bfb8e2a6c1a9a1d | reports/yaml_record_review/L-tryptophan.md; &#96;data/ingredients/mapped/L-tryptophan.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:31; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4a83586f8823cbd9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[836] | context_only | [{"current_record_sha256":"9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0","finding_id":"SEM:5b937255bbeab823449b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-tryptophan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-tryptophan (data/ingredients/mapped/L-tryptophan.yaml)'
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
summary: Per-record structured review for L-tryptophan (data/ingredients/mapped/L-tryptophan.yaml,
  record-e2111085524d8bda, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-tryptophan.yaml
    sha256: 9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0
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
  - path: reports/yaml_record_review/L-tryptophan.md
    sha256: 5bafa8b19005fb05354209d01e794658bece64f1577dbf1aac82edd55a4d075c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e2111085524d8bda
  path: data/ingredients/mapped/L-tryptophan.yaml
  label: L-tryptophan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-tryptophan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-tryptophan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-tryptophan.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e2111085524d8bda
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e2111085524d8bda
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e2111085524d8bda
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e2111085524d8bda
evidence:
- evidence_id: ev-b7bbc1b48a86d91d
  kind: record_content
  reference: data/ingredients/mapped/L-tryptophan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1261],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16828","line":1263,"mapping_status":"MAPPED","ontology_id":"CHEBI:16828","preferred_term":"L-Tryptophan"}],"identifier":"CHEBI:16828","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":100,"edge_count":100,"occurrences":100},"occurrence_statistics":{"media_count":100,"total_occurrences":100},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16828","ontology_label":"L-tryptophan","ontology_source":"CHEBI"},"preferred_term":"L-Tryptophan","sssom_rows":[{"data_row":1641,"object_id":"CHEBI:16828","object_label":"L-tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-tryptophan","synonym_count":9}'
  snapshot_sha256: 9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0
- evidence_id: ev-caf3eb18e3f672ff
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1261]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-511875cf66dd1c71
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-tryptophan; data-row positions=[1641]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1641,"object_id":"CHEBI:16828","object_label":"L-tryptophan","other":"(2S)-2-amino-3-(1H-indol-3-yl)propanoic
    acid|(S)-alpha-Amino-beta-(3-indolyl)-propionic acid|(S)-alpha-amino-1H-indole-3-propanoic
    acid|(S)-tryptophan|L-(-)-tryptophan|L-beta-3-indolylalanine|Tryptophan|CAS:73-22-3","predicate_id":"skos:exactMatch","subject_id":"MIM:L-tryptophan","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-74b978902421705f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1263]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16828","line":1263,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"100","ontology_id":"CHEBI:16828","preferred_term":"L-Tryptophan","total_occurrences":"100"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7bfb8e2a6c1a9a1d
  kind: prior_review
  reference: reports/yaml_record_review/L-tryptophan.md
  locator: '`data/ingredients/mapped/L-tryptophan.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:31; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5bafa8b19005fb05354209d01e794658bece64f1577dbf1aac82edd55a4d075c
  quote: "Recommended Edits:\n- Major: remove `Tryptophan` from the `EXACT_SYNONYM`\
    \ list on\n  `data/ingredients/mapped/L-tryptophan.yaml`, or rehome it to the\
    \ generic\n  tryptophan record if a non-preferred synonym is still needed there.\n\
    - Sync the aggregate copy and regenerate derived products after the YAML\n  changes;\
    \ rerun strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-4a83586f8823cbd9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[836]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0","finding_id":"SEM:5b937255bbeab823449b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d9f44b24d3c287e8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e2111085524d8bda
  evidence_ids:
  - ev-b7bbc1b48a86d91d
  - ev-caf3eb18e3f672ff
  - ev-511875cf66dd1c71
  - ev-74b978902421705f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9c8530aa7e25e5af
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e2111085524d8bda
  evidence_ids:
  - ev-7bfb8e2a6c1a9a1d
  - ev-b7bbc1b48a86d91d
  - ev-4a83586f8823cbd9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:30:17Z;
    reviewed SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0;
    current SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0;
    hash_changed=False. Reports=["reports/yaml_record_review/L-tryptophan.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16828
    identity, CAS value, PubChem structure, CultureMech nitrogen-source role, and
    occurrence count pass, but final SSSOM exports generic Tryptophan.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7bfb8e2a6c1a9a1d
    - ev-b7bbc1b48a86d91d
  - name: legacy-native-ids
    value: '["SEM:5b937255bbeab823449b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b7bbc1b48a86d91d
    - ev-7bfb8e2a6c1a9a1d
    - ev-4a83586f8823cbd9
findings:
- finding_id: rec-f-a0a66bbbeec5a92c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e2111085524d8bda
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-tryptophan'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:30:17Z;
    reviewed SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0;
    current SHA-256=9e95fed47a3744d5ca9420212a63488f02af4050687ee078f892f2a1b17c25e0;
    hash_changed=False. Reports=["reports/yaml_record_review/L-tryptophan.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16828
    identity, CAS value, PubChem structure, CultureMech nitrogen-source role, and
    occurrence count pass, but final SSSOM exports generic Tryptophan.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e2111085524d8bda
  evidence_ids:
  - ev-7bfb8e2a6c1a9a1d
  - ev-b7bbc1b48a86d91d
  - ev-4a83586f8823cbd9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-tryptophan.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
