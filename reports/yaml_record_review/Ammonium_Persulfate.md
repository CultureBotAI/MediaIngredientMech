# `data/ingredients/mapped/Ammonium_Persulfate.yaml`

## Verdict

Needs curation. The exact `CHEBI:156543` identity, CAS, chemistry, ChEBI synonym,
row-review confirmation, SSSOM row, and aggregate copy pass, but the record has
a provisional `NITROGEN_SOURCE` role inferred solely from inorganic-ammonium-salt
ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonium_Persulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:156543` with
  `ontology_mapping.ontology_id: CHEBI:156543`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:156543` to
  `ammonium persulfate` with formula `2H4N.O6S2`, CAS `7727-54-0`, SMILES
  `O=S([O-])OOS(=O)[O-].[NH4+].[NH4+]`, and InChIKey
  `VAZSKTXWXKYQJF-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium.yaml data/ingredients/mapped/Ammonium_Acetate.yaml data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml data/ingredients/mapped/Ammonium_Persulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Persulfate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned canonical `ammonium persulfate` and ChEBI's exact structural synonym
  for `CHEBI:156543`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:156543`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Ammonium_Persulfate` to `CHEBI:156543` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 402 maps
  `MIM:Ammonium_Persulfate` to `CHEBI:156543` with `skos:exactMatch`, CAS
  `7727-54-0`, and the `CONFIRMED` trailer.
- The only role is a `NITROGEN_SOURCE` computational prediction inferred from
  inorganic ammonium salt ancestry; no medium or source claim demonstrates that
  ammonium persulfate was curated as a nitrogen source.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, OAK/OLS confirmation, generated reports, and
  no CultureMech recipe membership rows for `CHEBI:156543`.

## Completeness

- CAS, formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported nitrogen-source role is the only active gap.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the provisional role.

## Recommended Edits

- In `data/ingredients/mapped/Ammonium_Persulfate.yaml`, replace the
  `NITROGEN_SOURCE` computational prediction with source-backed evidence, or
  remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Persulfate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
