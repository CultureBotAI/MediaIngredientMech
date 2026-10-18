# `data/ingredients/mapped/Sodium_L-lactate.yaml`

**Verdict**: pass with minor issues.

**Identity**: `Sodium L-lactate` is a rejected tombstone pointing at the live
`CHEBI:232798` / `sodium L-lactate` record. Fresh OLS4 lookup confirmed the
ChEBI label, CAS RN `867-56-1`, formula `C3H5O3.Na`, InChI, InChIKey, and
SMILES, and PubChem resolves the CAS RN to the same L-lactate structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_L-lactate.yaml
data/ingredients/mapped/Sodium_Lactate.yaml
data/ingredients/mapped/Sodium_M-arsenite.yaml
data/ingredients/mapped/Sodium_Malate.yaml
data/ingredients/mapped/Sodium_Maleate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The tombstone's identifier, ChEBI pointer, representative,
`kg_microbe_node_id`, CAS RN, formula, InChI, and SMILES all point at the same
live L-lactate identity. A hidden and ignored-inclusive search found no final
SSSOM subject row for `MIM:Sodium_L-lactate`; its duplicate label has been
merged into the live `Na-l-lactate.yaml` record, which is already separately
reviewed. The per-record YAML agrees with the regenerated aggregate row when
keyed by identifier and preferred term.

**Completeness**: Minor only: stale `CARBON_SOURCE` and `ENERGY_SOURCE` roles
remain on the rejected tombstone. They are inert because this record no longer
publishes a final SSSOM row, but they should be stripped if the tombstone is
cleaned for readability.

**Recommended Edits**: Optionally remove the stale role facets from this
rejected tombstone while preserving the rejection history and live-record
pointer.
