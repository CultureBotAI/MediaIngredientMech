# `data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml`

## Verdict

Needs curation, with major identity and final-SSSOM synonym issues. The target
ChEBI term is the generic fatty acid class, while the MIM source label denotes
a recipe-specific fatty acid mixture or stock, and mixture surface forms are
published as exact `other` synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml`.
- Identifier and grounding: `identifier: CHEBI:35366` with matching
  `ontology_mapping.ontology_id`, canonical label `fatty acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record has 4 CultureMech recipe occurrences, refreshed from the #337
  occurrence table.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI-primary subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, generic fatty-acid structure pattern, CultureMech alias
  backfill history, and occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fatty_Acid_Mixture_See_Medium_No_266` to `CHEBI:35366` with
  `skos:exactMatch`.
- Major: the preferred term says this is a fatty acid mixture that references
  Medium No. 266, but the record asserts exact identity to the generic
  `fatty acid` ChEBI class and overwrote an earlier `STOCK_SOLUTION`
  classification with `SINGLE_INGREDIENT`.
- Major: the final SSSOM `other` column exports `Fatty acid mixture` and
  `Fatty acid mixture (see below)`. Those are mixture or recipe-reference
  surfaces, not exact synonyms of CHEBI fatty acid.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fatty_Acid_Mixture_See_Medium_No_266`, `CHEBI:35366`, and the fatty
  acid mixture labels found the active YAML, aggregate copy, final SSSOM row,
  row-review provenance, CultureMech residual alias rows, CultureMech recipe
  memberships, and ignored aggregate backups.

## Completeness

- The CultureMech occurrences are populated.
- The exact identity, type, generic structure fields, and final SSSOM synonyms
  need repair before this row is semantically safe.

## Recommended Edits

- Major: review the four CultureMech occurrences and either mint a local
  fatty-acid-mixture stock identity or link the label to the concrete Medium
  No. 266 mixture it references.
- Major: if `CHEBI:35366` is retained, downgrade it to a broader parent rather
  than an exact identity, remove the mixture labels from exact `other`
  synonym export, choose the correct `ingredient_type`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
