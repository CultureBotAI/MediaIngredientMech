# `data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml`

## Verdict

Needs curation. The CAS-derived L-ornithine monohydrochloride identity, CAS RN,
PubChem structure, occurrence count, reviewed synonyms, and final SSSOM row
pass, but the amino-acid-source role is still a provisional CHEBI-ancestry
inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:195690` with
  `ontology_mapping.ontology_id: CHEBI:195690`, label
  `L-Ornithine monochlorohydrate/ornithine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `3184-13-2`, molecular formula
  `C5H12N2O2.HCl`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline-4-nitroanilide.yaml data/ingredients/mapped/L-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records. Engine A term validation was
  skipped for the non-OBO `kgmicrobe.compound` registry record.

## Evidence

- EBI OLS4 resolves `CHEBI:195690` as active
  `L-Ornithine monochlorohydrate/ornithine`.
- PubChem resolves CAS RN `3184-13-2` to CID `76654` with the same salt InChI
  as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:195690`; its
  `other` field contains a hydrochloride-specific synonym plus `CAS:3184-13-2`,
  with no free ornithine synonyms.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that this exact monohydrochloride was supplied as an
  amino-acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the separate free L-ornithine sibling.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml` with inspected
  source evidence for exact L-ornithine monohydrochloride use, or remove the
  provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
