# `data/ingredients/mapped/R-3-hydroxybutyrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `(R)-3-hydroxybutyrate` now maps to the stereospecific
`CHEBI:10983` term after `fix_stereoisomer_remaps`; the exact identity and the
final SSSOM `skos:exactMatch` row are correct. Fresh OLS4 lookup resolved
`CHEBI:10983` as `(R)-3-hydroxybutyrate`, and an exact OLS4 synonym lookup
resolved `(3R)-3-hydroxybutanoate` back to the same ChEBI term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Quinoline.yaml
data/ingredients/mapped/R-3-hydroxybutyrate.yaml
data/ingredients/mapped/R2A_agar.yaml
data/ingredients/mapped/Rabbit_Blood.yaml
data/ingredients/mapped/Rabbit_Serum.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for this CHEBI record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row, and final SSSOM row 2480 has the
right exact CHEBI target plus only the true ChEBI synonym
`(3R)-3-hydroxybutanoate` in `other`. PubChem lookup by the stereospecific name
resolved CID 6971058 with an isomeric SMILES of `C[C@H](CC(=O)[O-])O`, but the
stored `chemical_properties.smiles` and `chemical_properties.inchi` still lack
the chiral center after the earlier achiral `CHEBI:37054` mapping was repaired.

The `nutritional_roles.CARBON_SOURCE` assertion is also unsupported: its only
evidence is a `COMPUTATIONAL_PREDICTION` from
`infer_roles_from_name_lists` with the standard provisional curator note.

**Completeness**: Occurrence statistics are empty, no components or supplied
forms are asserted, and the published SSSOM synonym is clean. The consequential
gaps are the stale achiral structure fields and the provisional role.

**Recommended Edits**: Refresh `chemical_properties` from the stereospecific
`CHEBI:10983` or PubChem CID 6971058 structure, preserving the chiral SMILES and
InChI. Then either remove `nutritional_roles.CARBON_SOURCE` or replace the
name-list prediction with source-backed evidence for this exact anion, sync the
aggregate copy, and regenerate final SSSOM if any exported fields change.
