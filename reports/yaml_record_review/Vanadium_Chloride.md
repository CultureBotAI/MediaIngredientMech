# `data/ingredients/mapped/Vanadium_Chloride.yaml`

## Verdict

Needs curation. The CAS fallback identity, PubChem structure, aggregate row,
and final SSSOM row pass, but `TRACE_ELEMENT` is still supported only by a
provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Vanadium_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:7718-98-1` with matching
  `ontology_mapping.ontology_id`, label `vanadium chloride`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7718-98-1`.
- Chemical fields: formula `Cl3V`, PubChem CID `62647`, and a vanadium
  trichloride SMILES/InChI pair.
- Occurrences: 26 CultureMech recipe occurrences.
- Role: `TRACE_ELEMENT` with provisional in-session LLM evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Valerate` through `Vancomycin`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this CAS fallback row has no OBO adapter for that focused check.

## Evidence

- PubChem name lookup for CAS `7718-98-1` resolves to CID `62647`; that CID has
  formula `Cl3V` and the same SMILES/InChI recorded in `chemical_properties`.
- Fresh OLS4 CHEBI search for CAS `7718-98-1` returned no CHEBI documents, so
  the CAS fallback remains the best available exact registry identity.
- The final SSSOM row correctly maps
  `MIM:Vanadium_Chloride skos:exactMatch cas:7718-98-1` with no broad synonym
  strings in `other`.

## Issues

- Major: `nutritional_roles.TRACE_ELEMENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose text is explicitly
  `Assigned by in-session Claude reasoning (no external API)` and whose curator
  note calls the assignment provisional.

## Completeness

- The CAS fallback identity, PubChem structure, aggregate copy, occurrence
  count, and final SSSOM row agree.
- The vanadium trace-element role still needs database or curated recipe
  evidence before it is reviewable as a maintained facet.

## Recommended Edits

- Replace or remove `data/ingredients/mapped/Vanadium_Chloride.yaml`
  `nutritional_roles.TRACE_ELEMENT`; keep it only if a maintained source
  supports vanadium chloride as a trace element in the specific media records
  that use it, then rerun strict validation and SSSOM invariant checks.
