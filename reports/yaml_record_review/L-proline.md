# `data/ingredients/mapped/L-proline.yaml`

## Verdict

Needs curation. The L-proline identity, CAS RN, PubChem structure, occurrence
count, reviewed synonyms, and final SSSOM row pass, but the amino-acid-source
role is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/L-proline.yaml`.
- Identifier and grounding: `identifier: CHEBI:17203` with
  `ontology_mapping.ontology_id: CHEBI:17203`, label `L-proline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `147-85-3`, molecular formula `C5H9NO2`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline-4-nitroanilide.yaml data/ingredients/mapped/L-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-ornithine.yaml data/ingredients/mapped/L-ornithine_Monohydrochloride.yaml data/ingredients/mapped/L-phenylalanine.yaml data/ingredients/mapped/L-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records. Engine A term validation was
  skipped for the non-OBO `kgmicrobe.compound` registry record.

## Evidence

- EBI OLS4 resolves `CHEBI:17203` as active `L-proline` and lists CAS
  `147-85-3`.
- PubChem resolves CAS RN `147-85-3` to CID `145742` with formula `C5H9NO2`
  and the same InChI as the YAML record.
- Exact OLS searches for `PROLINE` and `2-Pyrrolidinecarboxylic acid` resolve
  to CHEBI:17203, and the repository keeps generic `Proline` separately on
  CHEBI:26271, so the inspected final synonyms do not cross that boundary.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17203`; its
  `other` field contains reviewed exact synonyms plus `CAS:147-85-3`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. The amino-acid ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that this exact ingredient was supplied as an amino
  acid source.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the generic proline sibling, and component
  references from multicomponent amino-acid records.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  synonyms, aggregate copy, and final SSSOM row are present and consistent.
- The provisional amino-acid role needs curation before it can be treated as a
  supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-proline.yaml` with inspected source evidence for
  exact L-proline use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
