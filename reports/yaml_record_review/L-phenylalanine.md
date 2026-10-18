# `data/ingredients/mapped/L-phenylalanine.yaml`

## Verdict

Needs curation. The L-phenylalanine identity, CAS RN, PubChem structure, and
occurrence count pass, but final SSSOM exports generic `Phenylalanine` and the
amino-acid-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/L-phenylalanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17295` with
  `ontology_mapping.ontology_id: CHEBI:17295`, label `L-phenylalanine`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `63-91-2`, molecular formula `C9H11NO2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline-4-nitroanilide.yaml data/ingredients/mapped/L-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records. Engine A term validation was
  skipped for the non-OBO `kgmicrobe.compound` registry record.

## Evidence

- EBI OLS4 resolves `CHEBI:17295` as active `L-phenylalanine` and lists CAS
  `63-91-2`.
- PubChem resolves CAS RN `63-91-2` to CID `6140` with formula `C9H11NO2` and
  the same InChI as the YAML record.
- Major: final SSSOM `other` still exports bare `Phenylalanine`; EBI OLS4
  exact search resolves that label to generic `CHEBI:28044`, not to the
  stereospecific L-phenylalanine row.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that this exact ingredient was supplied as an amino
  acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and component references from multicomponent
  amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count, and
  aggregate copy are present and internally consistent.
- The final SSSOM synonym surface and provisional amino-acid role need
  curation.

## Recommended Edits

- Major: remove or demote `Phenylalanine` in
  `data/ingredients/mapped/L-phenylalanine.yaml`; keep the exact synonym
  surface specific to `CHEBI:17295`.
- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` with inspected
  source evidence for exact L-phenylalanine use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
