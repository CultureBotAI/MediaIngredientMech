# `data/ingredients/mapped/(R)-lactate.yaml`

## Verdict

Needs curation. The exact ChEBI identity, the `D-lactate` raw synonym, the
anion formula/charge, and the synchronized SSSOM/docs rows are sound. The live
record appears to omit the absorbed `D-lactate` microbedecoder occurrence row,
so its non-media BacDive provenance is materially undercounted.

## Identity

- Reviewed record: `data/ingredients/mapped/(R)-lactate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16004` with
  `ontology_mapping.ontology_id: CHEBI:16004`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16004`
  uses ChEBI ID `CHEBI:16004`, ChEBI name `(R)-lactate`, ASCII name
  `(R)-lactate`, formula `C3H5O3`, net charge `-1`, average mass `89.070`, the
  same SMILES string, and the same InChI string stored in
  `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:16004` to `(R)-lactate`; aliases include `D-lactate`,
  `D-2-hydroxypropanoate`, and `D-2-hydroxypropionate`; metadata did not report
  an `is_obsolete` or `deprecated` flag.
- ChEBI boundaries checked: `CHEBI:16004` is the conjugate base of
  `(R)-lactic acid`, the enantiomer of `(S)-lactate`, and a parent of
  methylated/salt lactate records that the hidden search found under
  `data/ingredients/mapped/`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(R\)-lactate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(R\)-lactate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(R\)-lactate.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`: exact equality for the `(R)-lactate` entry; curation history length is `5` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28R~29-lactate skos:exactMatch CHEBI:16004`, with object label
  `(R)-lactate`, other text `D-lactate`, and `validation_method`
  `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:16004` identity; the label index marks both `(R)-lactate` and
  `D-lactate` `unique` for this record.

## Evidence

- The ontology mapping evidence is narrow enough for the active preferred term:
  the original microbedecoder source label was exactly `(R)-lactate`, and
  ChEBI currently resolves that ASCII name to `CHEBI:16004`.
- The folded synonym is also correct: ChEBI lists `D-lactate` as a synonym of
  `CHEBI:16004`, and `mappings/edison_residual_merges.tsv` records the
  `D-lactate -> CHEBI:16004` merge rationale.
- The chemical properties describe the same ChEBI anion: formula, net charge,
  mass, SMILES, and InChI all matched the official ChEBI page inspected for
  `CHEBI:16004`.
- Major: `occurrence_statistics.source_occurrences` lists the
  `kgmicrobe.trait:r_lactate` row, count `19`, but the record's own
  `MERGED_FROM_UNMAPPED_DUPLICATE` event says `D-lactate` was absorbed from
  `kgmicrobe.trait:d_lactate`, and `data/custom/microbedecoder/unmapped_labels.tsv`
  has that second row with count `17`. A curator cannot recover all BacDive
  `(R)`/`D`-lactate prevalence from the YAML record today.
- Minor: the `REVIEWED_AND_PROMOTED` event has a coarse
  `2026-08-04T00:00:00+00:00` timestamp that sorts before the
  `2026-08-04T03:08:34.142678+00:00` `FLAGGED_FOR_REVIEW` event it resolved.
  The list order still preserves the actual append order.
- `mappings/record_research_validation.tsv` still has stale rows for this
  record: direct ChEBI verification has now confirmed `CHEBI:16004`, and
  `ingredient_type` is no longer missing.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:16004 -e "(R)-lactate" -e r_lactate -e D-lactate -e d_lactate -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the active record, the `Methyl_(R)-lactate` ester,
  other distinct lactate salt records, the stranded `D-lactate` source row, and
  no unexamined active duplicate for `CHEBI:16004`.

## Completeness

- `D-lactate` is appropriately retained as a `RAW_TEXT` synonym because it came
  from a separate microbedecoder source row and is an exact ChEBI synonym for
  the same `(R)` anion.
- Empty component and role slots are acceptable: this is a single lactate anion
  record with no mixture partonomy, and BacDive metabolite
  production/utilization columns are not themselves claim-level evidence for a
  narrower nutritional role.
- `find . -path ./.git -prune -o -iname '*lactate*' -print` included ignored
  files and found salts, esters, a generic `Lactate.yaml`, and this
  stereospecific record; those filenames were checked as distinct lactate
  forms rather than missing duplicates.

## Recommended Edits

1. Update the maintained per-record input
   `data/ingredients/mapped/(R)-lactate.yaml` so
   `occurrence_statistics.source_occurrences` accounts for both microbedecoder
   rows: `kgmicrobe.trait:r_lactate` with count `19` and
   `kgmicrobe.trait:d_lactate` with count `17`. Append a curation-history event
   that names the `data/custom/microbedecoder` rows as the source, then run
   `just sync-curated` and regenerate the flat docs exports.
2. On a future provenance cleanup pass, fix or annotate the coarse
   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic
   order as well as append order.
3. Regenerate `mappings/record_research_validation.tsv` from its maintained
   recipe, or mark the stale `(R)-lactate` rows resolved, after the
   occurrence-source fix lands.
