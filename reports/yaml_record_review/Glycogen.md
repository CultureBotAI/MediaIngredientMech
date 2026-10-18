# `data/ingredients/mapped/Glycogen.yaml`

## Verdict

Needs curation. The exact match to active `CHEBI:28087` glycogen and the
MicrobeDecoder source occurrence pass, but `CARBON_SOURCE` is unsupported
computational curation and final SSSOM still publishes the process-qualified
raw label `autoclaved, Glycogen` in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycogen.yaml`.
- Identifier and grounding: `identifier: CHEBI:28087` with matching
  `ontology_mapping.ontology_id`, canonical label `glycogen`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Source occurrence: the record has zero CultureMech recipe occurrences and a
  separate MicrobeDecoder `BacDive_Metabolite_utilization` source occurrence
  count of 662.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml data/ingredients/mapped/Glycocyamine.yaml data/ingredients/mapped/Glycogen.yaml data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml data/ingredients/mapped/Glycolaldehyde.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycogen.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, raw CultureBotHT and MicrobeDecoder labels,
  MicrobeDecoder source occurrence, singleton type, and provisional
  carbon-source role as the per-record YAML.
- OLS4 resolves `CHEBI:28087` as `glycogen`, lists CAS `9005-79-2` as a
  database cross-reference, and defines the term as a polydisperse branched
  glucan, matching the generic glycogen identity.
- The `(+)-D-glycogen` duplicate was explicitly absorbed by #213 as an
  optical-rotation-prefixed duplicate of glycogen, not as a distinct blend.
- Major: `nutritional_roles.CARBON_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and a provisional curator
  note. No inspected CultureMech, database, or literature evidence supports
  that role for this record.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycogen` to `CHEBI:28087` by `skos:exactMatch`, but it exports
  `autoclaved, Glycogen` in `other`. That token is process-qualified raw text,
  not a true synonym for glycogen.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, final SSSOM rows for plain and
  bovine-liver glycogen, MicrobeDecoder residual inputs under ignored
  `data/custom`, row-review TSVs, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, MicrobeDecoder source occurrence, ingredient type,
  absorbed duplicate label, and final SSSOM row are populated.
- The carbon-source role needs claim-level support or removal.
- The process-qualified raw label needs to be removed from resolving synonym
  surfaces before final SSSOM is rebuilt.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` from
  `data/ingredients/mapped/Glycogen.yaml`, or replace the provisional CHEBI
  ancestry evidence with inspected source evidence that specifically supports
  glycogen as a carbon source.
- Major: retype `autoclaved, Glycogen` as a non-resolving rejected label, or
  teach `src/mediaingredientmech/synonym_policy.py` to filter process-qualified
  raw labels, then rebuild the final SSSOM so `MIM:Glycogen` no longer exports
  `autoclaved, Glycogen` in `other`.
