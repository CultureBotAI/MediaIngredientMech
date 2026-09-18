# `data/ingredients/mapped/L-glutamic_Acid.yaml`

## Verdict

Needs curation. The free L-glutamic acid identity, CAS RN, PubChem structure,
claim-level nitrogen-source role, occurrence count, and most synonyms pass,
but final SSSOM still exports `L-Glutamate`, which belongs to the charged
monoanion CHEBI:29985.

## Identity

- Reviewed record: `data/ingredients/mapped/L-glutamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16015` with
  `ontology_mapping.ontology_id: CHEBI:16015`, label `L-glutamic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-86-0`, molecular formula `C5H9NO4`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16015` as active `L-glutamic acid` and lists CAS
  `56-86-0`.
- PubChem resolves CAS RN `56-86-0` to CID `33032` with formula `C5H9NO4` and
  the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- Major: the final SSSOM `other` field still exports `L-Glutamate`. EBI OLS4
  exact search resolves `L-glutamate` to `CHEBI:29985`
  `L-glutamate(1-)`, not to neutral free-acid `CHEBI:16015`.
- The remaining final synonyms came from ChEBI or kg-microbe enrichment for
  the neutral L-glutamic acid row and do not cross an inspected stereochemical
  or salt boundary.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the separate generic glutamic acid sibling, and
  the L-glutamic acid monopotassium salt hydrate parent row.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, and aggregate copy are present and internally
  consistent.
- The final SSSOM synonym surface is incomplete until the charged L-glutamate
  label is removed from this neutral free-acid row.

## Recommended Edits

- Major: remove or demote `L-Glutamate` in
  `data/ingredients/mapped/L-glutamic_Acid.yaml`; keep that label for the
  charged L-glutamate identity.
- Sync the aggregate copy and regenerate the SSSOM/docs products so `other`
  stops publishing the cross-charge synonym; rerun strict, term, round-trip,
  component, and SSSOM validation.
