# `data/ingredients/mapped/Rhodocladonic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rhodocladonic Acid` maps exactly to defining `CHEBI:144215` /
`Rhodocladonic acid`. Fresh OLS4 lookup resolved the ChEBI CURIE, and detailed
ChEBI term annotations match the formula, SMILES, and InChI stored in YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml
data/ingredients/mapped/Rhamnolipid.yaml data/ingredients/mapped/Rhamnose.yaml
data/ingredients/mapped/Rhodinyl_Acetate.yaml
data/ingredients/mapped/Rhodocladonic_Acid.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for this CHEBI record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row, and final SSSOM row 2502 maps
exactly to `CHEBI:144215`. The structure is supported by ChEBI, but the stored
CultureBotHT CAS `26984-15-6` is not supported by either PubChem lookup or the
ChEBI term's own cross-references, so the final `CAS:26984-15-6` token is not a
verified synonym for the MIM subject.

**Completeness**: The exact ChEBI identity, structure, and ingredient type are
populated. The only unsafe payload is the unverified CAS.

**Recommended Edits**: Remove `chemical_properties.cas_rn: 26984-15-6` and let
the next SSSOM rebuild drop `CAS:26984-15-6`, unless an inspected authoritative
registry verifies that CAS for this exact ChEBI term.
