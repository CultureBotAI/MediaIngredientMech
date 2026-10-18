# `data/ingredients/mapped/Distilled_Water.yaml`

## Verdict

Pass with minor issues. The current record intentionally broadens the distilled
water surface to `CHEBI:15377` water, the rejected tap, demineralized, sterile,
and seawater-like labels stay out of the final SSSOM, and the published
synonyms are all usable water aliases. The remaining issue is weak
auto-proposed PubMed evidence on an already exact ubiquitous water identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Distilled_Water.yaml`.
- Identifier and grounding: `identifier: CHEBI:15377` with
  `ontology_mapping.ontology_id: CHEBI:15377`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 365/365 source occurrences.
- Local OAK resolves `CHEBI:15377` to active `water`, formula `H2O`, the
  expected InChI and SMILES, CAS xref `7732-18-5`, exact synonyms such as
  `[OH2]`, `dihydrogen oxide`, and `oxidane`, and related multilingual water
  synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:132764 CHEBI:34683 CHEBI:15377 CHEBI:42160 CHEBI:37070`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:15377`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `7732-18-5` to CID 962 with formula `H2O` and the same
  InChIKey as the record.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:15377`, `7732-18-5`, and the `Distiled water` typo found the active
  distilled-water record, expected component usages, and one unmapped
  provenance-only `Water_Distilled_Or_Tapwater` discussion.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Distilled_Water` to `CHEBI:15377` with `skos:exactMatch`, canonical
  object label `water`, CHEBI object source, curated water synonyms including
  the retained distilled-water medium aliases, and `CAS:7732-18-5`.
- The raw role and properties import strings and the tap, demineralized,
  double-distilled, bound, sterile, and charcoal-filtered seawater rejected
  labels are filtered out of final SSSOM publication.
- Minor: one `ontology_mapping.evidence` object is an auto-proposed PubMed
  snippet that mentions distilled water but does not independently ground the
  already exact water identity.

## Completeness

- CAS RN, formula, InChI, SMILES, exact water synonymy, broader raw water
  aliases, CultureMech liquid/solid-medium aliases, and occurrence provenance
  are populated.
- `H2O` and `dH2O` are intentionally retained as water aliases for this
  broadened identity.
- Supplied forms, mixture components, nutritional roles, physicochemical roles,
  biological roles, and environmental contexts are correctly empty.

## Recommended Edits

- Minor: remove the auto-proposed PubMed evidence from
  `data/ingredients/mapped/Distilled_Water.yaml`, or replace it with an explicit
  source note explaining why the distilled-water source surface is intentionally
  represented by broad `CHEBI:15377`; then synchronize
  `data/curated/mapped_ingredients.yaml`.
