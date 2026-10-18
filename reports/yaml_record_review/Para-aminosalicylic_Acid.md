# `data/ingredients/mapped/Para-aminosalicylic_Acid.yaml`

## Verdict

Needs curation; major. The CAS-to-ChEBI lookup for para-aminosalicylic acid
passes, but `AMINO_ACID_SOURCE` is only a provisional CHEBI-ancestry role.

## Identity

- Reviewed record: `data/ingredients/mapped/Para-aminosalicylic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:27565` with
  `ontology_mapping.ontology_id: CHEBI:27565`, label
  `4-aminosalicylic acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The existing OAK/OLS row review confirmed `CHEBI:27565` and found the
  preferred label already represented.
- A local CAS checksum calculation confirmed that `65-49-6` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Para-aminosalicylic_Acid` exactly to `CHEBI:27565`.

## Evidence

- The CAS-derived CHEBI primary identifier, mapping target, structured formula,
  InChI, and SMILES all describe 4-aminosalicylic acid.
- The final SSSOM exports only `4-amino-2-hydroxybenzoic acid` and
  `CAS:65-49-6` in `other`, both of which are same-substance labels for this
  record.
- Major: the `AMINO_ACID_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry.

## Completeness

- The CAS-to-CHEBI mapping and final SSSOM synonym set are complete enough.
- The amino-acid-source role needs direct recipe or experimental evidence
  before it should remain asserted.

## Recommended Edits

- Major: in `data/ingredients/mapped/Para-aminosalicylic_Acid.yaml`, either
  replace `nutritional_roles.AMINO_ACID_SOURCE` with cited source evidence, or
  remove the provisional role facet until source-backed role evidence is
  curated.
