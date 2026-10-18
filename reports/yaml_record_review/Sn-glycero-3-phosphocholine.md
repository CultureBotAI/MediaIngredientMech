# `data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `sn-glycero-3-phosphocholine` maps exactly to active, defining
`CHEBI:16870` / `choline alfoscerate`. Fresh OLS4 lookup resolved the ChEBI
term, and PubChem resolves CAS RN `28319-77-9` to CID 657272 with a formula and
InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sludge.yaml
data/ingredients/mapped/Sludge_fluid.yaml
data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml
data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the ENVO and
3 CHEBI files; `Sludge_fluid` was skipped because `MICRO` is outside the Engine
A OBO term-validation subset.

**Evidence**: The CAS-RN lookup, exact CHEBI identity, CAS field, structure
fields, occurrence counts, and component use in `NLDM_metabolites` pass. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`.

The final SSSOM row needs synonym cleanup. Row 2604 exports a large
kg-microbe-derived synonym set as `other`, but fresh OLS4 lookup lists only two
of the non-CAS exported tokens as exact ChEBI synonyms. The remaining exported
names are related synonyms and need exact-scope review before publication.

**Completeness**: The exact CHEBI identity, CAS field, structure fields,
occurrence counts, and final SSSOM subject agree. The exported synonym set
needs pruning to exact synonyms plus `CAS:28319-77-9`.

**Recommended Edits**: Remove or demote non-exact kg-microbe synonyms from
`data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml`, then rebuild final
SSSOM and confirm row 2604 exports only exact synonyms plus the CAS token.
