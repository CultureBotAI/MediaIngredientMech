# `data/ingredients/mapped/(S)-mandelic_Acid.yaml`

## Verdict

Pass with minor issues. The record maps the microbedecoder
`(S)-mandelic acid` source label to the active, structure-bearing ChEBI term
for the same neutral stereoisomer, and the per-record, aggregate, SSSOM, and
docs surfaces are synchronized. Remaining concerns are stale triage/report
rows, an optional missing synonym, and a coarse curation-history timestamp that
sorts before the review flag it resolved.

## Identity

- Reviewed record: `data/ingredients/mapped/(S)-mandelic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32800` with
  `ontology_mapping.ontology_id: CHEBI:32800`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:32800`
  uses ChEBI ID `CHEBI:32800`, ChEBI name and ASCII name `(S)-mandelic acid`,
  formula `C8H8O3`, net charge `0`, average mass `152.149`, the same SMILES
  string, and the same InChI string stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:32800` to `(S)-mandelic acid`; aliases include
  `(2S)-hydroxy(phenyl)acetic acid`,
  `(S)-2-Hydroxy-2-phenylacetic acid`, `(S)-Mandelic acid`,
  `(S)-Mandelsaeure`, `(S)-alpha-hydroxybenzeneacetic acid`, and
  `L-mandelic acid`; metadata did not report an `is_obsolete` or
  `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:s_mandelic_acid`, source label `(S)-mandelic acid`, source
  column `BacDive_Metabolite_utilization`, and count `2`, matching
  `occurrence_statistics.source_occurrences[0]`.
- Boundaries checked: `data/ingredients/mapped/Mandelic_Acid.yaml` is the
  broader `CHEBI:35825` `mandelic acid` record; the official ChEBI page says
  `CHEBI:32800` is a `mandelic acid`, is conjugate acid of `(S)-mandelate`
  `CHEBI:17756`, and is enantiomer of `(R)-mandelic acid` `CHEBI:17656`.
  `4-Hydroxymandelic_Acid_Monohydrate.yaml` and `Vanillylmandelic_Acid.yaml`
  are substituted mandelic-acid derivatives, not duplicates.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(S\)-mandelic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(S\)-mandelic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(S\)-mandelic_Acid.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `(S)-mandelic Acid` entry; curation history length is
  `4` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28S~29-mandelic_Acid skos:exactMatch CHEBI:32800`, with object label
  `(S)-mandelic acid` and `validation_method`
  `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:32800` identity; the label index marks `(S)-mandelic Acid`
  `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is exactly `(S)-mandelic acid`, and ChEBI
  currently resolves that ASCII name to `CHEBI:32800`.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, mass, SMILES, and InChI all matched the official ChEBI page
  inspected for `CHEBI:32800`.
- The zero media counts are not evidence of absence from microbedecoder. The
  non-media count is retained under `source_occurrences`, so the BacDive-derived
  prevalence remains traceable without inflating `total_occurrences`.
- Minor: the `REVIEWED_AND_PROMOTED` event has a coarse
  `2026-08-04T00:00:00+00:00` timestamp that sorts before the
  `2026-08-04T03:08:34.142678+00:00` `FLAGGED_FOR_REVIEW` event it resolved.
  The list order still preserves the actual append order.
- `mappings/record_research_validation.tsv` still has stale or now-satisfied
  rows for this record: direct ChEBI verification has now confirmed
  `CHEBI:32800`, `ingredient_type` is no longer missing, and the row claiming
  that `source_occurrences` conflicts with zero `total_occurrences` does not
  match the current BacDive/non-media counting convention.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e s_mandelic_acid -e CHEBI:32800 -e "(S)-mandelic Acid" -e "(S)-mandelic acid" -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows
  and no contradictory active curated record for `CHEBI:32800`.

## Completeness

- `synonyms: []` is acceptable for record identity because the only upstream
  source label is the preferred term modulo case. Adding `L-mandelic acid` from
  current ChEBI would be reasonable future enrichment but is not needed for
  SSSOM correctness.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and the BacDive metabolite-utilization
  source column is not itself claim-level evidence for a narrower nutritional
  role.
- `find . -path ./.git -prune -o -iname '*mandelic*' -print` included ignored
  files and found only generic, stereospecific, and substituted sibling terms
  among active YAML records.

## Recommended Edits

1. No identity, mapping, occurrence, or chemical-property edit is needed in
   `data/ingredients/mapped/(S)-mandelic_Acid.yaml`.
2. On a future provenance cleanup pass, fix or annotate the coarse
   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic
   order as well as append order.
3. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `(S)-mandelic_Acid` rows resolved so stale field-missing rows, now-satisfied
   direct-ChEBI checks, and the stale non-media occurrence complaint stop
   re-queuing this record.
4. On a future evidence-enrichment pass, consider adding exact synonym
   `L-mandelic acid` from current ChEBI.
