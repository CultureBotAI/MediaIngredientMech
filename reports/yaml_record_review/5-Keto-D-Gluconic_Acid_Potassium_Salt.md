# `data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml`

## Verdict

Needs curation, major. The CAS primary identity, potassium-salt chemistry,
`CHEBI:17426` parent, SSSOM registry rows, and aggregate copy are internally
consistent, but the record exports a non-exact parenthetical surface as a
synonym and carries two provisional nutritional roles with only computational
name-pattern evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:91446-96-7` with
  `ontology_mapping.ontology_id: CHEBI:17426`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- PubChem CID `23702137` reports `C6H9KO7`, the stored InChI, and a potassium
  salt with `[K+]`, agreeing with the record's CAS primary identity.
- The official ChEBI page resolves `CHEBI:17426` to the free acid
  `5-dehydro-D-gluconic acid`, formula `C6H10O7`, so the ontology row is
  correctly only a parent for the potassium salt.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Hydroxyoctanoate.yaml data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml data/ingredients/mapped/5-aminovaleric_Acid.yaml data/ingredients/mapped/5-dehydro-D-gluconate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned `CHEBI:17426` as `5-dehydro-D-gluconic acid`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned `CHEBI:17426` as the neutral acid, not the potassium salt.

## Evidence

- PubChem CID `23702137` lists `91446-96-7` and potassium-salt synonyms,
  including `5-Keto-D-gluconic acid potassium salt`, which supports the local
  CAS identity and populated formula, SMILES, InChI, and CID.
- The SSSOM rows correctly preserve three surfaces for the narrow match: a
  `skos:narrowMatch` row to `CHEBI:17426`, a `skos:exactMatch` registry row to
  `cas:91446-96-7`, and a `skos:exactMatch` companion row to
  `kgmicrobe.compound:5-keto-d-gluconic_acid_potassium_salt`.
- The `RAW_TEXT` synonym `5-Ketogluconate (5-dehydro-D-gluconate)` omits the
  potassium counterion, names the dehydro-D-gluconate parent in its
  parenthetical, is absent from PubChem's potassium-salt synonyms, and is
  exported in SSSOM `other`. That row should not be an exact surface of
  `cas:91446-96-7`.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` roles are asserted only from
  `COMPUTATIONAL_PREDICTION` entries that both say review is recommended. No
  inspected occurrence or source entry in the record supports either role for
  potassium 5-keto-D-gluconate.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  rows, stale advisory rows about the old `CHEBI:26218` parent, registry-triage
  rows, source review rows, and ignored aggregate backups. The stale `CHEBI:26218`
  rows are superseded by the current `CHEBI:17426` parent.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, the parent ChEBI mapping, and the
  registry SSSOM rows are populated.
- The record lacks exact synonyms that PubChem shows for the potassium form,
  such as `Potassium 5-ketogluconate`, and instead carries one parenthetical
  source label that is too broad for the salt.

## Recommended Edits

- In `data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml`,
  remove `5-Ketogluconate (5-dehydro-D-gluconate)` from `synonyms`, or move it
  to a non-exact source-occurrence surface that the SSSOM exporter will not emit
  as an exact `other` value for `cas:91446-96-7`; rebuild
  `mappings/ingredient_mappings.sssom.tsv` and the aggregate
  `data/curated/mapped_ingredients.yaml`.
- In the same maintained YAML, either remove the provisional `CARBON_SOURCE`
  and `ENERGY_SOURCE` roles or replace the computational placeholders with
  source-backed evidence scoped to this salt; rerun
  `uv run --frozen python scripts/validate_strict.py` and
  `uv run --frozen python scripts/validate_sssom_invariants.py` after the edit.
