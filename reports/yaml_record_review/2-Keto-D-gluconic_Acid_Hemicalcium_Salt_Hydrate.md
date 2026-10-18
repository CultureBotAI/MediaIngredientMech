# `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml`

## Verdict

Needs curation, major. The exact CAS for the unspecified hydrate resolves to a
water-containing calcium 2-ketogluconate, and the `skos:closeMatch` parent row
is appropriate, but the record lacks the exact CAS-backed formula/structure,
exports the separate monohydrate as an exact label, and asserts nutritional
roles from only provisional computational evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:1040352-40-6` with
  `ontology_mapping.ontology_id: CHEBI:27469`,
  `ontology_mapping.ontology_label: 2-dehydro-D-gluconic acid`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official parent ChEBI check: `CHEBI:27469` resolves to anhydrous
  `2-dehydro-D-gluconic acid`, formula `C6H10O7`, so it is not an exact term
  for the calcium salt hydrate.
- Exact PubChem check: CAS `1040352-40-6` resolves to CID `17749212`,
  `Calcium D-fructosonate--water (1/2/1)`, formula `C12H20CaO15`, a SMILES
  string with a water component, and a synonym
  `2-Keto-D-gluconic acid hemicalcium salt hydrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Hydroxypyridine.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml data/ingredients/mapped/2-Nitrophenol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed for the parent ChEBI CURIE.
- Whole-corpus checks run earlier in this review pass passed, including SSSOM
  invariants for the close parent plus exact CAS row; only the shared evidence
  validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:closeMatch` parent row to `CHEBI:27469` plus the exact
  `cas:1040352-40-6` registry row, but the parent row also exports
  `2-Keto-D-gluconic acid hemicalcium salt monohydrate` as `other_label`.

## Evidence

- ChEBI confirms the parent boundary: `CHEBI:27469` is the anhydrous acid, not a
  calcium salt hydrate.
- PubChem confirms that CAS `1040352-40-6` is water-containing and supports
  enriching the record with exact formula `C12H20CaO15`, SMILES, InChI, and CID
  `17749212`.
- Major: the exact monohydrate string is attached to the generic hydrate SSSOM
  row even though this corpus has a separate
  `2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml` record.
- Major: the `CARBON_SOURCE` and `ENERGY_SOURCE` roles are supported only by
  provisional computational evidence, not by inspected formulation-specific
  evidence for this exact hydrate.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, the exact CAS row, the monohydrate label leak, and stale pre-#342
  hydrate review rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- The record currently has only `cas_rn` under `chemical_properties`; exact
  PubChem structure fields are available for the active CAS.
- Empty component slots are acceptable for this modeled single hydrate.

## Recommended Edits

1. In
   `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml`,
   backfill formula `C12H20CaO15`, exact SMILES/InChI, and PubChem CID
   `17749212` for CAS `1040352-40-6`.
2. Remove `2-Keto-D-gluconic acid hemicalcium salt monohydrate` from exact label
   surfaces for the generic hydrate record.
3. Remove or directly substantiate the provisional `CARBON_SOURCE` and
   `ENERGY_SOURCE` roles.
4. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
5. Re-run strict/LinkML validation, `scripts/validate_sssom_invariants.py`, and
   docs/export checks after the chemistry, synonym, and role cleanup.
