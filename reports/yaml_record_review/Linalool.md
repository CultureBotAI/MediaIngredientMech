# `data/ingredients/mapped/Linalool.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:17580 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Linalool.yaml`.
- Identifier and grounding: `identifier: CHEBI:17580` with
  `ontology_mapping.ontology_id: CHEBI:17580`, label `linalool`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `78-70-6`, molecular formula `C10H18O`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lignin_Alkali` through `Lincomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Limonin.yaml`, `Linalool.yaml`, and `Lincomycin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:17580` as active `linalool`, lists
  `3,7-Dimethylocta-1,6-dien-3-ol` as a synonym, lists CAS `78-70-6`, and
  records the same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `78-70-6` to CID `6549` with formula `C10H18O` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17580`; its
  `other` field contains only the curated ChEBI synonym and `CAS:78-70-6`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
