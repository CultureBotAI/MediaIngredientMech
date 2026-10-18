# `data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml`

## Verdict

Needs curation, major. The stock-solution identity and narrow match to sodium
hydrogencarbonate pass, but two parenthetical source surfaces are not exact
synonyms of an 84 g/L sodium bicarbonate solution.

## Identity

- Reviewed record: `data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:84_gl_nahco3_solution` with
  `ontology_mapping.ontology_id: CHEBI:32139`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:32139` to
  `sodium hydrogencarbonate`, the parent compound of this concentration-specific
  stock solution.
- The record intentionally uses `ingredient_type: STOCK_SOLUTION`,
  `solution_type: OTHER`, and a minted kg-microbe ingredient identifier instead
  of claiming exact identity with neat sodium hydrogencarbonate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml data/ingredients/mapped/A-Cyclodextrin.yaml data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/AQDS.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected ChEBI label and sodium bicarbonate related synonyms for
  `CHEBI:32139`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:32139`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The #288 curation note supports representing an 84 g/L NaHCO3 stock solution
  as a local stock-solution ingredient with `skos:narrowMatch` to
  `CHEBI:32139`.
- The SSSOM export has the expected narrow row to `CHEBI:32139` and exact
  registry rows preserving the minted kg-microbe identifiers.
- `NaHCO3` is a valid other surface for the sodium bicarbonate component, but
  `(5% w/v solution)` is a different concentration from `84 g/L`, and
  `(after autoclaving)` is a preparation note rather than a name for this stock
  solution. Both are present as `RAW_TEXT` synonyms recovered from prior SSSOM
  `other` values.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM rows, source
  unmapped audit row, and ignored aggregate backups.

## Completeness

- The stock-solution classification, local kg-microbe identifier, and
  sodium-bicarbonate parent mapping are populated.
- Chemical properties are correctly absent because this is a prepared solution,
  not neat sodium hydrogencarbonate.

## Recommended Edits

- In `data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml`, remove
  `(5% w/v solution)` and `(after autoclaving)` from `synonyms`, or move them
  to occurrence-only provenance that does not make them names for the 84 g/L
  solution.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation and
  the SSSOM invariant check.
