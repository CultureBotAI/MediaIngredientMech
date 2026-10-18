# `data/ingredients/mapped/Lupeol.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:6570 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lupeol.yaml`.
- Identifier and grounding: `identifier: CHEBI:6570` with
  `ontology_mapping.ontology_id: CHEBI:6570`, label `lupeol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `545-47-1`, molecular formula `C30H50O`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lovastatin` through `Lupeol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:6570` as active `lupeol`, lists
  `(3beta)-lup-20(29)-en-3-ol` as a synonym, lists CAS `545-47-1`, and records
  the same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `545-47-1` to CID `259846` with formula `C30H50O` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6570`; its
  `other` field contains only the curated ChEBI synonym and `CAS:545-47-1`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
