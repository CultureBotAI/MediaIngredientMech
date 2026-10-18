# `data/ingredients/mapped/Abyssomicin_H.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The local
`kgmicrobe.compound:abyssomicin_h` placeholder is intentionally retained because
OLS candidate review found no exact external identity, but the selective-agent
role is still only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Abyssomicin_H.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:abyssomicin_h` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:abyssomicin_h`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, and
  `mapping_status: MAPPED`.
- The local placeholder represents the kg-microbe unmapped compound label
  `Abyssomicin H`; it is not being claimed as an external ChEBI or NCIT
  identity.
- The manual candidate review inspected `CHEBI:70593` Abyssomicin I,
  `CHEBI:132351` triptobenzene H, and `CHEBI:132354` triptoquinone H and
  retained the placeholder with `NO_IDENTITY_PROMOTION` because the candidates
  are different named compounds.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abyssomicin_G.yaml data/ingredients/mapped/Abyssomicin_H.yaml data/ingredients/mapped/Acacetin.yaml data/ingredients/mapped/Aces.yaml data/ingredients/mapped/Acetaldehyde.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Abyssomicin_H.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the OAK sqlite label adapter for the local `kgmicrobe.compound`
  placeholder; focused term validation is unavailable for this CURIE.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The YAML and unknown-term triage row both record this as an expected local
  registry placeholder pending an exact external ontology term.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  documents the three reviewed ChEBI candidates and concludes that they are
  different named compounds, not identity matches for Abyssomicin H.
- The SSSOM row maps `MIM:Abyssomicin_H` to the same local
  `kgmicrobe.compound:abyssomicin_h` registry identifier with
  `skos:exactMatch`.
- The `physicochemical_roles.SELECTIVE_AGENT` assertion is still sourced only
  to `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with the
  record's own `curator_note` saying review is recommended.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, unknown-term triage row, manual candidate review
  row, placeholder OLS candidate row, and ignored aggregate backups.

## Completeness

- The record is complete enough for an unmapped kg-microbe antibiotic
  placeholder: formula, CAS, and structure slots are empty because no exact
  external ontology or registry identity has been curated.
- The consequential gap is evidence for the selective-agent role; name-based
  inference alone is not enough to assert the role for this substance.

## Recommended Edits

- Replace or remove
  `data/ingredients/mapped/Abyssomicin_H.yaml`'s
  `physicochemical_roles.SELECTIVE_AGENT` entry after inspecting evidence that
  specifically supports Abyssomicin H as a selective agent. Re-run
  `scripts/validate_strict.py` and `scripts/validate_sssom_invariants.py`.
- Leave `kgmicrobe.compound:abyssomicin_h` in place unless a future exact
  external ontology identity is found.
