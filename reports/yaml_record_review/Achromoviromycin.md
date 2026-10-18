# `data/ingredients/mapped/Achromoviromycin.yaml`

## Verdict

Needs curation. The retained `kgmicrobe.compound` placeholder is intentional and
the no-hit OLS review found no exact external promotion target, but the
`SELECTIVE_AGENT` role is still only a provisional name-pattern assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Achromoviromycin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:achromoviromycin` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- The local placeholder preserves a kg-microbe compound surface until a curator
  can identify an exact CHEBI, NCIT, or other external ontology term.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` reports no prior
  OLS candidate and no normalized local duplicate; a fresh local ChEBI OAK
  search for `Achromoviromycin` also returned no hits.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetylated_Xylan.yaml data/ingredients/mapped/Acetylene.yaml data/ingredients/mapped/Achromoviromycin.yaml data/ingredients/mapped/Aconitate.yaml data/ingredients/mapped/Acridine_Orange.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Achromoviromycin.yaml 'CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO'`:
  exited 1, so the documented `validate-terms` Engine A would skip this
  non-OBO `kgmicrobe.compound` placeholder.
- `uv run --frozen runoak -i sqlite:obo:chebi search Achromoviromycin`: passed
  with no local ChEBI hits.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings elsewhere in the corpus.

## Evidence

- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records no exact label or synonym candidate from the 2026-05-06 OLS search
  across CHEBI, MeSH, NCIT, MICRO, BTO, and FOODON.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both classify the
  unresolved local CURIE as an expected registry identifier to keep pending
  promotion to an external ontology term.
- `mappings/ingredient_mappings.sssom.tsv` row 328 maps
  `MIM:Achromoviromycin` to its local placeholder with the expected
  `none|UNKNOWN_TERM|2026-07-07` trailer.
- `data/custom/microbedecoder/unmapped_labels.tsv` also contains
  `kgmicrobe.trait:achromoviromycin` in `BacDive_Metabolite_production`, but
  the current record was created from kg-microbe metatraits rather than that
  MicrobeDecoder row.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, placeholder no-hit rows, generated indexes, ignored
  aggregate backups, and stale advisory batch rows.
- The `physicochemical_roles.SELECTIVE_AGENT` row is only a name-pattern
  prediction; no inspected source supports achromoviromycin as a selective
  medium agent.

## Completeness

- The placeholder status is explicitly documented in `notes` and
  `curation_history`.
- `chemical_properties` is correctly empty while the record has no exact
  external chemical identity.
- No component, environmental context, discussion, or dataset entry is required
  for the current placeholder decision.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Achromoviromycin.yaml`, remove or evidence the
  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion, then run
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen python scripts/validate_component_partonomy.py`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
