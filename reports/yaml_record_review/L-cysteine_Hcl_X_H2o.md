# `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml`

## Verdict

Needs curation. The L-cysteine hydrochloride monohydrate identity, CAS value,
PubChem structure, duplicate merge, occurrence count, and CHEBI:91248 exact row
pass, but final SSSOM still exports concentration-qualified or anhydrous HCl
surface forms and the amino-acid-source role is provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91248` with
  `ontology_mapping.ontology_id: CHEBI:91248`, label
  `L-cysteine hydrochloride hydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7048-04-6`, molecular formula
  `C3H7NO2S.H2O.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cysteine.yaml data/ingredients/mapped/L-cysteine_Hcl.yaml data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml data/ingredients/mapped/L-cysteine_Zwitterion.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 exact search for `L-cysteine hydrochloride hydrate` resolves active
  `CHEBI:91248`, whose definition is the monohydrate form of L-cysteine
  hydrochloride and whose exact synonyms include the same water `(1/1)` labels
  used by this record.
- PubChem resolves CAS RN `7048-04-6` to CID `23462` with formula
  `C3H10ClNO3S` and an InChI equivalent to the YAML's
  `C3H7NO2S.H2O.HCl` monohydrate.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:91248` with
  `CAS:7048-04-6`, and the rejected `L-Cysteine hydrochloride monohydrate`
  duplicate has no exact final SSSOM subject row.
- Major: final SSSOM `other` still exports `Cystein-HCl x 2 H2O (5% (w/v))`.
  That token is both concentration-qualified and not a clean monohydrate
  synonym.
- Major: final SSSOM `other` still exports `Cystein-HCl`, an anhydrous HCl
  spelling that omits the required water of hydration.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern
  and says review is recommended. The name pattern can propose this role, but
  the record still lacks inspected source evidence that this monohydrate was
  used as an amino-acid source in a medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, hydrate review rows, local-registry solution sibling, rejected
  duplicate tombstone, docs projections, and residual alias rows.

## Completeness

- The exact ChEBI identity, CAS RN, structure, occurrence count, duplicate
  merge, aggregate copy, and exact final SSSOM row are present and consistent.
- The final SSSOM synonym surface needs cleanup, and the amino-acid role needs
  source-backed curation.

## Recommended Edits

- Major: remove concentration-qualified `Cystein-HCl x 2 H2O (5% (w/v))` and
  anhydrous `Cystein-HCl` from
  `data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml`.
- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` with source-backed evidence for this
  exact monohydrate, or remove the provisional role.
- Sync the aggregate copy and regenerate the SSSOM/docs products; rerun strict,
  term, round-trip, component, and SSSOM validation.
