# `data/ingredients/mapped/Lapachol.yaml`

## Verdict

Pass. The exact CHEBI:6377 identity, CAS RN, ChEBI structure, reviewed synonym,
and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lapachol.yaml`.
- Identifier and grounding: `identifier: CHEBI:6377` with
  `ontology_mapping.ontology_id: CHEBI:6377`, label `lapachol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `84-79-7`, molecular formula `C15H14O3`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lapachol` through `Lead_Ii_Nitrate`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lapachol.yaml data/ingredients/mapped/Lauric_Acid.yaml data/ingredients/mapped/Lawsone.yaml data/ingredients/mapped/Lead_Ii_Chloride.yaml data/ingredients/mapped/Lead_Ii_Nitrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:6377` as active `lapachol`, lists CAS `84-79-7`,
  and lists the same InChI as the YAML record.
- PubChem resolves CAS RN `84-79-7` to a naphthoquinone CID with formula
  `C15H14O3`; its InChI differs by tautomeric hydrogen placement from the CHEBI
  structure.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6377`; its
  `other` field contains the reviewed IUPAC synonym plus `CAS:84-79-7`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lapachol identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, ChEBI structure block, synonym,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
