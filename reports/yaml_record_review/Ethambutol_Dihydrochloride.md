# `data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml`

## Verdict

Pass. The supplied dihydrochloride salt maps to the form-specific ChEBI salt
term, PubChem confirms the same CAS-derived salt structure, and the final SSSOM
row does not collapse the salt to parent ethambutol.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:4878` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ethambutol dihydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `1070-11-7` resolved to CID 14051 with formula
  `C10H26Cl2N2O2` and the same two-HCl InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Etabetacin.yaml data/ingredients/mapped/Etamycin.yaml data/ingredients/mapped/Ethambutol.yaml data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml data/ingredients/mapped/Ethanol.yaml --out /tmp/mim_eta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI salt identifier, CAS RN, dot-separated formula, InChI, SMILES, and
  exact synonym as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethambutol_Dihydrochloride` to `CHEBI:4878` with `skos:exactMatch`;
  `N,N'-bis[(2S)-1-hydroxybutan-2-yl]ethane-1,2-diaminium dichloride` and
  `CAS:1070-11-7` are safe `other` tokens for the same salt identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Ethambutol_Dihydrochloride`, `CHEBI:4878`, and `1070-11-7` found the
  active YAML, aggregate copy, final SSSOM row, OAK/OLS row-review provenance,
  and expected generated indexes; it did not expose a contradictory active
  mapping.

## Completeness

- The exact salt identity, CAS RN, structure fields, exact synonym, and final
  SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
