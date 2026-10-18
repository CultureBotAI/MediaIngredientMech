# `data/ingredients/mapped/Granaticin.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:5533` granaticin, the
structure fields, the source-occurrence accounting, and the final SSSOM row
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Granaticin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5533` with matching
  `ontology_mapping.ontology_id`, canonical label `granaticin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C22H20O10`, molecular weight `444.392`, InChI
  `InChI=1S/C22H20O10/c1-5-11-15(21-8(30-5)4-10(24)32-21)19(27)13-14(17(11)25)20(28)16-12(18(13)26)7-3-9(23)22(16,29)6(2)31-7/h5-9,21,23,26,28-29H,3-4H2,1-2H3/t5?,6-,7-,8+,9-,21-,22-/m1/s1`,
  and the ChEBI/PubChem SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Granaticin.yaml data/ingredients/mapped/Grasseriomycin.yaml data/ingredients/mapped/Green_House_Soil.yaml data/ingredients/mapped/Grisamine.yaml data/ingredients/mapped/Griseolutein_A.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Granaticin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:5533` as `granaticin` with formula `C22H20O10`, the
  same InChI, the same SMILES, and CAS `19879-06-2`.
- The review-ingredients promotion correctly moved this record from
  `PENDING_REVIEW` to `MAPPED` after the imported OLS exact label match was
  checked locally.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Granaticin` to `CHEBI:5533` by `skos:exactMatch` and has an empty
  `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the MicrobeDecoder auto-mapped review entry, generated
  products, the final SSSOM row, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, singleton type, and final SSSOM row are
  populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
