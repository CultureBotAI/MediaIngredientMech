# `data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml`

## Verdict

Pass. This is a rejected duplicate tombstone for
`Ammonium chloride (nitrogen source)` that was merged into the live `Nh4cl`
record; strict validation still passes, and no active SSSOM or aggregate row is
exported for the tombstone subject.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml`.
- Identifier and grounding: `identifier: CHEBI:31206` with
  `ontology_mapping.ontology_id: CHEBI:31206`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: REJECTED`.
- Local OAK resolves `CHEBI:31206` to `ammonium chloride` with formula
  `Cl.H4N`, CAS `12125-02-9`, SMILES
  `[Cl-].[H][N+]([H])([H])[H]`, and InChIKey
  `NLXLAEXVIDQMFP-UHFFFAOYSA-N`.
- The `MERGED_INTO` history records that this duplicate was merged into
  `CHEBI:31206` `NH4Cl` and had SSSOM rows dropped.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium.yaml data/ingredients/mapped/Ammonium_Acetate.yaml data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml data/ingredients/mapped/Ammonium_Persulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned canonical `ammonium chloride`, `NH4Cl`, and related
  `CHEBI:31206` aliases.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:31206`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the historical
  `Ammonium_Chloride_(nitrogen_Source)` synonym-enrichment row as
  `ALREADY_REPRESENTED`; the live `Nh4cl` row carries
  `Ammonium chloride (nitrogen source)` as a synonym.
- `mappings/ingredient_mappings.sssom.tsv` row 2143 maps `MIM:Nh4cl` to
  `CHEBI:31206` with the merged surface forms.
- A hidden/ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`
  and `data/curated/mapped_ingredients.yaml` found no
  `MIM:Ammonium_Chloride_Nitrogen_Source` row, confirming the tombstone is not
  published.

## Completeness

- The merge history, rejected status, retained old mapping, and synonym pointer
  are enough to explain why this duplicate exists.
- This tombstone is intentionally absent from the mapped aggregate; the live
  `CHEBI:31206` curation surface is `data/ingredients/mapped/Nh4cl.yaml`.
- No chemical, role, occurrence, component, environmental context, discussion,
  or dataset edit is needed on the tombstone.

## Recommended Edits

- None.
