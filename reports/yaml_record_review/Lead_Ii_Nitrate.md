# `data/ingredients/mapped/Lead_Ii_Nitrate.yaml`

## Verdict

Pass. The CAS-backed CHEBI:37187 identity, CAS RN, PubChem structure, reviewed
synonyms, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lead_Ii_Nitrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:37187` with
  `ontology_mapping.ontology_id: CHEBI:37187`, label `lead nitrate`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `10099-74-8`, molecular formula `N2O6Pb`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lapachol` through `Lead_Ii_Nitrate`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lapachol.yaml data/ingredients/mapped/Lauric_Acid.yaml data/ingredients/mapped/Lawsone.yaml data/ingredients/mapped/Lead_Ii_Chloride.yaml data/ingredients/mapped/Lead_Ii_Nitrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:37187` as active `lead nitrate`, lists CAS
  `10099-74-8`, and lists `lead(II) nitrate` as an exact IUPAC synonym.
- PubChem resolves CAS RN `10099-74-8` to CID `24924` with formula `N2O6Pb` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:37187`; its
  `other` field contains reviewed IUPAC synonyms plus `CAS:10099-74-8`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lead nitrate
  identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, synonyms,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
