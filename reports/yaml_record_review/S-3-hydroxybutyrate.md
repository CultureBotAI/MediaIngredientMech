# `data/ingredients/mapped/S-3-hydroxybutyrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `(S)-3-hydroxybutyrate` maps exactly to active, defining
`CHEBI:11047` / `(S)-3-hydroxybutyrate`. Fresh OLS4 lookup resolved the ChEBI
term and confirmed `(3S)-3-hydroxybutanoate` as a ChEBI exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rutilantinone.yaml
data/ingredients/mapped/Rutin.yaml data/ingredients/mapped/Rye-bran.yaml
data/ingredients/mapped/S-3-hydroxybutyrate.yaml
data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` crashed on CAS-primary rows in the mixed batch; rerunning it on this
batch's CHEBI/FOODON subset passed.

**Evidence**: The curation history correctly remapped this record from
achiral `CHEBI:37054` to stereospecific `CHEBI:11047`, and final SSSOM row
2542 now maps exactly to CHEBI:11047 with only the exact ChEBI IUPAC synonym in
`other`. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`.

Two asserted fields still need curation. First, the local `chemical_properties`
block still carries achiral CHEBI:37054-derived structure strings: fresh OLS4
shows that CHEBI:11047 adds a `t3-` stereochemistry layer to the InChI and an
`@` center to the SMILES that the YAML lacks. Second, `nutritional_roles` still
asserts `CARBON_SOURCE` from a provisional name-pattern
`COMPUTATIONAL_PREDICTION`; there is no source-specific evidence that this
particular ingredient occurrence was used as a carbon source.

**Completeness**: The exact ChEBI identity and final SSSOM row are sound, but
the structure and role facets lag the stereoisomer remap and role-evidence
review.

**Recommended Edits**: In
`data/ingredients/mapped/S-3-hydroxybutyrate.yaml`, replace the achiral
`chemical_properties.inchi` and `chemical_properties.smiles` with the exact
CHEBI:11047 values, and either provide source evidence for the `CARBON_SOURCE`
role or remove that provisional facet. Regenerate final SSSOM after the YAML
repair.
