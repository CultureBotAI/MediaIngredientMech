# `data/ingredients/mapped/Limonin.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:16226 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Limonin.yaml`.
- Identifier and grounding: `identifier: CHEBI:16226` with
  `ontology_mapping.ontology_id: CHEBI:16226`, label `limonin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1180-71-8`, molecular formula `C26H30O8`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lignin_Alkali` through `Lincomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Limonin.yaml`, `Linalool.yaml`, and `Lincomycin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:16226` as active `limonin`, lists the long IUPAC
  synonym carried by the YAML record, lists CAS `1180-71-8`, and records the
  same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `1180-71-8` to CID `179651` with formula `C26H30O8`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16226`; its
  `other` field contains only the curated ChEBI synonym and `CAS:1180-71-8`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
