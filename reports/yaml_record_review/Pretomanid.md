# `data/ingredients/mapped/Pretomanid.yaml`

**Verdict**: pass.

**Identity**: `Pretomanid` is preserved as exact CAS `187235-37-6` with a parent `NARROW_MATCH` to active `NCIT:C166606` / `Pretomanid`. PubChem CID 456199 confirms the stored formula, SMILES, and InChI for the CAS identity.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pretomanid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pretomanid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored NCIT label.

**Evidence**: The NCIT term still resolves by exact label, and final SSSOM rows 2417-2419 keep the non-CHEBI parent together with exact `cas:187235-37-6` and `kgmicrobe.compound:pretomanid` identity rows. The final `CAS:187235-37-6` tokens match `chemical_properties.cas_rn`.

**Completeness**: The record has no active roles, components, or synonyms that overstate the CAS/NCIT identity. The local exact row preserves the supplied chemical form beside the broader registry parent.

**Recommended Edits**: None.
