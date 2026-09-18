# `data/ingredients/mapped/Glycolic_Acid.yaml`

## Verdict

Needs curation. The CultureBotHT exact match to active `CHEBI:17497` glycolic
acid, CAS RN, ChEBI synonym, structure fields, and final SSSOM row pass, but
`CARBON_SOURCE` remains an unsupported computational role.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycolic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17497` with matching
  `ontology_mapping.ontology_id`, canonical label `glycolic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `79-14-1`, formula `C2H4O3`, InChI
  `InChI=1S/C2H4O3/c3-1-2(4)5/h3H,1H2,(H,4,5)`, and SMILES `O=C(O)CO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycolate.yaml data/ingredients/mapped/Glycolic_Acid.yaml data/ingredients/mapped/Glycyl-L-proline.yaml data/ingredients/mapped/Glycyl-glycine.yaml data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycolic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CAS RN, formula, InChI, SMILES, exact synonym,
  singleton type, and provisional carbon-source role as the per-record YAML.
- OLS4 resolves `CHEBI:17497` as `glycolic acid`, lists `cas:79-14-1` as a
  database cross-reference, and lists `Hydroxyacetic acid` as an exact synonym.
- PubChem resolves CAS `79-14-1` to `Glycolic Acid` with formula `C2H4O3` and
  the same InChI as the record.
- Major: `nutritional_roles.CARBON_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and a provisional
  curator note. The role needs claim-level CultureMech or literature support;
  FEBA carbon-panel provenance in the import note is not attached to the role.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycolic_Acid` to `CHEBI:17497` by `skos:exactMatch` and keeps
  `Hydroxyacetic acid` plus `CAS:79-14-1` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, exact synonym,
  ingredient type, and final SSSOM row are populated.
- The carbon-source role needs claim-level support or removal.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` from
  `data/ingredients/mapped/Glycolic_Acid.yaml`, or replace the provisional
  name-pattern evidence with inspected source evidence that specifically
  supports glycolic acid as a carbon source.
