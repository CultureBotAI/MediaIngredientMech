# `data/ingredients/mapped/L-tryptophan.yaml`

## Verdict

Needs curation. The exact CHEBI:16828 identity, CAS RN, PubChem structure,
CultureMech nitrogen-source role, occurrence count, and most final synonyms
pass, but final SSSOM also exports bare `Tryptophan`, which is owned locally by
the generic tryptophan record.

## Identity

- Reviewed record: `data/ingredients/mapped/L-tryptophan.yaml`.
- Identifier and grounding: `identifier: CHEBI:16828` with
  `ontology_mapping.ontology_id: CHEBI:16828`, label `L-tryptophan`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16828`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `73-22-3`, molecular formula `C11H12N2O2`,
  InChI, and SMILES.
- Role facets: `nutritional_roles.NITROGEN_SOURCE` with
  `DATABASE_ENTRY` evidence from the imported CultureMech role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:16828` as active `L-tryptophan` and lists CAS
  `73-22-3`.
- PubChem resolves CAS RN `73-22-3` to CID `6305` with formula `C11H12N2O2`
  and the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` is backed by `DATABASE_ENTRY` evidence
  whose curator note preserves the original CultureMech role text, `Nitrogen
  Source`, matching the facet.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16828`; its
  `other` field contains L-tryptophan synonyms, bare `Tryptophan`, and
  `CAS:73-22-3`.
- Major: an exact OLS search for `Tryptophan` returns generic CHEBI:27897
  before L-specific CHEBI:16828, and `data/ingredients/mapped/Tryptophan.yaml`
  owns CHEBI:27897 locally. Exporting `Tryptophan` as an exact synonym for
  this L-specific record crosses that generic/L boundary in the final SSSOM
  row.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the generic and DL tryptophan siblings, and
  component references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, aggregate copy, and most exported synonyms are present
  and consistent.
- The bare generic synonym must be removed or demoted before the final SSSOM
  `other` field can be treated as exact for CHEBI:16828.

## Recommended Edits

- Major: remove `Tryptophan` from the `EXACT_SYNONYM` list on
  `data/ingredients/mapped/L-tryptophan.yaml`, or rehome it to the generic
  tryptophan record if a non-preferred synonym is still needed there.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
