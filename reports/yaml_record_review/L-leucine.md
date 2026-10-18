# `data/ingredients/mapped/L-leucine.yaml`

## Verdict

Needs curation. The L-leucine identity, CAS RN, PubChem structure, claim-level
nitrogen-source role, occurrence count, and active ChEBI grounding pass, but
final SSSOM still exports ambiguous bare `Leucine`.

## Identity

- Reviewed record: `data/ingredients/mapped/L-leucine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15603` with
  `ontology_mapping.ontology_id: CHEBI:15603`, label `L-leucine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `61-90-5`, molecular formula `C6H13NO2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:15603` as active `L-leucine` and lists CAS
  `61-90-5`.
- PubChem resolves CAS RN `61-90-5` to CID `6106` with formula `C6H13NO2` and
  the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- Major: final SSSOM `other` still exports bare `Leucine`. EBI OLS4 exact
  search returns a generic `CHEBI:25017` leucine class for that string, so the
  bare label is ambiguous across stereochemical forms and should not be
  exported as an exact synonym of the L-enantiomer.
- The remaining final synonyms came from kg-microbe enrichment for the
  L-leucine row and do not cross an inspected stereochemical or salt boundary.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and component references from multicomponent
  amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, and aggregate copy are present and internally
  consistent.
- The final SSSOM synonym surface is incomplete until the generic leucine label
  is removed from this L-enantiomer row.

## Recommended Edits

- Major: remove or demote `Leucine` in
  `data/ingredients/mapped/L-leucine.yaml`; keep the exact synonym surface
  specific to `CHEBI:15603`.
- Sync the aggregate copy and regenerate the SSSOM/docs products so `other`
  stops publishing the cross-stereochemistry synonym; rerun strict, term,
  round-trip, component, and SSSOM validation.
