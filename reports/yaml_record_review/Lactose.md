# `data/ingredients/mapped/Lactose.yaml`

## Verdict

Needs curation. The generic CHEBI:17716 lactose identity, CAS RN, PubChem
structure, CultureMech carbon-source role, and occurrence count pass, but final
SSSOM exports beta-lactose-specific and parse-artifact tokens, the energy-source
role is provisional, and one auto-proposed literature item is misplaced under
ontology-mapping evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17716` with
  `ontology_mapping.ontology_id: CHEBI:17716`, label `lactose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `63-42-3`, molecular formula `C12H22O11`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lactose` through `Lanthanum_Iii_Chloride`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lactose.yaml data/ingredients/mapped/Lactulose.yaml data/ingredients/mapped/Laminaribiose.yaml data/ingredients/mapped/Laminarin_From_Laminaria_Digitata.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:17716` as active `lactose`, lists CAS `63-42-3`, and
  lists the same InChI as the YAML record.
- PubChem resolves CAS RN `63-42-3` to CID `440995` with formula `C12H22O11`
  and the same InChI as the YAML record.
- The `nutritional_roles.CARBON_SOURCE` facet is backed by the original
  CultureMech role text `Carbon Source`, which supports the enum exactly.
- Major: final SSSOM `other` exports beta-lactose-specific labels
  `beta-D-Lactose`, `beta-D-galactopyranosyl-(1->4)-beta-D-glucose`, and
  `beta-D-glucopyranose, 4-O-beta-D-galactopyranosyl-` on generic lactose.
  Local `Beta-lactose.yaml` owns beta-specific lactose, so those labels erase a
  curated anomer boundary.
- Major: final SSSOM `other` exports `(2)-D-lactose`, even though the curation
  history documents its leading `(2)` as stray parse noise. A parse artifact is
  not a real synonym surface for lactose.
- Major: `nutritional_roles.ENERGY_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a canonical-substrate heuristic and
  explicitly says review is recommended.
- Minor: PMID `15915565` is stored as ontology-mapping evidence and says its
  auto-proposed explanation should be rephrased or removed. The snippet may
  support lactose being present in a growth medium, but it is not evidence for
  the exact CHEBI identity.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row plus `Alpha-Lactose` and `Beta-lactose` sibling records.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, carbon-source
  role, occurrence count, aggregate copy, and final SSSOM row are present.
- The final `other` field and provisional energy-source facet need curation
  before this record can be treated as fully reviewed.

## Recommended Edits

- Major: remove beta-lactose-specific labels from active synonyms in
  `data/ingredients/mapped/Lactose.yaml` or move any true beta-lactose aliases
  to `data/ingredients/mapped/Beta-lactose.yaml`.
- Major: retag `(2)-D-lactose` as provenance-only parse noise so it no longer
  reaches final SSSOM.
- Major: either replace `nutritional_roles.ENERGY_SOURCE` with inspected source
  evidence for exact generic lactose use, or remove the provisional role.
- Minor: move or remove the auto-proposed PMID `15915565` entry from
  `ontology_mapping.evidence`.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, term, product, component, and SSSOM validation.
