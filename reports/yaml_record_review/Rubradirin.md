# `data/ingredients/mapped/Rubradirin.yaml`

**Verdict**: needs curation, major issue.

**Identity**: The record currently maps bare `rubradirin` exactly to
`CHEBI:223718` / `Rubradirin B`. Fresh OLS4 lookup resolved CHEBI:223718 with
the same formula, InChI, SMILES, and long IUPAC exact synonym as the record, so
the structure fields are internally consistent for Rubradirin B.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Roxithromycin.yaml
data/ingredients/mapped/Rubidium_Chloride.yaml
data/ingredients/mapped/Rubradirin.yaml
data/ingredients/mapped/Rubrolone.yaml
data/ingredients/mapped/Rumen_Fluid.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. The final SSSOM row 2536 exact
maps `MIM:Rubradirin` to `CHEBI:223718`; it safely exports the ChEBI exact
IUPAC synonym but also exports `produces: rubradirin`, which is a
process-qualified source phrase rather than a synonym.

The exact identity needs curator review. Current OLS4 lists only `Rubradirin B`
and the long IUPAC label for CHEBI:223718; it does not list bare `rubradirin`
as an exact or related synonym. A hidden and ignored inclusive search under
`data/ingredients` found no second Rubradirin or Rubradirin B record, and the
broader hidden search across `data/ingredients`, `data/curated`, `mappings`,
`scripts`, `src`, `tests`, and `reports` found the live Rubradirin B mapping
only in this maintained record, derived aggregate/index/SSSOM rows, review
TSVs, and historical backups.

**Completeness**: No roles or components are asserted. The consequential gaps
are the unsupported `Rubradirin B` exact-match decision for a bare Rubradirin
subject and the process phrase published as a synonym.

**Recommended Edits**: Revisit
`data/ingredients/mapped/Rubradirin.yaml` against the original
`kgmicrobe.compound:rubradirin` source. If the source denotes Rubradirin B,
rename the MIM subject accordingly; otherwise demote the CHEBI:223718 mapping
to a non-exact relation or create a local registry identity for the broader
rubradirin surface. In the same maintained YAML, remove the
`produces: rubradirin` `sssom_other_backfill` synonym and regenerate final
SSSOM so row 2536 no longer exports it.
