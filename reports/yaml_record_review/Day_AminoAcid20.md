# `data/ingredients/mapped/Day_AminoAcid20.yaml`

## Verdict

Pass. The local stock-solution identity still has no OBO exact replacement, its
20 component rows match the CultureBotHT Mixes-tab recipe at 0.5 mM each, the
amino-acid-source role is source-backed, and the final SSSOM registry row has
no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Day_AminoAcid20.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:day_aminoacid20` with the same
  `ontology_mapping.ontology_id`, `ontology_label: Day_AminoAcid20`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: STOCK_SOLUTION`,
  `solution_type: AMINO_ACID_MIX`, and `mapping_status: MAPPED`.
- Live OLS exact search across CHEBI, NCIT, MeSH, FOODON, and ENVO for
  `Day_AminoAcid20` returned 0 results on 2026-09-16, preserving the local
  registry identity premise.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Das_Macro_Solution.yaml data/ingredients/mapped/Das_Vitamin_Cocktail.yaml data/ingredients/mapped/Daunorubicin.yaml data/ingredients/mapped/Day_AminoAcid20.yaml data/ingredients/mapped/Decanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Direct Engine A term validation over the same 5 files exited 1 on the local
  `kgmicrobe.ingredient` records. The documented `just validate-terms` wrapper
  intentionally skips non-OBO prefixes for Engine A; local registry rows are
  covered by strict schema validation, the SSSOM invariant check, and
  product-level id/label validation.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; all
  generated `docs/data` artifacts matched their producers and every curated
  label was resolvable.

## Evidence

- The CultureBotHT Mixes CSV exported from the source Google Sheet contains
  the 20 Day_AminoAcid20 component rows exactly as stored: `L-Alanine`,
  `L-Arginine`, `L-Asparagine`, `L-Aspartic Acid`, `L-Cysteine`,
  `Glutamic acid`, `L-Glutamine`, `Glycine`, `L-Histidine`,
  `L-Isoleucine`, `L-Leucine`, `L-Lysine`, `L-Methionine`,
  `L-Phenylalanine`, `L-Proline`, `L-Serine`, `L-Threonine`,
  `L-Tryptophan`, `L-tyrosine`, and `L-Valine`, each at `0.5 mM`.
- The `component_assertion` evidence points to the same Mixes-tab range and
  its `RECIPE_TRANSCRIPTION`/`COMPLETE` method describes has-part composition,
  not false identity.
- The `AMINO_ACID_SOURCE` role is supported by `DATABASE_ENTRY` evidence that
  cites the CultureBotHT Mixes tab and is no longer a provisional
  computational role.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for
  `kgmicrobe.ingredient:day_aminoacid20`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Day_AminoAcid20` to `kgmicrobe.ingredient:day_aminoacid20` with
  `skos:exactMatch`, object source `kgm:ingredient`, and empty `other`.

## Completeness

- The record has the expected local stock identity, raw CultureBotHT synonym,
  complete 20-component recipe decomposition, source-backed nutritional role,
  11 CultureBotHT occurrences, and final SSSOM registry row.
- Empty chemical properties, supplied-form details, and environmental contexts
  are appropriate for this stock mixture.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
