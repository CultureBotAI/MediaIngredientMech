# `data/ingredients/mapped/Leucodin.yaml`

## Verdict

Pass. The CAS-backed CHEBI:4441 identity, CAS RN, PubChem structure, empty
synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Leucodin.yaml`.
- Identifier and grounding: `identifier: CHEBI:4441` with
  `ontology_mapping.ontology_id: CHEBI:4441`, label `Desacetoxymatricarin`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `17946-87-1`, molecular formula `C15H18O3`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lecithin` through `Leucodin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lecithin.yaml data/ingredients/mapped/Lentilan_From_Mushroom.yaml data/ingredients/mapped/Leucodin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:4441` as active `Desacetoxymatricarin`, lists
  `Leucodin` as a related synonym, and lists CAS `17946-87-1`.
- PubChem resolves CAS RN `17946-87-1` to CID `167683` with formula `C15H18O3`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:4441`; its
  `other` field contains only `CAS:17946-87-1`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same leucodin identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
