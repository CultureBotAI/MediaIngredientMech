# `data/ingredients/mapped/Lead_Ii_Chloride.yaml`

## Verdict

Pass. The CAS-backed CHEBI:88212 identity, CAS RN, PubChem structure, reviewed
synonyms, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lead_Ii_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:88212` with
  `ontology_mapping.ontology_id: CHEBI:88212`, label `lead(II) chloride`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7758-95-4`, molecular formula `Cl2Pb`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lapachol` through `Lead_Ii_Nitrate`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lapachol.yaml data/ingredients/mapped/Lauric_Acid.yaml data/ingredients/mapped/Lawsone.yaml data/ingredients/mapped/Lead_Ii_Chloride.yaml data/ingredients/mapped/Lead_Ii_Nitrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:88212` as active `lead(II) chloride`, lists CAS
  `7758-95-4`, and lists the same InChI as the YAML record.
- PubChem resolves CAS RN `7758-95-4` to CID `24459` with formula `Cl2Pb` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:88212`; its
  `other` field contains reviewed IUPAC synonyms plus `CAS:7758-95-4`.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lead chloride
  identity.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, synonyms,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
