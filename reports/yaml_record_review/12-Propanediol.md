# `data/ingredients/mapped/12-Propanediol.yaml`

## Verdict

Needs curation. The CAS-derived `CHEBI:16997` identity is correct and complete,
but the record still has an unattached, generic `kgscan` discussion.

## Identity

- Reviewed record: `data/ingredients/mapped/12-Propanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16997` with
  `ontology_mapping.ontology_id: CHEBI:16997`, label `propane-1,2-diol`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16997`
  resolves to `propane-1,2-diol`, records synonym `1,2-Propanediol`, formula
  `C3H8O2`, SMILES `CC(O)CO`, the same InChI stored in
  `chemical_properties`, and CAS RN `57-55-6`.
- Mapping-method boundary: `CAS_RN_LOOKUP` is appropriate because the current
  CAS RN was the explicit CultureBotHT-to-ChEBI lookup key. The exact SSSOM
  predicate remains correct under `MAPPING_SEMANTICS.md` Rule D.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/12-Propanediol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/12-Propanediol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/11-Biphenyl-2-ol.yaml data/ingredients/mapped/112-trichloroethane.yaml data/ingredients/mapped/1122-Tetrachloroethane.yaml data/ingredients/mapped/12-Propanediol.yaml data/ingredients/mapped/12-dichloropropane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  matched after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:16997` row with CAS `57-55-6` and raw absorbed truncation labels in
  `other_label`.

## Evidence

- Current ChEBI verifies the CAS-backed exact identity and stored structure.
- `2-propandiol` and `1,2-propandiol` are both explicitly stored as `RAW_TEXT`
  artifacts rather than exact synonyms, which preserves source resolution
  without claiming they are normalized chemical names.
- Minor: `kgscan-2db2ffbbe7ca` is an unattached bundle of generic IBD,
  biopropanol, HMO, and plasmid-fitness gap sentences. Those snippets do not
  describe an unresolved mapping, synonym, CAS, structure, role, or occurrence
  question for propane-1,2-diol.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  stale validation rows that predate CAS regrading, and no duplicate active YAML
  for `CHEBI:16997`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN, formula, SMILES, and InChI are populated and match current ChEBI.

## Recommended Edits

1. Remove or replace `kgscan-2db2ffbbe7ca` with a claim-attached,
   propane-1,2-diol-specific discussion if an actual unresolved gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be live, regenerate
   it or clear the stale 1,2-propanediol rows.
3. No ChEBI, CAS RN, structure, SSSOM, aggregate, or docs edit is needed for the
   active identity.
