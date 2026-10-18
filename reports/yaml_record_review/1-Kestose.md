# `data/ingredients/mapped/1-Kestose.yaml`

## Verdict

Needs curation. The active ChEBI identity, exact synonym, structural chemistry,
single-ingredient type, nutritional-role inference, SSSOM row, and flat docs
exports agree for `1-kestose`, but the record still carries an open `kgscan`
discussion seeded from mostly unrelated gap-scan literature. That discussion
needs pruning or retargeting before this is a clean record-level review pass.

## Identity

- Reviewed record: `data/ingredients/mapped/1-Kestose.yaml`.
- Identifier and grounding: `identifier: CHEBI:16885` with
  `ontology_mapping.ontology_id: CHEBI:16885`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16885`
  uses ChEBI ID `CHEBI:16885`, ChEBI name `1-kestose`, formula `C18H32O16`,
  neutral charge, CAS `470-69-9`, the same SMILES string, and the same InChI
  string stored in `chemical_properties`; it classifies the term as a
  trisaccharide.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:16885` to `1-kestose`; its formula, charge, SMILES, InChI, and CAS
  xref match the record, and metadata did not report an `is_obsolete` or
  `deprecated` flag.
- Source provenance: the only retained mapping evidence is the original
  CultureBotHT database match. There are no source occurrences for this record,
  so `occurrence_statistics.total_occurrences: 0` and `media_count: 0` do not
  conflict with a populated `source_occurrences` list.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-Kestose.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-Kestose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-Kestose.yaml`:
  passed; 1 file scanned, 0 ERROR rows.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  the core record is synchronized. The aggregate has the same `1-Kestose`
  payload after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:1-Kestose skos:exactMatch CHEBI:16885`, with object label
  `1-kestose`, CAS `470-69-9`, the beta-D-fructofuranosyl exact synonym, and
  `validation_method` `OAK+OLS:chebi|CONFIRMED|2026-07-07`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:16885` identity; the label index marks the preferred label and
  exact synonym `unique`.

## Evidence

- The ontology mapping is exact: the source label is `1-Kestose`, and current
  ChEBI resolves the same structure-specific trisaccharide as `CHEBI:16885`.
- The exact synonym
  `beta-D-fructofuranosyl-(2->1)-beta-D-fructofuranosyl alpha-D-glucopyranoside`
  names the same ChEBI entity and is exported as the only SSSOM `other_label`.
- The chemical properties describe the same ChEBI term: formula, neutral
  charge, CAS, SMILES, and InChI all matched local OAK and the official ChEBI
  page inspected for `CHEBI:16885`.
- The `nutritional_roles.CARBON_SOURCE` claim is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from ChEBI carbohydrate ancestry with confidence
  `0.7`; it is acceptable as a provisional coarse role because the evidence
  does not claim a narrower organism, medium, or metabolism-specific behavior.
- Minor: `discussions[0]` is not a durable, record-specific knowledge gap.
  `PMID:41373036` and `DOI:10.21203/rs.3.rs-6822283/v1` discuss
  lignocellulose turnover, and `PMID:41367416` discusses heterogeneous human
  cohorts without a 1-kestose-specific prompt. `PMID:40284226` does mention
  1-kestose, but it is about rat cholesterol and triglyceride levels and has no
  populated `attaches_to` target.
- `mappings/record_research_validation.tsv` still has a stale exact-mapping
  conflict for this record. Direct ChEBI verification confirmed `CHEBI:16885`
  as the exact same linkage-defined stereochemical entity, so the report row no
  longer describes a live SSSOM defect.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:16885 -e "1-Kestose" -e "1-kestose" -e "470-69-9" -e "kgscan-f77a72b7ddb7" -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows and no
  duplicate active YAML for `CHEBI:16885`.

## Completeness

- Empty component and source-occurrence slots are acceptable: the record denotes
  a single ChEBI molecule, not a mixture, and the current YAML does not retain
  per-medium provenance for the CultureBotHT CAS import.
- The supplied-form fields are complete enough for this identity: hydrate,
  salt, charge, formula, SMILES, InChI, and CAS are all aligned with the active
  ChEBI term.
- `find . -path ./.git -prune -o -iname '*kestose*' -print` included ignored
  files and found only `./data/ingredients/mapped/1-Kestose.yaml` among local
  active records.

## Recommended Edits

1. Remove `PMID:41373036`, `DOI:10.21203/rs.3.rs-6822283/v1`, and
   `PMID:41367416` from `data/ingredients/mapped/1-Kestose.yaml`, or replace
   the whole `kgscan-f77a72b7ddb7` discussion with a record-specific knowledge
   gap attached to the role, mapping, or other exact claim it is meant to
   qualify.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the `1-Kestose`
   exact-mapping row resolved so this already-verified ChEBI mapping stops
   reappearing as `P2` review work.
3. No identity, synonym, chemical-property, ingredient-type, component, or
   SSSOM edit is needed for the active `CHEBI:16885` mapping.
