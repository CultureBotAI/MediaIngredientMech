# `data/ingredients/mapped/1122-Tetrachloroethane.yaml`

## Verdict

Needs curation. The exact mapping to `CHEBI:36026` is not supported by the raw
source label `2-tetrachloroethane`: repository mapping semantics explicitly
treat that fragment as ambiguous between `CHEBI:34024`
`1,1,1,2-tetrachloroethane` and `CHEBI:36026`
`1,1,2,2-tetrachloroethane`.

## Identity

- Reviewed record: `data/ingredients/mapped/1122-Tetrachloroethane.yaml`.
- Current identifier and grounding: `identifier: CHEBI:36026` with
  `ontology_mapping.ontology_id: CHEBI:36026`, label
  `1,1,2,2-tetrachloroethane`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI checks: current ChEBI resolves `CHEBI:36026` to
  `1,1,2,2-tetrachloroethane` with CAS RN `79-34-5` and also resolves
  `CHEBI:34024` to the same-formula sibling `1,1,1,2-tetrachloroethane` with
  CAS RN `630-20-6`.
- Source boundary: the only source occurrence preserved here is the
  microbedecoder raw label `2-tetrachloroethane`, and that label omits enough
  locants to distinguish the two tetrachloroethane isomers.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1122-Tetrachloroethane.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1122-Tetrachloroethane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/11-Biphenyl-2-ol.yaml data/ingredients/mapped/112-trichloroethane.yaml data/ingredients/mapped/1122-Tetrachloroethane.yaml data/ingredients/mapped/12-Propanediol.yaml data/ingredients/mapped/12-dichloropropane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- The generated `mappings/ingredient_mappings.sssom.tsv` exact row and docs rows
  faithfully publish the unsupported `CHEBI:36026` identity.

## Evidence

- The active mapping evidence is contradicted by local policy and by the
  record's own earlier review history. `MAPPING_SEMANTICS.md` names
  `2-tetrachloroethane` as an under-specified label that reaches both
  `CHEBI:34024` and `CHEBI:36026` and should get neither mapping row.
- `mappings/truncated_locants.tsv` still lists `2-tetrachloroethane` as the
  ambiguous `UNMAPPED_0785` fragment.
- The current repair explanation says no other compound ends in
  `2-tetrachloroethane`, but `1,1,1,2-tetrachloroethane` does. The Edison note
  embedded in the same record also states that the string does not uniquely
  identify a chemical.
- The raw ambiguous label is exported in SSSOM `other_label` and generated label
  indexes as a synonym of `CHEBI:36026`, so the unsupported choice is visible in
  final products.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  the active ambiguity rule in `MAPPING_SEMANTICS.md`, and the
  `mappings/truncated_locants.tsv` row.

## Completeness

- `notes` still describe the pre-repair unmapped state.
- `ingredient_type` and `chemical_properties` are absent, but those are
  secondary to the identity problem.
- The record has the original microbedecoder count, so the source occurrence is
  traceable; it is just not exact enough for the current ChEBI target.

## Recommended Edits

1. Move `data/ingredients/mapped/1122-Tetrachloroethane.yaml` back to an
   ambiguous/unmapped state for the source label `2-tetrachloroethane`, remove
   the exact `CHEBI:36026` identity row from SSSOM, and preserve
   `CHEBI:34024`/`CHEBI:36026` only as rejected or explanatory candidates.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `data/curated/unmapped_ingredients.yaml`, SSSOM, docs, and label indexes
   through the maintained sync/publish recipes so `2-tetrachloroethane` no
   longer resolves uniquely to `CHEBI:36026`.
3. Update the repair note that says `CHEBI:36026` is the only possible
   reconstruction; it conflicts with `MAPPING_SEMANTICS.md` and ChEBI's
   `CHEBI:34024` sibling.
