# Per-record structured review: D-malate (data/ingredients/mapped/D-malate.yaml)

- Review: 20261017T083000Z-d-malate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-malate (data/ingredients/mapped/D-malate.yaml, record-06029f98367f72eb, mapping_status=MAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-malate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-malate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-06029f98367f72eb | data/ingredients/mapped/D-malate.yaml | maintained | D-malate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-06029f98367f72eb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-06029f98367f72eb | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-06029f98367f72eb | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-06029f98367f72eb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-06029f98367f72eb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:49:05Z; reviewed SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494; current SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494; hash_changed=False. Reports=["reports/yaml_record_review/D-malate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI dianion identity, BacDive source-occurrence count, 0/0 CultureMech count, and empty final SSSOM payload pass, but the top-level import note is stale.

### Legacy field-missing triage rows

provenance: unknown. Targets: record-06029f98367f72eb.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Findings

### rec-f-5e947d99d3b9d00b: Historical review coverage and residual narrative: D-malate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-06029f98367f72eb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:49:05Z; reviewed SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494; current SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494; hash_changed=False. Reports=["reports/yaml_record_review/D-malate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI dianion identity, BacDive source-occurrence count, 0/0 CultureMech count, and empty final SSSOM payload pass, but the top-level import note is stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

### rec-f-ab41fb124143d484: Legacy field-missing triage rows: D-malate

minor / deferred / provisional; issue key: mim-reconciliation-legacy-field-missing-triage-rows-06029f98367f72eb.

The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

Disposition: The field-missing premise is stale for the named fields, but whether this historical TSV should be refreshed as a live queue is a separate ownership/policy question. No blanket issue closure is justified.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-54bbacc1e8a7d807 | data/ingredients/mapped/D-malate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[221],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15588","line":223,"mapping_status":"MAPPED","ontology_id":"CHEBI:15588","preferred_term":"D-malate"}],"identifier":"CHEBI:15588","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":33,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:15588","ontology_label":"(R)-malate(2-)","ontology_source":"CHEBI"},"preferred_term":"D-malate","sssom_rows":[{"data_row":946,"object_id":"CHEBI:15588","object_label":"(R)-malate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-malate","synonym_count":1} |
| ev-14a0968b175acf33 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [221] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c079dcc13ff76c6b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-malate; data-row positions=[946] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":946,"object_id":"CHEBI:15588","object_label":"(R)-malate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:D-malate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-3a6f7d2156b3a40e | docs/data/mapped_ingredients.csv; CSV lines=[223] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15588","line":223,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15588","preferred_term":"D-malate","total_occurrences":"0"}] |
| ev-35c3c30ff88e0371 | reports/yaml_record_review/D-malate.md; &#96;data/ingredients/mapped/D-malate.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:39; Completeness:55; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d05727040817f65e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[502] | context_only | [{"current_record_sha256":"77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494","finding_id":"SEM:ba656ba95907cb5eb18a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-214bdf6bc6ae2e8b | mappings/record_research_validation.tsv; lines=[860] | partial | FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"'chemical_properties' is unset; report supplies a value","documented_rationale":"yes","evidence":"formula &#96;C4H4O5&#96;; charge &#96;-2&#96;; average mass &#96;132.071&#96;; monoisotopic &#96;132.00697&#96;; SMILES &#96;O=C([O-])C[C@@H](O)C(=O)[O-]&#96;; InChIKey &#96;BJEPYKJPYRNKOW-UWTATZPHSA-L&#96;; **no CAS-RN** (see \u00a73)","identifier":"CHEBI:15588","kind":"FIELD_MISSING","lane":"claude","line":860,"mapping_quality":"SYNONYM_MATCH","preferred_term":"D-malate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:15588","slug":"D-malate","status_dir":"mapped"}}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-malate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-malate (data/ingredients/mapped/D-malate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=2
scientific_review: false
summary: Per-record structured review for D-malate (data/ingredients/mapped/D-malate.yaml,
  record-06029f98367f72eb, mapping_status=MAPPED). Records 0 open finding(s) and 2
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-malate.yaml
    sha256: 77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494
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
  - path: reports/yaml_record_review/D-malate.md
    sha256: cc33c0fb334fe50434ed95e469170aecc26df235be7e25f9ace21fdd0f5815ab
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: mappings/record_research_validation.tsv
    sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
    role: context
targets:
- target_id: record-06029f98367f72eb
  path: data/ingredients/mapped/D-malate.yaml
  label: D-malate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-malate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-malate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-malate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-06029f98367f72eb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-06029f98367f72eb
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-06029f98367f72eb
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-06029f98367f72eb
evidence:
- evidence_id: ev-54bbacc1e8a7d807
  kind: record_content
  reference: data/ingredients/mapped/D-malate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[221],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15588","line":223,"mapping_status":"MAPPED","ontology_id":"CHEBI:15588","preferred_term":"D-malate"}],"identifier":"CHEBI:15588","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":33,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:15588","ontology_label":"(R)-malate(2-)","ontology_source":"CHEBI"},"preferred_term":"D-malate","sssom_rows":[{"data_row":946,"object_id":"CHEBI:15588","object_label":"(R)-malate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-malate","synonym_count":1}'
  snapshot_sha256: 77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494
- evidence_id: ev-14a0968b175acf33
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [221]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c079dcc13ff76c6b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-malate; data-row positions=[946]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":946,"object_id":"CHEBI:15588","object_label":"(R)-malate(2-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:D-malate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3a6f7d2156b3a40e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[223]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15588","line":223,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15588","preferred_term":"D-malate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-35c3c30ff88e0371
  kind: prior_review
  reference: reports/yaml_record_review/D-malate.md
  locator: '`data/ingredients/mapped/D-malate.yaml`:2; Verdict:4; Identity:10; Validation:21;
    Evidence:39; Completeness:55; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cc33c0fb334fe50434ed95e469170aecc26df235be7e25f9ace21fdd0f5815ab
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-malate.yaml`, remove\
    \ or refresh the stale\n  top-level `notes` field.\n- Regenerate synchronized\
    \ curated products afterward, then rerun\n  `uv run --frozen python scripts/validate_strict.py`\
    \ and\n  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-malate.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`."
- evidence_id: ev-d05727040817f65e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[502]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494","finding_id":"SEM:ba656ba95907cb5eb18a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-214bdf6bc6ae2e8b
  kind: record_content
  reference: mappings/record_research_validation.tsv
  locator: lines=[860]
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: 'FIELD_MISSING entries conflict with populated current fields: [{"field":"chemical_properties","row":{"detail":"''chemical_properties''
    is unset; report supplies a value","documented_rationale":"yes","evidence":"formula
    `C4H4O5`; charge `-2`; average mass `132.071`; monoisotopic `132.00697`; SMILES
    `O=C([O-])C[C@@H](O)C(=O)[O-]`; InChIKey `BJEPYKJPYRNKOW-UWTATZPHSA-L`; **no CAS-RN**
    (see \u00a73)","identifier":"CHEBI:15588","kind":"FIELD_MISSING","lane":"claude","line":860,"mapping_quality":"SYNONYM_MATCH","preferred_term":"D-malate","priority":"P3","promoted_by":"promote_resolved_unmapped","recorded":"CHEBI:15588","slug":"D-malate","status_dir":"mapped"}}]'
  snapshot_sha256: 7e1b339c20eb07c163d4bacf36fe4f45b6e2132b83359932683ad6dddf467799
assessments:
- assessment_id: a-197597d327c7a28e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-06029f98367f72eb
  evidence_ids:
  - ev-54bbacc1e8a7d807
  - ev-14a0968b175acf33
  - ev-c079dcc13ff76c6b
  - ev-3a6f7d2156b3a40e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1f48802c9c4dc9ca
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-06029f98367f72eb
  evidence_ids:
  - ev-35c3c30ff88e0371
  - ev-54bbacc1e8a7d807
  - ev-d05727040817f65e
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:49:05Z;
    reviewed SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494;
    current SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494;
    hash_changed=False. Reports=["reports/yaml_record_review/D-malate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI
    dianion identity, BacDive source-occurrence count, 0/0 CultureMech count, and
    empty final SSSOM payload pass, but the top-level import note is stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-35c3c30ff88e0371
    - ev-54bbacc1e8a7d807
  - name: legacy-native-ids
    value: '["SEM:ba656ba95907cb5eb18a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-54bbacc1e8a7d807
    - ev-35c3c30ff88e0371
    - ev-d05727040817f65e
- assessment_id: a-214bdf6bc6ae2e8b
  area: provenance
  topic: Legacy field-missing triage rows
  outcome: unknown
  summary: The field-missing premise is stale for the named fields, but whether this
    historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  target_ids:
  - record-06029f98367f72eb
  evidence_ids:
  - ev-35c3c30ff88e0371
  - ev-54bbacc1e8a7d807
  - ev-214bdf6bc6ae2e8b
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-35c3c30ff88e0371
    - ev-54bbacc1e8a7d807
    - ev-214bdf6bc6ae2e8b
findings:
- finding_id: rec-f-5e947d99d3b9d00b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-06029f98367f72eb
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: D-malate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:49:05Z;
    reviewed SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494;
    current SHA-256=77dfba0badfef73f21ea7cd9af6714afd42befba1298e0e33991c38c4fc46494;
    hash_changed=False. Reports=["reports/yaml_record_review/D-malate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI
    dianion identity, BacDive source-occurrence count, 0/0 CultureMech count, and
    empty final SSSOM payload pass, but the top-level import note is stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-06029f98367f72eb
  evidence_ids:
  - ev-35c3c30ff88e0371
  - ev-54bbacc1e8a7d807
  - ev-d05727040817f65e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-malate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-ab41fb124143d484
  issue_key: mim-reconciliation-legacy-field-missing-triage-rows-06029f98367f72eb
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Legacy field-missing triage rows: D-malate'
  description: The field-missing premise is stale for the named fields, but whether
    this historical TSV should be refreshed as a live queue is a separate ownership/policy
    question. No blanket issue closure is justified.
  disposition_reason: The field-missing premise is stale for the named fields, but
    whether this historical TSV should be refreshed as a live queue is a separate
    ownership/policy question. No blanket issue closure is justified.
  target_ids:
  - record-06029f98367f72eb
  evidence_ids:
  - ev-35c3c30ff88e0371
  - ev-54bbacc1e8a7d807
  - ev-214bdf6bc6ae2e8b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-malate.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - legacy-field-missing-triage-rows
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
