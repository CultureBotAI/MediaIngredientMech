# `data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`

## Verdict

Pass. The DL source surface exact-matches active `CHEBI:37070`
2-methylbutyric acid, whose identity is non-stereospecific and carries the
racemic CAS RN `116-53-0`; the CultureMech carbon-source role is imported from
source role text, and the final SSSOM row publishes genuine same-substance
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:37070` with
  `ontology_mapping.ontology_id: CHEBI:37070`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 23/23 source occurrences.
- Local OAK resolves `CHEBI:37070` to active `2-methylbutyric acid`, formula
  `C5H10O2`, the expected InChI and SMILES, CAS xref `116-53-0`, and
  2-methylbutyric acid exact or related synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:132764 CHEBI:34683 CHEBI:15377 CHEBI:42160 CHEBI:37070`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:37070`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `116-53-0` to CID 8314 with formula `C5H10O2` and the
  same InChIKey as the record.
- The hidden/ignored-inclusive exact search over `data/ingredients` for
  `CHEBI:37070` and `116-53-0` found only
  `data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`.
- `nutritional_roles.CARBON_SOURCE` carries `DATABASE_ENTRY` evidence imported
  from the CultureMech pipeline with original role text `Carbon Source`, so it
  is not one of the provisional ChEBI-ancestry role inferences.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-2-methylbutyric_Acid` to `CHEBI:37070` with `skos:exactMatch`,
  canonical object label `2-methylbutyric acid`, CHEBI object source, true DL
  2-methylbutyric acid synonyms, and `CAS:116-53-0`.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy,
  CultureMech carbon-source role evidence, and occurrence provenance are
  populated.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- None.
