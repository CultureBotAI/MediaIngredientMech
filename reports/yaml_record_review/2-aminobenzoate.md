# `data/ingredients/mapped/2-aminobenzoate.yaml`

## Verdict

Needs curation, minor. The active synonym-grounded `CHEBI:16567` anthranilate
mapping and chemistry pass, but the top-level `notes` field still describes the
obsolete unmapped importer state.

## Identity

- Reviewed record: `data/ingredients/mapped/2-aminobenzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16567` with
  `ontology_mapping.ontology_id: CHEBI:16567`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16567`
  resolves to `anthranilate`, lists `2-aminobenzoate`, formula `C7H6NO2`, and
  an anion SMILES compatible with the stored `Nc1ccccc1C(=O)[O-]`.
- The one `microbedecoder` source occurrence is represented in
  `occurrence_statistics.source_occurrences`; the 0/0 top-level totals are
  expected because this source is non-media trait data.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Piperidinone.yaml data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml data/ingredients/mapped/2-_Methylthioethanol.yaml data/ingredients/mapped/2-aminobenzoate.yaml data/ingredients/mapped/2-aminopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-aminobenzoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-aminobenzoate` to `CHEBI:16567` row.

## Evidence

- The active ChEBI target confirms that `2-aminobenzoate` is an exact synonym of
  `CHEBI:16567` anthranilate and that the stored formula/SMILES describe the
  anion form.
- Stale: top-level `notes` still says there was no CAS-RN or CHEBI/NCIT match
  and curator review was needed, even though the record was promoted on
  2026-08-04.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 promotion precedes the 2026-08-04T02:54 import event.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the microbedecoder residual grounding, the active YAML/aggregate/SSSOM
  rows, and stale advisory rows, with no live contradiction of `CHEBI:16567`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, SMILES, and molecular weight are populated for the ChEBI/PubChem
  anion form.
- Empty component and role slots are acceptable for this single ChEBI anion.

## Recommended Edits

1. In `data/ingredients/mapped/2-aminobenzoate.yaml`, replace the stale `notes`
   text with a concise statement that the microbedecoder residual was promoted
   to `CHEBI:16567` through an exact ChEBI synonym match.
2. Leave the anion-specific `CHEBI:16567` identity in place; do not add neutral
   anthranilic-acid CAS data unless the identifier changes accordingly.
3. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-aminobenzoate.yaml`, `just validate-terms
   data/ingredients/mapped/2-aminobenzoate.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
