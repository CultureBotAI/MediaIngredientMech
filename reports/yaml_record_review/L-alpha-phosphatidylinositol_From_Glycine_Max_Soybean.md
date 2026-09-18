# `data/ingredients/mapped/L-α-phosphatidylinositol_From_Glycine_Max_Soybean.yaml`

## Verdict

Needs curation. The CAS-primary identity, close phosphatidylinositol class
grounding, exact CAS registry row, and final SSSOM output are directionally
correct for a soybean phosphatidylinositol mixture, but the YAML still
classifies the ingredient as a single ingredient with one PubChem structure.

## Identity

- Reviewed record: the Greek-letter soybean phosphatidylinositol YAML in
  `data/ingredients/mapped`.
- Identifier and grounding: `identifier: cas:97281-52-2` with
  `ontology_mapping.ontology_id: CHEBI:28874`, label
  `phosphatidylinositol`, source `CHEBI`,
  `mapping_quality: BROAD_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `97281-52-2`, molecular formula `C45H87O13P`,
  InChI, SMILES, and PubChem CID `15488999`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `L-valine` through `L_-tartaric_Acid`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-valine.yaml data/ingredients/mapped/LL-37.yaml data/ingredients/mapped/L_-tartaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records. Engine A term validation was
  skipped for this CAS-primary record because its primary ID is outside the
  CHEBI/OBO prefix scope.

## Evidence

- EBI OLS4 resolves `CHEBI:28874` as active `phosphatidylinositol`, a broader
  class for glycerophosphoinositols with one phosphatidyl group.
- PubChem resolves CAS RN `97281-52-2` to CID `15488999` with formula
  `C45H87O13P` and the same InChI as the YAML record.
- The `fix_id_label_correspondence` evidence explains that the commercial
  soybean product is a natural phosphatidylinositol mixture, has no
  single-structure CHEBI class, and should remain under its CAS primary ID with
  a broad parent match to CHEBI:28874 instead of being promoted to a CHEBI
  identifier.
- The final SSSOM preserves that identity as a `skos:closeMatch` row to
  `CHEBI:28874` plus a separate `skos:exactMatch` row to the
  `cas:97281-52-2` registry term.
- Major: the record-level evidence says the ingredient is a natural soybean
  mixture, but `ingredient_type: SINGLE_INGREDIENT` and the backfilled
  `chemical_properties` block capture one PubChem structure as though the
  supplied ingredient were a single phosphatidylinositol species.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM rows, and docs projections.

## Completeness

- The CAS identity, broad chemical-class parent, aggregate copy, and final
  SSSOM rows are present and consistent.
- The record is incomplete until its type and chemistry match the maintained
  mixture judgement instead of the representative PubChem structure.

## Recommended Edits

- Major: set the soybean phosphatidylinositol record back to
  `ingredient_type: UNDEFINED_MIXTURE` or another mixture type that matches the
  maintained CAS identity, and remove or qualify the single-species PubChem
  formula/InChI/SMILES so they are not asserted as the exact supplied mixture.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
