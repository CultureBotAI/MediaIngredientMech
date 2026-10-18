# `data/ingredients/mapped/Sarcosine.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `sarcosine` maps exactly to active, defining `CHEBI:15611` /
`sarcosine`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved
`107-97-1`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sarcidin.yaml data/ingredients/mapped/Sarcosine.yaml
data/ingredients/mapped/Sclareolide.yaml
data/ingredients/mapped/Scopoletin.yaml
data/ingredients/mapped/Sea_Salts.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Sarcosine`, `Sclareolide`,
`Scopoletin`, and `Sea_Salts`; the `kgmicrobe.compound` placeholder is outside
Engine A coverage.

**Evidence**: The exact CHEBI identity, CAS, structure fields, and final SSSOM
row pass. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`. Final SSSOM row 2560 maps exactly to
`CHEBI:15611` and exports only `CAS:107-97-1` in `other`.

The record still has a provisional `AMINO_ACID_SOURCE` role inferred from CHEBI
ancestry. Its only role evidence is `COMPUTATIONAL_PREDICTION`, and the
curator note explicitly says the role is provisional and needs review. That is
not enough support for a nutritional role facet on this otherwise exact
single-ingredient record.

**Completeness**: No components or curated synonyms are asserted. The chemical
identity is complete, but the role facet needs source-backed curation or
removal.

**Recommended Edits**: Revisit `nutritional_roles` for `sarcosine`. Replace
the inherited `AMINO_ACID_SOURCE` assertion with source-backed role evidence if
recipes actually use sarcosine that way, or remove the provisional role and
regenerate downstream role exports.
