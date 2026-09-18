# `data/ingredients/mapped/Beta-gentiobiose.yaml`

## Verdict

Needs curation, major. `CHEBI:71422` is a real ChEBI beta-gentiobiose term and
the structure fields match that term, but the microbedecoder source label does
not support exact identity to the reducing-end beta anomer rather than generic
gentiobiose.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-gentiobiose.yaml`.
- Current grounding: `identifier: CHEBI:71422` with
  `ontology_mapping.ontology_id: CHEBI:71422`,
  `ontology_label: beta-D-Glcp-(1->6)-beta-D-Glcp`,
  `ontology_source: CHEBI`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: MAPPED`.
- OLS confirms that `CHEBI:71422` is current, has `beta-gentiobiose` as a
  related synonym, and carries the formula, InChI, SMILES, mass, KEGG
  `C08240`, and CAS `554-91-6` values used by the record.
- OLS also returns the broader existing local target `CHEBI:28066`
  `gentiobiose` for an unqualified `gentiobiose` search.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 580 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The same search found five `mappings/record_research_validation.tsv`
  diagnostics disputing the `CHEBI:71422` identity. Both independent review
  lanes disputed the exact match; the strongest rows recommend generic
  `CHEBI:28066` `gentiobiose` rather than the current reducing-end beta term.
- Live OLS search for `MICRO:0000921` confirms that MicrO models
  `beta-gentiobiose`, `gentibiose`, and `gentiobiose` as synonyms on one
  `gentiobiose assimilation assay`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` contain separate
  BacDive metabolite-utilization labels for `gentiobiose` and
  `beta-gentiobiose`; the `beta-gentiobiose` label alone is not enough to
  assert the exact reducing-end anomer encoded by `CHEBI:71422`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The current ChEBI target, formula, InChI, SMILES, SSSOM row, and aggregate
  copy are internally synchronized.
- Major gap: the exact ChEBI row overstates the MicrobeDecoder/BacDive source
  identity. The maintained fix should either merge this raw label into the
  existing `CHEBI:28066` `Gentibiose` record or demote this record for expert
  review if the source really must retain separate beta-anomer semantics.
- Minor gap: top-level `notes` still say no CAS or CHEBI/NCIT match was found
  and that curator review was needed, even though the record was later
  promoted to `MAPPED`.

## Recommended Edits

- Major: update the maintained mapped record and synchronized aggregate/SSSOM
  surfaces so this raw MicrobeDecoder label no longer publishes an exact
  `MIM:Beta-gentiobiose` to `CHEBI:71422` identity. Prefer merging into
  `data/ingredients/mapped/Gentibiose.yaml` if review agrees that the BacDive
  source intended generic gentiobiose.
- Minor: when the identity is repaired, replace the stale import note in
  `data/ingredients/mapped/Beta-gentiobiose.yaml` or remove it as part of the
  merge.
- Re-run `uv run --frozen python scripts/validate_strict.py`, the
  `linkml-term-validator validate-data ... --labels` check for the affected
  records, and `uv run --frozen python scripts/validate_sssom_invariants.py`
  after synchronization.
