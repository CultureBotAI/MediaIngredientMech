# `data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml`

## Verdict

Needs curation. The CAS fallback identity, close match to `CHEBI:26707`
glycerol phosphate, exact CAS registry row, and parent-row SSSOM payload pass,
but `CARBON_SOURCE` remains an unsupported name-pattern role.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:55073-41-1`, close-mapped to
  `CHEBI:26707` with canonical label `glycerol phosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `55073-41-1`, PubChem CID `14754`, formula
  `C3H7Na2O6P`, InChI, and SMILES
  `C(C(COP(=O)([O-])[O-])O)O.[Na+].[Na+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycerol_Mono-oleate.yaml data/ingredients/mapped/Glycerol_Monostearate.yaml data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Glycine-NaOH_Buffer.yaml data/ingredients/mapped/Glycine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary identifier, close ChEBI mapping, PubChem structure,
  singleton type, provisional carbon-source role, and #342 close-match
  evidence as the per-record YAML.
- OLS4 resolves `CHEBI:26707` as `glycerol phosphate`, matching the YAML
  parent `ontology_mapping`.
- A bounded exact OLS4 search for `Glycerol phosphate disodium salt hydrate`
  under ChEBI found no form-specific term, so the CAS primary identity remains
  the specific identifier available to this record.
- PubChem resolves CAS `55073-41-1` to PubChem CID `14754` with the same
  formula, InChI, and SMILES as the YAML.
- Major: `nutritional_roles.CARBON_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and a provisional
  curator note. No inspected CultureMech, database, or literature evidence
  supports that role for this disodium hydrate record.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Glycerol_Phosphate_Disodium_Salt_Hydrate` to `CHEBI:26707` by
  `skos:closeMatch` and to the record's own `cas:55073-41-1` identifier by
  `skos:exactMatch`; both rows keep only `CAS:55073-41-1` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM rows, row-review TSVs,
  the hydrate anchor plan, and ignored aggregate backups.

## Completeness

- The CAS primary identity, PubChem formula, InChI, SMILES, close ChEBI parent,
  exact CAS SSSOM row, close ChEBI SSSOM row, and ingredient type are
  populated.
- The carbon-source role needs claim-level support or removal.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` from
  `data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml`, or
  replace the provisional name-pattern evidence with inspected source evidence
  that specifically supports this salt hydrate as a carbon source.
