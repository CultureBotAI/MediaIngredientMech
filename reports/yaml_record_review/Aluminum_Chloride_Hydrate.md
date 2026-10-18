# `data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, NCIT parent, exact CAS/local SSSOM
companion rows, CultureMech count, and aggregate copy pass, but the record still
stores an unspecified `hydrate` surface with a monohydrate-like PubChem formula
that `mappings/hydrate_review.tsv` already judged as requiring source
verification before a unique water stoichiometry can be asserted.

## Identity

- Reviewed record: `data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:10124-27-3` with
  `ontology_mapping.ontology_id: NCIT:C83530`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS resolves `NCIT:C83530` to `Aluminum Chloride`; this is a parent row
  for the hydrate, while `cas:10124-27-3` preserves the exact registry
  identity.
- PubChem resolves CAS `10124-27-3` to CID `16211594` with the same formula
  `AlCl3H2O`, SMILES `O.[Al](Cl)(Cl)Cl`, and InChI stored in the record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml data/ingredients/mapped/Amicoumacin_B.yaml data/ingredients/mapped/Amikacin.yaml data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml data/ingredients/mapped/Amino_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi search "aluminum chloride hydrate"`:
  returned no rows, agreeing with the CAS fallback history that no exact ChEBI
  term exists locally.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  `NCIT:C83530` by exact EBI OLS CURIE lookup, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` marks the older
  unknown-term row as prefix-validator coverage rather than a bad NCIT ID.
- `mappings/culturemech_recipe_membership.tsv` contains 28 `cas:10124-27-3`
  rows, matching `occurrence_statistics.total_occurrences: 28`.
- `mappings/ingredient_mappings.sssom.tsv` rows 386-388 export the required
  `skos:narrowMatch` to `NCIT:C83530`, exact CAS registry row, and exact
  `kgmicrobe.compound:aluminum_chloride_hydrate` companion row.
- `reports/hydrate_grounding.tsv` classifies the CAS primary as an
  `OK_OWN_CAS_ID`, but `mappings/hydrate_review.tsv` independently records that
  the label is an unspecified hydrate and the CAS/formula metadata does not
  securely establish a unique water stoichiometry.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM rows, CultureMech membership rows, NCIT
  validation row, hydrate review rows, generated reports, and stock-solution
  component references to the same CAS identity.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, mapping evidence, SSSOM
  parent and local identity rows, and `ingredient_type` are populated.
- The unresolved gap is hydrate form specificity: the active record should not
  treat `AlCl3H2O` as a curator-verified stoichiometry until the CultureBotHT or
  supplier source identifies the hydrated form.
- No synonym, role, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the unresolved formula.

## Recommended Edits

- In `data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml`, either confirm
  the exact hydrate stoichiometry from the CultureBotHT/supplier source and
  update the preferred term plus chemistry accordingly, or qualify/clear the
  formula so the CAS hydrate record does not overstate a verified monohydrate.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
