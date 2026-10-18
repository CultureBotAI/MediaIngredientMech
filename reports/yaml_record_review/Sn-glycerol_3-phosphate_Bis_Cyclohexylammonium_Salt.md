# `data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`

**Verdict**: needs curation, major issues.

**Identity**: `sn-Glycerol 3-phosphate bis(cyclohexylammonium) salt` is a
CAS-primary salt record with a curated narrow match to active parent
`CHEBI:15978` / `sn-glycerol 3-phosphate`. Fresh PubChem lookup resolves CAS RN
`29849-82-9` to CID 16219444 with a formula and InChI matching the record.
Fresh OLS4 searches by the CAS RN and full salt label found no exact ChEBI term
for the bis(cyclohexylammonium) salt.

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

**Evidence**: The narrow free-acid parent, exact CAS registry row, exact
kg-microbe registry row, and expected row-review `UNKNOWN_TERM`
classifications pass. The per-record YAML agrees with the regenerated aggregate
row when keyed by `(identifier, preferred_term)`.

Two assertions need curation. Final SSSOM row 2605 exports
`Glycerol 3-phosphate`, `(2R)-2,3-dihydroxypropyl dihydrogen phosphate`, and
`sn-glycerol 3-(dihydrogen phosphate)` as `other` for the bis salt. Those are
free-acid parent names, not exact salt synonyms. The `CARBON_SOURCE` role is
also only a `COMPUTATIONAL_PREDICTION` from a name pattern, and its curator note
explicitly says the assertion is provisional and needs review.

**Completeness**: Final SSSOM rows 2606-2607 correctly preserve the exact CAS
and kg-microbe registry identity rows. The broader-parent synonyms should be
removed from the salt subject, and the carbon-source role needs source-backed
curation or removal.

**Recommended Edits**: Remove the free-acid synonyms from
`data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
and from any generator-side synonym source that injects `Glycerol 3-phosphate`
into the narrow parent row, then rebuild final SSSOM and confirm row 2605 no
longer exports free-acid names. Replace the provisional `CARBON_SOURCE` role
with source-backed evidence, or remove it if no MediaIngredientMech source
supports using the bis salt as a carbon source.
