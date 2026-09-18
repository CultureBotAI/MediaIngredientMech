# `data/ingredients/mapped/Galactarate.yaml`

## Verdict

Pass with a minor stale-note issue. The bare MicrobeDecoder galactarate label is
intentionally grounded to active ChEBI `galactarate(2-)`, whose structure
matches the record, and the obsolete Edison alternative was not promoted; only
the top-level import note still describes the old unresolved state.

## Identity

- Reviewed record: `data/ingredients/mapped/Galactarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16537` with matching
  `ontology_mapping.ontology_id`, canonical label `galactarate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:16537` as an active dianion term with formula `C6H8O8`,
  charge `-2`, and the same InChI and SMILES recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml data/ingredients/mapped/GYPS.yaml data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder source occurrence, raw source synonym,
  mapping evidence, structure fields, and ingredient type as the per-record
  YAML.
- The mapping evidence explains the curator choice: bare anion labels are
  grounded to the bare-name ChEBI class when one exists, and here the
  fully-deprotonated `galactarate(2-)` term was selected instead of the
  mono-anion.
- `mappings/record_research_validation.tsv` notes that Edison proposed
  `CHEBI:30917`; OLS4 reports that `CHEBI:30917` is obsolete, and the active
  record does not use it.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Galactarate` to `CHEBI:16537` with `skos:exactMatch` and leaves `other`
  empty.
- Minor: the top-level `notes` field still contains the original
  MicrobeDecoder import text saying no CAS or CHEBI/NCIT match was found and
  curator review was needed, even though the record is now mapped to ChEBI.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, record-research validation row, generated indexes, and ignored aggregate
  backups.

## Completeness

- The active dianion identity, structure fields, MicrobeDecoder source
  occurrence, raw source synonym, and final SSSOM row are populated.
- I found no consequential missing CAS, role, component, environment, or
  synonym payload.

## Recommended Edits

- Minor: refresh the top-level `notes` in
  `data/ingredients/mapped/Galactarate.yaml` and
  `data/curated/mapped_ingredients.yaml` so it no longer reports the
  pre-promotion unresolved state.
