# `data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`

## Verdict

Needs curation, major. The exact CAS salt structure and narrow parent grounding
to `CHEBI:1148` are synchronized, but the record still exports a neutral-parent
acid synonym as exact for the sodium salt and asserts `CARBON_SOURCE` from only
a provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:5094-24-6` with
  `ontology_mapping.ontology_id: CHEBI:1148`,
  `ontology_mapping.ontology_label: 2-hydroxybutyric acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official parent ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:1148`
  resolves to neutral `2-hydroxybutyric acid`, formula `C4H8O3`, and lists
  `2-hydroxybutanoic acid` as a synonym of the neutral acid.
- Exact PubChem check: CAS `5094-24-6` resolves to CID `23663641`, sodium
  DL-2-hydroxybutyrate, formula `C4H7NaO3`, SMILES
  `CCC(C(=O)[O-])O.[Na+]`, and the same salt InChI as the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml data/ingredients/mapped/2-Ethylhexanol.yaml data/ingredients/mapped/2-Furfuraldehyde.yaml data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed for the parent ChEBI CURIE.
- Whole-corpus checks run earlier in this review pass passed, including SSSOM
  invariants for narrow parent plus exact registry rows; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `skos:narrowMatch` row to `CHEBI:1148` plus exact registry rows for
  `cas:5094-24-6` and the local kg-microbe compound.

## Evidence

- The exact PubChem record confirms the sodium-salt formula, SMILES, InChI, and
  PubChem CID now in the YAML.
- The parent ChEBI page confirms that `CHEBI:1148` is the neutral acid, so a
  non-exact `skos:narrowMatch` is the right relationship for the sodium salt.
- Major: `2-hydroxybutanoic acid` is a ChEBI synonym of the neutral parent, not
  an exact synonym of the sodium salt, yet it is exported in docs/label-index
  output for the active salt.
- Major: the `CARBON_SOURCE` nutritional role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence inferred from a name-pattern rule, not by
  inspected evidence that the exact sodium salt is used as a medium carbon
  source.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, exact CAS and local registry rows, and the live parent-synonym leak.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, PubChem CID, formula, SMILES, and InChI are populated for the exact
  sodium salt.
- Empty component slots are acceptable for this modeled single salt.

## Recommended Edits

1. In `data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`, remove
   `2-hydroxybutanoic acid` from the active sodium salt's exact synonyms.
2. Remove the provisional `CARBON_SOURCE` role or replace it with inspected
   formulation-specific evidence for this exact salt.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
4. Re-run strict/LinkML validation, `scripts/validate_sssom_invariants.py`, and
   docs/export checks after the synonym and role cleanup.
