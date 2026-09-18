# `data/ingredients/mapped/L-Galactose.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS registry value, formula, PubChem
structure, ChEBI synonym, empty occurrence count, and final SSSOM row are
consistent, but `CARBON_SOURCE` and `ENERGY_SOURCE` are only provisional
computational roles.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Galactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:37618` with
  `ontology_mapping.ontology_id: CHEBI:37618`, label `L-galactose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `15572-79-9` and molecular formula `C6H12O6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml data/ingredients/mapped/L-Deoxyalliin.yaml data/ingredients/mapped/L-Galactose.yaml data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Glutathione.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:37618` as active `L-galactose` and lists
  `L-galacto-hexose` as a synonym, supporting the exact ChEBI mapping and the
  curated synonym.
- PubChem resolves CAS RN `15572-79-9` to CID `84996` with formula `C6H12O6`
  and an L-galactose stereochemical InChI.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:37618` with
  only `L-galacto-hexose` and `CAS:15572-79-9` in `other`, both of which are
  synonyms for the same subject identity.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` have only `COMPUTATIONAL_PREDICTION`
  evidence from ChEBI ancestry and paired carbon-source inference, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to either
  role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, synonym support, CAS RN, formula, aggregate copy,
  empty occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source and energy-source roles are
  either supported by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,
  or literature sources can support L-galactose as a carbon and energy source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role changes.
