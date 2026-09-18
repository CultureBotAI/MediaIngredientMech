# `data/ingredients/mapped/Fermented_Rumen_Extract.yaml`

## Verdict

Pass with a minor provenance issue. The record deliberately preserves
Fermented Rumen Extract as a local undefined-mixture ingredient with a
kg-microbe registry identity and no asserted has-part decomposition, but the
top-level `notes` still carry the stale import-era "Curator review needed"
text.

## Identity

- Reviewed record: `data/ingredients/mapped/Fermented_Rumen_Extract.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:fermented_rumen_extract`, matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- The August 2026 history records the intended identity progression from
  MicrobeDecoder residual import to a local registry identity, and the #369
  migration corrected the prior false partonomy by removing rumen fluid as an
  active component.
- `occurrence_statistics` correctly keeps the 3 MicrobeDecoder
  BacDive-metabolite-utilization occurrences in `source_occurrences`; it does
  not inflate CultureMech `total_occurrences` or `media_count`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl3_X_6_H2o.yaml data/ingredients/mapped/Fepo4.yaml data/ingredients/mapped/Fermented_Rumen_Extract.yaml data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `just validate-terms`/Engine A was intentionally not run for this record
  because `kgmicrobe.ingredient:` is a local non-OBO prefix; the final SSSOM
  row was covered by the SSSOM invariant validator.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  registry identifier, fallback ontology mapping, MicrobeDecoder source
  occurrence, `UNDEFINED_MIXTURE` classification, absent components, and #369
  mapping evidence as the per-record YAML.
- The curated
  `mappings/microbedecoder_residual_research_decomposition.tsv` row for
  `UNMAPPED_0711` names Fermented Rumen Extract as a single undefined
  rumen-derived ingredient rather than a decomposed stock.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fermented_Rumen_Extract` to
  `kgmicrobe.ingredient:fermented_rumen_extract` with `skos:exactMatch`, uses
  `kgm:ingredient` as `object_source`, and exports no `other` noise.
- Minor: the top-level `notes` still say "no CAS-RN or CHEBI/NCIT match.
  Curator review needed." That sentence is stale after the August fallback
  registry promotion and the #369 partonomy repair.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Fermented_Rumen_Extract`, `fermented_rumen_extract`, and `Fermented Rumen
  Extract` found the active YAML, aggregate copy, final SSSOM row,
  MicrobeDecoder residual triage/decomposition rows, the component-partonomy
  migration special case, old ignored aggregate backups, and no active
  component assertion for this record. A hidden `find` outside `.git` found no
  checked-in research artifact at the curation-history `research/ingredients`
  path.

## Completeness

- The local identity, undefined-mixture classification, MicrobeDecoder source
  occurrence, no-component state, and registry SSSOM row are populated
  consistently.
- Empty chemical properties, nutritional roles, physicochemical roles,
  cellular-metabolic roles, environmental context, discussions, and components
  are acceptable for this local unresolved mixture record.

## Recommended Edits

- Minor: replace the stale import-era top-level `notes` in
  `data/ingredients/mapped/Fermented_Rumen_Extract.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
