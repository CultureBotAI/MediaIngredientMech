# `data/ingredients/mapped/L_-tartaric_Acid.yaml`

## Verdict

Needs curation. The exact CHEBI:15671 identity, CAS RN, PubChem structure,
occurrence count, reviewed synonyms, and final SSSOM row pass, but the
carbon-source role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L_-tartaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15671` with
  `ontology_mapping.ontology_id: CHEBI:15671`, label `L-tartaric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `87-69-4`, molecular formula `C4H6O6`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `L-valine` through `L_-tartaric_Acid`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-valine.yaml data/ingredients/mapped/LL-37.yaml data/ingredients/mapped/L_-tartaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:15671` as active `L-tartaric acid` and lists CAS
  `87-69-4`.
- PubChem resolves CAS RN `87-69-4` to CID `444305` with formula `C4H6O6` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:15671`; its
  `other` field contains reviewed L-tartaric acid synonyms plus `CAS:87-69-4`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact L-tartaric acid was supplied as a carbon
  source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, and docs projections.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/L_-tartaric_Acid.yaml` with inspected source
  evidence for exact L-tartaric acid use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
