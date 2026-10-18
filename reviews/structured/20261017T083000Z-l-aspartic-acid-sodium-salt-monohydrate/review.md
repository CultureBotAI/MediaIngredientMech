# Per-record structured review: L-Aspartic_Acid_Sodium_Salt_Monohydrate (data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml)

- Review: 20261017T083000Z-l-aspartic-acid-sodium-salt-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Aspartic_Acid_Sodium_Salt_Monohydrate (data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml, record-a03ccf06803d79d1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a03ccf06803d79d1 | data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml | maintained | L-Aspartic_Acid_Sodium_Salt_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a03ccf06803d79d1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a03ccf06803d79d1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a03ccf06803d79d1 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a03ccf06803d79d1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a03ccf06803d79d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:34Z; reviewed SHA-256=b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; current SHA-256=b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050234Z-L-Aspartic_Acid_Sodium_Salt_Monohydrate.md","reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md&#96; after the record changed from 2adc6833819d70d555e0573db31372d89bac15511a6d6f3c994297304808579e to b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-a03ccf06803d79d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-da43714a60aa3bba: Reassess prediction-only role support: L-Aspartic acid sodium salt monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-a03ccf06803d79d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-da43714a60aa3bba

Reassess prediction-only role support: L-Aspartic acid sodium salt monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c90feb771030e101 | data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1217],"raw_equal":true},"docs_rows":[{"identifier":"cas:323194-76-9","line":1219,"mapping_status":"MAPPED","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic acid sodium salt monohydrate"}],"identifier":"cas:323194-76-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17053","ontology_label":"L-aspartic acid","ontology_source":"CHEBI"},"preferred_term":"L-Aspartic acid sodium salt monohydrate","sssom_rows":[{"data_row":1563,"object_id":"CHEBI:17053","object_label":"L-aspartic acid","predicate_id":"skos:closeMatch"},{"data_row":1564,"object_id":"cas:323194-76-9","object_label":"L-Aspartic acid sodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","synonym_count":2} |
| ev-a947ba29cfc855f8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1217] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2017ad3ad12d0170 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate; data-row positions=[1563,1564] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1563,"object_id":"CHEBI:17053","object_label":"L-aspartic acid","other":"CAS:323194-76-9","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":1564,"object_id":"cas:323194-76-9","object_label":"L-Aspartic acid sodium salt monohydrate","other":"CAS:323194-76-9","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-6fdc733a830a5b85 | docs/data/mapped_ingredients.csv; CSV lines=[1219] | supports | Published identity and count rows inspected: [{"identifier":"cas:323194-76-9","line":1219,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic acid sodium salt monohydrate","total_occurrences":"2"}] |
| ev-7fda4658e83bf9be | reports/yaml_record_review/20261001T050234Z-L-Aspartic_Acid_Sodium_Salt_Monohydrate.md; YAML Record Review: L-Aspartic acid sodium salt monohydrate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0397e19e10b1c884 | reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md; &#96;data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:34; Completeness:62; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-86e9bbabaae7761b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[784,1765] | context_only | [{"current_record_sha256":"b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa","finding_id":"SEM:42ca6dc8a4b2bfa841ac","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa","finding_id":"SEM:4a110550f7042475f889","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f41c2a4ef6a1cee5 | data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-ddd2e281c5e64753 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-da43714a60aa3bba] | context_only | Predecessor structured review finding f-da43714a60aa3bba in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-aspartic-acid-sodium-salt-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Aspartic_Acid_Sodium_Salt_Monohydrate (data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml)'
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
summary: Per-record structured review for L-Aspartic_Acid_Sodium_Salt_Monohydrate
  (data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml, record-a03ccf06803d79d1,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
    sha256: b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa
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
  - path: reports/yaml_record_review/20261001T050234Z-L-Aspartic_Acid_Sodium_Salt_Monohydrate.md
    sha256: 6336d3abc085ef849ae067f184728c3caa127bdc5895b02d40454718904f8523
    role: context
  - path: reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md
    sha256: 9a77e3c7603e3d63ac461e20eb0402e9dc8c36b957217c7c0395db7c8dfb1405
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a03ccf06803d79d1
  path: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
  label: L-Aspartic_Acid_Sodium_Salt_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a03ccf06803d79d1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a03ccf06803d79d1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a03ccf06803d79d1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a03ccf06803d79d1
evidence:
- evidence_id: ev-c90feb771030e101
  kind: record_content
  reference: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1217],"raw_equal":true},"docs_rows":[{"identifier":"cas:323194-76-9","line":1219,"mapping_status":"MAPPED","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic
    acid sodium salt monohydrate"}],"identifier":"cas:323194-76-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:17053","ontology_label":"L-aspartic
    acid","ontology_source":"CHEBI"},"preferred_term":"L-Aspartic acid sodium salt
    monohydrate","sssom_rows":[{"data_row":1563,"object_id":"CHEBI:17053","object_label":"L-aspartic
    acid","predicate_id":"skos:closeMatch"},{"data_row":1564,"object_id":"cas:323194-76-9","object_label":"L-Aspartic
    acid sodium salt monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","synonym_count":2}'
  snapshot_sha256: b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa
- evidence_id: ev-a947ba29cfc855f8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1217]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2017ad3ad12d0170
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate; data-row positions=[1563,1564]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1563,"object_id":"CHEBI:17053","object_label":"L-aspartic
    acid","other":"CAS:323194-76-9","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":1564,"object_id":"cas:323194-76-9","object_label":"L-Aspartic
    acid sodium salt monohydrate","other":"CAS:323194-76-9","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6fdc733a830a5b85
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1219]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:323194-76-9","line":1219,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic
    acid sodium salt monohydrate","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7fda4658e83bf9be
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050234Z-L-Aspartic_Acid_Sodium_Salt_Monohydrate.md
  locator: 'YAML Record Review: L-Aspartic acid sodium salt monohydrate:2; Target:10;
    Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52;
    Recommended Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6336d3abc085ef849ae067f184728c3caa127bdc5895b02d40454718904f8523
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CAS primary
    identity, sodium-salt monohydrate structure, close parent mapping, exact CAS row,
    and hydrate review pass, but the local registry anchor is missing, parent synonyms
    publish, and AMINO_ACID_SOURCE is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`,
    `just validate-terms data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-0397e19e10b1c884
  kind: prior_review
  reference: reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md
  locator: '`data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`:2;
    Verdict:4; Identity:12; Validation:23; Evidence:34; Completeness:62; Recommended
    Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9a77e3c7603e3d63ac461e20eb0402e9dc8c36b957217c7c0395db7c8dfb1405
  quote: "Recommended Edits:\n- Major: repair final SSSOM generation for this CAS-primary\
    \ close-match hydrate\n  so `MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate` receives\
    \ an exact local\n  `kgmicrobe.compound:l-aspartic_acid_sodium_salt_monohydrate`\
    \ row alongside\n  the close parent and exact CAS rows.\n- Major: remove or demote\
    \ `(2S)-2-aminobutanedioic acid` and `ASPARTIC ACID` in\n  `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`.\n\
    - Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected\n  CultureMech,\
    \ FEBA, Hans80, or literature source can support this exact\n  sodium-salt monohydrate\
    \ form as an amino acid source.\n- Rerun strict, term, hydrate, round-trip, component,\
    \ and SSSOM validation after\n  those changes."
- evidence_id: ev-86e9bbabaae7761b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[784,1765]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa","finding_id":"SEM:42ca6dc8a4b2bfa841ac","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa","finding_id":"SEM:4a110550f7042475f889","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f41c2a4ef6a1cee5
  kind: record_content
  reference: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa
- evidence_id: ev-ddd2e281c5e64753
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-da43714a60aa3bba]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-da43714a60aa3bba in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-018b99da7a0e2e22
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a03ccf06803d79d1
  evidence_ids:
  - ev-c90feb771030e101
  - ev-a947ba29cfc855f8
  - ev-2017ad3ad12d0170
  - ev-6fdc733a830a5b85
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7b48c7ed610c1c9e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a03ccf06803d79d1
  evidence_ids:
  - ev-7fda4658e83bf9be
  - ev-0397e19e10b1c884
  - ev-c90feb771030e101
  - ev-86e9bbabaae7761b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:34Z;
    reviewed SHA-256=b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa;
    current SHA-256=b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050234Z-L-Aspartic_Acid_Sodium_Salt_Monohydrate.md","reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/L-Aspartic_Acid_Sodium_Salt_Monohydrate.md` after
    the record changed from 2adc6833819d70d555e0573db31372d89bac15511a6d6f3c994297304808579e
    to b08b501b65a3b83edd2af58a9c3818b3f998c3c2e382458d6af07dae5a6cb0aa; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7fda4658e83bf9be
    - ev-0397e19e10b1c884
    - ev-c90feb771030e101
  - name: legacy-native-ids
    value: '["SEM:42ca6dc8a4b2bfa841ac","SEM:4a110550f7042475f889"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c90feb771030e101
    - ev-7fda4658e83bf9be
    - ev-0397e19e10b1c884
    - ev-86e9bbabaae7761b
- assessment_id: a-f41c2a4ef6a1cee5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a03ccf06803d79d1
  evidence_ids:
  - ev-7fda4658e83bf9be
  - ev-0397e19e10b1c884
  - ev-f41c2a4ef6a1cee5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7fda4658e83bf9be
    - ev-0397e19e10b1c884
    - ev-f41c2a4ef6a1cee5
findings:
- finding_id: rec-f-da43714a60aa3bba
  issue_key: mim-reconciliation-role-support-a03ccf06803d79d1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Aspartic acid sodium salt monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a03ccf06803d79d1
  evidence_ids:
  - ev-7fda4658e83bf9be
  - ev-0397e19e10b1c884
  - ev-f41c2a4ef6a1cee5
  - ev-ddd2e281c5e64753
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-da43714a60aa3bba
actions:
- action_id: rec-action-da43714a60aa3bba
  description: 'Reassess prediction-only role support: L-Aspartic acid sodium salt
    monohydrate'
  finding_ids:
  - rec-f-da43714a60aa3bba
  target_ids:
  - record-a03ccf06803d79d1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml
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
