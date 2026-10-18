# Per-record structured review: Alk_So42 (data/ingredients/mapped/Alk_So42.yaml)

- Review: 20261017T083000Z-alk-so42
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alk_So42 (data/ingredients/mapped/Alk_So42.yaml, record-3a90e79f74a45533, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alk_So42.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alk_So42.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3a90e79f74a45533 | data/ingredients/mapped/Alk_So42.yaml | maintained | Alk_So42 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3a90e79f74a45533 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3a90e79f74a45533 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3a90e79f74a45533 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3a90e79f74a45533.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3a90e79f74a45533.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:39:28Z; reviewed SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed; current SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed; hash_changed=False. Reports=["reports/yaml_record_review/Alk_So42.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous potassium aluminium sulfate identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but unrelated sodium silicate and zinc sulfate fragments plus CultureMech metadata remain in synonyms.

## Findings

### rec-f-b64e3020582e47af: Historical review coverage and residual narrative: Alk_So42

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3a90e79f74a45533.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:39:28Z; reviewed SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed; current SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed; hash_changed=False. Reports=["reports/yaml_record_review/Alk_So42.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous potassium aluminium sulfate identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate pass, but unrelated sodium silicate and zinc sulfate fragments plus CultureMech metadata remain in synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8a0ddd8f8c130ed4 | data/ingredients/mapped/Alk_So42.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[468],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86463","line":470,"mapping_status":"MAPPED","ontology_id":"CHEBI:86463","preferred_term":"AlK(SO4)2"}],"identifier":"CHEBI:86463","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":240,"edge_count":240,"occurrences":240},"occurrence_statistics":{"media_count":240,"total_occurrences":240},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86463","ontology_label":"potassium aluminium sulfate","ontology_source":"CHEBI"},"preferred_term":"AlK(SO4)2","sssom_rows":[{"data_row":326,"object_id":"CHEBI:86463","object_label":"potassium aluminium sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alk_So42","synonym_count":17} |
| ev-924876d3390ddadb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [468] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c61ab53c4664a893 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alk_So42; data-row positions=[326] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":326,"object_id":"CHEBI:86463","object_label":"potassium aluminium sulfate","other":"Aluminum potassium sulfate&#124;potassium alum&#124;Aluminium potassium bis(sulphate)&#124;Aluminum potassium alum&#124;Aluminum potassium disulfate&#124;Burnt potassium alum&#124;Na SiO .9H O&#124;Potash alum&#124;Potassium aluminum alum&#124;ZnSO .7H O&#124;aluminium potassium sulfate (1/1/2)&#124;potassium aluminum disulfate&#124;KAl(SO4)2&#124;CAS:10043-67-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Alk_So42","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-58f23ebc67f5b675 | docs/data/mapped_ingredients.csv; CSV lines=[470] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86463","line":470,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"240","ontology_id":"CHEBI:86463","preferred_term":"AlK(SO4)2","total_occurrences":"240"}] |
| ev-a6cff1a02ef19e4f | reports/yaml_record_review/Alk_So42.md; &#96;data/ingredients/mapped/Alk_So42.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:47; Completeness:73; Recommended Edits:81 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f92acc4dd2e821b9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[231] | context_only | [{"current_record_sha256":"eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed","finding_id":"SEM:15761b556078b9a904a8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alk-so42
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alk_So42 (data/ingredients/mapped/Alk_So42.yaml)'
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
summary: Per-record structured review for Alk_So42 (data/ingredients/mapped/Alk_So42.yaml,
  record-3a90e79f74a45533, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alk_So42.yaml
    sha256: eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed
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
  - path: reports/yaml_record_review/Alk_So42.md
    sha256: 6e1d1f3dcd80a41a7c8e007e3e79e1c85c01201e97987df6c8e976bdf2ffa1fe
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3a90e79f74a45533
  path: data/ingredients/mapped/Alk_So42.yaml
  label: Alk_So42
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alk_So42.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alk_So42.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alk_So42.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3a90e79f74a45533
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3a90e79f74a45533
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3a90e79f74a45533
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3a90e79f74a45533
evidence:
- evidence_id: ev-8a0ddd8f8c130ed4
  kind: record_content
  reference: data/ingredients/mapped/Alk_So42.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[468],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86463","line":470,"mapping_status":"MAPPED","ontology_id":"CHEBI:86463","preferred_term":"AlK(SO4)2"}],"identifier":"CHEBI:86463","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":240,"edge_count":240,"occurrences":240},"occurrence_statistics":{"media_count":240,"total_occurrences":240},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86463","ontology_label":"potassium
    aluminium sulfate","ontology_source":"CHEBI"},"preferred_term":"AlK(SO4)2","sssom_rows":[{"data_row":326,"object_id":"CHEBI:86463","object_label":"potassium
    aluminium sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alk_So42","synonym_count":17}'
  snapshot_sha256: eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed
- evidence_id: ev-924876d3390ddadb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [468]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c61ab53c4664a893
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alk_So42; data-row positions=[326]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":326,"object_id":"CHEBI:86463","object_label":"potassium
    aluminium sulfate","other":"Aluminum potassium sulfate|potassium alum|Aluminium
    potassium bis(sulphate)|Aluminum potassium alum|Aluminum potassium disulfate|Burnt
    potassium alum|Na SiO .9H O|Potash alum|Potassium aluminum alum|ZnSO .7H O|aluminium
    potassium sulfate (1/1/2)|potassium aluminum disulfate|KAl(SO4)2|CAS:10043-67-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Alk_So42","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-58f23ebc67f5b675
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[470]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86463","line":470,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"240","ontology_id":"CHEBI:86463","preferred_term":"AlK(SO4)2","total_occurrences":"240"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a6cff1a02ef19e4f
  kind: prior_review
  reference: reports/yaml_record_review/Alk_So42.md
  locator: '`data/ingredients/mapped/Alk_So42.yaml`:2; Verdict:4; Identity:11; Validation:25;
    Evidence:47; Completeness:73; Recommended Edits:81'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6e1d1f3dcd80a41a7c8e007e3e79e1c85c01201e97987df6c8e976bdf2ffa1fe
  quote: "Recommended Edits:\n- Remove `Na SiO .9H O` and `ZnSO .7H O` from\n  `data/ingredients/mapped/Alk_So42.yaml`,\
    \ and correct\n  `mappings/ingredient_mappings_synonym_enrich_review.tsv` so the\
    \ row does not\n  claim those false aliases are represented.\n- Remove or move\
    \ the two CultureMech role/property raw synonyms from\n  `data/ingredients/mapped/Alk_So42.yaml`;\
    \ the curated\n  `nutritional_roles.TRACE_ELEMENT` entry already captures the\
    \ role.\n- Refresh the `TRACE_ELEMENT` evidence text from the current\n  `mappings/culturemech_recipe_membership.tsv`\
    \ count.\n- Regenerate synchronized products, then rerun\n  `uv run --frozen python\
    \ scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alk_So42.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-f92acc4dd2e821b9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[231]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed","finding_id":"SEM:15761b556078b9a904a8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b460975be7208001
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3a90e79f74a45533
  evidence_ids:
  - ev-8a0ddd8f8c130ed4
  - ev-924876d3390ddadb
  - ev-c61ab53c4664a893
  - ev-58f23ebc67f5b675
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ebc2e8aafd2f4dbe
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3a90e79f74a45533
  evidence_ids:
  - ev-a6cff1a02ef19e4f
  - ev-8a0ddd8f8c130ed4
  - ev-f92acc4dd2e821b9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:39:28Z;
    reviewed SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed;
    current SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Alk_So42.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous potassium
    aluminium sulfate identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate
    pass, but unrelated sodium silicate and zinc sulfate fragments plus CultureMech
    metadata remain in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a6cff1a02ef19e4f
    - ev-8a0ddd8f8c130ed4
  - name: legacy-native-ids
    value: '["SEM:15761b556078b9a904a8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8a0ddd8f8c130ed4
    - ev-a6cff1a02ef19e4f
    - ev-f92acc4dd2e821b9
findings:
- finding_id: rec-f-b64e3020582e47af
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3a90e79f74a45533
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Alk_So42'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:39:28Z;
    reviewed SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed;
    current SHA-256=eb7149b3301b2f405c59d0463b04bf6db774703bb3e914d125ffe9086ac717ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Alk_So42.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous potassium
    aluminium sulfate identity, CAS, chemistry, occurrence count, SSSOM row, and aggregate
    pass, but unrelated sodium silicate and zinc sulfate fragments plus CultureMech
    metadata remain in synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3a90e79f74a45533
  evidence_ids:
  - ev-a6cff1a02ef19e4f
  - ev-8a0ddd8f8c130ed4
  - ev-f92acc4dd2e821b9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alk_So42.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
