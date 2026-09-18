# `data/ingredients/mapped/Cis-aconitate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder cis-aconitate import is deliberately
grounded to the active trianion `CHEBI:16383`; its formula, InChI, SMILES,
58-count MicrobeDecoder source occurrence, SSSOM row, zero CultureMech
membership, and aggregate copy agree. The only active YAML defect is stale
top-level import prose that still says curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Cis-aconitate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16383`,
  `ontology_mapping.ontology_id: CHEBI:16383`,
  `ontology_label: cis-aconitate(3-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `cis-aconitate` returns active `CHEBI:16383`
  `cis-aconitate(3-)` and the adjacent neutral-acid sibling `CHEBI:32805`
  `cis-aconitic acid`; the local Edison-backed promotion explicitly chose the
  trianion term.
- PubChem lookup by `cis-aconitate` returns the neutral cis-aconitic-acid
  skeleton, and the stored ChEBI/PubChem formula `C6H3O6`, InChI charge layer
  `/p-3`, and anionic SMILES match the deprotonated `CHEBI:16383` form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `reports` found the active exact `MIM:Cis-aconitate` SSSOM row, the Edison
  research validation row, the MicrobeDecoder source rows, and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:16383` only in this active record.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:cis_aconitate` in `BacDive_Metabolite_utilization` with
  count 58, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:16383`
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

- Minor: in `data/ingredients/mapped/Cis-aconitate.yaml`, replace the stale
  top-level `notes` with current provenance that summarizes the
  `CHEBI:16383` trianion promotion.
