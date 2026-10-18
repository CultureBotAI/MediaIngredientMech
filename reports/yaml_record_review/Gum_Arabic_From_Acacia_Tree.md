# `data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml`

## Verdict

Needs curation. The FoodOn narrow parent, CAS fallback, registry companion row,
and final SSSOM rows pass for a local gum-arabic subject, but the record is
typed as `SINGLE_INGREDIENT` even though gum arabic is a variable acacia-sap
mixture rather than one defined molecule.

## Identity

- Reviewed record: `data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml`.
- Identifier and grounding: `identifier: cas:9000-01-5` with
  `ontology_mapping.ontology_id: FOODON:03412975`, label `gum arabic`, source
  `FOODON`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9000-01-5` with no formula, InChI, SMILES, or
  PubChem CID.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Guanidinium_Chloride.yaml data/ingredients/mapped/Guanine.yaml data/ingredients/mapped/Guanosine.yaml data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `FOODON:03412975` and the CAS registry
  CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `FOODON:03412975` as active `gum arabic`; its definition
  describes hardened sap from acacia trees, so the FoodOn row is a valid broad
  food-origin parent for the CAS fallback subject.
- Fresh PubChem lookup for CAS `9000-01-5` returned no CID, supporting the
  local CAS-primary fallback instead of a PubChem-backed CHEBI chemical
  structure.
- The final SSSOM correctly publishes the FoodOn parent as `skos:narrowMatch`,
  and preserves CAS `9000-01-5` plus
  `kgmicrobe.ingredient:gum_arabic_from_acacia_tree` as exact registry rows for
  the local subject.
- Major: `ingredient_type: SINGLE_INGREDIENT` is too specific. The record has
  no defined formula or structure and represents a variable natural mixture,
  matching the schema's `UNDEFINED_MIXTURE` category.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the final FoodOn, CAS, and
  local registry SSSOM rows plus row-review decisions that keep the registry
  identifiers.

## Completeness

- The FoodOn parent, CAS fallback identifier, and generated registry companion
  row are complete for a local gum-arabic record.
- The ingredient type is incomplete until it stops advertising this variable
  acacia gum as a single defined ingredient.

## Recommended Edits

- Major: change `ingredient_type` from `SINGLE_INGREDIENT` to
  `UNDEFINED_MIXTURE`.
- Major: adjust the two `auto_classify_ingredient_type` curation-history
  entries so they are not the only explanation for the current type after the
  correction.
