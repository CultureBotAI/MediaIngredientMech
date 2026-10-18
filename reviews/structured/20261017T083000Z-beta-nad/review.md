# Per-record structured review: Beta-nad (data/ingredients/mapped/Beta-nad.yaml)

- Review: 20261017T083000Z-beta-nad
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beta-nad (data/ingredients/mapped/Beta-nad.yaml, record-9b2dcfd7a3735c04, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beta-nad.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beta-nad.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9b2dcfd7a3735c04 | data/ingredients/mapped/Beta-nad.yaml | maintained | Beta-nad |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9b2dcfd7a3735c04 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9b2dcfd7a3735c04 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9b2dcfd7a3735c04 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9b2dcfd7a3735c04.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9b2dcfd7a3735c04.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:43:55Z; reviewed SHA-256=0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e; current SHA-256=0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e; hash_changed=False. Reports=["reports/yaml_record_review/Beta-nad.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI NAD(+) identity, aliases, CAS xref, ChEBI structure fields, SSSOM row, and aggregate copy pass, but chemical_properties.data_source is stale.

### Historical provisional-role concern

evidence: concern. Targets: record-9b2dcfd7a3735c04.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-9b2dcfd7a3735c04: Reassess prediction-only or empty role support: Beta-nad

major / open / confirmed; issue key: mim-reconciliation-role-support-9b2dcfd7a3735c04.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-9b2dcfd7a3735c04

Reassess prediction-only or empty role support: Beta-nad

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-607cdd7e546c791a | data/ingredients/mapped/Beta-nad.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[580],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15846","line":582,"mapping_status":"MAPPED","ontology_id":"CHEBI:15846","preferred_term":"beta-NAD"}],"identifier":"CHEBI:15846","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":17,"edge_count":17,"occurrences":17},"occurrence_statistics":{"media_count":17,"total_occurrences":17},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15846","ontology_label":"NAD(+)","ontology_source":"CHEBI"},"preferred_term":"beta-NAD","sssom_rows":[{"data_row":534,"object_id":"CHEBI:15846","object_label":"NAD(+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beta-nad","synonym_count":11} |
| ev-f6a2bb29c66fc88d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [580] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a22df8ae46d59a41 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beta-nad; data-row positions=[534] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":534,"object_id":"CHEBI:15846","object_label":"NAD(+)","other":"\u00df-NAD&#124;\u00df-nicotinamide adenine dinucleotide&#124;NAD+&#124;Nicotinamide adenine dinucleotide&#124;adenosine 5'-{3-[1-(3-carbamoylpyridinio)-1,4-anhydro-D-ribitol-5-yl] dihydrogen diphosphate}&#124;NAD&#124;nicotinamide adenine dinucleotide (NAD)&#124;NAD (Sigma)&#124;\u03b2-NAD&#124;\u03b2--NAD&#124;CAS:53-84-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Beta-nad","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5a7b951a57ac60f8 | docs/data/mapped_ingredients.csv; CSV lines=[582] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15846","line":582,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"17","ontology_id":"CHEBI:15846","preferred_term":"beta-NAD","total_occurrences":"17"}] |
| ev-938e5c0260ad2d60 | reports/yaml_record_review/Beta-nad.md; &#96;data/ingredients/mapped/Beta-nad.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:35; Completeness:56; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a619175a50be1b4d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[310,1630] | context_only | [{"current_record_sha256":"0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e","finding_id":"SEM:8671013fbe09ccdfeb11","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e","finding_id":"SEM:0b640ed902372ffa43ff","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8017eeb531bc00ab | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Beta-nad.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beta-nad
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beta-nad (data/ingredients/mapped/Beta-nad.yaml)'
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
summary: Per-record structured review for Beta-nad (data/ingredients/mapped/Beta-nad.yaml,
  record-9b2dcfd7a3735c04, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beta-nad.yaml
    sha256: 0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e
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
  - path: reports/yaml_record_review/Beta-nad.md
    sha256: 9af8ca4a464694d10b1057601889736c30da7c130ad98f33164f955b9d598916
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9b2dcfd7a3735c04
  path: data/ingredients/mapped/Beta-nad.yaml
  label: Beta-nad
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-nad.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beta-nad.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beta-nad.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9b2dcfd7a3735c04
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9b2dcfd7a3735c04
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9b2dcfd7a3735c04
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9b2dcfd7a3735c04
evidence:
- evidence_id: ev-607cdd7e546c791a
  kind: record_content
  reference: data/ingredients/mapped/Beta-nad.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[580],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15846","line":582,"mapping_status":"MAPPED","ontology_id":"CHEBI:15846","preferred_term":"beta-NAD"}],"identifier":"CHEBI:15846","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":17,"edge_count":17,"occurrences":17},"occurrence_statistics":{"media_count":17,"total_occurrences":17},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15846","ontology_label":"NAD(+)","ontology_source":"CHEBI"},"preferred_term":"beta-NAD","sssom_rows":[{"data_row":534,"object_id":"CHEBI:15846","object_label":"NAD(+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beta-nad","synonym_count":11}'
  snapshot_sha256: 0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e
- evidence_id: ev-f6a2bb29c66fc88d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [580]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a22df8ae46d59a41
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beta-nad; data-row positions=[534]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":534,"object_id":"CHEBI:15846","object_label":"NAD(+)","other":"\u00df-NAD|\u00df-nicotinamide
    adenine dinucleotide|NAD+|Nicotinamide adenine dinucleotide|adenosine 5''-{3-[1-(3-carbamoylpyridinio)-1,4-anhydro-D-ribitol-5-yl]
    dihydrogen diphosphate}|NAD|nicotinamide adenine dinucleotide (NAD)|NAD (Sigma)|\u03b2-NAD|\u03b2--NAD|CAS:53-84-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Beta-nad","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5a7b951a57ac60f8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[582]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15846","line":582,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"17","ontology_id":"CHEBI:15846","preferred_term":"beta-NAD","total_occurrences":"17"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-938e5c0260ad2d60
  kind: prior_review
  reference: reports/yaml_record_review/Beta-nad.md
  locator: '`data/ingredients/mapped/Beta-nad.yaml`:2; Verdict:4; Identity:11; Validation:25;
    Evidence:35; Completeness:56; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9af8ca4a464694d10b1057601889736c30da7c130ad98f33164f955b9d598916
  quote: "Recommended Edits:\n- Minor: update `data/ingredients/mapped/Beta-nad.yaml`\
    \ so\n  `chemical_properties.data_source` accurately names the source of the\n\
    \  `CHEBI:15846` formula, InChI, SMILES, and mass; then run\n  `just sync-curated`\
    \ and focused strict/term validation for the record."
- evidence_id: ev-a619175a50be1b4d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[310,1630]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e","finding_id":"SEM:8671013fbe09ccdfeb11","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e","finding_id":"SEM:0b640ed902372ffa43ff","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8017eeb531bc00ab
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Beta-nad.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cb6c2ebceebb87bc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9b2dcfd7a3735c04
  evidence_ids:
  - ev-607cdd7e546c791a
  - ev-f6a2bb29c66fc88d
  - ev-a22df8ae46d59a41
  - ev-5a7b951a57ac60f8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ab3d54646fafd941
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b2dcfd7a3735c04
  evidence_ids:
  - ev-938e5c0260ad2d60
  - ev-607cdd7e546c791a
  - ev-a619175a50be1b4d
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:43:55Z;
    reviewed SHA-256=0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e;
    current SHA-256=0bd44bae290a7c70cac9a511ccd66088d2322ced90006f0dd02656e725c8652e;
    hash_changed=False. Reports=["reports/yaml_record_review/Beta-nad.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI NAD(+)
    identity, aliases, CAS xref, ChEBI structure fields, SSSOM row, and aggregate
    copy pass, but chemical_properties.data_source is stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-938e5c0260ad2d60
    - ev-607cdd7e546c791a
  - name: legacy-native-ids
    value: '["SEM:8671013fbe09ccdfeb11","SEM:0b640ed902372ffa43ff"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-607cdd7e546c791a
    - ev-938e5c0260ad2d60
    - ev-a619175a50be1b4d
- assessment_id: a-role-9b2dcfd7a3735c04
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-9b2dcfd7a3735c04
  evidence_ids:
  - ev-607cdd7e546c791a
  - ev-8017eeb531bc00ab
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-607cdd7e546c791a
    - ev-8017eeb531bc00ab
findings:
- finding_id: rec-f-role-9b2dcfd7a3735c04
  issue_key: mim-reconciliation-role-support-9b2dcfd7a3735c04
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beta-nad'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-9b2dcfd7a3735c04
  evidence_ids:
  - ev-607cdd7e546c791a
  - ev-8017eeb531bc00ab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-nad.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-9b2dcfd7a3735c04
  description: 'Reassess prediction-only or empty role support: Beta-nad'
  finding_ids:
  - rec-f-role-9b2dcfd7a3735c04
  target_ids:
  - record-9b2dcfd7a3735c04
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-nad.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
