# `data/ingredients/mapped/Citramalate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder citramalate import is deliberately
grounded to the active generic dianion `CHEBI:13997`; its formula, InChI,
SMILES, one-count MicrobeDecoder source occurrence, SSSOM row, zero CultureMech
membership, and aggregate copy agree. The only active YAML defect is stale
top-level import prose that still says curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Citramalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:13997`,
  `ontology_mapping.ontology_id: CHEBI:13997`,
  `ontology_label: citramalate(2-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `citramalate(2-)` returns active `CHEBI:13997`
  labelled `citramalate(2-)`, plus stereospecific D- and L-citramalate sibling
  dianions that the bare MicrobeDecoder label does not select.
- PubChem lookup by `citramalate` returns the neutral acid and dianion; the
  dianion row has formula `C5H6O5-2` and the same `/p-2` standard InChI stored
  in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Citramalate` SSSOM row, the
  MicrobeDecoder source rows, matching aggregate/docs rows, and stale advisory
  rows that predate the populated ChEBI/PubChem formula and structure fields.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:13997` only in this active record.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:citramalate` in `BacDive_Metabolite_utilization` with count
  1, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:13997`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The top-level `notes` field still repeats the original unmapped import text:
  no CAS-RN or CHEBI/NCIT match and curator review needed. That text is stale
  after the `promote_resolved_unmapped` event and active ChEBI mapping.
- The record carries no role, component, or environment claims.

## Completeness

- The ChEBI identifier, formula, InChI, SMILES, MicrobeDecoder source
  occurrence, SSSOM row, aggregate copy, and docs row are populated and agree.
- The only active gap is the stale top-level note.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Citramalate.yaml`, replace the stale
  top-level `notes` with current provenance that summarizes the `CHEBI:13997`
  dianion promotion.
