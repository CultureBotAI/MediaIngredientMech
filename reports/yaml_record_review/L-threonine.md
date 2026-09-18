# `data/ingredients/mapped/L-threonine.yaml`

## Verdict

Needs curation. The L-threonine identity, CAS RN, PubChem structure, occurrence
count, reviewed synonyms, and final SSSOM row pass, but the amino-acid-source
role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-threonine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16857` with
  `ontology_mapping.ontology_id: CHEBI:16857`, label `L-threonine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16857`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `72-19-5`, molecular formula `C4H9NO3`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16857` as active `L-threonine` and lists CAS
  `72-19-5`.
- PubChem resolves CAS RN `72-19-5` to CID `6288` with formula `C4H9NO3` and
  the same InChI as the YAML record.
- Exact OLS search for exported synonym `2-Amino-3-hydroxybutyric acid`
  returns only CHEBI:16857 among ChEBI classes, so the final kg-microbe synonym
  set does not cross into the generic `Threonine` record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16857`; its
  `other` field contains reviewed L-threonine synonyms plus `CAS:72-19-5`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact L-threonine was supplied as an amino acid
  source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the generic Threonine sibling, and component
  references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-threonine.yaml` with inspected source evidence for
  exact L-threonine use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
