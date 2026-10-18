# Per-record structured review: L-Malic_Acid_Disodium_Salt_Monohydrate (data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml)

- Review: 20261017T083000Z-l-malic-acid-disodium-salt-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Malic_Acid_Disodium_Salt_Monohydrate (data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml, record-405458fa4de81278, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-405458fa4de81278 | data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml | maintained | L-Malic_Acid_Disodium_Salt_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-405458fa4de81278 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-405458fa4de81278 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-405458fa4de81278 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-405458fa4de81278.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-405458fa4de81278.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z; reviewed SHA-256=4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080; current SHA-256=4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080; hash_changed=False. Reports=["reports/yaml_record_review/L-Malic_Acid_Disodium_Salt_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, NCIT parent, exact CAS and kgmicrobe.compound rows, and hydrate review pass, but chemical_properties has the wrong PubChem structure and carbon/energy roles are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-405458fa4de81278.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-823ac14862c4c722: Reassess prediction-only role support: L-Malic acid disodium salt monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-405458fa4de81278.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-823ac14862c4c722

Reassess prediction-only role support: L-Malic acid disodium salt monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b09dcd58be19aab9 | data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1228],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-06-6","line":1230,"mapping_status":"MAPPED","ontology_id":"NCIT:C80654","preferred_term":"L-Malic acid disodium salt monohydrate"}],"identifier":"cas:207511-06-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C80654","ontology_label":"Malic Acid","ontology_source":"NCIT"},"preferred_term":"L-Malic acid disodium salt monohydrate","sssom_rows":[{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic Acid","predicate_id":"skos:broadMatch"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic acid disodium salt monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic acid disodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","synonym_count":0} |
| ev-72ac8a2c127f2554 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1228] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e0f1d4488fa5b878 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Malic_Acid_Disodium_Salt_Monohydrate; data-row positions=[1580, 1581, 1582] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic Acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic acid disodium salt monohydrate","other":"CAS:207511-06-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic acid disodium salt monohydrate","other":"CAS:207511-06-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-e9da53f43aaa4ede | docs/data/mapped_ingredients.csv; CSV lines=[1230] | supports | Published identity and count rows inspected: [{"identifier":"cas:207511-06-6","line":1230,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C80654","preferred_term":"L-Malic acid disodium salt monohydrate","total_occurrences":"0"}] |
| ev-5eca2d5b1b7dd992 | reports/yaml_record_review/L-Malic_Acid_Disodium_Salt_Monohydrate.md; &#96;data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:33; Completeness:60; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bdc908f9eb3eb8a7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[795,1784,1920] | context_only | [{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:5c494bf191db4bfed0df","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:0ad3b56193b3bb37d78e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:04a0eaa85019c2baeb96","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d67477a1d5bd1e42 | data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1228],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-06-6","line":1230,"mapping_status":"MAPPED","ontology_id":"NCIT:C80654","preferred_term":"L-Malic acid disodium salt monohydrate"}],"identifier":"cas:207511-06-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C80654","ontology_label":"Malic Acid","ontology_source":"NCIT"},"preferred_term":"L-Malic acid disodium salt monohydrate","sssom_rows":[{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic Acid","predicate_id":"skos:broadMatch"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic acid disodium salt monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic acid disodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","synonym_count":0} |
| ev-7ae4a3950b5f799a | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-823ac14862c4c722] | context_only | Predecessor structured review finding f-823ac14862c4c722 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-malic-acid-disodium-salt-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Malic_Acid_Disodium_Salt_Monohydrate (data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for L-Malic_Acid_Disodium_Salt_Monohydrate (data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml,
  record-405458fa4de81278, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    sha256: 4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080
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
  - path: reports/yaml_record_review/L-Malic_Acid_Disodium_Salt_Monohydrate.md
    sha256: 353d131fdf7fb3ebc3d7420924ec6a2e850dd39c131d9a23b6db5608554e7a39
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-405458fa4de81278
  path: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
  label: L-Malic_Acid_Disodium_Salt_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-405458fa4de81278
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-b09dcd58be19aab9
  - ev-72ac8a2c127f2554
  - ev-e0f1d4488fa5b878
  - ev-e9da53f43aaa4ede
  - ev-d67477a1d5bd1e42
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-b09dcd58be19aab9
  - ev-bdc908f9eb3eb8a7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-5eca2d5b1b7dd992
  - ev-bdc908f9eb3eb8a7
  - ev-7ae4a3950b5f799a
evidence:
- evidence_id: ev-b09dcd58be19aab9
  kind: record_content
  reference: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1228],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-06-6","line":1230,"mapping_status":"MAPPED","ontology_id":"NCIT:C80654","preferred_term":"L-Malic
    acid disodium salt monohydrate"}],"identifier":"cas:207511-06-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C80654","ontology_label":"Malic
    Acid","ontology_source":"NCIT"},"preferred_term":"L-Malic acid disodium salt monohydrate","sssom_rows":[{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic
    Acid","predicate_id":"skos:broadMatch"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic
    acid disodium salt monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic
    acid disodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","synonym_count":0}'
  snapshot_sha256: 4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080
- evidence_id: ev-72ac8a2c127f2554
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1228]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e0f1d4488fa5b878
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Malic_Acid_Disodium_Salt_Monohydrate; data-row positions=[1580,
    1581, 1582]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic
    Acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic
    acid disodium salt monohydrate","other":"CAS:207511-06-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic
    acid disodium salt monohydrate","other":"CAS:207511-06-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e9da53f43aaa4ede
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1230]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:207511-06-6","line":1230,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C80654","preferred_term":"L-Malic
    acid disodium salt monohydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5eca2d5b1b7dd992
  kind: prior_review
  reference: reports/yaml_record_review/L-Malic_Acid_Disodium_Salt_Monohydrate.md
  locator: '`data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml`:2;
    Verdict:4; Identity:11; Validation:22; Evidence:33; Completeness:60; Recommended
    Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 353d131fdf7fb3ebc3d7420924ec6a2e850dd39c131d9a23b6db5608554e7a39
  quote: "Recommended Edits:\n- Major: replace `chemical_properties.pubchem_cid`,\
    \ `molecular_formula`,\n  `smiles`, and `inchi` in\n  `data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml`\
    \ with\n  values from a PubChem record that actually resolves CAS RN `207511-06-6`.\n\
    - Major: remove `nutritional_roles.CARBON_SOURCE` and\n  `nutritional_roles.ENERGY_SOURCE`\
    \ unless inspected CultureMech, FEBA, Hans80,\n  or literature sources can support\
    \ L-malic acid disodium salt monohydrate as a\n  carbon and energy source.\n-\
    \ Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation\n\
    \  after those changes."
- evidence_id: ev-bdc908f9eb3eb8a7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[795,1784,1920]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:5c494bf191db4bfed0df","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:0ad3b56193b3bb37d78e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080","finding_id":"SEM:04a0eaa85019c2baeb96","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d67477a1d5bd1e42
  kind: record_content
  reference: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1228],"raw_equal":true},"docs_rows":[{"identifier":"cas:207511-06-6","line":1230,"mapping_status":"MAPPED","ontology_id":"NCIT:C80654","preferred_term":"L-Malic
    acid disodium salt monohydrate"}],"identifier":"cas:207511-06-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C80654","ontology_label":"Malic
    Acid","ontology_source":"NCIT"},"preferred_term":"L-Malic acid disodium salt monohydrate","sssom_rows":[{"data_row":1580,"object_id":"NCIT:C80654","object_label":"Malic
    Acid","predicate_id":"skos:broadMatch"},{"data_row":1581,"object_id":"cas:207511-06-6","object_label":"L-Malic
    acid disodium salt monohydrate","predicate_id":"skos:exactMatch"},{"data_row":1582,"object_id":"kgmicrobe.compound:l-malic_acid_disodium_salt_monohydrate","object_label":"L-Malic
    acid disodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid_Disodium_Salt_Monohydrate","synonym_count":0}'
  snapshot_sha256: 4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080
- evidence_id: ev-7ae4a3950b5f799a
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-823ac14862c4c722]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-823ac14862c4c722 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-bf7253bf81028a04
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-b09dcd58be19aab9
  - ev-72ac8a2c127f2554
  - ev-e0f1d4488fa5b878
  - ev-e9da53f43aaa4ede
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f8b3ca2902641b29
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-5eca2d5b1b7dd992
  - ev-b09dcd58be19aab9
  - ev-bdc908f9eb3eb8a7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z;
    reviewed SHA-256=4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080;
    current SHA-256=4896efa3f3c06d572e3bf8dffffb131ab36f1e1a31fac75394acca8db7c43080;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Malic_Acid_Disodium_Salt_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, NCIT parent, exact CAS and kgmicrobe.compound rows, and hydrate
    review pass, but chemical_properties has the wrong PubChem structure and carbon/energy
    roles are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5eca2d5b1b7dd992
    - ev-b09dcd58be19aab9
  - name: legacy-native-ids
    value: '["SEM:5c494bf191db4bfed0df","SEM:0ad3b56193b3bb37d78e","SEM:04a0eaa85019c2baeb96"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b09dcd58be19aab9
    - ev-5eca2d5b1b7dd992
    - ev-bdc908f9eb3eb8a7
- assessment_id: a-d67477a1d5bd1e42
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-5eca2d5b1b7dd992
  - ev-d67477a1d5bd1e42
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5eca2d5b1b7dd992
    - ev-d67477a1d5bd1e42
findings:
- finding_id: rec-f-823ac14862c4c722
  issue_key: mim-reconciliation-role-support-405458fa4de81278
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Malic acid disodium salt monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-405458fa4de81278
  evidence_ids:
  - ev-5eca2d5b1b7dd992
  - ev-d67477a1d5bd1e42
  - ev-7ae4a3950b5f799a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-823ac14862c4c722
actions:
- action_id: rec-action-823ac14862c4c722
  description: 'Reassess prediction-only role support: L-Malic acid disodium salt
    monohydrate'
  finding_ids:
  - rec-f-823ac14862c4c722
  target_ids:
  - record-405458fa4de81278
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
