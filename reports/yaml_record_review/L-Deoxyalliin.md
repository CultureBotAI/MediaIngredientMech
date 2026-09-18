# `data/ingredients/mapped/L-Deoxyalliin.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI lookup identity, active ChEBI term, formula,
PubChem structure, ChEBI synonym, empty occurrence count, and final SSSOM row
are consistent, but `AMINO_ACID_SOURCE` is only provisional ChEBI-ancestry
evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Deoxyalliin.yaml`.
- Identifier and grounding: `identifier: CHEBI:74077` with
  `ontology_mapping.ontology_id: CHEBI:74077`, label `S-allylcysteine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `21593-77-1`, molecular formula `C6H11NO2S`,
  InChI, and SMILES.

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

- EBI OLS4 resolves `CHEBI:74077` as active `S-allylcysteine` and lists
  `L-deoxyalliin` plus `S-prop-2-en-1-yl-L-cysteine` as synonyms, supporting
  the synonym-grade ChEBI identity that was established by CAS lookup.
- PubChem resolves CAS RN `21593-77-1` to CID `9793905` with formula
  `C6H11NO2S` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:74077` with
  only `S-prop-2-en-1-yl-L-cysteine` and `CAS:21593-77-1` in `other`, both of
  which are synonyms for the same subject identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, synonym support, CAS RN, formula, structure,
  aggregate copy, empty occurrence count, and final SSSOM row are present and
  consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-deoxyalliin as
  an amino acid source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role change.
