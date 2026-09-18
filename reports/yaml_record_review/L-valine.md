# `data/ingredients/mapped/L-valine.yaml`

## Verdict

Needs curation. The exact CHEBI:16414 identity, CAS RN, PubChem structure,
occurrence count, and most final synonyms pass, but the amino-acid-source role
is provisional and the final SSSOM exports bare `Valine`, which also resolves
to the generic valine class.

## Identity

- Reviewed record: `data/ingredients/mapped/L-valine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16414` with
  `ontology_mapping.ontology_id: CHEBI:16414`, label `L-valine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16414`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `72-18-4`, molecular formula `C5H11NO2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `L-valine` through `L_-tartaric_Acid`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-valine.yaml data/ingredients/mapped/LL-37.yaml data/ingredients/mapped/L_-tartaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records. Engine A term validation was
  skipped for the CAS-primary soybean phosphatidylinositol record and the
  local `kgmicrobe.ingredient` registry record.

## Evidence

- EBI OLS4 resolves `CHEBI:16414` as active `L-valine` and lists CAS
  `72-18-4`.
- PubChem resolves CAS RN `72-18-4` to CID `6287` with formula `C5H11NO2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16414`; its
  `other` field contains L-valine synonyms, bare `Valine`, and `CAS:72-18-4`.
- Major: exact OLS search for `Valine` returns generic CHEBI:27266 before
  L-specific CHEBI:16414. Exporting the bare token from this L-specific record
  crosses the generic/L boundary in the final SSSOM row.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact L-valine was supplied as an amino acid
  source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, D-valine sibling, and component references from
  multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  aggregate copy, and most final synonyms are present and consistent.
- The provisional role and generic `Valine` synonym need curation before the
  record can be treated as complete.

## Recommended Edits

- Major: remove `Valine` from the `EXACT` synonym list on
  `data/ingredients/mapped/L-valine.yaml`.
- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` with inspected
  source evidence for exact L-valine use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
