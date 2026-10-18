# `data/ingredients/mapped/Glycocyamine.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup to active `CHEBI:16344` guanidinoacetic acid
is structurally consistent, the CAS provenance is retained as
`CAS_RN_LOOKUP`, and the final SSSOM row exports only ChEBI synonyms plus the
CAS payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycocyamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16344` with matching
  `ontology_mapping.ontology_id`, canonical label `guanidinoacetic acid`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `352-97-6`, formula `C3H7N3O2`, InChI
  `InChI=1S/C3H7N3O2/c4-3(5)6-1-2(7)8/h1H2,(H,7,8)(H4,4,5,6)`, and SMILES
  `N=C(N)NCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml data/ingredients/mapped/Glycocyamine.yaml data/ingredients/mapped/Glycogen.yaml data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml data/ingredients/mapped/Glycolaldehyde.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycocyamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS-to-ChEBI mapping, CAS RN, formula, InChI, SMILES, exact synonyms,
  and singleton type as the per-record YAML.
- OLS4 resolves `CHEBI:16344` as `guanidinoacetic acid`, lists
  `cas:352-97-6` as a database cross-reference, and lists
  `(carbamimidamido)acetic acid` and `N-carbamimidoylglycine` as exact
  synonyms.
- PubChem resolves CAS `352-97-6` to `Guanidinoacetic Acid` with formula
  `C3H7N3O2` and the same InChI as the record.
- The `CAS_RN_LOOKUP` grade is the correct MAPPING_SEMANTICS method grade for
  a record created by an explicit CAS-to-ChEBI xref lookup, and the final
  identity row still uses `skos:exactMatch` as required by Rule D.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycocyamine` to `CHEBI:16344` by `skos:exactMatch` and keeps the two
  curated ChEBI synonyms plus `CAS:352-97-6` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS lookup provenance, CAS RN, formula, InChI,
  SMILES, exact synonyms, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
