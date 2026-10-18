# `data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml`

## Verdict

Needs curation, major. The re-grounded exact `CHEBI:18281`
2,5-didehydro-D-gluconic-acid identity and chemistry pass, but the raw
comma-truncated source label is still exported as an exact SSSOM `other`
surface.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18281` with
  `ontology_mapping.ontology_id: CHEBI:18281`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:18281` to
  `2,5-didehydro-D-gluconic acid` with formula `C6H8O7`, CAS `2595-33-7`,
  the stored SMILES, and the stored InChI.
- Local OAK metadata carries the same formula, structure strings, CAS xref,
  and exact synonym `D-threo-hexo-2,5-diulosonic acid`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml data/ingredients/mapped/5-fluorouracil.yaml data/ingredients/mapped/5-methyluridine.yaml data/ingredients/mapped/5-oxoproline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the official exact and related synonym set for `CHEBI:18281`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:18281`.

## Evidence

- The current `CHEBI:18281` grounding matches the active ChEBI neutral acid
  and the stored formula, SMILES, InChI, and molecular weight.
- The history and mapping evidence correctly preserve the `CHEBI:17426` false
  start as superseded and state that 5-dehydro-D-gluconic acid and
  2,5-didehydro-D-gluconic acid are distinct compounds.
- The source label `5-didehydro-D-gluconic Acid` is still present as a
  `RAW_TEXT` synonym and is exported in SSSOM `other`. That string is a
  comma-truncated artifact missing the leading `2,`; it is not an exact synonym
  of `CHEBI:18281`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, `truncated_locants.tsv` evidence for the lost locant, the
  `apply_locant_corrections.py` repair entry, stale advisory rows in
  `record_research_validation.tsv`, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence count, corrected
  ChEBI grounding, and `ingredient_type` are populated.
- The record is otherwise empty in the optional roles, components,
  environmental context, and discussion sections.

## Recommended Edits

- In `data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml`, remove
  `5-didehydro-D-gluconic Acid` from `synonyms` or move it to a source
  occurrence field that the SSSOM exporter will not emit as an exact `other`
  label; rebuild `mappings/ingredient_mappings.sssom.tsv` and
  `data/curated/mapped_ingredients.yaml`.
- After the edit, rerun `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_sssom_invariants.py`, and
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  to prove the exact-match `other` value is gone and generated products remain
  consistent.
