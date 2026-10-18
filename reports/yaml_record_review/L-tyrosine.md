# `data/ingredients/mapped/L-tyrosine.yaml`

## Verdict

Needs curation. The exact CHEBI:17895 identity, CAS RN, PubChem structure,
occurrence count, and most final synonyms pass, but `AMINO_ACID_SOURCE` is
provisional and the final SSSOM exports bare `TYROSINE`, which also resolves to
the generic tyrosine class.

## Identity

- Reviewed record: `data/ingredients/mapped/L-tyrosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17895` with
  `ontology_mapping.ontology_id: CHEBI:17895`, label `L-tyrosine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:17895`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `60-18-4`, molecular formula `C9H11NO3`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-threonine.yaml data/ingredients/mapped/L-tryptophan.yaml data/ingredients/mapped/L-tyrosine.yaml data/ingredients/mapped/L-tyrosine_2-naphthylamide.yaml data/ingredients/mapped/L-tyrosine_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17895` as active `L-tyrosine` and lists CAS
  `60-18-4`.
- PubChem resolves CAS RN `60-18-4` to CID `6057` with formula `C9H11NO3` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17895`; its
  `other` field contains reviewed L-tyrosine synonyms, bare `TYROSINE`, and
  `CAS:60-18-4`.
- Major: exact OLS search for `TYROSINE` returns generic CHEBI:18186 before
  L-specific CHEBI:17895, and `data/ingredients/mapped/DL-Tyrosine.yaml`
  already uses CHEBI:18186 as the closest available stereo-unspecified tyrosine
  parent. Exporting the bare token from this L-specific record crosses that
  boundary in the final SSSOM row.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact L-tyrosine was supplied as an amino acid
  source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the DL-tyrosine sibling, and component
  references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  aggregate copy, and most final synonyms are present and consistent.
- The provisional role and generic `TYROSINE` synonym need curation before the
  record can be treated as complete.

## Recommended Edits

- Major: remove `TYROSINE` from the `EXACT_SYNONYM` list on
  `data/ingredients/mapped/L-tyrosine.yaml`.
- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` with inspected
  source evidence for exact L-tyrosine use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
