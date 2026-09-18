# `data/ingredients/mapped/Shikimic_Acid.yaml`

**Verdict**: needs curation, major issues.

**Identity**: `Shikimic Acid` maps exactly to active, defining `CHEBI:16119` /
`shikimic acid`. Fresh OLS4 lookup resolved the ChEBI term, and its CAS RN
`138-59-0`, formula, InChI, and PubChem CID 8742 all agree with the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sheep_blood.yaml
data/ingredients/mapped/Shikimic_Acid.yaml
data/ingredients/mapped/Showdomycin.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_A.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_C.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sheep_blood` was skipped because
`MICRO` is outside the Engine A CHEBI/OBO term-validation subset.

**Evidence**: The CAS-RN lookup, exact CHEBI identity, structure fields, and CAS
field pass. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`.

Two material assertions need curation. `Shikimate` is not an exact synonym of
`CHEBI:16119`: fresh OLS4 lookup resolves `shikimate` to separate active term
`CHEBI:36208`, a conjugate base of shikimic acid, and ChEBI lists `Shikimate`
on `CHEBI:16119` only as a related synonym. Keeping that token as an
`EXACT_SYNONYM` makes final SSSOM row 2576 export the anion name in `other` for
the acid record. The `CARBON_SOURCE` role is also only a
`COMPUTATIONAL_PREDICTION` from a curated name pattern, and its curator note
explicitly says the assertion is provisional and needs review.

**Completeness**: The exact acid identity, CAS field, and chemical structure
are present. The incorrect conjugate-base synonym should be removed or
demoted, and the carbon-source role needs source-backed curation or removal.

**Recommended Edits**: Remove or demote `Shikimate` from
`data/ingredients/mapped/Shikimic_Acid.yaml`, then rebuild final SSSOM and
confirm row 2576 no longer exports it as `other`. Replace the provisional
`CARBON_SOURCE` role with source-backed evidence, or remove it if no
MediaIngredientMech source supports using shikimic acid as a carbon source.
