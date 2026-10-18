# `data/ingredients/mapped/L-cysteine_Hcl.yaml`

## Verdict

Needs curation. The anhydrous L-cysteine hydrochloride identity, CAS value,
PubChem structure, occurrence count, and final CAS token pass, but final SSSOM
still exports a QSY9-derived synonym and the amino-acid-source role is
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/L-cysteine_Hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:91247` with
  `ontology_mapping.ontology_id: CHEBI:91247`, label
  `L-cysteine hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `52-89-1`, molecular formula `C3H7NO2S.HCl`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cysteine.yaml data/ingredients/mapped/L-cysteine_Hcl.yaml data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml data/ingredients/mapped/L-cysteine_Zwitterion.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:91247` as active `L-cysteine hydrochloride`, lists
  CAS `52-89-1`, and reports formula `C3H7NO2S.HCl` with the same InChI as the
  YAML record.
- PubChem resolves CAS RN `52-89-1` to CID `60960` with the hydrochloride
  formula and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:91247` with
  anhydrous HCl surface forms and `CAS:52-89-1`; the raw CultureMech note
  `(add to make medium anoxic)` is correctly filtered out.
- Major: the final SSSOM `other` field still exports the long sulfoanilinium
  label inherited from the old CHEBI:52891 QSY9 misgrounding. EBI OLS4 resolves
  that label on active `CHEBI:52891` `QSY9 succinimidyl ester(1+)`, not on
  CHEBI:91247.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern
  and says review is recommended. The name pattern can propose this role, but
  the record still lacks inspected source evidence that this hydrochloride was
  used as an amino-acid source in a medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, CultureMech residual alias rows, docs projections, and the
  anhydrous-vs-monohydrate sibling records.

## Completeness

- The exact ChEBI identity, corrected CAS RN, structure, occurrence count, and
  aggregate copy are present and consistent.
- The QSY9 carry-over synonym and provisional amino-acid-source role still need
  curation.

## Recommended Edits

- Major: remove the long QSY9 exact synonym from
  `data/ingredients/mapped/L-cysteine_Hcl.yaml`; the historical curation events
  already identify CHEBI:52891 as unrelated to this hydrochloride.
- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` with source-backed evidence for this
  exact anhydrous HCl form, or remove the provisional role.
- Sync the aggregate copy and regenerate the SSSOM/docs products; rerun strict,
  term, round-trip, component, and SSSOM validation.
