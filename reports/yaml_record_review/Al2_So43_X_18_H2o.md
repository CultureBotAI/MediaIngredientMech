# `data/ingredients/mapped/Al2_So43_X_18_H2o.yaml`

## Verdict

Pass with minor issues. The exact octadecahydrate identity, CAS xref, hydrate
synonyms, ChEBI chemistry, occurrence count, SSSOM row, and aggregate copy pass;
only one historical auto-backfill event has truncated structure text.

## Identity

- Reviewed record: `data/ingredients/mapped/Al2_So43_X_18_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:74779` with
  `ontology_mapping.ontology_id: CHEBI:74779`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:74779` to
  `aluminium sulfate octadecahydrate` with formula `2Al.18H2O.3O4S`, CAS
  `7784-31-8`, SMILES, and InChIKey `AMVQGJHFDJVOOB-UHFFFAOYSA-H`.
- Local OAK lists `Al2(SO4)3.18H2O`, `aluminium sulfate.18H2O`, and
  `aluminum sulfate.18H2O` as related synonyms and
  `aluminium sulfate--water (1/18)` as an exact synonym of the same ChEBI term.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Agave.yaml data/ingredients/mapped/Air-dried_Garden_Soil.yaml data/ingredients/mapped/Air.yaml data/ingredients/mapped/Al2_So43_X_18_H2o.yaml data/ingredients/mapped/Alanosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Al2_So43_X_18_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:74779 CHEBI:221124`:
  returned the expected labels and aliases for both ChEBI terms checked in this
  batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:74779 CHEBI:221124`:
  returned the exact formula, SMILES, InChI, InChIKey, charge, average mass,
  and monoisotopic mass for `CHEBI:74779`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `reports/hydrate_grounding.tsv` classifies the same CHEBI identity as
  `OK_HYDRATE_TERM`.
- `mappings/hydrate_review.tsv` says the named octadecahydrate is an
  established isolated form and that the ChEBI identity/formula agree.
- `mappings/culturemech_recipe_membership.tsv` contains 2 rows for
  `CHEBI:74779`, matching both `occurrence_statistics` counters.
- `mappings/ingredient_mappings.sssom.tsv` row 359 maps
  `MIM:Al2_So43_X_18_H2o` to `CHEBI:74779` with `skos:exactMatch` and exports
  the hydrate surface forms plus CAS `7784-31-8`.
- The historical `2026-05-01T08:08:27.909775+00:00`
  `AUTO_BACKFILL_CHEBI_CHEMISTRY` event truncates the InChI and SMILES in its
  `changes` text, but the current `chemical_properties` block is complete.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, hydrate-review rows, occurrence rows,
  generated indexes, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, exact hydrate mapping, hydrate-form synonyms,
  occurrence statistics, curation history, and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None for current identity or mapping. Avoid rewriting the old append-only
  history entry solely to expand its truncated structure prose.
