# `data/ingredients/mapped/Halomicin.yaml`

## Verdict

Needs curation. The local placeholder identity remains appropriate because no
exact external grounding or local duplicate is available, but the
`SELECTIVE_AGENT` role is only a curated-name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Halomicin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:halomicin` with the
  same local `ontology_mapping.ontology_id`,
  `ontology_source: kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Role facet: `SELECTIVE_AGENT` with `COMPUTATIONAL_PREDICTION` evidence from a
  curated media-role name pattern.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H3bo3.yaml data/ingredients/mapped/HOMOPIPES.yaml data/ingredients/mapped/Haemin.yaml data/ingredients/mapped/Halomicin.yaml data/ingredients/mapped/Hans_1000x_Minerals.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.compound` CURIE is local to MIM and outside the OBO/CAS scope of
  this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, matching
  aggregate copies, generated products, row-review TSVs that keep the local
  placeholder pending curator promotion, and the final SSSOM row.
- Fresh OLS4 exact search did not find a `Halomicin` class; it found only
  related MeSH classes for `halomicin B` and `halomicins`.
- PubChem name lookup for `Halomicin` returned no CID.
- The final SSSOM publishes one exact local registry row from `MIM:Halomicin`
  to `kgmicrobe.compound:halomicin`.
- Major: the `SELECTIVE_AGENT` facet is supported only by
  `reference_type: COMPUTATIONAL_PREDICTION` from a name-pattern rule.

## Completeness

- The local placeholder identifier, exact local SSSOM row, and row-review
  evidence are complete for a placeholder retained until external promotion is
  possible.
- The role facet is incomplete until a curator either supplies external
  evidence for halomicin as a selective agent or removes the provisional role.

## Recommended Edits

- Major: review the `SELECTIVE_AGENT` facet and either replace the
  name-pattern prediction with an external database/literature source or remove
  the unsupported role.
