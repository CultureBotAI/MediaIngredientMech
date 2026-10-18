# `data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium aluminum chloride` is preserved as CAS `74978-20-4`, with exact CAS and KG-Microbe registry rows in final SSSOM rows 2389 and 2390. The non-exact parent row, however, maps the subject to `NCIT:C83530` / `Aluminum Chloride` from a stem-substring match that drops `Potassium` from the source label.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Aluminum_Chloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the NCIT parent label.

**Evidence**: The CAS and KG-Microbe exact rows preserve the unresolved salt identity, but the `NCIT:C83530` parent row is only substring-derived and does not establish that potassium aluminum chloride is a narrower class of aluminum chloride. PubChem lookup by CAS `74978-20-4` found no CID to corroborate the CAS subject or the `AlKCl2` synonym. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected final parent row, registry sibling rows, and row-review triage records.

**Completeness**: The salt is missing source-backed structure fields and a chemically checked parent. The exact registry rows make the subject publishable, but the NCIT parent should not be treated as reviewed chemical grounding yet.

**Recommended Edits**: Re-curate `data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml`: verify CAS `74978-20-4`, formula `AlKCl2`, and the intended source form against an inspected registry source, then replace or remove the `NCIT:C83530` parent if no source supports an aluminum-chloride parent relation. Regenerate SSSOM and re-run strict validation plus `scripts/validate_sssom_invariants.py`.
