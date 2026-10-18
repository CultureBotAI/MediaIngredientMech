# `data/ingredients/mapped/Aminovalerate.yaml`

## Verdict

Pass. The local `kgmicrobe.compound:aminovalerate` identity intentionally
preserves the unresolved MicrobeDecoder substrate label without collapsing it
onto a specific aminopentanoate isomer; the source occurrence, SSSOM row, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Aminovalerate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:aminovalerate` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- `uv run --frozen runoak -i sqlite:obo:chebi search "aminovalerate"` returned
  no local ChEBI hit for the generic label.
- The nearby `5-aminovaleric_Acid` record is an exact positional-isomer row;
  this record correctly avoids reusing that specific CHEBI identity for the
  generic `aminovalerate` substrate label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aminoacids.yaml data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml data/ingredients/mapped/Aminophenazone.yaml data/ingredients/mapped/Aminovalerate.yaml data/ingredients/mapped/Ammonia.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Aminovalerate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1 because `kgmicrobe.compound` is a local non-OBO prefix. Engine A was
  intentionally skipped for this record.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.compound:aminovalerate` in `bergey:substrates` with count `1`,
  matching `source_occurrences`.
- The `#213` evidence says ChEBI, NCIT, FOODON, ENVO, MeSH, BTO, UBERON, and
  exact live OLS4 were searched and no term was found to denote the generic
  `Aminovalerate` label.
- `mappings/ingredient_mappings.sssom.tsv` row 396 maps
  `MIM:Aminovalerate` to `kgmicrobe.compound:aminovalerate` with
  `skos:exactMatch` and the promote-resolved-unmapped provenance trailer.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, advisory
  fallback-agreement row, generated reports, and the separate
  `5-aminovaleric_Acid` positional-isomer record.

## Completeness

- Local identity, raw source synonym, source occurrence, mapping evidence, and
  curation history are populated.
- No structure, role, component, environmental context, discussion, or dataset
  entry is needed while the positional identity remains unresolved.
- `mappings/culturemech_recipe_membership.tsv` has no
  `kgmicrobe.compound:aminovalerate` row, which is consistent with
  `occurrence_statistics.total_occurrences: 0` because the record is sourced
  from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
