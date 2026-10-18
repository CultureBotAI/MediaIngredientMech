# Per-record structured review: 5-Keto-D-Gluconic_Acid_Potassium_Salt (data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml)

- Review: 20261017T083000Z-5-keto-d-gluconic-acid-potassium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 5-Keto-D-Gluconic_Acid_Potassium_Salt (data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml, record-c28c83652c95a2cb, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c28c83652c95a2cb | data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml | maintained | 5-Keto-D-Gluconic_Acid_Potassium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c28c83652c95a2cb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c28c83652c95a2cb | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c28c83652c95a2cb | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c28c83652c95a2cb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c28c83652c95a2cb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:38:34Z; reviewed SHA-256=4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f; current SHA-256=4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f; hash_changed=False. Reports=["reports/yaml_record_review/5-Keto-D-Gluconic_Acid_Potassium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, potassium-salt chemistry, ChEBI parent, and registry rows pass, but the record exports a non-exact parenthetical synonym and carries two provisional nutritional roles.

### Historical provisional-role concern

evidence: concern. Targets: record-c28c83652c95a2cb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b6ed0146bdc2a474: Reassess prediction-only role support: 5-Keto-D-Gluconic Acid potassium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-c28c83652c95a2cb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b6ed0146bdc2a474

Reassess prediction-only role support: 5-Keto-D-Gluconic Acid potassium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a182d82b72394995 | data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[409],"raw_equal":true},"docs_rows":[{"identifier":"cas:91446-96-7","line":411,"mapping_status":"MAPPED","ontology_id":"CHEBI:17426","preferred_term":"5-Keto-D-Gluconic Acid potassium salt"}],"identifier":"cas:91446-96-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17426","ontology_label":"5-dehydro-D-gluconic acid","ontology_source":"CHEBI"},"preferred_term":"5-Keto-D-Gluconic Acid potassium salt","sssom_rows":[{"data_row":227,"object_id":"CHEBI:17426","object_label":"5-dehydro-D-gluconic acid","predicate_id":"skos:broadMatch"},{"data_row":228,"object_id":"cas:91446-96-7","object_label":"5-Keto-D-Gluconic Acid potassium salt","predicate_id":"skos:exactMatch"},{"data_row":229,"object_id":"kgmicrobe.compound:5-keto-d-gluconic_acid_potassium_salt","object_label":"5-Keto-D-Gluconic Acid potassium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","synonym_count":1} |
| ev-e0bdf9c633abef73 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [409] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd04ec2125a2de9b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt; data-row positions=[227,228,229] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":227,"object_id":"CHEBI:17426","object_label":"5-dehydro-D-gluconic acid","other":"5-Ketogluconate (5-dehydro-D-gluconate)","predicate_id":"skos:broadMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":228,"object_id":"cas:91446-96-7","object_label":"5-Keto-D-Gluconic Acid potassium salt","other":"CAS:91446-96-7","predicate_id":"skos:exactMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":229,"object_id":"kgmicrobe.compound:5-keto-d-gluconic_acid_potassium_salt","object_label":"5-Keto-D-Gluconic Acid potassium salt","other":"CAS:91446-96-7","predicate_id":"skos:exactMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-d11714b8a9bac0bc | docs/data/mapped_ingredients.csv; CSV lines=[411] | supports | Published identity and count rows inspected: [{"identifier":"cas:91446-96-7","line":411,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17426","preferred_term":"5-Keto-D-Gluconic Acid potassium salt","total_occurrences":"0"}] |
| ev-3536e1b151e0c9df | reports/yaml_record_review/5-Keto-D-Gluconic_Acid_Potassium_Salt.md; &#96;data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:37; Completeness:61; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8277952e8620e402 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[163,1809,1840] | context_only | [{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:ec19357b7b34e86beb7f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:8c65a9c78c4e6daabb19","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:750f44f3f7ecec4f91ef","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7874ef7264333217 | data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-de93821cdac90ee8 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-b6ed0146bdc2a474] | context_only | Predecessor structured review finding f-b6ed0146bdc2a474 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-5-keto-d-gluconic-acid-potassium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 5-Keto-D-Gluconic_Acid_Potassium_Salt (data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml)'
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
summary: Per-record structured review for 5-Keto-D-Gluconic_Acid_Potassium_Salt (data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml,
  record-c28c83652c95a2cb, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
    sha256: 4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/5-Keto-D-Gluconic_Acid_Potassium_Salt.md
    sha256: 5992b72be89808c65114d91f724b359938c9c21d3c149aa7577c6653efc1d23c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c28c83652c95a2cb
  path: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
  label: 5-Keto-D-Gluconic_Acid_Potassium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c28c83652c95a2cb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c28c83652c95a2cb
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-c28c83652c95a2cb
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c28c83652c95a2cb
evidence:
- evidence_id: ev-a182d82b72394995
  kind: record_content
  reference: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[409],"raw_equal":true},"docs_rows":[{"identifier":"cas:91446-96-7","line":411,"mapping_status":"MAPPED","ontology_id":"CHEBI:17426","preferred_term":"5-Keto-D-Gluconic
    Acid potassium salt"}],"identifier":"cas:91446-96-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17426","ontology_label":"5-dehydro-D-gluconic
    acid","ontology_source":"CHEBI"},"preferred_term":"5-Keto-D-Gluconic Acid potassium
    salt","sssom_rows":[{"data_row":227,"object_id":"CHEBI:17426","object_label":"5-dehydro-D-gluconic
    acid","predicate_id":"skos:broadMatch"},{"data_row":228,"object_id":"cas:91446-96-7","object_label":"5-Keto-D-Gluconic
    Acid potassium salt","predicate_id":"skos:exactMatch"},{"data_row":229,"object_id":"kgmicrobe.compound:5-keto-d-gluconic_acid_potassium_salt","object_label":"5-Keto-D-Gluconic
    Acid potassium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","synonym_count":1}'
  snapshot_sha256: 4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f
- evidence_id: ev-e0bdf9c633abef73
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [409]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd04ec2125a2de9b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt; data-row positions=[227,228,229]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":227,"object_id":"CHEBI:17426","object_label":"5-dehydro-D-gluconic
    acid","other":"5-Ketogluconate (5-dehydro-D-gluconate)","predicate_id":"skos:broadMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":228,"object_id":"cas:91446-96-7","object_label":"5-Keto-D-Gluconic
    Acid potassium salt","other":"CAS:91446-96-7","predicate_id":"skos:exactMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":229,"object_id":"kgmicrobe.compound:5-keto-d-gluconic_acid_potassium_salt","object_label":"5-Keto-D-Gluconic
    Acid potassium salt","other":"CAS:91446-96-7","predicate_id":"skos:exactMatch","subject_id":"MIM:5-Keto-D-Gluconic_Acid_Potassium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d11714b8a9bac0bc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[411]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:91446-96-7","line":411,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17426","preferred_term":"5-Keto-D-Gluconic
    Acid potassium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3536e1b151e0c9df
  kind: prior_review
  reference: reports/yaml_record_review/5-Keto-D-Gluconic_Acid_Potassium_Salt.md
  locator: '`data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml`:2;
    Verdict:4; Identity:12; Validation:26; Evidence:37; Completeness:61; Recommended
    Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5992b72be89808c65114d91f724b359938c9c21d3c149aa7577c6653efc1d23c
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml`,\n\
    \  remove `5-Ketogluconate (5-dehydro-D-gluconate)` from `synonyms`, or move it\n\
    \  to a non-exact source-occurrence surface that the SSSOM exporter will not emit\n\
    \  as an exact `other` value for `cas:91446-96-7`; rebuild\n  `mappings/ingredient_mappings.sssom.tsv`\
    \ and the aggregate\n  `data/curated/mapped_ingredients.yaml`.\n- In the same\
    \ maintained YAML, either remove the provisional `CARBON_SOURCE`\n  and `ENERGY_SOURCE`\
    \ roles or replace the computational placeholders with\n  source-backed evidence\
    \ scoped to this salt; rerun\n  `uv run --frozen python scripts/validate_strict.py`\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py` after the\
    \ edit."
- evidence_id: ev-8277952e8620e402
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[163,1809,1840]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:ec19357b7b34e86beb7f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:8c65a9c78c4e6daabb19","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f","finding_id":"SEM:750f44f3f7ecec4f91ef","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7874ef7264333217
  kind: record_content
  reference: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f
- evidence_id: ev-de93821cdac90ee8
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-b6ed0146bdc2a474]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b6ed0146bdc2a474 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-9eecc4c5c3648342
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c28c83652c95a2cb
  evidence_ids:
  - ev-a182d82b72394995
  - ev-e0bdf9c633abef73
  - ev-dd04ec2125a2de9b
  - ev-d11714b8a9bac0bc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8cfe32205fb33b43
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c28c83652c95a2cb
  evidence_ids:
  - ev-3536e1b151e0c9df
  - ev-a182d82b72394995
  - ev-8277952e8620e402
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:38:34Z;
    reviewed SHA-256=4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f;
    current SHA-256=4715d7c9d7bb965f7f3db53cf64b2cfb1ac1a748dc0af3b38ca38ca5c888e42f;
    hash_changed=False. Reports=["reports/yaml_record_review/5-Keto-D-Gluconic_Acid_Potassium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, potassium-salt chemistry, ChEBI parent, and registry rows pass,
    but the record exports a non-exact parenthetical synonym and carries two provisional
    nutritional roles.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3536e1b151e0c9df
    - ev-a182d82b72394995
  - name: legacy-native-ids
    value: '["SEM:ec19357b7b34e86beb7f","SEM:8c65a9c78c4e6daabb19","SEM:750f44f3f7ecec4f91ef"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a182d82b72394995
    - ev-3536e1b151e0c9df
    - ev-8277952e8620e402
- assessment_id: a-7874ef7264333217
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c28c83652c95a2cb
  evidence_ids:
  - ev-3536e1b151e0c9df
  - ev-7874ef7264333217
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3536e1b151e0c9df
    - ev-7874ef7264333217
findings:
- finding_id: rec-f-b6ed0146bdc2a474
  issue_key: mim-reconciliation-role-support-c28c83652c95a2cb
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 5-Keto-D-Gluconic Acid potassium
    salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c28c83652c95a2cb
  evidence_ids:
  - ev-3536e1b151e0c9df
  - ev-7874ef7264333217
  - ev-de93821cdac90ee8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-b6ed0146bdc2a474
actions:
- action_id: rec-action-b6ed0146bdc2a474
  description: 'Reassess prediction-only role support: 5-Keto-D-Gluconic Acid potassium
    salt'
  finding_ids:
  - rec-f-b6ed0146bdc2a474
  target_ids:
  - record-c28c83652c95a2cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
