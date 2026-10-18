# Per-record structured review: Uranyl_Acetate (data/ingredients/mapped/Uranyl_Acetate.yaml)

- Review: 20261017T083000Z-uranyl-acetate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Uranyl_Acetate (data/ingredients/mapped/Uranyl_Acetate.yaml, record-d30488b3527d4e81, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Uranyl_Acetate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Uranyl_Acetate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d30488b3527d4e81 | data/ingredients/mapped/Uranyl_Acetate.yaml | maintained | Uranyl_Acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d30488b3527d4e81 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d30488b3527d4e81 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d30488b3527d4e81 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d30488b3527d4e81.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d30488b3527d4e81.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:29:12Z; reviewed SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da; current SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da; hash_changed=False. Reports=["reports/yaml_record_review/Uranyl_Acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity and MeSH parent rows pass, but PubChem structure fields are pinned to an older CID that no longer carries CAS 541-09-3.

## Findings

### rec-f-47ffc4b1f23484c8: Historical review coverage and residual narrative: Uranyl_Acetate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d30488b3527d4e81.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:29:12Z; reviewed SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da; current SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da; hash_changed=False. Reports=["reports/yaml_record_review/Uranyl_Acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity and MeSH parent rows pass, but PubChem structure fields are pinned to an older CID that no longer carries CAS 541-09-3.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bafa31ae41dde7df | data/ingredients/mapped/Uranyl_Acetate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2023],"raw_equal":true},"docs_rows":[{"identifier":"cas:541-09-3","line":2025,"mapping_status":"MAPPED","ontology_id":"mesh:C005460","preferred_term":"Uranyl acetate"}],"identifier":"cas:541-09-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C005460","ontology_label":"uranyl acetate","ontology_source":"MESH"},"preferred_term":"Uranyl acetate","sssom_rows":[{"data_row":2866,"object_id":"mesh:C005460","object_label":"uranyl acetate","predicate_id":"skos:broadMatch"},{"data_row":2867,"object_id":"cas:541-09-3","object_label":"Uranyl acetate","predicate_id":"skos:exactMatch"},{"data_row":2868,"object_id":"kgmicrobe.compound:uranyl_acetate","object_label":"Uranyl acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Uranyl_Acetate","synonym_count":0} |
| ev-bb2798f7acde77e3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2023] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cb341f62f087b533 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Uranyl_Acetate; data-row positions=[2866,2867,2868] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2866,"object_id":"mesh:C005460","object_label":"uranyl acetate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2867,"object_id":"cas:541-09-3","object_label":"Uranyl acetate","other":"CAS:541-09-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2868,"object_id":"kgmicrobe.compound:uranyl_acetate","object_label":"Uranyl acetate","other":"CAS:541-09-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-ab69cab0b6540fc5 | docs/data/mapped_ingredients.csv; CSV lines=[2025] | supports | Published identity and count rows inspected: [{"identifier":"cas:541-09-3","line":2025,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C005460","preferred_term":"Uranyl acetate","total_occurrences":"2"}] |
| ev-37611c031d098528 | reports/yaml_record_review/Uranyl_Acetate.md; &#96;data/ingredients/mapped/Uranyl_Acetate.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:33; Issues:41; Major: PubChem fields are pinned to an outdated CAS representation:43; Completeness:54; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2d6b6253754ab986 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1331] | context_only | [{"current_record_sha256":"dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da","finding_id":"SEM:ab8cc7e641cac7d4e38d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-uranyl-acetate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Uranyl_Acetate (data/ingredients/mapped/Uranyl_Acetate.yaml)'
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
summary: Per-record structured review for Uranyl_Acetate (data/ingredients/mapped/Uranyl_Acetate.yaml,
  record-d30488b3527d4e81, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Uranyl_Acetate.yaml
    sha256: dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Uranyl_Acetate.md
    sha256: 6c458aea562d0e478ba2b889fba3264f39913ab7ae4b83ea95b8225da25c1592
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d30488b3527d4e81
  path: data/ingredients/mapped/Uranyl_Acetate.yaml
  label: Uranyl_Acetate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Uranyl_Acetate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Uranyl_Acetate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Uranyl_Acetate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d30488b3527d4e81
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d30488b3527d4e81
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d30488b3527d4e81
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d30488b3527d4e81
evidence:
- evidence_id: ev-bafa31ae41dde7df
  kind: record_content
  reference: data/ingredients/mapped/Uranyl_Acetate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2023],"raw_equal":true},"docs_rows":[{"identifier":"cas:541-09-3","line":2025,"mapping_status":"MAPPED","ontology_id":"mesh:C005460","preferred_term":"Uranyl
    acetate"}],"identifier":"cas:541-09-3","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C005460","ontology_label":"uranyl
    acetate","ontology_source":"MESH"},"preferred_term":"Uranyl acetate","sssom_rows":[{"data_row":2866,"object_id":"mesh:C005460","object_label":"uranyl
    acetate","predicate_id":"skos:broadMatch"},{"data_row":2867,"object_id":"cas:541-09-3","object_label":"Uranyl
    acetate","predicate_id":"skos:exactMatch"},{"data_row":2868,"object_id":"kgmicrobe.compound:uranyl_acetate","object_label":"Uranyl
    acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Uranyl_Acetate","synonym_count":0}'
  snapshot_sha256: dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da
- evidence_id: ev-bb2798f7acde77e3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2023]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cb341f62f087b533
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Uranyl_Acetate; data-row positions=[2866,2867,2868]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2866,"object_id":"mesh:C005460","object_label":"uranyl
    acetate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2867,"object_id":"cas:541-09-3","object_label":"Uranyl
    acetate","other":"CAS:541-09-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2868,"object_id":"kgmicrobe.compound:uranyl_acetate","object_label":"Uranyl
    acetate","other":"CAS:541-09-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Uranyl_Acetate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ab69cab0b6540fc5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2025]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:541-09-3","line":2025,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C005460","preferred_term":"Uranyl
    acetate","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-37611c031d098528
  kind: prior_review
  reference: reports/yaml_record_review/Uranyl_Acetate.md
  locator: '`data/ingredients/mapped/Uranyl_Acetate.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:33; Issues:41; Major: PubChem fields are pinned to an
    outdated CAS representation:43; Completeness:54; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6c458aea562d0e478ba2b889fba3264f39913ab7ae4b83ea95b8225da25c1592
  quote: "Issues:\n\n\nMajor: PubChem fields are pinned to an outdated CAS representation:\n\
    `chemical_properties.pubchem_cid` is `10915`, whose current PubChem synonyms no\n\
    longer include `541-09-3` and whose formula is `C4H8O6U`. A fresh PubChem CAS\n\
    lookup for `541-09-3` resolves instead to CID 21226249 with formula `C4H6O6U`\n\
    and a charged diacetate representation.\n\nThe CAS primary identifier and parent\
    \ MeSH mapping still make sense, but the\nrecord should refresh `chemical_properties`\
    \ from the current CAS-specific\nPubChem compound.\n\nRecommended Edits:\n- Refresh\
    \ `chemical_properties` from the current PubChem record for\n  `CAS:541-09-3`,\
    \ preserving the `NARROW_MATCH` MeSH parent and exact CAS /\n  `kgmicrobe.compound`\
    \ registry SSSOM rows."
- evidence_id: ev-2d6b6253754ab986
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1331]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da","finding_id":"SEM:ab8cc7e641cac7d4e38d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9b2cafb2aedb417d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d30488b3527d4e81
  evidence_ids:
  - ev-bafa31ae41dde7df
  - ev-bb2798f7acde77e3
  - ev-cb341f62f087b533
  - ev-ab69cab0b6540fc5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8ac3cf1a93f9f205
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d30488b3527d4e81
  evidence_ids:
  - ev-37611c031d098528
  - ev-bafa31ae41dde7df
  - ev-2d6b6253754ab986
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:29:12Z;
    reviewed SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da;
    current SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da;
    hash_changed=False. Reports=["reports/yaml_record_review/Uranyl_Acetate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity and MeSH parent rows pass, but PubChem structure fields are pinned to
    an older CID that no longer carries CAS 541-09-3.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-37611c031d098528
    - ev-bafa31ae41dde7df
  - name: legacy-native-ids
    value: '["SEM:ab8cc7e641cac7d4e38d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bafa31ae41dde7df
    - ev-37611c031d098528
    - ev-2d6b6253754ab986
findings:
- finding_id: rec-f-47ffc4b1f23484c8
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d30488b3527d4e81
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Uranyl_Acetate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:29:12Z;
    reviewed SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da;
    current SHA-256=dfdead3435fc397c9fe10f37f921b231ccf519e062ea8da080a69b91e9dac0da;
    hash_changed=False. Reports=["reports/yaml_record_review/Uranyl_Acetate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity and MeSH parent rows pass, but PubChem structure fields are pinned to
    an older CID that no longer carries CAS 541-09-3.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d30488b3527d4e81
  evidence_ids:
  - ev-37611c031d098528
  - ev-bafa31ae41dde7df
  - ev-2d6b6253754ab986
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Uranyl_Acetate.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
