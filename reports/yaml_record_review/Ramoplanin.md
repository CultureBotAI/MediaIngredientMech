# `data/ingredients/mapped/Ramoplanin.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Ramoplanin` maps exactly to defining `CHEBI:29670` /
`Ramoplanin`. The OLS4 term details and PubChem lookup by `CHEBI:29670` both
resolve the `C119H154ClN21O40` structure already stored in YAML, so the ChEBI
identity and structure are sound.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml
data/ingredients/mapped/Racemomycin_E.yaml data/ingredients/mapped/Radicicol.yaml
data/ingredients/mapped/Raffinose.yaml data/ingredients/mapped/Ramoplanin.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row, and final SSSOM row 2492 maps
`MIM:Ramoplanin` exactly to `CHEBI:29670`. However, the stored CAS
`76168-82-6` is not the CAS carried by ChEBI for this term: `CHEBI:29670`
cross-references `81988-88-7`, which PubChem resolves to the same CID 16129628
and the same InChI as the YAML, while `76168-82-6` resolves to a different
PubChem CID with formula `C106H170ClN21O30`.

**Completeness**: The exact ontology grounding, structure, and ingredient type
are populated; the unsafe payload is the stale CAS copied from CultureBotHT into
`chemical_properties.cas_rn` and final SSSOM `other`.

**Recommended Edits**: Replace `chemical_properties.cas_rn: 76168-82-6` with the
verified `CHEBI:29670` cross-reference `81988-88-7`, record the ChEBI/PubChem
evidence in curation history, sync `data/curated/mapped_ingredients.yaml`, and
regenerate the final SSSOM so `CAS:76168-82-6` is no longer published.
