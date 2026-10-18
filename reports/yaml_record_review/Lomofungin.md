# `data/ingredients/mapped/Lomofungin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:224243 identity, active ChEBI/PubChem
structure, empty synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lomofungin.yaml`.
- Identifier and grounding: `identifier: CHEBI:224243` with
  `ontology_mapping.ontology_id: CHEBI:224243`, label `Lomofungin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C15H10N2O6`, InChI, SMILES, and
  molecular weight from ChEBI and PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Locust_Bean_Gum` through `Loratadine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:224243` as active `Lomofungin`, records formula
  `C15H10N2O6`, and records the same InChI and SMILES as the YAML record.
- PubChem resolves the name `lomofungin` to CID `33612` with formula
  `C15H10N2O6` and the same InChI as the YAML record.
- The MicrobeDecoder occurrence is retained in `source_occurrences` as one
  `BacDive_Metabolite_production` import, while `total_occurrences` and
  `media_count` correctly remain zero for the media-recipe corpus.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:224243` and has
  an empty `other` field.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
