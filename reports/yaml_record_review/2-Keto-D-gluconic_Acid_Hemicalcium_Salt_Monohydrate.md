# `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`

## Verdict

Needs curation, blocker. The record label says monohydrate, but the active CAS,
formula, SMILES, InChI, and PubChem CID all resolve to an anhydrous calcium
2-ketogluconate rather than a water-containing monohydrate.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:3470-37-9` with
  `ontology_mapping.ontology_id: CHEBI:27469`,
  `ontology_mapping.ontology_label: 2-dehydro-D-gluconic acid`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official parent ChEBI check: `CHEBI:27469` resolves to anhydrous
  `2-dehydro-D-gluconic acid`, formula `C6H10O7`, so it is not an exact term
  for a calcium salt monohydrate.
- CAS/PubChem conflict: querying CAS `3470-37-9` resolves to CID `25113464`,
  `Calcium 2-ketogluconate`, formula `C12H18CaO14`, and an InChI without
  `.H2O`; the YAML stores the same anhydrous formula and an old adjacent
  PubChem CID `25113463`, whose synonyms also lack hydrate or monohydrate text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Hydroxypyridine.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml data/ingredients/mapped/2-Nitrophenol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed for the parent ChEBI CURIE.
- Whole-corpus checks run earlier in this review pass passed, including SSSOM
  invariants for the close parent plus exact CAS row; only the shared evidence
  validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:closeMatch` parent row to `CHEBI:27469` plus the exact
  `cas:3470-37-9` registry row, but that exact registry row uses the unsupported
  monohydrate label.

## Evidence

- The non-exact ChEBI parent is appropriate for a calcium salt form.
- Blocker: the exact registry identity is internally inconsistent. The record
  asserts that CAS `3470-37-9` is exact for the monohydrate label, while current
  PubChem resolves that CAS to an anhydrous calcium salt with formula
  `C12H18CaO14`.
- Major: the `CARBON_SOURCE` and `ENERGY_SOURCE` roles are supported only by
  provisional computational evidence, not by inspected formulation-specific
  evidence for this exact calcium salt form.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found old Edison rows that questioned
  the monohydrate state; that hydrate-state concern is still live in the active
  chemistry.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, InChI, and PubChem CID are populated, but they
  support an anhydrous salt rather than the record's monohydrate label.
- Empty component slots are acceptable once the exact supplied form is corrected.

## Recommended Edits

1. In
   `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml`,
   reconcile the preferred label, CAS RN, formula, SMILES, InChI, and PubChem
   CID so they all describe the same hydrate state.
2. Remove or directly substantiate the provisional `CARBON_SOURCE` and
   `ENERGY_SOURCE` roles.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
4. Re-run strict/LinkML validation, `scripts/validate_sssom_invariants.py`, and
   docs/export checks after the identity and role cleanup.
