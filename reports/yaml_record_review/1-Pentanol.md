# `data/ingredients/mapped/1-Pentanol.yaml`

## Verdict

Needs curation. The record correctly keeps a CAS-derived exact mapping from
the CultureBotHT `1-Pentanol` label to active `CHEBI:44884` `pentan-1-ol`,
and the August `CAS_RN_LOOKUP` regrade accurately preserves how that mapping
was established. The remaining live problem is an open `kgscan` discussion
whose gap-scan evidence is generic flavor/VOC or nanocarrier literature rather
than an actionable issue attached to this ingredient record.

## Identity

- Reviewed record: `data/ingredients/mapped/1-Pentanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:44884` with
  `ontology_mapping.ontology_id: CHEBI:44884`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:44884`
  uses ChEBI ID `CHEBI:44884`, ChEBI name `pentan-1-ol`, formula `C5H12O`,
  net charge `0`, average mass `88.150`, CAS `71-41-0`, and the same SMILES
  and InChI strings stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:44884` to `pentan-1-ol` and includes `1-pentanol` in its alias list.
  The record's source label and the ChEBI primary name are exact synonyms for
  the same linear C5 primary alcohol.
- Boundary checked: the hidden/ignored-inclusive filename search found
  `CyclopentanolCO2.yaml` as the only similarly named active YAML record; it is
  a carbon dioxide cosubstrate entry for a cyclic alcohol and not a duplicate
  of linear `1-Pentanol.yaml`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-Pentanol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-Pentanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-Pentanol.yaml`:
  passed; 1 file scanned, 0 ERROR rows.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  the core record is synchronized. The aggregate has the same `1-Pentanol`
  payload after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-Pentanol skos:exactMatch CHEBI:44884`, with object label
  `pentan-1-ol`, CAS `71-41-0`, and `validation_method`
  `OAK+OLS:chebi|CONFIRMED|2026-07-07`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:44884` identity; the label index marks both `1-Pentanol` and
  `pentan-1-ol` `unique`.

## Evidence

- The ontology mapping evidence is narrow enough: the record was created from
  the CultureBotHT CAS RN `71-41-0`, and current ChEBI lists `71-41-0` on
  `CHEBI:44884`.
- The `CAS_RN_LOOKUP` grade is more precise than a lexical grade for this
  record. The preferred term `1-Pentanol` appears as a ChEBI synonym, but the
  curation history states that the current retained mapping was resolved by CAS
  xref, and the SSSOM predicate remains `skos:exactMatch`.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, CAS, SMILES, and InChI all matched the official ChEBI page inspected
  for `CHEBI:44884`.
- Minor: `discussions[0]` is not a record-specific knowledge gap.
  `PMID:42278216` discusses diatom-based nanocarriers,
  `PMID:42073201` and `PMID:40946651` carry broad flavor-formation mechanism
  gaps, and `PMID:42193735` is a volatile-organic-compound mixture prompt.
  None is attached to a precise unresolved mapping, role, source-occurrence, or
  chemical-form question for `1-Pentanol`.
- `mappings/record_research_validation.tsv` still has stale or optional rows
  for this record. Direct ChEBI verification refutes the stale `CURIE_REFUTED`
  row, and the blank `synonyms` list is an enrichment opportunity rather than a
  final-SSSOM defect because the ontology label already exports `pentan-1-ol`.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:44884 -e 1-Pentanol -e pentan-1-ol -e 71-41-0 -e kgscan-fedfdc7a75ff -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, ignored
  aggregate backups, and no duplicate active YAML for `CHEBI:44884`.

## Completeness

- Empty component, role, and source-occurrence slots are acceptable: this record
  denotes a single neutral ChEBI molecule, has no imported per-medium
  occurrence, and does not need a mixture partonomy.
- `synonyms: []` is non-blocking. Adding exact ChEBI aliases such as
  `n-pentanol` and `pentan-1-ol` would improve search coverage, but the current
  identity and SSSOM row are already recoverable through the preferred term,
  canonical ontology label, and CAS RN.
- `find . -path ./.git -prune -o -iname '*pentanol*' -print` included ignored
  files and found only `./data/ingredients/mapped/1-Pentanol.yaml` plus
  `./data/ingredients/mapped/CyclopentanolCO2.yaml` among active records.

## Recommended Edits

1. Remove or replace `kgscan-fedfdc7a75ff` in
   `data/ingredients/mapped/1-Pentanol.yaml` with a 1-pentanol-specific,
   claim-attached discussion if an actual unresolved evidence gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the `1-Pentanol`
   `CURIE_REFUTED` row resolved and downgrade the synonym row to optional
   enrichment.
3. On a future synonym-enrichment pass, consider adding exact ChEBI aliases for
   `n-pentanol` and `pentan-1-ol`.
4. No identifier, mapping predicate, mapping grade, chemical-property,
   ingredient-type, component, or SSSOM edit is needed for the active
   `CHEBI:44884` mapping.
