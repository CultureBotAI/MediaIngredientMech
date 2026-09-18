# `data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml`

## Verdict

Needs curation. The CultureBotHT CAS `22059-21-8` disambiguates the source
label to active `CHEBI:18053` `1-aminocyclopropanecarboxylic acid`, and the
current record, aggregate, SSSOM row, and docs exports agree on that mapping.
The remaining issue is an open `kgscan` discussion whose gap-scan citations
are not about this ChEBI entity or any unresolved claim on this record.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml`.
- Identifier and grounding: `identifier: CHEBI:18053` with
  `ontology_mapping.ontology_id: CHEBI:18053`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:18053`
  uses ChEBI ID `CHEBI:18053`, ChEBI name
  `1-aminocyclopropanecarboxylic acid`, formula `C4H7NO2`, net charge `0`,
  average mass `101.105`, CAS `22059-21-8`, and the same SMILES and InChI
  strings stored in `chemical_properties`.
- The apparent acid/carboxylate ambiguity is resolved by the imported CAS RN.
  ChEBI has a distinct conjugate-base term, `CHEBI:30526`
  `1-aminocyclopropanecarboxylate`, but the retained CultureBotHT
  `22059-21-8` registry number belongs to the neutral acid `CHEBI:18053`.
- The exact synonym
  `1-Aminocyclopropane-1-carboxylic acid` names the same ChEBI entity and is
  already exported as an SSSOM `other_label`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml data/ingredients/mapped/1-butanolCO2.yaml`:
  passed; 2 files scanned, 0 ERROR rows.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed the full product id/label gate; the reported plausibility warnings
  were non-blocking and all id/label pairs corresponded.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  the core record is synchronized. The aggregate has the same
  `1-aminocyclopropane-1-carboxylate` payload after excluding the
  per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-aminocyclopropane-1-carboxylate skos:exactMatch CHEBI:18053`, with
  object label `1-aminocyclopropanecarboxylic acid`, CAS `22059-21-8`, the
  exact synonym as `other_label`, and `validation_method`
  `OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:18053` identity; the label index marks the preferred term,
  exact synonym, and ontology label `unique`.

## Evidence

- The ontology mapping evidence is narrow enough: the record was created from
  the CultureBotHT CAS RN `22059-21-8`, and current ChEBI lists `22059-21-8`
  on `CHEBI:18053`.
- The `CAS_RN_LOOKUP` grade is the right mapping-quality value. It preserves
  the CAS-to-ChEBI provenance and avoids overstating a direct lexical match
  against the canonical ChEBI label.
- The `nutritional_roles.AMINO_ACID_SOURCE` claim is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from ChEBI amino-acid ancestry with confidence
  `0.7`; it is acceptable as a provisional coarse role because the evidence
  does not claim a narrower organism, medium, or metabolism-specific behavior.
- Minor: `discussions[0]` is not a record-specific knowledge gap. The DOI
  entry is about conifer root rot/damping-off, `PMID:40776541` is about the
  ginseng rhizosphere, `PMID:42028995` is about coal gangue, and
  `PMID:42197634` carries a broad food-production prompt. None is attached to
  a precise unresolved mapping, role, source-occurrence, or chemical-form
  question for 1-aminocyclopropanecarboxylic acid.
- `mappings/record_research_validation.tsv` still has two stale rows for this
  record. Direct ChEBI verification with the CultureBotHT CAS confirms the
  acid form, and literature evidence that ACC appears in DF-ACC minimal medium
  does not refute zero occurrences in the local source corpus.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:18053 -e 1-aminocyclopropane-1-carboxylate -e 1-aminocyclopropanecarboxylic -e 22059-21-8 -e kgscan-afcc7416ff5f -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, ignored
  aggregate backups, and no duplicate active YAML for `CHEBI:18053`.

## Completeness

- Empty component and source-occurrence slots are acceptable: the record
  denotes a single neutral ChEBI molecule and does not retain per-medium
  occurrence evidence from CultureBotHT.
- The supplied-form fields are complete enough for this CAS-grounded identity:
  the formula, SMILES, InChI, CAS RN, exact synonym, and canonical ChEBI label
  all resolve to the same neutral acid.
- `find . -path ./.git -prune -o \( -iname '*aminocyclopropane*' -o -iname '*butanol*' -o -iname '*carbon*dioxide*' \) -print`
  included ignored files and found only the reviewed record for
  `*aminocyclopropane*` among active YAML records.

## Recommended Edits

1. Remove or replace `kgscan-afcc7416ff5f` in
   `data/ingredients/mapped/1-aminocyclopropane-1-carboxylate.yaml` with a
   claim-attached discussion if an actual unresolved ACC evidence gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `1-aminocyclopropane-1-carboxylate` acid/protonation and occurrence-summary
   rows resolved.
3. No identifier, mapping predicate, mapping grade, exact synonym,
   chemical-property, ingredient-type, component, role, or SSSOM edit is
   needed for the active `CHEBI:18053` mapping.
