# `data/ingredients/mapped/Aminoacids.yaml`

## Verdict

Needs curation. The `kgmicrobe.ingredient:aminoacids` fallback identity,
stock-solution classification, CultureMech occurrence count, SSSOM row, and
aggregate copy pass, but the active STOCK_SOLUTION record still has no
component-level recipe representation.

## Identity

- Reviewed record: `data/ingredients/mapped/Aminoacids.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:aminoacids` with a matching local
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The local identity is intentionally not mapped to amino-acid class
  `CHEBI:33709`: the `#288` evidence says this is an amino acid stock/pre-mix,
  not one chemical substance.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: AMINO_ACID_MIX` are
  present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aminoacids.yaml data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml data/ingredients/mapped/Aminophenazone.yaml data/ingredients/mapped/Aminovalerate.yaml data/ingredients/mapped/Ammonia.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Aminoacids.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1 because `kgmicrobe.ingredient` is a local non-OBO prefix. Engine A
  was intentionally skipped for this record.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` records no exact OLS hit
  for the original `UNMAPPED_0324` `Aminoacids` label.
- The `CLASSIFIED_STOCK_SOLUTION` history entry identifies the record as an
  amino-acid stock/pre-mix pending component-level curation; the `#288`
  mapping evidence documents the kg-microbe ingredient fallback.
- `mappings/culturemech_recipe_membership.tsv` contains six
  `kgmicrobe.ingredient:aminoacids` rows, matching
  `occurrence_statistics.total_occurrences: 6`.
- `mappings/ingredient_mappings.sssom.tsv` row 393 maps `MIM:Aminoacids` to
  `kgmicrobe.ingredient:aminoacids` with `skos:exactMatch` and the
  promote-resolved-unmapped provenance trailer.
- `reports/causal_graph_readiness.tsv` also flags this mapped fallback as
  lacking component edges.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, six CultureMech membership rows, SSSOM row, original
  OLS audit row, causal-readiness row, and generated reports.

## Completeness

- Local identity, stock-solution type, CultureMech occurrence statistics, and
  append-only curation history are populated.
- The record has no `components`, so the modeled amino-acid mix is not yet
  reproducible from curated member ingredients.
- No chemical-properties, role, environmental context, discussion, or dataset
  entry is otherwise needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Aminoacids.yaml`, add component records for the
  amino-acid stock/pre-mix once the maintained source recipe establishes its
  member amino acids and amounts.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
