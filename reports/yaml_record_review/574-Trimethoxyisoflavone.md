# `data/ingredients/mapped/574-Trimethoxyisoflavone.yaml`

## Verdict

Pass with minor issues. The local CAS identity, PubChem CID, chemistry, SSSOM
registry row, and aggregate copy pass; one historic auto-backfill `changes`
string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/574-Trimethoxyisoflavone.yaml`.
- Identifier and grounding: `identifier: cas:1162-82-9` with
  `ontology_mapping.ontology_id: cas:1162-82-9`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `1162-82-9` to CID `136420`.
- PubChem CID `136420` reports formula `C18H16O5`, the stored SMILES, and the
  stored InChI, and its synonym list includes
  `5,7,4'-trimethoxyisoflavone`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-trimethoxybenzoate.yaml data/ingredients/mapped/56-dihydro-5-azathymidine.yaml data/ingredients/mapped/574-Trimethoxyisoflavone.yaml data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml data/ingredients/mapped/6-Hydroxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/574-Trimethoxyisoflavone.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, as expected for a CAS primary record. Engine A was skipped because
  `cas:` is not an OBO-resolvable prefix.
- The prior whole-corpus `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  run covered registry rows and passed with all id/label pairs corresponding.

## Evidence

- PubChem confirms the stored CAS, PubChem CID, formula, SMILES, InChI, and
  name for 5,7,4'-trimethoxyisoflavone.
- The SSSOM row maps `MIM:574-Trimethoxyisoflavone` to `cas:1162-82-9` with
  `skos:exactMatch`, `registry:cas`, and `CAS:1162-82-9` in `other`.
- The `AUTO_BACKFILL_PUBCHEM_CHEMISTRY` event's `changes` string truncates the
  InChI at `.../c1-20-12-6-4-11(5-7-12)14-10-23-`, but the live
  `chemical_properties.inchi` value is complete and agrees with PubChem.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, registry-triage row, OAK/OLS review rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, and `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_PUBCHEM_CHEMISTRY].changes` string in
  `data/ingredients/mapped/574-Trimethoxyisoflavone.yaml` so it no longer shows
  a truncated InChI. No identity, chemistry, or SSSOM edit is required.
