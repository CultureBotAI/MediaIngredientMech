# `data/ingredients/mapped/Alphaalpha-Trehalose.yaml`

## Verdict

Needs curation. The exact `CHEBI:16551` alpha,alpha-trehalose grounding and
restored CultureMech residual evidence pass, but this newer residual record has
not been through the ingredient-type and ChEBI chemistry backfills, and its
single CultureMech occurrence is still absent from the refreshed
recipe-membership table.

## Identity

- Reviewed record: `data/ingredients/mapped/Alphaalpha-Trehalose.yaml`.
- Identifier and grounding: `identifier: CHEBI:16551` with
  `ontology_mapping.ontology_id: CHEBI:16551`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16551` to
  `alpha,alpha-trehalose` with formula `C12H22O11`, CAS `99-20-7`, SMILES
  `OC[C@H]1O[C@H](O[C@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O)[C@H](O)[C@@H](O)[C@@H]1O`,
  and InChIKey `HDTRYLNUVZCQOY-LIZSDCNHSA-N`.
- ChEBI lists `alpha,alpha-Trehalose` as a related synonym of
  `alpha,alpha-trehalose`, matching the restored residual grounding.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml data/ingredients/mapped/Alpha-toxicarol_Dl.yaml data/ingredients/mapped/Alphaalpha-Trehalose.yaml data/ingredients/mapped/Althiomycin.yaml data/ingredients/mapped/Aluminium_Sulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alphaalpha-Trehalose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned canonical `alpha,alpha-trehalose` plus
  `alpha,alpha-Trehalose`, `alpha-D-Trehalose`, `Trehalose`, and other ChEBI
  aliases for `CHEBI:16551`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:16551`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with the same 104 non-blocking
  plausibility warnings seen at corpus scope.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_residual_groundings.tsv` records one residual
  `alpha,alpha-Trehalose` mention across one recipe and grounds it to
  `CHEBI:16551`.
- `mappings/ingredient_mappings.sssom.tsv` row 383 maps
  `MIM:Alphaalpha-Trehalose` to `CHEBI:16551` with `skos:exactMatch`, the
  CultureMech residual occurrence source, and the `#541` evidence-restoration
  curator tag.
- A hidden/ignored-inclusive search over
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:16551` row, so
  the stored `1/1` counters are not represented in that refreshed membership
  table.
- The ChEBI page and local ChEBI metadata can supply formula, SMILES, InChI,
  InChIKey, CAS, and mass values, but `chemical_properties` is still missing
  from the active YAML.
- The active YAML also lacks `ingredient_type`, so it missed the
  `classify_ingredient_type` pass that older CHEBI primaries received.

## Completeness

- Mapping evidence, occurrence statistics, and append-only creation/restoration
  history are populated.
- Formula, SMILES, InChI, CAS, molecular weight, and `ingredient_type` are
  missing despite the exact ChEBI identity.
- No synonym, role, component, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the missing chemistry and type fields.

## Recommended Edits

- Backfill `chemical_properties` in
  `data/ingredients/mapped/Alphaalpha-Trehalose.yaml` from `CHEBI:16551`.
- Add `ingredient_type: SINGLE_INGREDIENT` and an audit event reflecting the
  classification.
- Refresh CultureMech membership so the one residual alpha,alpha-trehalose
  recipe is represented in `mappings/culturemech_recipe_membership.tsv`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alphaalpha-Trehalose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
