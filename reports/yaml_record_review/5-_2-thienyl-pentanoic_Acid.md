# `data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml`

## Verdict

Pass, none. The local CAS identity, PubChem chemistry, SSSOM registry row, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml`.
- Identifier and grounding: `identifier: cas:21010-06-0` with
  `ontology_mapping.ontology_id: cas:21010-06-0`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem CID `152324` reports formula `C9H12O2S`, the stored SMILES, and the
  stored InChI for the same structure.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Hydroxyoctanoate.yaml data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml data/ingredients/mapped/5-aminovaleric_Acid.yaml data/ingredients/mapped/5-dehydro-D-gluconate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, as expected for a CAS primary record. Engine A was skipped because
  `cas:` is not an OBO-resolvable prefix.
- The prior whole-corpus `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  run covered registry rows and passed with all id/label pairs corresponding.

## Evidence

- PubChem CID `152324` lists `21010-06-0` as a synonym and reports the same
  `C9H12O2S` formula, SMILES, and InChI as the YAML record.
- The SSSOM row maps `MIM:5-_2-thienyl-pentanoic_Acid` to `cas:21010-06-0`
  with `skos:exactMatch`, `registry:cas`, `semapv:ManualMappingCuration`, and
  `CAS:21010-06-0` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, stale pre-alias rows for `MIM:5-~282-thienyl~29-pentanoic_Acid`, the
  maintained alias table, and ignored aggregate backups. The stale encoded slug
  is aliased to the current slug in `mappings/mim_curie_aliases.tsv`.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, and `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
