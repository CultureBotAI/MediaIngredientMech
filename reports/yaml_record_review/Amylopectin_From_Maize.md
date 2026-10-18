# `data/ingredients/mapped/Amylopectin_From_Maize.yaml`

## Verdict

Pass. The source-qualified local primary identifier, broader `CHEBI:28057`
amylopectin parent, exact local SSSOM identity rows, CAS, aggregate copy, and
zero CultureMech memberships agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Amylopectin_From_Maize.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:amylopectin_from_maize`
  with `ontology_mapping.ontology_id: CHEBI:28057`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:28057` to
  `amylopectin`; local OAK also records CAS `9037-22-3`.
- The #322 history explains both required pieces of the current shape: the
  maize-qualified label is narrower than ChEBI's unqualified amylopectin class,
  and the record therefore needs its own local primary identifier.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amylopectin_From_Maize.yaml data/ingredients/mapped/Amylose_From_Potato.yaml data/ingredients/mapped/Anabasine_Hydrochloride.yaml data/ingredients/mapped/Anaerobic_water.yaml data/ingredients/mapped/Andirobin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amylopectin_From_Maize.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28057 CHEBI:28102`:
  returned canonical `amylopectin` for `CHEBI:28057`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28057 CHEBI:28102`:
  returned CAS `9037-22-3` for `CHEBI:28057`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` rows 416-418 export the expected
  `skos:narrowMatch` row to `CHEBI:28057`, the exact
  `kgmicrobe.ingredient:amylopectin_from_maize` registry row, and the exact
  `kgmicrobe.compound:amylopectin_from_maize` companion row.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` mark the historical
  amylopectin-from-maize synonym-enrichment proposal as already represented.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech memberships, SSSOM and row-review TSVs, and batch
  review reports found the active YAML, aggregate copy, SSSOM identity rows,
  row-review rows, and no `culturemech_recipe_membership.tsv` rows for this
  local identifier or `CHEBI:28057`.

## Completeness

- CAS, curation history, local identity SSSOM rows, and `ingredient_type` are
  populated.
- Formula, SMILES, and InChI are correctly absent because `CHEBI:28057` itself
  carries no structural definition in ChEBI.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
