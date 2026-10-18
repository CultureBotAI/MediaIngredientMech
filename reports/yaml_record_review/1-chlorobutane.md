# `data/ingredients/mapped/1-chlorobutane.yaml`

## Verdict

Pass with minor issues. `CHEBI:747005` now resolves to active
`1-chlorobutane`, its current ChEBI structure matches the stored formula,
SMILES, InChI, and mass, and the per-record YAML, aggregate, SSSOM row, and
docs exports agree. Remaining work is cleanup outside this record: stale
validation TSV rows still reflect the old high-accession false positive, and
CAS/synonym enrichment would be useful but not required for identity.

## Identity

- Reviewed record: `data/ingredients/mapped/1-chlorobutane.yaml`.
- Identifier and grounding: `identifier: CHEBI:747005` with
  `ontology_mapping.ontology_id: CHEBI:747005`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:747005`
  uses ChEBI ID `CHEBI:747005`, ChEBI name `1-chlorobutane`, formula
  `C4H9Cl`, net charge `0`, average mass `92.569`, SMILES `CCCCCl`, and the
  same InChI stored in `chemical_properties`.
- Source provenance: the MicrobeDecoder source label was exactly
  `1-chlorobutane`; `occurrence_statistics.source_occurrences[0]` retains the
  `BacDive_Metabolite_utilization` count of `1`.
- Boundary checked: the similarly named active records found by bounded search
  are other chloroalkane or chloropropane labels, not duplicates of
  `1-chlorobutane`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-chlorobutane.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-chlorobutane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  exact equality for the `1-chlorobutane` entry.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-chlorobutane skos:exactMatch CHEBI:747005`, with object label
  `1-chlorobutane` and the August 4 manual approval.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:747005` identity; the label index marks `1-chlorobutane`
  `unique`.

## Evidence

- The ontology mapping is exact. The preferred term and current ChEBI label are
  the same neutral 1-haloalkane, and the high `747005` accession is now
  resolvable in current ChEBI and the term validator.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, average mass, SMILES, and InChI all matched the official page.
- The non-media MicrobeDecoder occurrence is traceable through
  `source_occurrences`; retaining `total_occurrences: 0` and `media_count: 0`
  is consistent with the BacDive-derived non-media counting convention used
  elsewhere in the corpus.
- `mappings/record_research_validation.tsv` still has stale rows arguing that
  `CHEBI:747005` was unverified, that the occurrence summary was
  contradictory, and that `ingredient_type` was unset. Current ChEBI, the
  retained source occurrence, and `ingredient_type: SINGLE_INGREDIENT` make
  those rows stale. The CAS row for `109-69-3` is optional enrichment pending
  direct source verification.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:747005 -e 1-chlorobutane -e CCCCCl -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, ignored
  aggregate backups, historical false-positive-demotion files, and no duplicate
  active YAML for `CHEBI:747005`.

## Completeness

- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy and no retained claim-level evidence for
  a nutritional or physicochemical role.
- `synonyms: []` is non-blocking. Current ChEBI has exact aliases such as
  `butyl chloride` and `N-butyl chloride` that would improve search coverage,
  but the exact preferred label already grounds the record.
- `find . -path ./.git -prune -o \( -iname '*chlorobutane*' -o -iname '*chloropropane*' -o -iname '*methylimidazolium*' \) -print`
  included ignored files and found no second active `1-chlorobutane` record.

## Recommended Edits

1. No identity, mapping, chemical-property, occurrence, ingredient-type, SSSOM,
   or docs edit is needed in `data/ingredients/mapped/1-chlorobutane.yaml`.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `1-chlorobutane` CURIE, quality, occurrence, and ingredient-type rows
   resolved.
3. On a future enrichment pass, verify and add exact aliases such as
   `butyl chloride` and CAS `109-69-3` from an authoritative source.
