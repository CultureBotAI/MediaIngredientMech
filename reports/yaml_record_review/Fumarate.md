# `data/ingredients/mapped/Fumarate.yaml`

## Verdict

Pass with minor issues. The promoted fumarate anion identity, CHEBI structure
fields, MicrobeDecoder and CultureMech occurrence counts, and final SSSOM row
pass, but top-level `notes` still contain stale pre-promotion import text.

## Identity

- Reviewed record: `data/ingredients/mapped/Fumarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29806` with matching
  `ontology_mapping.ontology_id`, canonical label `fumarate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local ChEBI metadata confirms `CHEBI:29806` is active `fumarate(2-)` with the
  formula, SMILES, and InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fructose-asparagine.yaml data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28757 CHEBI:5181 CHEBI:33984 CHEBI:29806`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and synonyms
  for `CHEBI:29806`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, curated anion-grounding rationale, structure fields,
  CultureMech and MicrobeDecoder occurrence counts, ingredient type, and stale
  top-level notes as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fumarate`
  to `CHEBI:29806` with `skos:exactMatch` and an empty `other` column.
- The current curated evidence explains why the bare `Fumarate` source label
  should resolve to fully deprotonated `fumarate(2-)`; subsequent research
  validation records mark the earlier Edison disagreement as resolved.
- Minor: top-level `notes` still say no CAS RN or CHEBI/NCIT match was found
  and curator review is needed even though the record has since been promoted,
  typed, populated with ChEBI/PubChem structure fields, and exported.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, CultureMech recipe memberships, resolved research-validation rows,
  and fumarate-containing component decompositions.

## Completeness

- The exact fumarate anion identity, structure fields, CultureMech and
  MicrobeDecoder occurrence counts, and final SSSOM identity row are populated.
- No component, role, environment, unsafe final synonym, or missing structure
  gap remains for the current ChEBI identity.

## Recommended Edits

- Minor: replace the stale top-level `notes` in
  `data/ingredients/mapped/Fumarate.yaml` with a short post-promotion statement
  that the bare anion label was reviewed and grounded to `fumarate(2-)`.
