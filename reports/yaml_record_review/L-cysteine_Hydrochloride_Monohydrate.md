# `data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml`

## Verdict

Pass with minor issues. This rejected duplicate correctly tombstones a
CHEBI:91248 L-cysteine hydrochloride monohydrate record that was merged into
`L-cysteine_Hcl_X_H2o`; only stale active-record fields remain on the rejected
copy.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91248` with
  `ontology_mapping.ontology_id: CHEBI:91248`, label
  `L-cysteine hydrochloride hydrate`, source `CHEBI`, `mapping_quality:
  CAS_RN_LOOKUP`, and `mapping_status: REJECTED`.
- Chemical properties: CAS RN `7048-04-6`, molecular formula
  `C3H7NO2S.H2O.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cysteine.yaml data/ingredients/mapped/L-cysteine_Hcl.yaml data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml data/ingredients/mapped/L-cysteine_Zwitterion.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 exact search for `L-cysteine hydrochloride hydrate` resolves active
  `CHEBI:91248`; PubChem resolves CAS RN `7048-04-6` to the same monohydrate
  InChI and formula family recorded in this YAML.
- The curation history marks this duplicate as `MERGED_INTO`
  `L-Cysteine HCl x H2O` on CHEBI:91248, and the active
  `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml` record now owns the
  occurrence-bearing monohydrate identity.
- A hidden and ignored-inclusive exact subject search of
  `mappings/ingredient_mappings.sssom.tsv` found no final SSSOM row for this
  tombstone.
- Minor: `nutritional_roles.AMINO_ACID_SOURCE`, chemical properties, and old
  synonyms are still populated on the rejected duplicate. Because the record
  is not exported as a final SSSOM subject, these are stale tombstone fields
  rather than a live publication defect.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, generated
  rejected docs row, hydrate review row, and the active CHEBI:91248 sibling.

## Completeness

- The duplicate disposition is present and points to the active monohydrate
  record.
- The rejected record can be simplified by dropping active-only roles and
  synonyms, but the final SSSOM is already free of this duplicate subject.

## Recommended Edits

- Minor: clear stale active-only role and synonym fields from
  `data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml` if this
  tombstone is edited again; keep the `MERGED_INTO` event that points to
  `L-Cysteine HCl x H2O`.
