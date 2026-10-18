# `data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml`

## Verdict

Needs curation. The record correctly keeps `cas:2922-28-3` as its exact
identity and only close-matches the adenine parent, but the hydrate state still
needs source-level support because the CAS/PubChem structure lacks a water
component.

## Identity

- Reviewed record: `data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:2922-28-3` with
  `ontology_mapping.ontology_id: CHEBI:16708`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16708` to the anhydrous
  free base `adenine`, not to the hydrochloride hydrate.
- A local ChEBI OAK search for `Adenine hydrochloride hydrate` returned no
  exact ChEBI hit, consistent with keeping the CAS registry identity.
- PubChem resolves CAS `2922-28-3` to CID `76219`, matching the stored
  `chemical_properties.pubchem_cid`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml data/ingredients/mapped/Adenomycin.yaml data/ingredients/mapped/Adenosine.yaml data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml data/ingredients/mapped/Adenosine_5-monophosphate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi search 'Adenine hydrochloride hydrate'`:
  passed with no local ChEBI hits.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned the expected labels and aliases for the ChEBI targets in this batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 344 close-matches
  `MIM:Adenine_Hydrochloride_Hydrate` to `CHEBI:16708`; row 345 preserves the
  CAS registry identity.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the CAS row
  as an expected registry identifier, not an OAK/OLS ontology term.
- `mappings/culturemech_recipe_membership.tsv` contains 22 rows for
  `cas:2922-28-3`, matching `occurrence_statistics`.
- `mappings/hydrate_review.tsv` flags this same record as `NEEDS_SOURCE`: the
  label says only hydrate and the CAS/formula metadata does not establish a
  unique water stoichiometry.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, close and registry SSSOM rows, occurrence rows, unknown-term triage row,
  hydrate-review row, component references in `NLDM_metabolites`, generated
  indexes, and ignored aggregate backups.

## Completeness

- CAS, PubChem CID, close parent mapping, occurrence statistics, curation
  history, and `ingredient_type` are populated.
- The exact hydrate stoichiometry and supplier/source evidence remain
  unresolved.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Inspect the CultureBotHT or source-media records that supplied CAS
  `2922-28-3`; either confirm the hydrated form and update the structure
  evidence accordingly, or relabel the exact CAS identity if it is only adenine
  hydrochloride.
- Keep `CHEBI:16708` as a close parent/neighbor rather than an exact identity
  unless ChEBI adds a term for the exact supplied form.
