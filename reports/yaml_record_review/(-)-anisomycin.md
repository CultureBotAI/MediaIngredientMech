# `data/ingredients/mapped/(-)-anisomycin.yaml`

## Verdict

Pass with a minor queue/reporting issue. The curated record, aggregate copy,
SSSOM row, and published docs rows all consistently denote `CHEBI:338412`
`(-)-anisomycin`; the only follow-up is to clear stale Edison validation rows
that still describe pre-`ingredient_type` state or ask for a ChEBI identity
confirmation that this review has now performed.

## Identity

- Reviewed record: `data/ingredients/mapped/(-)-anisomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:338412` with
  `ontology_mapping.ontology_id: CHEBI:338412`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:338412`
  uses ChEBI ID `CHEBI:338412`, ChEBI name `(-)-anisomycin`, ASCII name
  `(-)-anisomycin`, IUPAC name
  `(2R,3S,4S)-4-hydroxy-2-(4-methoxybenzyl)pyrrolidin-3-yl acetate`,
  formula `C14H19NO4`, average mass `265.309`, the same SMILES string, and the
  same InChI string stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:338412` to `(-)-anisomycin`; `entity_metadata_map` for the term did
  not report an `is_obsolete` or `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:anisomycin`, source label `(-)-anisomycin`, source columns
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity`, and count
  `10`, matching `occurrence_statistics.source_occurrences[0]`.
- The ASCII preferred term is equivalent to ChEBI's ASCII name; the official
  display name uses a Unicode minus only as a glyph difference.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(-\)-anisomycin.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(-\)-anisomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(-\)-anisomycin.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`: exact equality for the `(-)-anisomycin` entry; curation history length is `5` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28-~29-anisomycin skos:exactMatch CHEBI:338412`, with object label
  `(-)-anisomycin` and `validation_method` `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:338412`/`(-)-anisomycin` identity; the label index marks the
  label `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is exactly `(-)-anisomycin`, and ChEBI currently
  resolves that ASCII name to `CHEBI:338412`.
- The chemical properties describe the same ChEBI term: formula, mass, SMILES,
  and InChI all matched the official ChEBI page inspected for `CHEBI:338412`.
- The zero media counts are not evidence of absence from microbedecoder. The
  non-media count is retained under `source_occurrences`, so the BacDive-derived
  prevalence remains traceable without inflating `total_occurrences`.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:338412 -e "(-)-anisomycin" -e anisomycin -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows and
  no contradictory curated record.
- `mappings/record_research_validation.tsv` still has two Edison rows for this
  record:
  - `P1 CURIE_REFUTED`: asked a curator to confirm that current ChEBI
    `CHEBI:338412` denotes `(2R,3S,4S)` anisomycin and is not obsolete or
    merged. The current ChEBI page and local OAK check satisfy that bounded
    concern for this review.
  - `P3 FIELD_MISSING`: says `ingredient_type` is unset. That row is stale;
    the record now has `ingredient_type: SINGLE_INGREDIENT`.

## Completeness

- `synonyms: []` is acceptable here because the only upstream source label is
  the preferred term; no broader, hydrate, salt, or raw-text variant was found
  that needs to be retained.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and this review found no inspected
  ingredient-role literature that should be attached.
- `find . -path ./.git -prune -o -iname '*anisomycin*' -print` included ignored
  files and found only `data/ingredients/mapped/(-)-anisomycin.yaml`; there is
  no local anisomycin-named research report alongside the live record.

## Recommended Edits

1. No edit is needed in `data/ingredients/mapped/(-)-anisomycin.yaml`.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the two
   `(-)-anisomycin` rows resolved so the stale P3 and now-satisfied P1 do not
   keep re-queuing this record.
