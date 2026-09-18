# `data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml`

## Verdict

Needs curation. `MICRO:0000567` is an active generic heart-infusion-agar class,
but this record is catalog-specific and final SSSOM exports other vendor
catalog variants as exact synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml`.
- Identifier and grounding: `identifier: MICRO:0000567` with
  `ontology_mapping.ontology_id: MICRO:0000567`, label
  `heart infusion agar`, source `MICRO`, `mapping_quality: SYNONYM_MATCH`,
  `match_level: NORMALIZED`, and `mapping_status: MAPPED`.
- Occurrence statistics: `total_occurrences: 1` and `media_count: 1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Harmol.yaml data/ingredients/mapped/Harmol_Hydrochloride.yaml data/ingredients/mapped/Hcl.yaml data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml data/ingredients/mapped/Hecogenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped for this file because the
  `MICRO` target is outside the CHEBI/OBO subset used in this batch.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `MICRO:0000567` as active `heart infusion agar`; its definition
  denotes the generic organic-rich solid medium containing heart infusion and
  tryptose.
- The record preferred term preserves a BD catalog number, and both stored
  synonyms are other vendor catalog labels: `Heart Infusion Agar (Difco)` and
  `Heart infusion agar (Eiken)`.
- Major: final SSSOM publishes
  `MIM:Heart_Infusion_Agar_BD_211065 skos:exactMatch MICRO:0000567`, erasing
  the BD catalog boundary rather than preserving a local catalog-specific
  subject with a broader generic parent.
- Major: final SSSOM exports the Difco and Eiken catalog labels as exact
  synonyms of the BD-specific subject.

## Completeness

- The generic MICRO target is active and relevant.
- The record is incomplete until it separates catalog-specific surface forms
  from the generic `heart infusion agar` medium class.

## Recommended Edits

- Major: reground the BD 211065 record as a local catalog-specific identity with
  a parent or close generic relationship to `MICRO:0000567`, or demote the
  catalog suffix if the record is intended to represent generic heart infusion
  agar.
- Major: suppress or retype the Difco and Eiken catalog aliases so they no
  longer publish as exact synonyms of the BD-specific subject.
