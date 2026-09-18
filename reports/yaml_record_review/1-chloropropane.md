# `data/ingredients/mapped/1-chloropropane.yaml`

## Verdict

Pass with minor issues. `CHEBI:747004` now resolves to active
`1-chloropropane`, its current ChEBI structure matches the stored formula,
SMILES, InChI, and mass, and the recovered SSSOM surface form
`n-propyl chloride` is an exact name for the same compound. Remaining issues
are stale `record_research_validation.tsv` rows and optional CAS enrichment.

## Identity

- Reviewed record: `data/ingredients/mapped/1-chloropropane.yaml`.
- Identifier and grounding: `identifier: CHEBI:747004` with
  `ontology_mapping.ontology_id: CHEBI:747004`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:747004`
  uses ChEBI ID `CHEBI:747004`, ChEBI name `1-chloropropane`, formula
  `C3H7Cl`, net charge `0`, average mass `78.542`, SMILES `CCCCl`, and the
  same InChI stored in `chemical_properties`.
- Source provenance: the MicrobeDecoder source label was exactly
  `1-chloropropane`; `occurrence_statistics.source_occurrences[0]` retains the
  `BacDive_Metabolite_utilization` count of `1`.
- The backfilled `RAW_TEXT` synonym `n-propyl chloride` is exact for
  1-chloropropane and is exported as the only SSSOM `other_label`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-chloropropane.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-chloropropane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-chlorobutane.yaml data/ingredients/mapped/1-chloropropane.yaml data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`:
  passed; 3 files scanned, 0 ERROR rows.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed the full product id/label gate earlier in this review pass.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `1-chloropropane` entry.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-chloropropane skos:exactMatch CHEBI:747004`, with object label
  `1-chloropropane`, `n-propyl chloride` as `other_label`, and the August 4
  manual approval.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:747004` identity; the label index marks both the preferred label
  and `n-propyl chloride` `unique`.

## Evidence

- The ontology mapping is exact. The preferred term and current ChEBI label are
  the same neutral 1-haloalkane, and the high `747004` accession is now
  resolvable in current ChEBI and the term validator.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, average mass, SMILES, and InChI all matched the official page.
- The non-media MicrobeDecoder occurrence is traceable through
  `source_occurrences`; retaining `total_occurrences: 0` and `media_count: 0`
  is consistent with the BacDive-derived non-media counting convention used
  elsewhere in the corpus.
- `mappings/record_research_validation.tsv` still has stale rows arguing that
  `CHEBI:747004` was unverified, that the mapping quality was uncertain, and
  that `ingredient_type` was unset. Current ChEBI and
  `ingredient_type: SINGLE_INGREDIENT` make those rows stale. The CAS row for
  `540-54-5` is optional enrichment pending direct source verification.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:747004 -e 1-chloropropane -e "n-propyl chloride" -e CCCCl -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, ignored
  aggregate backups, historical false-positive-demotion files, and no duplicate
  active YAML for `CHEBI:747004`.

## Completeness

- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy and no retained claim-level evidence for
  a nutritional or physicochemical role.
- `n-propyl chloride` covers the important recovered alternate label. No
  additional exact synonym is needed for SSSOM correctness.
- `find . -path ./.git -prune -o \( -iname '*chlorobutane*' -o -iname '*chloropropane*' -o -iname '*methylimidazolium*' \) -print`
  included ignored files and found no second active `1-chloropropane` record.

## Recommended Edits

1. No identity, mapping, synonym, chemical-property, occurrence,
   ingredient-type, SSSOM, or docs edit is needed in
   `data/ingredients/mapped/1-chloropropane.yaml`.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `1-chloropropane` CURIE, quality, and ingredient-type rows resolved.
3. On a future enrichment pass, verify and add CAS `540-54-5` from an
   authoritative source.
