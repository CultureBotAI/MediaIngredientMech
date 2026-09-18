# `data/ingredients/mapped/L-isoleucine.yaml`

## Verdict

Needs curation. The L-isoleucine identity, CAS RN, PubChem structure,
occurrence count, and active ChEBI grounding pass, but the amino-acid-source
role is provisional and final SSSOM still exports the generic `Isoleucine`
label.

## Identity

- Reviewed record: `data/ingredients/mapped/L-isoleucine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17191` with
  `ontology_mapping.ontology_id: CHEBI:17191`, label `L-isoleucine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `73-32-5`, molecular formula `C6H13NO2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17191` as active `L-isoleucine` and lists CAS
  `73-32-5`.
- PubChem resolves CAS RN `73-32-5` to CID `6306` with formula `C6H13NO2` and
  the same InChI as the YAML record.
- Major: final SSSOM `other` still exports bare `Isoleucine`; EBI OLS4 exact
  search resolves that label to generic `CHEBI:24898`, not to the
  stereospecific L-isoleucine row.
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

- Major: remove or demote `Isoleucine` in
  `data/ingredients/mapped/L-isoleucine.yaml`; keep the exact synonym surface
  specific to `CHEBI:17191`.
- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` with inspected
  source evidence for exact L-isoleucine use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
