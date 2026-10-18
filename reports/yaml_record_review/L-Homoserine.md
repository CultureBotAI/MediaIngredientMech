# `data/ingredients/mapped/L-Homoserine.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS value, formula, PubChem
structure, empty occurrence count, and final SSSOM row are consistent, but
`AMINO_ACID_SOURCE` is only provisional ChEBI-ancestry evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Homoserine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15699` with
  `ontology_mapping.ontology_id: CHEBI:15699`, label `L-homoserine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `672-15-1`, molecular formula `C4H9NO3`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/L-Homoserine.yaml data/ingredients/mapped/L-Malic_Acid.yaml data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Meta-tyrosine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:15699` as active `L-homoserine`, supporting the
  exact ChEBI identity.
- PubChem resolves CAS RN `672-15-1` to CID `12647` with formula `C4H9NO3` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:15699` with
  only `CAS:672-15-1` in `other`, which belongs to the same subject identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-homoserine as
  an amino acid source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role change.
