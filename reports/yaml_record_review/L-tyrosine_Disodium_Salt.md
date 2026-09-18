# `data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`

## Verdict

Needs curation. The CAS-derived CHEBI:53696 identity, disodium-salt structure,
FEBA occurrence count, synonyms, and final SSSOM row pass, but the
amino-acid-source role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:53696` with
  `ontology_mapping.ontology_id: CHEBI:53696`, label
  `disodium L-tyrosinate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `69847-45-6`, molecular formula `C9H9NO3.2Na`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:53696` as active `disodium L-tyrosinate` and lists
  CAS `69847-45-6`.
- PubChem resolves CAS RN `69847-45-6` to CID `44120124` with formula
  `C9H9NNa2O3`; this is equivalent to the YAML formula `C9H9NO3.2Na`, and the
  InChI matches.
- Exact OLS search for final synonym `L-Tyrosine sodium salt (1:2)` returns
  only CHEBI:53696 among ChEBI classes.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:53696`; its
  `other` field contains the reviewed salt synonym plus `CAS:69847-45-6`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and says
  review is recommended. The tyrosine salt name is enough to propose the role,
  but the record still lacks inspected FEBA or literature evidence that the
  exact disodium salt was supplied as an amino acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and FEBA-derived occurrence rows.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml` with inspected source
  evidence for exact L-tyrosine disodium salt use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
