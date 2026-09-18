# `data/ingredients/mapped/Capreomycin.yaml`

## Verdict

Pass. The MicrobeDecoder import is exactly grounded to active `CHEBI:3371`
capreomycin, and its generalized ChEBI formula/structure bundle,
MicrobeDecoder occurrence provenance, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Capreomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3371`,
  `ontology_mapping.ontology_id: CHEBI:3371`,
  `ontology_label: capreomycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3371` returns active label `capreomycin` and the
  generalized formula `C25H43N14O7R`, matching the local ChEBI/PubChem backfill.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` records the exact
  `CHEBI:3371` label match that promoted this MicrobeDecoder row back to
  `MAPPED`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Capreomycin` SSSOM row and
  matching aggregate/docs rows.
- The record has 0/0 media occurrences and a separate MicrobeDecoder
  `source_occurrences` count of 6 across antibiotic resistance, antibiotic
  sensitivity, and metabolite-production columns; no CultureMech recipe use is
  implied.

## Completeness

- The exact ChEBI identifier, generalized formula, InChI, SMILES, molecular
  weight, single-ingredient classification, MicrobeDecoder provenance, SSSOM
  row, aggregate copy, and docs row are populated.
- No role is asserted, which is appropriate for the current evidence.

## Recommended Edits

- None for this record.
