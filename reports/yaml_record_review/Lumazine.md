# `data/ingredients/mapped/Lumazine.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:16489 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lumazine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16489` with
  `ontology_mapping.ontology_id: CHEBI:16489`, label `lumazine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `487-21-8`, molecular formula `C6H4N4O2`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lovastatin` through `Lupeol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:16489` as active `lumazine`, lists
  `pteridine-2,4-diol` as a synonym, lists CAS `487-21-8`, and records the same
  formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `487-21-8` to CID `10250` with formula `C6H4N4O2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16489`; its
  `other` field contains only the curated ChEBI synonym and `CAS:487-21-8`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
