# `data/ingredients/mapped/L-lysine.yaml`

## Verdict

Needs curation. The L-lysine identity, CAS RN, PubChem structure, occurrence
count, reviewed synonyms, and final SSSOM row pass, but the amino-acid-source
role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-lysine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18019` with
  `ontology_mapping.ontology_id: CHEBI:18019`, label `L-lysine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-87-1`, molecular formula `C6H14N2O2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:18019` as active `L-lysine` and lists CAS
  `56-87-1`.
- PubChem resolves CAS RN `56-87-1` to CID `5962` with formula `C6H14N2O2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18019`; its
  `other` field contains reviewed exact synonyms plus `CAS:56-87-1`, with no
  lysine hydrochloride sibling synonyms.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that this exact ingredient was supplied as an amino
  acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the separate L-lysine hydrochloride sibling,
  and component references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-lysine.yaml` with inspected source evidence for
  exact L-lysine use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
