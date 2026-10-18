# `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`

## Verdict

Needs curation. The CAS primary tetrahydrate identity, `skos:closeMatch`
anhydrous ChEBI parent, exact CAS SSSOM row, 12 CultureMech memberships,
hydrate regrade, and rejected 24-hydrate sibling pass, but the record still
stores and exports an anhydrous-parent synonym as exact and carries a
provisional `TRACE_ELEMENT` role.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`.
- Identifier and grounding: `identifier: cas:12054-85-2` with
  `ontology_mapping.ontology_id: CHEBI:91249`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:91249` to anhydrous
  `ammonium molybdate` with formula `2H4N.MoO4`; the active record's CAS,
  formula `H32Mo7N6O28`, and PubChem CID `16211167` denote the tetrahydrate.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium.yaml data/ingredients/mapped/Ammonium_Acetate.yaml data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml data/ingredients/mapped/Ammonium_Persulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned canonical `ammonium molybdate`, `Diammonium molybdate`, and
  `bisammonium dioxido(dioxo)molybdenum` aliases for the anhydrous
  `CHEBI:91249` parent.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned anhydrous formula and structure metadata for `CHEBI:91249`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The `#342` curation evidence and `REGRADED_HYDRATE_TO_CLOSE_MATCH` history
  correctly state that a hydrate is not narrower than its anhydrous form and
  that `CHEBI:91249` is only a `CLOSE_MATCH` parent.
- `mappings/culturemech_recipe_membership.tsv` contains 12
  `cas:12054-85-2` rows, matching `occurrence_statistics.total_occurrences:
  12`.
- `mappings/ingredient_mappings.sssom.tsv` rows 400-401 export the close ChEBI
  row and exact CAS registry row for `MIM:Ammonium_Molybdate_Tetrahydrate`.
- The active record still carries `bisammonium dioxido(dioxo)molybdenum` as
  `EXACT_SYNONYM`; that is an alias of the anhydrous `CHEBI:91249` parent, not
  of ammonium molybdate tetrahydrate.
- The active `TRACE_ELEMENT` role cites only in-session Claude reasoning and
  remains explicitly provisional.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM rows, 12 CultureMech membership rows, row-review
  outputs, hydrate-family rows, and the separate diammonium-molybdate record.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, close-parent evidence,
  exact CAS SSSOM identity, rejected sibling hydrate label, curation history,
  and `ingredient_type` are populated.
- The anhydrous exact synonym and provisional trace-element role remain the
  consequential gaps.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the over-broad synonym and provisional role.

## Recommended Edits

- In `data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml`, remove or
  reject `bisammonium dioxido(dioxo)molybdenum` so an anhydrous
  `CHEBI:91249` alias is not exported as an exact tetrahydrate label.
- Replace the provisional `TRACE_ELEMENT` assignment with source-backed
  evidence, or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
