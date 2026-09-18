# `data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml`

## Verdict

Needs curation. The record correctly uses a local identifier for the distinct
0.02 M disodium phosphate heptahydrate stock solution and a close parent row to
anhydrous `CHEBI:34683`, but the curated chemical payload and final SSSOM
`other` values still leak anhydrous, heptahydrate, and dihydrate solute labels
onto the stock-solution subject.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:disodium_phosphate_heptahydrate_~28002_m_stock~29`
  with `ingredient_type: STOCK_SOLUTION`,
  `ontology_mapping.ontology_id: CHEBI:34683`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and 1/1 source
  occurrence.
- Local OAK resolves `CHEBI:34683` to active `disodium hydrogenphosphate`, the
  anhydrous disodium phosphate species with formula `HO4P.2Na` and molecular
  weight 141.958, not the heptahydrate and not a 0.02 M stock solution.
- The local `kgmicrobe.ingredient` registry row is exact for the stock solution;
  the `CHEBI:34683` ontology row is only a close parent, which is the correct
  direction for this distinct hydrated stock-solution subject.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:132764 CHEBI:34683 CHEBI:15377 CHEBI:42160 CHEBI:37070`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:34683`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:34683`, `CHEBI:131825`, `disodium_phosphate_heptahydrate`, and
  `sodium hydrogen phosphate--water` found this stock-solution record, the
  related active sodium phosphate hydrate records, and the active anhydrous
  `Na2hpo4` record.
- The final `mappings/ingredient_mappings.sssom.tsv` registry sibling maps
  `MIM:Disodium_Phosphate_Heptahydrate_002_M_Stock` to the local exact
  `kgmicrobe.ingredient` identifier, while its ChEBI row keeps the expected
  `skos:closeMatch` predicate to `CHEBI:34683`.
- Major: `chemical_properties` carries the anhydrous
  `CHEBI:34683` formula, InChI, and molecular weight even though the subject is
  the aqueous 0.02 M stock solution.
- Major: the final ChEBI SSSOM row publishes solute, heptahydrate, and
  dihydrate labels in `other`, including the heptahydrate synonym and two
  active dihydrate labels. None is an exact synonym for the MIM subject, which
  is a prepared 0.02 M stock solution.

## Completeness

- The local stock-solution identifier and the exact local SSSOM row preserve
  the distinction between the stock and the parent anhydrous ChEBI term.
- The one source occurrence is accounted for.
- The record has five dihydrate labels typed as `REJECTED_LABEL`, but two
  dihydrate labels remain active and can still reach the published SSSOM.

## Recommended Edits

- Major: remove or replace the anhydrous formula, InChI, molecular weight, and
  derived ChEBI/PubChem structure payload in
  `data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml`;
  then synchronize `data/curated/mapped_ingredients.yaml`.
- Major: demote the two remaining dihydrate labels and any other non-stock
  solute names that are not true synonyms for the 0.02 M stock solution; then
  regenerate `mappings/ingredient_mappings.sssom.tsv` so the close parent row
  no longer exports them in `other`.
