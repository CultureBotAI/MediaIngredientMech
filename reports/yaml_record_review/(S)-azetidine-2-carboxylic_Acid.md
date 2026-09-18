# `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml`

## Verdict

Pass with minor issues. The record maps the microbedecoder
`(S)-azetidine-2-carboxylic acid` source label to the active, structure-bearing
ChEBI term for the same stereoisomer, and the per-record, aggregate, SSSOM, MIM
CURIE alias, and docs surfaces are synchronized. Remaining concerns are stale
triage/report rows, optional missing synonyms and CAS, and a coarse
curation-history timestamp that sorts before the review flag it resolved.

## Identity

- Reviewed record:
  `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:6198` with
  `ontology_mapping.ontology_id: CHEBI:6198`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:6198`
  uses ChEBI ID `CHEBI:6198`, ChEBI name and ASCII name
  `(S)-azetidine-2-carboxylic acid`, formula `C4H7NO2`, net charge `0`,
  average mass `101.105`, the same SMILES string, and the same InChI string
  stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:6198` to `(S)-azetidine-2-carboxylic acid`; aliases include
  `(2S)-azetidine-2-carboxylic acid`,
  `(S)-(-)-Azetidine-2-carboxylic acid`,
  `(S)-2-azetidinecarboxylic acid`, `Azetidyl-2-carboxylic acid`, and
  `L-Azetidine 2-carboxylic acid`; metadata did not report an `is_obsolete` or
  `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:s_azetidine_2_carboxylic_acid`, source label
  `(S)-azetidine-2-carboxylic acid`, source column
  `BacDive_Metabolite_production`, and count `1`, matching
  `occurrence_statistics.source_occurrences[0]`.
- Boundary checked: the official ChEBI page relates `CHEBI:6198` to the parent
  `azetidine-2-carboxylic acid`, the enantiomer
  `(R)-azetidine-2-carboxylic acid` `CHEBI:38109`, and the tautomer
  `(S)-azetidine-2-carboxylate zwitterion` `CHEBI:231534`. No separate active
  YAML record for any azetidine sibling was present in this repository.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(S\)-azetidine-2-carboxylic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(S\)-azetidine-2-carboxylic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(S\)-azetidine-2-carboxylic_Acid.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `(S)-azetidine-2-carboxylic Acid` entry; curation
  history length is `4` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28S~29-azetidine-2-carboxylic_Acid skos:exactMatch CHEBI:6198`, with
  object label `(S)-azetidine-2-carboxylic acid` and `validation_method`
  `OLS:chebi|CONFIRMED|2026-09-02`.
- `mappings/mim_curie_alias_seeds.tsv` and
  `mappings/mim_curie_aliases.tsv` carry the historical spelling alias
  `MIM:(S)-azetidine-2-carboxylic_Acid` to the escaped
  `MIM:~28S~29-azetidine-2-carboxylic_Acid` SSSOM subject.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:6198` identity; the label index marks
  `(S)-azetidine-2-carboxylic Acid` `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is exactly `(S)-azetidine-2-carboxylic acid`, and
  ChEBI currently resolves that ASCII name to `CHEBI:6198`.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, mass, SMILES, and InChI all matched the official ChEBI page
  inspected for `CHEBI:6198`.
- The zero media counts are not evidence of absence from microbedecoder. The
  non-media count is retained under `source_occurrences`, so the BacDive-derived
  prevalence remains traceable without inflating `total_occurrences`.
- Minor: the `REVIEWED_AND_PROMOTED` event has a coarse
  `2026-08-04T00:00:00+00:00` timestamp that sorts before the
  `2026-08-04T03:08:34.142678+00:00` `FLAGGED_FOR_REVIEW` event it resolved.
  The list order still preserves the actual append order.
- `mappings/record_research_validation.tsv` still has stale or now-satisfied
  rows for this record: direct ChEBI verification has now confirmed
  `CHEBI:6198`, `ingredient_type` is no longer missing, and the proposed
  `L-azetidine-2-carboxylic acid`, `AZC`, and CAS `2133-34-8` additions are
  useful enrichment but not mapping blockers.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:6198 -e "(S)-azetidine-2-carboxylic Acid" -e "(S)-azetidine-2-carboxylic acid" -e s_azetidine_2_carboxylic_acid -e azetidine-2-carboxylic -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows
  and no contradictory active curated record for `CHEBI:6198`.

## Completeness

- `synonyms: []` is acceptable for record identity because the only upstream
  source label is the preferred term modulo case. Adding the ChEBI/Kegg
  `L-Azetidine 2-carboxylic acid` synonym or literature-backed `AZC` short form
  would be reasonable future enrichment but is not needed for SSSOM
  correctness.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and the BacDive metabolite-production
  source column is not itself claim-level evidence for a narrower nutritional
  role.
- `find . -path ./.git -prune -o -iname '*azetidine*' -print` included ignored
  files and found only
  `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml` among YAML
  records.

## Recommended Edits

1. No identity, mapping, occurrence, or chemical-property edit is needed in
   `data/ingredients/mapped/(S)-azetidine-2-carboxylic_Acid.yaml`.
2. On a future provenance cleanup pass, fix or annotate the coarse
   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic
   order as well as append order.
3. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `(S)-azetidine-2-carboxylic_Acid` rows resolved so stale field-missing rows
   and now-satisfied direct-ChEBI checks stop re-queuing this record.
4. On a future evidence-enrichment pass, consider adding CAS `2133-34-8`,
   exact synonym `L-Azetidine 2-carboxylic acid`, and acronym `AZC` after its
   paper evidence is checked against this exact stereoisomer.
