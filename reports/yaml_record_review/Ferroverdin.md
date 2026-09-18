# `data/ingredients/mapped/Ferroverdin.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The exact ChEBI
Ferroverdin identity and structure fields pass, but the final SSSOM `other`
column still exports a `produces:` payload as if it were an exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferroverdin.yaml`.
- Identifier and grounding: `identifier: CHEBI:219729` with matching
  `ontology_mapping.ontology_id`, canonical label `Ferroverdin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `chemical_properties` carry the ChEBI-derived formula, InChI, and SMILES for
  ferroverdin.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferrous_Ion.yaml data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml data/ingredients/mapped/Ferroverdin.yaml data/ingredients/mapped/Ferulate.yaml data/ingredients/mapped/Ferulic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferroverdin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, ChEBI structure fields, and synonym payload as the
  per-record YAML.
- The OAK/OLS row-review manifest confirms `MIM:Ferroverdin` to
  `CHEBI:219729` as correct, and the final
  `mappings/ingredient_mappings.sssom.tsv` row maps the subject to that ChEBI
  term with `skos:exactMatch`.
- The final SSSOM `other` token
  `(4-ethenylphenyl) 4-hydroxy-3-nitrosobenzoate;iron(2+)` is a same-substance
  label from ChEBI synonym review.
- Major: the final SSSOM `other` column also exports
  `produces: ferroverdin`, which is a production-role statement rather than an
  exact synonym.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferroverdin` and
  `ferroverdin` found the active YAML, aggregate copy, final SSSOM row,
  OAK/OLS row-review provenance, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, structure fields, ingredient type, and accepted
  exact synonym are populated.
- The final SSSOM synonym payload needs filtering for the `produces:` token.

## Recommended Edits

- Major: remove or retype `produces: ferroverdin` in
  `data/ingredients/mapped/Ferroverdin.yaml` so it no longer exports as an
  exact synonym, sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
