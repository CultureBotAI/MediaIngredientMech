# `data/ingredients/mapped/(2)-D-lyxose.yaml`

## Verdict

Needs curation. The core identity is now correct: the damaged raw
`(2)-D-lyxose` string is retained as `RAW_TEXT`, the preferred identity is
`D-lyxose`, the record maps to `CHEBI:62318`, and the folded
`D-(-)-lyxose`/`CHEBI:16789` aldehydo record is represented as a rejected
tombstone. The live record still appears to miss the main microbedecoder
`D-lyxose` occurrence row, so its non-media BacDive provenance is materially
undercounted.

## Identity

- Reviewed record: `data/ingredients/mapped/(2)-D-lyxose.yaml`.
- Identifier and grounding: `identifier: CHEBI:62318` with
  `ontology_mapping.ontology_id: CHEBI:62318`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: current `CHEBI:62318` is `D-lyxose`, defined by ChEBI
  as any lyxose with D-configuration; it has no structure section on its ChEBI
  page, and ChEBI lists `aldehydo-D-lyxose`, `D-lyxofuranose`, and
  `D-lyxopyranose` as narrower incoming children.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:62318` to `D-lyxose` and did not report `is_obsolete` or
  `deprecated`.
- The supplied CAS form is coherent with the merge history: current
  `CHEBI:16789` is `aldehydo-D-lyxose`, ChEBI defines it as the open-chain
  aldehyde form of D-lyxose, ChEBI lists it as a child of `CHEBI:62318`, and
  ChEBI lists CAS `1114-34-7` on `CHEBI:16789`.
- Boundary checked: `data/ingredients/mapped/D-_-lyxose.yaml` is the rejected
  aldehydo tombstone that was merged into this record, and
  `data/ingredients/mapped/L-lyxose.yaml` is the opposite enantiomer at
  `CHEBI:62320`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(2\)-D-lyxose.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(2\)-D-lyxose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(2\)-D-lyxose.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`: exact equality for the `D-lyxose` entry; curation history length is `6` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~282~29-D-lyxose skos:exactMatch CHEBI:62318`, with object label
  `D-lyxose` and `validation_method` `OLS:chebi|SYNONYM_ENRICH|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` publish
  the active `D-lyxose` row, the rejected `D-(-)-lyxose` row, and unique label
  index entries for `(2)-D-lyxose`, `D-(-)-lyxose`, `D-lyxo-pentose`, and
  `D-lyxose` resolving to the active `CHEBI:62318` record.

## Evidence

- The damaged raw source string is preserved at the narrowest place available:
  `(2)-D-lyxose` is a `RAW_TEXT` synonym, while the preferred term was corrected
  to the current ChEBI label.
- The folded aldehydo labels are evidence-backed synonyms. ChEBI `CHEBI:16789`
  carries `D-lyxose`, `D-Lyx`, and `D-lyxo-pentose`, and the rejected
  `D-_-lyxose.yaml` tombstone records its `MERGED_INTO` transition.
- `supplied_form[0].cas_rn: 1114-34-7` is placed on the exact commercial/open
  aldehydo form rather than on `chemical_properties` for the broader
  `CHEBI:62318` class term, matching the merge note that ChEBI attaches the CAS
  to `CHEBI:16789`.
- Major: `occurrence_statistics.source_occurrences` lists only the damaged
  `kgmicrobe.trait:2_d_lyxose` row, count `1`, from
  `data/custom/microbedecoder/unmapped_labels.tsv`; the same upstream file also
  has `kgmicrobe.trait:d_lyxose`, label `D-lyxose`, count `159`, and
  `data/custom/microbedecoder/ingredient_candidates.tsv` marks that direct
  label as already represented. A curator cannot recover all BacDive
  D-lyxose prevalence from the YAML record today.
- Minor: record-level `notes` still say the original imported record had no
  CAS-RN or CHEBI/NCIT match and needed curator review. Later curation history
  superseded that import state.
- `mappings/record_research_validation.tsv` still has stale Edison rows about
  the old label, old slug, old `EXACT_MATCH` grade, old missing
  `ingredient_type`, and the one-count occurrence state; the current label,
  raw-text synonym, `SYNONYM_MATCH` grade, and `ingredient_type` have resolved
  all except the occurrence-count concern.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:62318 -e CHEBI:16789 -e "(2)-D-lyxose" -e D-lyxose -e D-lyxo-pentose -e 2_d_lyxose -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the active record, the rejected aldehydo tombstone,
  the `L-lyxose` enantiomer boundary, the stranded microbedecoder direct
  `D-lyxose` source row, and no unexamined active duplicate for the same
  `CHEBI:62318` identity.

## Completeness

- Leaving `chemical_properties` absent is acceptable because the active ChEBI
  term is a D-lyxose class term, not one structure-bearing tautomer.
- Empty component and role slots are acceptable: this is a single sugar record
  with no mixture partonomy, and the BacDive metabolite-utilization source
  column is not itself claim-level evidence for a narrower nutritional role.
- `find . -path ./.git -prune -o -iname '*lyxose*' -print` included ignored
  files and found only this record plus the `D-_-lyxose` rejected tombstone and
  `L-lyxose` enantiomer among live YAML files.

## Recommended Edits

1. Update the maintained per-record input
   `data/ingredients/mapped/(2)-D-lyxose.yaml` so
   `occurrence_statistics.source_occurrences` accounts for both microbedecoder
   rows: `kgmicrobe.trait:d_lyxose` with count `159` and
   `kgmicrobe.trait:2_d_lyxose` with count `1`. Append a curation-history event
   that names the `data/custom/microbedecoder` rows as the source, then run
   `just sync-curated` and regenerate the flat docs exports.
2. Remove or replace the stale top-level `notes` import sentence when the
   occurrence fix is made; the later `curation_history` already records why the
   damaged source string was corrected and the aldehydo record was folded in.
3. Regenerate `mappings/record_research_validation.tsv` from its maintained
   recipe, or mark the stale `(2)-D-lyxose` rows resolved, after the
   occurrence-source fix lands.
