# Per-record structured review: 4-vinylphenol (data/ingredients/mapped/4-vinylphenol.yaml)

- Review: 20261017T083000Z-4-vinylphenol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 4-vinylphenol (data/ingredients/mapped/4-vinylphenol.yaml, record-88ed3645c26c14b6, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/4-vinylphenol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/4-vinylphenol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-88ed3645c26c14b6 | data/ingredients/mapped/4-vinylphenol.yaml | maintained | 4-vinylphenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-88ed3645c26c14b6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-88ed3645c26c14b6 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-88ed3645c26c14b6 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-88ed3645c26c14b6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-88ed3645c26c14b6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:33:07Z; reviewed SHA-256=8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9; current SHA-256=8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9; hash_changed=False. Reports=["reports/yaml_record_review/4-vinylphenol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI 4-hydroxystyrene identity passes, but two trace-minerals source labels are stored and exported as exact synonyms of the chemical.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-88ed3645c26c14b6.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace minerals (see Medium No.151"},{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace minerals(see Medium No.151)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-88ed3645c26c14b6.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

## Findings

### rec-scope-f-be91e29ea6694d28: Adjudicate source scope of exported tokens: 4-vinylphenol

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-88ed3645c26c14b6.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report separately alleges trace-mineral/4-vinylphenol identity conflation. That stronger claim remains in the original report and narrative reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a30c5b4d27c54326 | data/ingredients/mapped/4-vinylphenol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[397],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:1883","line":399,"mapping_status":"MAPPED","ontology_id":"CHEBI:1883","preferred_term":"4-vinylphenol"}],"identifier":"CHEBI:1883","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:1883","ontology_label":"4-hydroxystyrene","ontology_source":"CHEBI"},"preferred_term":"4-vinylphenol","sssom_rows":[{"data_row":215,"object_id":"CHEBI:1883","object_label":"4-hydroxystyrene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-vinylphenol","synonym_count":3} |
| ev-ae558191b7650ff8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [397] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5411f74c8ccead5d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-vinylphenol; data-row positions=[215] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":215,"object_id":"CHEBI:1883","object_label":"4-hydroxystyrene","other":"4-ethenylphenol&#124;Trace minerals (see Medium No.151&#124;Trace minerals(see Medium No.151)&#124;CAS:2628-17-3","predicate_id":"skos:exactMatch","subject_id":"MIM:4-vinylphenol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-738dce96d98f0b27 | docs/data/mapped_ingredients.csv; CSV lines=[399] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:1883","line":399,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:1883","preferred_term":"4-vinylphenol","total_occurrences":"0"}] |
| ev-bd1a1d6f224cb9f2 | reports/yaml_record_review/4-vinylphenol.md; &#96;data/ingredients/mapped/4-vinylphenol.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:31; Completeness:49; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-44de6ad13aadec37 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[160] | context_only | [{"current_record_sha256":"8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9","finding_id":"SEM:902a8fd6eafd76c8cdf5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-f983f8801d1e4699 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-be91e29ea6694d28] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-d8b130cb30e86aec | data/ingredients/mapped/4-vinylphenol.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "sssom_other_backfill", "synonym_text": "Trace minerals (see Medium No.151", "synonym_type": "RAW_TEXT"}, {"source": "sssom_other_backfill", "synonym_text": "Trace minerals(see Medium No.151)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_FROM_CAS_LOOKUP", "changes": "Created from CultureBotHT CAS-RN=2628-17-3; CHEBI resolved via OAK CHEBI sqlite (cas xref); Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref). ", "curator": "audit_cas_chebi_followup", "llm_assisted": false, "new_status": "MAPPED", "timestamp": "2026-04-29T06:34:31.158938+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:31.933265+00:00"}, {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C8H8O; inchi=InChI=1S/C8H8O/c1-2-7-3-5-8(9)6-4-7/h2-6,9H,1H2; smiles=C=Cc1ccc(O)cc1", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T08:08:27.759520+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:12.131604+00:00"}, {"action": "REGRADED_EXACT_TO_SYNONYM", "changes": "mapping_quality EXACT_MATCH -&gt; SYNONYM_MATCH (#317). The record's label does not equal the term's primary label '4-hydroxystyrene'; it matches the ChEBI synonym '4-vinylphenol' on CHEBI:1883. The schema defines EXACT_MATCH as a direct match to the term and SYNONYM_MATCH as a match to a known synonym, so the recorded grade overstated. ontology_id is unchanged \u2014 the term is correct. The SSSOM predicate is unaffected (both grades emit skos:exactMatch).", "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-10T00:00:00+00:00"}, {"action": "REGRADED_TO_CAS_RN_LOOKUP", "changes": "mapping_quality SYNONYM_MATCH -&gt; CAS_RN_LOOKUP (#317). The record was created by an explicit CAS-to-ChEBI lookup and its current CAS RN 2628-17-3 uniquely resolves by ChEBI xref to CHEBI:1883 '4-hydroxystyrene'. CAS_RN_LOOKUP records the method that established this mapping; a lexical grade would discard that provenance. ontology_id is unchanged. The own-identifier SSSOM predicate remains skos:exactMatch under Rule D (#438), independently of mapping quality.", "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-24T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Recovered 1 surface form(s) that the published SSSOM &#96;other&#96; carried but no curated record did, so a rebuild would have dropped them from KGX: 'Trace minerals (see Medium No.151'. Tokens already present on the kg-microbe ontology node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted": false, "timestamp": "2026-09-02T17:40:44.716277+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Recovered 1 surface form(s) that the published SSSOM &#96;other&#96; carried but no curated record did, so a rebuild would have dropped them from KGX: 'Trace minerals(see Medium No.151)'. Tokens already present on the kg-microbe ontology node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted": false, "timestamp": "2026-09-02T22:41:49.137449+00:00"}], "identifier": "CHEBI:1883", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref). ", "source": "CultureBotHT"}], "mapping_quality": "CAS_RN_LOOKUP", "ontology_id": "CHEBI:1883", "ontology_label": "4-hydroxystyrene", "ontology_source": "CHEBI"}} |
| ev-0de8553689e72bef | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-vinylphenol | supports | [{"comment": "", "confidence": "0.9", "data_row": 215, "mapping_date": "2026-09-02", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "CHEBI:1883", "object_label": "4-hydroxystyrene", "object_source": "obo:chebi.owl", "other": "4-ethenylphenol&#124;Trace minerals (see Medium No.151&#124;Trace minerals(see Medium No.151)&#124;CAS:2628-17-3", "predicate_id": "skos:exactMatch", "source": "MIM:CultureBotHT&#124;MIM:curator=claude_sssom_surface_form_backfill&#124;kgm:chebi_xrefs&#124;kgm:mediadive_compounds&#124;kgm:mediaingredientmech_reviewed&#124;kgm:mediaingredientmech_reviewed[curator=audit_cas_chebi_followup]&#124;kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]&#124;kgm:mediaingredientmech_reviewed[curator=regrade_synonym_matches]&#124;kgm:primary_mappings[kegg_compound]", "subject_id": "MIM:4-vinylphenol", "subject_label": "4-vinylphenol", "validation_method": "OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-93f74be01346ddd4 | reports/yaml_record_review/4-vinylphenol.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-2d38e4eca6353261 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-be91e29ea6694d28] | context_only | Predecessor structured review finding scope-f-be91e29ea6694d28 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-4-vinylphenol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 4-vinylphenol (data/ingredients/mapped/4-vinylphenol.yaml)'
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
summary: Per-record structured review for 4-vinylphenol (data/ingredients/mapped/4-vinylphenol.yaml,
  record-88ed3645c26c14b6, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/4-vinylphenol.yaml
    sha256: 8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
    role: context
  - path: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
    sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
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
  - path: reports/yaml_record_review/4-vinylphenol.md
    sha256: 2214bfc494f21e540ca4c95362b07f22597d870efc1ef0937d619d09bb58e1b8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-88ed3645c26c14b6
  path: data/ingredients/mapped/4-vinylphenol.yaml
  label: 4-vinylphenol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-vinylphenol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/4-vinylphenol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/4-vinylphenol.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-88ed3645c26c14b6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-88ed3645c26c14b6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-88ed3645c26c14b6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-88ed3645c26c14b6
evidence:
- evidence_id: ev-a30c5b4d27c54326
  kind: record_content
  reference: data/ingredients/mapped/4-vinylphenol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[397],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:1883","line":399,"mapping_status":"MAPPED","ontology_id":"CHEBI:1883","preferred_term":"4-vinylphenol"}],"identifier":"CHEBI:1883","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:1883","ontology_label":"4-hydroxystyrene","ontology_source":"CHEBI"},"preferred_term":"4-vinylphenol","sssom_rows":[{"data_row":215,"object_id":"CHEBI:1883","object_label":"4-hydroxystyrene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-vinylphenol","synonym_count":3}'
  snapshot_sha256: 8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9
- evidence_id: ev-ae558191b7650ff8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [397]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5411f74c8ccead5d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-vinylphenol; data-row positions=[215]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":215,"object_id":"CHEBI:1883","object_label":"4-hydroxystyrene","other":"4-ethenylphenol|Trace
    minerals (see Medium No.151|Trace minerals(see Medium No.151)|CAS:2628-17-3","predicate_id":"skos:exactMatch","subject_id":"MIM:4-vinylphenol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-738dce96d98f0b27
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[399]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:1883","line":399,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:1883","preferred_term":"4-vinylphenol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bd1a1d6f224cb9f2
  kind: prior_review
  reference: reports/yaml_record_review/4-vinylphenol.md
  locator: '`data/ingredients/mapped/4-vinylphenol.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:31; Completeness:49; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2214bfc494f21e540ca4c95362b07f22597d870efc1ef0937d619d09bb58e1b8
  quote: "Recommended Edits:\n1. Remove or reject the two `Trace minerals...` `RAW_TEXT`\
    \ synonyms in\n   `data/ingredients/mapped/4-vinylphenol.yaml` and\n   `data/curated/mapped_ingredients.yaml`,\
    \ then regenerate SSSOM and docs so\n   those medium-note fragments no longer\
    \ publish as exact synonym labels."
- evidence_id: ev-44de6ad13aadec37
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[160]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9","finding_id":"SEM:902a8fd6eafd76c8cdf5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-823412d1eacb6795
  kind: record_content
  reference: MAPPING_SEMANTICS.md
  locator: Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: Raw spellings may remain resolvable when they denote the same substance.
    Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not
    adjudicate that distinction.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: ev-f983f8801d1e4699
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-be91e29ea6694d28]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace minerals (see
    Medium No.151\"},{\"reason\":\"unresolved recipe cross-reference in a resolving
    synonym\",\"token\":\"Trace minerals(see Medium No.151)\"}]. Truncated concentration
    strings and context-dependent instructions need scoped curation. This check does
    not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids": ["ev-bd1a1d6f224cb9f2",
    "ev-5411f74c8ccead5d"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-be91e29ea6694d28",
    "issue_key": "mim-reconciliation-exported-context-tokens-88ed3645c26c14b6", "owner_paths":
    [{"path": "data/ingredients/mapped/4-vinylphenol.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-88ed3645c26c14b6"], "title": "Review nonportable exported tokens: 4-vinylphenol"}'
- evidence_id: ev-d8b130cb30e86aec
  kind: record_content
  reference: data/ingredients/mapped/4-vinylphenol.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "sssom_other_backfill", "synonym_text":
    "Trace minerals (see Medium No.151", "synonym_type": "RAW_TEXT"}, {"source": "sssom_other_backfill",
    "synonym_text": "Trace minerals(see Medium No.151)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_FROM_CAS_LOOKUP", "changes": "Created from CultureBotHT
    CAS-RN=2628-17-3; CHEBI resolved via OAK CHEBI sqlite (cas xref); Imported from
    CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI sqlite (cas xref).
    ", "curator": "audit_cas_chebi_followup", "llm_assisted": false, "new_status":
    "MAPPED", "timestamp": "2026-04-29T06:34:31.158938+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (CHEBI primary)", "curator":
    "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-01T07:35:31.933265+00:00"},
    {"action": "AUTO_BACKFILL_CHEBI_CHEMISTRY", "changes": "molecular_formula=C8H8O;
    inchi=InChI=1S/C8H8O/c1-2-7-3-5-8(9)6-4-7/h2-6,9H,1H2; smiles=C=Cc1ccc(O)cc1",
    "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp":
    "2026-05-01T08:08:27.759520+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=SINGLE_INGREDIENT (chemical structure populated
    (molecular_formula))", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:12.131604+00:00"}, {"action": "REGRADED_EXACT_TO_SYNONYM",
    "changes": "mapping_quality EXACT_MATCH -> SYNONYM_MATCH (#317). The record''s
    label does not equal the term''s primary label ''4-hydroxystyrene''; it matches
    the ChEBI synonym ''4-vinylphenol'' on CHEBI:1883. The schema defines EXACT_MATCH
    as a direct match to the term and SYNONYM_MATCH as a match to a known synonym,
    so the recorded grade overstated. ontology_id is unchanged \u2014 the term is
    correct. The SSSOM predicate is unaffected (both grades emit skos:exactMatch).",
    "curator": "regrade_synonym_matches", "llm_assisted": false, "timestamp": "2026-08-10T00:00:00+00:00"},
    {"action": "REGRADED_TO_CAS_RN_LOOKUP", "changes": "mapping_quality SYNONYM_MATCH
    -> CAS_RN_LOOKUP (#317). The record was created by an explicit CAS-to-ChEBI lookup
    and its current CAS RN 2628-17-3 uniquely resolves by ChEBI xref to CHEBI:1883
    ''4-hydroxystyrene''. CAS_RN_LOOKUP records the method that established this mapping;
    a lexical grade would discard that provenance. ontology_id is unchanged. The own-identifier
    SSSOM predicate remains skos:exactMatch under Rule D (#438), independently of
    mapping quality.", "curator": "regrade_synonym_matches", "llm_assisted": false,
    "timestamp": "2026-08-24T00:00:00+00:00"}, {"action": "ADDED_SYNONYMS", "changes":
    "Recovered 1 surface form(s) that the published SSSOM `other` carried but no curated
    record did, so a rebuild would have dropped them from KGX: ''Trace minerals (see
    Medium No.151''. Tokens already present on the kg-microbe ontology node were left
    out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill", "llm_assisted":
    false, "timestamp": "2026-09-02T17:40:44.716277+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Recovered 1 surface form(s) that the published SSSOM `other` carried
    but no curated record did, so a rebuild would have dropped them from KGX: ''Trace
    minerals(see Medium No.151)''. Tokens already present on the kg-microbe ontology
    node were left out as redundant (#520).", "curator": "claude_sssom_surface_form_backfill",
    "llm_assisted": false, "timestamp": "2026-09-02T22:41:49.137449+00:00"}], "identifier":
    "CHEBI:1883", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes":
    "Imported from CultureBotHT. CAS-RN\u2192CHEBI mapping resolved via OAK CHEBI
    sqlite (cas xref). ", "source": "CultureBotHT"}], "mapping_quality": "CAS_RN_LOOKUP",
    "ontology_id": "CHEBI:1883", "ontology_label": "4-hydroxystyrene", "ontology_source":
    "CHEBI"}}'
  snapshot_sha256: 8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9
- evidence_id: ev-0de8553689e72bef
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-vinylphenol
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 215, "mapping_date":
    "2026-09-02", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "CHEBI:1883", "object_label": "4-hydroxystyrene", "object_source": "obo:chebi.owl",
    "other": "4-ethenylphenol|Trace minerals (see Medium No.151|Trace minerals(see
    Medium No.151)|CAS:2628-17-3", "predicate_id": "skos:exactMatch", "source": "MIM:CultureBotHT|MIM:curator=claude_sssom_surface_form_backfill|kgm:chebi_xrefs|kgm:mediadive_compounds|kgm:mediaingredientmech_reviewed|kgm:mediaingredientmech_reviewed[curator=audit_cas_chebi_followup]|kgm:mediaingredientmech_reviewed[curator=auto_classify_ingredient_type]|kgm:mediaingredientmech_reviewed[curator=regrade_synonym_matches]|kgm:primary_mappings[kegg_compound]",
    "subject_id": "MIM:4-vinylphenol", "subject_label": "4-vinylphenol", "validation_method":
    "OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-93f74be01346ddd4
  kind: prior_review
  reference: reports/yaml_record_review/4-vinylphenol.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 2214bfc494f21e540ca4c95362b07f22597d870efc1ef0937d619d09bb58e1b8
  quote: "# `data/ingredients/mapped/4-vinylphenol.yaml`\n\n## Verdict\n\nNeeds curation,\
    \ major. The CAS-backed `CHEBI:1883` 4-hydroxystyrene identity,\nCAS, chemistry,\
    \ and SSSOM exact-match row pass, but two trace-minerals source\nlabels are stored\
    \ and exported as exact synonyms of the chemical.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/4-vinylphenol.yaml`.\n- Identifier and grounding:\
    \ `identifier: CHEBI:1883` with\n  `ontology_mapping.ontology_id: CHEBI:1883`,\
    \ source `CHEBI`,\n  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.\n\
    - Official OLS/ChEBI check: `CHEBI:1883` is active and resolves to\n  `4-hydroxystyrene`.\n\
    - The current ChEBI page reports CAS `2628-17-3`, formula `C8H8O`, the stored\n\
    \  SMILES, and the stored InChI for `CHEBI:1883`.\n- `ingredient_type: SINGLE_INGREDIENT`\
    \ is present.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py\
    \ data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml\
    \ data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml\
    \ data/ingredients/mapped/5-Azacytidine.yaml`:\n  passed; 5 files scanned, 0 ERROR\
    \ rows.\n- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-vinylphenol.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`:\n  passed.\n- `uv run --frozen python scripts/validate_component_partonomy.py`:\
    \ passed;\n  2951 records, 83 decompositions, 505 components, 0 violations.\n\n\
    ## Evidence\n\n- The active ChEBI term, CAS, formula, SMILES, InChI, and exact\
    \ synonym\n  `4-vinylphenol` support the CAS-based grounding to `CHEBI:1883`.\n\
    - The explicit CAS regrade is appropriate: the record was created through\n  CultureBotHT\
    \ CAS `2628-17-3` resolving by ChEBI xref to `CHEBI:1883`, so\n  `CAS_RN_LOOKUP`\
    \ preserves the mapping method better than a lexical grade.\n- The exact ChEBI\
    \ synonym `4-ethenylphenol` is acceptable.\n- Major: `Trace minerals (see Medium\
    \ No.151` and\n  `Trace minerals(see Medium No.151)` are media note fragments,\
    \ not names for\n  4-vinylphenol. They leak through the aggregate copy, SSSOM\
    \ `other`, generated\n  ingredient JSON, and generated `label_index` as synonyms\
    \ for `CHEBI:1883`.\n- The hidden/ignored-inclusive search over `data`, `mappings`,\
    \ `docs`,\n  `UNIFIED_INGREDIENT_MAPPING.tsv`, `src`, `scripts`, `tests`, `conf`,\n\
    \  `.github`, and `.claude` found the active YAML, aggregate copy, SSSOM row,\n\
    \  generated docs, row-review outputs, stale advisory rows, and ignored\n  aggregate\
    \ backups for this identifier and the bad trace-minerals strings.\n\n## Completeness\n\
    \n- CAS, formula, InChI, SMILES, `ingredient_type`, and the legitimate\n  `4-ethenylphenol`\
    \ exact synonym are populated.\n- No roles, components, environment, or discussion\
    \ entries need review.\n\n## Recommended Edits\n\n1. Remove or reject the two\
    \ `Trace minerals...` `RAW_TEXT` synonyms in\n   `data/ingredients/mapped/4-vinylphenol.yaml`\
    \ and\n   `data/curated/mapped_ingredients.yaml`, then regenerate SSSOM and docs\
    \ so\n   those medium-note fragments no longer publish as exact synonym labels.\n"
- evidence_id: ev-2d38e4eca6353261
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-be91e29ea6694d28]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-be91e29ea6694d28 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-df61165041c81d33
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-a30c5b4d27c54326
  - ev-ae558191b7650ff8
  - ev-5411f74c8ccead5d
  - ev-738dce96d98f0b27
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a3c6b47576350690
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-bd1a1d6f224cb9f2
  - ev-a30c5b4d27c54326
  - ev-44de6ad13aadec37
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:33:07Z;
    reviewed SHA-256=8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9;
    current SHA-256=8d4c406e24cbb343fb17cd6345b6628caf2e27ca07510c73c8ff2376a815c0f9;
    hash_changed=False. Reports=["reports/yaml_record_review/4-vinylphenol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-backed
    CHEBI 4-hydroxystyrene identity passes, but two trace-minerals source labels are
    stored and exported as exact synonyms of the chemical.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bd1a1d6f224cb9f2
    - ev-a30c5b4d27c54326
  - name: legacy-native-ids
    value: '["SEM:902a8fd6eafd76c8cdf5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a30c5b4d27c54326
    - ev-bd1a1d6f224cb9f2
    - ev-44de6ad13aadec37
- assessment_id: a-3d895cd2523d71bf
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Trace minerals (see Medium
    No.151"},{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace
    minerals(see Medium No.151)"}]. Truncated concentration strings and context-dependent
    instructions need scoped curation. This check does not reject catalog/RAW_TEXT
    synonyms as a class.'
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-bd1a1d6f224cb9f2
  - ev-5411f74c8ccead5d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bd1a1d6f224cb9f2
    - ev-5411f74c8ccead5d
- assessment_id: scope-f-be91e29ea6694d28
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. The historical
    report separately alleges trace-mineral/4-vinylphenol identity conflation. That
    stronger claim remains in the original report and narrative reassessment; the
    recipe-pointer heuristic neither adjudicates nor retires it.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-f983f8801d1e4699
  - ev-d8b130cb30e86aec
  - ev-0de8553689e72bef
  - ev-93f74be01346ddd4
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-f983f8801d1e4699
    - ev-d8b130cb30e86aec
    - ev-0de8553689e72bef
    - ev-93f74be01346ddd4
findings:
- finding_id: rec-scope-f-be91e29ea6694d28
  issue_key: mim-reconciliation-exported-context-tokens-88ed3645c26c14b6
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: 4-vinylphenol'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report separately alleges trace-mineral/4-vinylphenol
    identity conflation. That stronger claim remains in the original report and narrative
    reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.
  target_ids:
  - record-88ed3645c26c14b6
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-f983f8801d1e4699
  - ev-d8b130cb30e86aec
  - ev-0de8553689e72bef
  - ev-93f74be01346ddd4
  - ev-2d38e4eca6353261
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-vinylphenol.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report separately alleges trace-mineral/4-vinylphenol
    identity conflation. That stronger claim remains in the original report and narrative
    reassessment; the recipe-pointer heuristic neither adjudicates nor retires it.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T030852Z-mim-token-scope-reassessment
    finding_id: scope-f-be91e29ea6694d28
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02, 20261011T030852Z-mim-token-scope-reassessment.
```
