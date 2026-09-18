# `data/ingredients/mapped/Actinomycin_A.yaml`

## Verdict

Needs curation. The `CHEBI:15369` narrow parent and local
`kgmicrobe.compound:actinomycin_a` identity are represented consistently, but
the `SELECTIVE_AGENT` role is still only a provisional name-pattern assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Actinomycin_A.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:actinomycin_a` with
  `ontology_mapping.ontology_id: CHEBI:15369`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:15369` to the broader
  class `actinomycin`.
- Local OAK did not return an exact ChEBI hit for `Actinomycin A`; the record
  retains a local kg-microbe identity and publishes the actinomycin parent as
  `skos:narrowMatch`.
- The `produces: actinomycin A` RAW_TEXT synonym is a recovered source surface
  from SSSOM `other`, not an exact ontology synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acriflavine.yaml data/ingredients/mapped/Actein.yaml data/ingredients/mapped/Actinohivin.yaml data/ingredients/mapped/Actinomycetin.yaml data/ingredients/mapped/Actinomycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Actinomycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:70241 CHEBI:15369`:
  returned `actinomycin` and its related plural synonyms for `CHEBI:15369`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:70241 CHEBI:15369`:
  returned the ChEBI `actinomycin` class metadata and no exact formula or
  structure fields for `CHEBI:15369`.
- `uv run --frozen runoak -i sqlite:obo:chebi search 'Actinomycin A'`: passed
  with no local exact ChEBI hit.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The current YAML preserves the LOW-confidence kg-microbe placeholder evidence
  and records the later CHEBI parent backfill separately.
- `mappings/ingredient_mappings.sssom.tsv` exports `MIM:Actinomycin_A`
  `skos:narrowMatch` `CHEBI:15369` plus a sibling `skos:exactMatch` registry
  row for `kgmicrobe.compound:actinomycin_a`, matching the mapping semantics for
  local identities with ontology parents.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  proposed `Actinomycin A` enrichment was already represented by the preferred
  term or synonyms.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the
  kg-microbe row as an expected local registry identifier.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, both SSSOM rows, synonym-enrich review row, unknown-term triage row,
  generated indexes, ignored aggregate backups, and stale advisory batch rows.
- The `physicochemical_roles.SELECTIVE_AGENT` row is only a name-pattern
  prediction; no inspected source supports actinomycin A as a selective medium
  agent.

## Completeness

- `chemical_properties` is correctly empty because the active ontology mapping
  is to a broad ChEBI class and no exact actinomycin A structure has been
  curated.
- No component, environmental context, discussion, or dataset entry is required
  for the current parent mapping.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Actinomycin_A.yaml`, remove or evidence the
  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion, then run
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen python scripts/validate_component_partonomy.py`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
