# `data/ingredients/mapped/Filipin.yaml`

## Verdict

Pass with minor issues. The record maps `Filipin` to the exact MeSH antibiotic
complex rather than to a narrower `filipin III` component, but it is missing an
explicit mixture `ingredient_type` and still carries stale import-era top-level
notes.

## Identity

- Reviewed record: `data/ingredients/mapped/Filipin.yaml`.
- Identifier and grounding: `identifier: mesh:D005372` with matching
  `ontology_mapping.ontology_id`, label `Filipin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS for MeSH resolves `mesh:D005372` as `Filipin`, marks it
  non-obsolete, and defines it as a complex of polyene antibiotics obtained
  from `Streptomyces filipinensis`.
- The curated evidence correctly rejects CHEBI and NCIT `filipin III` as
  over-specific for a source label that denotes the filipin complex.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fildes_Enrichment.yaml data/ingredients/mapped/Filipin.yaml data/ingredients/mapped/Filtered_Seawater.yaml data/ingredients/mapped/Fish-sperm_Dna.yaml data/ingredients/mapped/Fish_peptone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Filipin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MeSH identifier, MicrobeDecoder source occurrence, missing
  `ingredient_type`, and stale top-level notes as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Filipin` to
  `mesh:D005372` with `skos:exactMatch` and an empty `other` column.
- `mappings/record_research_validation.tsv` records a resolved lane
  disagreement in which the Claude lane confirmed the current MeSH grounding
  after the Edison lane had failed to verify the CURIE.
- `mappings/microbedecoder_residual_research_proposed.tsv` and
  `mappings/microbedecoder_residual_deferred_ncit.tsv` show the rejected
  over-specific CHEBI and NCIT `filipin III` candidates; those component
  groundings did not reach the active YAML or final SSSOM row.
- Minor: MeSH defines filipin as an antibiotic complex, but the record has no
  `ingredient_type`.
- Minor: top-level `notes` still say curator review is needed even though the
  record was promoted to the curated MeSH term in #213.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MeSH promotion provenance, MicrobeDecoder
  deferred candidates, lane-disagreement resolution, and ignored historical
  batch reports.

## Completeness

- The exact MeSH complex identity, MicrobeDecoder source occurrence, and final
  SSSOM identity row are populated.
- No role, component, environment, or final synonym payload needs evidence in
  the current record.
- The missing mixture type is the only consequential field gap.

## Recommended Edits

- Minor: set the curator-confirmed `ingredient_type`, likely
  `UNDEFINED_MIXTURE`, in `data/ingredients/mapped/Filipin.yaml`; while
  touching the record, remove stale top-level review notes, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  final SSSOM invariant gates.
