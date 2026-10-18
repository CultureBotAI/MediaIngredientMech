# `data/ingredients/mapped/2-deoxyadenosine.yaml`

## Verdict

Needs curation, minor. The active exact `CHEBI:17256` grounding and chemistry
pass, but the top-level `notes` field still describes the obsolete unmapped
importer state.

## Identity

- Reviewed record: `data/ingredients/mapped/2-deoxyadenosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17256` with
  `ontology_mapping.ontology_id: CHEBI:17256`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:17256`
  resolves to `2'-deoxyadenosine` and lists formula `C10H13N5O3`.
- The 15 `microbedecoder` source occurrences are represented in
  `occurrence_statistics.source_occurrences`; the 0/0 top-level totals are
  expected because this source is non-media trait data.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml data/ingredients/mapped/2-butanolCO2.yaml data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml data/ingredients/mapped/2-dehydro-D-gluconate.yaml data/ingredients/mapped/2-deoxyadenosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-deoxyadenosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-deoxyadenosine` to `CHEBI:17256` row.

## Evidence

- The active ChEBI target confirms the mapped anhydrous nucleoside identity and
  formula.
- The sibling `2-Deoxyadenosine_Monohydrate` record keeps its monohydrate CAS
  identity separate and only points to `CHEBI:17256` as a parent, so there is no
  hydrate collapse in this anhydrous record.
- Stale: top-level `notes` still say there was no CAS-RN or CHEBI/NCIT match
  and curator review was needed, even though the record was promoted on
  2026-08-04.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 promotion precedes the 2026-08-04T02:54 import event.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows, the intentionally separate
  monohydrate sibling, and stale advisory rows, with no live contradiction of
  `CHEBI:17256`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, SMILES, and molecular weight are populated for the active
  anhydrous nucleoside form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. In `data/ingredients/mapped/2-deoxyadenosine.yaml`, replace the stale `notes`
   text with a concise statement that the microbedecoder residual was promoted
   to `CHEBI:17256` through an exact local ChEBI verification.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-deoxyadenosine.yaml`, `just validate-terms
   data/ingredients/mapped/2-deoxyadenosine.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
