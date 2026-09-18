# `data/ingredients/mapped/Rutilantinone.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rutilantinone` is represented as a CAS fallback
`cas:21288-61-9`. PubChem resolves `21288-61-9` to a CID that lists
`Rutilantinone`, and the CAS identifier in the record, `chemical_properties`,
and final SSSOM row agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rutilantinone.yaml
data/ingredients/mapped/Rutin.yaml data/ingredients/mapped/Rye-bran.yaml
data/ingredients/mapped/S-3-hydroxybutyrate.yaml
data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` crashed on the first CAS-primary fallback because the OBO SQLite
adapter cannot label `cas:` registry IDs; rerunning it on the CHEBI/FOODON
subset, Rutin, Rye-bran, and S-3-hydroxybutyrate, passed.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2539 maps exactly
to `cas:21288-61-9`, uses `registry:cas`, and exports only
`CAS:21288-61-9`.

The fallback should be revisited because a CHEBI primary now appears to exist.
PubChem's `21288-61-9` CID also lists `CHEBI:108590`, and fresh OLS4 lookup of
CHEBI:108590 resolved an active ChEBI term with the same molecular formula and
InChIKey as the PubChem CAS record. The ChEBI label is the long IUPAC surface,
not `Rutilantinone`, so the term needs curator confirmation before replacing
the CAS fallback.

**Completeness**: OLS4 exact CAS search for `21288-61-9` found no direct ChEBI
xref, which explains why the row-review table still treats the CAS CURIE as an
expected registry identifier. No roles, components, or structure fields are
asserted locally.

**Recommended Edits**: Revisit
`data/ingredients/mapped/Rutilantinone.yaml` and confirm whether the active
CHEBI:108590 term is exactly Rutilantinone. If it is, promote the record from
`cas:21288-61-9` to CHEBI:108590, populate CHEBI-derived structure fields, and
regenerate final SSSOM so row 2539 no longer publishes a CAS fallback as the
primary object.
