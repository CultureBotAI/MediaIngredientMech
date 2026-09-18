# `data/ingredients/mapped/L-arginine_X_Hcl.yaml`

## Verdict

Needs curation. The CultureMech exact ChEBI identity, CAS value, PubChem
structure, and occurrence count pass, but one exported synonym contains an
`HCI` typo and `AMINO_ACID_SOURCE` is only a provisional CHEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-arginine_X_Hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:31235` with
  `ontology_mapping.ontology_id: CHEBI:31235`, label
  `Arginine hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1119-34-2`, molecular formula
  `C6H14N4O2.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-alanylglycine.yaml data/ingredients/mapped/L-alliin.yaml data/ingredients/mapped/L-alpha-Phosphatidylcholine.yaml data/ingredients/mapped/L-arginine.yaml data/ingredients/mapped/L-arginine_X_Hcl.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:31235` as active `Arginine hydrochloride`, lists CAS
  `1119-34-2`, and reports formula `C6H14N4O2.HCl` with the same InChI as the
  YAML record.
- PubChem resolves CAS RN `1119-34-2` to CID `66250` with the hydrochloride
  formula and the same InChI as the YAML record.
- Major: the final SSSOM `other` field exports `L-Arginine x HCI`, where `HCI`
  ends with a capital `I` rather than lowercase `l`. A live EBI OLS exact
  search for that token returned zero ChEBI hits, and the correct `L-Arginine x
  HCl` form is already the preferred MIM term.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry and says review is
  recommended. Class ancestry can propose this role, but the record still lacks
  inspected source evidence that arginine hydrochloride was used as an
  amino-acid source in a medium.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the older synonym-enrich review row that
  accepted the typo as already represented.

## Completeness

- The exact ChEBI identity, CAS RN, structure, occurrence count, and aggregate
  copy are present and consistent.
- The SSSOM synonym surface and amino-acid role need source-backed curation.

## Recommended Edits

- Major: remove `L-Arginine x HCI` from the synonym list in
  `data/ingredients/mapped/L-arginine_X_Hcl.yaml`, or correct it only if an
  inspected source shows that a non-preferred alias is needed after the existing
  `L-Arginine x HCl` preferred term.
- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` with source-backed evidence for this
  exact hydrochloride, or remove the provisional role.
- Sync the aggregate copy and regenerate the SSSOM/docs products so `other`
  stops publishing the typo; rerun strict, term, round-trip, component, and
  SSSOM validation.
