# `data/ingredients/mapped/Ammonium_Acetate.yaml`

## Verdict

Needs curation. The exact `CHEBI:62947` identity, CAS, chemistry, nitrogen role,
67 CultureMech memberships, SSSOM row, and aggregate copy pass, but the active
synonym list still contains two imported CultureMech role/property metadata
strings that are not labels for ammonium acetate.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonium_Acetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:62947` with
  `ontology_mapping.ontology_id: CHEBI:62947`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:62947` to
  `ammonium acetate` with formula `C2H3O2.H4N`, SMILES
  `CC(=O)[O-].[NH4+]`, and InChIKey `USFZMSVCRYTOJT-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium.yaml data/ingredients/mapped/Ammonium_Acetate.yaml data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml data/ingredients/mapped/Ammonium_Persulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Acetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned canonical `ammonium acetate` and the expected acetate aliases for
  `CHEBI:62947`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:62947`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Ammonium_Acetate` to `CHEBI:62947` mapping.
- `mappings/culturemech_recipe_membership.tsv` contains 67 `CHEBI:62947` rows,
  matching `occurrence_statistics.total_occurrences: 67`.
- `mappings/ingredient_mappings.sssom.tsv` row 399 maps
  `MIM:Ammonium_Acetate` to `CHEBI:62947` with `skos:exactMatch`, the
  expected ChEBI abbreviations, CAS `631-61-8`, and the OAK/OLS confirmation
  trailer.
- The `NITROGEN_SOURCE` role is backed by the imported CultureMech
  `Nitrogen Source` role text, but the old role/property text copies remain in
  `synonyms` as `RAW_TEXT`.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, OAK/OLS confirmation, 67 CultureMech
  membership rows, generated reports, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, nitrogen-source role,
  curation history, and `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the two non-label synonym entries.

## Recommended Edits

- Remove the two `Role: Nitrogen source; Properties: ...` entries from
  `data/ingredients/mapped/Ammonium_Acetate.yaml` `synonyms`; they are
  CultureMech metadata already represented by `nutritional_roles`, not source
  labels.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Acetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
