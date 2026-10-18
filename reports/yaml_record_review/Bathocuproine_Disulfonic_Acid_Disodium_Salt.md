# `data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`

## Verdict

Needs curation, major. The CAS primary identity, PubChem-backed disodium salt
chemistry, CHEBI parent `skos:narrowMatch`, SSSOM registry rows, and aggregate
copy are coherent, but the salt record also carries a parent-acid ChEBI synonym
as an `EXACT_SYNONYM`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:52698-84-7` with
  `ontology_mapping.ontology_id: CHEBI:63934`,
  `ontology_label: bathocuproine disulfonic acid`,
  `ontology_source: CHEBI`, `mapping_quality: NARROW_MATCH`, and
  `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:63934` to
  `bathocuproine disulfonic acid`, and exact CHEBI label/synonym search for the
  full `Bathocuproine disulfonic acid disodium salt` label returned no exact
  term.
- PubChem resolves CAS `52698-84-7` to CID 15678335, formula
  `C26H18N2Na2O6S2`, and the same standard InChI stored under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Baicalein.yaml data/ingredients/mapped/Bakers_Yeast.yaml data/ingredients/mapped/Balhimycin.yaml data/ingredients/mapped/Bandamycin.yaml data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The authoritative SSSOM rows are the parent `skos:narrowMatch` to
  `CHEBI:63934`, the `skos:exactMatch` registry row to `cas:52698-84-7`, and
  the Rule B1 companion registry row to
  `kgmicrobe.compound:bathocuproine_disulfonic_acid_disodium_salt`.
- The absorbed `Bathocuproinedisulfonic acid disodium salt` spelling is exact
  for the PubChem CID 15678335 salt: PubChem lists it as a CID synonym together
  with CAS `52698-84-7`.
- The synonym
  `4,4'-(2,9-dimethyl-1,10-phenanthroline-4,7-diyl)dibenzenesulfonic acid`
  is an exact synonym of the parent `CHEBI:63934` acid. The salt record's own
  formula is `C26H18N2Na2O6S2`, so the acid-only label is not an exact synonym
  of this `cas:52698-84-7` disodium salt record.

## Completeness

- The CAS registry identifier, CAS number, PubChem CID, formula, InChI, SMILES,
  parent CHEBI grounding, registry SSSOM rows, duplicate-merge history, and
  aggregate copy are populated.
- No exact CHEBI identifier is required while exact OLS search still finds only
  the parent acid and no disodium salt term.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`,
  remove the parent-acid exact synonym
  `4,4'-(2,9-dimethyl-1,10-phenanthroline-4,7-diyl)dibenzenesulfonic acid` or
  move it to a non-exact parent-term note, then run `just sync-curated` and
  rebuild `mappings/ingredient_mappings.sssom.tsv` so the salt SSSOM rows no
  longer advertise the acid label as a subject synonym.
