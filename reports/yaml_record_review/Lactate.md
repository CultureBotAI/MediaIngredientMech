# `data/ingredients/mapped/Lactate.yaml`

## Verdict

Needs curation. The exact generic CHEBI:24996 lactate identity, CAS RN,
PubChem structure, occurrence count, and final exact row pass, but final SSSOM
publishes process-qualified and L-specific labels as synonyms for the generic
lactate parent, and both nutritional roles are still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactate.yaml`.
- Identifier and grounding: `identifier: CHEBI:24996` with
  `ontology_mapping.ontology_id: CHEBI:24996`, label `lactate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `113-21-3`, molecular formula `C3H5O3`, InChI,
  and SMILES for the lactate anion.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacidipine` through `Lacto-N-fucopentaose_I`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacidipine.yaml data/ingredients/mapped/Lactate.yaml data/ingredients/mapped/Lactitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:24996` as active `lactate` and lists same-parent
  synonyms such as `2-hydroxypropanoate`, `2-hydroxypropionate`,
  `MeCH(OH)CO2 anion`, `b-lactate`, and `beta-lactate`.
- PubChem resolves CAS RN `113-21-3` to a lactate CID with an equivalent
  anion formula and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:24996`.
- Major: final SSSOM `other` exports `produces: DL-lactate`, which is a
  process-qualified trait fragment rather than a synonym for lactate.
- Major: final SSSOM `other` also exports L-specific labels
  `(+)-lactate`, `(2S)-2-hydroxypropanoate`, `(S)-lactate`, `L(+)-lactate`,
  `L-(+)-lactate`, and `L-lactate` on the stereochemically unspecified
  `CHEBI:24996` lactate parent. Those tokens erase the boundary between
  generic lactate and the existing L-lactate-specific records.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from name-list and canonical-substrate
  heuristics and explicitly say review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row plus adjacent MIM subjects including `Glucose_Lactate`,
  `Sodium_D-Lactate`, `Sodium_Lactate`, and `Na-l-lactate`; the specific
  sodium salt records confirm that salt and stereochemical aliases need to stay
  off this generic parent row.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, occurrence count,
  aggregate copy, and final SSSOM row are present.
- The published `other` field and provisional nutritional-role facets need
  curation before this record can be treated as fully reviewed.

## Recommended Edits

- Major: remove `produces: DL-lactate` from active exact synonyms in
  `data/ingredients/mapped/Lactate.yaml` or retag it as provenance-only so it no
  longer reaches final SSSOM.
- Major: remove the L-specific synonyms from the generic `CHEBI:24996` record
  or move any true L-lactate labels to the exact L-lactate record that owns that
  stereochemistry.
- Major: either replace `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` with inspected source evidence for exact
  generic lactate use, or remove the provisional roles.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, term, product, component, and SSSOM validation.
