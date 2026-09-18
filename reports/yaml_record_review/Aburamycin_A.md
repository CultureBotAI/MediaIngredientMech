# `data/ingredients/mapped/Aburamycin_A.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The local
`kgmicrobe.compound:aburamycin_a` placeholder is intentionally retained because
OLS candidate review found no exact external identity, but the selective-agent
role is still only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Aburamycin_A.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:aburamycin_a` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:aburamycin_a`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, and
  `mapping_status: MAPPED`.
- The local placeholder represents the kg-microbe unmapped compound label
  `Aburamycin A`; it is not being claimed as an external ChEBI or NCIT
  identity.
- The manual candidate review inspected the low-confidence OLS candidates
  `CHEBI:199303` A83094A, `CHEBI:199353` A-90289 A, and `CHEBI:199611`
  A32390A and retained the placeholder with `NO_IDENTITY_PROMOTION`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abikoviromycin.yaml data/ingredients/mapped/Abscisic_Acid.yaml data/ingredients/mapped/Aburamycin_A.yaml data/ingredients/mapped/Abyssomicin_B.yaml data/ingredients/mapped/Abyssomicin_D.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aburamycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  documents the three reviewed ChEBI candidates and concludes that their labels
  are not label or synonym identity matches for Aburamycin A.
- The SSSOM row maps `MIM:Aburamycin_A` to the same local
  `kgmicrobe.compound:aburamycin_a` registry identifier with
  `skos:exactMatch`.
- The `physicochemical_roles.SELECTIVE_AGENT` assertion is still sourced only
  to `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with the
  record's own `curator_note` saying review is recommended.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, unknown-term
  triage row, manual candidate review row, and ignored aggregate backups.

## Completeness

- The record is complete enough for an unmapped kg-microbe antibiotic
  placeholder: formula, CAS, and structure slots are empty because no exact
  external ontology or registry identity has been curated.
- The consequential gap is evidence for the selective-agent role; name-based
  inference alone is not enough to assert the role for this substance.

## Recommended Edits

- Replace or remove
  `data/ingredients/mapped/Aburamycin_A.yaml`'s
  `physicochemical_roles.SELECTIVE_AGENT` entry after inspecting evidence that
  specifically supports Aburamycin A as a selective agent. Re-run
  `scripts/validate_strict.py` and `scripts/validate_sssom_invariants.py`.
- Leave `kgmicrobe.compound:aburamycin_a` in place unless a future exact
  external ontology identity is found.
