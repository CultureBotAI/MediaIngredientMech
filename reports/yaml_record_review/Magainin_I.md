# `data/ingredients/mapped/Magainin_I.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:201898 identity, CAS RN, ChEBI structure,
exact ChEBI IUPAC synonym, aggregate copy, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Magainin_I.yaml`.
- Identifier and grounding: `identifier: CHEBI:201898` with
  `ontology_mapping.ontology_id: CHEBI:201898`, label `Magainin I`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `108433-99-4`, molecular formula
  `C112H177N29O28S`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Macro_Component_2_For_J_Medium` through `Magnesium`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  CHEBI-primary subset `Macrolide_Antibiotic`, `Magainin_I`, `Magnesium(2)`,
  and `Magnesium`; `Macro_Component_2_For_J_Medium` was skipped because its
  primary identifier uses a local prefix outside the CHEBI/OBO term adapter
  scope.

## Evidence

- EBI OLS4 resolves `CHEBI:201898` as active `Magainin I` and records the same
  formula, InChI, SMILES, and exact IUPAC synonym as the YAML record.
- PubChem resolves CAS RN `108433-99-4` to multiple CIDs, so ChEBI is the
  supporting structure source for this record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:201898`; its
  `other` field contains the curated IUPAC synonym and `CAS:108433-99-4`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
