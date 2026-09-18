# `data/ingredients/mapped/Escin.yaml`

## Verdict

Pass. The CAS-to-ChEBI lookup is preserved as a CAS lookup grade, `Escin` is an
accepted synonym of active ChEBI `Aescin`, and the final SSSOM row publishes
only the matching CAS token in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Escin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2500` with matching
  `ontology_mapping.ontology_id`, canonical label `Aescin`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:2500` to active `Aescin`.
- Live OLS for `CHEBI:2500` carries related synonyms `Aescin` and `Escin`,
  CAS xref `6805-41-0`, generalized formula `C55H86O24`, and the same InChI
  and SMILES now recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Erythrose.yaml data/ingredients/mapped/Escin.yaml data/ingredients/mapped/Esculin_Ferric_Citrate.yaml data/ingredients/mapped/Esculin_Monohydrate.yaml data/ingredients/mapped/Estragole.yaml --out /tmp/mim_esc_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Escin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, CAS lookup grade, and
  regrade history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Escin` to
  `CHEBI:2500` with `skos:exactMatch`; this is the record's own-identifier row,
  so Rule D allows the exact predicate while `mapping_quality` preserves
  `CAS_RN_LOOKUP` provenance.
- The row's only `other` token is `CAS:6805-41-0`, which is the active ChEBI
  xref for the same term.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Escin`, `CHEBI:2500`,
  `Aescin`, and `6805-41-0` found the active YAML, aggregate copy, final SSSOM
  row, OAK/OLS row-review provenance, and expected generated indexes; it did
  not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure, and final SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
