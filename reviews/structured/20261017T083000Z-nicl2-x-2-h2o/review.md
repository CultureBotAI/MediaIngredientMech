# Per-record structured review: Nicl2_X_2_H2o (data/ingredients/mapped/Nicl2_X_2_H2o.yaml)

- Review: 20261017T083000Z-nicl2-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nicl2_X_2_H2o (data/ingredients/mapped/Nicl2_X_2_H2o.yaml, record-5f2d78dbe06a0f9d, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nicl2_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nicl2_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5f2d78dbe06a0f9d | data/ingredients/mapped/Nicl2_X_2_H2o.yaml | maintained | Nicl2_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5f2d78dbe06a0f9d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5f2d78dbe06a0f9d | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5f2d78dbe06a0f9d | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5f2d78dbe06a0f9d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5f2d78dbe06a0f9d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:01Z; reviewed SHA-256=ab4f6d9e5c9b4b7bf7151b6541d357f074ac6b4876cc61fd8be82cf7c85b46dd; current SHA-256=63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050301Z-Nicl2_X_2_H2o.md","reports/yaml_record_review/Nicl2_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Nicl2_X_2_H2o.md&#96; after the record changed from 6b43693a206b10af5013fa73afea10360d69666ed0a90dcb0f00618bdff297dc to ab4f6d9e5c9b4b7bf7151b6541d357f074ac6b4876cc61fd8be82cf7c85b46dd; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-5f2d78dbe06a0f9d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a55340403d52f750: Reassess prediction-only role support: NiCl2 x 2 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-5f2d78dbe06a0f9d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a55340403d52f750

Reassess prediction-only role support: NiCl2 x 2 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7b4eed946bdc587b | data/ingredients/mapped/Nicl2_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1556],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_status":"MAPPED","ontology_id":"CHEBI:34887","preferred_term":"NiCl2 x 2 H2O"}],"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":21},"occurrence_statistics":{"media_count":20,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34887","ontology_label":"nickel dichloride","ontology_source":"CHEBI"},"preferred_term":"NiCl2 x 2 H2O","sssom_rows":[{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel dichloride","predicate_id":"skos:closeMatch"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2 x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nicl2_X_2_H2o","synonym_count":18} |
| ev-435536912b4bfafc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1556] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-63cccdf04618bf60 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nicl2_X_2_H2o; data-row positions=[2083, 2084] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel dichloride","other":"NiCl2 x 2H2O&#124;NiCl2\u00b72H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Nicl2_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2 x 2 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Nicl2_X_2_H2o","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-5036e8e631f726ad | docs/data/mapped_ingredients.csv; CSV lines=[1558] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"CHEBI:34887","preferred_term":"NiCl2 x 2 H2O","total_occurrences":"21"}] |
| ev-1fca7f0b218f9c90 | reports/yaml_record_review/20261001T050301Z-Nicl2_X_2_H2o.md; YAML Record Review: NiCl2 x 2 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a5d10b3440eae0c4 | reports/yaml_record_review/Nicl2_X_2_H2o.md; &#96;data/ingredients/mapped/Nicl2_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:29; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-69f1a3f52c7db430 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1054,2094] | context_only | [{"current_record_sha256":"63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a","finding_id":"SEM:02e6181420c944985f86","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a","finding_id":"SEM:49ccab231b08d59dbaf1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d21a17cd9613f0ac | data/ingredients/mapped/Nicl2_X_2_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1556],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_status":"MAPPED","ontology_id":"CHEBI:34887","preferred_term":"NiCl2 x 2 H2O"}],"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":21},"occurrence_statistics":{"media_count":20,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34887","ontology_label":"nickel dichloride","ontology_source":"CHEBI"},"preferred_term":"NiCl2 x 2 H2O","sssom_rows":[{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel dichloride","predicate_id":"skos:closeMatch"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2 x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nicl2_X_2_H2o","synonym_count":18} |
| ev-9bfed7a1aed2134c | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-a55340403d52f750] | context_only | Predecessor structured review finding f-a55340403d52f750 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nicl2-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nicl2_X_2_H2o (data/ingredients/mapped/Nicl2_X_2_H2o.yaml)'
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
summary: Per-record structured review for Nicl2_X_2_H2o (data/ingredients/mapped/Nicl2_X_2_H2o.yaml,
  record-5f2d78dbe06a0f9d, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
    sha256: 63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a
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
  - path: reports/yaml_record_review/20261001T050301Z-Nicl2_X_2_H2o.md
    sha256: 9ef75cac1d63b2b2a14ebe2509ee635950b05d676985e19bc225fe7f324ece74
    role: context
  - path: reports/yaml_record_review/Nicl2_X_2_H2o.md
    sha256: 52ff69cdda5c11b880236d1056afd693d79b0a13320929d950fbd102be24e292
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5f2d78dbe06a0f9d
  path: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
  label: Nicl2_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nicl2_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nicl2_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5f2d78dbe06a0f9d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-7b4eed946bdc587b
  - ev-435536912b4bfafc
  - ev-63cccdf04618bf60
  - ev-5036e8e631f726ad
  - ev-d21a17cd9613f0ac
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-7b4eed946bdc587b
  - ev-69f1a3f52c7db430
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-1fca7f0b218f9c90
  - ev-a5d10b3440eae0c4
  - ev-69f1a3f52c7db430
  - ev-9bfed7a1aed2134c
evidence:
- evidence_id: ev-7b4eed946bdc587b
  kind: record_content
  reference: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1556],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_status":"MAPPED","ontology_id":"CHEBI:34887","preferred_term":"NiCl2
    x 2 H2O"}],"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":21},"occurrence_statistics":{"media_count":20,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34887","ontology_label":"nickel
    dichloride","ontology_source":"CHEBI"},"preferred_term":"NiCl2 x 2 H2O","sssom_rows":[{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2
    x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nicl2_X_2_H2o","synonym_count":18}'
  snapshot_sha256: 63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a
- evidence_id: ev-435536912b4bfafc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1556]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-63cccdf04618bf60
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nicl2_X_2_H2o; data-row positions=[2083, 2084]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel
    dichloride","other":"NiCl2 x 2H2O|NiCl2\u00b72H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Nicl2_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2
    x 2 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Nicl2_X_2_H2o","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5036e8e631f726ad
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1558]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"CHEBI:34887","preferred_term":"NiCl2
    x 2 H2O","total_occurrences":"21"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1fca7f0b218f9c90
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050301Z-Nicl2_X_2_H2o.md
  locator: 'YAML Record Review: NiCl2 x 2 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9ef75cac1d63b2b2a14ebe2509ee635950b05d676985e19bc225fe7f324ece74
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Nicl2_X_2_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    dihydrate identity has final rows, but stale anhydrous structure, parent synonyms,
    and a provisional TRACE_ELEMENT role remain.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Nicl2_X_2_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Nicl2_X_2_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Nicl2_X_2_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-a5d10b3440eae0c4
  kind: prior_review
  reference: reports/yaml_record_review/Nicl2_X_2_H2o.md
  locator: '`data/ingredients/mapped/Nicl2_X_2_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:29; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 52ff69cdda5c11b880236d1056afd693d79b0a13320929d950fbd102be24e292
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nicl2_X_2_H2o.yaml`,\
    \ either replace the\n  stale anhydrous InChI/SMILES with dihydrate-specific structure\
    \ evidence or\n  clear them until that evidence exists.\n- Major: reject or demote\
    \ `nickel(2+) chloride` and `nickel(II) chloride` on\n  the local dihydrate record,\
    \ then rebuild final SSSOM so the close-match row\n  does not publish anhydrous\
    \ parent synonyms.\n- Major: replace the provisional `TRACE_ELEMENT` role with\
    \ inspected\n  claim-level evidence or remove it."
- evidence_id: ev-69f1a3f52c7db430
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1054,2094]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a","finding_id":"SEM:02e6181420c944985f86","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a","finding_id":"SEM:49ccab231b08d59dbaf1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d21a17cd9613f0ac
  kind: record_content
  reference: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1556],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","line":1558,"mapping_status":"MAPPED","ontology_id":"CHEBI:34887","preferred_term":"NiCl2
    x 2 H2O"}],"identifier":"kgmicrobe.compound:nicl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":21},"occurrence_statistics":{"media_count":20,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34887","ontology_label":"nickel
    dichloride","ontology_source":"CHEBI"},"preferred_term":"NiCl2 x 2 H2O","sssom_rows":[{"data_row":2083,"object_id":"CHEBI:34887","object_label":"nickel
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":2084,"object_id":"kgmicrobe.compound:nicl2_x_2_h2o","object_label":"NiCl2
    x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nicl2_X_2_H2o","synonym_count":18}'
  snapshot_sha256: 63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a
- evidence_id: ev-9bfed7a1aed2134c
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-a55340403d52f750]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a55340403d52f750 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-62e746dc12c836f5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-7b4eed946bdc587b
  - ev-435536912b4bfafc
  - ev-63cccdf04618bf60
  - ev-5036e8e631f726ad
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d1ad1dc4d1b448f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-1fca7f0b218f9c90
  - ev-a5d10b3440eae0c4
  - ev-7b4eed946bdc587b
  - ev-69f1a3f52c7db430
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:01Z;
    reviewed SHA-256=ab4f6d9e5c9b4b7bf7151b6541d357f074ac6b4876cc61fd8be82cf7c85b46dd;
    current SHA-256=63b0fccca5b4c6331435b5ca6f1c6b30710447cb8a4118b97cec1cc2f2e1b85a;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050301Z-Nicl2_X_2_H2o.md","reports/yaml_record_review/Nicl2_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Nicl2_X_2_H2o.md` after the record changed from 6b43693a206b10af5013fa73afea10360d69666ed0a90dcb0f00618bdff297dc
    to ab4f6d9e5c9b4b7bf7151b6541d357f074ac6b4876cc61fd8be82cf7c85b46dd; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1fca7f0b218f9c90
    - ev-a5d10b3440eae0c4
    - ev-7b4eed946bdc587b
  - name: legacy-native-ids
    value: '["SEM:02e6181420c944985f86","SEM:49ccab231b08d59dbaf1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7b4eed946bdc587b
    - ev-1fca7f0b218f9c90
    - ev-a5d10b3440eae0c4
    - ev-69f1a3f52c7db430
- assessment_id: a-d21a17cd9613f0ac
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-1fca7f0b218f9c90
  - ev-a5d10b3440eae0c4
  - ev-d21a17cd9613f0ac
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1fca7f0b218f9c90
    - ev-a5d10b3440eae0c4
    - ev-d21a17cd9613f0ac
findings:
- finding_id: rec-f-a55340403d52f750
  issue_key: mim-reconciliation-role-support-5f2d78dbe06a0f9d
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: NiCl2 x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f2d78dbe06a0f9d
  evidence_ids:
  - ev-1fca7f0b218f9c90
  - ev-a5d10b3440eae0c4
  - ev-d21a17cd9613f0ac
  - ev-9bfed7a1aed2134c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-a55340403d52f750
actions:
- action_id: rec-action-a55340403d52f750
  description: 'Reassess prediction-only role support: NiCl2 x 2 H2O'
  finding_ids:
  - rec-f-a55340403d52f750
  target_ids:
  - record-5f2d78dbe06a0f9d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nicl2_X_2_H2o.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
