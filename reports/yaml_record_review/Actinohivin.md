# `data/ingredients/mapped/Actinohivin.yaml`

## Verdict

Pass. The retained `kgmicrobe.compound` placeholder, no-hit promotion review,
SSSOM registry row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Actinohivin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:actinohivin` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- The local placeholder preserves the kg-microbe compound surface until a
  curator can identify an exact external ontology term.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` reports no prior
  OLS candidate and no normalized local duplicate; a fresh local ChEBI OAK
  search for `Actinohivin` also returned no hits.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acriflavine.yaml data/ingredients/mapped/Actein.yaml data/ingredients/mapped/Actinohivin.yaml data/ingredients/mapped/Actinomycetin.yaml data/ingredients/mapped/Actinomycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Actinohivin.yaml 'CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO'`:
  exited 1, so the documented `validate-terms` Engine A would skip this
  non-OBO `kgmicrobe.compound` placeholder.
- `uv run --frozen runoak -i sqlite:obo:chebi search 'Actinohivin'`: passed with
  no local ChEBI hits.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records no exact label or synonym candidate from the 2026-05-06 OLS search
  across CHEBI, MeSH, NCIT, MICRO, BTO, and FOODON.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records no
  normalized local duplicate and no exact OLS candidate.
- `mappings/ingredient_mappings.sssom.tsv` row 335 maps `MIM:Actinohivin` to
  the local placeholder with the expected `none|UNKNOWN_TERM|2026-07-07`
  trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, placeholder no-hit rows, generated indexes, ignored
  aggregate backups, and stale advisory batch rows.

## Completeness

- The placeholder status is explicitly documented in `notes` and
  `curation_history`.
- `chemical_properties` is correctly empty while the record has no exact
  external chemical identity.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
