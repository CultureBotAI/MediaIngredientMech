# `data/ingredients/mapped/Glyoxylate.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:36655` glyoxylate, the
anion structure fields, the source-occurrence accounting, and the final SSSOM
row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Glyoxylate.yaml`.
- Identifier and grounding: `identifier: CHEBI:36655` with matching
  `ontology_mapping.ontology_id`, canonical label `glyoxylate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C2HO3`, molecular weight `73.027`, InChI
  `InChI=1S/C2H2O3/c3-1-2(4)5/h1H,(H,4,5)/p-1`, and SMILES
  `[H]C(=O)C(=O)[O-]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycylglycine.yaml data/ingredients/mapped/Glycylglycylglycine.yaml data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml data/ingredients/mapped/Glyoxylate.yaml data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glyoxylate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:36655` as `glyoxylate` with formula `C2HO3`, charge
  `-1`, the same InChI, and the same SMILES as the record.
- The review-ingredients promotion correctly moved this record from
  `PENDING_REVIEW` to `MAPPED` after the imported OLS exact label match was
  checked locally.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glyoxylate` to `CHEBI:36655` by `skos:exactMatch` and has an empty
  `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the MicrobeDecoder auto-mapped review entry, generated
  products, the final SSSOM row, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, anion formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, singleton type, and final SSSOM row are
  populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
