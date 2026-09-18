# `data/ingredients/mapped/Glycolaldehyde.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:17071` glycolaldehyde, the
#320 CAS correction from dimer to monomer, the ChEBI synonym, and the final
SSSOM row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycolaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:17071` with matching
  `ontology_mapping.ontology_id`, canonical label `glycolaldehyde`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `141-46-8`, formula `C2H4O2`, InChI
  `InChI=1S/C2H4O2/c3-1-2-4/h1,4H,2H2`, and SMILES `[H]C(=O)CO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml data/ingredients/mapped/Glycocyamine.yaml data/ingredients/mapped/Glycogen.yaml data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml data/ingredients/mapped/Glycolaldehyde.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycolaldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, corrected monomer CAS RN, formula, InChI, SMILES,
  exact synonym, and singleton type as the per-record YAML.
- OLS4 resolves `CHEBI:17071` as `glycolaldehyde`, lists `cas:141-46-8` as a
  database cross-reference, and lists `Hydroxyacetaldehyde` as an exact
  synonym.
- PubChem resolves CAS `141-46-8` to `Glycolaldehyde` with formula `C2H4O2` and
  the same InChI as the record.
- The #320 correction removed CAS `23147-58-2`, which denoted the dimer rather
  than this monomer.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycolaldehyde` to `CHEBI:17071` by `skos:exactMatch` and keeps
  `Hydroxyacetaldehyde` plus `CAS:141-46-8` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, corrected CAS RN, formula, InChI, SMILES, exact
  synonym, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
