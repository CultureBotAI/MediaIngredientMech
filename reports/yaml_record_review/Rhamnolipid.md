# `data/ingredients/mapped/Rhamnolipid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rhamnolipid` is CAS-grounded to defining `CHEBI:62570` /
`2-O-alpha-L-rhamnosyl-alpha-L-rhamnosyl-3-hydroxydecanoyl-3-hydroxydecanoic
acid`. Fresh OLS4 lookup resolved the ChEBI CURIE, and PubChem lookup by the
stored CAS `4348-76-9` resolved CID 5458394 with the same formula and InChI as
the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml
data/ingredients/mapped/Rhamnolipid.yaml data/ingredients/mapped/Rhamnose.yaml
data/ingredients/mapped/Rhodinyl_Acetate.yaml
data/ingredients/mapped/Rhodocladonic_Acid.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for this CHEBI record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2499 maps exactly to
`CHEBI:62570`; `CAS:4348-76-9` matches the stored `chemical_properties.cas_rn`,
and the long exported `other` token is already represented as a curated exact
synonym.

The `physicochemical_roles.SURFACTANT` assertion is unsupported: its only
evidence is a `COMPUTATIONAL_PREDICTION` from `infer_roles_from_chebi_ancestry`
with the standard provisional curator note.

**Completeness**: The CAS-backed ChEBI identity, chemical properties, ingredient
type, and final SSSOM row agree. The only active gap is the provisional
surfactant role.

**Recommended Edits**: Either remove `physicochemical_roles.SURFACTANT` or add
source-backed evidence that this exact rhamnolipid is used as a surfactant in
the relevant media context.
