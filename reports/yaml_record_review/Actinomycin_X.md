# `data/ingredients/mapped/Actinomycin_X.yaml`

## Verdict

Needs curation. The MicrobeDecoder source occurrence is traceable, but the exact
MeSH mapping is disputed as the wrong actinomycin X sense and the top-level
notes still say curator review is needed after promotion.

## Identity

- Reviewed record: `data/ingredients/mapped/Actinomycin_X.yaml`.
- Identifier and grounding: `identifier: mesh:C041783` with
  `ontology_mapping.ontology_id: mesh:C041783`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The current record asserts that BacDive `actinomycin X` exactly denotes MeSH
  `mesh:C041783`.
- `mappings/record_research_validation.tsv` contains independent dispute rows
  for this exact record. The most specific dispute says MeSH `C041783` denotes
  `actinomycin X-14873B/C/D` rather than the classical broad actinomycin X
  family.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Actinomycin_D.yaml data/ingredients/mapped/Actinomycin_X.yaml data/ingredients/mapped/Actinotiocin.yaml data/ingredients/mapped/Activated_Charcoal.yaml data/ingredients/mapped/Adenine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Actinomycin_X.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:mesh aliases mesh:C041783 mesh:C006403`:
  reached the local MeSH adapter, but the adapter returned only stub `None`
  labels for both SCR terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:actinomycin_x` in `BacDive_Metabolite_production` with count
  `2`, matching `source_occurrences`.
- `mappings/ingredient_mappings.sssom.tsv` row 340 maps
  `MIM:Actinomycin_X` to `mesh:C041783` with the manual promotion trailer.
- Advisory rows in `mappings/record_research_validation.tsv` report that both
  reviewed research lanes disputed the `mesh:C041783` exact match; they also
  flag the `#213` note saying that ChEBI only carries X2 and X0delta congeners
  as stale because ChEBI has a broader `CHEBI:15369` actinomycin family.
- The top-level `notes` still say the MicrobeDecoder import had no CAS or
  CHEBI/NCIT match and needed curator review even though the same file now maps
  to `mesh:C041783`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, MicrobeDecoder raw occurrence, `record_research_validation`
  disputes, generated indexes, ignored aggregate backups, and stale advisory
  batch rows.

## Completeness

- No role, component, environmental context, or dataset entry is needed while
  the identity is unresolved.
- `chemical_properties` is correctly empty for a MeSH family-level mapping.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Actinomycin_X.yaml`, replace `mesh:C041783` with a
  better parent or local identity, or mark the record unresolved if no exact
  family term exists.
- Remove or rewrite the `#213` evidence note so it no longer claims that the
  checked ChEBI hierarchy lacked a broad actinomycin family term.
- Refresh the stale top-level `notes`.
