# `data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml`

## Verdict

Pass, none. The local CAS identity, PubChem CID/name resolution, populated
chemistry, SSSOM registry row, and aggregate copy pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml`.
- Identifier and grounding: `identifier: cas:247167-54-0` with
  `ontology_mapping.ontology_id: cas:247167-54-0`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `247167-54-0` to the stored CID `10131246`, and CID
  `10131246` lists `(5z)-4-bromo-5-(bromomethylene)-2(5h)-furanone` as a
  synonym.
- The stored SMILES and InChI represent the same `C5H2Br2O2` dibrominated
  furanone with the explicit `5Z` alkene stereo.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-trimethoxybenzoate.yaml data/ingredients/mapped/56-dihydro-5-azathymidine.yaml data/ingredients/mapped/574-Trimethoxyisoflavone.yaml data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml data/ingredients/mapped/6-Hydroxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, as expected for a CAS primary record. Engine A was skipped because
  `cas:` is not an OBO-resolvable prefix.
- The prior whole-corpus `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  run covered registry rows and passed with all id/label pairs corresponding.

## Evidence

- PubChem confirms the stored CAS/CID pair and exact stereospecific name for
  `(5z)-4-bromo-5-(bromomethylene)-2(5h)-furanone`.
- PubChem's property endpoint returned an empty body for CID `10131246`, so the
  bounded official check for this review verified CAS, CID, and synonyms rather
  than re-fetching formula/SMILES/InChI. The populated formula is internally
  consistent with the stored SMILES and InChI.
- The SSSOM row maps `MIM:5z-4-bromo-5-_Bromomethylene-2_5h-furanone` to
  `cas:247167-54-0` with `skos:exactMatch`, `registry:cas`, and
  `CAS:247167-54-0` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, maintained MIM alias for the escaped original slug, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, and `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
