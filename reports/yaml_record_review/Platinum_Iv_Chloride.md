# `data/ingredients/mapped/Platinum_Iv_Chloride.yaml`

**Verdict**: pass.

**Identity**: `platinum (IV) chloride` is preserved as the CAS-registry identity `cas:13454-96-1` after CultureBotHT import, with `Cl4Pt`, `Cl[Pt](Cl)(Cl)Cl`, and the matching InChI from PubChem CID 26031. The identifier, `chemical_properties.cas_rn`, `FALLBACK_REGISTRY` mapping, PubChem CID, and final SSSOM row 2348 all denote platinum tetrachloride.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Platinum_Iv_Chloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. Engine A term validation was skipped intentionally because `cas` is a non-OBO registry prefix covered by product validation rather than `linkml-term-validator` OAK lookup.

**Evidence**: PubChem CID 26031 confirmed the stored formula, connectivity SMILES, InChI, and CAS synonym `13454-96-1`. Fresh exact CHEBI OLS lookups for `13454-96-1` and `platinum tetrachloride` returned no CHEBI documents, which is consistent with the fallback CAS decision. The final SSSOM row uses a CAS exact row with `CAS:13454-96-1` in `other`; that token is allowed because it restates the record's own `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The record has the CAS number, formula, structure strings, PubChem CID, and no unsupported active synonyms or roles. No component block is expected for this single defined compound.

**Recommended Edits**: None.
