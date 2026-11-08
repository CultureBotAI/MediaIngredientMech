# Worker01 source applicability for Pipes

- Review: 20261108T041341Z-worker01-pipes-source-scope
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-08T04:12:53.301222Z
- Finished UTC: 2026-11-08T04:13:41.763072Z
- Reviewer: /root/issue_context (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Bounded source identity and preparation-qualifier review only. PIPES class relation is supported but exact supplied-form correspondence remains unresolved.

## Scope And Provenance

One existing candidate reviewed for its assigned frozen-source applicability; complete owner read, roles and publication eligibility excluded.

Selection: Concentration allocation case118
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58d67db32a86a359869819624568d625e7051358.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:39033 | data/ingredients/mapped/Pipes.yaml | maintained | PIPES |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native strict closed-schema check | passed | True | CHEBI:39033 | Two explicit maintained paths; exit0; no errors. |
| Primary source and ontology identity/form comparison | failed | True | CHEBI:39033 | Supplied reagent and recipe qualifier distinguished; ontology compared with current record. |
| Whole-record release and corpus export checks | not_applicable | False | CHEBI:39033 | No maintained data edits or publication support are issued by this bounded review. |

## Scientific And Domain Assessments

### Reagent versus prepared stock and final concentration

identity: concern. Targets: CHEBI:39033.

10mM is final PIPES concentration; broad PIPES class is known, but supplied neutral/salt form is not established.

## Findings

### PIPES-form-scope: Most-specific supplied PIPES form is not established by grouping-term identity

major / open / provisional; issue key: mim-pipes-grouping-term-supplied-form.

Current record attaches CAS5625-37-6 to CHEBI39033, while the live ChEBI term contains no structure/CAS and haschildren. TOGO source only says PIPES(final10mM). Resolve ontology children and original supplied reagent before adding an exact source alias or representing a specific molecular form. No claim is made that the current class label is nonexistent.

## Recommended Actions And Acceptance Checks

### resolve-pipes-form

Check the original PIPES reagent specification and ChEBI child identity/CAS before a bounded owner edit or alias. Retain generic/final-concentration source context meanwhile.

- A source-bound supplied-form identifier agrees with independently inspected ontology structure/CAS.
- Re-review complete changed owner payload and synchronized surfaces; do not clear historical holds through this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/ingredients/mapped/Pipes.yaml; Complete current IngredientRecord; identifier, chemical_properties, mapping and all provenance/history/roles inspected | context_only | Existing candidate is a maintained record; source correspondence does not approve role evidence or published payload. |
| source | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2567; comments paragraph4 and PIPES component; full API response | supports | The medium is buffered atpH6.8 with PIPES10mM; concentration is final medium, not stock. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39033; _embedded.terms[0], label, annotations, synonyms, is_obsolete and has_children | partial | CHEBI39033 PIPES is nonobsolete but has children and no formula/CAS annotation; it cannot certify CAS5625-37-6 as the most specific supplied form. |
| strict | reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/native-two-strict-command.json; Exact two-path command; exit0;2files0ERROR | supports | Native strict closed-schema validator passed both current records; no scientific conclusion follows. |
| holds | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; Tricine rows SEM:03e6b59c36007b80eda7 and SEM:45145f975f47c92be184; complete retained ledger used only to preserve historical holds | context_only | Historical provisional-role obligations remain open; this source identity scope does not retire any existing issue or hold. |

## Limits And Additional Notes

- This self-review does not satisfy independent campaign review.
- No global synonym is added; preparation/final-concentration qualifiers remain source-local.
- Full role evidence, all historical findings, corpus exports and release selectors were not reassessed; no inherited hold is removed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T041341Z-worker01-pipes-source-scope
kind: record
repository: CultureBotAI/MediaIngredientMech
title: Worker01 source applicability for Pipes
started_at: '2026-11-08T04:12:53.301222Z'
finished_at: '2026-11-08T04:13:41.763072Z'
reviewer:
  identity: /root/issue_context
  kind: agent
  independence: self_review
  independence_basis: Primary case author; separate skeptical campaign reviewer is
    required and not represented by this native record observation.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Bounded source identity and preparation-qualifier review only. PIPES class
  relation is supported but exact supplied-form correspondence remains unresolved.
source:
  git_revision: 58d67db32a86a359869819624568d625e7051358
  state: working_tree
  inputs:
  - path: MAPPING_SEMANTICS.md
    sha256: 6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062
    role: context
  - path: data/ingredients/mapped/Pipes.yaml
    sha256: b1c03abbda78f24f8a0c533d6e25e4e067da3f54558fc53295348b244b66d28a
    role: target
  - path: reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/native-two-strict-command.json
    sha256: cf60ba4d3404e1fac41b2e54c718e5993c55b2a98f1783e816bbb154f07ba7af
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/primary/CHEBI-39033.json
    sha256: 4209365b4df4a8a75c070d0fd7eaa29d040363a25998a7966cb7ef04b173411c
    role: context
  - path: reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/primary/TOGO-M2567.json
    sha256: c9a50e065c57cb4a13ed2ef29ad01f58a3cffd829971253e44d2e0f44d4a4731
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: c56c4d4d7332181e239798804ba80a6f49cfc7ed81d835c29312f25a963b64cf
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
targets:
- target_id: CHEBI:39033
  path: data/ingredients/mapped/Pipes.yaml
  label: PIPES
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pipes.yaml
    role: maintained ingredient; aggregate must be synchronized only at authorized
      integration
scope:
  description: One existing candidate reviewed for its assigned frozen-source applicability;
    complete owner read, roles and publication eligibility excluded.
  selection: Concentration allocation case118
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:39033
  exclusions:
  - target: Role/evidence quality and final SSSOM publication payload
    reason: Outside this source-identity assessment; all existing holds retained.
checks:
- check_id: strict
  name: Native strict closed-schema check
  status: passed
  required: true
  summary: Two explicit maintained paths; exit0; no errors.
  target_ids:
  - CHEBI:39033
  command: .temp/all-unmatched-worker-01/shard-venv/bin/python scripts/validate_strict.py
    data/ingredients/mapped/Tricine.yaml data/ingredients/mapped/Pipes.yaml --out
    reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/native-two-strict.tsv
    --workers 1
  exit_code: 0
  evidence_ids:
  - strict
- check_id: identity
  name: Primary source and ontology identity/form comparison
  status: failed
  required: true
  summary: Supplied reagent and recipe qualifier distinguished; ontology compared
    with current record.
  target_ids:
  - CHEBI:39033
  evidence_ids:
  - record
  - source
  - ontology
- check_id: publication
  name: Whole-record release and corpus export checks
  status: not_applicable
  required: false
  summary: No maintained data edits or publication support are issued by this bounded
    review.
  target_ids:
  - CHEBI:39033
evidence:
- evidence_id: record
  kind: record_content
  reference: data/ingredients/mapped/Pipes.yaml
  locator: Complete current IngredientRecord; identifier, chemical_properties, mapping
    and all provenance/history/roles inspected
  accessed_at: '2026-11-08T04:13:41.763072Z'
  support: context_only
  summary: Existing candidate is a maintained record; source correspondence does not
    approve role evidence or published payload.
  snapshot_sha256: b1c03abbda78f24f8a0c533d6e25e4e067da3f54558fc53295348b244b66d28a
- evidence_id: source
  kind: primary_source
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2567
  locator: comments paragraph4 and PIPES component; full API response
  accessed_at: '2026-11-08T04:06:15.736013Z'
  support: supports
  summary: The medium is buffered atpH6.8 with PIPES10mM; concentration is final medium,
    not stock.
  snapshot_sha256: c9a50e065c57cb4a13ed2ef29ad01f58a3cffd829971253e44d2e0f44d4a4731
- evidence_id: ontology
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:39033
  locator: _embedded.terms[0], label, annotations, synonyms, is_obsolete and has_children
  accessed_at: '2026-11-08T04:09:58.417956Z'
  support: partial
  summary: CHEBI39033 PIPES is nonobsolete but has children and no formula/CAS annotation;
    it cannot certify CAS5625-37-6 as the most specific supplied form.
  snapshot_sha256: 4209365b4df4a8a75c070d0fd7eaa29d040363a25998a7966cb7ef04b173411c
- evidence_id: strict
  kind: validation
  reference: reports/all_unmatched_20261107/worker-01/shard/concentration_stocks/captures/native-two-strict-command.json
  locator: Exact two-path command; exit0;2files0ERROR
  accessed_at: '2026-11-08T04:12:54.016883Z'
  support: supports
  summary: Native strict closed-schema validator passed both current records; no scientific
    conclusion follows.
  snapshot_sha256: cf60ba4d3404e1fac41b2e54c718e5993c55b2a98f1783e816bbb154f07ba7af
- evidence_id: holds
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: Tricine rows SEM:03e6b59c36007b80eda7 and SEM:45145f975f47c92be184; complete
    retained ledger used only to preserve historical holds
  accessed_at: '2026-11-08T04:13:41.763072Z'
  support: context_only
  summary: Historical provisional-role obligations remain open; this source identity
    scope does not retire any existing issue or hold.
  snapshot_sha256: c56c4d4d7332181e239798804ba80a6f49cfc7ed81d835c29312f25a963b64cf
assessments:
- assessment_id: source-form
  area: identity
  topic: Reagent versus prepared stock and final concentration
  outcome: concern
  summary: 10mM is final PIPES concentration; broad PIPES class is known, but supplied
    neutral/salt form is not established.
  target_ids:
  - CHEBI:39033
  evidence_ids:
  - record
  - source
  - ontology
findings:
- finding_id: PIPES-form-scope
  issue_key: mim-pipes-grouping-term-supplied-form
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Most-specific supplied PIPES form is not established by grouping-term identity
  description: Current record attaches CAS5625-37-6 to CHEBI39033, while the live
    ChEBI term contains no structure/CAS and haschildren. TOGO source only says PIPES(final10mM).
    Resolve ontology children and original supplied reagent before adding an exact
    source alias or representing a specific molecular form. No claim is made that
    the current class label is nonexistent.
  target_ids:
  - CHEBI:39033
  field_paths:
  - identifier
  - chemical_properties.cas_rn
  - ontology_mapping
  evidence_ids:
  - record
  - source
  - ontology
  rule_id: MAPPING_SEMANTICS most-specific supplied identity
  native_severity: P2
  normalization_reason: Exact supplied-form scope is materially unsupported for this
    new source claim.
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pipes.yaml
    role: maintained ingredient; aggregate must be synchronized only at authorized
      integration
actions:
- action_id: resolve-pipes-form
  description: Check the original PIPES reagent specification and ChEBI child identity/CAS
    before a bounded owner edit or alias. Retain generic/final-concentration source
    context meanwhile.
  finding_ids:
  - PIPES-form-scope
  target_ids:
  - CHEBI:39033
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pipes.yaml
    role: maintained ingredient; aggregate must be synchronized only at authorized
      integration
  acceptance_checks:
  - A source-bound supplied-form identifier agrees with independently inspected ontology
    structure/CAS.
  - Re-review complete changed owner payload and synchronized surfaces; do not clear
    historical holds through this review.
limitations:
- This self-review does not satisfy independent campaign review.
- No global synonym is added; preparation/final-concentration qualifiers remain source-local.
- Full role evidence, all historical findings, corpus exports and release selectors
  were not reassessed; no inherited hold is removed.
```
