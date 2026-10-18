# `data/ingredients/mapped/2-aminopentanoic_Acid.yaml`

## Verdict

Pass with minor issues. The active `CHEBI:19475` identity, microbedecoder
provenance, and chemistry pass; only non-monotonic curation history timestamps
and stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-aminopentanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:19475` with
  `ontology_mapping.ontology_id: CHEBI:19475`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:19475`
  resolves to `2-aminopentanoic acid`, lists `norvaline`, formula `C5H11NO2`,
  and SMILES compatible with the stored `CCCC(N)C(=O)O`.
- The three `microbedecoder` source occurrences are represented in
  `occurrence_statistics.source_occurrences`; the 0/0 top-level totals are
  expected because this source is non-media trait data.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Piperidinone.yaml data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml data/ingredients/mapped/2-_Methylthioethanol.yaml data/ingredients/mapped/2-aminobenzoate.yaml data/ingredients/mapped/2-aminopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-aminopentanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-aminopentanoic_Acid` to `CHEBI:19475` row.

## Evidence

- The active ChEBI target confirms the mapped identity, formula, and SMILES for
  `2-aminopentanoic acid`.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  asked for direct ChEBI verification or `ingredient_type` enrichment; the
  current ChEBI page resolves the term, and `ingredient_type` is populated.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the microbedecoder source rows, active YAML/aggregate/SSSOM rows, and
  stale advisory rows, with no live contradiction of `CHEBI:19475`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, SMILES, and molecular weight are populated for the active
  chemical form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:19475` uncertainty no longer implies pending
   work.
2. Optionally repair the same-day 2026-08-04 curation-history timestamp ordering
   if an audit-order cleanup batch touches this record later.
3. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-aminopentanoic_Acid` record.
