# `data/ingredients/mapped/Uridine_5-monophosphate_Disodium_Salt.yaml`

## Verdict

Pass. The CAS fallback identity, PubChem-resolved disodium 5'-UMP structure,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Uridine_5-monophosphate_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:3387-36-8` with matching
  `ontology_mapping.ontology_id`, label
  `Uridine 5-monophosphate disodium salt`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `3387-36-8`.
- Chemical fields: formula `C9H11N2Na2O9P`, PubChem CID `169020`, and a
  disodium uridine 5'-monophosphate SMILES/InChI pair.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uridine_5-monophosphate_Disodium_Salt` through `V-8_Juice`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this CAS fallback row has no OBO adapter for that focused check.

## Evidence

- PubChem name lookup for CAS `3387-36-8` resolves to CID `169020`; its synonym
  set includes `3387-36-8` and disodium uridine 5'-monophosphate labels.
- PubChem CID `169020` has the same formula, connectivity SMILES, and InChI
  recorded in `chemical_properties`.
- Fresh OLS4 CHEBI search for CAS `3387-36-8` returned no CHEBI documents, so
  the CAS fallback remains the best available exact registry identity.
- The final SSSOM row correctly maps
  `MIM:Uridine_5-monophosphate_Disodium_Salt skos:exactMatch cas:3387-36-8`
  with no broad parent synonyms in `other`.

## Issues

None.

## Completeness

- The CAS fallback identity, PubChem structure, aggregate copy, and final SSSOM
  row agree.

## Recommended Edits

None.
