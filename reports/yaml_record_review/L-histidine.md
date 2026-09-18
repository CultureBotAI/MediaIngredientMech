# `data/ingredients/mapped/L-histidine.yaml`

## Verdict

Needs curation. The L-histidine identity, corrected CAS RN, PubChem structure,
claim-level nitrogen-source role, occurrence count, and active ChEBI grounding
pass, but final SSSOM still exports bare `Histidine`, which belongs on the
generic CHEBI:27570 sibling rather than the L-enantiomer row.

## Identity

- Reviewed record: `data/ingredients/mapped/L-histidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15971` with
  `ontology_mapping.ontology_id: CHEBI:15971`, label `L-histidine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `71-00-1`, molecular formula `C6H9N3O2`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:15971` as active `L-histidine` and lists CAS
  `71-00-1`.
- PubChem resolves CAS RN `71-00-1` to CID `6274` with formula `C6H9N3O2` and
  the same InChI as the YAML record.
- The curation history corrected earlier CHEBI contamination to `CHEBI:15971`
  and resolved the merged CAS conflict in favor of the OAK canonical
  `71-00-1` xref.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- Major: the final SSSOM `other` field still exports `Histidine`. EBI OLS4
  exact search resolves bare `Histidine` to `CHEBI:27570`, and this repository
  has a separate `data/ingredients/mapped/Dl-histidine.yaml` record for that
  generic histidine identity.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the generic histidine sibling, and the
  L-histidine hydrochloride monohydrate parent rows.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, and aggregate copy are present and internally
  consistent.
- The final SSSOM synonym surface is incomplete until the generic histidine
  label is removed from this L-enantiomer row.

## Recommended Edits

- Major: remove `Histidine` from
  `data/ingredients/mapped/L-histidine.yaml`; keep the bare label only on the
  existing generic `data/ingredients/mapped/Dl-histidine.yaml` record.
- Sync the aggregate copy and regenerate the SSSOM/docs products so `other`
  stops publishing the cross-stereochemistry synonym; rerun strict, term,
  round-trip, component, and SSSOM validation.
