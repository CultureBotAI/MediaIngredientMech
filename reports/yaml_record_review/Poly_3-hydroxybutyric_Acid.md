# `data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Poly(3-hydroxybutyric acid)` is preserved as the CAS identity `cas:29435-48-1`, but its parent row maps it as narrower than `CHEBI:20067` / `3-hydroxybutyric acid`. That CHEBI target denotes the monomer acid, not the polymer/oligomer CAS object: PubChem CID 71311208 confirms the stored `C12H20O6` structure for CAS `29435-48-1`, and its synonym list includes `Poly((R)-(-)-3-hydroxybutyrate)` rather than the monomer identity.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly_3-hydroxybutyric_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored CHEBI label even though the parent target is semantically wrong.

**Evidence**: The final SSSOM rows correctly add exact registry siblings for the CAS and KG-Microbe identities required by the `NARROW_MATCH` record, and `CAS:29435-48-1` is a valid `other` token for those exact rows. Row 2358, however, points at the monomer `3-hydroxybutyric acid`, and its `other` value exports `3-hydroxybutanoic acid`, a synonym of the monomer rather than the polymer/oligomer subject. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, alias, and final SSSOM references.

**Completeness**: The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Recommended Edits**: Re-curate `data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml` so the parent mapping no longer treats the polymer/oligomer as a child of monomeric `CHEBI:20067`; either map it exactly to the appropriate PHB polymer term or preserve the CAS identity with a chemically valid parent. Remove the monomer-only `3-hydroxybutanoic acid` active synonym, and either replace the provisional `CARBON_SOURCE` evidence with source-backed evidence scoped to this form or remove the role. Then regenerate the SSSOM rows and run strict validation plus `scripts/validate_sssom_invariants.py`.
