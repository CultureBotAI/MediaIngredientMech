# `data/ingredients/mapped/Lacto-N-neotetraose.yaml`

## Verdict

Needs curation. The CHEBI:60239 label, structure, reviewed synonym, and final
SSSOM row agree with each other, but the CAS-RN lookup needs curator review
because PubChem now resolves the record's CAS/name surface to a different
InChIKey, and the carbon-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacto-N-neotetraose.yaml`.
- Identifier and grounding: `identifier: CHEBI:60239` with
  `ontology_mapping.ontology_id: CHEBI:60239`, label
  `beta-D-Gal-(1->4)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `13007-32-4`, molecular formula `C26H45NO21`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacto-N-fucopentaose_II` through `Lactone`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml data/ingredients/mapped/Lacto-N-neotetraose.yaml data/ingredients/mapped/Lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:60239` as active, lists
  `Lacto-N-neotetraose` as a related synonym, lists CAS `13007-32-4`, and lists
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:60239`; its
  `other` field contains the reviewed IUPAC synonym plus `CAS:13007-32-4`.
- Major: the record was created from a CAS-RN lookup, but PubChem now resolves
  both `13007-32-4` and `Lacto-N-neotetraose` to CID `121853` with InChIKey
  `RBMYDHMFFAVMMM-PLQWBNBWSA-N`, while the YAML/ChEBI structure has InChIKey
  `IEQCXFNWPAHHQR-YKLSGRGUSA-N` and resolves separately in PubChem to CID
  `9831622`. The ChEBI mapping may still be correct for the preferred term, but
  the CAS-derived evidence and final `CAS:13007-32-4` payload need an explicit
  source-of-truth decision.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and
  explicitly says review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same Lacto-N-neotetraose
  label.

## Completeness

- The active CHEBI identity, CHEBI formula, CHEBI structure, aggregate copy, and
  final SSSOM row are present.
- The CAS RN should not be treated as reviewed until the PubChem/ChEBI
  structural conflict is resolved.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: resolve CAS RN `13007-32-4` against `CHEBI:60239` and PubChem CIDs
  `121853` and `9831622`; then either keep the current ChEBI grounding with
  reviewed CAS provenance, move the CAS value off this record, or remap if the
  CultureBotHT row denoted the PubChem CID instead.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected source
  evidence for exact Lacto-N-neotetraose use, or remove the provisional role.
- Sync the aggregate copy and regenerate final SSSOM after any YAML changes;
  rerun strict, term, product, component, and SSSOM validation.
