# `data/ingredients/mapped/L-fucose.yaml`

## Verdict

Needs curation. The CultureMech exact CHEBI:18287 identity, CAS RN, PubChem
formula, occurrence count, reviewed synonyms, and final SSSOM row pass, but the
carbon-source role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-fucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:18287` with
  `ontology_mapping.ontology_id: CHEBI:18287`, label `L-fucose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `2438-80-4` and molecular formula `C6H12O5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cystine.yaml data/ingredients/mapped/L-fructose.yaml data/ingredients/mapped/L-fucose.yaml data/ingredients/mapped/L-galactonate.yaml data/ingredients/mapped/L-galactonic_Acid_Gamma-lactone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:18287` as active `L-fucose`, lists CAS
  `2438-80-4`, includes the YAML synonyms, and reports formula `C6H12O5`.
- PubChem resolves CAS RN `2438-80-4` to CID `17106` with formula `C6H12O5`,
  matching the YAML formula.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18287`; its
  `other` field contains reviewed exact synonyms plus `CAS:2438-80-4`, with no
  broader sibling, CAS-only noise, or raw role text.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that this exact ingredient was supplied as a carbon
  source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, and docs projections.

## Completeness

- The ChEBI identity, CAS RN, formula, occurrence count, synonyms, aggregate
  copy, and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/L-fucose.yaml` with inspected source evidence for
  the exact L-fucose use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
