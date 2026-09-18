# `data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml`

## Verdict

Needs curation, major. The CAS salt has the expected narrow parent grounding to
`CHEBI:86350`, and #326 fixed the formula, but the record still carries the
neutral parent acid's InChI, SMILES, and synonym as exact fields on the lithium
salt.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:7284-15-3` with
  `ontology_mapping.ontology_id: CHEBI:86350`,
  `ontology_mapping.ontology_label: 2-deoxy-D-ribonic acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official parent ChEBI check: the current EMBL-EBI ChEBI page for
  `CHEBI:86350` resolves to neutral `2-deoxy-D-ribonic acid`, formula
  `C5H10O5`, and the same acid InChI that still appears in the YAML.
- Exact PubChem check: CAS `7284-15-3` resolves to CID `154704589`,
  `2-Deoxy-D-ribonic acid lithium salt`, formula `C5H9LiO5`, SMILES
  `[Li+].C([C@@H]([C@@H](CO)O)O)C(=O)[O-]`, and an InChI with `.Li` and
  `q;+1/p-1`, all matching the salt rather than the parent acid.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxy-D-glucose.yaml data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml data/ingredients/mapped/2-Deoxycytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed for the parent ChEBI CURIE.
- Whole-corpus checks run earlier in this review pass passed, including SSSOM
  invariants for narrow parent plus exact registry rows; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:narrowMatch` row to `CHEBI:86350` plus exact registry rows for
  `cas:7284-15-3` and the local kg-microbe compound.

## Evidence

- The parent ChEBI page confirms that `CHEBI:86350` is the neutral parent acid,
  so a non-exact `skos:narrowMatch` is the right relationship for the lithium
  salt.
- The exact PubChem record confirms that the #326 formula repair to `C5H9LiO5`
  was correct.
- Major: `chemical_properties.inchi` and `chemical_properties.smiles` still
  describe the protonated parent acid and omit lithium, so they are not exact
  for CAS `7284-15-3`.
- Major: `2-deoxy-D-erythro-pentonic acid` is a ChEBI synonym of the neutral
  parent, not an exact synonym of the lithium salt, yet it is exported in
  docs/label-index output for the active salt.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found stale Edison rows that still
  mention the pre-#326 parent formula; those formula rows are stale, but their
  InChI/SMILES/synonym findings remain live.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Empty component and role slots are acceptable for this single salt.
- The exact CAS and local registry rows correctly preserve the salt identity
  alongside the non-exact parent ChEBI row.

## Recommended Edits

1. In `data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml`, replace
   the parent-acid InChI and SMILES with exact CAS `7284-15-3` lithium-salt
   structure values or remove them if the structure representation should not
   include disconnected salt components.
2. Remove `2-deoxy-D-erythro-pentonic acid` from the active salt's exact
   `synonyms`.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
4. Re-run strict/LinkML validation, `scripts/validate_sssom_invariants.py`, and
   docs/export checks after the structure and synonym cleanup.
