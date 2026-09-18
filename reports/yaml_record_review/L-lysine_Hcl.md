# `data/ingredients/mapped/L-lysine_Hcl.yaml`

## Verdict

Needs curation. The L-lysine hydrochloride identity, CAS RN, PubChem structure,
occurrence count, reviewed synonyms, and final SSSOM row pass, but the
amino-acid-source role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-lysine_Hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:53633` with
  `ontology_mapping.ontology_id: CHEBI:53633`, label
  `L-lysine hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `657-27-2`, molecular formula
  `C6H14N2O2.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:53633` as active `L-lysine hydrochloride` and lists
  CAS `657-27-2`.
- PubChem resolves CAS RN `657-27-2` to CID `69568` with the same salt InChI
  as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:53633`; its
  `other` field contains hydrochloride-specific synonyms plus `CAS:657-27-2`,
  with no free L-lysine synonyms.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern
  and says review is recommended. The name pattern can propose this role, but
  the record still lacks inspected source evidence that L-lysine hydrochloride
  was supplied as an amino-acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the separate free L-lysine sibling.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-lysine_Hcl.yaml` with inspected source evidence
  for exact L-lysine hydrochloride use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
