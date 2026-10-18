# `data/ingredients/mapped/L-serine.yaml`

## Verdict

Pass. The CultureMech exact CHEBI:17115 identity, CAS RN, PubChem structure,
nitrogen-source role, occurrence count, reviewed synonyms, and final SSSOM row
are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-serine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17115` with
  `ontology_mapping.ontology_id: CHEBI:17115`, label `L-serine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:17115`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-45-1`, molecular formula `C3H7NO3`, InChI,
  and SMILES.
- Role facets: `nutritional_roles.NITROGEN_SOURCE` with
  `DATABASE_ENTRY` evidence from the imported CultureMech role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17115` as active `L-serine` and lists CAS
  `56-45-1`.
- PubChem resolves CAS RN `56-45-1` to CID `5951` with formula `C3H7NO3` and
  the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` is backed by `DATABASE_ENTRY` evidence
  whose curator note preserves the original CultureMech role text, `Nitrogen
  Source`, matching the facet.
- The exact OLS search for final synonym `beta-Hydroxyalanine` returns
  CHEBI:17115, and the remaining exported kg-microbe synonyms are
  stereospecific L-serine names.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17115`; its
  `other` field contains reviewed exact synonyms plus `CAS:56-45-1`.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and component references from multicomponent
  amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count, role
  facet, synonyms, aggregate copy, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
