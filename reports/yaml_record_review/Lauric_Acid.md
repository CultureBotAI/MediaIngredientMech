# `data/ingredients/mapped/Lauric_Acid.yaml`

## Verdict

Pass. The CAS-backed CHEBI:30805 identity, CAS RN, PubChem structure, empty
synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lauric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30805` with
  `ontology_mapping.ontology_id: CHEBI:30805`, label `dodecanoic acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `143-07-7`, molecular formula `C12H24O2`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lapachol` through `Lead_Ii_Nitrate`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lapachol.yaml data/ingredients/mapped/Lauric_Acid.yaml data/ingredients/mapped/Lawsone.yaml data/ingredients/mapped/Lead_Ii_Chloride.yaml data/ingredients/mapped/Lead_Ii_Nitrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:30805` as active `dodecanoic acid`, lists CAS
  `143-07-7`, and lists `Lauric acid` as a related synonym.
- PubChem resolves CAS RN `143-07-7` to CID `3893` with formula `C12H24O2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:30805`; its
  `other` field contains only `CAS:143-07-7`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and a separate `Dodecanoate` anion record, confirming this record denotes
  the neutral acid rather than the dodecanoate conjugate base.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.

## Recommended Edits

- None.
