# `data/ingredients/mapped/Sclareolide.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sclareolide` is represented as exact CAS `564-20-5` with a
`NARROW_MATCH` parent to `mesh:C109395` / `sclareolide`. Fresh OLS4 exact
search still resolved the MeSH parent and did not find a ChEBI replacement.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sarcidin.yaml data/ingredients/mapped/Sarcosine.yaml
data/ingredients/mapped/Sclareolide.yaml
data/ingredients/mapped/Scopoletin.yaml
data/ingredients/mapped/Sea_Salts.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Sarcosine`, `Sclareolide`,
`Scopoletin`, and `Sea_Salts`; the `kgmicrobe.compound` placeholder is outside
Engine A coverage.

**Evidence**: The parent MeSH mapping and the three final SSSOM rows have the
right broad shape: row 2561 keeps the MeSH parent as `skos:narrowMatch`, row
2562 preserves exact `cas:564-20-5`, and row 2563 keeps the exact kg-microbe
registry sibling required by Rule B1. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`.

The local PubChem structure is stale or under-specified for the CAS identity.
Fresh PubChem lookup of `564-20-5` resolved stereospecific CID `929262` and
the stereospecific InChI; the YAML still stores achiral CID `61129` and the
achiral InChI/SMILES. CID `61129` lacks `564-20-5` and instead carries
`1216-84-8`, while CID `929262` carries `Sclareolide`, `564-20-5`, and the
defined stereochemistry.

**Completeness**: The CAS and kg-microbe final exact rows correctly preserve
local identity beside the MeSH parent, but the local `chemical_properties`
block no longer matches the CAS registry identity precisely.

**Recommended Edits**: Recheck the original CultureBotHT CAS source. If it
intended `564-20-5`, update `chemical_properties.pubchem_cid` to `929262` and
replace the achiral InChI/SMILES with the stereospecific PubChem values before
regenerating downstream exports.
