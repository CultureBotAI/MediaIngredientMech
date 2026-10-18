# `data/ingredients/mapped/Amylose_From_Potato.yaml`

## Verdict

Needs curation. The CAS-to-`CHEBI:28102` lookup, amylose chemistry, exact ChEBI
synonym, row-review disposition, SSSOM row, and aggregate copy are internally
consistent, but the potato-qualified record still reuses the broader amylose
identifier as an exact identity and carries a provisional `CARBON_SOURCE` role
inferred only from ChEBI ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Amylose_From_Potato.yaml`.
- Identifier and grounding: `identifier: CHEBI:28102` with
  `ontology_mapping.ontology_id: CHEBI:28102`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:28102` to `amylose`
  with formula `(C6H10O5)n.H2O`, CAS `9005-82-7`, the stored SMILES and InChI,
  and InChIKey `WQZGKKKJIJFFOK-DVKNGEFBSA-N`.
- The preferred term is source-qualified as potato amylose; the ChEBI term and
  the current CAS xref identify unqualified amylose.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amylopectin_From_Maize.yaml data/ingredients/mapped/Amylose_From_Potato.yaml data/ingredients/mapped/Anabasine_Hydrochloride.yaml data/ingredients/mapped/Anaerobic_water.yaml data/ingredients/mapped/Andirobin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amylose_From_Potato.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28057 CHEBI:28102`:
  returned canonical `amylose` and the stored exact structural synonym for
  `CHEBI:28102`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28057 CHEBI:28102`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:28102`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_synonym_enrich_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` mark the historical
  Amylose-from-potato synonym-enrichment proposal as already represented.
- `mappings/ingredient_mappings.sssom.tsv` row 419 maps
  `MIM:Amylose_From_Potato` directly to `CHEBI:28102` with `skos:exactMatch`,
  CAS `9005-82-7`, the exact structural synonym, and a `SYNONYM_ENRICH`
  trailer.
- The source-qualified label has the same shape as
  `Amylopectin_From_Maize.yaml`, but it has not been regraded to
  `NARROW_MATCH` or minted to a local identifier.
- The only role is a `CARBON_SOURCE` computational prediction inferred from
  carbohydrate ancestry; no medium or source claim demonstrates that amylose
  from potato was curated as a carbon source.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech memberships, SSSOM and row-review TSVs, and batch
  review reports found the active YAML, aggregate copy, exact SSSOM row,
  row-review rows, and no `culturemech_recipe_membership.tsv` rows for
  `CHEBI:28102`.

## Completeness

- CAS, formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The over-broad primary identifier/exact SSSOM identity and unsupported
  carbon-source role remain active gaps.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including both gaps.

## Recommended Edits

- Regrade `data/ingredients/mapped/Amylose_From_Potato.yaml` as narrower than
  `CHEBI:28102` and mint a local primary identifier, following the #322 pattern
  already used by `data/ingredients/mapped/Amylopectin_From_Maize.yaml`.
- Replace the provisional `CARBON_SOURCE` assignment with source-backed
  evidence, or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amylose_From_Potato.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
