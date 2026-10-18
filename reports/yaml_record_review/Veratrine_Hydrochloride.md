# `data/ingredients/mapped/Veratrine_Hydrochloride.yaml`

## Verdict

Pass. The CAS fallback identity, PubChem-resolved hydrochloride structure,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Veratrine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:17666-25-0` with matching
  `ontology_mapping.ontology_id`, label `Veratrine hydrochloride`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `17666-25-0`.
- Chemical fields: formula `C32H50ClNO9`, PubChem CID `16220094`, and
  PubChem-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Veratrine_Hydrochloride` through `Viomycin`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this CAS fallback row has no OBO adapter for that focused check.

## Evidence

- PubChem CID `16220094` has CAS synonym `17666-25-0`,
  `Veratrine hydrochloride` labels, formula `C32H50ClNO9`, and the same
  connectivity SMILES/InChI as the YAML.
- Fresh OLS4 CHEBI search for CAS `17666-25-0` returned no CHEBI documents, so
  the CAS fallback remains the best available exact registry identity.
- The final SSSOM row correctly maps
  `MIM:Veratrine_Hydrochloride skos:exactMatch cas:17666-25-0` with no
  unsupported labels in `other`.

## Issues

None.

## Completeness

- The CAS fallback identity, PubChem structure, aggregate copy, and final SSSOM
  row agree.

## Recommended Edits

None.
