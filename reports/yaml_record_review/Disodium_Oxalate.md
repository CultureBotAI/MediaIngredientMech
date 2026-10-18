# `data/ingredients/mapped/Disodium_Oxalate.yaml`

## Verdict

Pass. The MicrobeDecoder record exact-matches active `CHEBI:132764` sodium
oxalate by synonym, the CAS RN and structure fields agree with ChEBI and
PubChem, and the final SSSOM row contains only true same-substance synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Disodium_Oxalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132764` with
  `ontology_mapping.ontology_id: CHEBI:132764`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 9/9 source occurrences.
- Local OAK resolves `CHEBI:132764` to active `sodium oxalate`, formula
  `C2O4.2Na`, the expected InChI, SMILES, CAS xref `62-76-0`, and exact or
  related synonyms covering disodium oxalate surfaces such as `Oxalic acid,
  disodium salt`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:132764 CHEBI:34683 CHEBI:15377 CHEBI:42160 CHEBI:37070`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:132764`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `62-76-0` to CID 6125 with formula `C2Na2O4` and the
  same InChIKey as the record.
- The hidden/ignored-inclusive exact search over `data/ingredients` for
  `CHEBI:132764` and `62-76-0` found only
  `data/ingredients/mapped/Disodium_Oxalate.yaml`.
- The row-review tables classify the Na-oxalate source surface as already
  represented by `CHEBI:132764`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Disodium_Oxalate` to `CHEBI:132764` with `skos:exactMatch`, canonical
  object label `sodium oxalate`, CHEBI object source, disodium oxalate
  synonymy, and `CAS:62-76-0`.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy, and
  MicrobeDecoder occurrence provenance are populated.
- No mixture components, supplied forms, nutritional roles, physiochemical
  roles, biological roles, or environmental contexts are needed for the exact
  disodium oxalate identity.

## Recommended Edits

- None.
