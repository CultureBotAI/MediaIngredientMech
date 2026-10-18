# Per-record structured review: DL-2-Aminobutyric_Acid (data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml)

- Review: 20261017T083000Z-dl-2-aminobutyric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for DL-2-Aminobutyric_Acid (data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml, record-6a4d8059b4f70549, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6a4d8059b4f70549 | data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml | maintained | DL-2-Aminobutyric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6a4d8059b4f70549 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6a4d8059b4f70549 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6a4d8059b4f70549 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6a4d8059b4f70549.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6a4d8059b4f70549.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:01:00Z; reviewed SHA-256=e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78; current SHA-256=e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78; hash_changed=False. Reports=["reports/yaml_record_review/DL-2-Aminobutyric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The September stereochemical repair holds, but the amino-acid-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-6a4d8059b4f70549.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d918ac5af1e08434: Reassess prediction-only role support: DL-2-Aminobutyric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-6a4d8059b4f70549.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d918ac5af1e08434

Reassess prediction-only role support: DL-2-Aminobutyric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-15bf7c1ba4988c42 | data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[850],"raw_equal":true},"docs_rows":[{"identifier":"cas:2835-81-6","line":852,"mapping_status":"MAPPED","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric acid"}],"identifier":"cas:2835-81-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35621","ontology_label":"alpha-aminobutyric acid","ontology_source":"CHEBI"},"preferred_term":"DL-2-Aminobutyric acid","sssom_rows":[{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric acid","predicate_id":"skos:broadMatch"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric acid","predicate_id":"skos:exactMatch"},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminobutyric_Acid","synonym_count":1} |
| ev-4c8aef4cf0083f68 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [850] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5e14475831b65831 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:DL-2-Aminobutyric_Acid; data-row positions=[970, 971, 972] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric acid","other":"CAS:2835-81-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":""},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric acid","other":"CAS:2835-81-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":""}] |
| ev-919465d237f51878 | docs/data/mapped_ingredients.csv; CSV lines=[852] | supports | Published identity and count rows inspected: [{"identifier":"cas:2835-81-6","line":852,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric acid","total_occurrences":"0"}] |
| ev-4e732a5235384ec8 | reports/yaml_record_review/DL-2-Aminobutyric_Acid.md; &#96;data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml&#96;:2; Verdict:4; Identity:13; Validation:28; Evidence:48; Completeness:64; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c6b7b893a0fadd5e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[513,1590] | context_only | [{"current_record_sha256":"e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78","finding_id":"SEM:cd7e50d80dfa24bb42e8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78","finding_id":"SEM:cc11d26b6fa09128fc84","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d0af6dd4b32f7378 | data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[850],"raw_equal":true},"docs_rows":[{"identifier":"cas:2835-81-6","line":852,"mapping_status":"MAPPED","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric acid"}],"identifier":"cas:2835-81-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35621","ontology_label":"alpha-aminobutyric acid","ontology_source":"CHEBI"},"preferred_term":"DL-2-Aminobutyric acid","sssom_rows":[{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric acid","predicate_id":"skos:broadMatch"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric acid","predicate_id":"skos:exactMatch"},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminobutyric_Acid","synonym_count":1} |
| ev-e7bcc8f36f1b2270 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-d918ac5af1e08434] | context_only | Predecessor structured review finding f-d918ac5af1e08434 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dl-2-aminobutyric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: DL-2-Aminobutyric_Acid (data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml)'
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
summary: Per-record structured review for DL-2-Aminobutyric_Acid (data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml,
  record-6a4d8059b4f70549, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
    sha256: e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/DL-2-Aminobutyric_Acid.md
    sha256: efd3aec4c7e17e59e78cf0888f9f10d851d15387e62f3362ccbef01edd3929d9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6a4d8059b4f70549
  path: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
  label: DL-2-Aminobutyric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6a4d8059b4f70549
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-15bf7c1ba4988c42
  - ev-4c8aef4cf0083f68
  - ev-5e14475831b65831
  - ev-919465d237f51878
  - ev-d0af6dd4b32f7378
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-15bf7c1ba4988c42
  - ev-c6b7b893a0fadd5e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-4e732a5235384ec8
  - ev-c6b7b893a0fadd5e
  - ev-e7bcc8f36f1b2270
evidence:
- evidence_id: ev-15bf7c1ba4988c42
  kind: record_content
  reference: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[850],"raw_equal":true},"docs_rows":[{"identifier":"cas:2835-81-6","line":852,"mapping_status":"MAPPED","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric
    acid"}],"identifier":"cas:2835-81-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35621","ontology_label":"alpha-aminobutyric
    acid","ontology_source":"CHEBI"},"preferred_term":"DL-2-Aminobutyric acid","sssom_rows":[{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric
    acid","predicate_id":"skos:broadMatch"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric
    acid","predicate_id":"skos:exactMatch"},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminobutyric_Acid","synonym_count":1}'
  snapshot_sha256: e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78
- evidence_id: ev-4c8aef4cf0083f68
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [850]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5e14475831b65831
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:DL-2-Aminobutyric_Acid; data-row positions=[970, 971, 972]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric
    acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric
    acid","other":"CAS:2835-81-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":""},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric
    acid","other":"CAS:2835-81-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-2-Aminobutyric_Acid","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-919465d237f51878
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[852]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:2835-81-6","line":852,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4e732a5235384ec8
  kind: prior_review
  reference: reports/yaml_record_review/DL-2-Aminobutyric_Acid.md
  locator: '`data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml`:2; Verdict:4; Identity:13;
    Validation:28; Evidence:48; Completeness:64; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: efd3aec4c7e17e59e78cf0888f9f10d851d15387e62f3362ccbef01edd3929d9
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml`,\
    \ remove the\n  provisional `AMINO_ACID_SOURCE` role or replace its\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence with inspected claim-level evidence for\n  this supplied form.\n- Regenerate\
    \ synchronized curated and SSSOM products, then rerun\n  `uv run --frozen python\
    \ scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator validate-data\
    \ data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-c6b7b893a0fadd5e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[513,1590]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78","finding_id":"SEM:cd7e50d80dfa24bb42e8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78","finding_id":"SEM:cc11d26b6fa09128fc84","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d0af6dd4b32f7378
  kind: record_content
  reference: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[850],"raw_equal":true},"docs_rows":[{"identifier":"cas:2835-81-6","line":852,"mapping_status":"MAPPED","ontology_id":"CHEBI:35621","preferred_term":"DL-2-Aminobutyric
    acid"}],"identifier":"cas:2835-81-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:35621","ontology_label":"alpha-aminobutyric
    acid","ontology_source":"CHEBI"},"preferred_term":"DL-2-Aminobutyric acid","sssom_rows":[{"data_row":970,"object_id":"CHEBI:35621","object_label":"alpha-aminobutyric
    acid","predicate_id":"skos:broadMatch"},{"data_row":971,"object_id":"cas:2835-81-6","object_label":"DL-2-Aminobutyric
    acid","predicate_id":"skos:exactMatch"},{"data_row":972,"object_id":"kgmicrobe.compound:dl-2-aminobutyric_acid","object_label":"DL-2-Aminobutyric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-2-Aminobutyric_Acid","synonym_count":1}'
  snapshot_sha256: e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78
- evidence_id: ev-e7bcc8f36f1b2270
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-d918ac5af1e08434]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d918ac5af1e08434 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-9ef1ba3386ae3876
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-15bf7c1ba4988c42
  - ev-4c8aef4cf0083f68
  - ev-5e14475831b65831
  - ev-919465d237f51878
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b0b017fca99671f0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-4e732a5235384ec8
  - ev-15bf7c1ba4988c42
  - ev-c6b7b893a0fadd5e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:01:00Z;
    reviewed SHA-256=e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78;
    current SHA-256=e501ada73b6ef2379f63302d706513f4350d8b81585b2a5a917e7b2fa596ed78;
    hash_changed=False. Reports=["reports/yaml_record_review/DL-2-Aminobutyric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The September
    stereochemical repair holds, but the amino-acid-source role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4e732a5235384ec8
    - ev-15bf7c1ba4988c42
  - name: legacy-native-ids
    value: '["SEM:cd7e50d80dfa24bb42e8","SEM:cc11d26b6fa09128fc84"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-15bf7c1ba4988c42
    - ev-4e732a5235384ec8
    - ev-c6b7b893a0fadd5e
- assessment_id: a-d0af6dd4b32f7378
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-4e732a5235384ec8
  - ev-d0af6dd4b32f7378
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4e732a5235384ec8
    - ev-d0af6dd4b32f7378
findings:
- finding_id: rec-f-d918ac5af1e08434
  issue_key: mim-reconciliation-role-support-6a4d8059b4f70549
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: DL-2-Aminobutyric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6a4d8059b4f70549
  evidence_ids:
  - ev-4e732a5235384ec8
  - ev-d0af6dd4b32f7378
  - ev-e7bcc8f36f1b2270
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-d918ac5af1e08434
actions:
- action_id: rec-action-d918ac5af1e08434
  description: 'Reassess prediction-only role support: DL-2-Aminobutyric acid'
  finding_ids:
  - rec-f-d918ac5af1e08434
  target_ids:
  - record-6a4d8059b4f70549
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
