# `data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Simvastatin Hydroxy Acid Ammonium Salt` is a CAS-primary salt
record with a curated narrow match to active parent `CHEBI:169041` /
`simvastatin hydroxy acid`. Fresh PubChem lookup resolves CAS RN `139893-43-9`
to CID 10961424, and PubChem's formula and InChI agree with the ammonium-salt
record. Fresh OLS4 searches by the CAS RN and full salt label found no exact
ChEBI term for the ammonium salt.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Simvastatin.yaml
data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml
data/ingredients/mapped/Sinapic_Acid.yaml
data/ingredients/mapped/Sinapinaldehyde.yaml
data/ingredients/mapped/Sinomenine.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CAS fallback identity, PubChem structure fields,
`skos:narrowMatch` parent row, exact CAS registry row, exact kg-microbe registry
row, and expected row-review `UNKNOWN_TERM` classifications pass. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`.

The remaining issue is the curated synonym. The YAML stores the systematic name
of the free acid, and fresh OLS4 lookup confirms that ChEBI lists that string as
an exact synonym of parent `CHEBI:169041`, not of the ammonium salt. Final SSSOM
row 2586 exports that broader-parent acid synonym in `other` for
`MIM:Simvastatin_Hydroxy_Acid_Ammonium_Salt`, which erases the ammonium-salt
boundary even though the predicate is correctly narrow.

**Completeness**: Final SSSOM rows 2586-2588 correctly preserve the narrow
parent mapping plus CAS and kg-microbe exact registry identity rows. The
broader-parent exact synonym should be removed from the salt subject.

**Recommended Edits**: Remove the free-acid systematic synonym from
`data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml`, then
rebuild final SSSOM and confirm row 2586 no longer exports it as `other`.
