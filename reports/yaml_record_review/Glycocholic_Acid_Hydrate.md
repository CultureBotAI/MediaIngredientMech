# `data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml`

## Verdict

Needs curation. The record uses the active `CHEBI:182320` glycocholic-acid
hydrate term and PubChem supports the hydrate formula for CAS `1192657-83-2`,
but `chemical_properties` now combine that hydrate formula with an anhydrous
InChI and SMILES.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:182320` with matching
  `ontology_mapping.ontology_id`, canonical label `Glycocholic acid hydrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `1192657-83-2`, formula `C26H45NO7`, an
  anhydrous InChI, and an anhydrous SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml data/ingredients/mapped/Glycocyamine.yaml data/ingredients/mapped/Glycogen.yaml data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml data/ingredients/mapped/Glycolaldehyde.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, hydrate formula, anhydrous InChI/SMILES, exact
  synonym, singleton type, and #321 note as the per-record YAML.
- OLS4 resolves `CHEBI:182320` as `Glycocholic acid hydrate` and lists the
  stored IUPAC string as an exact synonym, so the ontology identity and final
  SSSOM synonym are current.
- PubChem resolves CAS `1192657-83-2` to title `Glycocholic acid hydrate`,
  formula `C26H45NO7`, and an InChI that explicitly includes `.H2O`.
- Major: the #321 repair updated `molecular_formula` to the PubChem hydrate
  value while leaving ChEBI's anhydrous InChI and SMILES in place. The formula
  now denotes an extra water of hydration that the structural fields omit.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycocholic_Acid_Hydrate` to `CHEBI:182320` by `skos:exactMatch` and
  keeps the OLS4 synonym plus `CAS:1192657-83-2` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  the hydrate-guard exception text for this ChEBI term, and ignored aggregate
  backups.

## Completeness

- The exact ChEBI identity, CAS RN, hydrate formula, exact synonym, ingredient
  type, and final SSSOM row are populated.
- The structural fields need to be reconciled with the curated hydrate formula.

## Recommended Edits

- Major: in `data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml`, replace
  the anhydrous `chemical_properties.inchi` and `chemical_properties.smiles`
  with hydrate-aware PubChem values, or if unbound water should remain outside
  the structural fields, document that convention and stop storing a formula
  that cannot be reproduced from those fields.
