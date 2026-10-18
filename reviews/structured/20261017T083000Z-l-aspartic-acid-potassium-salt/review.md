# Per-record structured review: L-Aspartic_Acid_Potassium_Salt (data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml)

- Review: 20261017T083000Z-l-aspartic-acid-potassium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Aspartic_Acid_Potassium_Salt (data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml, record-5a26b130defc6088, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5a26b130defc6088 | data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml | maintained | L-Aspartic_Acid_Potassium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5a26b130defc6088 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5a26b130defc6088 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5a26b130defc6088 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5a26b130defc6088.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5a26b130defc6088.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:33Z; reviewed SHA-256=1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e; current SHA-256=1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050233Z-L-Aspartic_Acid_Potassium_Salt.md","reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md&#96; after the record changed from c3bd6c8b66450d9bf49816dcd43cb0fabc2733221fccb293cc1c23ed12968505 to 1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-5a26b130defc6088.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-215bf391c3ec606a: Reassess prediction-only role support: L-Aspartic acid potassium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-5a26b130defc6088.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-215bf391c3ec606a

Reassess prediction-only role support: L-Aspartic acid potassium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-030f10a2c4bb82a9 | data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1216],"raw_equal":true},"docs_rows":[{"identifier":"cas:1115-63-5","line":1218,"mapping_status":"MAPPED","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic acid potassium salt"}],"identifier":"cas:1115-63-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17053","ontology_label":"L-aspartic acid","ontology_source":"CHEBI"},"preferred_term":"L-Aspartic acid potassium salt","sssom_rows":[{"data_row":1560,"object_id":"CHEBI:17053","object_label":"L-aspartic acid","predicate_id":"skos:broadMatch"},{"data_row":1561,"object_id":"cas:1115-63-5","object_label":"L-Aspartic acid potassium salt","predicate_id":"skos:exactMatch"},{"data_row":1562,"object_id":"kgmicrobe.compound:l-aspartic_acid_potassium_salt","object_label":"L-Aspartic acid potassium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Aspartic_Acid_Potassium_Salt","synonym_count":2} |
| ev-294666258d54a6d2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1216] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-55902fe167ec03f1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Aspartic_Acid_Potassium_Salt; data-row positions=[1560,1561,1562] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1560,"object_id":"CHEBI:17053","object_label":"L-aspartic acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1561,"object_id":"cas:1115-63-5","object_label":"L-Aspartic acid potassium salt","other":"CAS:1115-63-5","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1562,"object_id":"kgmicrobe.compound:l-aspartic_acid_potassium_salt","object_label":"L-Aspartic acid potassium salt","other":"CAS:1115-63-5","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-75c8ff000a9f7754 | docs/data/mapped_ingredients.csv; CSV lines=[1218] | supports | Published identity and count rows inspected: [{"identifier":"cas:1115-63-5","line":1218,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic acid potassium salt","total_occurrences":"1"}] |
| ev-7e4e43f7655af90d | reports/yaml_record_review/20261001T050233Z-L-Aspartic_Acid_Potassium_Salt.md; YAML Record Review: L-Aspartic acid potassium salt:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f13b26cc73a4e6ba | reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md; &#96;data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:57; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-21b33ab905007953 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[783,1872] | context_only | [{"current_record_sha256":"1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e","finding_id":"SEM:582b2d6764f7068cf922","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e","finding_id":"SEM:4bd73f77dc3937c682d0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-beefba3df6b94613 | data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-263b84a4ed941cde | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-215bf391c3ec606a] | context_only | Predecessor structured review finding f-215bf391c3ec606a in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-aspartic-acid-potassium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Aspartic_Acid_Potassium_Salt (data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml)'
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
summary: Per-record structured review for L-Aspartic_Acid_Potassium_Salt (data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml,
  record-5a26b130defc6088, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
    sha256: 1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e
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
  - path: reports/yaml_record_review/20261001T050233Z-L-Aspartic_Acid_Potassium_Salt.md
    sha256: c4ee5ef21c98e88f75a108df0796a1a11cacd92e86af8975a692b130a3b89f3a
    role: context
  - path: reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md
    sha256: d27d6725d3f9a631431ec4e9228fc137648530c3867796cb0d11b5f72d2b6ffd
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5a26b130defc6088
  path: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
  label: L-Aspartic_Acid_Potassium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5a26b130defc6088
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5a26b130defc6088
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5a26b130defc6088
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5a26b130defc6088
evidence:
- evidence_id: ev-030f10a2c4bb82a9
  kind: record_content
  reference: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1216],"raw_equal":true},"docs_rows":[{"identifier":"cas:1115-63-5","line":1218,"mapping_status":"MAPPED","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic
    acid potassium salt"}],"identifier":"cas:1115-63-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17053","ontology_label":"L-aspartic
    acid","ontology_source":"CHEBI"},"preferred_term":"L-Aspartic acid potassium salt","sssom_rows":[{"data_row":1560,"object_id":"CHEBI:17053","object_label":"L-aspartic
    acid","predicate_id":"skos:broadMatch"},{"data_row":1561,"object_id":"cas:1115-63-5","object_label":"L-Aspartic
    acid potassium salt","predicate_id":"skos:exactMatch"},{"data_row":1562,"object_id":"kgmicrobe.compound:l-aspartic_acid_potassium_salt","object_label":"L-Aspartic
    acid potassium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Aspartic_Acid_Potassium_Salt","synonym_count":2}'
  snapshot_sha256: 1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e
- evidence_id: ev-294666258d54a6d2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1216]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-55902fe167ec03f1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Aspartic_Acid_Potassium_Salt; data-row positions=[1560,1561,1562]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1560,"object_id":"CHEBI:17053","object_label":"L-aspartic
    acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1561,"object_id":"cas:1115-63-5","object_label":"L-Aspartic
    acid potassium salt","other":"CAS:1115-63-5","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1562,"object_id":"kgmicrobe.compound:l-aspartic_acid_potassium_salt","object_label":"L-Aspartic
    acid potassium salt","other":"CAS:1115-63-5","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Aspartic_Acid_Potassium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-75c8ff000a9f7754
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1218]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:1115-63-5","line":1218,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17053","preferred_term":"L-Aspartic
    acid potassium salt","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7e4e43f7655af90d
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050233Z-L-Aspartic_Acid_Potassium_Salt.md
  locator: 'YAML Record Review: L-Aspartic acid potassium salt:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c4ee5ef21c98e88f75a108df0796a1a11cacd92e86af8975a692b130a3b89f3a
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CAS primary
    identity, potassium-salt PubChem structure, ChEBI parent mapping, registry rows,
    and occurrence count pass, but parent L-aspartic acid synonyms publish on the
    salt mapping and AMINO_ACID_SOURCE is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`,
    `just validate-terms data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-f13b26cc73a4e6ba
  kind: prior_review
  reference: reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md
  locator: '`data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`:2; Verdict:4;
    Identity:11; Validation:21; Evidence:32; Completeness:57; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d27d6725d3f9a631431ec4e9228fc137648530c3867796cb0d11b5f72d2b6ffd
  quote: "Recommended Edits:\n- Major: remove or demote `(2S)-2-aminobutanedioic acid`\
    \ and `ASPARTIC ACID` in\n  `data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`,\
    \ then\n  regenerate the aggregate and final SSSOM.\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ unless an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-aspartic acid\n  potassium salt as an amino acid source.\n- Rerun strict,\
    \ term, round-trip, component, and SSSOM validation after those\n  changes."
- evidence_id: ev-21b33ab905007953
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[783,1872]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e","finding_id":"SEM:582b2d6764f7068cf922","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e","finding_id":"SEM:4bd73f77dc3937c682d0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-beefba3df6b94613
  kind: record_content
  reference: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e
- evidence_id: ev-263b84a4ed941cde
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-215bf391c3ec606a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-215bf391c3ec606a in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-16f99c63ed72eecd
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5a26b130defc6088
  evidence_ids:
  - ev-030f10a2c4bb82a9
  - ev-294666258d54a6d2
  - ev-55902fe167ec03f1
  - ev-75c8ff000a9f7754
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-69f26ee614b79db6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5a26b130defc6088
  evidence_ids:
  - ev-7e4e43f7655af90d
  - ev-f13b26cc73a4e6ba
  - ev-030f10a2c4bb82a9
  - ev-21b33ab905007953
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:33Z;
    reviewed SHA-256=1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e;
    current SHA-256=1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050233Z-L-Aspartic_Acid_Potassium_Salt.md","reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/L-Aspartic_Acid_Potassium_Salt.md` after the record
    changed from c3bd6c8b66450d9bf49816dcd43cb0fabc2733221fccb293cc1c23ed12968505
    to 1799f0371433518f3a4add09e07a602ffbc153545880ce15666f6b0399f51a3e; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7e4e43f7655af90d
    - ev-f13b26cc73a4e6ba
    - ev-030f10a2c4bb82a9
  - name: legacy-native-ids
    value: '["SEM:582b2d6764f7068cf922","SEM:4bd73f77dc3937c682d0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-030f10a2c4bb82a9
    - ev-7e4e43f7655af90d
    - ev-f13b26cc73a4e6ba
    - ev-21b33ab905007953
- assessment_id: a-beefba3df6b94613
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5a26b130defc6088
  evidence_ids:
  - ev-7e4e43f7655af90d
  - ev-f13b26cc73a4e6ba
  - ev-beefba3df6b94613
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7e4e43f7655af90d
    - ev-f13b26cc73a4e6ba
    - ev-beefba3df6b94613
findings:
- finding_id: rec-f-215bf391c3ec606a
  issue_key: mim-reconciliation-role-support-5a26b130defc6088
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Aspartic acid potassium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5a26b130defc6088
  evidence_ids:
  - ev-7e4e43f7655af90d
  - ev-f13b26cc73a4e6ba
  - ev-beefba3df6b94613
  - ev-263b84a4ed941cde
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
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
    finding_id: f-215bf391c3ec606a
actions:
- action_id: rec-action-215bf391c3ec606a
  description: 'Reassess prediction-only role support: L-Aspartic acid potassium salt'
  finding_ids:
  - rec-f-215bf391c3ec606a
  target_ids:
  - record-5a26b130defc6088
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml
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
